# Entrevista de concepção do projeto de qualificação

**Pesquisador:** Luiz Gabriel  
**Programa:** PROFCOMP/UFPA  
**Tema de partida:** plataforma interativa para o ensino de *machine learning* a estudantes do Ensino Médio  
**Início da entrevista:** 9 de outubro de 2026  
**Status:** em construção, sem decisões confirmadas

## Finalidade deste registro

Este arquivo guarda as ideias do pesquisador antes de transformá-las em problema de pesquisa, objetivos, referencial teórico ou metodologia. As respostas são registros de intenção e hipótese, não decisões acadêmicas aprovadas. Decisões confirmadas deverão ser registradas separadamente em `docs/DECISIONS.md`.

## Rodada 1 — origem e direção do tema

### Pergunta 1 — motivação

O que fez você querer pesquisar o ensino de *machine learning* no Ensino Médio? Há alguma situação de sala de aula, dificuldade que você observou ou inquietação profissional que esteja na origem dessa ideia?

**Resposta de Luiz:**

O interesse nasce da possibilidade de inserir o ensino de *machine learning* no Ensino Médio como uma via para ensinar computação. A Base Nacional Comum Curricular (BNCC) Computação é percebida como uma referência nacional importante, e a proposta se relaciona ao propósito do PROFCOMP de difundir o ensino de computação, incluindo pensamento computacional e outros fundamentos da área.

O foco inicial é investigar se é possível ensinar fundamentos básicos de *machine learning* de forma didática a estudantes do Ensino Médio, apoiando-se em uma plataforma interativa. A motivação também está ligada ao crescimento da inteligência artificial na cultura digital contemporânea, pois os estudantes precisam compreender, para além do uso de ferramentas, o que é inteligência artificial, como ela é criada e como ocorre o treinamento de sistemas baseados em dados.

### Pergunta 2 — transformação desejada

Quando o estudante terminar de usar a plataforma, o que você gostaria que ele conseguisse compreender, explicar ou fazer que hoje tende a ser difícil?

**Resposta de Luiz:**

Espera-se que os estudantes compreendam conceitos básicos associados a cinco problemas ou modelos de *machine learning* trabalhados na plataforma, consigam diferenciá-los e reproduzir experimentos elementares. A intenção também é que tenham um primeiro contato compreensível com a matemática envolvida, sem perder de vista a explicação conceitual de cada modelo.

O protótipo atual explora regressão linear, regressão logística, k-vizinhos mais próximos, árvore de decisão e k-means. Esta lista é um ponto de partida para a entrevista e não representa, ainda, a seleção final do produto educacional.

### Pergunta 3 — recorte de público e contexto

Em que contexto você imagina a aplicação: qual série ou faixa do Ensino Médio, qual componente curricular, e em escola pública, privada ou ambos? Se ainda não houver definição, registre a hipótese atual.

**Resposta de Luiz:**

O público previsto é composto por estudantes do Ensino Médio de escolas públicas. A série ou turma ainda não foi definida, portanto o recorte permanece aberto dentro desse nível de ensino até que a viabilidade de aplicação seja confirmada.

### Pergunta 4 — diferencial pedagógico

Entre visualização, experimentação com parâmetros, explicação matemática gradual, programação, situações do cotidiano e outros elementos, quais parecem indispensáveis para o produto e por quê?

**Resposta de Luiz:**

Embora os elementos inegociáveis ainda estejam sendo elaborados, há uma direção pedagógica nítida: trabalhar dados, interpretação de gráficos e critérios ou fundamentos próprios da computação, articulando esses conhecimentos ao funcionamento inicial de modelos de *machine learning*.

A plataforma não deve se limitar à apresentação de resultados. A expectativa é favorecer processos cognitivos que levem o estudante a compreender noções básicas e, em seguida, refletir sobre como uma inteligência artificial é construída e treinada a partir de dados.

## Rodada 2 — desafios, mediação e conhecimentos prévios

### Pergunta 5 — dificuldades previstas

Hoje, qual é a maior dificuldade que você imagina que um estudante do Ensino Médio enfrenta ao tentar entender inteligência artificial e *machine learning*?

**Resposta de Luiz:**

