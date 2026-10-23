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
      {/* Eixos */}
      <line stroke="rgba(140, 180, 220, 0.35)" strokeLinecap="round" strokeWidth="2" x1="10" x2="54" y1="52" y2="52" />
      <line stroke="rgba(140, 180, 220, 0.35)" strokeLinecap="round" strokeWidth="2" x1="10" x2="10" y1="52" y2="10" />
      {/* Resíduos/Erros verticais */}
      <line stroke="rgba(242, 102, 60, 0.5)" strokeDasharray="2 3" strokeWidth="1.5" x1="22" x2="22" y1="44" y2="38" />
      <line stroke="rgba(242, 102, 60, 0.5)" strokeDasharray="2 3" strokeWidth="1.5" x1="34" x2="34" y1="26" y2="30" />
      <line stroke="rgba(242, 102, 60, 0.5)" strokeDasharray="2 3" strokeWidth="1.5" x1="46" x2="46" y1="16" y2="22" />
      {/* Reta ajustada */}
      <line stroke="#ff6b3d" strokeLinecap="round" strokeWidth="3" x1="14" x2="52" y1="46" y2="16" />
      {/* Pontos de dados */}
      <circle cx="22" cy="44" fill="#82c8ee" r="3.5" stroke="#081d3d" strokeWidth="1.5" />
      <circle cx="34" cy="26" fill="#82c8ee" r="3.5" stroke="#081d3d" strokeWidth="1.5" />
      <circle cx="46" cy="16" fill="#82c8ee" r="3.5" stroke="#081d3d" strokeWidth="1.5" />
      <circle cx="28" cy="36" fill="#fff" r="3" stroke="#ff6b3d" strokeWidth="1.5" />
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
      {/* Eixos */}
      <line stroke="rgba(140, 180, 220, 0.35)" strokeLinecap="round" strokeWidth="2" x1="10" x2="54" y1="52" y2="52" />
      <line stroke="rgba(140, 180, 220, 0.35)" strokeLinecap="round" strokeWidth="2" x1="10" x2="10" y1="52" y2="10" />
      {/* Linha de limiar de probabilidade 0.5 */}
      <line stroke="rgba(140, 180, 220, 0.25)" strokeDasharray="3 3" strokeWidth="1.5" x1="10" x2="54" y1="32" y2="32" />
      {/* Curva sigmoide */}
      <path
        d="M12 48 C 26 48, 28 46, 32 32 C 36 18, 38 16, 52 16"
        fill="none"
        stroke="#ff6b3d"
        strokeLinecap="round"
        strokeWidth="3"
      />
      {/* Pontos classe 0 e classe 1 */}
      <circle cx="16" cy="48" fill="#82c8ee" r="3" />
      <circle cx="24" cy="48" fill="#82c8ee" r="3" />
      <circle cx="40" cy="16" fill="#ff6b3d" r="3" />
      <circle cx="48" cy="16" fill="#ff6b3d" r="3" />
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
      {/* Raio de vizinhança k-NN */}
      <circle cx="32" cy="32" fill="rgba(130, 200, 238, 0.08)" r="20" stroke="#82c8ee" strokeDasharray="3 3" strokeWidth="1.5" />
      {/* Conexões com os 3 vizinhos mais próximos */}
      <line stroke="rgba(255, 107, 61, 0.6)" strokeDasharray="2 2" strokeWidth="1.5" x1="32" x2="22" y1="32" y2="24" />
      <line stroke="rgba(255, 107, 61, 0.6)" strokeDasharray="2 2" strokeWidth="1.5" x1="32" x2="24" y1="32" y2="40" />
      <line stroke="rgba(255, 107, 61, 0.6)" strokeDasharray="2 2" strokeWidth="1.5" x1="32" x2="44" y1="32" y2="30" />
      {/* Ponto de consulta (interrogação central) */}
      <circle cx="32" cy="32" fill="#ff6b3d" r="4.5" stroke="#fff" strokeWidth="2" />
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
      {/* Ramos */}
      <line stroke="#ff6b3d" strokeWidth="2" x1="32" x2="18" y1="18" y2="32" />
      <line stroke="#82c8ee" strokeWidth="2" x1="32" x2="46" y1="18" y2="32" />
      <line stroke="#ff6b3d" strokeWidth="1.8" x1="18" x2="11" y1="34" y2="48" />
      <line stroke="#82c8ee" strokeWidth="1.8" x1="18" x2="25" y1="34" y2="48" />
      <line stroke="#ff6b3d" strokeWidth="1.8" x1="46" x2="46" y1="34" y2="48" />
      {/* Nó raiz */}
      <circle cx="32" cy="18" fill="#081d3d" r="5" stroke="#ff6b3d" strokeWidth="2" />
      {/* Nós intermediários */}
      <circle cx="18" cy="33" fill="#081d3d" r="4" stroke="#ff6b3d" strokeWidth="1.8" />
      <circle cx="46" cy="33" fill="#081d3d" r="4" stroke="#82c8ee" strokeWidth="1.8" />
      {/* Folhas / Decisões finais */}
      <rect fill="#ff6b3d" height="7" rx="2" width="7" x="7.5" y="46" />
      <rect fill="#82c8ee" height="7" rx="2" width="7" x="21.5" y="46" />
      <rect fill="#ff6b3d" height="7" rx="2" width="7" x="42.5" y="46" />
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
      {/* Halo de cluster 1 */}
      <circle cx="22" cy="24" fill="rgba(130, 200, 238, 0.12)" r="13" stroke="rgba(130, 200, 238, 0.4)" strokeDasharray="3 3" />
      {/* Halo de cluster 2 */}
      <circle cx="44" cy="38" fill="rgba(255, 107, 61, 0.12)" r="13" stroke="rgba(255, 107, 61, 0.4)" strokeDasharray="3 3" />
      {/* Centróide 1 (Cruz ou anel) */}
      <circle cx="22" cy="24" fill="#82c8ee" r="4" stroke="#fff" strokeWidth="1.5" />
      <line stroke="#fff" strokeWidth="1.5" x1="22" x2="22" y1="21" y2="27" />
      <line stroke="#fff" strokeWidth="1.5" x1="19" x2="25" y1="24" y2="24" />
      {/* Centróide 2 */}
      <circle cx="44" cy="38" fill="#ff6b3d" r="4" stroke="#fff" strokeWidth="1.5" />
      <line stroke="#fff" strokeWidth="1.5" x1="44" x2="44" y1="35" y2="41" />
      <line stroke="#fff" strokeWidth="1.5" x1="41" x2="47" y1="38" y2="38" />
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
