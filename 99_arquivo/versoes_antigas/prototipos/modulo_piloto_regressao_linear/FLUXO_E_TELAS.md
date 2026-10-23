# Fluxo e telas — módulo-piloto de regressão linear

## Fluxo principal

**prever → alterar → observar → explicar**. A pessoa estudante só recebe a reta ajustada depois de manipular uma reta própria e refletir sobre os resíduos.

## T01 — Situação e previsão inicial

- **Propósito pedagógico:** ativar a ideia de tendência antes de apresentar fórmula ou ajuste automático.
- **Conteúdo:** breve cenário da mola, pergunta orientadora e seis medições sintéticas; campos “Para uma massa intermediária, o alongamento será aproximadamente…” e “Por quê?”.
- **Interação:** escolher ou digitar uma previsão e uma justificativa curta; avançar sem correção binária.
- **Resposta esperada:** estimativa coerente com o crescimento geral e justificativa baseada na observação, mesmo que imprecisa.
- **Feedback:** “Sua previsão será comparada com uma reta que você vai ajustar; procure depois explicar o que a sustentava ou a faria mudar.”
- **Componentes:** título, texto do contexto, tabela compacta de dados, campo de previsão, campo de justificativa, botão Avançar.
- **Estados:** normal: dados e campos disponíveis; vazio: aviso orienta a registrar uma estimativa, mas permite explorar; carregando: indicador textual “preparando dados sintéticos”; erro: mensagem com opção de tentar novamente ou continuar com tabela estática.
- **Acessibilidade:** campos rotulados, instruções antes dos campos, ordem de tabulação linear, foco visível, tabela legível por leitor de tela e alternativa de leitura dos pares de dados.

## T02 — Pontos e reta manual

- **Propósito pedagógico:** reconhecer a tendência e testar como uma reta pode representá-la.
- **Conteúdo:** gráfico massa × alongamento, reta manipulável e explicação curta de inclinação `b` (cm/g) e intercepto `a` (cm). A reta ajustada, os resíduos e o ponto atípico ainda não são mostrados nesta etapa.
- **Interação:** mover inclinação e intercepto por teclado ou controles equivalentes; reiniciar experimento.
- **Resposta esperada:** aproximar a reta do conjunto como um todo, não apenas de um ponto.
- **Feedback:** descrição atualizada, por exemplo: “A reta sobe mais rapidamente; para a mesma massa, as previsões ficaram maiores.”
- **Componentes:** gráfico 2D, painel de explicação, controles de inclinação e intercepto, descrição textual do gráfico, tabela alternativa, botão Reiniciar.
- **Estados:** normal: pontos e reta visíveis; vazio: mensagem se os dados não estiverem disponíveis; carregando: desenho estático com status textual; erro: tabela alternativa permanece disponível e explica que o gráfico não pôde ser exibido.
- **Acessibilidade:** cada controle tem rótulo, valor atual e instrução de teclado; gráfico tem resumo textual atualizado; pontos possuem identificação também na tabela; cores não são a única distinção.

## T03 — Resíduos visíveis

- **Propósito pedagógico:** relacionar diferença vertical entre observado e previsto ao resíduo.
- **Conteúdo:** segmentos verticais entre cada ponto e a reta, mais uma explicação de valor observado `y` (cm), previsto `ŷ` (cm) e resíduo `eᵢ = yᵢ − ŷᵢ` (cm).
- **Interação:** mostrar ou esconder resíduos; selecionar um ponto na tabela ou no gráfico para destacar seu par `y` e `ŷ`.
- **Resposta esperada:** dizer que um resíduo positivo indica ponto acima da reta e um negativo, ponto abaixo.
- **Feedback:** explica a diferença selecionada, sem classificar a resposta apenas como certa ou errada.
- **Componentes:** gráfico, alternância “Mostrar resíduos”, tabela com `x`, `y`, `ŷ` e `eᵢ`, painel de explicação do ponto selecionado.
- **Estados:** normal: resíduos e tabela sincronizados; vazio: instrução para voltar e carregar os dados; carregando: aviso textual de atualização; erro: valores do ponto selecionado aparecem em texto e a alternância informa indisponibilidade visual.
- **Acessibilidade:** alternância operável por teclado; seleção indicada por texto, contorno e símbolo; tabela é equivalente informacional do gráfico; redução de movimento desativa transições dos segmentos.

## T04 — Matemática em camadas

