// Fonte didática: instrumento da Aula 2, cenário de passos e distância.
export type PointIdentifier = string;
export type StepCount = number;
export type DistanceMeters = number;
export type PointKind = 'base' | 'atipico';
export type InitiallyVisible = boolean;
export type PointObservation = string;

export interface RegressionDataPoint {
  id: PointIdentifier;
  x: StepCount;
  y: DistanceMeters;
  tipo: PointKind;
  visivelInicialmente: InitiallyVisible;
  observacao: PointObservation;
}

export interface MeasurementUnits {
  x: 'passos';
  y: 'm';
  intercept: 'm';
  slope: 'm/passo';
  residual: 'm';
  squaredError: 'm²';
}

export interface ParameterControl {
  min: number;
  max: number;
  step: number;
  initial: number;
  unit: string;
}

export interface AxisDefinition {
  min: number;
  max: number;
  step: number;
  unit: string;
}

export const unidades: MeasurementUnits = {
  x: 'passos',
  y: 'm',
  intercept: 'm',
  slope: 'm/passo',
  residual: 'm',
  squaredError: 'm²',
};

export const controles = {
  intercept: { min: -1, max: 2, step: 0.1, initial: 0.5, unit: 'm' },
  slope: { min: 0.3, max: 0.9, step: 0.05, initial: 0.45, unit: 'm/passo' },
} satisfies Record<string, ParameterControl>;

export const eixos = {
  x: { min: 0, max: 28, step: 4, unit: 'passos' },
  y: { min: -1, max: 18, step: 3, unit: 'm' },
} satisfies Record<'x' | 'y', AxisDefinition>;

export const pontosBase: readonly RegressionDataPoint[] = [
  { id: 'P01', x: 4, y: 2.5, tipo: 'base', visivelInicialmente: true, observacao: 'medição sintética base' },
  { id: 'P02', x: 8, y: 5, tipo: 'base', visivelInicialmente: true, observacao: 'medição sintética base' },
  { id: 'P03', x: 12, y: 7.2, tipo: 'base', visivelInicialmente: true, observacao: 'medição sintética base' },
  { id: 'P04', x: 16, y: 9.8, tipo: 'base', visivelInicialmente: true, observacao: 'medição sintética base' },
  { id: 'P05', x: 20, y: 12.1, tipo: 'base', visivelInicialmente: true, observacao: 'medição sintética base' },
  { id: 'P06', x: 24, y: 14.7, tipo: 'base', visivelInicialmente: true, observacao: 'medição sintética base' },
];

export const pontoP07: RegressionDataPoint = {
  id: 'P07',
  x: 12,
  y: 14,
  tipo: 'atipico',
  visivelInicialmente: false,
  observacao: 'medição sintética a investigar; não presumir erro',
};

export const pontosP07: readonly RegressionDataPoint[] = [pontoP07];
export const todosPontos: readonly RegressionDataPoint[] = [...pontosBase, ...pontosP07];

// Aliases mantêm compatibilidade com o primeiro protótipo técnico.
export const pontosRegressao = todosPontos;
export const pontoAtipico = pontoP07;
