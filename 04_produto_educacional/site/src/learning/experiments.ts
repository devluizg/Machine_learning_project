export interface PlanePoint {
  id: string;
  x: number;
  y: number;
}

export interface LabeledPoint extends PlanePoint {
  label: 'A' | 'B';
}

export function logisticProbability(x: number, midpoint: number, steepness: number): number {
  return 1 / (1 + Math.exp(-steepness * (x - midpoint)));
}

export function logisticFromWeights(x: number, bias: number, weight: number): number {
  return 1 / (1 + Math.exp(-(bias + weight * ((x - 5) / 5))));
}

export interface BinaryObservation { x: number; label: 0 | 1 }

export function trainLogistic(points: readonly BinaryObservation[], steps: number, learningRate: number) {
  if (!points.length || steps < 0 || !Number.isInteger(steps) || learningRate <= 0) throw new Error('Treino inválido');
  let bias = 0;
  let weight = 0;
  const history = [];
  for (let step = 0; step <= steps; step++) {
    const loss = points.reduce((sum, point) => {
      const p = Math.min(1 - 1e-12, Math.max(1e-12, logisticFromWeights(point.x, bias, weight)));
      return sum - point.label * Math.log(p) - (1 - point.label) * Math.log(1 - p);
    }, 0) / points.length;
    history.push({ step, bias, weight, loss });
    const gradientBias = points.reduce((sum, point) => sum + logisticFromWeights(point.x, bias, weight) - point.label, 0) / points.length;
    const gradientWeight = points.reduce((sum, point) => sum + (logisticFromWeights(point.x, bias, weight) - point.label) * ((point.x - 5) / 5), 0) / points.length;
    bias -= learningRate * gradientBias;
    weight -= learningRate * gradientWeight;
  }
  return history;
}

export type DistanceMetric = 'euclidean' | 'manhattan';

export function pointDistance(a: PlanePoint, b: PlanePoint, metric: DistanceMetric = 'euclidean'): number {
  return metric === 'manhattan' ? Math.abs(a.x - b.x) + Math.abs(a.y - b.y) : Math.hypot(a.x - b.x, a.y - b.y);
}

export function classifyKnn(points: readonly LabeledPoint[], target: PlanePoint, k: number, metric: DistanceMetric = 'euclidean', weighted = false) {
  if (!Number.isInteger(k) || k < 1 || k > points.length) throw new Error('k inválido');
  const neighbors = points
    .map((point) => ({ ...point, distance: pointDistance(point, target, metric) }))
    .sort((a, b) => a.distance - b.distance || a.id.localeCompare(b.id))
    .slice(0, k);
  const votesA = neighbors.filter((point) => point.label === 'A').length;
  const votesB = k - votesA;
  const exact = neighbors.filter((point) => point.distance === 0);
  const ballot = exact.length ? exact : neighbors;
  const scoreA = ballot.reduce((sum, point) => sum + (point.label === 'A' ? weighted && !exact.length ? 1 / Math.max(point.distance, 0.001) : 1 : 0), 0);
  const scoreB = ballot.reduce((sum, point) => sum + (point.label === 'B' ? weighted && !exact.length ? 1 / Math.max(point.distance, 0.001) : 1 : 0), 0);
  const label = scoreA === scoreB ? neighbors[0]!.label : scoreA > scoreB ? 'A' : 'B';
  return { neighbors, votesA, votesB, scoreA, scoreB, label };
}

export interface TreeNode {
  count: number;
  countA: number;
  countB: number;
  label: 'A' | 'B';
  gini: number;
  axis?: 'x' | 'y';
  threshold?: number;
  left?: TreeNode;
  right?: TreeNode;
}

