export interface DataPoint {
  id?: string;
  x: number;
  y: number;
}

export interface LineParameters {
  a: number;
  b: number;
}

export interface ResidualResult extends DataPoint {
  yPredicted: number;
  residual: number;
  squaredError: number;
}

export interface ExperimentMetrics {
  parameters: LineParameters;
  sse: number;
  mse: number;
}

export interface RegressionResult extends ExperimentMetrics {
  residuals: ResidualResult[];
}

export interface ExperimentComparison {
  previous: ExperimentMetrics;
  current: ExperimentMetrics;
  deltaA: number;
  deltaB: number;
  deltaSSE: number;
  deltaMSE: number;
  directionA: 'aumentou' | 'diminuiu' | 'igual';
  directionB: 'aumentou' | 'diminuiu' | 'igual';
  directionMSE: 'aumentou' | 'diminuiu' | 'igual';
}

// Compatibilidade temporária com nomes da primeira fundação.
export type Point = DataPoint;
export type Linha = LineParameters;
export type Residuo = ResidualResult;

function assertFinite(value: number, name: string): void {
  if (!Number.isFinite(value)) throw new Error(`${name} deve ser um número finito.`);
}

function assertDataPoints(points: readonly DataPoint[]): void {
  points.forEach((point) => {
    assertFinite(point.x, 'x');
    assertFinite(point.y, 'y');
  });
}

function compareDirection(
  delta: number,
  tolerance: number,
): ExperimentComparison['directionA'] {
  if (delta > tolerance) return 'aumentou';
  if (delta < -tolerance) return 'diminuiu';
  return 'igual';
}

export function prever(a: number, b: number, x: number): number {
  assertFinite(a, 'a');
  assertFinite(b, 'b');
  assertFinite(x, 'x');
  const result = a + b * x;
  assertFinite(result, 'previsão');
  return result;
}

export function calcularResiduos(
  points: readonly DataPoint[],
  parameters: LineParameters,
): ResidualResult[] {
  assertDataPoints(points);
  return points.map((point) => {
    const yPredicted = prever(parameters.a, parameters.b, point.x);
    const residual = point.y - yPredicted;
    const squaredError = residual ** 2;
    assertFinite(squaredError, 'erro quadrático');
    return { ...point, yPredicted, residual, squaredError };
  });
}

export function calcularSSE(residuals: readonly Pick<ResidualResult, 'residual'>[]): number {
  // A lista vazia representa soma sem termos e, por definição, tem SSE igual a zero.
  const sse = residuals.reduce((sum, result) => {
    assertFinite(result.residual, 'resíduo');
    return sum + result.residual ** 2;
  }, 0);
  assertFinite(sse, 'SSE');
  return sse;
}

export function calcularMSE(residuals: readonly Pick<ResidualResult, 'residual'>[]): number {
  if (residuals.length === 0) throw new Error('MSE requer ao menos um ponto.');
  const mse = calcularSSE(residuals) / residuals.length;
  assertFinite(mse, 'MSE');
  return mse;
}

export function regressaoOLS(points: readonly DataPoint[]): RegressionResult {
  if (points.length < 2) throw new Error('OLS requer ao menos dois pontos.');
  assertDataPoints(points);
  const meanX = points.reduce((sum, point) => sum + point.x, 0) / points.length;
  const meanY = points.reduce((sum, point) => sum + point.y, 0) / points.length;
  const numerator = points.reduce(
    (sum, point) => sum + (point.x - meanX) * (point.y - meanY),
    0,
  );
  const denominator = points.reduce((sum, point) => sum + (point.x - meanX) ** 2, 0);
  if (denominator === 0) throw new Error('OLS requer ao menos dois valores de x distintos.');
  const b = numerator / denominator;
  const parameters = { a: meanY - b * meanX, b };
  const residuals = calcularResiduos(points, parameters);
  const sse = calcularSSE(residuals);
  const mse = calcularMSE(residuals);
  return { parameters, residuals, sse, mse };
}

export function trainLinearGradient(points: readonly DataPoint[], steps: number, learningRate: number) {
  if (!points.length || !Number.isInteger(steps) || steps < 0 || !Number.isFinite(learningRate) || learningRate <= 0 || learningRate > 1) throw new Error('Treino inválido');
  let a = 0;
  let scaledSlope = 0;
  const history = [];
  for (let step = 0; step <= steps; step++) {
    const parameters = { a, b: scaledSlope / 50 };
    history.push({ step, parameters, mse: calcularMSE(calcularResiduos(points, parameters)) });
    const gradientA = points.reduce((sum, point) => sum + 2 * (a + scaledSlope * point.x / 50 - point.y), 0) / points.length;
    const gradientB = points.reduce((sum, point) => sum + 2 * (a + scaledSlope * point.x / 50 - point.y) * point.x / 50, 0) / points.length;
    a -= learningRate * gradientA;
    scaledSlope -= learningRate * gradientB;
  }
  return history;
}

export function compararExperimentos(
  previous: ExperimentMetrics,
  current: ExperimentMetrics,
  tolerance = 0.000000001,
): ExperimentComparison {
  if (!Number.isFinite(tolerance) || tolerance < 0) {
    throw new Error('Tolerância deve ser um número finito não negativo.');
  }
  const values = [
    previous.parameters.a,
    previous.parameters.b,
    previous.sse,
    previous.mse,
    current.parameters.a,
    current.parameters.b,
    current.sse,
    current.mse,
  ];
  values.forEach((value, index) => assertFinite(value, `métrica ${index + 1}`));
  const deltaA = current.parameters.a - previous.parameters.a;
  const deltaB = current.parameters.b - previous.parameters.b;
  const deltaSSE = current.sse - previous.sse;
  const deltaMSE = current.mse - previous.mse;
  return {
    previous,
    current,
    deltaA,
    deltaB,
    deltaSSE,
    deltaMSE,
    directionA: compareDirection(deltaA, tolerance),
    directionB: compareDirection(deltaB, tolerance),
    directionMSE: compareDirection(deltaMSE, tolerance),
  };
}

export function formatarNumero(value: number, precision = 3, locale = 'pt-BR'): string {
  assertFinite(value, 'valor');
  if (!Number.isInteger(precision) || precision < 0 || precision > 20) {
    throw new Error('Precisão deve ser um inteiro entre 0 e 20.');
  }
  const rounded = Number(value.toFixed(precision));
  const normalized = Object.is(rounded, -0) ? 0 : rounded;
  return new Intl.NumberFormat(locale, {
    minimumFractionDigits: precision,
    maximumFractionDigits: precision,
  }).format(normalized);
}

export function formatarComUnidade(
  value: number,
  unit: string,
  precision = 3,
  locale = 'pt-BR',
): string {
  const formatted = formatarNumero(value, precision, locale);
  return unit ? `${formatted} ${unit}` : formatted;
}

export const formatar = (
  value: number,
  precision = 3,
  unit = '',
  locale = 'pt-BR',
): string => formatarComUnidade(value, unit, precision, locale);
