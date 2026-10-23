import { useEffect, useRef } from 'react';

// Shaders GLSL para renderização estelar acelerada por WebGL na GPU
const VERTEX_SHADER_SOURCE = `
  attribute vec3 aPosition;
  attribute float aPhase;
  attribute float aSize;
  attribute vec3 aColor;

  uniform mat4 uProjection;
  uniform mat4 uView;
  uniform mat4 uModel;
  uniform float uTime;
  uniform vec3 uMouse;
  uniform float uScroll;
  uniform float uPixelRatio;

  varying vec3 vColor;
  varying float vAlpha;

  void main() {
    vec3 pos = aPosition;

    // Deriva lenta e orgânica celestial
    float t = uTime * 0.35 + aPhase * 6.28318;
    pos.x += sin(t * 0.7) * 0.12;
    pos.y += cos(t * 0.8) * 0.12;
    pos.z += sin(t * 0.5) * 0.09;

    // Dispersão suave conforme o scroll da página (mergulho no cosmos)
    pos.z -= uScroll * 1.8;
    pos.x *= 1.0 + uScroll * 0.22;
    pos.y *= 1.0 + uScroll * 0.22;

    // Transformação para coordenadas do modelo
    vec4 worldPos = uModel * vec4(pos, 1.0);

    // Interação física suave com o mouse (repulsão cósmica)
    vec3 mouseDiff = worldPos.xyz - uMouse;
    float mouseDist = length(mouseDiff);
    float repulsionRadius = 2.4;
    if (mouseDist < repulsionRadius) {
      float force = smoothstep(repulsionRadius, 0.0, mouseDist) * 0.75;
      worldPos.xyz += normalize(mouseDiff + vec3(0.0001)) * force;
    }

    vec4 viewPos = uView * worldPos;
    gl_Position = uProjection * viewPos;

    // Tamanho do ponto com atenuação de perspectiva realista
    float depthFactor = clamp(8.0 / max(0.5, -viewPos.z), 0.4, 3.2);
    gl_PointSize = aSize * uPixelRatio * depthFactor;

    // Cintilação suave e atenuação de profundidade
    float twinkle = 0.75 + 0.25 * sin(uTime * 1.4 + aPhase * 12.0);
    float depthAlpha = smoothstep(-18.0, -3.0, viewPos.z);
    vColor = aColor;
    vAlpha = twinkle * depthAlpha;
  }
`;

const FRAGMENT_SHADER_SOURCE = `
  precision mediump float;
  varying vec3 vColor;
  varying float vAlpha;

  void main() {
    // Coordenada do centro do ponto: -0.5 a +0.5
    vec2 coord = gl_PointCoord - vec2(0.5);
    float dist = length(coord);
    if (dist > 0.5) {
      discard;
    }

    // Núcleo estelar brilhante com halo gradiente suave
    float core = smoothstep(0.5, 0.08, dist);
    float halo = exp(-dist * 5.0);
    float alpha = (core * 0.65 + halo * 0.35) * vAlpha;

    gl_FragColor = vec4(vColor, alpha);
  }
`;

// Shaders para os anéis de órbitas astronômicas
const RING_VERT_SOURCE = `
  attribute vec3 aPosition;
  uniform mat4 uProjection;
  uniform mat4 uView;
  uniform mat4 uModel;
  void main() {
    gl_Position = uProjection * uView * uModel * vec4(aPosition, 1.0);
  }
`;

const RING_FRAG_SOURCE = `
  precision mediump float;
  uniform vec4 uRingColor;
  void main() {
    gl_FragColor = uRingColor;
  }
`;

function createShader(gl: WebGLRenderingContext, type: number, source: string): WebGLShader | null {
  const shader = gl.createShader(type);
  if (!shader) return null;
  gl.shaderSource(shader, source);
  gl.compileShader(shader);
  if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
    gl.deleteShader(shader);
    return null;
  }
  return shader;
}

function createProgram(
  gl: WebGLRenderingContext,
  vertexShader: WebGLShader,
  fragmentShader: WebGLShader
): WebGLProgram | null {
  const program = gl.createProgram();
  if (!program) return null;
  gl.attachShader(program, vertexShader);
  gl.attachShader(program, fragmentShader);
  gl.linkProgram(program);
  if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
    gl.deleteProgram(program);
    return null;
  }
  return program;
}

// Cria matriz de projeção em perspectiva 4x4
function mat4Perspective(out: Float32Array, fovy: number, aspect: number, near: number, far: number) {
  const f = 1.0 / Math.tan(fovy / 2);
  const nf = 1 / (near - far);
  out.fill(0);
  out[0] = f / aspect;
  out[5] = f;
  out[10] = (far + near) * nf;
  out[11] = -1;
  out[14] = 2 * far * near * nf;
}

