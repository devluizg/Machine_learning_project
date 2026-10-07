# Estado da implementação — 03/10/2026

O protótipo local tem cinco laboratórios autorais, com pergunta, hipótese, gráfico 2D, projeção 3D de grandeza matemática, controles, resultado textual, fórmula, reflexão e tarefa de aplicação. Cálculos e dados são locais; respostas não são transmitidas nem persistidas.

A página inicial e o cabeçalho dos módulos têm agora um fundo de pontos com reação ao cursor, controle de pausa e alternativa estática para movimento reduzido/toque. É uma camada decorativa em Canvas nativo, separada das visualizações didáticas.

- Linear: comparação manual/treinada, mínimos quadrados, outlier, resíduos e curva de MSE.
- Logística: dados separados/sobrepostos, ajuste por perda logarítmica, limiar e curva de perda.
- k-NN: distância, k, voto ponderado e regiões; sem treino de parâmetros por definição.
- Árvore: divisões treinadas por Gini e caminho de decisão.
- k-means: atribuição, movimento dos centróides e WSS.
- `npm run build`, `npm run lint`, `npm run test:run`: aprovados; 28 testes.

Pendente: revisão com professor e estudantes, teste formal de acessibilidade/responsividade, instrumentos da pesquisa e decisões sobre modelos e identidade final. A [matriz de validação](VALIDACAO_CINCO_MODELOS.md) discrimina funções implementadas e lacunas frente à referência.
