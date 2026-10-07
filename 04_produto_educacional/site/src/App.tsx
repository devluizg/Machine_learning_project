import { useEffect, useState } from 'react';
import { AmbientParticles } from './components/AmbientParticles';
import { KmeansModule, KnnModule, LinearModule, LogisticModule, TreeModule } from './learning/Modules';

const models = [
  { id: 'regressao-linear', number: '01', name: 'Regressão linear', family: 'REGRESSÃO', question: 'Como prever um valor?', summary: 'Tendência, reta, resíduos e erro quadrático.', symbol: '↗', component: LinearModule },
  { id: 'regressao-logistica', number: '02', name: 'Regressão logística', family: 'CLASSIFICAÇÃO', question: 'Como estimar uma chance?', summary: 'Probabilidade, sigmoide e decisão.', symbol: '∿', component: LogisticModule },
  { id: 'knn', number: '03', name: 'k-vizinhos próximos', family: 'CLASSIFICAÇÃO', question: 'O que dizem os vizinhos?', summary: 'Distância, vizinhança e votação.', symbol: '✣', component: KnnModule },
  { id: 'arvore', number: '04', name: 'Árvore de decisão', family: 'CLASSIFICAÇÃO', question: 'Que caminho seguir?', summary: 'Regras, divisões e caminhos.', symbol: '⌁', component: TreeModule },
  { id: 'kmeans', number: '05', name: 'k-means', family: 'AGRUPAMENTO', question: 'Como encontrar grupos?', summary: 'Atribuições, centróides e atualização.', symbol: '◌', component: KmeansModule },
] as const;

type ModelId = (typeof models)[number]['id'];

