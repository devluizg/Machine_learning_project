import type { ResidualResult } from '../domain/regression';
import { formatarNumero } from '../domain/regression';

interface DataTableProps {
  rows: readonly ResidualResult[];
  sse: number;
  mse: number;
  selectedPointId: string | null;
  onSelectPoint: (id: string) => void;
}

export function DataTable({ rows, sse, mse, selectedPointId, onSelectPoint }: DataTableProps) {
  return (
    <section aria-labelledby="data-table-title" className="table-card">
      <h2 id="data-table-title">Tabela equivalente ao gráfico</h2>
      <p>Use a tabela para consultar os mesmos pontos, previsões e resíduos representados no gráfico.</p>
      <div className="table-scroll">
        <table>
          <caption>Conjunto-base e valores derivados da reta manual inicial.</caption>
          <thead>
            <tr><th scope="col">Ponto</th><th scope="col">Massa (g)</th><th scope="col">Observado (cm)</th><th scope="col">Previsto (cm)</th><th scope="col">Resíduo (cm)</th><th scope="col">Resíduo² (cm²)</th><th scope="col">Ação</th></tr>
          </thead>
          <tbody>
            {rows.map((row) => {
              const pointId = row.id ?? `${row.x}-${row.y}`;
              return (
              <tr aria-current={pointId === selectedPointId ? 'true' : undefined} key={pointId}>
                <th scope="row">{pointId}</th>
                <td>{formatarNumero(row.x, 0)}</td>
                <td>{formatarNumero(row.y, 2)}</td>
                <td>{formatarNumero(row.yPredicted, 3)}</td>
                <td>{formatarNumero(row.residual, 3)}</td>
                <td>{formatarNumero(row.squaredError, 2)}</td>
                <td><button onClick={() => onSelectPoint(pointId)} type="button">{pointId === selectedPointId ? 'Selecionado' : 'Selecionar'}</button></td>
              </tr>
              );
            })}
          </tbody>
        </table>
      </div>
      <p className="metrics">SSE: {formatarNumero(sse, 3)} cm² · MSE: {formatarNumero(mse, 3)} cm²</p>
    </section>
  );
}
