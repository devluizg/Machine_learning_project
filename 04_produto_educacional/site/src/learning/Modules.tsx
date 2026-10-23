import { useMemo, useState } from 'react';
import { controles, pontoP07, pontosBase } from '../data/regressao-linear';
import { calcularMSE, calcularResiduos, formatarNumero, prever, regressaoOLS, trainLinearGradient } from '../domain/regression';
import { assignClusters, classifyKnn, classifyLinearSvm, logisticFromWeights, logisticProbability, moveCentroids, pointDistance, predictDecisionTree, trainDecisionTree, trainLinearSvm, trainLogistic, withinClusterSumOfSquares } from './experiments';
import type { BinaryObservation, DistanceMetric, LabeledPoint, LinearSvmFit, PlanePoint, TreeNode } from './experiments';
import { QuickCheck } from './GuidedLearning';
import type { QuickCheckSpec } from './GuidedLearning';
import { LearningCurve, LossSurface3D, Plot, RangeControl } from './Visuals';

const practiceByQuestion: Record<string, { task: string; use: string; limit: string }> = {
  'Como uma reta resume uma tendência?': { task: 'Na exploração livre, inclua P07. A reta de menor erro muda? Explique por que um único ponto distante pode ter tanta influência.', use: 'Estimar uma tendência aproximadamente linear dentro da faixa observada.', limit: 'Valores atípicos e extrapolação podem distorcer previsões.' },
  'Como uma curva vira uma decisão?': { task: 'Na exploração livre, compare as classes separadas e sobrepostas. Mude só o limiar: a porcentagem mudou ou apenas a decisão?', use: 'Estimar chances de duas categorias quando existem exemplos rotulados.', limit: 'A probabilidade estimada pode estar mal calibrada; acerto no treino não garante generalização.' },
  'Como uma fronteira separa duas classes?': { task: 'Compare a fronteira escolhida por você com a sugerida pelo algoritmo. Depois inclua o ponto próximo: o que acontece com a margem?', use: 'Classificar dois conjuntos quando uma fronteira aproximadamente reta faz sentido.', limit: 'Classes sobrepostas, pontos atípicos e fronteiras curvas podem exigir outra estratégia.' },
  'Quem decide a classe de um ponto novo?': { task: 'Na exploração livre, escolha centro e borda; compare k = 1 e k = 7. Onde a decisão passa a ignorar detalhes locais?', use: 'Classificar conjuntos pequenos, quando proximidade tem significado.', limit: 'Escalas diferentes e muitos atributos podem tornar distância pouco informativa.' },
  'Como a árvore aprende perguntas a partir dos exemplos?': { task: 'Compare profundidades 0, 2 e 4. O acerto nos exemplos aumenta? Isso prova que acertará casos novos?', use: 'Explicar uma decisão por perguntas em sequência.', limit: 'Árvores profundas podem decorar os dados usados para construí-las.' },
  'Como surgem grupos sem rótulos prévios?': { task: 'Na exploração livre, comece com centros próximos e depois espalhados. Compare o caminho da WSS e os grupos finais.', use: 'Explorar padrões em dados sem categorias conhecidas.', limit: 'O número de grupos deve ser escolhido; faixas alongadas podem não combinar com centros redondos.' },
};

interface LabProps {
  question: string;
  predictionQuestion: string;
  scenario: string;
  concept: string;
  guidedAction: React.ReactNode;
  workedExample: React.ReactNode;
  quickCheck: QuickCheckSpec;
  onEnterGuided: () => void;
  formula: string;
  children: React.ReactNode;
  result: React.ReactNode;
  note: string;
  visual: React.ReactNode;
}

function Lab({ question, predictionQuestion, scenario, concept, guidedAction, workedExample, quickCheck, onEnterGuided, formula, children, result, note, visual }: LabProps) {
  const [learningMode, setLearningMode] = useState<'guiado' | 'livre'>('guiado');
  const practice = practiceByQuestion[question];
  return <>
    <div className="lab-intro"><span className="section-number">01 / ENTENDA O PROBLEMA</span><h2>{question}</h2><p>{scenario}</p><p className="concept-line"><strong>Ideia principal:</strong> {concept}</p><div className="learning-mode" role="group" aria-label="Modo de aprendizagem"><button aria-pressed={learningMode === 'guiado'} onClick={() => { if (learningMode !== 'guiado') onEnterGuided(); setLearningMode('guiado'); }} type="button">Modo aula</button><button aria-pressed={learningMode === 'livre'} onClick={() => setLearningMode('livre')} type="button">Aprofundamento opcional</button></div><p className="mode-hint">{learningMode === 'guiado' ? 'Siga apenas a ação indicada para este encontro. O aprofundamento fica disponível depois da atividade principal.' : 'Controles avançados e vistas 3D estão liberados. Voltar ao modo aula restaura o exercício obrigatório.'}</p></div>
    <div className="lab-grid">
      <section className="visual-card" aria-label="Visualização do experimento"><div className="visual-card-head"><span className="tiny-label">EXPERIMENTO VISUAL</span><span className="synthetic-badge">Dados sintéticos</span></div>{visual}</section>
      <aside className="control-card"><span className="section-number">02 / PREVEJA E EXPERIMENTE</span><h3>{learningMode === 'guiado' ? 'Faça um teste de cada vez' : 'Controle o modelo'}</h3><div className="prediction-prompt"><label htmlFor="prediction-note">Antes de alterar: {predictionQuestion}</label><textarea id="prediction-note" placeholder="Eu acho que..." rows={2} /></div>{learningMode === 'guiado' ? guidedAction : children}<div aria-live="polite" className="outcome-card"><span className="tiny-label">O QUE ACONTECEU</span>{result}</div></aside>
    </div>
    {learningMode === 'guiado' && <div className="worked-card"><span className="section-number">03 / VEJA A CONTA ACONTECER</span>{workedExample}</div>}
    <div className="learning-bottom"><section className="math-card"><span className="section-number">04 / LIGUE À MATEMÁTICA</span><div className="formula">{formula.split('•').map((expression, index) => <span className="formula-expression" key={`${question}-formula-${index}`}>{expression.trim()}</span>)}</div><p>{note}</p></section><section className="reflection-card"><span className="section-number">05 / EXPLIQUE</span><label htmlFor="student-note">O que mudou quando você alterou o controle? Explique com suas palavras.</label><textarea id="student-note" key={question} placeholder="Minha hipótese é que..." rows={3} /><small>Rascunho local: não é enviado nem salvo.</small></section></div>
    {learningMode === 'guiado' && <QuickCheck spec={quickCheck} />}
    {practice && <section className="practice-card"><span className="section-number">06 / APLIQUE E QUESTIONE</span><h3>Uma pergunta para levar adiante</h3><p>{practice.task}</p><div><p><strong>Onde ajuda:</strong> {practice.use}</p><p><strong>Onde exige cuidado:</strong> {practice.limit}</p></div></section>}
  </>;
}

