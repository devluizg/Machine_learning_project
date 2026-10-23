import { useEffect, useState } from 'react';
import { AmbientParticles } from './components/AmbientParticles';
import { HeroDemo } from './components/HeroDemo';
import {
  ArrowUpRightIcon,
  LinearRegressionIcon,
  LogisticRegressionIcon,
  KnnIcon,
  DecisionTreeIcon,
  KmeansIcon,
} from './components/ModelIcons';
import { ComparisonPage, TeacherGuidePage } from './learning/CourseSupport';
import { HelpPage, LessonContext, StudentJourneyPage } from './learning/LearningSupport';
import { KmeansModule, KnnModule, LinearModule, LogisticModule, TreeModule } from './learning/Modules';

const PRODUCT_VERSION = '0.2.0-campo';

const models = [
  { id: 'regressao-linear', number: '01', name: 'Regressão linear', family: 'REGRESSÃO', question: 'Como prever um valor?', summary: 'Tendência, reta, resíduos e erro quadrático.', icon: LinearRegressionIcon, component: LinearModule },
  { id: 'regressao-logistica', number: '02', name: 'Regressão logística', family: 'CLASSIFICAÇÃO', question: 'Como estimar uma chance?', summary: 'Probabilidade, sigmoide e decisão.', icon: LogisticRegressionIcon, component: LogisticModule },
  { id: 'knn', number: '03', name: 'k-vizinhos mais próximos', family: 'CLASSIFICAÇÃO', question: 'O que dizem os vizinhos?', summary: 'Distância, vizinhança e votação.', icon: KnnIcon, component: KnnModule },
  { id: 'arvore', number: '04', name: 'Árvore de decisão', family: 'CLASSIFICAÇÃO', question: 'Que caminho seguir?', summary: 'Regras, divisões e caminhos.', icon: DecisionTreeIcon, component: TreeModule },
  { id: 'kmeans', number: '05', name: 'k-means', family: 'AGRUPAMENTO', question: 'Como encontrar grupos?', summary: 'Atribuições, centróides e atualização.', icon: KmeansIcon, component: KmeansModule },
] as const;

type ModelId = (typeof models)[number]['id'];
type RouteId = ModelId | 'sintese' | 'percurso' | 'professor' | 'ajuda';

