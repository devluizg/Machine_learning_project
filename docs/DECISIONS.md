# Registro de decisões

Este documento registra decisões confirmadas e evita que sugestões sejam tratadas como definições do projeto.

## Decisões confirmadas

### 2026-10-23 — Nome do produto educacional

- A identificação visual do site passa a ser `Machine Learning Project`.
- O nome anterior, `plural.`, deixa de ser usado na interface, no título da página e nos metadados do projeto.

### 2026-10-23 — Identidade visual do produto educacional

- O site usa três famílias cromáticas: azul-marinho (`#081d3d`), laranja (`#ff6b3d`) e azul-claro (`#82c8ee`).
- Branco e tons neutros permanecem em fundos, textos e bordas para garantir leitura.
- Gráficos, destaques, estados e ilustrações seguem a mesma paleta.
- Botões e links com aparência de botão usam formato arredondado em todas as páginas.

### 2026-10-23 — Percurso das oito aulas e versão de aplicação do site

- A plataforma passa a identificar o lugar de cada módulo na sequência de oito encontros e a oferecer uma página de percurso para estudantes.
- O modo guiado recebe o nome `modo aula` e permanece como entrada obrigatória recomendada; controles avançados, métricas de treino e vistas 3D são apresentados como aprofundamento opcional.
- A área docente reúne o roteiro de cinquenta minutos, uma conferência de infraestrutura e os PDFs públicos das aulas 2 a 7.
- O diagnóstico inicial e o instrumento final permanecem fora dos arquivos públicos do site para preservar os procedimentos da pesquisa.
- Uma página de ajuda reúne orientação de teclado, reinício, alternativas textuais, redução de movimento, glossário e funcionamento local.
- A versão de aplicação passa a ser identificada como `0.2.0-campo`. Ainda são necessários testes com estudantes, leitor de tela, projeção e equipamentos reais antes de considerar o produto validado.

### 2026-10-03 — Novo foco do projeto

- O projeto será uma plataforma para ensino de *machine learning*.
- O público prioritário será formado por estudantes do Ensino Médio iniciantes em *machine learning*.
- A experiência deverá ser visual, interativa e voltada à compreensão da matemática dos modelos.
- A plataforma incluirá somente alguns modelos selecionados, não todos os tipos de modelos.
- O trabalho será utilizado no projeto de pré-defesa do mestrado profissional ProfComp de Luiz Gabriel.
- O orientador atual é o professor Marcos Braga.
- A plataforma NEURON será uma referência inicial de inspiração.
- O produto educacional terá a forma de um site interativo.
- O trabalho acadêmico e o desenvolvimento do site serão organizados no mesmo projeto, em áreas separadas e articuladas.

### 2026-10-03 — Orquestração econômica de inteligência artificial

- Um modelo avançado atuará como supervisor, responsável por planejamento, decisões complexas, síntese e validação.
- Um modelo mais econômico executará pesquisas focadas, operações mecânicas, testes e pequenas implementações bem especificadas.
- Tarefas determinísticas de um único passo poderão ser executadas diretamente pelo supervisor quando abrir outro agente custar mais tokens.
- O sistema utilizará pacotes mínimos de contexto e respostas estruturadas.
- Trabalho além do pedido somente será executado quando necessário para evitar erro, resolver bloqueio ou atender exigência relevante de segurança, ética ou conformidade acadêmica.

### 2026-10-03 — Arquitetura da fatia vertical de regressão linear

- Para a primeira fatia vertical navegável do módulo-piloto, foi escolhida a pilha Vite + React + TypeScript, com SVG nativo.
- A decisão atende ao estado local das seis etapas, à separação entre cálculos e interface, à acessibilidade e aos testes, sem exigir servidor.
- HTML/CSS/JavaScript puro e Vite + Svelte + TypeScript foram considerados; React foi selecionado pelo equilíbrio entre componentes, tipagem, testes e continuidade do projeto.
- Não serão criados backend, banco, autenticação, API, serviços externos ou coleta de respostas nesta fatia.
- A reta ajustada será uma referência matemática independente dos controles manuais; seus coeficientes reais devem ser exibidos mesmo fora do intervalo dos sliders.
- Esta decisão se limita ao módulo-piloto e poderá ser revista se validação humana, requisitos institucionais ou acessibilidade impuserem mudança.

### 2026-10-03 — Recorte da versão simplificada de cinco modelos