export function trainDecisionTree(points: readonly LabeledPoint[], maxDepth: number, minLeaf = 2): TreeNode {
  if (!points.length || !Number.isInteger(maxDepth) || maxDepth < 0) throw new Error('Dados ou profundidade inválidos');
  const grow = (subset: readonly LabeledPoint[], depth: number): TreeNode => {
    const countA = subset.filter((point) => point.label === 'A').length;
    const countB = subset.length - countA;
    const p = countA / subset.length;
    const node: TreeNode = { count: subset.length, countA, countB, label: countA >= countB ? 'A' : 'B', gini: 2 * p * (1 - p) };
    if (depth >= maxDepth || subset.length < minLeaf * 2 || node.gini === 0) return node;
    let best: { axis: 'x' | 'y'; threshold: number; impurity: number } | undefined;
    for (const axis of ['x', 'y'] as const) {
      const values = [...new Set(subset.map((point) => point[axis]))].sort((a, b) => a - b);
      for (let index = 0; index < values.length - 1; index++) {
        const threshold = (values[index]! + values[index + 1]!) / 2;
        const left = subset.filter((point) => point[axis] < threshold);
        const right = subset.filter((point) => point[axis] >= threshold);
        if (left.length < minLeaf || right.length < minLeaf) continue;
        const impurity = [left, right].reduce((sum, group) => {
          const fractionA = group.filter((point) => point.label === 'A').length / group.length;
          return sum + (group.length / subset.length) * 2 * fractionA * (1 - fractionA);
        }, 0);
        if (!best || impurity < best.impurity - 1e-10) best = { axis, threshold, impurity };
      }
    }
    if (!best || best.impurity >= node.gini - 1e-10) return node;
    return { ...node, axis: best.axis, threshold: best.threshold,
      left: grow(subset.filter((point) => point[best.axis] < best.threshold), depth + 1),
      right: grow(subset.filter((point) => point[best.axis] >= best.threshold), depth + 1) };
  };
  return grow(points, 0);
}

export function predictDecisionTree(tree: TreeNode, point: PlanePoint) {
  const path: string[] = [];
  let node = tree;
  while (node.axis && node.threshold !== undefined && node.left && node.right) {
    const goesLeft = point[node.axis] < node.threshold;
    path.push(`${node.axis === 'x' ? 'Eixo horizontal' : 'Eixo vertical'} ${goesLeft ? '<' : '≥'} ${node.threshold.toLocaleString('pt-BR', { maximumFractionDigits: 1 })}`);
    node = goesLeft ? node.left : node.right;
  }
  return { label: node.label, path, leaf: node };
}

export function followTree(humidity: number, temperature: number) {
  if (humidity < 45) return { decision: 'Regar', path: ['Umidade menor que 45%', 'Sim → regar'] };
  if (temperature > 30) return { decision: 'Observar de perto', path: ['Umidade menor que 45%', 'Não', 'Temperatura acima de 30 °C', 'Sim → observar de perto'] };
  return { decision: 'Aguardar', path: ['Umidade menor que 45%', 'Não', 'Temperatura acima de 30 °C', 'Não → aguardar'] };
}

export function assignClusters(points: readonly PlanePoint[], centroids: readonly PlanePoint[]) {
  if (centroids.length === 0) throw new Error('É necessário ao menos um centróide');
  return points.map((point) => {
    let cluster = 0;
    let bestDistance = Number.POSITIVE_INFINITY;
    centroids.forEach((centroid, index) => {
      const distance = Math.hypot(point.x - centroid.x, point.y - centroid.y);
      if (distance < bestDistance) {
        bestDistance = distance;
        cluster = index;
      }
    });
    return { ...point, cluster, distance: bestDistance };
  });
}

export function moveCentroids(assignments: ReturnType<typeof assignClusters>, centroids: readonly PlanePoint[]) {
  return centroids.map((centroid, index) => {
    const group = assignments.filter((point) => point.cluster === index);
    if (group.length === 0) return centroid;
    return {
      ...centroid,
      x: group.reduce((sum, point) => sum + point.x, 0) / group.length,
      y: group.reduce((sum, point) => sum + point.y, 0) / group.length,
    };
  });
}

export function withinClusterSumOfSquares(assignments: ReturnType<typeof assignClusters>): number {
  return assignments.reduce((sum, point) => sum + point.distance ** 2, 0);
}