function routeFromHash(): RouteId | null {
  const id = window.location.hash.replace(/^#\/?/, '');
  if (id === 'sintese' || id === 'percurso' || id === 'professor' || id === 'ajuda') return id;
  return models.find((model) => model.id === id)?.id ?? null;
}

export default function App() {
  const [route, setRoute] = useState<RouteId | null>(routeFromHash);
  const [motionPaused, setMotionPaused] = useState(() => window.matchMedia('(prefers-reduced-motion: reduce)').matches);

  useEffect(() => {
    const update = () => setRoute(routeFromHash());
    window.addEventListener('hashchange', update);
    return () => window.removeEventListener('hashchange', update);
  }, []);

  useEffect(() => {
    if (!route && window.location.hash === '#modelos') document.getElementById('modelos')?.scrollIntoView();
    else {
      window.scrollTo({ left: 0, top: 0, behavior: 'instant' });
      document.documentElement.scrollLeft = 0;
      document.body.scrollLeft = 0;
      document.querySelector<HTMLElement>('.main-nav')?.scrollTo({ left: 0, behavior: 'instant' });
    }
  }, [route]);

  const active = models.find((model) => model.id === route) ?? null;
  const ActiveModule = active?.component;
  const ActiveIcon = active?.icon;

  return (
    <div className="site-shell">
      <AmbientParticles paused={motionPaused} />
      <a className="skip-link" href="#conteudo" onClick={(event) => { event.preventDefault(); document.getElementById('conteudo')?.focus(); }}>
        Ir para o conteúdo
      </a>
      <header className="site-header">
        <a aria-label="Início do laboratório" className="wordmark" href="#/">
          Machine Learning Project
        </a>
        <nav aria-label="Navegação principal" className="main-nav">
          <a className={!route ? 'nav-active' : ''} href="#/">Início</a>
          <a className={route === 'percurso' ? 'nav-active' : ''} href="#/percurso">As 8 aulas</a>
          <a className={route === 'sintese' ? 'nav-active' : ''} href="#/sintese">Comparar</a>
          <a className={route === 'professor' ? 'nav-active' : ''} href="#/professor">Roteiro docente</a>
          <a className={route === 'ajuda' ? 'nav-active' : ''} href="#/ajuda">Ajuda</a>
        </nav>
        <button
          className="header-motion-toggle"
          type="button"
          aria-pressed={!motionPaused}
          onClick={() => setMotionPaused(!motionPaused)}
          title={motionPaused ? 'Ativar animação do céu estrelado' : 'Pausar animação do céu estrelado'}
        >
          <span className={`header-motion-dot ${motionPaused ? 'is-paused' : ''}`} />
          <span>{motionPaused ? 'Ativar movimento de fundo' : 'Pausar movimento de fundo'}</span>
        </button>
      </header>

      <main id="conteudo" tabIndex={-1}>
        {!route ? (
          <>
            <section className="hero">
              <div className="hero-copy">
                <div className="hero-overline">
                  <span className="pulse-dot" /> APRENDA EXPLORANDO · ENSINO MÉDIO
                </div>
                <h1>
                  Machine learning,<br />
                  <em>sem caixa-preta.</em>
                </h1>
                <p>
                  Explore os dados. Observe o gráfico. Compreenda os fundamentos matemáticos de cinco modelos, um experimento por vez.
                </p>
                <div className="hero-actions">
                  <a className="hero-cta" href="#modelos">
                    <span>Explorar os modelos</span>
                    <ArrowUpRightIcon />
                  </a>
                </div>
                <a className="journey-shortcut" href="#/percurso">Ver o percurso das oito aulas →</a>
                <div className="hero-micro">
                  Sem cadastro · Dados inventados para aprender · Em português
                </div>
              </div>

              {/* Mini-laboratório interativo vivo substituindo a figura estática */}
              <HeroDemo />
            </section>

            <section className="beginner-primer" aria-labelledby="primer-title">
              <div>
                <span className="section-number">ANTES DO PRIMEIRO EXPERIMENTO</span>
                <h2 id="primer-title">Como uma máquina aprende com exemplos?</h2>
                <p>
                  Ela não “entende” como uma pessoa. Neste laboratório, um modelo usa números de exemplos inventados para produzir previsões ou grupos. Você verá o que ele recebeu, como mudou e onde pode errar.
                </p>
                <a className="primer-link" href="#/regressao-linear">
                  <span>Começar pela regressão linear</span>
                  <ArrowUpRightIcon />
                </a>
              </div>
              <ol>
                <li>
                  <strong>Dados</strong>
                  <span>Medidas e, em alguns modelos, a resposta conhecida.</span>
                </li>
                <li>
                  <strong>Modelo</strong>
                  <span>Uma regra matemática que tenta relacionar os dados.</span>
                </li>
                <li>
                  <strong>Treino ou consulta</strong>
                  <span>Alguns modelos ajustam parâmetros; o k-NN consulta exemplos guardados.</span>
                </li>
                <li>
                  <strong>Teste</strong>
                  <span>Casos separados ajudam a perguntar se a regra serve fora dos exemplos usados para ajustá-la.</span>
                </li>
              </ol>
              <details className="primer-glossary">
                <summary>Palavras que você vai encontrar</summary>
                <p>
                  <strong>Parâmetro:</strong> número que muda o comportamento do modelo. <strong>Erro:</strong> diferença entre resultado e referência conhecida. <strong>Rótulo:</strong> categoria informada para um exemplo. <strong>Classificar:</strong> escolher uma categoria. <strong>Agrupar:</strong> reunir exemplos semelhantes sem rótulos prévios.
                </p>
              </details>
            </section>

            <section className="principle-strip" aria-label="Como aprender">
              <div className="principle-card">
                <span className="principle-num">01</span>
                <div>
                  <strong>Observe</strong>
                  <p>Leia os dados e imagine o resultado antes de testar qualquer hipótese.</p>
                </div>
              </div>
              <div className="principle-card">
                <span className="principle-num">02</span>
                <div>
                  <strong>Experimente</strong>
                  <p>Altere um controle de cada vez para isolar o efeito de cada parâmetro.</p>
                </div>
              </div>
              <div className="principle-card">
                <span className="principle-num">03</span>
                <div>
                  <strong>Explique</strong>
                  <p>Conecte o que mudou no gráfico à decisão do modelo e à sua fórmula matemática.</p>
                </div>
              </div>
            </section>

            <section className="model-section" id="modelos">
              <div className="section-heading">
                <div>
                  <span className="section-number">UM PEQUENO ATLAS</span>
                  <h2>
                    Cinco maneiras de<br />
                    <em>aprender com dados.</em>
                  </h2>
                </div>
                <p>
                  Três ideias centrais: prever valores, escolher classes e descobrir grupos. Se esta é sua primeira visita, comece pelo modelo 01; depois escolha livremente.
                </p>
              </div>
              <div className="model-grid">
                {models.map((model) => {
                  const Icon = model.icon;
                  return (
                    <a className="model-card" href={`#/${model.id}`} key={model.id}>
                      <div className="model-card-top">
                        <span>{model.number} / 05</span>
                        <span>{model.family}</span>
                      </div>
                      <div className="model-icon-wrap" aria-hidden="true">
                        <Icon />
                      </div>
                      <h3>{model.name}</h3>
                      <p>{model.summary}</p>
                      <span className="model-link">
                        <span>Abrir experimento</span>
                        <ArrowUpRightIcon />
                      </span>
                    </a>
                  );
                })}
              </div>

              <div className="home-support-strip">
                <div className="home-support-card">
                  <div className="support-card-head">
                    <span className="support-badge">ENCONTRO 07 · SÍNTESE COMPARATIVA</span>
                  </div>
                  <h3>Compare antes de escolher.</h3>
                  <p>
                    Veja lado a lado a finalidade, a entrada, a saída, o mecanismo de cálculo e os limites de aplicação dos cinco modelos.
                  </p>
                  <a href="#/sintese" className="support-card-btn">
                    <span>Abrir síntese comparativa</span>
                    <ArrowUpRightIcon />
                  </a>
                </div>

                <div className="home-support-card">
                  <div className="support-card-head">
                    <span className="support-badge accent">ROTEIRO DIDÁTICO · 8 AULAS</span>
                  </div>
                  <h3>Saiba onde você está.</h3>
                  <p>
                    Consulte o objetivo pedagógico, a ação principal do estudante e a explicação esperada em cada uma das oito aulas.
                  </p>
                  <a href="#/percurso" className="support-card-btn">
                    <span>Abrir percurso das aulas</span>
                    <ArrowUpRightIcon />
                  </a>
                </div>
              </div>
            </section>
          </>
        ) : route === 'sintese' ? (
          <ComparisonPage />
        ) : route === 'percurso' ? (
          <StudentJourneyPage />
        ) : route === 'professor' ? (
          <TeacherGuidePage />
        ) : route === 'ajuda' ? (
          <HelpPage />
        ) : active ? (
          <div className="module-page">
            <section className="module-hero">
              <div className="module-topline">
                <a className="back-link" href="#/">← Voltar ao início</a>
              </div>
              <div className="module-hero-body">
                <div>
                  <span className="module-family">
                    MODELO {active.number} / 05 <span>·</span> {active.family}
                  </span>
                  <h1>
                    {active.name}<span className="module-period">.</span>
                  </h1>
                  <p>
                    {active.question} <span>{active.summary}</span>
                  </p>
                </div>
                {ActiveIcon && (
                  <div aria-hidden="true" className="module-hero-icon-wrap">
                    <ActiveIcon className="module-hero-svg" />
                  </div>
                )}
              </div>
            </section>
            <nav aria-label="Escolher outro modelo" className="module-tabs">
              <span className="tabs-hint" aria-hidden="true">Deslize para ver mais →</span>
              {models.map((model) => (
                <a
                  aria-current={active.id === model.id ? 'page' : undefined}
                  href={`#/${model.id}`}
                  key={model.id}
                >
                  <span>{model.number}</span> {model.name}
                </a>
              ))}
              <a href="#/sintese">
                <span>07</span> Síntese
              </a>
            </nav>
            <div className="module-content" key={active.id}>
              <LessonContext modelId={active.id} />
              {ActiveModule && <ActiveModule />}
            </div>
            <section className="next-model">
              <span className="tiny-label">CONTINUE EXPLORANDO</span>
              <h2>
                {active.id === 'kmeans'
                  ? 'Agora compare os cinco modelos.'
                  : 'O próximo modelo conta outra história.'}
              </h2>
              <a
                href={
                  active.id === 'kmeans'
                    ? '#/sintese'
                    : `#/${models[models.findIndex((model) => model.id === active.id) + 1]!.id}`
                }
              >
                <span>{active.id === 'kmeans' ? 'Abrir síntese comparativa' : 'Próximo experimento'}</span>
                <ArrowUpRightIcon />
              </a>
            </section>
          </div>
        ) : null}
      </main>
      <footer className="site-footer">
        <span>Machine Learning Project <small>v{PRODUCT_VERSION}</small></span>
        <p>
          Protótipo autoral para investigação pedagógica · PROFCOMP/UFPA. Funciona localmente, sem conta ou coleta de respostas. <a href="#/ajuda">Ajuda de uso</a>
        </p>
      </footer>
    </div>
  );
}
