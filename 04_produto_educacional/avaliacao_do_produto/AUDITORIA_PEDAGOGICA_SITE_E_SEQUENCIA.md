# Auditoria pedagógica do protótipo frente à sequência didática

**Data:** 18 de outubro de 2026
**Escopo:** verificação de aderência entre o protótipo local, a sequência de oito encontros, a matriz curricular e os instrumentos preliminares.  
**Não é:** validação com estudantes, teste de acessibilidade completo ou avaliação de aprendizagem.

## 1. Resultado geral

O protótipo já oferece a estrutura central necessária à sequência: introdução para iniciantes, módulo guiado, pergunta de previsão, controle principal, consequência visual e numérica, explicação matemática, espaço de explicação própria, verificação imediata e discussão de limite. Essa arquitetura está alinhada ao ciclo prever, experimentar, observar e explicar.

A revisão técnica também foi executada no estado atual do site:

- npm run lint: aprovado;
- npm run test:run: aprovado, com 34 testes;
- npm run build: aprovado.

A auditoria registra aderência pedagógica a partir da inspeção do protótipo e dos documentos. Essa inspeção não constitui validação com estudantes. Os cenários da sequência foram alinhados aos conjuntos sintéticos atualmente exibidos no site. O núcleo final comparável seguirá a matriz de correspondência com o diagnóstico, enquanto o desafio de transferência utilizará situações diferentes das aulas.

## 2. Aderência por módulo

| Módulo | Ação essencial da sequência | Recurso já implementado | Situação | Ajuste pedagógico necessário |
| --- | --- | --- | --- | --- |
| Regressão linear | Alterar inclinação e interpretar previsão, resíduo e erro na relação entre passos e distância. | Inclinação, reta manual ou treinada, previsão para 20 passos, resíduos, MSE e aula guiada. | Aderente após alinhamento documental. | Usar na sequência o mesmo cenário do site: passos e distância percorrida. |
| Regressão logística | Alterar limiar e distinguir probabilidade de classificação. | Limiar, curva, dados separados ou sobrepostos, treino e questão guiada. | Aderente. | Tornar o cenário do sensor mais concreto e manter o mesmo vocabulário no instrumento final. |
| k-vizinhos mais próximos (k-NN) | Alterar k e explicar decisão por proximidade e votação em amostras descritas por doçura e acidez. | Número de vizinhos, distância, vizinhos destacados, votos e questão guiada. | Aderente após alinhamento documental. | Usar na sequência o mesmo cenário do site: amostras por doçura e acidez. |
| Árvore de decisão | Alterar profundidade e explicar regras e caminhos com objetos descritos por largura e altura. | Profundidade, regra inicial, caminho destacado, regiões e questão guiada. | Aderente após alinhamento documental. | Usar na sequência o mesmo cenário do site: objetos por largura e altura. |
| k-means | Alternar atribuição e movimento dos centróides em amostras sem rótulos descritas por doçura e acidez. | Atribuição, movimento, número de grupos, WSS e questão guiada. | Aderente após alinhamento documental. | Usar na sequência o mesmo cenário do site e explicitar ausência de rótulos: amostras por doçura e acidez. |
| Comparação | Escolher finalidade e modelo em situação nova. | Síntese explícita com finalidade, entrada, saída, mecanismo, controle e limite dos cinco modelos. | Aderente no protótipo. | Validar clareza e tempo de uso durante o piloto. |

## 3. Ajustes priorizados

### Prioridade 0: necessários antes da aplicação em campo

1. **Escolher e padronizar os cinco cenários.**  
   Os roteiros dos encontros 2, 4, 5 e 6 foram alinhados aos cenários atuais do site: passos e distância percorrida; amostras por doçura e acidez; objetos por largura e altura; e amostras sem rótulos por doçura e acidez. O núcleo final comparável seguirá a matriz definida com o diagnóstico. O desafio de transferência manterá situações diferentes das aulas. Essa decisão documental não declara validação com estudantes.