- A pedido de Luiz, a **versão de protótipo** do site passa a oferecer regressão linear, regressão logística, k-NN, árvore de decisão e k-means.
- O objetivo é comparar três ideias — regressão, classificação e agrupamento — com um experimento guiado e poucos controles por modelo, em português brasileiro.
- A implementação reutiliza Vite + React + TypeScript e SVG nativo já adotados no piloto; não adiciona backend, banco, autenticação, API externa, coleta de respostas ou deploy.
- Esta é uma decisão de **escopo de protótipo**, não aprovação da lista final de modelos, da identidade visual definitiva nem da metodologia da pesquisa. Esses itens ainda dependem de validação com o orientador.
- O nome visual provisório “plural.” serve apenas ao protótipo; não constitui definição da marca do produto.
- A metodologia `replica-skill` é adaptada como análise de padrões públicos e verificação dos objetivos próprios. Não serão buscadas paridade visual, cópia de conteúdo ou arquitetura SaaS da referência.

### 2026-10-03 — Ampliação funcional solicitada para o protótipo

- Luiz solicitou maior profundidade funcional nos cinco laboratórios e confirmou a inclusão de vistas 3D e controles de treinamento.
- A ampliação mantém o recorte autoral e local: vistas 3D são projeções SVG rotacionáveis de grandezas matemáticas calculadas, não cópia das cenas do NEURON nem afirmação de que os dados tenham três atributos.
- Regressões linear e logística recebem passos de otimização; árvore aprende divisões dos dados; k-means mostra iteração e WSS. k-NN não recebe treino fictício, pois decide a partir dos exemplos armazenados.
- A inclusão desses recursos no protótipo não aprova sua permanência no produto final nem substitui validação pedagógica e de acessibilidade.

### 2026-10-03 — Movimento ambiental autoral no protótipo

- A pedido de Luiz, a abertura e os cabeçalhos dos módulos recebem um campo decorativo de pontos com profundidade, conexões leves e reação ao cursor.
- O efeito usa Canvas nativo apenas como camada visual; os gráficos didáticos e suas alternativas textuais continuam em SVG/HTML. Não há biblioteca 3D, serviço externo nem coleta de posição do cursor.
- Há controle visível de pausa. A animação fica estática com preferência por movimento reduzido ou ponteiro de toque e para quando sai da tela ou a aba fica oculta.
- A composição, as cores e o movimento são autorais; não reproduzem partículas, código, ilustrações ou identidade visual da referência.

### 2026-10-03 — Camada guiada para estudantes iniciantes no protótipo

- A pedido de Luiz, o protótipo dos cinco modelos recebe uma entrada conceitual e aulas guiadas como modo inicial; a exploração livre e as vistas 3D permanecem disponíveis.
- Cada aula relaciona situação fictícia, uma ação prioritária, consequência visível, exemplo numérico e checagem com retorno imediato.
- Logística e árvore usam pequenos casos sintéticos reservados, distintos dos dados de ajuste, apenas para ilustrar a diferença entre treino e teste.
- As respostas permanecem locais e não são coletadas. A implementação não valida aprendizagem nem define método de pesquisa; a efetividade didática e a acessibilidade exigem avaliação posterior com orientação acadêmica.

### 2026-10-04 — Ambiente visual de céu noturno no protótipo

- A pedido de Luiz, a abertura passa a usar um azul-marinho profundo, em vez do tom azul-esverdeado anterior, como base para o campo autoral de pontos e conexões.
- Os cinco módulos reutilizam esse mesmo ambiente de céu noturno durante a leitura e os experimentos; gráficos, controles e atividades permanecem em cartões claros para conservar contraste, foco pedagógico e legibilidade.
- O movimento segue estritamente decorativo: mantém o botão de pausa, respeita preferência por redução de movimento, permanece estático em ponteiro de toque e não interfere nos cálculos ou nos gráficos didáticos.
- A composição continua autoral e provisória, sem reproduzir identidade ou ativos da referência externa.

### 2026-10-04 — Ritmo e direção do campo de constelações

- O campo de pontos passa a permanecer em deriva lenta contínua, mesmo sem presença do cursor, para reforçar a ideia de céu noturno vivo sem disputar atenção com o conteúdo.
- Ao mover o cursor próximo aos pontos, a perturbação ganha intensidade temporária e acompanha a direção do deslocamento do mouse; o efeito perde força suavemente ao parar ou afastar o cursor.
- A resposta permanece limitada a uma área próxima ao cursor; velocidade e deslocamento são amortecidos por quadro para evitar tremida. Pausa, preferência por movimento reduzido, toque e interrupção fora de tela continuam desativando a animação.

### 2026-10-09 — Enquadramento curricular e nível introdutório da proposta

