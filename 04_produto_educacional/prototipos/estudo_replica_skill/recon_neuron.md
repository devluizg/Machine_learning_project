# Reconhecimento público e clean-room do NEURON

## Limites da observação

Foram usadas apenas telas públicas e navegação normal. Não houve inspeção de código, bundles, chamadas de rede, APIs ou áreas privadas. Este documento registra categorias de fluxo e interação para informar um produto autoral; não é uma especificação para reprodução da referência.

## Inventário enxuto de telas

| Tela pública observada | Papel geral observado | Aproveitamento permitido como categoria |
| --- | --- | --- |
| Inicial | Apresenta proposta de aprendizagem visual e acesso à exploração. | Porta de entrada curta que explique o propósito da plataforma própria. |
| Atlas/índice | Agrupa modelos em famílias e oferece filtros. | Índice reduzido, organizado pelos poucos modelos que forem aprovados. |
| Glossário | Lista termos e conecta definições aos módulos. | Glossário contextual, em linguagem introdutória e ligado ao ponto de uso. |
| Regressão linear | Explora ajuste, resíduos, erro e aprendizagem iterativa. | Categoria “dados + linha + erro + efeito de parâmetros”. |
| Regressão logística | Apresenta intuição, sigmoide, probabilidade e laboratório com controles de classificação. | Categoria “entrada + probabilidade + limiar + decisão”, com muito menos controles. |
| Classificação k-NN | Explora vizinhança, distância, votação e fronteiras de decisão. | Categoria “pontos rotulados + regra local + fronteira visível”. |
| Árvore de decisão | Relaciona perguntas sucessivas, regiões divididas no plano e representação da árvore. | Categoria “regra + divisão + caminho até a decisão”. |
| Agrupamento k-means | Explora atribuição, centróides, iterações e dispersão. | Categoria “dados sem rótulo + grupos provisórios + atualização”. |

## Fluxo de aprendizagem observado

1. Selecionar uma família ou modelo no atlas.
2. Avançar por seções consistentes: intuição, laboratório, matemática, perspectivas e prática.
3. Alterar dados ou parâmetros no laboratório e observar gráficos, métricas ou estados atualizados.
4. Relacionar a mudança com fórmula, legenda ou explicação textual.
5. Retomar conceitos por glossário e navegar a outros modelos.

**Inferência:** a repetição das seções parece reduzir a carga de navegação e cria uma rotina de estudo. Para o produto próprio, essa rotina só é útil se cada seção responder a um objetivo de aprendizagem explícito.

## Componentes recorrentes

- Navegação por atlas/família de modelos e por seções do módulo.
- Explicação conceitual ao lado ou antes da exploração.
- Gráfico de pontos, linha/curva, regiões de decisão ou agrupamentos por cor.
- Controles numéricos, seleção de conjunto de dados, alternâncias e botões de etapa/iteração.
- Métricas, legendas e observações ligadas ao estado do experimento.
- Fórmula acompanhada por referências a elementos visuais.
- Glossário navegável e alternância de tema claro/escuro.

## Estados importantes observados

| Estado | Evidência pública | Relevância para o produto próprio |
| --- | --- | --- |
| Dados iniciais e dados alterados | Inclusão de ruído, quantidade de pontos, forma ou outliers. | Tornar a relação entre dados e resultado observável. |
| Parâmetro alterado | Taxa de aprendizagem, passos, `k`, métrica, número de grupos e inicialização. | Limitar controles a parâmetros que o estudante consiga interpretar. |
| Etapa de cálculo/iteração | Curva de perda, atribuição e atualização visualizadas por passo. | Oferecer pausar, avançar e reiniciar com explicação. |
| Variação de visualização | Dados, contornos, perda, vista superior/3D e regiões de decisão. | Priorizar vista 2D e alternativa textual; 3D somente se tiver propósito didático. |
| Resultado/métrica | R², RMSE, acurácia, WSS e curva de cotovelo. | Mostrar métrica apenas depois de explicar o que ela responde. |

## Padrões de interação observados

- Regressão linear: pontos, reta ajustada, resíduos e quadrados de erro; controles de tamanho da amostra, ruído, taxa, passos, outliers e novo conjunto; comparação de estratégias de ajuste.
- Regressão logística: probabilidade e sigmoide são relacionadas a uma fronteira de decisão; o laboratório público oferece vários controles de treino e vistas alternativas. Nosso protótipo usa uma sigmoide didática sem simular treinamento.
- Classificação k-NN: escolha de forma dos dados, `k`, métrica e ponderação; clique para destacar vizinhos; regiões de decisão e resultado por valor de `k`.
- Árvore de decisão: o laboratório público apresenta regiões separadas por cortes, uma árvore aprendida e controles como profundidade e critério. Nosso protótipo apresenta uma árvore fixa para explicar apenas regras, divisões e caminho; não afirma aprender a árvore.
- Agrupamento k-means: escolha de `k`, dispersão, formato e inicialização; iteração que alterna atribuição e reposicionamento; soma de quadrados e curva de cotovelo.

**Inferência:** a combinação “controle pequeno → consequência gráfica imediata → frase explicativa” é transferível para o Ensino Médio. A quantidade de opções simultâneas observada, porém, deve ser reduzida.

## Acessibilidade observável e limites

Foram percebidos controles e links nomeados, foco navegável na interface, alternância claro/escuro e eixos/legendas textuais. Não foram verificados formalmente uso integral por teclado, leitor de tela, contraste, responsividade ou equivalentes não visuais para gráficos 3D/canvas. Isso deve ser requisito de projeto, não uma inferência de conformidade da referência.

## Elementos fora do nosso produto nesta etapa

- Nome, logotipo, textos, exemplos, ilustrações, paleta e organização visual distintiva do NEURON.
- Inglês/alemão como idioma-base: o produto será planejado em português brasileiro.
- Catálogo amplo de famílias e dezenas de termos de glossário.
- Conteúdos avançados sem andaime, como decomposições matriciais, inferência estatística, dimensão elevada, kernels, NP-hard, GMM e HNSW.
- Controles 3D, múltiplas métricas e opções técnicas quando não puderem ser justificados por um objetivo de aprendizagem para iniciantes.

## Referências de observação pública

- [Inicial](https://kw1fpt-ahmet-duyar.shinyapps.io/Neuron/#/)
- [Atlas](https://kw1fpt-ahmet-duyar.shinyapps.io/Neuron/#/atlas)
- [Glossário](https://kw1fpt-ahmet-duyar.shinyapps.io/Neuron/#/glossar)
- [Regressão linear](https://kw1fpt-ahmet-duyar.shinyapps.io/Neuron/#/m/linreg)
- [Regressão logística](https://kw1fpt-ahmet-duyar.shinyapps.io/Neuron/#/m/logreg)
- [k-NN](https://kw1fpt-ahmet-duyar.shinyapps.io/Neuron/#/m/knn)
- [Árvore de decisão](https://kw1fpt-ahmet-duyar.shinyapps.io/Neuron/#/m/tree)
- [k-means](https://kw1fpt-ahmet-duyar.shinyapps.io/Neuron/#/m/kmeans)