// Cria matriz de translação 4x4
function mat4Translation(out: Float32Array, x: number, y: number, z: number) {
  out.fill(0);
  out[0] = 1;
  out[5] = 1;
  out[10] = 1;
  out[15] = 1;
  out[12] = x;
  out[13] = y;
  out[14] = z;
}

export function AmbientParticles({ paused = false }: { paused?: boolean; viewport?: boolean }) {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const gl = canvas.getContext('webgl', {
      alpha: true,
      antialias: true,
      depth: false,
      powerPreference: 'high-performance',
    });

    if (!gl) return;

    // Compilação dos shaders de partículas
    const vs = createShader(gl, gl.VERTEX_SHADER, VERTEX_SHADER_SOURCE);
    const fs = createShader(gl, gl.FRAGMENT_SHADER, FRAGMENT_SHADER_SOURCE);
    if (!vs || !fs) return;

    const program = createProgram(gl, vs, fs);
    if (!program) return;

    // Compilação dos shaders de anéis orbitais
    const ringVs = createShader(gl, gl.VERTEX_SHADER, RING_VERT_SOURCE);
    const ringFs = createShader(gl, gl.FRAGMENT_SHADER, RING_FRAG_SOURCE);
    const ringProgram = ringVs && ringFs ? createProgram(gl, ringVs, ringFs) : null;

    // Localização de atributos e uniformes do programa de partículas
    const aPosition = gl.getAttribLocation(program, 'aPosition');
    const aPhase = gl.getAttribLocation(program, 'aPhase');
    const aSize = gl.getAttribLocation(program, 'aSize');
    const aColor = gl.getAttribLocation(program, 'aColor');

    const uProjection = gl.getUniformLocation(program, 'uProjection');
    const uView = gl.getUniformLocation(program, 'uView');
    const uModel = gl.getUniformLocation(program, 'uModel');
    const uTime = gl.getUniformLocation(program, 'uTime');
    const uMouse = gl.getUniformLocation(program, 'uMouse');
    const uScroll = gl.getUniformLocation(program, 'uScroll');
    const uPixelRatio = gl.getUniformLocation(program, 'uPixelRatio');

    // Localização para anéis orbitais
    const ringPos = ringProgram ? gl.getAttribLocation(ringProgram, 'aPosition') : -1;
    const ringProj = ringProgram ? gl.getUniformLocation(ringProgram, 'uProjection') : null;
    const ringView = ringProgram ? gl.getUniformLocation(ringProgram, 'uView') : null;
    const ringModel = ringProgram ? gl.getUniformLocation(ringProgram, 'uModel') : null;
    const ringColor = ringProgram ? gl.getUniformLocation(ringProgram, 'uRingColor') : null;

    // Geração determinística do campo estelar de constelações (+50%: 5.700 partículas no desktop e 3.300 no mobile)
    const PARTICLE_COUNT = window.innerWidth < 800 ? 3300 : 5700;
    const positions = new Float32Array(PARTICLE_COUNT * 3);
    const phases = new Float32Array(PARTICLE_COUNT);
    const sizes = new Float32Array(PARTICLE_COUNT);
    const colors = new Float32Array(PARTICLE_COUNT * 3);

    let seed = 42;
    const pseudoRandom = () => {
      seed = (seed * 1664525 + 1013904223) >>> 0;
      return seed / 4294967296;
    };

    // Paleta de constelação noturna:
    // - Azul gelo / ciano celestial
    // - Branco pérola estelar
    // - Âmbar dourado sutil (representando pontos de dados / estrelas quentes)
    const STAR_PALETTES = [
      [0.65, 0.84, 0.98], // Azul celestial
      [0.85, 0.93, 1.0],  // Branco estelar
      [0.45, 0.72, 0.95], // Ciano profundo
      [0.98, 0.76, 0.52], // Âmbar sutil de dados ML
      [0.55, 0.88, 0.92], // Turquesa estelar
    ];

    for (let i = 0; i < PARTICLE_COUNT; i++) {
      // Distribuição elipsoidal ampla com concentração na faixa da visão
      const radius = 2.0 + Math.pow(pseudoRandom(), 0.6) * 11.5;
      const theta = pseudoRandom() * Math.PI * 2;
      const phi = Math.acos(2 * pseudoRandom() - 1);

      positions[i * 3] = radius * Math.sin(phi) * Math.cos(theta) * 1.55;
      positions[i * 3 + 1] = radius * Math.cos(phi) * 0.95;
      positions[i * 3 + 2] = (radius * Math.sin(phi) * Math.sin(theta) * 0.8) - 1.5;

      phases[i] = pseudoRandom();
      sizes[i] = 1.4 + Math.pow(pseudoRandom(), 2) * 3.4;

      const paletteIndex = Math.floor(pseudoRandom() * STAR_PALETTES.length);
      const color = STAR_PALETTES[paletteIndex]!;
      colors[i * 3] = color[0]!;
      colors[i * 3 + 1] = color[1]!;
      colors[i * 3 + 2] = color[2]!;
    }

    // Buffers de GPU
    const posBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, posBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, positions, gl.STATIC_DRAW);

    const phaseBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, phaseBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, phases, gl.STATIC_DRAW);

    const sizeBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, sizeBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, sizes, gl.STATIC_DRAW);

    const colorBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, colors, gl.STATIC_DRAW);

    // Buffers para os anéis de órbitas astronômicas
    const RING_SEGMENTS = 140;
    const ringVertices = new Float32Array((RING_SEGMENTS + 1) * 3);
    const ringRadius = 5.8;
    for (let i = 0; i <= RING_SEGMENTS; i++) {
      const angle = (i / RING_SEGMENTS) * Math.PI * 2;
      ringVertices[i * 3] = Math.cos(angle) * ringRadius;
      ringVertices[i * 3 + 1] = Math.sin(angle) * (ringRadius * 0.88);
      ringVertices[i * 3 + 2] = 0;
    }
    const ringBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, ringBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, ringVertices, gl.STATIC_DRAW);

    // Estado da animação e interatividade
    let animationFrameId = 0;
    let isVisible = true;
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const isPaused = paused || prefersReducedMotion;

    let targetMouseX = 0;
    let targetMouseY = 0;
    let currentMouseX = 0;
    let currentMouseY = 0;
    let mouseWorldX = 999.0;
    let mouseWorldY = 999.0;
    let currentScroll = 0;
    let targetScroll = 0;

    const projMatrix = new Float32Array(16);
    const viewMatrix = new Float32Array(16);
    const modelMatrix = new Float32Array(16);

    mat4Translation(viewMatrix, 0, 0, -8.5);

    function resize() {
      if (!canvas || !gl) return;
      const width = window.innerWidth;
      const height = window.innerHeight;
      const dpr = Math.min(2, window.devicePixelRatio || 1);

      if (canvas.width !== Math.round(width * dpr) || canvas.height !== Math.round(height * dpr)) {
        canvas.width = Math.round(width * dpr);
        canvas.height = Math.round(height * dpr);
        gl.viewport(0, 0, canvas.width, canvas.height);
      }

      mat4Perspective(projMatrix, (48 * Math.PI) / 180, width / height, 0.1, 100.0);
    }

    function onPointerMove(e: PointerEvent) {
      const nx = (e.clientX / window.innerWidth) * 2 - 1;
      const ny = -(e.clientY / window.innerHeight) * 2 + 1;
      targetMouseX = nx;
      targetMouseY = ny;

      // Converte para coordenadas mundiais estimadas no plano Z central
      mouseWorldX = nx * 5.2;
      mouseWorldY = ny * 3.4;
    }

    function onPointerLeave() {
      targetMouseX = 0;
      targetMouseY = 0;
      mouseWorldX = 999.0;
      mouseWorldY = 999.0;
    }

    function onScroll() {
      const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      targetScroll = Math.min(1.5, window.scrollY / maxScroll);
    }

    const startTime = performance.now();

    function render(currentTime: number) {
      if (!gl) return;

      const elapsed = (currentTime - startTime) / 1000;

      // Interpolação inercial suave do mouse e do scroll (lerp)
      currentMouseX += (targetMouseX - currentMouseX) * 0.045;
      currentMouseY += (targetMouseY - currentMouseY) * 0.045;
      currentScroll += (targetScroll - currentScroll) * 0.06;

      gl.clearColor(0, 0, 0, 0);
      gl.clear(gl.COLOR_BUFFER_BIT);

      gl.enable(gl.BLEND);
      gl.blendFunc(gl.SRC_ALPHA, gl.ONE); // Blend aditivo para brilho estelar translúcido

      // Matriz de modelo com rotação cósmica lenta + inclinação pelo mouse
      const rotY = elapsed * 0.05 + currentMouseX * 0.28;
      const rotX = -currentMouseY * 0.18 + 0.12;
      const cy = Math.cos(rotY), sy = Math.sin(rotY);
      const cx = Math.cos(rotX), sx = Math.sin(rotX);

      modelMatrix.fill(0);
      modelMatrix[0] = cy;
      modelMatrix[1] = sy * sx;
      modelMatrix[2] = -sy * cx;
      modelMatrix[4] = 0;
      modelMatrix[5] = cx;
      modelMatrix[6] = sx;
      modelMatrix[8] = sy;
      modelMatrix[9] = -cy * sx;
      modelMatrix[10] = cy * cx;
      modelMatrix[15] = 1;

      // 1. Renderização dos pontos da constelação
      gl.useProgram(program);

      gl.uniformMatrix4fv(uProjection, false, projMatrix);
      gl.uniformMatrix4fv(uView, false, viewMatrix);
      gl.uniformMatrix4fv(uModel, false, modelMatrix);
      gl.uniform1f(uTime, elapsed);
      gl.uniform3f(uMouse, mouseWorldX, mouseWorldY, 0.0);
      gl.uniform1f(uScroll, currentScroll);
      gl.uniform1f(uPixelRatio, Math.min(2, window.devicePixelRatio || 1));

      gl.enableVertexAttribArray(aPosition);
      gl.bindBuffer(gl.ARRAY_BUFFER, posBuffer);
      gl.vertexAttribPointer(aPosition, 3, gl.FLOAT, false, 0, 0);

      gl.enableVertexAttribArray(aPhase);
      gl.bindBuffer(gl.ARRAY_BUFFER, phaseBuffer);
      gl.vertexAttribPointer(aPhase, 1, gl.FLOAT, false, 0, 0);

      gl.enableVertexAttribArray(aSize);
      gl.bindBuffer(gl.ARRAY_BUFFER, sizeBuffer);
      gl.vertexAttribPointer(aSize, 1, gl.FLOAT, false, 0, 0);

      gl.enableVertexAttribArray(aColor);
      gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
      gl.vertexAttribPointer(aColor, 3, gl.FLOAT, false, 0, 0);

      gl.drawArrays(gl.POINTS, 0, PARTICLE_COUNT);

      // 2. Renderização de anéis de órbitas astronômicas sutis
      if (ringProgram && ringPos !== -1) {
        gl.useProgram(ringProgram);
        gl.uniformMatrix4fv(ringProj, false, projMatrix);
        gl.uniformMatrix4fv(ringView, false, viewMatrix);
        gl.uniformMatrix4fv(ringModel, false, modelMatrix);
        gl.uniform4f(ringColor, 0.45, 0.72, 0.95, 0.08); // Anel tênue celeste

        gl.enableVertexAttribArray(ringPos);
        gl.bindBuffer(gl.ARRAY_BUFFER, ringBuffer);
        gl.vertexAttribPointer(ringPos, 3, gl.FLOAT, false, 0, 0);

        gl.drawArrays(gl.LINE_STRIP, 0, RING_SEGMENTS + 1);
      }

      if (!isPaused && isVisible) {
        animationFrameId = requestAnimationFrame(render);
      }
    }

    function startLoop() {
      if (!animationFrameId && !isPaused && isVisible && !document.hidden) {
        animationFrameId = requestAnimationFrame(render);
      }
    }

    function stopLoop() {
      if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
        animationFrameId = 0;
      }
    }

    const onVisibilityChange = () => {
      if (document.hidden) {
        stopLoop();
      } else {
        startLoop();
      }
    };

    const intersectionObserver = new IntersectionObserver(([entry]) => {
      isVisible = entry?.isIntersecting ?? false;
      if (isVisible) {
        startLoop();
      } else {
        stopLoop();
      }
    });

    intersectionObserver.observe(canvas);
    window.addEventListener('resize', resize);
    window.addEventListener('pointermove', onPointerMove, { passive: true });
    window.addEventListener('pointerleave', onPointerLeave);
    window.addEventListener('scroll', onScroll, { passive: true });
    document.addEventListener('visibilitychange', onVisibilityChange);

    resize();
    render(performance.now());
    if (!isPaused) {
      startLoop();
    }

    return () => {
      stopLoop();
      intersectionObserver.disconnect();
      window.removeEventListener('resize', resize);
      window.removeEventListener('pointermove', onPointerMove);
      window.removeEventListener('pointerleave', onPointerLeave);
      window.removeEventListener('scroll', onScroll);
      document.removeEventListener('visibilitychange', onVisibilityChange);

      // Liberação de memória WebGL na desmontagem
      gl.deleteBuffer(posBuffer);
      gl.deleteBuffer(phaseBuffer);
      gl.deleteBuffer(sizeBuffer);
      gl.deleteBuffer(colorBuffer);
      gl.deleteBuffer(ringBuffer);
      gl.deleteProgram(program);
      if (ringProgram) gl.deleteProgram(ringProgram);
    };
  }, [paused]);

  return (
    <canvas
      ref={canvasRef}
      className="ambient-particles-canvas"
      aria-hidden="true"
    />
  );
}
