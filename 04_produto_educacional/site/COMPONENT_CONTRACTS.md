# Contratos dos componentes da fatia vertical

| Componente | Responsabilidade e entradas | Saídas, estados e eventos | Teclado, acessibilidade e falhas |
| --- | --- | --- | --- |
| `ModuleShell` | Recebe estado e ações do módulo; compõe T01–T06. | Renderiza etapa atual; eventos avançar, voltar e reiniciar. | Ordem de foco inicia no título da etapa; anuncia mudança de etapa; preserva textos em erro. |
| `StepNavigator` | Recebe etapa atual e regras de habilitação. | Emite navegação válida, sem pular revelações. | Botões nativos com estado desabilitado explicado; falha é bloqueio de regra, não erro técnico. |
| `InitialPredictionForm` | Recebe/preenche previsão e justificativa. | Emite atualização e confirmação de registro. | `label` visível, ajuda contextual e erros de campo em texto; campos vazios não revelam referência. |
| `ParameterControls` | Recebe `a`, `b`, limites, passos e ações. | Emite alteração discreta; valores e unidades atualizados. | Botões e entradas nativas; seta/Tab operáveis; foco visível; limite anunciado. Falha: rejeitar atualização inválida e manter valor anterior. |
| `RegressionChart` | Recebe pontos ativos, duas retas, resíduos, seleção, eixos fixos. | SVG e evento de seleção. | Cada ponto tem nome e controle equivalente na tabela; linha manual/referência distinguíveis sem cor; se SVG falhar, sinaliza indisponibilidade sem destruir dados. |
| `DataTable` | Recebe a mesma série calculada do gráfico. | Tabela e evento de seleção. | Cabeçalhos com unidades, linha selecionada identificada por texto e foco; é alternativa completa quando gráfico falha. |
| `ResidualToggle` | Recebe visibilidade e regra da etapa. | Alterna somente segmentos/coluna, não cálculos. | Controle com `aria-pressed` ou checkbox e anúncio de estado. |
| `MathCards` | Recebe etapa dos cartões e resultados selecionados. | Revela fórmula seguinte e navegação de retorno. | Fórmula tem texto de leitura, símbolos e unidades definidos; sem animação obrigatória. |
| `FitComparison` | Recebe OLS independente, reta manual e regra de liberação. | Revela referência sem alterar `aManual`/`bManual`. | Rótulos incluem coeficientes reais, inclusive `a=1,282903` com P07; falha de OLS mostra mensagem e último resultado. |
| `OutlierChallenge` | Recebe previsão de P07, visibilidade e ações. | Registra previsão e só então emite inclusão/remoção de P07. | Texto informa resultado oculto; P07 tem rótulo textual, não julgamento de erro. |
| `FeedbackRegion` | Recebe comparação derivada e erro atual. | Texto determinístico em região de status. | Não repete tabela inteira; nenhuma informação apenas por cor. |
| `SynthesisForm` | Recebe três respostas e regras de reinício. | Emite atualizações e confirmação de descarte. | Campos rotulados; feedback por critérios, sem “certo/errado”; falha preserva texto. |
