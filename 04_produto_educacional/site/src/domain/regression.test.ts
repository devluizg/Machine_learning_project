import { describe, expect, it } from 'vitest';
import {
  controles,
  eixos,
  pontoP07,
  pontosBase,
  pontosP07,
  todosPontos,
  unidades,
} from '../data/regressao-linear';
import {
  calcularMSE,
  calcularResiduos,
  calcularSSE,
  compararExperimentos,
  formatarComUnidade,
  formatarNumero,
  prever,
  regressaoOLS,
  trainLinearGradient,
  type DataPoint,
} from './regression';

const base: readonly DataPoint[] = pontosBase;
const all: readonly DataPoint[] = todosPontos;
const close = (actual: number, expected: number) =>
  expect(Math.abs(actual - expected)).toBeLessThanOrEqual(0.000001);

it('treino da reta reduz o erro e aproxima a solução de referência', () => {
  const history = trainLinearGradient(base, 80, 0.08);
  expect(history.at(-1)!.mse).toBeLessThan(history[0]!.mse);
  expect(history.at(-1)!.mse).toBeGreaterThanOrEqual(regressaoOLS(base).mse - 0.000001);
});

describe('contratos do módulo de regressão linear', () => {
  it('01 — publica exatamente seis pontos-base', () => expect(pontosBase).toHaveLength(6));
  it('02 — separa P07 e conserva todos os sete dados', () => {
    expect(pontosP07).toEqual([pontoP07]);
    expect(todosPontos).toHaveLength(7);
    expect(pontosBase.every(({ visivelInicialmente }) => visivelInicialmente)).toBe(true);
    expect(pontoP07).toMatchObject({
      visivelInicialmente: false,
      observacao: 'medição sintética a investigar; não presumir erro',
    });
  });
  it('03 — publica unidades, controles e eixos definidos', () => {
    expect(unidades).toMatchObject({ x: 'g', y: 'cm', slope: 'cm/g', squaredError: 'cm²' });
    expect(controles.intercept).toMatchObject({ min: -0.5, max: 1, step: 0.1, initial: 0.5 });
    expect(controles.slope).toMatchObject({ min: 0.04, max: 0.14, step: 0.01, initial: 0.06 });
    expect(eixos).toMatchObject({ x: { min: 0, max: 70, step: 10 }, y: { min: -0.5, max: 10, step: 1 } });
  });
  it('04 — prevê y=a+bx sem arredondar', () => expect(prever(0.5, 0.06, 35)).toBe(2.6));
  it('05 — rejeita entrada não finita na previsão', () => expect(() => prever(Infinity, 1, 1)).toThrow(/finito/));
  it('06 — resíduos mantêm id e calculam erro e quadrado', () => {
    expect(calcularResiduos(base.slice(0, 1), { a: 0.5, b: 0.06 })[0]).toMatchObject({
      id: 'P01', yPredicted: 1.1, residual: -0.020000000000000018,
    });
  });
  it('07 — resíduos rejeitam valores não finitos e não mutam os dados', () => {
    const before = structuredClone(base);
    expect(() => calcularResiduos([{ x: NaN, y: 1 }], { a: 0, b: 1 })).toThrow(/finito/);
    calcularResiduos(base, { a: 0.5, b: 0.06 });
    expect(base).toEqual(before);
  });
  it('08 — SSE e MSE implementam soma e média dos quadrados', () => {
    const residuals = calcularResiduos(base, { a: 0.5, b: 0.06 });
    close(calcularSSE(residuals), 7.5715);
    close(calcularMSE(residuals), 1.2619166666666667);
  });
  it('09 — MSE de lista vazia gera erro explicativo', () => expect(() => calcularMSE([])).toThrow(/ao menos um ponto/));
  it('10 — N01: reta inicial prevê 2,6 em x=35', () => close(prever(0.5, 0.06, 35), 2.6));
  it('11 — N02: inclinação 0,10 dá MSE 0,257917', () => {
    close(calcularMSE(calcularResiduos(base, { a: 0.5, b: 0.1 })), 0.2579166666666667);
  });
  it('12 — N03: intercepto 0 dá MSE 2,413583', () => {
    close(calcularMSE(calcularResiduos(base, { a: 0, b: 0.06 })), 2.4135833333333335);
  });
  it('13 — N04: reta manual próxima dá SSE e MSE esperados', () => {
    const residuals = calcularResiduos(base, { a: 0, b: 0.1 });
    close(calcularSSE(residuals), 0.0575);
    close(calcularMSE(residuals), 0.009583333333333334);
  });
  it('14 — N05: OLS-base devolve parâmetros e métricas esperados', () => {
    const result = regressaoOLS(base);
    close(result.parameters.a, 0.042666666666666714);
    close(result.parameters.b, 0.09882857142857142);
    close(result.sse, 0.05508190476190478);
    close(result.mse, 0.009180317460317463);
    close(prever(result.parameters.a, result.parameters.b, 35), 3.5016666666666665);
  });
  it('15 — OLS devolve resíduos identificados e não altera entrada', () => {
    const before = structuredClone(base);
    const result = regressaoOLS(base);
    expect(result.residuals.map(({ id }) => id)).toEqual(['P01', 'P02', 'P03', 'P04', 'P05', 'P06']);
    expect(base).toEqual(before);
  });
  it('16 — N06: OLS com P07 tem intercepto acima do limite manual e métricas corretas', () => {
    const result = regressaoOLS(all);
    expect(result.parameters.a).toBeGreaterThan(controles.intercept.max);
    close(result.parameters.a, 1.282903225806452);
    close(result.parameters.b, 0.08554032258064516);
    close(result.sse, 25.599969354838708);
    close(result.mse, 3.6571384792626725);
    expect(result.residuals.map(({ id }) => id)).toContain('P07');
  });
  it('17 — N07 e N08: resíduo P03 positivo e P04 negativo', () => {
    const result = regressaoOLS(base);
    expect(result.residuals.find(({ id }) => id === 'P03')!.residual).toBeGreaterThan(0);
    expect(result.residuals.find(({ id }) => id === 'P04')!.residual).toBeLessThan(0);
  });
  it('18 — OLS rejeita entradas insuficientes, constantes ou não finitas', () => {
    expect(() => regressaoOLS([{ x: 1, y: 2 }])).toThrow(/dois pontos/);
    expect(() => regressaoOLS([{ x: 2, y: 1 }, { x: 2, y: 3 }])).toThrow(/distintos/);
    expect(() => regressaoOLS([{ x: NaN, y: 1 }, { x: 2, y: 3 }])).toThrow(/finito/);
    expect(() => regressaoOLS([{ x: Infinity, y: 1 }, { x: 2, y: 3 }])).toThrow(/finito/);
  });
  it('19 — comparação retorna variações e direção determinística', () => {
    const comparison = compararExperimentos(
      { parameters: { a: 0, b: 0.1 }, sse: 1, mse: 1 },
      { parameters: { a: 1, b: 0.05 }, sse: 2, mse: 0.5 },
    );
    expect(comparison).toMatchObject({ deltaA: 1, deltaB: -0.05, deltaSSE: 1, deltaMSE: -0.5,
      directionA: 'aumentou', directionB: 'diminuiu', directionMSE: 'diminuiu' });
    expect(() => compararExperimentos(
      { parameters: { a: NaN, b: 1 }, sse: 0, mse: 0 },
      { parameters: { a: 0, b: 1 }, sse: 0, mse: 0 },
    )).toThrow(/finito/);
    const practicallyEqual = compararExperimentos(
      { parameters: { a: 0, b: 0 }, sse: 0, mse: 0 },
      { parameters: { a: 0.0000000001, b: 0 }, sse: 0, mse: 0 },
    );
    expect(practicallyEqual.directionA).toBe('igual');
  });
  it('20 — formatação usa vírgula, unidade, precisão e normaliza -0,000', () => {
    expect(formatarNumero(-0.0001)).toBe('0,000');
    expect(formatarComUnidade(0.098828571, 'cm/g')).toBe('0,099 cm/g');
    expect(formatarNumero(2.5, 1)).toBe('2,5');
  });
});