export function LinearModule() {
  const [a, setA] = useState(controles.intercept.initial);
  const [b, setB] = useState(controles.slope.initial);
  const [showResiduals, setShowResiduals] = useState(false);
  const [showOutlier, setShowOutlier] = useState(false);
  const [showFit, setShowFit] = useState(false);
  const [mode, setMode] = useState<'manual' | 'treino'>('manual');
  const [step, setStep] = useState(0);
  const [rate, setRate] = useState(0.08);
  const [view3d, setView3d] = useState(false);
  const [angle, setAngle] = useState(35);
  const points = useMemo(() => showOutlier ? [...pontosBase, pontoP07] : [...pontosBase], [showOutlier]);
  const fitted = useMemo(() => regressaoOLS(points), [points]);
  const history = useMemo(() => trainLinearGradient(points, 80, rate), [points, rate]);
  const active = mode === 'treino' ? history[step]!.parameters : { a, b };
  const rows = useMemo(() => calcularResiduos(points, active), [points, active.a, active.b]);
  const mse = calcularMSE(rows);
  const selected = rows[4]!;
  const forecast = prever(active.a, active.b, 20);
  const surfaceSample = (u: number, v: number) => calcularMSE(calcularResiduos(points, { a: -1 + u * 3, b: 0.3 + v * 0.6 }));
  return <Lab onEnterGuided={() => { setA(controles.intercept.initial); setB(controles.slope.initial); setShowResiduals(false); setShowOutlier(false); setShowFit(false); setMode("manual"); setStep(0); setRate(0.08); setView3d(false); }} question="Como uma reta resume uma tendência?" scenario="Uma turma registra quantos passos uma pessoa deu e a distância percorrida. Cada ponto representa um caso do conjunto didático; queremos estimar a distância para 20 passos." concept="A reta resume a tendência dos dados para produzir uma previsão numérica, sem transformar essa previsão em uma resposta exata para todas as pessoas." predictionQuestion="se a inclinação aumentar, a previsão para 20 passos sobe ou desce?" guidedAction={<><p className="guide-instruction">Primeiro, altere somente a inclinação. Depois, veja o algoritmo ajustar a reta para reduzir o erro.</p><div className="segmented-control"><span>Quem ajusta a reta?</span><div><button aria-pressed={mode === 'manual'} onClick={() => { setMode('manual'); setView3d(false); }} type="button">Eu ajusto</button><button aria-pressed={mode === 'treino'} onClick={() => { setMode('treino'); setStep(0); setView3d(false); }} type="button">Algoritmo treina</button></div></div>{mode === 'manual' ? <RangeControl id="linear-guide-slope" label="Inclinação da reta" value={b} min={controles.slope.min} max={controles.slope.max} step={controles.slope.step} unit="m/passo" explanation="Observe a previsão para 20 passos e o erro quando a reta gira." onChange={setB} /> : <><p>O treino parte de a = 0 e b = 0. Em cada etapa, ambos mudam na direção que reduz o erro destes dados.</p><RangeControl id="linear-guide-step" label="Etapa do treino" value={step} min={0} max={80} step={1} explanation="Compare a etapa 0 com a etapa 1 e depois avance." onChange={setStep} /><button className="step-button" disabled={step === 80} onClick={() => setStep((value) => value + 1)} type="button">Avançar uma etapa</button></>}</>} workedExample={<><h3>Um ponto explica o erro</h3><p>Para 20 passos: previsão = {formatarNumero(active.a, 2)} + {formatarNumero(active.b, 3)} × 20 = <strong>{formatarNumero(forecast, 2)} m</strong>. Distância observada = {formatarNumero(selected.y, 2)} m. Diferença = {formatarNumero(selected.residual, 2)} m; quadrado da diferença = {formatarNumero(selected.squaredError, 2)} m².</p><p>O MSE é a média desses quadrados em {rows.length} pontos: {formatarNumero(mse, 3)} m². {mode === 'treino' && `Na etapa 0 era ${formatarNumero(history[0]!.mse, 3)} m²; na etapa ${step}, ${formatarNumero(history[step]!.mse, 3)} m². O treino começa no zero por escolha didática, não porque essa reta já seja boa.`}</p></>} quickCheck={{ question: 'Ao aumentar apenas a inclinação, o que acontece com a previsão para um número positivo de passos?', options: ['A previsão tende a subir.', 'O número de passos observado muda.', 'O algoritmo troca os dados usados.'], correct: 0, explanation: 'Em ŷ = a + bx, aumentar b aumenta bx quando x é positivo.', retryHint: 'Olhe a fórmula ŷ = a + bx e mantenha x = 20 passos fixo. Tente outra resposta.' }} formula={`ŷ = a + bx   •   MSE = Σ(y − ŷ)² / ${rows.length}`} note="A reta prevê uma distância para cada número de passos. O resíduo é a diferença vertical entre observado e previsto. O treino reduz o MSE passo a passo; o ajuste de referência encontra a reta de menor erro para estes mesmos pontos." result={<><strong>{formatarNumero(forecast, 2)} m</strong><p>Previsão para 20 passos; observado: {formatarNumero(selected.y, 2)} m. Resíduo: {formatarNumero(selected.residual, 2)} m. MSE atual: {formatarNumero(mse, 3)} m²; menor MSE possível aqui: {formatarNumero(fitted.mse, 3)} m².</p></>} visual={<>{view3d ? <LossSurface3D title="Paisagem do erro da reta" sample={surfaceSample} marker={[Math.max(0, Math.min(1, (active.a + 1) / 3)), Math.max(0, Math.min(1, (active.b - .3) / .6))]} angle={angle} /> : <Plot title="Passos e distância" description={`${points.length} medições. Linhas tracejadas ligam cada ponto aos eixos. Reta atual com inclinação ${formatarNumero(active.b, 3)} metro por passo. Previsão para 20 passos: ${formatarNumero(forecast, 2)} metros.`} xLabel="Número de passos" yLabel="Distância (m)" xMax={28} xTicks={[0, 4, 8, 12, 16, 20, 24, 28]} yMin={-1} yMax={18} yTicks={[0, 3, 6, 9, 12, 15, 18]}>{(x, y) => <>
    {rows.map((row) => <g aria-hidden="true" className="point-guides" key={`guide-${row.id}`}>
      <line x1={x(0)} x2={x(row.x)} y1={y(row.y)} y2={y(row.y)} />
      <line x1={x(row.x)} x2={x(row.x)} y1={y(0)} y2={y(row.y)} />
    </g>)}
    {showResiduals && rows.map((row) => <line className="residual-line" key={`r${row.id}`} x1={x(row.x)} x2={x(row.x)} y1={y(row.y)} y2={y(row.yPredicted)} />)}
    {showFit && <line className="fit-line" x1={x(0)} x2={x(28)} y1={y(fitted.parameters.a)} y2={y(prever(fitted.parameters.a, fitted.parameters.b, 28))} />}
    <line className="model-line" x1={x(0)} x2={x(28)} y1={y(active.a)} y2={y(active.a + active.b * 28)} />
    {rows.map((row) => <g aria-label={`${row.x} passos e ${formatarNumero(row.y, 1)} metros`} key={row.id}>
      <rect className="point-coordinate-bg" height={21} rx={7} width={62} x={x(row.x) + 4} y={y(row.y) - 28} />
      <circle className="point-halo" cx={x(row.x)} cy={y(row.y)} r={row.x === 20 ? 12 : 11} />
      <circle className={`data-dot ${row.id === 'P07' ? 'outlier-dot' : ''}`} cx={x(row.x)} cy={y(row.y)} r={row.x === 20 ? 8 : 7} />
      <text className="point-coordinate" x={x(row.x) + 10} y={y(row.y) - 13}>{row.x}; {formatarNumero(row.y, 1)}</text>
    </g>)}
    <g aria-label={`Previsão para 20 passos: ${formatarNumero(forecast, 2)} metros`} className="forecast-marker">
      <circle className="forecast-halo" cx={x(20)} cy={y(forecast)} r={12} />
      <circle className="forecast-dot" cx={x(20)} cy={y(forecast)} r={7} />
      <line className="forecast-leader" x1={x(20) + 7} x2={x(20) + 15} y1={y(forecast) + 7} y2={y(forecast) + 15} />
      <rect className="forecast-label-bg" height={27} rx={8} width={82} x={x(20) + 11} y={y(forecast) + 12} />
      <text className="chart-annotation" x={x(20) + 21} y={y(forecast) + 31}>previsão</text>
    </g>
  </>}</Plot>}<p className="visual-caption"><span className="legend-dot" /> medição <span className="legend-line" /> reta atual <span className="legend-ring" /> previsão para 20 passos</p>{mode === 'treino' && <LearningCurve title="Erro por etapa do treino" values={history.map((item) => item.mse)} current={step} />}<details className="chart-data"><summary>Consultar valores e erros do gráfico</summary><div className="table-scroll"><table><thead><tr><th>Passos</th><th>Observado (m)</th><th>Previsto (m)</th><th>Diferença (m)</th><th>Erro² (m²)</th></tr></thead><tbody>{rows.map((row) => <tr key={row.id}><td>{row.x}</td><td>{formatarNumero(row.y, 2)}</td><td>{formatarNumero(row.yPredicted, 2)}</td><td>{formatarNumero(row.residual, 2)}</td><td>{formatarNumero(row.squaredError, 2)}</td></tr>)}</tbody></table></div></details></>}>
    <div className="segmented-control"><span>Modo de exploração</span><div><button aria-pressed={mode === 'manual'} onClick={() => setMode('manual')} type="button">Mover reta</button><button aria-pressed={mode === 'treino'} onClick={() => setMode('treino')} type="button">Treinar reta</button></div></div>
    {mode === 'manual' ? <><RangeControl id="linear-slope" label="Inclinação da reta (b)" value={b} min={controles.slope.min} max={controles.slope.max} step={controles.slope.step} unit="m/passo" explanation="Mais inclinação aumenta a distância prevista para o mesmo número de passos." onChange={setB} /><RangeControl id="linear-intercept" label="Posição inicial (a)" value={a} min={controles.intercept.min} max={controles.intercept.max} step={controles.intercept.step} unit="m" explanation="Move a reta para cima ou para baixo sem mudar sua inclinação." onChange={setA} /></> : <><RangeControl id="linear-step" label="Etapa do treino" value={step} min={0} max={80} step={1} explanation="O algoritmo reduz o erro em pequenos passos." onChange={setStep} /><RangeControl id="linear-rate" label="Tamanho do passo" value={rate} min={0.02} max={0.2} step={0.02} explanation="Controla o quanto a reta muda em cada etapa." onChange={setRate} /></>}
    <label className="check-row"><input checked={showResiduals} onChange={(event) => setShowResiduals(event.target.checked)} type="checkbox" /> Mostrar distâncias entre pontos e reta</label>
    <label className="check-row"><input checked={showOutlier} onChange={(event) => setShowOutlier(event.target.checked)} type="checkbox" /> Incluir medição atípica P07</label>
    <label className="check-row"><input checked={showFit} onChange={(event) => setShowFit(event.target.checked)} type="checkbox" /> Comparar com ajuste de menor erro</label>
    <label className="check-row"><input checked={view3d} onChange={(event) => setView3d(event.target.checked)} type="checkbox" /> Ver paisagem do erro em 3D</label>
    {view3d && <RangeControl id="linear-angle" label="Ângulo da vista" value={angle} min={0} max={90} step={5} unit="°" explanation="Gira apenas a visualização, sem alterar os cálculos." onChange={setAngle} />}
    <button className="reset-button" onClick={() => { setA(controles.intercept.initial); setB(controles.slope.initial); setShowResiduals(false); setShowOutlier(false); setShowFit(false); setMode('manual'); setStep(0); setView3d(false); }} type="button">Recomeçar experimento</button>
  </Lab>;
}