- A pesquisa passa a declarar explicitamente o *machine learning* como conteúdo introdutório de Computação para estudantes do Ensino Médio, e não como uma versão reduzida de formação técnica ou universitária em inteligência artificial.
- O nível de aprofundamento priorizará dados, características, finalidade do modelo, regras, parâmetros, treinamento, previsão, classificação, agrupamento, erro e limites, articulados a matemática elementar retomada no contexto das atividades.
- A plataforma interativa será compreendida como recurso de informática na educação e de mediação docente. O objeto de ensino e investigação será a compreensão de conceitos e práticas de Computação, não o simples uso do site ou de ferramentas de IA.
- A articulação com a BNCC Computação ocorrerá pelos eixos Pensamento Computacional, Mundo Digital e Cultura Digital. A matriz preliminar em `03_pesquisa/MATRIZ_BNCC_OBJETIVOS_ATIVIDADES_E_EVIDENCIAS.md` relaciona objetivos de aprendizagem, atividades, evidências esperadas e as habilidades EM13CO10, EM13CO11 e EM13CO12; sua seleção final permanece condicionada ao currículo da rede, à série e à validação do orientador.
- A seleção dos cinco modelos no protótipo permanece sujeita à validação do orientador; esta decisão não a converte em lista final aprovada.
- Foi elaborado um diagnóstico inicial individual, armazenado em `03_pesquisa/instrumentos/diagnostico_inicial_v01/`. O instrumento final e sua matriz de comparabilidade serão consolidados somente após revisão do orientador, adequação ao campo e confirmação das exigências éticas e institucionais.
- A sequência preliminar de oito encontros foi detalhada em `03_pesquisa/metodologia/SEQUENCIA_DIDATICA_PRELIMINAR_OITO_ENCONTROS.md`. Ela preserva os cinco módulos do protótipo como conteúdos introdutórios e mantém previsões no site como atividade formativa, enquanto diagnóstico, desafio final e registros docentes constituem as fontes de análise planejadas.
- A auditoria pedagógica do site identificou aderência funcional aos cinco encontros de modelo e uma lacuna de coerência entre os cenários atualmente implementados e os cenários propostos na sequência. Nenhum cenário foi alterado nesta etapa; a escolha e a padronização dos cinco contextos sintéticos devem preceder mudanças de dados, eixos ou textos no código.
- A redação do projeto de qualificação adotará como meta aproximada entre 12 mil e 18 mil palavras de texto corrido, sem contar referências, anexos e elementos pré-textuais. Essa é uma meta de planejamento, não uma exigência institucional confirmada.
- A qualificação passou a incluir contribuições esperadas, limites reconhecidos e cronograma por etapas. As datas não foram preenchidas, pois dependem da confirmação do campo, do calendário escolar e das exigências institucionais e éticas.

### 2026-10-18 — Delimitação da avaliação da intervenção

- A pergunta de pesquisa passa a focalizar mudanças, permanências e dificuldades nas explicações dos estudantes ao longo da sequência.
- A intervenção mantém oito encontros e cinco modelos, avaliados principalmente por conceitos transversais: dados e finalidade, alteração e consequência, representação e conceito, possibilidades e limites.
- O diagnóstico e o primeiro bloco do instrumento final terão questões comparáveis em operação cognitiva, extensão e dificuldade.
- O instrumento final terá um segundo bloco de transferência, analisado separadamente do núcleo comparável.
- Os encontros 2, 4 e 6 terão registros individuais breves antes e depois da exploração, cobrindo previsão numérica, classificação e agrupamento.
- A análise utilizará rubrica de três níveis, justificativas qualitativas, frequências com denominadores e tabelas de transição por dimensão.
- Um questionário breve de percepção poderá avaliar clareza, dificuldade e uso da plataforma, sem ser tratado como evidência de aprendizagem.
- O desenho não atribuirá à plataforma um efeito causal isolado, pois a intervenção também inclui mediação docente, atividades e interação entre estudantes.

### 2026-10-18 — Apoio à comparação e à condução da sequência

- O protótipo passa a incluir uma síntese comparativa para o encontro 7, organizada por finalidade, dados de entrada, saída, mecanismo, controle principal e limite dos cinco modelos.
- O protótipo passa a incluir um roteiro docente imprimível para os oito encontros, com distribuição de cinquenta minutos e acesso ao recurso correspondente.
- Os cenários usados na condução dos encontros 2, 4, 5 e 6 serão os mesmos apresentados no site. Contextos diferentes permanecem nos instrumentos quando sua função for examinar comparabilidade ou transferência.
- O termo em português será padronizado como “k-vizinhos mais próximos”, acompanhado de “k-NN” quando conveniente.
- Previsões e explicações digitadas no site continuam formativas, locais e sem armazenamento. Diagnóstico, registros intermediários e instrumento final permanecem externos ao site.
- Métricas e visualizações 3D permanecem como aprofundamento opcional; não integram o percurso obrigatório da aula guiada.

