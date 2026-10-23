import { useEffect, useRef, useState } from 'react';
import { ArrowUpRightIcon } from './ModelIcons';

export function HeroDemo() {
  // Estado do controle: 0 a 100%
  const [sliderPercent, setSliderPercent] = useState(25);
  const [isUserInteracting, setIsUserInteracting] = useState(false);
  const [isAutoPaused, setIsAutoPaused] = useState(false);
  const [cursorPos, setCursorPos] = useState({ x: 340, y: 160, clicking: false, visible: true });

  const interactionTimeoutRef = useRef<number | null>(null);
  const animFrameRef = useRef<number | null>(null);
  const sliderBarRef = useRef<SVGRectElement | null>(null);
  const svgRef = useRef<SVGSVGElement | null>(null);

  // Dados sintéticos de Regressão Linear (Modelo 01)
  const points = [
    { x: 70, y: 220 },
    { x: 125, y: 195 },
    { x: 180, y: 160 },
    { x: 235, y: 125 },
    { x: 290, y: 95 },
    { x: 345, y: 65 },
  ];

  // Geometria da barra de controle no SVG
  const trackX1 = 60;
  const trackX2 = 340;
  const trackWidth = trackX2 - trackX1; // 280px
  const trackY = 285;

  // Cálculo da reta conforme o slider (0 a 100%)
  // Inclinação ideal ocorre em torno de 65% (slope ~ 0.65)
  const slope = 0.2 + (sliderPercent / 100) * 0.9;
  // A reta passa pelo ponto central (210, 140): y - 140 = -slope * (x - 210)
  const lineYAt = (x: number) => 143 - slope * (x - 208);
  const lineXStart = 45;
  const lineYStart = lineYAt(lineXStart);
  const lineXEnd = 365;
  const lineYEnd = lineYAt(lineXEnd);

  // Cálculo didático do erro residual médio (MSE ilustrativo)
  const totalError = Math.round(
    points.reduce((acc, pt) => acc + Math.pow(pt.y - lineYAt(pt.x), 2), 0) / points.length
  );
  const isOptimal = Math.abs(sliderPercent - 65) <= 4;

  // Animação cíclica do mouse virtual e do ajuste da reta
  useEffect(() => {
    if (isUserInteracting || isAutoPaused) return;

    const startTime = performance.now();
    const CYCLE_DURATION = 8400; // 8.4 segundos por ciclo em loop

    function animate(time: number) {
      const elapsed = (time - startTime) % CYCLE_DURATION;
      const t = elapsed / CYCLE_DURATION;

      let targetPercent = 25;
      let mouseX = 350;
      let mouseY = 180;
      let clicking = false;
      let visible = true;

      if (t < 0.14) {
        // Fase 1 (0 a 1.2s): Cursor se move em direção ao botão do controle
        const p = t / 0.14;
        const ease = p * p * (3 - 2 * p);
        targetPercent = 25;
        const thumbX = trackX1 + 0.25 * trackWidth;
        mouseX = 340 + (thumbX - 340) * ease;
        mouseY = 160 + (trackY - 160) * ease;
        clicking = false;
        visible = true;
      } else if (t < 0.2) {
        // Fase 2 (1.2s a 1.7s): Cursor atinge o botão e clica (press)
        targetPercent = 25;
        mouseX = trackX1 + 0.25 * trackWidth;
        mouseY = trackY;
        clicking = true;
        visible = true;
      } else if (t < 0.48) {
        // Fase 3 (1.7s a 4.0s): Cursor arrasta o controle para a direita até o ponto ótimo (65%)
        const p = (t - 0.2) / 0.28;
        const ease = 0.5 - 0.5 * Math.cos(p * Math.PI);
        targetPercent = 25 + ease * 40; // vai de 25 a 65%
        mouseX = trackX1 + (targetPercent / 100) * trackWidth;
        mouseY = trackY;
        clicking = true;
        visible = true;
      } else if (t < 0.6) {
        // Fase 4 (4.0s a 5.0s): Passa um pouco (vai até 88%) para mostrar o erro voltando a subir
        const p = (t - 0.48) / 0.12;
        const ease = 0.5 - 0.5 * Math.cos(p * Math.PI);
        targetPercent = 65 + ease * 23; // vai de 65% até 88%
        mouseX = trackX1 + (targetPercent / 100) * trackWidth;
        mouseY = trackY;
        clicking = true;
        visible = true;
      } else if (t < 0.74) {
        // Fase 5 (5.0s a 6.2s): Retorna com precisão ao ponto ideal (65%)
        const p = (t - 0.6) / 0.14;
        const ease = 0.5 - 0.5 * Math.cos(p * Math.PI);
        targetPercent = 88 - ease * 23; // volta de 88% para 65%
        mouseX = trackX1 + (targetPercent / 100) * trackWidth;
        mouseY = trackY;
        clicking = true;
        visible = true;
      } else if (t < 0.85) {
        // Fase 6 (6.2s a 7.1s): Solta o clique e aponta para o gráfico ajustado
        targetPercent = 65;
        const p = (t - 0.74) / 0.11;
        const ease = p * p;
        mouseX = trackX1 + 0.65 * trackWidth + p * 30;
        mouseY = trackY - ease * 50;
        clicking = false;
        visible = true;
      } else {
        // Fase 7 (7.1s a 8.4s): Fade out suave do cursor e reset para reiniciar o loop
        const p = (t - 0.85) / 0.15;
        targetPercent = 65 - p * 40; // reseta de 65 para 25%
        mouseX = trackX1 + 0.65 * trackWidth + 30;
        mouseY = trackY - 50;
        clicking = false;
        visible = p < 0.5;
      }

      setSliderPercent(targetPercent);
      setCursorPos({ x: mouseX, y: mouseY, clicking, visible });
      animFrameRef.current = requestAnimationFrame(animate);
    }

    animFrameRef.current = requestAnimationFrame(animate);

    return () => {
      if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current);
    };
  }, [isUserInteracting, isAutoPaused]);

  const [isDragging, setIsDragging] = useState(false);

  function updateSliderFromClientX(clientX: number) {
    if (!svgRef.current) return;
    const rect = svgRef.current.getBoundingClientRect();
    const svgX = ((clientX - rect.left) / rect.width) * 400;
    const clampedX = Math.max(trackX1, Math.min(trackX2, svgX));
    const newPercent = ((clampedX - trackX1) / trackWidth) * 100;
    setSliderPercent(newPercent);
  }

  // Permite que o estudante interaja manualmente via teclado / input
  function handleManualSliderChange(e: React.ChangeEvent<HTMLInputElement>) {
    setIsUserInteracting(true);
    setSliderPercent(Number(e.target.value));

    if (interactionTimeoutRef.current) clearTimeout(interactionTimeoutRef.current);
    interactionTimeoutRef.current = window.setTimeout(() => {
      setIsUserInteracting(false);
    }, 4500);
  }

  // Permite arrastar ou clicar direto no SVG
  function handleSvgPointerDown(e: React.PointerEvent<SVGSVGElement>) {
    if (!svgRef.current) return;
    const rect = svgRef.current.getBoundingClientRect();
    const svgY = ((e.clientY - rect.top) / rect.height) * 320;

    // Se clicou na área do slider
    if (svgY >= trackY - 25 && svgY <= trackY + 25) {
      try {
        e.currentTarget.setPointerCapture(e.pointerId);
      } catch {
        // Ignora caso ambiente não suporte pointer capture
      }
      setIsDragging(true);
      setIsUserInteracting(true);
      updateSliderFromClientX(e.clientX);

      if (interactionTimeoutRef.current) clearTimeout(interactionTimeoutRef.current);
    }
  }

  function handleSvgPointerMove(e: React.PointerEvent<SVGSVGElement>) {
    if (!isDragging) return;
    updateSliderFromClientX(e.clientX);
  }

  function handleSvgPointerUp(e: React.PointerEvent<SVGSVGElement>) {
    if (isDragging) {
      try {
        e.currentTarget.releasePointerCapture(e.pointerId);
      } catch {
        // Ignora
      }
      setIsDragging(false);
      if (interactionTimeoutRef.current) clearTimeout(interactionTimeoutRef.current);
      interactionTimeoutRef.current = window.setTimeout(() => {
        setIsUserInteracting(false);
      }, 4500);
    }
  }

  const currentThumbPos = trackX1 + (sliderPercent / 100) * trackWidth;

  return (
    <div className="hero-interactive-card">
      <div className="hero-card-header">
        <div className="hero-card-badge">
          <span className="pulse-dot" />
          <span>DEMO ANIMADA EM LOOP · APRENDA EXPLORANDO</span>
        </div>
        <button
          type="button"
          className="demo-toggle-btn"
          onClick={() => {
            setIsAutoPaused(!isAutoPaused);
            setIsUserInteracting(false);
          }}
          title={isAutoPaused ? 'Retomar animação em loop' : 'Pausar loop'}
        >
          {isAutoPaused ? '▶ Retomar Loop' : '⏸ Pausar'}
        </button>
      </div>

      <div className="hero-card-canvas">
        {/* Placar de métricas fora da área de desenho do gráfico: impede sobreposição pela reta */}
        <div className="demo-metrics-strip">
          <div className="metric-chip">
            <span className="metric-label">INCLINAÇÃO:</span>
            <span className="metric-value">{slope.toFixed(2)}</span>
          </div>
          <div className={`metric-chip ${isOptimal ? 'is-optimal' : 'is-evaluating'}`}>
            <span className="metric-dot" />
            <span className="metric-value">
              {isOptimal ? '✓ AJUSTE ÓTIMO · ERRO MÍNIMO' : `ERRO QUADRÁTICO: ${totalError}`}
            </span>
          </div>
        </div>

        <svg
          ref={svgRef}
          viewBox="0 0 400 320"
          className="hero-demo-svg"
          onPointerDown={handleSvgPointerDown}
          onPointerMove={handleSvgPointerMove}
          onPointerUp={handleSvgPointerUp}
          onPointerCancel={handleSvgPointerUp}
        >
          <defs>
            {/* Máscara de corte para manter a reta dentro dos limites dos eixos cartesianos */}
            <clipPath id="plotAreaClip">
              <rect x="39" y="34" width="332" height="217" />
            </clipPath>

            {/* Gradiente da reta ajustada */}
            <linearGradient id="lineGlowGrad" x1="0%" y1="100%" x2="100%" y2="0%">
              <stop offset="0%" stopColor="#82c8ee" />
              <stop offset="100%" stopColor="#ff6b3d" />
            </linearGradient>

            {/* Sombra suave do cursor */}
            <filter id="cursorShadow" x="-30%" y="-30%" width="160%" height="160%">
              <feDropShadow dx="1.5" dy="2.5" stdDeviation="2.5" floodColor="#000" floodOpacity="0.6" />
            </filter>

            {/* Brilho da reta */}
            <filter id="neonLineGlow" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="3" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
          </defs>

          {/* Eixos cartesianos */}
          <line x1="40" y1="250" x2="370" y2="250" stroke="rgba(140, 180, 220, 0.22)" strokeWidth="1.5" />
          <line x1="40" y1="35" x2="40" y2="250" stroke="rgba(140, 180, 220, 0.22)" strokeWidth="1.5" />

          {/* Marcações de grade discretas */}
          {[90, 140, 190].map((y) => (
            <line
              key={y}
              x1="40"
              y1={y}
              x2="370"
              y2={y}
              stroke="rgba(140, 180, 220, 0.08)"
              strokeDasharray="2 3"
            />
          ))}

          {/* Linhas pontilhadas dos resíduos/erros (cada ponto até a reta) */}
          {points.map((pt, i) => {
            const predY = lineYAt(pt.x);
            const dist = Math.abs(pt.y - predY);
            const isSmall = dist < 12;
            return (
              <g key={i}>
                <line
                  x1={pt.x}
                  y1={pt.y}
                  x2={pt.x}
                  y2={predY}
                  stroke={isSmall ? '#82c8ee' : '#ff6b3d'}
                  strokeWidth={isSmall ? '1.5' : '2'}
                  strokeDasharray="3 3"
                  opacity={isSmall ? '0.6' : '0.9'}
                />
                {/* Marcador na interseção da reta */}
                <circle
                  cx={pt.x}
                  cy={predY}
                  r="2.5"
                  fill={isSmall ? '#82c8ee' : '#ff6b3d'}
                />
              </g>
            );
          })}

          {/* Reta com brilho de neon suave (cortada na área do gráfico) */}
          <line
            x1={lineXStart}
            y1={lineYStart}
            x2={lineXEnd}
            y2={lineYEnd}
            stroke="url(#lineGlowGrad)"
            strokeWidth="3.5"
            strokeLinecap="round"
            filter="url(#neonLineGlow)"
            clipPath="url(#plotAreaClip)"
          />

          {/* Pontos de dados (Exemplos de treinamento) */}
          {points.map((pt, i) => (
            <g key={i}>
              <circle cx={pt.x} cy={pt.y} r="8" fill="rgba(56, 189, 248, 0.18)" />
              <circle cx={pt.x} cy={pt.y} r="5" fill="#f8fafc" stroke="#041228" strokeWidth="2" />
            </g>
          ))}

          {/* Trilho e controle do Slider desenhados no próprio SVG para sincronia perfeita */}
          <g>
            <text x="60" y="274" fill="#94a3b8" fontSize="10.5" fontWeight="600">
              Arraste ou observe o ajuste do modelo:
            </text>

            {/* Trilho base */}
            <rect
              ref={sliderBarRef}
              x={trackX1}
              y={trackY - 3}
              width={trackWidth}
              height="6"
              rx="3"
              fill="rgba(148, 163, 184, 0.25)"
              cursor="pointer"
            />
            {/* Trilho preenchido */}
            <rect
              x={trackX1}
              y={trackY - 3}
              width={currentThumbPos - trackX1}
              height="6"
              rx="3"
              fill={isOptimal ? '#82c8ee' : '#ff6b3d'}
              cursor="pointer"
            />

            {/* Marcador do ponto ótimo de referência */}
            <line
              x1={trackX1 + 0.65 * trackWidth}
              y1={trackY - 7}
              x2={trackX1 + 0.65 * trackWidth}
              y2={trackY + 7}
              stroke="#82c8ee"
              strokeWidth="2"
              opacity="0.75"
            />

            {/* Botão circular do slider (Thumb) */}
            <circle
              cx={currentThumbPos}
              cy={trackY}
              r="9"
              fill={isOptimal ? '#82c8ee' : '#ff6b3d'}
              stroke="#ffffff"
              strokeWidth="2.5"
              cursor="grab"
              filter="url(#cursorShadow)"
            />
          </g>

          {/* O MOUSEZINHO ANIMADO (Cursor SVG em tempo real) */}
          {!isUserInteracting && cursorPos.visible && (
            <g
              transform={`translate(${cursorPos.x}, ${cursorPos.y})`}
              filter="url(#cursorShadow)"
              pointerEvents="none"
              style={{ transition: 'opacity 0.3s ease' }}
            >
              {/* Anel de clique quando pressionado */}
              {cursorPos.clicking && (
                <circle
                  cx="3"
                  cy="3"
                  r="14"
                  fill="rgba(255, 107, 61, 0.25)"
                  stroke="#ff6b3d"
                  strokeWidth="1.8"
                >
                  <animate
                    attributeName="r"
                    values="10;16;12"
                    dur="0.6s"
                    repeatCount="indefinite"
                  />
                  <animate
                    attributeName="opacity"
                    values="0.8;0.3;0.6"
                    dur="0.6s"
                    repeatCount="indefinite"
                  />
                </circle>
              )}

              {/* Ícone vetorizado do cursor do mouse */}
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none">
                <path
                  d="M4 3L11 20L14 13L21 10L4 3Z"
                  fill="#ffffff"
                  stroke="#020914"
                  strokeWidth="2"
                  strokeLinejoin="round"
                />
              </svg>
            </g>
          )}
        </svg>
      </div>

      <div className="hero-card-controls">
        {/* Controle nativo acessível oculto visualmente apenas para suporte a leitores de tela e teclado */}
        <label htmlFor="hero-demo-slider" className="sr-only">
          Controle da inclinação da reta de regressão
        </label>
        <input
          id="hero-demo-slider"
          type="range"
          min="0"
          max="100"
          value={Math.round(sliderPercent)}
          onChange={handleManualSliderChange}
          className="sr-only"
        />

        <div className="hero-card-footer">
          <span>O modelo ajusta a reta para minimizar o erro quadrático (MSE).</span>
          <a href="#/regressao-linear" className="hero-mini-cta">
            <span>Explorar modelo 01</span>
            <ArrowUpRightIcon />
          </a>
        </div>
      </div>
    </div>
  );
}