export function LogisticModule() {
  const [xValue, setXValue] = useState(6);
  const [midpoint, setMidpoint] = useState(5);
  const [steepness, setSteepness] = useState(1);
  const [threshold, setThreshold] = useState(0.5);
  const [mode, setMode] = useState<'manual' | 'treino'>('manual');
  const [dataset, setDataset] = useState<'separado' | 'sobreposto'>('separado');
  const [step, setStep] = useState(0);
  const [view3d, setView3d] = useState(false);
  const [angle, setAngle] = useState(35);
  const observations: BinaryObservation[] = dataset === 'separado' ? [{ x: 1, label: 0 }, { x: 2, label: 0 }, { x: 3, label: 0 }, { x: 4, label: 0 }, { x: 6, label: 1 }, { x: 7, label: 1 }, { x: 8, label: 1 }, { x: 9, label: 1 }] : [{ x: 1, label: 0 }, { x: 3, label: 0 }, { x: 4, label: 1 }, { x: 5, label: 0 }, { x: 6, label: 1 }, { x: 7, label: 0 }, { x: 8, label: 1 }, { x: 9, label: 1 }];
  const heldout: BinaryObservation[] = dataset === 'separado' ? [{ x: 1.5, label: 0 }, { x: 3.5, label: 0 }, { x: 6.5, label: 1 }, { x: 8.5, label: 1 }] : [{ x: 2.5, label: 0 }, { x: 4.5, label: 1 }, { x: 6.5, label: 1 }, { x: 7.5, label: 0 }];
  const history = useMemo(() => trainLogistic(observations, 80, 0.5), [dataset]);
  const weights = history[step]!;
  const probabilityFor = (x: number) => mode === 'treino' ? logisticFromWeights(x, weights.bias, weights.weight) : logisticProbability(x, midpoint, steepness);
  const probability = probabilityFor(xValue);
  const curve = Array.from({ length: 101 }, (_, index) => ({ x: index / 10, p: probabilityFor(index / 10) }));
  const correct = observations.filter((point) => (probabilityFor(point.x) >= threshold ? 1 : 0) === point.label).length;
  const testCorrect = heldout.filter((point) => (probabilityFor(point.x) >= threshold ? 1 : 0) === point.label).length;
  const lossAt = (bias: number, weight: number) => observations.reduce((sum, point) => { const p = Math.max(1e-9, Math.min(1 - 1e-9, logisticFromWeights(point.x, bias, weight))); return sum - point.label * Math.log(p) - (1 - point.label) * Math.log(1 - p); }, 0) / observations.length;
  return <Lab onEnterGuided={() => { setXValue(6); setMidpoint(5); setSteepness(1); setThreshold(0.5); setMode("manual"); setDataset("separado"); setStep(0); setView3d(false); }} question="Como uma curva vira uma decisão?" scenario="Um sensor fictício produz uma leitura de 0 a 10. Queremos separar o estado A (normal) do estado B (alerta) usando exemplos já rotulados. Leituras sobrepostas mostram que nem sempre há separação perfeita." concept="A curva estima um valor entre 0 e 1 para B; o limiar converte esse valor em uma classe." predictionQuestion="se o limiar subir, mais casos serão classificados como A ou como B?" guidedAction={<><p className="guide-instruction">Mude só o limiar. A curva fica no mesmo lugar: apenas a regra para escolher A ou B muda.</p><RangeControl id="logistic-guide-threshold" label="Limiar para escolher B" value={threshold} min={0.2} max={0.8} step={0.05} explanation="Compare a porcentagem e a classe após cada mudança." onChange={setThreshold} /><div className="segmented-control"><span>Depois, veja o treino</span><div><button aria-pressed={mode === 'manual'} onClick={() => { setMode('manual'); setView3d(false); }} type="button">Curva manual</button><button aria-pressed={mode === 'treino'} onClick={() => { setMode('treino'); setStep(0); setView3d(false); }} type="button">Curva treinada</button></div></div>{mode === 'treino' && <><p>Etapa 0: pesos iguais a zero produzem 50% para todas as leituras. O algoritmo ajusta os pesos para reduzir a perda.</p><RangeControl id="logistic-guide-step" label="Etapa do treino" value={step} min={0} max={80} step={1} explanation="Comece comparando as etapas 0 e 1." onChange={setStep} /><button className="step-button" disabled={step === 80} onClick={() => setStep((value) => value + 1)} type="button">Avançar uma etapa</button></>}</>} workedExample={<><h3>Da curva à decisão</h3><p>Na leitura {xValue}, a curva indica {Math.round(probability * 100)}% para B. Como o limiar está em {Math.round(threshold * 100)}%, a regra escolhe <strong>{probability >= threshold ? 'B (alerta)' : 'A (normal)'}</strong>. Alterar o limiar não altera a porcentagem.</p>{mode === 'treino' ? <p>Treino: perda média na etapa 0 = {formatarNumero(history[0]!.loss, 3)}; na etapa {step} = {formatarNumero(history[step]!.loss, 3)}. Peso principal: {formatarNumero(history[0]!.weight, 3)} → {formatarNumero(history[step]!.weight, 3)}. Um passo ajusta o peso, recalcula todas as chances e compara a perda.</p> : <p>Esta curva foi posicionada manualmente: a porcentagem ilustra o cálculo, mas não é uma chance comprovada ou calibrada.</p>}</>} quickCheck={{ question: 'Se apenas o limiar passar de 50% para 70%, o que muda?', options: ['A porcentagem calculada para cada caso.', 'A classe escolhida para alguns casos, mas não a curva.', 'Os rótulos dos exemplos usados no treino.'], correct: 1, explanation: 'O limiar é a regra de decisão posterior à curva.', retryHint: 'Veja se o ponto da curva se move quando altera somente o limiar.' }} formula="p(x) = 1 / (1 + e⁻ᶻ)   •   z = b + w(x − 5)/5" note="A sigmoide transforma um valor calculado em um número entre 0 e 1. O treino ajusta b e w para reduzir a perda logarítmica nos exemplos rotulados. O limiar só muda a decisão, não a curva. A porcentagem deste exercício não deve ser tratada como probabilidade calibrada para um sensor real." result={<><strong>{Math.round(probability * 100)}%</strong><p>{mode === 'manual' ? 'Valor ilustrativo da curva manual' : 'Saída da curva treinada'} para B na leitura {xValue}; limiar {Math.round(threshold * 100)}%: <b>classe {probability >= threshold ? 'B' : 'A'}</b>.</p><p>{mode === 'treino' ? `Acertos nos 8 exemplos de treino: ${correct}/8. Casos reservados e não usados no ajuste: ${testCorrect}/${heldout.length}.` : `Correspondências nos 8 exemplos exibidos: ${correct}/8. A curva manual não foi treinada.`}</p>{mode === 'treino' && <p>Etapa {step}: perda logarítmica {formatarNumero(weights.loss, 3)}. Quatro casos reservados ilustram a diferença entre ajuste e teste; são dados inventados, não uma validação real.</p>}</>} visual={<>{view3d ? <LossSurface3D title="Paisagem da perda logística" sample={(u, v) => lossAt(-3 + u * 6, -1 + v * 7)} marker={[Math.max(0, Math.min(1, (weights.bias + 3) / 6)), Math.max(0, Math.min(1, (weights.weight + 1) / 7))]} angle={angle} /> : <Plot title="Curva sigmoide" description={`Para entrada ${xValue}, a saída da curva para B é ${Math.round(probability * 100)} por cento. ${correct} de ${observations.length} exemplos exibidos classificados corretamente.`} xLabel="Leitura do sensor (0–10)" yLabel="Saída da curva para B" xMax={10} yMax={1}>{(x, y) => <>
    <line className="threshold-line" x1={x(0)} x2={x(10)} y1={y(threshold)} y2={y(threshold)} />
    <path className="model-curve" d={curve.map((point, index) => `${index ? 'L' : 'M'}${x(point.x)},${y(point.p)}`).join(' ')} />
    <line className="probe-line" x1={x(xValue)} x2={x(xValue)} y1={y(0)} y2={y(probability)} />
    {observations.map((point, index) => <circle key={index} className={`class-dot ${point.label === 0 ? 'class-a' : 'class-b'}`} cx={x(point.x)} cy={y(point.label ? .96 : .04)} r={5} />)}
    <circle className="forecast-dot" cx={x(xValue)} cy={y(probability)} r={9} /><text className="chart-annotation" x={x(xValue) + 12} y={y(probability) - 12}>{Math.round(probability * 100)}%</text>
  </>}</Plot>}<p className="visual-caption"><span className="legend-line" /> saída da curva <span className="legend-dash" /> limiar <span className="legend-dot class-a" /> A <span className="legend-dot class-b" /> B</p>{mode === 'treino' && <LearningCurve title="Perda por etapa do treino" values={history.map((item) => item.loss)} current={step} />}<details className="chart-data"><summary>Consultar exemplos de treino e casos reservados</summary><div className="table-scroll"><table><thead><tr><th>Conjunto</th><th>Leitura</th><th>Etiqueta</th><th>Escolha da curva</th></tr></thead><tbody>{observations.map((point, index) => <tr key={`treino-${index}`}><td>Treino</td><td>{point.x}</td><td>{point.label ? 'B' : 'A'}</td><td>{probabilityFor(point.x) >= threshold ? 'B' : 'A'}</td></tr>)}{heldout.map((point, index) => <tr key={`teste-${index}`}><td>Reservado</td><td>{point.x}</td><td>{point.label ? 'B' : 'A'}</td><td>{probabilityFor(point.x) >= threshold ? 'B' : 'A'}</td></tr>)}</tbody></table></div></details></>}> 
    <div className="segmented-control"><span>Dados de aprendizagem</span><div><button aria-pressed={dataset === 'separado'} onClick={() => setDataset('separado')} type="button">Classes separadas</button><button aria-pressed={dataset === 'sobreposto'} onClick={() => setDataset('sobreposto')} type="button">Classes sobrepostas</button></div></div>
    <div className="segmented-control"><span>Modo de exploração</span><div><button aria-pressed={mode === 'manual'} onClick={() => setMode('manual')} type="button">Mover curva</button><button aria-pressed={mode === 'treino'} onClick={() => setMode('treino')} type="button">Treinar curva</button></div></div>
    <RangeControl id="logistic-x" label="Valor de entrada" value={xValue} min={0} max={10} step={0.5} explanation="Percorra a curva: o ponto mostra a probabilidade para esse valor." onChange={setXValue} />
    <RangeControl id="logistic-threshold" label="Limiar de decisão" value={threshold} min={0.2} max={0.8} step={0.05} explanation="Muda a classe escolhida sem alterar a curva de probabilidades." onChange={setThreshold} />
    {mode === 'manual' ? <><RangeControl id="logistic-mid" label="Ponto central (m)" value={midpoint} min={2} max={8} step={0.5} explanation="Desloca o ponto em que a probabilidade chega a 50%." onChange={setMidpoint} /><RangeControl id="logistic-steep" label="Inclinação da transição (k)" value={steepness} min={0.5} max={2} step={0.25} explanation="Controla quão rápida é a passagem de A para B." onChange={setSteepness} /></> : <RangeControl id="logistic-step" label="Etapa do treino" value={step} min={0} max={80} step={1} explanation="Cada etapa atualiza os pesos para reduzir a perda logarítmica." onChange={setStep} />}
    <label className="check-row"><input checked={view3d} onChange={(event) => { setView3d(event.target.checked); if (event.target.checked) setMode('treino'); }} type="checkbox" /> Ver perda do treino em 3D</label>
    {view3d && <RangeControl id="logistic-angle" label="Ângulo da vista" value={angle} min={0} max={90} step={5} unit="°" explanation="Gira apenas a visualização da perda." onChange={setAngle} />}
  </Lab>;
}