### 2026-10-23 — Organização das versões e referência metodológica de trabalho

- A versão 5 do projeto de qualificação, em `01_qualificacao/texto/projeto_qualificacao_v5_20261018/`, passa a ser a referência principal de edição.
- As versões anteriores foram preservadas em `99_arquivo/versoes_antigas/qualificacao/`, sem exclusão de arquivos ou histórico.
- A proposta resumida de aplicação passa a ser o documento principal para a reunião de orientação. Ela apresenta um planejamento para apreciação, não uma metodologia já aprovada.
- Os documentos de metodologia mantidos como complementares são o guia metodológico detalhado, a sequência preliminar de oito encontros, o diagnóstico individual atual e o checklist de execução.
- O arquivo antigo que reunia diagnóstico e desafio final foi arquivado por conter um desenho de instrumentos diferente do atual. O instrumento final permanece pendente de validação do orientador.

### 2026-10-23 — Transição para céu noturno integral e aceleração por WebGL

- A pedido de Luiz, o background do site passa a envolver 100% da plataforma em um tom contínuo de azul-marinho de céu noturno (deep navy), unificando a página inicial, os módulos e as páginas de apoio sob a mesma atmosfera cósmica.
- O campo decorativo de constelação foi reimplementado com WebGL nativo de alta performance (shaders GLSL na GPU), eliminando os gargalos de CPU do Canvas 2D e alcançando fluidez a 60–120 FPS com 3.800 partículas tridimensionais, órbitas elípticas e atenuação de perspectiva.
- O efeito reproduz com elegância matemática a física suave do mouse (repulsão e rotação giroscópica) e a dispersão expansiva pelo scroll da página.
- Nenhuma dependência externa adicional foi introduzida no `package.json`, garantindo código 100% autoral, leve e sustentável.
### 2026-10-23 — Modernização dos botões, ícones vetoriais e card interativo na abertura

