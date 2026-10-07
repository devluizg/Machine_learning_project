# Arquitetura mínima da fatia vertical

> Histórico do plano original de regressão linear. Em 03/10/2026, o protótipo foi ampliado por solicitação de Luiz para cinco módulos, reutilizando a mesma pilha estática e estado local. O código atual está em `src/learning/` para os novos experimentos; as etapas completas T01–T06 abaixo continuam como plano, não como funcionalidade concluída.

## Visão geral

Uma aplicação estática em Vite + React + TypeScript carrega dados locais, calcula o experimento com funções puras e deriva, a partir de um único estado local, a tela T01–T06, SVG, tabela, descrição e feedback.

```text
dados locais ──> domínio matemático puro ──> estado do módulo
                      ↑                         │
controles e etapas ───┴─────────────────────────┤
                                                ├── etapas T01–T06
                                                ├── SVG + tabela + descrição
                                                ├── feedback e região de status
                                                └── formulário de síntese
```

## Fluxo de dados

1. `dados/regressaoLinear.ts` define os seis pontos-base, P07 e metadados de unidades; nenhum dado vem da rede.
2. O estado seleciona conjunto ativo, parâmetros manuais e visibilidades.
3. Funções puras calculam previsões, resíduos, SSE, MSE e OLS a partir de números completos.
4. Um seletor deriva duas séries: a reta manual e, quando solicitada, a referência OLS do conjunto ativo.
5. SVG, tabela, descrição textual e feedback recebem o mesmo resultado derivado; nenhum deles recalcula por conta própria.

## Domínio matemático

Funções sem acesso ao DOM ou ao estado de React:

| Função | Entrada | Saída/contrato |
| --- | --- | --- |
| `prever` | `a`, `b`, `x` | `ŷ = a + bx`, sem arredondamento. |
| `calcularResiduos` | pontos, reta | linhas com `ŷ`, `e = y−ŷ` e `e²`. |
| `calcularSSE` / `calcularMSE` | resíduos | números em cm²; `MSE = SSE/n`. |
| `regressaoOLS` | pelo menos dois `x` distintos | `{a,b}` de mínimos quadrados com intercepto; erro explícito se denominador for zero. |
| `formatar` | número, precisão, unidade | apenas texto de exibição; nunca retorna valor para novo cálculo. |
| `compararExperimentos` | estado anterior e atual | diferenças numéricas e direção para feedback determinístico. |

Aceitar variação interna de até `0,000001` nos testes numéricos. A referência sem P07 é `a=0,042667`, `b=0,098829`; com P07 é `a=1,282903`, `b=0,085540` quando exibida a seis casas.

## Estado local do módulo

| Campo | Classe | Regra |
| --- | --- | --- |
| `etapaAtual` (`T01`–`T06`) | sessão | Avança/recua por regras pedagógicas. |
| `aManual`, `bManual` | sessão, reiniciável | Iniciam em `0,5` e `0,06`; limites da especificação. |
| `residuosVisiveis`, `retaAjustadaVisivel`, `p07Visivel` | sessão, reiniciável | Liberação progressiva; não sincronizar com controles. |
| `pontoSelecionado` | sessão, reiniciável | Identificador ou `null`. |
| previsão e justificativa iniciais; previsão de P07; sínteses | sessão, preservável | Preservar em falha recuperável e solicitar confirmação antes de descarte. |
| `erro` | sessão | Descreve falha de cálculo ou gráfico; último resultado válido permanece. |
| `movimentoReduzido` | derivado da preferência do dispositivo, com opção local | Desliga transições não essenciais. |

São derivados, não armazenados: pontos ativos, linhas calculadas, SSE/MSE manual, OLS, SSE/MSE OLS, descrição textual e feedback. `Reiniciar` restaura apenas estado numérico e de visibilidade; textos só são apagados após confirmação explícita. Não há persistência entre sessões, armazenamento remoto ou conta.

## Visualização e acessibilidade

SVG nativo recebe domínios fixos `x: 0–70 g` e `y: -0,5–10 cm`. Deve desenhar eixos, pontos, reta manual, reta ajustada rotulada, resíduos e seleção. Linha manual e referência usam padrão/traço/rótulo além de cor; P07 recebe forma e texto distintos. A reta OLS usa seus coeficientes reais mesmo quando `a=1,282903` excede o máximo manual de `1,0`; ela não move controles e permanece dentro do eixo vertical.

A tabela mostra o conjunto ativo com `x`, `y`, `ŷ`, `e`, `e²`, SSE e MSE. A descrição persistente resume conjunto, parâmetros, visibilidades, ponto selecionado e valores relevantes. Controles nativos têm rótulo, unidade e valor; ordem de foco segue conteúdo, controles, tabela e navegação. Uma região de status anuncia somente a consequência da ação. Fórmulas recebem leitura textual equivalente. `prefers-reduced-motion` elimina animações.

## Erros

Atualizações numéricas são atômicas: validar o novo valor, calcular por completo e então substituir o resultado; em erro, manter último resultado válido e anunciar. Falha de SVG não bloqueia tabela, descrição, controles ou formulários. O estado de erro não descarta respostas da sessão.

## Estrutura proposta

```text
04_produto_educacional/site/
├── ADR-001-STACK.md
├── ARCHITECTURE.md
├── COMPONENT_CONTRACTS.md
├── TEST_STRATEGY.md
├── BUILD_ROADMAP.md
├── SCOPE_FENCE.md
└── src/                         # criado apenas na implementação posterior
    ├── data/regressao-linear.ts
    ├── domain/regression.ts
    ├── state/useRegressionModule.ts
    ├── components/{ModuleShell,StepNavigator,ParameterControls,DataTable,FeedbackRegion}.tsx
    ├── visualization/RegressionChart.tsx
    ├── steps/{T01Situation,T02ManualLine,T03Residuals,T04Math,T05Outlier,T06Synthesis}.tsx
    ├── accessibility/{chartDescription,announcements}.ts
    ├── styles/{tokens,global,module}.css
    └── tests/{unit,component,e2e}/
```

`src/` é uma árvore planejada, não criada nesta etapa. Não há backend porque todos os dados, cálculos e respostas ficam no navegador; Vite pode gerar um site estático para hospedagem futura.