Há dificuldades que podem começar pelo próprio manuseio do computador, pois alguns estudantes apresentam pouca familiaridade com esse uso. Contudo, o gargalo principal previsto é matemático e interpretativo. Para compreender processos de *machine learning*, os estudantes precisam mobilizar ideias como plano cartesiano, leitura de gráficos, coordenadas, análise de dados e tabelas.

Como professor de Matemática, o pesquisador entende que pode tornar esses conteúdos mais claros, mas reconhece que eles exigem atenção central na proposta didática.

### Pergunta 6 — uso de IA e formação crítica

O que você acha que costuma acontecer quando a IA é ensinada apenas pelo uso de ferramentas prontas, sem explicar dados, treinamento e modelos?

**Resposta de Luiz:**

Na percepção inicial do pesquisador, parte dos adolescentes utiliza ferramentas de inteligência artificial sobretudo para obter respostas rápidas, copiar trabalhos ou evitar o próprio processo de pensamento. Essa é uma hipótese a ser investigada ou tratada criticamente, não uma afirmação sobre todos os estudantes.

A proposta pretendida desloca o uso da IA para uma relação de apoio à aprendizagem. Ao compreender como formular problemas, decompô-los e dialogar com sistemas de inteligência artificial, o estudante poderá desenvolver pensamento computacional e participar de modo mais consciente da cultura digital.

### Pergunta 7 — forma de uso da plataforma

Você imagina que a plataforma seja usada pelo estudante sozinho, em aula mediada pelo professor, ou nas duas situações?

**Resposta de Luiz:**

A ideia principal é que a plataforma componha uma sequência didática guiada e mediada pelo professor. Essa sequência deve avançar gradualmente pelos fundamentos matemáticos, pelos dados e pelos conceitos elementares de *machine learning*, conduzindo a construção do conhecimento até o uso dos recursos interativos.

O uso autônomo não está excluído, mas não é o centro da proposta nesta fase.

### Pergunta 8 — matemática a mobilizar

Quando fala em entender ‘um pouco da matemática’, que tipo de matemática você imagina ser viável: leitura de gráficos, média e distância, funções, probabilidade, ou outro caminho?

**Resposta de Luiz:**

O percurso matemático poderá mobilizar leitura e interpretação de gráficos, média, estatística, funções e probabilidade. A seleção, a profundidade e a ordem desses conceitos ainda deverão ser definidas conforme os modelos escolhidos, a série participante e a sequência didática.

## Rodada 3 — campo de aplicação, produto e pesquisa

### Campo possível e sua condição de viabilidade

**Registro de Luiz:**

O pesquisador atua em uma escola pública de tempo integral e atualmente ministra a disciplina PPA, ‘Projeto Permanente por Afinidade’, espaço de eixos eletivos no qual já trabalha conteúdos de computação. Por isso, uma turma de PPA, possivelmente do 1º ano do Ensino Médio, é um campo viável para a intervenção.

Entretanto, o campo não está garantido para o próximo ano letivo. A lotação docente é redefinida anualmente, a continuidade da turma de PPA não é certa e o período letivo atual termina em dezembro de 2026, o que pode inviabilizar a realização de oito aulas ainda neste ano. Caso o PPA não esteja disponível, a aplicação poderá ocorrer em outra turma de Ensino Médio sob docência do pesquisador, inclusive em aulas de Matemática, desde que o tempo e as condições de aplicação sejam definidos.

**Implicação para o projeto:**

O texto da qualificação deve apresentar PPA e 1º ano como cenário preferencial ou previsto, e não como requisito inalterável. A formulação final deverá informar que turma, componente curricular, escola e calendário serão confirmados antes da produção de dados.

### Uso e papel do produto educacional

**Registro de Luiz:**

A plataforma será usada inicialmente pelo próprio pesquisador em sua mediação docente durante a pesquisa. Não se planeja uma etapa separada de validação técnica do site por terceiros antes da intervenção. A prioridade atual é concluir a concepção da dissertação e do produto educacional, deixando os ajustes finos do site para depois dessa definição.

**Cuidado metodológico a preservar:**

O uso mediado pelo pesquisador não dispensa o registro de como o produto funcionou em sala, pois os registros de atividades, dificuldades e observações podem ajudar a interpretar a intervenção. Isso não equivale a alegar validação independente da plataforma ou prova de aprendizagem decorrente somente do site.

### Hipótese metodológica inicial

**Síntese para discussão com o orientador:**

