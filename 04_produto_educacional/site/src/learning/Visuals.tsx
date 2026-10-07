import type { ReactNode } from 'react';

interface PlotProps {
  title: string;
  description: string;
  xLabel: string;
  yLabel: string;
  xMin?: number;
  xMax: number;
  yMin?: number;
  yMax: number;
  xTicks?: number[];
  yTicks?: number[];
  children: (x: (value: number) => number, y: (value: number) => number) => ReactNode;
}

const W = 680;
const H = 410;
const box = { left: 70, right: 34, top: 24, bottom: 62 };

export function Plot({ title, description, xLabel, yLabel, xMin = 0, xMax, yMin = 0, yMax, xTicks, yTicks, children }: PlotProps) {
  const right = W - box.right;
  const bottom = H - box.bottom;
  const x = (value: number) => box.left + ((value - xMin) / (xMax - xMin)) * (right - box.left);
  const y = (value: number) => bottom - ((value - yMin) / (yMax - yMin)) * (bottom - box.top);
  const xMarks = xTicks ?? Array.from({ length: 6 }, (_, index) => xMin + (index * (xMax - xMin)) / 5);
  const yMarks = yTicks ?? Array.from({ length: 5 }, (_, index) => yMin + (index * (yMax - yMin)) / 4);
  return (
    <svg aria-label={`${title}. ${description}`} className="learning-plot" role="img" viewBox={`0 0 ${W} ${H}`}>
      <rect className="plot-field" x={box.left} y={box.top} width={right - box.left} height={bottom - box.top} />
      {yMarks.map((tick) => <g key={`y${tick}`}><line className="plot-grid" x1={box.left} x2={right} y1={y(tick)} y2={y(tick)} /><text className="plot-tick" textAnchor="end" x={box.left - 12} y={y(tick) + 5}>{tick.toLocaleString('pt-BR', { maximumFractionDigits: 2 })}</text></g>)}
      {xMarks.map((tick) => <g key={`x${tick}`}><line className="plot-grid vertical" x1={x(tick)} x2={x(tick)} y1={box.top} y2={bottom} /><text className="plot-tick" textAnchor="middle" x={x(tick)} y={bottom + 25}>{tick.toLocaleString('pt-BR', { maximumFractionDigits: 2 })}</text></g>)}
      <line className="plot-axis" x1={box.left} x2={right} y1={bottom} y2={bottom} />
      <line className="plot-axis" x1={box.left} x2={box.left} y1={box.top} y2={bottom} />
      {children(x, y)}
      <text className="plot-axis-label" textAnchor="middle" x={(box.left + right) / 2} y={H - 13}>{xLabel}</text>
      <text className="plot-axis-label" textAnchor="middle" transform={`rotate(-90 19 ${(box.top + bottom) / 2})`} x={19} y={(box.top + bottom) / 2}>{yLabel}</text>
    </svg>
  );
}

interface RangeControlProps {
  id: string;
  label: string;
  value: number;
  min: number;
  max: number;
  step: number;
  unit?: string;
  explanation: string;
  onChange: (value: number) => void;
}

export function RangeControl({ id, label, value, min, max, step, unit = '', explanation, onChange }: RangeControlProps) {
  return (
    <div className="range-control">
      <div className="range-heading"><label htmlFor={id}>{label}</label><output htmlFor={id}>{value.toLocaleString('pt-BR', { maximumFractionDigits: 2 })}{unit && ` ${unit}`}</output></div>
      <input id={id} max={max} min={min} onChange={(event) => onChange(Number(event.target.value))} step={step} type="range" value={value} />
      <p>{explanation}</p>
    </div>
  );
}

export function LearningCurve({ title, values, current }: { title: string; values: readonly number[]; current: number }) {
  const maximum = Math.max(...values, 0.001);
  const x = (index: number) => 58 + index * 295 / Math.max(1, values.length - 1);
  const y = (value: number) => 160 - value / maximum * 125;
  return <div className="mini-chart"><strong>{title}</strong><svg role="img" aria-label={`${title}. Início: ${values[0]?.toFixed(2)}. Etapa ${current}: ${values[current]?.toFixed(2)}.`} viewBox="0 0 400 190"><line className="plot-axis" x1="58" x2="360" y1="160" y2="160" /><line className="plot-axis" x1="58" x2="58" y1="20" y2="160" /><path className="learning-line" d={values.map((value, index) => `${index ? 'L' : 'M'} ${x(index)} ${y(value)}`).join(' ')} /><circle className="learning-marker" cx={x(current)} cy={y(values[current] ?? 0)} r="7" /><text className="plot-tick" x="55" y="181">0</text><text className="plot-tick" x="330" y="181">etapa</text></svg><p>O ponto destacado corresponde à etapa escolhida. Menor erro indica melhor ajuste aos dados deste exercício.</p></div>;
}

export function LossSurface3D({ title, sample, marker, angle, xLabel = 'parâmetro 1', yLabel = 'parâmetro 2', zLabel = 'erro', explanation = 'A altura é o erro, não uma terceira variável dos dados.' }: { title: string; sample: (u: number, v: number) => number; marker: [number, number]; angle: number; xLabel?: string; yLabel?: string; zLabel?: string; explanation?: string }) {
  const cos = Math.cos(angle * Math.PI / 180);
  const sin = Math.sin(angle * Math.PI / 180);
  const values = Array.from({ length: 13 }, (_, i) => Array.from({ length: 13 }, (_, j) => sample(i / 12, j / 12)));
  const max = Math.max(...values.flat(), 0.001);
  const project = (u: number, v: number, z: number) => ({ x: 260 + (u - .5) * 240 * cos - (v - .5) * 240 * sin, y: 210 + (u - .5) * 115 * sin + (v - .5) * 115 * cos - z / max * 130 });
  const markerPosition = project(marker[0], marker[1], sample(marker[0], marker[1]));
  return <div className="surface-3d"><strong>{title}</strong><svg viewBox="0 0 520 350" role="img" aria-label={`${title}. Superfície projetada em perspectiva. Eixos horizontais: ${xLabel} e ${yLabel}; altura: ${zLabel}.`}><path className="surface-base" d="M80 245 L260 345 L445 245 L260 145 Z" />{values.map((row, i) => <polyline key={`row-${i}`} className="surface-line" points={row.map((value, j) => { const point = project(i / 12, j / 12, value); return `${point.x},${point.y}`; }).join(' ')} />)}{values.map((_, j) => <polyline key={`col-${j}`} className="surface-line cross" points={values.map((row, i) => { const point = project(i / 12, j / 12, row[j]!); return `${point.x},${point.y}`; }).join(' ')} />)}<circle className="surface-marker" cx={markerPosition.x} cy={markerPosition.y} r="8" /><text className="surface-label" x="40" y="252">{xLabel}</text><text className="surface-label" x="365" y="285">{yLabel}</text><text className="surface-label" x="260" y="25">{zLabel} ↑</text></svg><p>Perspectiva de uma superfície calculada; gire para ver a mesma relação de outro ângulo. {explanation}</p></div>;
}