2. **Revisar acessibilidade e infraestrutura em uso real.**  
   O site possui alternativas textuais, controles nativos, descrições e preferência por redução de movimento. Ainda assim, faltam teste manual por teclado, leitor de tela, contraste, navegação em tela menor e projeção em laboratório. Isso deve ocorrer antes de levar o protótipo à turma.

3. **Verificar a linguagem de cada tela com o nível introdutório.**  
   MSE, perda logarítmica, Gini e WSS podem permanecer como aprofundamento, mas a aula guiada deve apresentar primeiro a interpretação em linguagem comum. O professor não precisa explorar todos os controles do modo livre durante os 50 minutos.

### Prioridade 1: melhora importante da aplicação

4. **Síntese comparativa para o encontro 7 implementada no protótipo.**
   O recurso compara finalidade, dados de entrada, saída, mecanismo, controle principal e limite de regressão linear, regressão logística, k-NN, árvore e k-means. Ele não calcula nada novo nem coleta respostas.

5. **Roteiro docente implementado no protótipo.**
   O roteiro apresenta os oito encontros, a distribuição de cinquenta minutos, a pergunta orientadora, a síntese esperada e o acesso ao recurso de cada aula. Há uma versão para impressão. A implementação não pressupõe teste ou validação com estudantes.

6. **Reduzir a concorrência visual nas primeiras explorações.**  
   As vistas 3D, os controles avançados e as métricas de treino devem ficar fora do foco inicial de cada aula. O modo guiado já ajuda; falta confirmar em uso que nenhum controle secundário distraia a atenção do estudante.

### Prioridade 2: somente depois da primeira aplicação ou se o orientador solicitar

7. Fazer ajustes de identidade visual ou acrescentar outros conjuntos de dados.
8. Criar novos modos de avaliação automática, persistência de respostas, conta de estudante ou qualquer coleta digital. Esses recursos não são necessários ao desenho atual e alterariam o escopo e a análise ética.
9. Acrescentar algoritmos, métricas ou formalizações matemáticas avançadas.

## 4. Mapa de coerência entre aula e site

| Aula | Elemento que deve ser usado no site | Elemento que não deve ser obrigatório |
| --- | --- | --- |
| 1 | Introdução inicial: dados, modelo, treino ou consulta, teste, classificação e agrupamento. | Exploração livre, vista 3D e fórmulas. |
| 2 | Passos e distância percorrida, inclinação, previsão em ponto fixo, resíduo e gráfico de reta. | Superfície 3D, taxa de aprendizagem, ponto atípico. |
| 3 | Limiar, probabilidade e classe resultante. | Treino por perda logarítmica e superfície 3D. |
| 4 | Amostras por doçura e acidez, valor de k, distâncias, vizinhos destacados e votos. | Métrica Manhattan, voto ponderado, regiões e vista 3D. |
| 5 | Objetos por largura e altura, profundidade pequena, regra e caminho da decisão. | Cálculo formal de Gini, regiões completas e vista 3D. |
| 6 | Amostras sem rótulos por doçura e acidez; atribuir pontos e mover centróides. | WSS como fórmula, outras formas de dados e vista 3D. |
| 7 | Navegação entre módulos e síntese comparativa disponível na rota de comparação. | Repetir o treino ou todas as métricas de cada modelo. |
| 8 | Nenhum uso durante a resposta individual ao desafio final. | Consulta ao site, internet ou materiais de aula. |

## 5. Decisão recomendada

Recomenda-se manter os mecanismos e controles já implementados e realizar uma adaptação pedagógica focalizada, começando pelos cenários e textos. A decisão registrada para execução agora é:

1. alinhar documentalmente os encontros 2, 4, 5 e 6 aos cenários atuais do site;
2. usar a síntese comparativa do encontro 7 e o roteiro docente já implementados;
3. manter os instrumentos em contextos distintos para observar transferência;
4. executar teste manual de acessibilidade e projeção antes do uso em campo;
5. revisar a sequência e os instrumentos contra a versão consolidada do site.

As ações documentadas nesta auditoria não representam validação com estudantes. Até aqui, trata-se de inspeção do protótipo e alinhamento de planejamento.

Esse caminho mantém o produto enxuto e preserva o rompimento com uma plataforma que apenas exibe resultados prontos.
