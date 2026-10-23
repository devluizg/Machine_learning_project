# Estado da implementação, atualização de 23/10/2026

O protótipo local tem cinco laboratórios autorais, com pergunta, hipótese, gráfico 2D, projeção 3D de grandeza matemática, controles, resultado textual, fórmula, reflexão e tarefa de aplicação. Cálculos e dados são locais; respostas não são transmitidas nem persistidas.

A página inicial e o cabeçalho dos módulos têm agora um fundo de pontos com reação ao cursor, controle de pausa e alternativa estática para movimento reduzido/toque. É uma camada decorativa em Canvas nativo, separada das visualizações didáticas.

- Linear: comparação manual/treinada, mínimos quadrados, outlier, resíduos e curva de MSE.
- SVM linear: fronteira manual ou sugerida, margem, vetores de suporte e classificação de ponto novo.
- k-NN: distância, k, voto ponderado e regiões; sem treino de parâmetros por definição.
- Árvore: divisões treinadas por Gini e caminho de decisão.
- k-means: atribuição, movimento dos centróides e WSS.
- Síntese do encontro 7: comparação de finalidade, entrada, saída, mecanismo, controle e limite dos cinco modelos.
- Roteiro docente: oito encontros de cinquenta minutos, acesso direto aos recursos e versão para impressão.
- Percurso do estudante: oito aulas com objetivo, ação, explicação esperada e indicação de uso ou não uso do site.
- Contexto do encontro: os cinco módulos identificam a aula e destacam previsão, ação obrigatória e explicação.
- Modo aula: percurso inicial focado; controles avançados e 3D permanecem como aprofundamento opcional.
- Ajuda: teclado, reinício, redução de movimento, leitura textual dos dados, uso local e glossário.
- Materiais docentes: PDFs públicos das aulas 2 a 7; diagnóstico e instrumento final permanecem fora do site.
- Versão de aplicação: identificação `0.2.0-campo` no rodapé e instruções para execução local.
- `npm run build`, `npm run lint`, `npm run test:run`: aprovados; 34 testes.

Pendente: revisão com professor e estudantes, teste formal com leitor de tela, verificação de contraste e projeção nos equipamentos reais do laboratório, revisão dos instrumentos da pesquisa e decisões sobre modelos e identidade final. A [matriz de validação](VALIDACAO_CINCO_MODELOS.md) discrimina funções implementadas e lacunas frente à referência.
