export function ArrowUpRightIcon({ className = 'icon-arrow' }: { className?: string }) {
  return (
    <svg
      aria-hidden="true"
      className={className}
      fill="none"
      height="14"
      stroke="currentColor"
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth="2.2"
      viewBox="0 0 24 24"
      width="14"
    >
      <line x1="7" x2="17" y1="17" y2="7" />
      <polyline points="7 7 17 7 17 17" />
    </svg>
  );
}

export function LinearRegressionIcon({ className = 'model-svg-icon' }: { className?: string }) {
  return (
    <svg
      aria-hidden="true"
      className={className}
      fill="none"
      height="48"
      viewBox="0 0 64 64"
      width="48"
    >
      <defs>
        <style>{`
          @keyframes linTilt {
            0%, 100% { transform: rotate(-5deg); }
            50% { transform: rotate(5deg); }
          }
          @keyframes linDash {
            0% { stroke-dashoffset: 0; }
            100% { stroke-dashoffset: 10; }
          }
          @keyframes linPulse {
            0%, 100% { opacity: 0.7; transform: scale(0.95); }
            50% { opacity: 1; transform: scale(1.08); }
          }
          .lin-rot-group {
            transform-origin: 33px 31px;
            animation: linTilt 5.5s ease-in-out infinite;
          }
          .lin-residue {
            stroke-dasharray: 2 3;
            animation: linDash 4s linear infinite;
          }
          .lin-point {
            transform-origin: center;
            animation: linPulse 4s ease-in-out infinite alternate;
          }
          @media (prefers-reduced-motion: reduce) {
            .lin-rot-group, .lin-residue, .lin-point { animation: none !important; }
          }
        `}</style>
      </defs>
      {/* Eixos */}
      <line stroke="rgba(140, 180, 220, 0.35)" strokeLinecap="round" strokeWidth="2" x1="10" x2="54" y1="52" y2="52" />
      <line stroke="rgba(140, 180, 220, 0.35)" strokeLinecap="round" strokeWidth="2" x1="10" x2="10" y1="52" y2="10" />
      {/* Resíduos/Erros verticais */}
      <line className="lin-residue" stroke="rgba(242, 102, 60, 0.65)" strokeWidth="1.5" x1="22" x2="22" y1="44" y2="38" />
      <line className="lin-residue" stroke="rgba(242, 102, 60, 0.65)" strokeWidth="1.5" x1="34" x2="34" y1="26" y2="30" />
      <line className="lin-residue" stroke="rgba(242, 102, 60, 0.65)" strokeWidth="1.5" x1="46" x2="46" y1="16" y2="22" />
      {/* Reta ajustada com animação suave de rotação/ajuste */}
      <g className="lin-rot-group">
        <line stroke="#ff6b3d" strokeLinecap="round" strokeWidth="3" x1="14" x2="52" y1="46" y2="16" />
        <circle cx="33" cy="31" fill="#fff" r="2.5" />
      </g>
      {/* Pontos de dados */}
      <circle className="lin-point" cx="22" cy="44" fill="#82c8ee" r="3.5" stroke="#081d3d" strokeWidth="1.5" />
      <circle className="lin-point" cx="34" cy="26" fill="#82c8ee" r="3.5" stroke="#081d3d" strokeWidth="1.5" style={{ animationDelay: '0.8s' }} />
      <circle className="lin-point" cx="46" cy="16" fill="#82c8ee" r="3.5" stroke="#081d3d" strokeWidth="1.5" style={{ animationDelay: '1.6s' }} />
      <circle className="lin-point" cx="28" cy="36" fill="#fff" r="3" stroke="#ff6b3d" strokeWidth="1.5" style={{ animationDelay: '2.4s' }} />
    </svg>
  );
}

