import { describe, expect, it } from 'vitest';
import { assignClusters, classifyKnn, followTree, logisticProbability, moveCentroids, predictDecisionTree, trainDecisionTree, trainLogistic, withinClusterSumOfSquares } from './experiments';

describe('experimentos dos modelos', () => {
  it('sigmoide cruza 50% no ponto central e aumenta com x', () => {
    expect(logisticProbability(5, 5, 1)).toBe(0.5);
    expect(logisticProbability(7, 5, 1)).toBeGreaterThan(logisticProbability(3, 5, 1));
  });

  it('treino logístico reduz perda em dados separáveis', () => {
    const history = trainLogistic([{ x: 2, label: 0 }, { x: 3, label: 0 }, { x: 7, label: 1 }, { x: 8, label: 1 }], 80, 0.5);
    expect(history.at(-1)!.loss).toBeLessThan(history[0]!.loss);
  });

  it('k-NN vota entre vizinhos realmente mais próximos', () => {
    const points = [
      { id: 'a1', x: 1, y: 1, label: 'A' as const },
      { id: 'a2', x: 2, y: 1, label: 'A' as const },
      { id: 'b1', x: 8, y: 8, label: 'B' as const },
    ];
    expect(classifyKnn(points, { id: 'novo', x: 1, y: 2 }, 3)).toMatchObject({ votesA: 2, votesB: 1, label: 'A' });
  });

  it('k-NN alterna distância e peso sem inventar treino', () => {
    const points = [{ id: 'a', x: 0, y: 0, label: 'A' as const }, { id: 'b1', x: 2, y: 2, label: 'B' as const }, { id: 'b2', x: 2, y: 3, label: 'B' as const }];
    expect(classifyKnn(points, { id: 'q', x: 0.1, y: 0.1 }, 3).label).toBe('B');
    expect(classifyKnn(points, { id: 'q', x: 0.1, y: 0.1 }, 3, 'manhattan', true).label).toBe('A');
  });

  it('árvore segue caminhos mutuamente exclusivos', () => {
    expect(followTree(30, 20).decision).toBe('Regar');
    expect(followTree(60, 32).decision).toBe('Observar de perto');
    expect(followTree(60, 22).decision).toBe('Aguardar');
  });

  it('árvore aprende divisão e usa profundidade máxima', () => {
    const points = [{ id: 'a1', x: 1, y: 1, label: 'A' as const }, { id: 'a2', x: 2, y: 2, label: 'A' as const }, { id: 'b1', x: 8, y: 1, label: 'B' as const }, { id: 'b2', x: 9, y: 2, label: 'B' as const }];
    expect(trainDecisionTree(points, 0).axis).toBeUndefined();
    const tree = trainDecisionTree(points, 1);
    expect(predictDecisionTree(tree, { id: 'q', x: 9, y: 1 }).label).toBe('B');
    expect(predictDecisionTree(tree, { id: 'q', x: 1, y: 1 }).label).toBe('A');
  });

  it('k-means atribui ao centróide mais próximo e calcula nova média', () => {
    const points = [{ id: 'p1', x: 1, y: 1 }, { id: 'p2', x: 3, y: 1 }, { id: 'p3', x: 9, y: 9 }];
    const centroids = [{ id: 'c1', x: 0, y: 0 }, { id: 'c2', x: 10, y: 10 }];
    const assigned = assignClusters(points, centroids);
    expect(assigned.map((point) => point.cluster)).toEqual([0, 0, 1]);
    expect(moveCentroids(assigned, centroids)).toEqual([{ id: 'c1', x: 2, y: 1 }, { id: 'c2', x: 9, y: 9 }]);
    expect(withinClusterSumOfSquares(assignClusters(points, moveCentroids(assigned, centroids)))).toBeLessThan(withinClusterSumOfSquares(assigned));
  });
});