O enquadramento mais aderente, nesta fase, é uma pesquisa aplicada, de abordagem predominantemente qualitativa, desenvolvida por meio de uma intervenção pedagógica com apoio de dados quantitativos descritivos. A investigação deve focalizar as explicações, previsões e produções dos estudantes ao longo da sequência didática.

‘Estudo de caso’ poderá ser usado como estratégia complementar se a análise se concentrar em uma turma e em seu contexto delimitado. ‘Pesquisa baseada em design’ somente deverá ser adotada se o estudo incluir ciclos planejados de concepção, aplicação, análise e redesenho do produto; uma aplicação única não basta para justificar esse enquadramento.

## Rodada 4 — compreensão a observar

### Núcleo da aprendizagem pretendida

**Registro de Luiz:**

Os cinco modelos presentes no site constituem o conteúdo a ser ensinado. Entretanto, o objetivo central não é que os estudantes apenas memorizem seus nomes ou definições. Espera-se que distingam dados e características e compreendam a ideia elementar de cada modelo, mas, principalmente, que consigam pensar sobre as consequências de alterar um parâmetro ou elemento dos dados.

O estudante deve formular uma hipótese sobre o que ocorrerá, mudar um controle, observar a transformação do gráfico ou da decisão do modelo e refletir sobre o resultado. Essa reflexão deve articular o conceito do modelo, a representação gráfica e a matemática mobilizada na atividade. A intenção é aproximar essa ação de dimensões do pensamento computacional, em especial a análise de relações entre entradas, regras e resultados.

### Formulação provisória de evidência de compreensão

Uma evidência central será a capacidade de o estudante antecipar uma consequência de uma alteração simples, confrontar sua hipótese com o experimento e explicar o que aconteceu usando, no nível esperado para a turma, elementos do conceito, do gráfico e da matemática do modelo.

## Rodada 5 — profundidade e distribuição dos modelos

### Limites percebidos pelo pesquisador

**Registro de Luiz:**

O tempo disponível é restrito, possivelmente oito aulas, e os estudantes podem apresentar fragilidades na base matemática. Uma apresentação única de um conteúdo novo não garante que ele se mantenha disponível para uso ou explicação na aula seguinte. A sequência precisa prever retomadas e não pode interromper o currículo regular por um período desproporcional.

### Decisão de trabalho atual

**Registro de Luiz:**

Os cinco modelos do produto, regressão linear, regressão logística, k-vizinhos mais próximos, árvore de decisão e k-means, serão tratados como conteúdos centrais da sequência didática. Não se pretende apresentá-los como um conjunto no qual somente dois são efetivamente ensinados e os demais aparecem apenas como exemplos.

O desafio a resolver posteriormente é a sequencialidade didática dentro do tempo disponível. A proposta deverá organizar introduções, comparações e retomadas para que os estudantes consigam diferenciar os cinco modelos e suas formas de trabalhar com dados. Igual importância pedagógica não exige a mesma formalização matemática para todos, mas exige que cada modelo tenha uma experiência guiada, uma oportunidade de previsão, experimentação e explicação, e um lugar claro na síntese comparativa final.

## Rodada 6 — entrada na sequência didática

### Decisão de trabalho atual

**Registro de Luiz:**

A sequência deverá combinar duas portas de entrada. Primeiro, situações de inteligência artificial presentes no cotidiano dos estudantes podem motivar a pergunta sobre como uma máquina produz recomendações, classificações ou previsões. Em seguida, a discussão deve chegar rapidamente a um problema concreto que possa ser investigado com dados na plataforma.

Essa escolha procura evitar tanto uma abertura apenas abstrata sobre tecnologia quanto uma introdução matemática desconectada de uma questão significativa para os estudantes. Dados, gráficos e conceitos matemáticos serão introduzidos quando ajudarem a compreender o problema proposto.

### Cenários didáticos — critérios e hipóteses iniciais

**Registro de Luiz:**

Os exemplos ainda não devem ser apresentados como validados para a turma. A orientação é construir propostas didáticas iniciais e, posteriormente, verificar na prática se são compreensíveis, relevantes e adequadas ao tempo de aula.

**Critérios de seleção:**