export function LogisticRegressionIcon({ className = 'model-svg-icon' }: { className?: string }) {
  return (
    <svg
      aria-hidden="true"
      className={className}
      fill="none"
      height="48"
      viewBox="0 0 64 64"
      width="48"
    >
      <defs>
        <style>{`
          @keyframes logDraw {
            0% { stroke-dashoffset: 75; }
            50% { stroke-dashoffset: 0; }
            100% { stroke-dashoffset: 0; }
          }
          @keyframes logDash {
            0% { stroke-dashoffset: 0; }
            100% { stroke-dashoffset: 12; }
          }
          @keyframes logPulse {
            0%, 100% { opacity: 0.55; transform: scale(0.9); }
            50% { opacity: 1; transform: scale(1.12); }
          }
          .log-curve {
            stroke-dasharray: 75;
            animation: logDraw 6s ease-in-out infinite alternate;
          }
          .log-threshold {
            stroke-dasharray: 3 3;
            animation: logDash 3.5s linear infinite;
          }
          .log-pt-blue {
            transform-origin: center;
            animation: logPulse 3.5s ease-in-out infinite;
          }
          .log-pt-orange {
            transform-origin: center;
            animation: logPulse 3.5s ease-in-out infinite 1.75s;
          }
          @media (prefers-reduced-motion: reduce) {
            .log-curve, .log-threshold, .log-pt-blue, .log-pt-orange { animation: none !important; }
          }
        `}</style>
      </defs>
      {/* Eixos */}
      <line stroke="rgba(140, 180, 220, 0.35)" strokeLinecap="round" strokeWidth="2" x1="10" x2="54" y1="52" y2="52" />
      <line stroke="rgba(140, 180, 220, 0.35)" strokeLinecap="round" strokeWidth="2" x1="10" x2="10" y1="52" y2="10" />
      {/* Linha de limiar de probabilidade 0.5 */}
      <line className="log-threshold" stroke="rgba(140, 180, 220, 0.35)" strokeWidth="1.5" x1="10" x2="54" y1="32" y2="32" />
      {/* Curva sigmoide com animação de traçado contínuo */}
      <path
        className="log-curve"
        d="M12 48 C 26 48, 28 46, 32 32 C 36 18, 38 16, 52 16"
        fill="none"
        stroke="#ff6b3d"
        strokeLinecap="round"
        strokeWidth="3"
      />
      {/* Pontos classe 0 e classe 1 */}
      <circle className="log-pt-blue" cx="16" cy="48" fill="#82c8ee" r="3.2" />
      <circle className="log-pt-blue" cx="24" cy="48" fill="#82c8ee" r="3.2" />
      <circle className="log-pt-orange" cx="40" cy="16" fill="#ff6b3d" r="3.2" />
      <circle className="log-pt-orange" cx="48" cy="16" fill="#ff6b3d" r="3.2" />
    </svg>
  );
}

export function SvmIcon({ className = 'model-svg-icon' }: { className?: string }) {
  return (
    <svg aria-hidden="true" className={className} fill="none" height="48" viewBox="0 0 64 64" width="48">
      <defs><style>{`
        @keyframes svmLine { 0%,100% { transform: translateX(-2px); } 50% { transform: translateX(2px); } }
        @keyframes svmPoint { 0%,100% { opacity:.65; } 50% { opacity:1; } }
        .svm-icon-line { animation: svmLine 3.6s ease-in-out infinite; transform-origin:center; }
        .svm-icon-point { animation: svmPoint 2.6s ease-in-out infinite; }
        @media (prefers-reduced-motion: reduce) { .svm-icon-line,.svm-icon-point { animation:none!important; } }
      `}</style></defs>
      <line stroke="rgba(140,180,220,.35)" strokeLinecap="round" strokeWidth="2" x1="10" x2="54" y1="52" y2="52" />
      <line stroke="rgba(140,180,220,.35)" strokeLinecap="round" strokeWidth="2" x1="10" x2="10" y1="52" y2="10" />
      <g className="svm-icon-line"><line stroke="rgba(130,200,238,.55)" strokeDasharray="3 3" strokeWidth="1.5" x1="20" x2="49" y1="48" y2="19" /><line stroke="#ff6b3d" strokeLinecap="round" strokeWidth="3" x1="16" x2="45" y1="48" y2="19" /><line stroke="rgba(130,200,238,.55)" strokeDasharray="3 3" strokeWidth="1.5" x1="12" x2="41" y1="48" y2="19" /></g>
      <circle className="svm-icon-point" cx="18" cy="39" fill="#82c8ee" r="3.2" /><circle className="svm-icon-point" cx="26" cy="45" fill="#82c8ee" r="3.2" style={{ animationDelay: '.5s' }} /><circle className="svm-icon-point" cx="31" cy="32" fill="#82c8ee" r="3.2" style={{ animationDelay: '1s' }} />
      <circle className="svm-icon-point" cx="38" cy="27" fill="#ff6b3d" r="3.2" style={{ animationDelay: '.3s' }} /><circle className="svm-icon-point" cx="46" cy="21" fill="#ff6b3d" r="3.2" style={{ animationDelay: '.8s' }} /><circle className="svm-icon-point" cx="47" cy="34" fill="#ff6b3d" r="3.2" style={{ animationDelay: '1.3s' }} />
    </svg>
  );
}