const knnPoints: readonly LabeledPoint[] = [
  { id: 'A1', x: 1.2, y: 2, label: 'A' }, { id: 'A2', x: 2.1, y: 3.2, label: 'A' }, { id: 'A3', x: 3, y: 1.7, label: 'A' }, { id: 'A4', x: 3.3, y: 4.1, label: 'A' }, { id: 'A5', x: 4.1, y: 2.7, label: 'A' },
  { id: 'B1', x: 5.7, y: 7.2, label: 'B' }, { id: 'B2', x: 6.8, y: 6, label: 'B' }, { id: 'B3', x: 7.6, y: 8.1, label: 'B' }, { id: 'B4', x: 8.2, y: 5.8, label: 'B' }, { id: 'B5', x: 6, y: 4.2, label: 'B' },
];
const knnRingPoints: readonly LabeledPoint[] = [
  { id: 'A1', x: 4.1, y: 4.1, label: 'A' }, { id: 'A2', x: 5, y: 3.8, label: 'A' }, { id: 'A3', x: 5.9, y: 4.5, label: 'A' }, { id: 'A4', x: 4.4, y: 5.7, label: 'A' }, { id: 'A5', x: 5.7, y: 5.8, label: 'A' },
  { id: 'B1', x: 1.3, y: 5, label: 'B' }, { id: 'B2', x: 3, y: 8.1, label: 'B' }, { id: 'B3', x: 6.9, y: 8.2, label: 'B' }, { id: 'B4', x: 8.6, y: 5.3, label: 'B' }, { id: 'B5', x: 7.2, y: 1.8, label: 'B' }, { id: 'B6', x: 2.7, y: 1.9, label: 'B' },
];

export function KnnModule() {
  const [k, setK] = useState(3);
  const [targetX, setTargetX] = useState(5);
  const [targetY, setTargetY] = useState(5);
  const [metric, setMetric] = useState<DistanceMetric>('euclidean');
  const [weighted, setWeighted] = useState(false);
  const [dataset, setDataset] = useState<'ilhas' | 'anel'>('ilhas');
  const [showRegions, setShowRegions] = useState(false);
  const [view3d, setView3d] = useState(false);
  const [angle, setAngle] = useState(35);
  const points = dataset === 'ilhas' ? knnPoints : knnRingPoints;
  const target = { id: 'novo', x: targetX, y: targetY };
  const result = classifyKnn(points, target, k, metric, weighted);
  const neighborIds = new Set(result.neighbors.map((point) => point.id));
  const cells = showRegions ? Array.from({ length: 20 * 20 }, (_, index) => { const cx = index % 20 * .5 + .25; const cy = Math.floor(index / 20) * .5 + .25; return { id: index, cx, cy, label: classifyKnn(points, { id: 'grade', x: cx, y: cy }, k, metric, weighted).label }; }) : [];
  return <Lab onEnterGuided={() => { setK(3); setTargetX(5); setTargetY(5); setMetric("euclidean"); setWeighted(false); setDataset("ilhas"); setShowRegions(false); setView3d(false); }} question="Quem decide a classe de um ponto novo?" scenario="Imagine amostras fictícias descritas por doçura e acidez, cada uma de 0 a 10. Exemplos conhecidos receberam etiqueta A ou B. Para uma nova amostra, perguntamos quais exemplos estão mais perto; as etiquetas são apenas didáticas." concept="k-NN guarda os exemplos e decide pelo voto dos k mais próximos; não ajusta pesos em um treino." predictionQuestion="se k aumentar, os vizinhos adicionais podem mudar a votação?" guidedAction={<><p className="guide-instruction">O ponto com ? é novo. Mude apenas k e conte os vizinhos destacados antes de ler a classe prevista.</p><RangeControl id="knn-guide-k" label="Quantos vizinhos votam? (k)" value={k} min={1} max={7} step={2} explanation="De 1 a 7 exemplos participam da decisão." onChange={setK} /></>} workedExample={<><h3>Uma distância e uma votação</h3><p>O vizinho mais próximo é {result.neighbors[0]!.id}, classe {result.neighbors[0]!.label}. Diferenças para o ponto novo: |{formatarNumero(targetX, 1)} − {formatarNumero(result.neighbors[0]!.x, 1)}| na doçura e |{formatarNumero(targetY, 1)} − {formatarNumero(result.neighbors[0]!.y, 1)}| na acidez. Distância {metric === 'euclidean' ? 'em linha reta' : 'em quadras'} = {formatarNumero(result.neighbors[0]!.distance, 2)}.</p><p>Entre {k} vizinhos, A recebe {result.votesA} voto(s) e B recebe {result.votesB}. Não houve uma fase de ajuste: a decisão foi calculada agora, a partir dos exemplos guardados. Como as duas medidas usam a mesma escala de 0 a 10, nenhuma domina só pela unidade.</p></>} quickCheck={{ question: 'O que acontece quando chega uma nova amostra no k-NN?', options: ['O algoritmo reajusta pesos por 80 etapas.', 'Ele mede distâncias aos exemplos guardados e reúne os votos.', 'Ele escolhe centróides para grupos sem rótulo.'], correct: 1, explanation: 'Aqui a decisão é feita ao consultar os exemplos, sem treinamento de parâmetros.', retryHint: 'Observe as linhas que ligam o ponto ? aos vizinhos destacados.' }} formula={metric === 'euclidean' ? 'd = √[(x₁ − x₂)² + (y₁ − y₂)²]' : 'd = |x₁ − x₂| + |y₁ − y₂|'} note="k-NN não ajusta pesos durante um treino: guarda os exemplos e calcula distâncias quando chega um ponto novo. O voto pode ser simples ou dar mais peso a vizinhos próximos. As regiões mostram a decisão em muitas posições do plano. Se as duas características tiverem unidades muito diferentes, precisam ser comparadas em escalas adequadas." result={<><strong>Classe {result.label}</strong><p>Entre os {k} vizinhos: {result.votesA} voto(s) A e {result.votesB} voto(s) B. {weighted && `Pesos somados: A ${formatarNumero(result.scoreA, 2)}, B ${formatarNumero(result.scoreB, 2)}.`}</p><p>Vizinhos: {result.neighbors.map((point) => `${point.id} (${point.label}; d=${formatarNumero(point.distance, 1)})`).join(', ')}.</p></>} visual={<>{view3d ? <LossSurface3D title="Força local do voto B" sample={(u, v) => { const vote = classifyKnn(points, { id: 'mapa', x: u * 10, y: v * 10 }, k, metric, weighted); return vote.scoreB / (vote.scoreA + vote.scoreB); }} marker={[targetX / 10, targetY / 10]} angle={angle} xLabel="doçura" yLabel="acidez" zLabel="voto B" explanation="A altura é a fração do voto para B no local, não um atributo adicional." /> : <Plot title="Vizinhos mais próximos" description={`Ponto novo em ${targetX}, ${targetY}. Os ${k} vizinhos mais próximos votam em classe ${result.label}. Distância ${metric === 'euclidean' ? 'euclidiana' : 'Manhattan'}.`} xLabel="Doçura (0–10)" yLabel="Acidez (0–10)" xMax={10} yMax={10}>{(x, y) => <>
    {cells.map((cell) => <rect key={cell.id} className={`decision-cell ${cell.label === 'A' ? 'decision-a' : 'decision-b'}`} x={x(cell.cx - .25)} y={y(cell.cy + .25)} width={x(.5) - x(0)} height={y(0) - y(.5)} />)}
    {result.neighbors.map((point) => <line className="neighbor-line" key={`l${point.id}`} x1={x(targetX)} x2={x(point.x)} y1={y(targetY)} y2={y(point.y)} />)}
    {points.map((point) => <g key={point.id}><circle className={`class-dot ${point.label === 'A' ? 'class-a' : 'class-b'} ${neighborIds.has(point.id) ? 'chosen-neighbor' : ''}`} cx={x(point.x)} cy={y(point.y)} r={neighborIds.has(point.id) ? 10 : 8} /><text className="point-label" x={x(point.x) + 12} y={y(point.y) - 8}>{point.id}</text></g>)}
    <circle className="query-dot" cx={x(targetX)} cy={y(targetY)} r={12} /><text className="query-label" textAnchor="middle" x={x(targetX)} y={y(targetY) + 5}>?</text>
  </>}</Plot>}<p className="visual-caption"><span className="legend-dot class-a" /> classe A <span className="legend-dot class-b" /> classe B <span className="legend-ring" /> ponto novo</p><details className="chart-data"><summary>Consultar posições e vizinhos por texto</summary><div className="table-scroll"><table><thead><tr><th>Exemplo</th><th>Doçura</th><th>Acidez</th><th>Classe</th><th>Distância ao novo</th></tr></thead><tbody>{points.map((point) => <tr key={point.id}><td>{point.id}{neighborIds.has(point.id) ? ' · vizinho' : ''}</td><td>{formatarNumero(point.x, 1)}</td><td>{formatarNumero(point.y, 1)}</td><td>{point.label}</td><td>{formatarNumero(pointDistance(point, target, metric), 2)}</td></tr>)}</tbody></table></div></details></>}> 
    <div className="segmented-control"><span>Distribuição dos exemplos</span><div><button aria-pressed={dataset === 'ilhas'} onClick={() => setDataset('ilhas')} type="button">Dois conjuntos</button><button aria-pressed={dataset === 'anel'} onClick={() => setDataset('anel')} type="button">Centro e borda</button></div></div>
    <RangeControl id="knn-k" label="Número de vizinhos (k)" value={k} min={1} max={7} step={2} explanation="Observe se a votação muda quando mais vizinhos participam." onChange={setK} />
    <div className="segmented-control"><span>Como medir distância?</span><div><button aria-pressed={metric === 'euclidean'} onClick={() => setMetric('euclidean')} type="button">Linha reta</button><button aria-pressed={metric === 'manhattan'} onClick={() => setMetric('manhattan')} type="button">Em quadras</button></div></div>
    <label className="check-row"><input checked={weighted} onChange={(event) => setWeighted(event.target.checked)} type="checkbox" /> Dar mais peso aos vizinhos próximos</label>
    <label className="check-row"><input checked={showRegions} onChange={(event) => setShowRegions(event.target.checked)} type="checkbox" /> Mostrar regiões de decisão</label>
    <label className="check-row"><input checked={view3d} onChange={(event) => setView3d(event.target.checked)} type="checkbox" /> Ver força do voto em 3D</label>
    {view3d && <RangeControl id="knn-angle" label="Ângulo da vista" value={angle} min={0} max={90} step={5} unit="°" explanation="Gira apenas o gráfico; vizinhos e votos não mudam." onChange={setAngle} />}
    <RangeControl id="knn-x" label="Posição horizontal do ponto novo" value={targetX} min={1} max={9} step={0.5} explanation="Mova o ponto sem alterar os exemplos conhecidos." onChange={setTargetX} />
    <RangeControl id="knn-y" label="Posição vertical do ponto novo" value={targetY} min={1} max={9} step={0.5} explanation="A distância considera as duas características." onChange={setTargetY} />
  </Lab>;
}

