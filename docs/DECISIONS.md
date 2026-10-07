# Registro de decisões

Este documento registra decisões confirmadas e evita que sugestões sejam tratadas como definições do projeto.

## Decisões confirmadas

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