export function KnnIcon({ className = 'model-svg-icon' }: { className?: string }) {
  return (
    <svg
      aria-hidden="true"
      className={className}
      fill="none"
      height="48"
      viewBox="0 0 64 64"
      width="48"
    >
      <defs>
        <style>{`
          @keyframes knnExpand {
            0%, 100% { r: 14px; opacity: 0.45; }
            50% { r: 21px; opacity: 0.95; }
          }
          @keyframes knnLinks {
            0%, 100% { opacity: 0.2; stroke-dashoffset: 6; }
            50% { opacity: 0.85; stroke-dashoffset: 0; }
          }
          @keyframes knnCenter {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.15); }
          }
          .knn-search-radius {
            transform-origin: 32px 32px;
            animation: knnExpand 5s ease-in-out infinite;
          }
          .knn-link {
            stroke-dasharray: 3 3;
            animation: knnLinks 5s ease-in-out infinite;
          }
          .knn-target {
            transform-origin: 32px 32px;
            animation: knnCenter 2.5s ease-in-out infinite;
          }
          @media (prefers-reduced-motion: reduce) {
            .knn-search-radius, .knn-link, .knn-target { animation: none !important; }
          }
        `}</style>
      </defs>
      {/* Raio de vizinhança k-NN que expande e contrai suavemente */}
      <circle className="knn-search-radius" cx="32" cy="32" fill="rgba(130, 200, 238, 0.08)" r="20" stroke="#82c8ee" strokeDasharray="3 3" strokeWidth="1.5" />
      {/* Conexões com os 3 vizinhos mais próximos */}
      <line className="knn-link" stroke="rgba(255, 107, 61, 0.75)" strokeWidth="1.5" x1="32" x2="22" y1="32" y2="24" />
      <line className="knn-link" stroke="rgba(255, 107, 61, 0.75)" strokeWidth="1.5" x1="32" x2="24" y1="32" y2="40" />
      <line className="knn-link" stroke="rgba(255, 107, 61, 0.75)" strokeWidth="1.5" x1="32" x2="44" y1="32" y2="30" />
      {/* Ponto de consulta (interrogação central com pulso suave) */}
      <circle className="knn-target" cx="32" cy="32" fill="#ff6b3d" r="4.5" stroke="#fff" strokeWidth="2" />
      {/* Vizinhos próximos */}
      <circle cx="22" cy="24" fill="#82c8ee" r="3.5" />
      <circle cx="24" cy="40" fill="#82c8ee" r="3.5" />
      <circle cx="44" cy="30" fill="#ff6b3d" r="3.5" />
      {/* Pontos mais distantes fora do raio */}
      <circle cx="14" cy="16" fill="rgba(130, 200, 238, 0.4)" r="2.5" />
      <circle cx="50" cy="46" fill="rgba(255, 107, 61, 0.4)" r="2.5" />
    </svg>
  );
}

export function DecisionTreeIcon({ className = 'model-svg-icon' }: { className?: string }) {
  return (
    <svg
      aria-hidden="true"
      className={className}
      fill="none"
      height="48"
      viewBox="0 0 64 64"
      width="48"
    >
      <defs>
        <style>{`
          @keyframes treeStep1 {
            0%, 100% { opacity: 0.4; }
            15%, 45% { opacity: 1; filter: drop-shadow(0 0 4px #ff6b3d); }
          }
          @keyframes treeStep2 {
            0%, 25%, 100% { opacity: 0.4; }
            40%, 70% { opacity: 1; filter: drop-shadow(0 0 4px #82c8ee); }
          }
          @keyframes treeStep3 {
            0%, 50%, 100% { opacity: 0.4; }
            65%, 90% { opacity: 1; filter: drop-shadow(0 0 4px #ff6b3d); }
          }
          .tree-root { animation: treeStep1 5s ease-in-out infinite; }
          .tree-mid-left { animation: treeStep2 5s ease-in-out infinite; }
          .tree-mid-right { animation: treeStep1 5s ease-in-out infinite 1.5s; }
          .tree-leaf-1 { animation: treeStep3 5s ease-in-out infinite; }
          .tree-leaf-2 { animation: treeStep2 5s ease-in-out infinite 1s; }
          @media (prefers-reduced-motion: reduce) {
            .tree-root, .tree-mid-left, .tree-mid-right, .tree-leaf-1, .tree-leaf-2 { animation: none !important; }
          }
        `}</style>
      </defs>
      {/* Ramos */}
      <line stroke="#ff6b3d" strokeWidth="2" x1="32" x2="18" y1="18" y2="32" />
      <line stroke="#82c8ee" strokeWidth="2" x1="32" x2="46" y1="18" y2="32" />
      <line stroke="#ff6b3d" strokeWidth="1.8" x1="18" x2="11" y1="34" y2="48" />
      <line stroke="#82c8ee" strokeWidth="1.8" x1="18" x2="25" y1="34" y2="48" />
      <line stroke="#ff6b3d" strokeWidth="1.8" x1="46" x2="46" y1="34" y2="48" />
      {/* Nó raiz com pulso no topo */}
      <circle className="tree-root" cx="32" cy="18" fill="#081d3d" r="5" stroke="#ff6b3d" strokeWidth="2" />
      {/* Nós intermediários */}
      <circle className="tree-mid-left" cx="18" cy="33" fill="#081d3d" r="4" stroke="#ff6b3d" strokeWidth="1.8" />
      <circle className="tree-mid-right" cx="46" cy="33" fill="#081d3d" r="4" stroke="#82c8ee" strokeWidth="1.8" />
      {/* Folhas / Decisões finais */}
      <rect className="tree-leaf-1" fill="#ff6b3d" height="7" rx="2" width="7" x="7.5" y="46" />
      <rect className="tree-leaf-2" fill="#82c8ee" height="7" rx="2" width="7" x="21.5" y="46" />
      <rect className="tree-leaf-1" fill="#ff6b3d" height="7" rx="2" width="7" x="42.5" y="46" style={{ animationDelay: '2s' }} />
    </svg>
  );
}

