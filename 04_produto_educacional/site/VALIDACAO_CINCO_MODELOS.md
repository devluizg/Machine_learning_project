# Validação do protótipo ampliado — 03/10/2026

Comparação clean room de fluxos públicos do [NEURON](https://kw1fpt-ahmet-duyar.shinyapps.io/Neuron/) com objetivos próprios do Ensino Médio. `replica-recon` identificou padrões, `replica-architect` delimitou a implementação local, `replica-design` orientou visualização autoral, `replica-test` verificou interações e `replica-diff` registrou as lacunas. Não se busca paridade visual, textual ou de código.

## Rastreabilidade funcional

| Modelo | Interações implementadas | Aprendizagem observável | Ainda não incluído |
| --- | --- | --- | --- |
| Regressão linear | Reta manual, outlier, resíduos, OLS, treino por etapas/taxa, MSE, curva e perda 3D | Comparar ajuste, erro e influência de ponto atípico | Aleatorização, R², quadrados desenhados, contornos de perda |
| Regressão logística | Dois conjuntos, curva manual, limiar, treino por log-loss, casos sintéticos reservados, perda 3D | Separar chance, decisão, ajuste dos pesos e resultado fora do treino | Duas características, fronteira planar, validação externa, regularização |
| k-NN | Dois conjuntos, k, duas distâncias, voto ponderado, regiões, força do voto 3D | Ver efeito da vizinhança e da definição de proximidade | Curva de acurácia por k, teste independente, mais formas de dados |
| Árvore de decisão | Divisões aprendidas por Gini, profundidade, regiões, regras, caminho, casos sintéticos reservados e proporção da folha 3D | Relacionar perguntas, regiões e diferença entre treino e teste | Critério entropia, validação externa, amostras/ruído ajustáveis |
| k-means | k, forma, inicialização, atribuir/mover, WSS por rodada e distância 3D | Observar a atualização dos centros e queda da WSS | Curva do cotovelo, k-means++, mais conjuntos e animação automática |

As vistas 3D são projeções rotacionáveis em SVG de valores calculados. A altura **não** afirma terceira característica dos dados. k-NN não tem etapa de treinamento de parâmetros; essa ausência é explicitada ao estudante. A [camada guiada para iniciantes](PLANO_APRENDIZAGEM_INICIANTES.md) acrescenta situações fictícias, cálculo do estado atual, retorno a questões de compreensão e tabelas textuais.

## Verificações

- `npm run build`, `npm run lint` e `npm run test:run`: aprovados; 28 testes de domínio.
- Navegador local: conferidos os cinco módulos, início do treino linear/logístico, divisões da árvore, alternância 2D/3D do k-NN e queda da WSS após atualizar centróides.
- Gráficos possuem descrições textuais; tabela da regressão e lista de regras da árvore oferecem alternativas. Isso **não substitui** teste formal de teclado, leitor de tela, contraste e uso móvel.

## Pendências pedagógicas e técnicas

1. Validar exemplos, matemática em camadas e volume de controles com professor e estudantes. Mais recursos podem aumentar carga cognitiva.
2. Os casos reservados de logística e árvore são somente ilustrações sintéticas. Antes de qualquer afirmação sobre generalização serão necessários dados e desenho de avaliação apropriados; os demais modelos ainda não exibem teste independente.
3. Auditar acessibilidade das superfícies 3D, das cores e das interações móveis com participantes reais.
4. A lista final de modelos, a identidade e a metodologia da pesquisa ainda aguardam decisões acadêmicas.