const treePoints: readonly LabeledPoint[] = [
  { id: '1', x: 1, y: 1, label: 'A' }, { id: '2', x: 2, y: 2, label: 'A' }, { id: '3', x: 2, y: 4, label: 'A' }, { id: '4', x: 3, y: 3, label: 'A' },
  { id: '5', x: 4, y: 1, label: 'A' }, { id: '6', x: 4, y: 7, label: 'B' }, { id: '7', x: 5, y: 8, label: 'B' }, { id: '8', x: 6, y: 7, label: 'B' },
  { id: '9', x: 7, y: 8, label: 'B' }, { id: '10', x: 8, y: 6, label: 'B' }, { id: '11', x: 8, y: 2, label: 'A' }, { id: '12', x: 9, y: 3, label: 'A' },
  { id: '13', x: 7, y: 2, label: 'A' }, { id: '14', x: 6, y: 3, label: 'B' }, { id: '15', x: 5, y: 4, label: 'B' }, { id: '16', x: 3, y: 8, label: 'B' },
];

function TreeOutline({ node, target, onPath = true, depth = 0 }: { node: TreeNode; target?: PlanePoint; onPath?: boolean; depth?: number }) {
  const rule = node.axis && node.threshold !== undefined ? `${node.axis === 'x' ? 'Horizontal' : 'Vertical'} < ${formatarNumero(node.threshold, 1)}?` : `Classe ${node.label}`;
  const goesLeft = target && node.axis && node.threshold !== undefined ? target[node.axis] < node.threshold : false;
  return <li className={target && onPath ? 'tree-active-node' : ''}><span>{rule} <small>({node.count} exemplos, impureza {formatarNumero(node.gini, 2)})</small></span>{node.left && node.right && depth < 4 && <ul><TreeOutline node={node.left} target={target} onPath={onPath && goesLeft} depth={depth + 1} /><TreeOutline node={node.right} target={target} onPath={onPath && !goesLeft} depth={depth + 1} /></ul>}</li>;
}

