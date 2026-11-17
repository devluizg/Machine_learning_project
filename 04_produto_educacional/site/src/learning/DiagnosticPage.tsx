import { LessonActivitySheet } from './LessonActivitySheet';
import { lessonActivities } from './lessonActivities';

const diagnosticTableRows = [
  { dia: 1, temperatura: '24 °C', pessoas: 12, consumo: '5 unidades' },
  { dia: 2, temperatura: '26 °C', pessoas: 18, consumo: '7 unidades' },
  { dia: 3, temperatura: '28 °C', pessoas: 20, consumo: '8 unidades' },
  { dia: 4, temperatura: '30 °C', pessoas: 25, consumo: '10 unidades' },
] as const;

export function DiagnosticPage() {
  const spec = lessonActivities['diagnostico-inicial']!;

  return (
    <div className="module-page">
      <section className="module-hero">
        <div className="module-topline">
          <a className="back-link" href="#/">← Voltar ao início</a>
          <span className="pill-badge">Aula 1 · Instrumento preliminar</span>
        </div>
        <div className="module-hero-body">
          <span className="section-number">DIAGNÓSTICO INICIAL · AULA 1</span>
          <h1>Como computadores aprendem com dados</h1>
          <p>
            Este questionário <strong>não é prova</strong> e <strong>não vale nota</strong>. Responda do seu jeito,
            explicando como você pensou — não precisa saber programação nem inteligência artificial.
          </p>
        </div>
      </section>

      <div className="module-content">
        <section className="worked-card" aria-label="Tabela de apoio para as Questões 1 e 2">
          <span className="section-number">DADOS DE APOIO · QUESTÕES 1 E 2</span>
          <h3>Anotações de uma sala da escola em 4 dias</h3>
          <p>
            A escola anotou a temperatura, quantas pessoas estavam na sala e o gasto de energia em 4 dias. Use esta
            tabela para responder às Questões 1 e 2 logo abaixo.
          </p>
          <div className="table-scroll">
            <table className="activity-fill-table">
              <thead>
                <tr>
                  <th>Dia</th>
                  <th>Temperatura</th>
                  <th>Pessoas na sala</th>
                  <th>Gasto de energia</th>
                </tr>
              </thead>
              <tbody>
                {diagnosticTableRows.map((row) => (
                  <tr key={row.dia}>
                    <td className="activity-table-label">{row.dia}</td>
                    <td>{row.temperatura}</td>
                    <td>{row.pessoas}</td>
                    <td>{row.consumo}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        <LessonActivitySheet spec={spec} />
      </div>
    </div>
  );
}