- A pedido de Luiz, os botões quadrados rígidos foram substituídos por botões de formato pílula (*pill-shaped* com `border-radius: 9999px`), gradientes suaves vibrantes em laranja/coral, sombras luminosas discretas (*ambient glow*) e micro-interações fluidas no hover.
- A figura estática e inclinada da abertura (`FIG. 01`) foi substituída por um componente de demonstração animada em loop contínuo ([`HeroDemo.tsx`](file:///home/luiz/Machine_learning_project/04_produto_educacional/site/src/components/HeroDemo.tsx)), simulando um vídeo vetorial em HTML/SVG. Na animação, um cursor de mouse se aproxima suavemente do controle deslizante, clica e ajusta o parâmetro de inclinação da regressão linear em tempo real, ilustrando a rotação da reta, a variação dos resíduos e a minimização do erro quadrático (MSE), reiniciando o ciclo suavemente. A qualquer momento, a intervenção manual do estudante oculta o cursor e transfere o controle interativo direto para ele.
- Os caracteres textuais estáticos dos cinco modelos foram substituídos por ícones vetoriais SVG desenhados sob medida ([`ModelIcons.tsx`](file:///home/luiz/Machine_learning_project/04_produto_educacional/site/src/components/ModelIcons.tsx)), expressando visualmente o mecanismo de cada algoritmo (reta e dispersão, sigmoide, raio de vizinhança k-NN, árvore ramificada e centróides k-means).
- Os cards de modelos e seções ganharam cantos arredondados modernos (16px a 24px) com efeito aero-glass translúcido e setas direcionais SVG dinâmicas.

### 2026-10-23 — Refinamento visual da simulação HeroDemo (eliminação de sobreposição e unificação do slider)

- A sobreposição de texto relatada por Luiz — onde a rotação e inclinação da reta de regressão linear passava por cima dos rótulos de inclinação e erro quadrático (`ERRO QUADRÁTICO` / `✓ AJUSTE ÓTIMO`) — foi resolvida estruturalmente:
  1. As métricas foram extraídas da área interna do gráfico SVG e alocadas em uma barra dedicada de placar (`.demo-metrics-strip`) com chips visuais estilizados logo acima do gráfico. Com isso, a reta pode se mover em qualquer ângulo com total desobstrução, sem colidir com nenhum texto.
  2. Foi adicionada uma máscara de corte vetorial (`<clipPath id="plotAreaClip">`) que restringe a reta rigorosamente à área útil dos eixos cartesianos, eliminando transbordamentos nas bordas.
  3. A segunda barra de slider HTML redundante que aparecia abaixo do gráfico foi removida da interface visual e convertida em controle acessível (`.sr-only`), unificando a interação na barra integrada do próprio SVG onde o cursor animado interage e onde o usuário pode clicar e arrastar diretamente via Pointer Events.

### 2026-10-23 — Realocação do controle de animação de fundo para a barra de navegação superior

- A pedido de Luiz, o botão "Pausar movimento de fundo" foi retirado do lado do botão principal "Explorar os modelos", deixando a chamada para ação principal desimpedida, limpa e com máximo destaque na Hero.
- O controle de animação de fundo foi promovido para o cabeçalho superior permanente (`site-header`), substituindo a pílula estática ("PROTÓTIPO EDUCACIONAL"). O novo botão em formato pílula exibe o status em tempo real com indicador luminoso suave (`header-motion-dot`) e permite pausar ou retomar o céu estrelado em qualquer página da plataforma.

### 2026-10-23 — Ajuste de tom acadêmico no subtítulo da Hero

- A redação informal "Mexa nos dados. Observe o gráfico. Entenda a matemática por trás de cinco modelos, um experimento de cada vez." foi atualizada para "Explore os dados. Observe o gráfico. Compreenda os fundamentos matemáticos de cinco modelos, um experimento por vez.". A alteração eleva o rigor e a precisão pedagógica condizentes com a dissertação de mestrado profissional (ProfComp), substituindo o coloquialismo pelo convite à exploração investigativa e conceitual.

### 2026-10-23 — Refinamento estilístico da página inicial: método em cartões arredondados, ícones animados e desembolamento do rodapé

- A seção "Observe, experimente e explique" (`.principle-strip`), que antes ficava solta em uma moldura retangular com bordas abertas, foi remodelada em três cartões arredondados (`border-radius: 22px`) com efeito aero-glass translúcido, identificadores numéricos pílula (`01`, `02`, `03`) e micro-interação no hover, integrando-se harmoniosamente à linguagem visual do projeto.
- Os ícones vetoriais dos cinco modelos ([`ModelIcons.tsx`](file:///home/luiz/Machine_learning_project/04_produto_educacional/site/src/components/ModelIcons.tsx)) ganharam animações contínuas, suaves e lentas (ciclos de 4s a 6s) aceleradas na GPU, simulando o funcionamento e a montagem de cada algoritmo em tempo real:
  - *Regressão linear:* a reta oscila suavemente o ângulo de inclinação enquanto os resíduos pontilhados fluem e os pontos de dados pulsam sutilmente;
  - *Regressão logística:* a curva sigmoide traça sua probabilidade continuamente enquanto o limiar pontilhado flui e as classes alternam certeza;
  - *k-NN:* o raio de vizinhança expande e contrai simulando a busca por vizinhos mais próximos com conexões ativas e pulso de radar no ponto de consulta;
  - *Árvore de decisão:* pulsos luminosos percorrem hierarquicamente os ramos do nó raiz às folhas, simulando a avaliação de caminhos de decisão;
  - *k-means:* centróides realizam translação orbital suave enquanto os halos pontilhados dos clusters giram lentamente.
- Os blocos inferiores de apoio ("Encontro 7" e "Sequência completa"), que estavam empilhados e colados ao grid dos modelos, foram reestruturados em uma grade de apoio de duas colunas (`.home-support-strip`) com espaçamento generoso (`margin-top: 54px`, linha divisória sutil), cartões arredondados com badges temáticas e botões pílula independentes, eliminando a sensação de embolamento.

## Sugestões em análise

- Organizar cada módulo em intuição, experimento, matemática, interpretação e atividade.
- Validar academicamente se os cinco modelos usados no protótipo devem compor o produto final.
- Avaliar a aprendizagem por meio de uma intervenção com estudantes.

Esses itens são possibilidades e não devem ser tratados como aprovados até validação com o orientador.

## Decisões pendentes

- Título provisório da dissertação e do produto.
- Problema e pergunta de pesquisa.
- Objetivos geral e específicos.
- Lista final de modelos.
- Conteúdos matemáticos e nível de profundidade.
- Instituição, disciplina e participantes da aplicação.
- Metodologia de pesquisa e instrumentos de coleta.
- Identidade visual e nome da plataforma.

## Como registrar novas decisões

Adicione uma seção com data, decisão, justificativa, alternativas consideradas e consequências para o escopo.