export function TreeModule() {
  const [depth, setDepth] = useState(2);
  const [targetX, setTargetX] = useState(5);
  const [targetY, setTargetY] = useState(5);
  const [showRegions, setShowRegions] = useState(true);
  const [view3d, setView3d] = useState(false);
  const [angle, setAngle] = useState(35);
  const tree = useMemo(() => trainDecisionTree(treePoints, depth), [depth]);
  const outcome = predictDecisionTree(tree, { id: 'novo', x: targetX, y: targetY });
  const cells = showRegions ? Array.from({ length: 20 * 20 }, (_, index) => { const cx = index % 20 * .5 + .25; const cy = Math.floor(index / 20) * .5 + .25; return { id: index, cx, cy, label: predictDecisionTree(tree, { id: 'grade', x: cx, y: cy }).label }; }) : [];
  const correct = treePoints.filter((point) => predictDecisionTree(tree, point).label === point.label).length;
  const heldout: readonly LabeledPoint[] = [{ id: 'T1', x: 1.5, y: 1.5, label: 'A' }, { id: 'T2', x: 5.5, y: 7.5, label: 'B' }, { id: 'T3', x: 8.5, y: 2.5, label: 'A' }, { id: 'T4', x: 5.5, y: 3.5, label: 'B' }];
  const testCorrect = heldout.filter((point) => predictDecisionTree(tree, point).label === point.label).length;
  const afterSplit = tree.left && tree.right ? (tree.left.count * tree.left.gini + tree.right.count * tree.right.gini) / tree.count : tree.gini;
  return <Lab onEnterGuided={() => { setDepth(2); setTargetX(5); setTargetY(5); setShowRegions(true); setView3d(false); }} question="Como a árvore aprende perguntas a partir dos exemplos?" scenario="Objetos fictícios têm duas medidas de 0 a 10: largura e altura. Alguns foram etiquetados A ou B. A árvore cria perguntas como ‘largura menor que um limite?’ para separar as etiquetas." concept="Treinar a árvore é escolher divisões que deixam os grupos menos misturados; usar a árvore é seguir um caminho de perguntas." predictionQuestion="ao permitir mais divisões, as regiões ficarão mais simples ou mais detalhadas?" guidedAction={<><p className="guide-instruction">Permita primeiro nenhuma pergunta e depois uma ou duas. Observe as regiões e a regra que surge.</p><RangeControl id="tree-guide-depth" label="Máximo de perguntas em sequência" value={depth} min={0} max={4} step={1} explanation="Aumentar a profundidade pode criar regiões mais detalhadas." onChange={setDepth} /></>} workedExample={<><h3>Veja a primeira pergunta aprendida</h3><p>Na raiz há {tree.countA} exemplos A e {tree.countB} B. Mistura inicial (Gini): {formatarNumero(tree.gini, 2)}. {tree.axis ? `A árvore escolheu ${tree.axis === 'x' ? 'largura' : 'altura'} < ${formatarNumero(tree.threshold!, 1)}; a mistura média dos dois lados caiu para ${formatarNumero(afterSplit, 2)}.` : 'Sem divisões permitidas, ela só pode escolher a classe mais frequente.'}</p><p>Para o ponto novo ({targetX}; {targetY}), siga as regras destacadas até a classe {outcome.label}:</p><ul className="tree-outline tree-guided"><TreeOutline node={tree} target={{ id: 'novo', x: targetX, y: targetY }} /></ul><p>Ramo de cima = “sim”; ramo de baixo = “não”. A linha realçada é o caminho do ponto novo.</p></>} quickCheck={{ question: 'O que significa permitir mais profundidade?', options: ['A árvore poderá fazer mais perguntas em sequência.', 'Os valores dos exemplos serão apagados.', 'O acerto nos dados novos estará garantido.'], correct: 0, explanation: 'Mais profundidade permite regras específicas, mas não garante acerto fora dos dados usados no treino.', retryHint: 'Compare o número de ramos e as regiões quando a profundidade muda.' }} formula="Gini = 1 − p(A)² − p(B)²" note="Em cada divisão, a árvore escolhe um limite que reduz a mistura de classes (impureza de Gini). Profundidade maior permite regras mais específicas, mas pode decorar os exemplos. Treino e teste usam pontos diferentes neste exercício sintético." result={<><strong>Classe {outcome.label}</strong><p>Caminho: {outcome.path.length ? outcome.path.join(' → ') : 'Sem divisão: classe majoritária'}. Folha com {outcome.leaf.count} exemplos.</p><p>Acertos nos {treePoints.length} pontos de treino: {correct}/{treePoints.length}. Acertos em 4 casos reservados, não usados na construção: {testCorrect}/4. Isto ilustra generalização; não a comprova.</p></>} visual={<>{view3d ? <LossSurface3D title="Altura da proporção B por região" sample={(u, v) => { const leaf = predictDecisionTree(tree, { id: 'mapa', x: u * 10, y: v * 10 }).leaf; return leaf.countB / leaf.count; }} marker={[targetX / 10, targetY / 10]} angle={angle} xLabel="largura" yLabel="altura" zLabel="fração B" explanation="Cada patamar é a proporção de exemplos B na folha correspondente; não é uma probabilidade calibrada." /> : <Plot title="Regiões aprendidas pela árvore" description={`Árvore com profundidade máxima ${depth}. Ponto novo em ${targetX}, ${targetY}, classificado como ${outcome.label}. ${correct} de ${treePoints.length} exemplos de treino classificados corretamente.`} xLabel="Largura (0–10)" yLabel="Altura (0–10)" xMax={10} yMax={10}>{(x, y) => <>
    {cells.map((cell) => <rect key={cell.id} className={`decision-cell ${cell.label === 'A' ? 'decision-a' : 'decision-b'}`} x={x(cell.cx - .25)} y={y(cell.cy + .25)} width={x(.5) - x(0)} height={y(0) - y(.5)} />)}
    {treePoints.map((point) => <circle key={point.id} className={`class-dot ${point.label === 'A' ? 'class-a' : 'class-b'}`} cx={x(point.x)} cy={y(point.y)} r={8} />)}
    <circle className="query-dot" cx={x(targetX)} cy={y(targetY)} r={11} /><text className="query-label" textAnchor="middle" x={x(targetX)} y={y(targetY) + 5}>?</text>
  </>}</Plot>}<p className="visual-caption"><span className="legend-dot class-a" /> classe A <span className="legend-dot class-b" /> classe B <span className="legend-ring" /> ponto novo</p><details className="chart-data"><summary>Ver as regras aprendidas</summary><ul className="tree-outline"><TreeOutline node={tree} target={{ id: 'novo', x: targetX, y: targetY }} /></ul><p>Em cada pergunta, o primeiro ramo representa “sim”; o segundo, “não”.</p></details><details className="chart-data"><summary>Consultar casos de treino e reservados</summary><div className="table-scroll"><table><thead><tr><th>Conjunto</th><th>Largura</th><th>Altura</th><th>Etiqueta</th><th>Escolha da árvore</th></tr></thead><tbody>{[...treePoints.map((point) => ({ ...point, set: 'Treino' })), ...heldout.map((point) => ({ ...point, set: 'Reservado' }))].map((point) => <tr key={point.id}><td>{point.set}</td><td>{point.x}</td><td>{point.y}</td><td>{point.label}</td><td>{predictDecisionTree(tree, point).label}</td></tr>)}</tbody></table></div></details></>}> 
    <RangeControl id="tree-depth" label="Máximo de perguntas em sequência" value={depth} min={0} max={4} step={1} explanation="Aumentar a profundidade permite divisões adicionais dos dados." onChange={setDepth} />
    <RangeControl id="tree-x" label="Posição horizontal do caso novo" value={targetX} min={0} max={10} step={0.5} explanation="Veja quais regras o caso percorre." onChange={setTargetX} />
    <RangeControl id="tree-y" label="Posição vertical do caso novo" value={targetY} min={0} max={10} step={0.5} explanation="Mudar esta característica pode alterar o ramo." onChange={setTargetY} />
    <label className="check-row"><input checked={showRegions} onChange={(event) => setShowRegions(event.target.checked)} type="checkbox" /> Mostrar regiões aprendidas</label>
    <label className="check-row"><input checked={view3d} onChange={(event) => setView3d(event.target.checked)} type="checkbox" /> Ver patamares da árvore em 3D</label>
    {view3d && <RangeControl id="tree-angle" label="Ângulo da vista" value={angle} min={0} max={90} step={5} unit="°" explanation="Gira apenas a visualização das regiões." onChange={setAngle} />}
    <div className="decision-path"><span className="tiny-label">CAMINHO ATIVO</span>{outcome.path.map((item, index) => <span key={index}>{item}</span>)}</div>
  </Lab>;
}

const clusterPoints: readonly PlanePoint[] = [
  { id: 'P1', x: 1.1, y: 2.1 }, { id: 'P2', x: 1.9, y: 3 }, { id: 'P3', x: 2.7, y: 1.7 }, { id: 'P4', x: 3.1, y: 3.3 },
  { id: 'P5', x: 4.4, y: 7.2 }, { id: 'P6', x: 5.1, y: 8.1 }, { id: 'P7', x: 5.8, y: 6.8 }, { id: 'P8', x: 6.1, y: 8.4 },
  { id: 'P9', x: 7.3, y: 2.2 }, { id: 'P10', x: 8.2, y: 3.1 }, { id: 'P11', x: 8.6, y: 1.8 }, { id: 'P12', x: 7.5, y: 3.8 },
];

function initialCentroids(k: number): PlanePoint[] {
  return k === 2 ? [{ id: 'C1', x: 2, y: 5 }, { id: 'C2', x: 8, y: 5 }] : [{ id: 'C1', x: 1.5, y: 4.5 }, { id: 'C2', x: 5, y: 9 }, { id: 'C3', x: 8.5, y: 4.5 }];
}