function routeFromHash(): ModelId | null {
  const id = window.location.hash.replace(/^#\/?/, '');
  return models.find((model) => model.id === id)?.id ?? null;
}

export default function App() {
  const [activeId, setActiveId] = useState<ModelId | null>(routeFromHash);
  const [motionPaused, setMotionPaused] = useState(() => window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  useEffect(() => {
    const update = () => setActiveId(routeFromHash());
    window.addEventListener('hashchange', update);
    return () => window.removeEventListener('hashchange', update);
  }, []);
  useEffect(() => {
    if (!activeId && window.location.hash === '#modelos') document.getElementById('modelos')?.scrollIntoView();
    else window.scrollTo(0, 0);
  }, [activeId]);
  const active = models.find((model) => model.id === activeId) ?? null;
  const ActiveModule = active?.component;

  return <div className="site-shell">
    <a className="skip-link" href="#conteudo" onClick={(event) => { event.preventDefault(); document.getElementById('conteudo')?.focus(); }}>Ir para o conteúdo</a>
    <header className="site-header">
      <a aria-label="Início do laboratório" className="wordmark" href="#/">plural<span className="wordmark-dot">.</span><small>LABORATÓRIO DE APRENDIZAGEM</small></a>
      <nav aria-label="Navegação principal" className="main-nav"><a className={!active ? 'nav-active' : ''} href="#/">Início</a><a href="#modelos">Os 5 modelos</a></nav>
      <span className="header-pill">PROTÓTIPO EDUCACIONAL <span>↗</span></span>
    </header>

    <main id="conteudo" tabIndex={-1}>
      {!active ? <>
        <section className="hero">
          <AmbientParticles paused={motionPaused} />
          <div className="hero-copy"><div className="hero-overline"><span className="pulse-dot" /> APRENDA EXPLORANDO · ENSINO MÉDIO</div><h1>Machine learning,<br /><em>sem caixa-preta.</em></h1><p>Mexa nos dados. Observe o gráfico. Entenda a matemática por trás de cinco modelos — um experimento de cada vez.</p><a className="hero-cta" href="#modelos">Explorar os modelos <span aria-hidden="true">↗</span></a><div className="hero-micro">Sem cadastro · Dados inventados para aprender · Em português</div><button className="motion-toggle" type="button" aria-pressed={!motionPaused} onClick={() => setMotionPaused(!motionPaused)}>{motionPaused ? 'Ativar movimento de fundo' : 'Pausar movimento de fundo'}</button></div>
          <div aria-hidden="true" className="hero-art"><AmbientParticles paused={motionPaused} /><span className="art-index">FIG. 01 — APRENDER É EXPERIMENTAR</span><svg viewBox="0 0 460 400"><line className="art-axis" x1="45" x2="418" y1="345" y2="345" /><line className="art-axis" x1="45" x2="45" y1="45" y2="345" /><path className="art-curve" d="M50 310 C130 300 140 290 200 215 S300 100 410 90" /><circle className="art-point p1" cx="100" cy="290" r="8" /><circle className="art-point p2" cx="147" cy="278" r="8" /><circle className="art-point p3" cx="190" cy="235" r="8" /><circle className="art-point p4" cx="252" cy="200" r="8" /><circle className="art-point p5" cx="315" cy="133" r="8" /><circle className="art-point p6" cx="374" cy="113" r="8" /><circle className="art-target" cx="252" cy="171" r="13" /><line className="art-gap" x1="252" x2="252" y1="171" y2="200" /><text x="68" y="73">DADOS → MODELO → SENTIDO</text><text x="294" y="303">E SE...?</text></svg><div className="art-caption"><span>01 / 05</span><span>Uma mudança.<br />Uma descoberta.</span></div></div>
        </section>
        <section className="beginner-primer" aria-labelledby="primer-title">
          <div><span className="section-number">ANTES DO PRIMEIRO EXPERIMENTO</span><h2 id="primer-title">Como uma máquina aprende com exemplos?</h2><p>Ela não “entende” como uma pessoa. Neste laboratório, um modelo usa números de exemplos inventados para produzir previsões ou grupos. Você verá o que ele recebeu, como mudou e onde pode errar.</p><a className="primer-link" href="#/regressao-linear">Começar pela regressão linear <span aria-hidden="true">→</span></a></div>
          <ol><li><strong>Dados</strong><span>Medidas e, em alguns modelos, a resposta conhecida.</span></li><li><strong>Modelo</strong><span>Uma regra matemática que tenta relacionar os dados.</span></li><li><strong>Treino ou consulta</strong><span>Alguns modelos ajustam parâmetros; o k-NN consulta exemplos guardados.</span></li><li><strong>Teste</strong><span>Casos separados ajudam a perguntar se a regra serve fora dos exemplos usados para ajustá-la.</span></li></ol>
          <details className="primer-glossary"><summary>Palavras que você vai encontrar</summary><p><strong>Parâmetro:</strong> número que muda o comportamento do modelo. <strong>Erro:</strong> diferença entre resultado e referência conhecida. <strong>Rótulo:</strong> categoria informada para um exemplo. <strong>Classificar:</strong> escolher uma categoria. <strong>Agrupar:</strong> reunir exemplos semelhantes sem rótulos prévios.</p></details>
        </section>
        <section className="principle-strip" aria-label="Como aprender"><div><span>01</span><strong>Observe</strong><small>Leia os dados e imagine o resultado.</small></div><div><span>02</span><strong>Experimente</strong><small>Altere um controle de cada vez.</small></div><div><span>03</span><strong>Explique</strong><small>Conecte gráfico, decisão e fórmula.</small></div></section>
        <section className="model-section" id="modelos"><div className="section-heading"><div><span className="section-number">UM PEQUENO ATLAS</span><h2>Cinco maneiras de<br /><em>aprender com dados.</em></h2></div><p>Três ideias centrais: prever valores, escolher classes e descobrir grupos. Se esta é sua primeira visita, comece pelo modelo 01; depois escolha livremente.</p></div><div className="model-grid">{models.map((model) => <a className="model-card" href={`#/${model.id}`} key={model.id}><div className="model-card-top"><span>{model.number} / 05</span><span>{model.family}</span></div><span aria-hidden="true" className="model-symbol">{model.symbol}</span><h3>{model.name}</h3><p>{model.summary}</p><span className="model-link">Abrir experimento <span aria-hidden="true">↗</span></span></a>)}</div></section>
      </> : <div className="module-page">
        <AmbientParticles paused={motionPaused} viewport />
        <section className="module-hero"><div className="module-topline"><a className="back-link" href="#/">← Voltar ao início</a><button className="motion-toggle" type="button" aria-pressed={!motionPaused} onClick={() => setMotionPaused(!motionPaused)}>{motionPaused ? 'Ativar movimento de fundo' : 'Pausar movimento de fundo'}</button></div><div className="module-hero-body"><div><span className="module-family">MODELO {active.number} / 05 <span>—</span> {active.family}</span><h1>{active.name}<span className="module-period">.</span></h1><p>{active.question} <span>{active.summary}</span></p></div><span aria-hidden="true" className="module-hero-symbol">{active.symbol}</span></div></section>
        <nav aria-label="Escolher outro modelo" className="module-tabs">{models.map((model) => <a aria-current={active.id === model.id ? 'page' : undefined} href={`#/${model.id}`} key={model.id}><span>{model.number}</span> {model.name}</a>)}</nav>
        <div className="module-content" key={active.id}>{ActiveModule && <ActiveModule />}</div>
        <section className="next-model"><span className="tiny-label">CONTINUE EXPLORANDO</span><h2>O próximo modelo conta outra história.</h2><a href={`#/${models[(models.findIndex((model) => model.id === active.id) + 1) % models.length]!.id}`}>Próximo experimento <span aria-hidden="true">↗</span></a></section>
      </div>}
    </main>
    <footer className="site-footer"><span>plural<span className="wordmark-dot">.</span> / laboratório de aprendizagem</span><p>Protótipo autoral para investigação pedagógica · PROFCOMP/UFPA. Conteúdo e exemplos sujeitos a validação didática. Nenhuma resposta é coletada.</p></footer>
  </div>;
}
