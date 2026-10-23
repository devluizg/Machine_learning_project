import { moduleLessonContexts, studentLessons } from './coursePlan';
import type { ModelComparison } from './coursePlan';

export function LessonContext({ modelId }: { modelId: ModelComparison['id'] }) {
  const lesson = moduleLessonContexts[modelId];

  return <aside className="lesson-context" aria-labelledby="lesson-context-title">
    <div className="lesson-context-marker" aria-hidden="true">
      <span>AULA</span>
      <strong>{lesson.meeting}</strong>
      <small>DE 8</small>
    </div>
    <div className="lesson-context-body">
      <span className="tiny-label">SEU FOCO NESTE ENCONTRO</span>
      <h2 id="lesson-context-title">{lesson.objective}</h2>
      <div className="lesson-context-steps">
        <p><strong>Antes</strong>{lesson.before}</p>
        <p><strong>Experimente</strong>{lesson.action}</p>
        <p><strong>Explique</strong>{lesson.explanation}</p>
      </div>
      <p className="lesson-context-next"><strong>Depois:</strong> {lesson.next}</p>
    </div>
  </aside>;
}

export function StudentJourneyPage() {
  return <div className="support-page journey-page">
    <section className="support-hero">
      <a className="back-link" href="#/">← Voltar ao início</a>
      <span className="module-family">PERCURSO DO ESTUDANTE</span>
      <h1>Oito aulas, uma pergunta de cada vez.</h1>
      <p>Em cada encontro, comece pela tarefa, registre uma previsão, experimente e explique o resultado. As aulas 1 e 8 seguem as orientações do professor.</p>
    </section>
    <section className="journey-list" aria-label="Percurso das oito aulas">
      {studentLessons.map((lesson) => <article className={`journey-card ${lesson.siteUse === 'sem-site' ? 'is-offline' : ''}`} key={lesson.number}>
        <div className="journey-number"><span>AULA</span><strong>{String(lesson.number).padStart(2, '0')}</strong></div>
        <div className="journey-card-body">
          <div className="journey-card-heading">
            <div><span>{lesson.siteUse === 'com-site' ? 'COM APOIO DO SITE' : 'SEM CONSULTA AO SITE'}</span><h2>{lesson.title}</h2></div>
            {lesson.route && lesson.number !== 1 && <a href={`#${lesson.route}`}>Abrir aula <span aria-hidden="true">↗</span></a>}
          </div>
          <p className="journey-purpose">{lesson.purpose}</p>
          <dl><div><dt>O que fazer</dt><dd>{lesson.action}</dd></div><div><dt>O que explicar</dt><dd>{lesson.evidence}</dd></div></dl>
        </div>
      </article>)}
    </section>
    <aside className="journey-privacy">
      <strong>Seus rascunhos ficam neste navegador.</strong>
      <p>O site não cria conta, não envia respostas e não substitui os materiais em papel entregues pelo professor.</p>
    </aside>
  </div>;
}

export function HelpPage() {
  return <div className="support-page help-page">
    <section className="support-hero">
      <a className="back-link" href="#/">← Voltar ao início</a>
      <span className="module-family">AJUDA RÁPIDA</span>
      <h1>Use um controle. Observe uma consequência.</h1>
      <p>O laboratório foi organizado para funcionar com mouse, touchpad ou teclado. Comece sempre pelo modo aula.</p>
    </section>
    <section className="help-grid" aria-label="Instruções de uso">
      <article><span>01</span><h2>Comece pelo modo aula</h2><p>Leia a situação, escreva uma previsão e altere apenas o controle indicado. A exploração livre é opcional.</p></article>
      <article><span>02</span><h2>Use o teclado</h2><p>Pressione Tab para avançar. Em um controle deslizante, use as setas. Enter ou Espaço ativa botões e opções.</p></article>
      <article><span>03</span><h2>Consulte os dados</h2><p>Abra “Consultar valores” abaixo do gráfico quando cores, pontos ou linhas não forem suficientes para acompanhar o resultado.</p></article>
      <article><span>04</span><h2>Recomece quando precisar</h2><p>Use “Recomeçar experimento” no modo livre ou volte ao modo aula para restaurar o primeiro exercício.</p></article>
      <article><span>05</span><h2>Reduza o movimento</h2><p>Pause o fundo pelo botão visível. A preferência de movimento reduzido do sistema também é respeitada.</p></article>
      <article><span>06</span><h2>Sem conexão externa</h2><p>Depois de instalado no computador da escola, o laboratório executa os cálculos localmente e não depende de conta.</p></article>
    </section>
    <section className="help-glossary" aria-labelledby="help-glossary-title">
      <span className="section-number">PALAVRAS DO PERCURSO</span>
      <h2 id="help-glossary-title">Glossário essencial</h2>
      <dl>
        <div><dt>Dado</dt><dd>Informação usada para descrever um exemplo.</dd></div>
        <div><dt>Parâmetro</dt><dd>Número que altera o comportamento do modelo.</dd></div>
        <div><dt>Margem</dt><dd>Espaço entre a fronteira e os exemplos mais próximos das duas classes.</dd></div>
        <div><dt>Rótulo</dt><dd>Categoria conhecida atribuída a um exemplo.</dd></div>
        <div><dt>Centróide</dt><dd>Centro calculado a partir dos pontos de um grupo.</dd></div>
        <div><dt>Erro</dt><dd>Diferença entre uma referência observada e o valor previsto.</dd></div>
      </dl>
    </section>
  </div>;
}