export function KmeansModule() {
  const [k, setK] = useState(3);
  const [shape, setShape] = useState<'ilhas' | 'faixa'>('ilhas');
  const [start, setStart] = useState<'separado' | 'proximo'>('separado');
  const [view3d, setView3d] = useState(false);
  const [angle, setAngle] = useState(35);
  const [centroids, setCentroids] = useState<PlanePoint[]>(() => initialCentroids(3));
  const [phase, setPhase] = useState<'initial' | 'assigned' | 'moved'>('initial');
  const [round, setRound] = useState(0);
  const [wssHistory, setWssHistory] = useState<number[]>([]);
  const [changedGroups, setChangedGroups] = useState<number | null>(null);
  const points = shape === 'ilhas' ? clusterPoints : clusterPoints.map((point) => ({ ...point, x: 1 + point.x * .85, y: 2 + .35 * point.x + (point.y - 5) * .4 }));
  const assignments = assignClusters(points, centroids);
  const wss = withinClusterSumOfSquares(assignments);
  const showGroups = phase === 'assigned';
  const firstGroup = assignments.filter((point) => point.cluster === 0);
  const firstMean = firstGroup.length ? { x: firstGroup.reduce((sum, point) => sum + point.x, 0) / firstGroup.length, y: firstGroup.reduce((sum, point) => sum + point.y, 0) / firstGroup.length } : null;
  function nextStep() {
    if (phase === 'assigned') { const next = moveCentroids(assignments, centroids); const reassigned = assignClusters(points, next); setChangedGroups(reassigned.filter((point, index) => point.cluster !== assignments[index]!.cluster).length); setCentroids(next); setWssHistory([...wssHistory, withinClusterSumOfSquares(reassigned)]); setPhase('moved'); setRound(round + 1); }
    else { setWssHistory(wssHistory.length ? wssHistory : [wss]); setPhase('assigned'); }
  }
  function reset(value = k, nextShape = shape, nextStart = start) { setK(value); setShape(nextShape); setStart(nextStart); setCentroids(nextStart === 'proximo' ? value === 2 ? [{ id: 'C1', x: 1.5, y: 2 }, { id: 'C2', x: 2.5, y: 2.5 }] : [{ id: 'C1', x: 1.5, y: 2 }, { id: 'C2', x: 2.5, y: 2.5 }, { id: 'C3', x: 3, y: 3 }] : initialCentroids(value)); setPhase('initial'); setRound(0); setWssHistory([]); setChangedGroups(null); }
  return <Lab onEnterGuided={() => { reset(3, "ilhas", "separado"); setView3d(false); }} question="Como surgem grupos sem rótulos prévios?" scenario="Imagine amostras fictícias medidas por doçura e acidez (0 a 10), sem etiquetas A ou B. Queremos apenas descobrir conjuntos de pontos parecidos; o algoritmo não sabe o significado real de cada grupo." concept="k-means alterna duas ações: aproximar cada ponto de um centro e mover cada centro para a média dos pontos atribuídos." predictionQuestion="depois de mover os centróides, algum ponto pode mudar de grupo na próxima atribuição?" guidedAction={<><p className="guide-instruction">Clique uma vez para atribuir os pontos. Observe as linhas. Clique de novo para mover os centros. Repita e compare.</p><button className="primary-button" onClick={nextStep} type="button">{phase === 'assigned' ? 'Mover centróides para as médias' : 'Atribuir pontos aos centros'} <span aria-hidden="true">→</span></button><button className="reset-button" onClick={() => reset()} type="button">Reiniciar agrupamento</button></>} workedExample={<><h3>Calcule um centro com os pontos</h3><p>{firstGroup.length ? `O grupo do centro 1 recebe ${firstGroup.length} ponto(s): ${firstGroup.map((point) => point.id).join(', ')}. A média horizontal é ${formatarNumero(firstMean!.x, 2)}; a vertical é ${formatarNumero(firstMean!.y, 2)}. Ao clicar em “Mover centróides”, o centro 1 vai para essas médias.` : 'O centro 1 ficou sem pontos; nesse caso, ele permanece onde estava.'}</p><p>WSS atual = {formatarNumero(wss, 1)}, soma dos quadrados das distâncias de cada ponto ao seu centro. {changedGroups !== null && `Após o último movimento, ${changedGroups} ponto(s) mudaria(m) de grupo na nova atribuição.`} Quando os grupos e centros param de mudar, o processo estabiliza neste exemplo; isso não garante que os grupos tenham significado fora dele.</p></>} quickCheck={{ question: 'Depois de atribuir pontos aos centros, como cada centro se move?', options: ['Para a média das posições dos pontos do seu grupo.', 'Para a posição do ponto mais distante.', 'Para uma etiqueta A ou B já conhecida.'], correct: 0, explanation: 'O centro é atualizado pela média das coordenadas do grupo atribuído.', retryHint: 'Consulte a conta do centro 1 logo acima e tente novamente.' }} formula="centro do grupo = média das posições   •   WSS = Σ distância²" note="Cada ponto vai ao centro mais próximo; cada centro se move para a média do seu grupo. A soma das distâncias ao quadrado (WSS) mede quão compactos os grupos ficam. Mais grupos ou outra posição inicial podem mudar o resultado; WSS menor, sozinha, não prova agrupamento melhor." result={<><strong>{k} grupos</strong><p>{phase === 'initial' ? 'Comece atribuindo cada ponto ao centróide mais próximo.' : phase === 'assigned' ? 'Pontos atribuídos. Agora mova os centróides para a média de cada grupo.' : `Centróides movidos na rodada ${round}. Atribua novamente para ver se algum ponto troca de grupo.`}</p><p>WSS atual: {formatarNumero(wss, 1)}. {showGroups && centroids.map((centroid, index) => `${centroid.id}: ${assignments.filter((point) => point.cluster === index).length} ponto(s)`).join(' · ')}</p>{changedGroups !== null && <p>Trocas previstas após a última atualização: {changedGroups}. {changedGroups === 0 ? 'Nenhum ponto trocou de grupo; confira se novos movimentos ainda alteram os centros.' : 'Outra rodada pode redistribuir os pontos.'}</p>}</>} visual={<>{view3d ? <LossSurface3D title="Distância até o centro mais próximo" sample={(u, v) => Math.min(...centroids.map((center) => (u * 10 - center.x) ** 2 + (v * 10 - center.y) ** 2))} marker={[points[0]!.x / 10, points[0]!.y / 10]} angle={angle} xLabel="doçura" yLabel="acidez" zLabel="distância²" explanation="Os vales indicam posições dos centróides. A altura não é uma terceira característica dos pontos." /> : <Plot title="Agrupamento k-means" description={`${k} centróides e 12 pontos sem rótulo. Estado: ${phase === 'assigned' ? 'pontos atribuídos' : phase === 'moved' ? 'centróides atualizados' : 'inicial'}. Rodadas completas: ${round}. WSS ${formatarNumero(wss, 1)}.`} xLabel="Doçura (0–10)" yLabel="Acidez (0–10)" xMax={10} yMax={10}>{(x, y) => <>
    {showGroups && assignments.map((point) => <line className={`cluster-link cluster-${point.cluster}`} key={`l${point.id}`} x1={x(point.x)} x2={x(centroids[point.cluster]!.x)} y1={y(point.y)} y2={y(centroids[point.cluster]!.y)} />)}
    {assignments.map((point) => <circle className={`cluster-point ${showGroups ? `cluster-${point.cluster}` : ''}`} cx={x(point.x)} cy={y(point.y)} key={point.id} r={8} />)}
    {centroids.map((centroid, index) => <g key={centroid.id}><circle className={`centroid centroid-${index}`} cx={x(centroid.x)} cy={y(centroid.y)} r={15} /><text className="centroid-label" textAnchor="middle" x={x(centroid.x)} y={y(centroid.y) + 5}>{index + 1}</text></g>)}
  </>}</Plot>}<p className="visual-caption">Círculos grandes numerados são centróides; as linhas aparecem na etapa de atribuição.</p>{wssHistory.length > 1 && <LearningCurve title="Compactação por rodada (WSS)" values={wssHistory} current={wssHistory.length - 1} />}<details className="chart-data"><summary>Consultar pontos e grupos por texto</summary><div className="table-scroll"><table><thead><tr><th>Ponto</th><th>Doçura</th><th>Acidez</th><th>Centro mais próximo</th><th>Distância</th></tr></thead><tbody>{assignments.map((point) => <tr key={point.id}><td>{point.id}</td><td>{formatarNumero(point.x, 1)}</td><td>{formatarNumero(point.y, 1)}</td><td>{centroids[point.cluster]!.id}</td><td>{formatarNumero(point.distance, 2)}</td></tr>)}</tbody></table></div></details></>}> 
    <div className="segmented-control" aria-label="Quantidade de grupos"><span>Número de grupos (k)</span><div><button aria-pressed={k === 2} onClick={() => reset(2)} type="button">2 grupos</button><button aria-pressed={k === 3} onClick={() => reset(3)} type="button">3 grupos</button></div></div>
    <div className="segmented-control"><span>Forma dos dados</span><div><button aria-pressed={shape === 'ilhas'} onClick={() => reset(k, 'ilhas')} type="button">Ilhas</button><button aria-pressed={shape === 'faixa'} onClick={() => reset(k, 'faixa')} type="button">Faixa inclinada</button></div></div>
    <div className="segmented-control"><span>Posição inicial dos centros</span><div><button aria-pressed={start === 'separado'} onClick={() => reset(k, shape, 'separado')} type="button">Espalhados</button><button aria-pressed={start === 'proximo'} onClick={() => reset(k, shape, 'proximo')} type="button">Próximos</button></div></div>
    <label className="check-row"><input checked={view3d} onChange={(event) => setView3d(event.target.checked)} type="checkbox" /> Ver distância aos centros em 3D</label>
    {view3d && <RangeControl id="kmeans-angle" label="Ângulo da vista" value={angle} min={0} max={90} step={5} unit="°" explanation="Gira a visualização; o agrupamento não muda." onChange={setAngle} />}
    <button className="primary-button" onClick={nextStep} type="button">{phase === 'assigned' ? 'Mover centróides' : 'Atribuir pontos'} <span aria-hidden="true">→</span></button>
    <button className="reset-button" onClick={() => reset()} type="button">Reiniciar agrupamento</button>
    <p className="control-hint">Rodadas completas: {round}. Cada rodada tem duas etapas: atribuir e mover.</p>
  </Lab>;
}

const svmBasePoints: readonly LabeledPoint[] = [
  { id: 'A1', x: 1.4, y: 2.0, label: 'A' }, { id: 'A2', x: 2.4, y: 3.7, label: 'A' },
  { id: 'A3', x: 3.3, y: 1.8, label: 'A' }, { id: 'A4', x: 3.8, y: 4.2, label: 'A' },
  { id: 'B1', x: 6.2, y: 6.1, label: 'B' }, { id: 'B2', x: 7.0, y: 7.7, label: 'B' },
  { id: 'B3', x: 8.3, y: 5.8, label: 'B' }, { id: 'B4', x: 8.7, y: 8.2, label: 'B' },
];

const svmNearPoint: LabeledPoint = { id: 'A5', x: 5.0, y: 5.4, label: 'A' };

function svmNormal(degrees: number) {
  const radians = degrees * Math.PI / 180;
  return { x: Math.cos(radians), y: Math.sin(radians) };
}

function boundarySegment(normal: { x: number; y: number }, cutoff: number) {
  const candidates: PlanePoint[] = [];
  if (Math.abs(normal.y) > 1e-6) {
    [0, 10].forEach((x) => { const y = (cutoff - normal.x * x) / normal.y; if (y >= 0 && y <= 10) candidates.push({ id: `x${x}`, x, y }); });
  }
  if (Math.abs(normal.x) > 1e-6) {
    [0, 10].forEach((y) => { const x = (cutoff - normal.y * y) / normal.x; if (x >= 0 && x <= 10) candidates.push({ id: `y${y}`, x, y }); });
  }
  const unique = candidates.filter((point, index, list) => list.findIndex((other) => Math.hypot(other.x - point.x, other.y - point.y) < 1e-5) === index);
  return unique.slice(0, 2);
}

