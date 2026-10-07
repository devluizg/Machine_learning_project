import { useEffect, useRef } from 'react';

type Dot = { x: number; y: number; depth: number; size: number; phase: number; family: number };

const centers: [number, number][] = [[0.08, 0.18], [0.34, 0.82], [0.52, 0.14], [0.79, 0.26], [0.91, 0.81]];

function makeDots(): Dot[] {
  // Sequência fixa: a composição não muda a cada visita nem depende de dados do estudante.
  let seed = 2077;
  const random = () => { seed = (seed * 1664525 + 1013904223) >>> 0; return seed / 4294967296; };
  return Array.from({ length: 85 }, (_, index) => {
    const family = index % centers.length;
    const [cx, cy] = centers[family]!;
    return {
      x: Math.max(0.02, Math.min(0.98, cx + (random() - 0.5) * 0.28)),
      y: Math.max(0.04, Math.min(0.96, cy + (random() - 0.5) * 0.35)),
      depth: 0.18 + random() * 0.82,
      size: 1.1 + random() * 1.8,
      phase: random() * Math.PI * 2,
      family,
    };
  });
}

const dots = makeDots();
const links = dots.flatMap((dot, index) => dots.slice(index + 1).map((other, offset) => ({ a: index, b: index + offset + 1, distance: Math.hypot(dot.x - other.x, dot.y - other.y), sameFamily: dot.family === other.family }))).filter((link) => link.sameFamily && link.distance < 0.12).slice(0, 110);