export function KmeansIcon({ className = 'model-svg-icon' }: { className?: string }) {
  return (
    <svg
      aria-hidden="true"
      className={className}
      fill="none"
      height="48"
      viewBox="0 0 64 64"
      width="48"
    >
      <defs>
        <style>{`
          @keyframes kmCentroid1 {
            0%, 100% { transform: translate(0, 0); }
            50% { transform: translate(2px, -2px); }
          }
          @keyframes kmCentroid2 {
            0%, 100% { transform: translate(0, 0); }
            50% { transform: translate(-2px, 2px); }
          }
          @keyframes kmHalo1 {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
          }
          @keyframes kmHalo2 {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(-360deg); }
          }
          .km-c1 {
            animation: kmCentroid1 5s ease-in-out infinite;
          }
          .km-c2 {
            animation: kmCentroid2 5s ease-in-out infinite;
          }
          .km-h1 {
            transform-origin: 22px 24px;
            animation: kmHalo1 14s linear infinite;
          }
          .km-h2 {
            transform-origin: 44px 38px;
            animation: kmHalo2 14s linear infinite;
          }
          @media (prefers-reduced-motion: reduce) {
            .km-c1, .km-c2, .km-h1, .km-h2 { animation: none !important; }
          }
        `}</style>
      </defs>
      {/* Halo de cluster 1 com rotação lenta */}
      <circle className="km-h1" cx="22" cy="24" fill="rgba(130, 200, 238, 0.12)" r="13" stroke="rgba(130, 200, 238, 0.45)" strokeDasharray="3 3" />
      {/* Halo de cluster 2 com rotação lenta invertida */}
      <circle className="km-h2" cx="44" cy="38" fill="rgba(255, 107, 61, 0.12)" r="13" stroke="rgba(255, 107, 61, 0.45)" strokeDasharray="3 3" />
      {/* Centróide 1 móvel */}
      <g className="km-c1">
        <circle cx="22" cy="24" fill="#82c8ee" r="4" stroke="#fff" strokeWidth="1.5" />
        <line stroke="#fff" strokeWidth="1.5" x1="22" x2="22" y1="21" y2="27" />
        <line stroke="#fff" strokeWidth="1.5" x1="19" x2="25" y1="24" y2="24" />
      </g>
      {/* Centróide 2 móvel */}
      <g className="km-c2">
        <circle cx="44" cy="38" fill="#ff6b3d" r="4" stroke="#fff" strokeWidth="1.5" />
        <line stroke="#fff" strokeWidth="1.5" x1="44" x2="44" y1="35" y2="41" />
        <line stroke="#fff" strokeWidth="1.5" x1="41" x2="47" y1="38" y2="38" />
      </g>
      {/* Pontos do cluster 1 */}
      <circle cx="16" cy="20" fill="#82c8ee" r="2.5" />
      <circle cx="26" cy="18" fill="#82c8ee" r="2.5" />
      <circle cx="20" cy="31" fill="#82c8ee" r="2.5" />
      {/* Pontos do cluster 2 */}
      <circle cx="39" cy="42" fill="#ff6b3d" r="2.5" />
      <circle cx="48" cy="33" fill="#ff6b3d" r="2.5" />
      <circle cx="49" cy="44" fill="#ff6b3d" r="2.5" />
    </svg>
  );
}