- **Propósito pedagógico:** dar significado à notação depois da experiência visual.
- **Conteúdo:** três cartões progressivos: `ŷ = a + bx` (cm); `eᵢ = yᵢ − ŷᵢ` (cm); `MSE = (1/n) Σ(yᵢ − ŷᵢ)²` (cm²). O cartão final esclarece que, com `n` fixo, minimizar MSE e minimizar a soma dos resíduos ao quadrado seleciona a mesma reta.
- **Interação:** revelar um cartão por vez; retornar ao ponto selecionado e observar o valor correspondente quando a reta muda.
- **Resposta esperada:** localizar no gráfico ou na tabela cada elemento da fórmula e explicar sua necessidade.
- **Feedback:** para previsão, informa que a fórmula calcula a altura da reta; para resíduo, que mede a diferença vertical e seu sinal; para MSE, que é a média dos desvios ao quadrado, dá peso maior aos grandes afastamentos e serve de critério para comparar retas no mesmo conjunto.
- **Componentes:** cartões de fórmula, glossário contextual de símbolos, ligação textual ao gráfico/tabela, botão Voltar ao experimento.
- **Estados:** normal: cartões em sequência; vazio: símbolos exibidos com exemplo textual quando não houver ponto selecionado; carregando: status textual; erro: fórmulas permanecem legíveis e os vínculos dinâmicos informam indisponibilidade.
- **Acessibilidade:** fórmulas têm leitura textual equivalente, símbolos são definidos no próprio cartão, abertura não depende de animação, foco vai ao título do cartão revelado.

## T05 — Comparação e ponto atípico

- **Propósito pedagógico:** comparar uma escolha manual a uma referência ajustada e interpretar a influência de um caso incomum.
- **Conteúdo:** primeiro, uma descrição de que uma nova medida candidata ficou muito distante da tendência; somente após a previsão, a tela mostra o ponto atípico sintético. A reta ajustada é disponibilizada como referência porque a tentativa manual já ocorreu em T02.
- **Interação:** responder à previsão sobre o possível efeito do ponto; adicionar o ponto; mostrar a reta ajustada; comparar MSE e resíduos; remover o ponto para nova comparação.
- **Resposta esperada:** reconhecer que um ponto muito afastado pode elevar o MSE e deslocar a reta que minimiza a soma dos resíduos ao quadrado (ou, com `n` fixo, o MSE).
- **Feedback:** primeiro registra a previsão sem revelar o resultado; depois contrasta as duas situações em linguagem qualitativa e convida a investigar a origem do ponto, em vez de removê-lo automaticamente.
- **Componentes:** pergunta de previsão, gráfico comparativo após a resposta, botão “Mostrar reta ajustada”, alternância do ponto atípico, descrição textual comparativa, acesso à tabela alternativa, botão Reiniciar.
- **Estados:** normal: comparação disponível; vazio: explicação de que os dados base são necessários; carregando: aviso “calculando a comparação”; erro: a previsão e a tabela permanecem, com mensagem de que a referência ajustada não está disponível.
- **Acessibilidade:** as retas têm rótulos e estilos não cromáticos; ponto atípico recebe rótulo textual na tabela e no gráfico; mudança de estado é anunciada sem movimento obrigatório.

## T06 — Síntese e limitações

- **Propósito pedagógico:** consolidar os três objetivos e delimitar o que a representação linear não garante.
- **Conteúdo:** três perguntas abertas, uma sobre tendência, outra sobre resíduo e outra sobre MSE; nota não avaliativa sobre previsão aproximada, ponto atípico e a diferença entre ajuste aos dados e explicação física.
- **Interação:** registrar síntese; revisar respostas, tabela e descrição textual do gráfico; reiniciar se desejar.
- **Resposta esperada:** explicação qualitativa, com ao menos uma evidência do experimento em cada ideia central.
- **Feedback:** devolutiva por critérios: menciona presença de tendência, diferença observado-previsto e comparação do conjunto; sugere rever a etapa correspondente quando faltar uma conexão.
- **Componentes:** campos de síntese, lista de retomada, links internos para etapas, botão Reiniciar.
- **Estados:** normal: perguntas e retomadas ativas; vazio: campos continuam disponíveis com modelo de frase; carregando: estado reservado apenas para atualização de conteúdo, sem pressupor salvamento; erro: respostas da sessão não são descartadas e há instrução para copiar o texto antes de tentar novamente.
- **Acessibilidade:** linguagem clara, campos rotulados, mensagens não baseadas em cor, foco no feedback, layout de uma coluna em telas estreitas.

## Regra transversal de estados e respostas

Os dados sintéticos são locais ao módulo e, quando houver falha recuperável de visualização ou atualização, previsões, justificativas e sínteses já digitadas na sessão devem permanecer visíveis. Isso é um requisito de experiência, não uma decisão sobre armazenamento, autenticação ou tecnologia.