- usar dados sintéticos e evitar comparações, desempenho ou informações reais dos estudantes;
- permitir que a mudança de dado ou parâmetro tenha efeito visível no gráfico ou na decisão;
- exigir pouca contextualização externa para que o foco permaneça no modelo;
- fazer sentido para estudantes do Ensino Médio de escola pública sem pressupor acesso individual a tecnologias ou experiências específicas;
- possibilitar explicação matemática gradual.

**Hipóteses iniciais a revisar:**

- regressão linear: temperatura e consumo fictício de energia em uma sala, para prever um valor e discutir tendência, erro e ponto atípico;
- regressão logística: leitura fictícia de sensor para estimar a chance de um alerta, distinguindo probabilidade e limiar de decisão;
- k-NN: classificação de objetos ou situações fictícias por duas características mensuráveis, para discutir proximidade, distância e votação;
- árvore de decisão: decisão sobre irrigação de uma horta escolar simulada, usando regras relacionadas à umidade e à temperatura;
- k-means: agrupamento de pontos de coleta fictícios em um mapa de bairro, para discutir proximidade, centróides e ausência de rótulos.

Essas hipóteses não substituem a futura validação didática durante a preparação e a aplicação da sequência.

## Rodada 7 — organização dos estudantes

### Hipótese inicial

**Registro de Luiz:**

A experimentação na plataforma será planejada, a princípio, para duplas. Essa organização favorece conversa durante a manipulação dos controles e responde melhor à disponibilidade variável de computadores em escola pública.

Para que a pesquisa não perca as compreensões de cada participante, a previsão inicial e a explicação final poderão ser registradas individualmente, ainda que a exploração dos dados e parâmetros ocorra em dupla. A adequação dessa combinação deverá ser revista conforme o campo, a infraestrutura e a dinâmica da turma.

## Rodada 8 — evidências e dimensão da coleta

### Decisão de trabalho atual

**Registro de Luiz:**

A intervenção não utilizará cartilha extensa acompanhando cada aula. Para reduzir a carga de aplicação e análise, a coleta inicial será composta por três fontes:

- diagnóstico individual curto, aplicado antes da sequência;
- desafio final individual, aplicado ao fim da sequência, incluindo algumas questões equivalentes ou comparáveis às do diagnóstico;
- registro docente breve por aula, em tópicos, sobre dificuldades recorrentes, condições de uso e intervenções relevantes.

As perguntas inseridas no site terão função de devolutiva pedagógica imediata e não constituirão, nesta configuração, fonte principal de dados, pois as respostas não são persistidas.

### Tratamento e apresentação das produções

**Registro de Luiz:**

As respostas de todos os participantes poderão compor o corpus anonimizado de análise, mas não serão reproduzidas integralmente na dissertação. O texto final deverá apresentar sínteses por critérios de compreensão, frequências descritivas quando úteis e poucos excertos ilustrativos identificados por códigos, como ‘E07’. Os instrumentos-modelo poderão integrar os apêndices; os registros reais permanecerão protegidos e separados do repositório público.

## Rodada 9 — direção da pergunta de pesquisa

### Posição do pesquisador

**Registro de Luiz:**

O projeto se vincula à importância atribuída ao ensino de Computação, ao pensamento computacional e à integração da Computação à Educação Básica. A intenção é usar *machine learning* como conteúdo de Computação que permita relacionar dados, gráficos, matemática e decisões de sistemas de inteligência artificial, observando se os estudantes conseguem demonstrar compreensão nesse percurso.

### Delimitação recomendada para discussão

O trabalho não deve prometer demonstrar que o pensamento computacional melhora, de modo geral, a aprendizagem em Matemática, Língua Portuguesa ou outras disciplinas, pois isso exigiria outro desenho de pesquisa e instrumentos específicos. O pensamento computacional poderá aparecer como referência curricular e como dimensão mobilizada pelas atividades, especialmente na análise de relações entre dados, regras, parâmetros e resultados.

A pergunta de pesquisa deverá focalizar as evidências de compreensão conceitual, matemática e representacional de fundamentos de *machine learning* produzidas durante a intervenção, sem atribuir causalidade ampla ou generalização para todos os contextos escolares.

## Próximas rodadas previstas

- Delimitação do problema e da pergunta de pesquisa;
- conteúdo de *machine learning*, matemática e conhecimentos prévios;
- desenho da plataforma e experiências de aprendizagem;
- metodologia, participantes, instrumentos e cuidados éticos;
- viabilidade, cronograma e diálogo com o orientador.