export function AmbientParticles({ paused, viewport = false }: { paused: boolean; viewport?: boolean }) {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const parent = canvas?.parentElement;
    const ctx = canvas?.getContext('2d', { alpha: true });
    if (!canvas || !parent || !ctx) return;

    let width = 1;
    let height = 1;
    let frame = 0;
    let visible = true;
    const coarsePointer = window.matchMedia('(pointer: coarse)').matches;
    let reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches || coarsePointer;
    let pointerActive = false;
    let pointerX = 0;
    let pointerY = 0;
    let previousPointerX = 0;
    let previousPointerY = 0;
    let previousPointerTime = 0;
    let pointerVelocityX = 0;
    let pointerVelocityY = 0;
    let easedVelocityX = 0;
    let easedVelocityY = 0;
    let pointerEnergy = 0;
    let easedX = 0;
    let easedY = 0;
    let previousFrameTime = 0;
    const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');

    function resize() {
      const rect = parent!.getBoundingClientRect();
      width = Math.max(1, viewport ? window.innerWidth : rect.width);
      height = Math.max(1, viewport ? window.innerHeight : rect.height);
      if (easedX === 0 && easedY === 0) { easedX = width * 0.62; easedY = height * 0.48; }
      const density = Math.min(2, window.devicePixelRatio || 1);
      canvas!.width = Math.round(width * density);
      canvas!.height = Math.round(height * density);
      ctx!.setTransform(density, 0, 0, density, 0, 0);
      if (paused || reduced) draw(0);
    }

    function onPointerMove(event: PointerEvent) {
      if (event.pointerType === 'touch' || paused || reduced) return;
      const rect = parent!.getBoundingClientRect();
      pointerX = viewport ? event.clientX : event.clientX - rect.left;
      pointerY = viewport ? event.clientY : event.clientY - rect.top;
      const now = performance.now();
      if (pointerActive) {
        const elapsed = Math.max(16, now - previousPointerTime);
        const rawX = (pointerX - previousPointerX) / elapsed;
        const rawY = (pointerY - previousPointerY) / elapsed;
        const magnitude = Math.hypot(rawX, rawY);
        const capped = magnitude > 0.48 ? 0.48 / magnitude : 1;
        pointerVelocityX = pointerVelocityX * 0.8 + rawX * capped * 0.2;
        pointerVelocityY = pointerVelocityY * 0.8 + rawY * capped * 0.2;
      }
      previousPointerX = pointerX;
      previousPointerY = pointerY;
      previousPointerTime = now;
      pointerEnergy = 1;
      pointerActive = true;
    }

    function onPointerLeave() { pointerActive = false; }
    function onMotionChange(event: MediaQueryListEvent) { reduced = event.matches || coarsePointer; if (reduced) draw(0); else start(); }

    function draw(time: number) {
      ctx!.clearRect(0, 0, width, height);
      const moving = !paused && !reduced;
      const elapsed = previousFrameTime ? Math.min(40, Math.max(0, time - previousFrameTime)) : 16;
      previousFrameTime = time;
      pointerEnergy *= Math.pow(0.86, elapsed / 16);
      // Amortecimento por quadro: mudanças bruscas no cursor não deslocam as
      // constelações instantaneamente, evitando o aspecto de tremida.
      const velocitySmoothing = 1 - Math.exp(-elapsed / 150);
      const targetVelocityX = pointerActive ? pointerVelocityX * pointerEnergy : 0;
      const targetVelocityY = pointerActive ? pointerVelocityY * pointerEnergy : 0;
      easedVelocityX += (targetVelocityX - easedVelocityX) * velocitySmoothing;
      easedVelocityY += (targetVelocityY - easedVelocityY) * velocitySmoothing;
      const restingX = width * 0.62;
      const restingY = height * 0.48;
      easedX += ((pointerActive ? pointerX : restingX) - easedX) * (moving ? 0.065 : 1);
      easedY += ((pointerActive ? pointerY : restingY) - easedY) * (moving ? 0.065 : 1);

      const positions = dots.map((dot) => {
        const depthScale = 0.82 + dot.depth * 0.28;
        // A deriva precisa ser perceptível sem competir com a leitura: cada
        // constelação percorre uma órbita ampla e lenta, em fases diferentes.
        const driftX = moving ? Math.sin(time * 0.00062 + dot.phase) * 17 * dot.depth : 0;
        const driftY = moving ? Math.cos(time * 0.00051 + dot.phase * 1.13) * 19 * dot.depth : 0;
        const parallaxX = moving ? (easedX - width / 2) * dot.depth * 0.045 : 0;
        const parallaxY = moving ? (easedY - height / 2) * dot.depth * 0.04 : 0;
        const baseX = width / 2 + (dot.x - 0.5) * width * depthScale + driftX + parallaxX;
        const baseY = height / 2 + (dot.y - 0.5) * height * depthScale + driftY + parallaxY;
        const distance = Math.hypot(easedX - baseX, easedY - baseY);
        const proximity = pointerActive && moving ? Math.exp(-distance * distance / 48000) : 0;
        const attraction = proximity * (0.03 + dot.depth * 0.06);
        // A perturbação acompanha a direção do cursor: perto do mouse, os pontos
        // ganham velocidade no mesmo sentido e voltam suavemente à deriva lenta.
        const directionalX = easedVelocityX * 28 * proximity * (0.72 + dot.depth * 0.35);
        const directionalY = easedVelocityY * 28 * proximity * (0.72 + dot.depth * 0.35);
        return { x: baseX + (easedX - baseX) * attraction + directionalX, y: baseY + (easedY - baseY) * attraction + directionalY, distance, size: dot.size * (0.7 + dot.depth * 0.6), depth: dot.depth };
      });

      for (const link of links) {
        const a = positions[link.a]!;
        const b = positions[link.b]!;
        ctx!.beginPath();
        ctx!.moveTo(a.x, a.y);
        ctx!.lineTo(b.x, b.y);
        ctx!.strokeStyle = `rgba(154, 204, 205, ${0.035 + Math.min(a.depth, b.depth) * 0.085})`;
        ctx!.lineWidth = 1;
        ctx!.stroke();
      }

      positions.forEach((position, index) => {
        const near = pointerActive && moving ? Math.max(0, 1 - position.distance / 190) : 0;
        const accent = index % 11 === 0;
        ctx!.beginPath();
        ctx!.arc(position.x, position.y, position.size + near * 1.8, 0, Math.PI * 2);
        ctx!.fillStyle = accent ? `rgba(255, 155, 111, ${0.3 + position.depth * 0.42 + near * 0.18})` : `rgba(195, 226, 219, ${0.16 + position.depth * 0.45 + near * 0.25})`;
        ctx!.fill();
      });

      if (pointerActive && moving) {
        const nearest = positions.map((position, index) => ({ index, distance: position.distance })).sort((a, b) => a.distance - b.distance).slice(0, 5);
        nearest.forEach(({ index, distance }) => {
          if (distance > 175) return;
          const point = positions[index]!;
          ctx!.beginPath();
          ctx!.moveTo(easedX, easedY);
          ctx!.lineTo(point.x, point.y);
          ctx!.strokeStyle = `rgba(255, 164, 124, ${0.29 * (1 - distance / 175)})`;
          ctx!.stroke();
        });
        ctx!.beginPath();
        ctx!.arc(easedX, easedY, 6, 0, Math.PI * 2);
        ctx!.strokeStyle = 'rgba(255, 170, 132, 0.6)';
        ctx!.lineWidth = 1.5;
        ctx!.stroke();
      }
    }

    function tick(time: number) {
      if (!visible || paused || reduced || document.hidden) { frame = 0; return; }
      draw(time);
      frame = window.requestAnimationFrame(tick);
    }

    function start() {
      if (!frame && visible && !paused && !reduced && !document.hidden) frame = window.requestAnimationFrame(tick);
    }

    const resizeObserver = new ResizeObserver(resize);
    const intersectionObserver = new IntersectionObserver(([entry]) => { visible = entry?.isIntersecting ?? false; if (visible) start(); else if (frame) { window.cancelAnimationFrame(frame); frame = 0; } });
    const onVisibility = () => { if (document.hidden && frame) { window.cancelAnimationFrame(frame); frame = 0; } else start(); };

    resizeObserver.observe(parent);
    intersectionObserver.observe(parent);
    if (viewport) window.addEventListener('resize', resize);
    parent.addEventListener('pointermove', onPointerMove);
    parent.addEventListener('pointerleave', onPointerLeave);
    motionQuery.addEventListener('change', onMotionChange);
    document.addEventListener('visibilitychange', onVisibility);
    resize();
    start();

    return () => {
      if (frame) window.cancelAnimationFrame(frame);
      resizeObserver.disconnect();
      intersectionObserver.disconnect();
      if (viewport) window.removeEventListener('resize', resize);
      parent.removeEventListener('pointermove', onPointerMove);
      parent.removeEventListener('pointerleave', onPointerLeave);
      motionQuery.removeEventListener('change', onMotionChange);
      document.removeEventListener('visibilitychange', onVisibility);
    };
  }, [paused, viewport]);

  return <canvas ref={canvasRef} className="ambient-particles" aria-hidden="true" />;
}
