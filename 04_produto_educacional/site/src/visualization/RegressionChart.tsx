import type { AxisDefinition } from '../data/regressao-linear';
import type { LineParameters, ResidualResult } from '../domain/regression';

interface RegressionChartProps {
  rows: readonly ResidualResult[];
  line: LineParameters;
  xAxis: AxisDefinition;
  yAxis: AxisDefinition;
  selectedPointId: string | null;
  onSelectPoint: (id: string) => void;
}

const WIDTH = 720;
const HEIGHT = 440;
const PADDING = { top: 32, right: 28, bottom: 58, left: 72 };

function scale(value: number, min: number, max: number, outputMin: number, outputMax: number): number {
  return outputMin + ((value - min) / (max - min)) * (outputMax - outputMin);
}

export function RegressionChart({
  rows,
  line,
  xAxis,
  yAxis,
  selectedPointId,
  onSelectPoint,
}: RegressionChartProps) {
  const plotLeft = PADDING.left;
  const plotRight = WIDTH - PADDING.right;
  const plotTop = PADDING.top;
  const plotBottom = HEIGHT - PADDING.bottom;
  const xToPixel = (x: number) => scale(x, xAxis.min, xAxis.max, plotLeft, plotRight);
  const yToPixel = (y: number) => scale(y, yAxis.min, yAxis.max, plotBottom, plotTop);
  const lineStart = line.a + line.b * xAxis.min;
  const lineEnd = line.a + line.b * xAxis.max;
  const xTicks = Array.from({ length: (xAxis.max - xAxis.min) / xAxis.step + 1 }, (_, index) => xAxis.min + index * xAxis.step);
  const yTicks = Array.from({ length: (yAxis.max - yAxis.min) / yAxis.step + 1 }, (_, index) => yAxis.min + index * yAxis.step);

  return (
    <figure className="chart-card">
      <figcaption id="chart-title">Dados sintéticos e reta manual inicial</figcaption>
      <svg
        aria-labelledby="chart-title chart-summary"
        className="regression-chart"
        role="img"
        viewBox={`0 0 ${WIDTH} ${HEIGHT}`}
      >
        <desc id="chart-summary">
          Seis pontos-base de massa e alongamento. A reta manual inicial usa intercepto de 0,500 centímetros e inclinação de 0,060 centímetros por grama.
        </desc>
        <rect className="plot-background" height={plotBottom - plotTop} width={plotRight - plotLeft} x={plotLeft} y={plotTop} />
        {xTicks.map((tick) => (
          <g key={`x-${tick}`}>
            <line className="grid-line" x1={xToPixel(tick)} x2={xToPixel(tick)} y1={plotTop} y2={plotBottom} />
            <text className="tick-label" textAnchor="middle" x={xToPixel(tick)} y={plotBottom + 22}>{tick}</text>
          </g>
        ))}
        {yTicks.map((tick) => (
          <g key={`y-${tick}`}>
            <line className="grid-line" x1={plotLeft} x2={plotRight} y1={yToPixel(tick)} y2={yToPixel(tick)} />
            <text className="tick-label" textAnchor="end" x={plotLeft - 10} y={yToPixel(tick) + 4}>{tick}</text>
          </g>
        ))}
        <line className="axis-line" x1={plotLeft} x2={plotRight} y1={plotBottom} y2={plotBottom} />
        <line className="axis-line" x1={plotLeft} x2={plotLeft} y1={plotTop} y2={plotBottom} />
        <line
          className="manual-line"
          x1={xToPixel(xAxis.min)}
          x2={xToPixel(xAxis.max)}
          y1={yToPixel(lineStart)}
          y2={yToPixel(lineEnd)}
        />
        {rows.map((row) => {
          const pointId = row.id ?? `${row.x}-${row.y}`;
          const isSelected = pointId === selectedPointId;
          return (
            <circle
              aria-label={`${pointId}: massa ${row.x} gramas, alongamento ${row.y} centímetros`}
              className={isSelected ? 'data-point data-point-selected' : 'data-point'}
              cx={xToPixel(row.x)}
              cy={yToPixel(row.y)}
              data-point-id={pointId}
              key={pointId}
              onClick={() => onSelectPoint(pointId)}
              onKeyDown={(event) => {
                if (event.key === 'Enter' || event.key === ' ') {
                  event.preventDefault();
                  onSelectPoint(pointId);
                }
              }}
              r={isSelected ? 8 : 6}
              role="button"
              tabIndex={0}
            />
          );
        })}
        <text className="axis-title" textAnchor="middle" x={(plotLeft + plotRight) / 2} y={HEIGHT - 12}>Massa (g)</text>
        <text className="axis-title" textAnchor="middle" transform={`rotate(-90 18 ${(plotTop + plotBottom) / 2})`} x={18} y={(plotTop + plotBottom) / 2}>Alongamento (cm)</text>
      </svg>
      <p className="chart-legend"><span className="legend-line" /> Reta manual inicial: ŷ = 0,500 + 0,060x</p>
    </figure>
  );
}
