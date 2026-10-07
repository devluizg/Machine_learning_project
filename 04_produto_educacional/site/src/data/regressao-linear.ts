// Fonte: ../../prototipos/modulo_piloto_regressao_linear/DADOS_SINTETICOS.csv
export type PointIdentifier = string;
export type MassGrams = number;
export type ElongationCentimeters = number;
export type PointKind = 'base' | 'atipico';
export type InitiallyVisible = boolean;
export type PointObservation = string;

export interface RegressionDataPoint {
  id: PointIdentifier;
  x: MassGrams;
  y: ElongationCentimeters;
  tipo: PointKind;
  visivelInicialmente: InitiallyVisible;
  observacao: PointObservation;
}

export interface MeasurementUnits {
  x: 'g';
  y: 'cm';
  intercept: 'cm';
  slope: 'cm/g';
  residual: 'cm';
  squaredError: 'cm²';
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
  x: 'g',
  y: 'cm',
  intercept: 'cm',
  slope: 'cm/g',
  residual: 'cm',
  squaredError: 'cm²',
};

export const controles = {
  intercept: { min: -0.5, max: 1, step: 0.1, initial: 0.5, unit: 'cm' },
  slope: { min: 0.04, max: 0.14, step: 0.01, initial: 0.06, unit: 'cm/g' },
} satisfies Record<string, ParameterControl>;

export const eixos = {
  x: { min: 0, max: 70, step: 10, unit: 'g' },
  y: { min: -0.5, max: 10, step: 1, unit: 'cm' },
} satisfies Record<'x' | 'y', AxisDefinition>;

export const pontosBase: readonly RegressionDataPoint[] = [
  { id: 'P01', x: 10, y: 1.08, tipo: 'base', visivelInicialmente: true, observacao: 'medição sintética base' },
  { id: 'P02', x: 20, y: 1.91, tipo: 'base', visivelInicialmente: true, observacao: 'medição sintética base' },
  { id: 'P03', x: 30, y: 3.12, tipo: 'base', visivelInicialmente: true, observacao: 'medição sintética base' },
  { id: 'P04', x: 40, y: 3.87, tipo: 'base', visivelInicialmente: true, observacao: 'medição sintética base' },
  { id: 'P05', x: 50, y: 5.09, tipo: 'base', visivelInicialmente: true, observacao: 'medição sintética base' },
  { id: 'P06', x: 60, y: 5.94, tipo: 'base', visivelInicialmente: true, observacao: 'medição sintética base' },
];

export const pontoP07: RegressionDataPoint = {
  id: 'P07',
  x: 30,
  y: 8.5,
  tipo: 'atipico',
  visivelInicialmente: false,
  observacao: 'medição sintética a investigar; não presumir erro',
};

export const pontosP07: readonly RegressionDataPoint[] = [pontoP07];
export const todosPontos: readonly RegressionDataPoint[] = [...pontosBase, ...pontosP07];

// Aliases mantêm compatibilidade com o primeiro protótipo técnico.
export const pontosRegressao = todosPontos;
export const pontoAtipico = pontoP07;