export function SvmModule() {
  const [dataset, setDataset] = useState<'separadas' | 'proxima'>('separadas');
  const [mode, setMode] = useState<'manual' | 'sugerida'>('manual');
  const [angle, setAngle] = useState(45);
  const [cutoff, setCutoff] = useState(6.4);
  const [targetX, setTargetX] = useState(5);
  const [targetY, setTargetY] = useState(5);
  const [showMargin, setShowMargin] = useState(true);
  const points = dataset === 'separadas' ? svmBasePoints : [...svmBasePoints, svmNearPoint];
  const suggested = useMemo(() => trainLinearSvm(points), [points]);
  const normal = svmNormal(angle);
  const manualDistances = points.map((point) => Math.abs(normal.x * point.x + normal.y * point.y - cutoff));
  const manualFit: LinearSvmFit = {
    normal,
    bias: -cutoff,
    margin: Math.min(...manualDistances),
    supportIds: points.filter((_, index) => manualDistances[index]! <= Math.min(...manualDistances) + .08).map((point) => point.id),
    separable: points.every((point) => classifyLinearSvm(point, { normal, bias: -cutoff }).label === point.label),
  };
  const fit = mode === 'sugerida' ? suggested : manualFit;
  const activeCutoff = -fit.bias;
  const target = { id: 'novo', x: targetX, y: targetY };
  const outcome = classifyLinearSvm(target, fit);
  const correct = points.filter((point) => classifyLinearSvm(point, fit).label === point.label).length;
  const supportIds = new Set(fit.supportIds);
  const line = boundarySegment(fit.normal, activeCutoff);
  const upperMargin = boundarySegment(fit.normal, activeCutoff + fit.margin);
  const lowerMargin = boundarySegment(fit.normal, activeCutoff - fit.margin);
  const score = outcome.score;
  return <Lab onEnterGuided={() => { setDataset('separadas'); setMode('manual'); setAngle(45); setCutoff(6.4); setTargetX(5); setTargetY(5); setShowMargin(true); }} question="Como uma fronteira separa duas classes?" scenario="Amostras fictícias de sementes têm comprimento e largura entre 0 e 10. Algumas já receberam rótulo A ou B. A SVM procura uma linha que separe as duas classes com espaço entre elas." concept="A fronteira divide as classes; a margem mede a distância até os exemplos que ficaram mais próximos da linha." predictionQuestion="se a fronteira se aproximar de uma classe, a margem aumenta ou diminui?" guidedAction={<><p className="guide-instruction">Primeiro, mova somente a posição da fronteira. Depois, peça ao algoritmo uma sugestão e compare as duas margens.</p><RangeControl id="svm-guide-cutoff" label="Posição da fronteira" value={cutoff} min={4} max={10} step={.1} explanation="Mantenha a inclinação fixa e veja quais pontos ficam mais perto da linha." onChange={setCutoff} /><div className="segmented-control"><span>Quem posiciona a fronteira?</span><div><button aria-pressed={mode === 'manual'} onClick={() => setMode('manual')} type="button">Eu posiciono</button><button aria-pressed={mode === 'sugerida'} onClick={() => setMode('sugerida')} type="button">Algoritmo sugere</button></div></div></>} workedExample={<><h3>Leia a fronteira e a margem</h3><p>A linha atual usa a regra {formatarNumero(fit.normal.x, 2)} × comprimento + {formatarNumero(fit.normal.y, 2)} × largura = {formatarNumero(activeCutoff, 2)}. Os exemplos mais próximos são {fit.supportIds.join(' e ') || 'os pontos marcados'}.</p><p>A margem é {formatarNumero(fit.margin, 2)} unidade(s). {fit.separable ? 'Nenhum exemplo exibido ficou no lado da outra classe.' : 'Há exemplos no lado oposto da fronteira; neste caso, a linha não separa perfeitamente as classes.'} Para o ponto novo, o valor calculado é {formatarNumero(score, 2)}: como ele é {score >= 0 ? 'maior ou igual a zero, a classe indicada é B' : 'menor que zero, a classe indicada é A'}.</p></>} quickCheck={{ question: 'O que indica uma margem maior entre duas classes separadas?', options: ['A fronteira está mais distante dos exemplos mais próximos das classes.', 'Os rótulos dos exemplos foram apagados.', 'A SVM passou a formar grupos sem rótulos.'], correct: 0, explanation: 'A margem é o espaço entre a fronteira e os exemplos que a limitam.', retryHint: 'Observe as duas linhas tracejadas paralelas à fronteira.' }} formula="w₁x + w₂y + b = 0   •   margem = distância até os exemplos mais próximos" note="A SVM linear escolhe uma fronteira para duas classes rotuladas. Os vetores de suporte são os exemplos mais próximos da fronteira; eles delimitam a margem. A regra funciona bem neste conjunto sintético separado, mas dados sobrepostos ou uma divisão curva podem exigir outra estratégia." result={<><strong>Classe {outcome.label}</strong><p>Ponto novo: ({formatarNumero(targetX, 1)}; {formatarNumero(targetY, 1)}). Está no lado {outcome.label} da fronteira.</p><p>Margem: {formatarNumero(fit.margin, 2)}. Acertos nos exemplos exibidos: {correct}/{points.length}. {fit.separable ? 'Separação completa neste cenário.' : 'Separação incompleta neste cenário.'}</p></>} visual={<><Plot title="Fronteira de decisão da SVM" description={`Amostras de sementes em duas classes. Fronteira ${mode === 'sugerida' ? 'sugerida pelo algoritmo' : 'posicionada manualmente'}. Margem ${formatarNumero(fit.margin, 2)}.`} xLabel="Comprimento (0–10)" yLabel="Largura (0–10)" xMax={10} yMax={10}>{(x, y) => <>
    {showMargin && upperMargin.length === 2 && <line className="svm-margin-line" x1={x(upperMargin[0]!.x)} y1={y(upperMargin[0]!.y)} x2={x(upperMargin[1]!.x)} y2={y(upperMargin[1]!.y)} />}
    {showMargin && lowerMargin.length === 2 && <line className="svm-margin-line" x1={x(lowerMargin[0]!.x)} y1={y(lowerMargin[0]!.y)} x2={x(lowerMargin[1]!.x)} y2={y(lowerMargin[1]!.y)} />}
    {line.length === 2 && <line className="svm-boundary-line" x1={x(line[0]!.x)} y1={y(line[0]!.y)} x2={x(line[1]!.x)} y2={y(line[1]!.y)} />}
    {points.map((point) => <g key={point.id}><circle className={`class-dot ${point.label === 'A' ? 'class-a' : 'class-b'} ${supportIds.has(point.id) ? 'svm-support-point' : ''}`} cx={x(point.x)} cy={y(point.y)} r={supportIds.has(point.id) ? 10 : 8} /><text className="point-label" x={x(point.x) + 12} y={y(point.y) - 8}>{point.id}</text></g>)}
    <circle className="query-dot" cx={x(targetX)} cy={y(targetY)} r={11} /><text className="query-label" textAnchor="middle" x={x(targetX)} y={y(targetY) + 5}>?</text>
  </>}</Plot><p className="visual-caption"><span className="legend-dot class-a" /> classe A <span className="legend-dot class-b" /> classe B <span className="legend-svm-line" /> fronteira <span className="legend-dash" /> margem <span className="legend-ring" /> ponto novo</p><details className="chart-data"><summary>Consultar pontos e classificação por texto</summary><div className="table-scroll"><table><thead><tr><th>Exemplo</th><th>Comprimento</th><th>Largura</th><th>Classe</th><th>Resultado da SVM</th><th>Vetores de suporte</th></tr></thead><tbody>{points.map((point) => <tr key={point.id}><td>{point.id}</td><td>{formatarNumero(point.x, 1)}</td><td>{formatarNumero(point.y, 1)}</td><td>{point.label}</td><td>{classifyLinearSvm(point, fit).label}</td><td>{supportIds.has(point.id) ? 'sim' : 'não'}</td></tr>)}</tbody></table></div></details></>}>
    <div className="segmented-control"><span>Distribuição das classes</span><div><button aria-pressed={dataset === 'separadas'} onClick={() => setDataset('separadas')} type="button">Classes separadas</button><button aria-pressed={dataset === 'proxima'} onClick={() => setDataset('proxima')} type="button">Ponto próximo</button></div></div>
    <div className="segmented-control"><span>Fronteira de decisão</span><div><button aria-pressed={mode === 'manual'} onClick={() => setMode('manual')} type="button">Posicionar linha</button><button aria-pressed={mode === 'sugerida'} onClick={() => setMode('sugerida')} type="button">Ver sugestão</button></div></div>
    {mode === 'manual' && <><RangeControl id="svm-angle" label="Orientação da fronteira" value={angle} min={20} max={70} step={1} unit="°" explanation="Gire a linha para comparar quais pontos ficam próximos dela." onChange={setAngle} /><RangeControl id="svm-cutoff" label="Posição da fronteira" value={cutoff} min={4} max={10} step={.1} explanation="Desloque a linha sem mudar sua orientação." onChange={setCutoff} /></>}
    <RangeControl id="svm-x" label="Comprimento do ponto novo" value={targetX} min={0} max={10} step={.5} explanation="Mova o ponto novo e veja em qual lado da fronteira ele fica." onChange={setTargetX} />
    <RangeControl id="svm-y" label="Largura do ponto novo" value={targetY} min={0} max={10} step={.5} explanation="As duas medidas participam da classificação." onChange={setTargetY} />
    <label className="check-row"><input checked={showMargin} onChange={(event) => setShowMargin(event.target.checked)} type="checkbox" /> Mostrar margem e vetores de suporte</label>
    <button className="reset-button" onClick={() => { setDataset('separadas'); setMode('manual'); setAngle(45); setCutoff(6.4); setTargetX(5); setTargetY(5); setShowMargin(true); }} type="button">Recomeçar experimento</button>
  </Lab>;
}
