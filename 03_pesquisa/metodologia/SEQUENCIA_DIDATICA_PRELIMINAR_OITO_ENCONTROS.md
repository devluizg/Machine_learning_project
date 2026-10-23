# Sequência didática preliminar de oito encontros

**Projeto:** Ensino introdutório de *machine learning* no Ensino Médio por meio de uma sequência didática apoiada por plataforma interativa  
**Público previsto:** estudantes de Ensino Médio de escola pública, iniciantes em *machine learning*  
**Duração inicial:** oito encontros de aproximadamente 50 minutos  
**Status:** planejamento de trabalho. Deve ser ajustado à turma, ao componente curricular, à infraestrutura e à validação do orientador.

## 1. Princípios de organização

A sequência ensina fundamentos de Computação por meio de cinco modelos introdutórios de *machine learning*. O site é recurso de mediação; não substitui a explicação, a problematização nem a síntese conduzida pelo professor.

Todos os encontros retomam o ciclo **prever → experimentar → observar → explicar**. A exploração será individual, com uso dos computadores do laboratório e, conforme a disponibilidade confirmada no campo, de Chromebooks. As respostas digitadas no site têm função formativa imediata e não constituem fonte principal dos dados da pesquisa.

A proposta não exige programação prévia. A Matemática entra quando ajuda a interpretar o modelo: coordenadas e tendência na regressão linear; porcentagem e limiar na regressão logística; distância no k-vizinhos mais próximos (k-NN); condições lógicas na árvore; média e proximidade no k-means. Não serão ensinadas demonstrações formais de cálculo, álgebra linear, otimização ou generalização estatística.

## 2. Preparação comum

Antes do primeiro encontro, o professor deverá:

- confirmar funcionamento local do site e abrir os cinco módulos em cada computador disponível;
- confirmar cerca de 20 computadores do laboratório e a disponibilidade de Chromebooks para completar o acesso individual;
- preparar opção de projeção coletiva para falhas técnicas;
- definir os códigos anônimos dos instrumentos individuais;
- conferir se cenários exibidos pelo site correspondem aos cenários usados na aula;
- manter acessíveis tabelas ou descrições textuais dos gráficos;
- organizar o diagnóstico atual em `03_pesquisa/instrumentos/diagnostico_inicial_v01/` e preparar o instrumento final somente após a validação do orientador.

Somente dados sintéticos serão usados. Nenhum exemplo utilizará notas, frequência, comportamento, endereço ou outra informação pessoal dos estudantes.

## 3. Visão geral

| Encontro | Questão orientadora | Modelo ou foco | Produto formativo |
| --- | --- | --- | --- |
| 1 | Como um sistema pode usar exemplos para produzir uma resposta? | Dados, características, modelos e tipos de tarefa | Diagnóstico individual e classificação oral de situações. |
| 2 | Como prever o alongamento de uma mola a partir da massa? | Regressão linear | Explicação sobre massa, inclinação, previsão do alongamento e erro. |
| 3 | Como uma chance pode virar uma decisão? | Regressão logística | Explicação da diferença entre probabilidade e limiar. |
| 4 | O que as amostras próximas dizem sobre uma nova amostra? | k-vizinhos mais próximos (k-NN) | Justificativa baseada em doçura, acidez, distância, vizinhos e votação. |
| 5 | Como perguntas sobre largura e altura levam a uma decisão? | Árvore de decisão | Explicação de caminho de decisão e regra aplicada a objetos. |
| 6 | Como agrupar amostras por doçura e acidez sem categorias prévias? | k-means | Explicação de centróides e agrupamento sem rótulos. |
| 7 | Que tipo de problema cada modelo ajuda a enfrentar? | Comparação dos cinco modelos | Escolha justificada de finalidade e modelo. |
| 8 | Como explicar uma decisão sem tratá-la como mágica? | Síntese | Instrumento final individual: núcleo comparável, desafio de transferência e questionário de percepção. |

## 4. Detalhamento dos encontros

### Encontro 1: Dados, modelos e tarefas

**Objetivos:** reconhecer que um sistema computacional pode usar dados para produzir previsão, classificação ou agrupamento; diferenciar dado, característica, resultado desejado e modelo; discutir possibilidade e limite de IA.

**Relação curricular:** EM13CO10 e EM13CO12.

| Tempo | Ação | Mediação |
| --- | --- | --- |
| 0–5 min | Apresentar o percurso e esclarecer que não há prova escolar. | Explicar que a pesquisa busca compreender explicações, não classificar estudantes. |
| 5–25 min | Aplicar o diagnóstico individual. | Esclarecer vocabulário sem indicar resposta e recolher pelo código. |
| 25–35 min | Discutir três situações: estimar consumo, escolher categoria e formar grupos próximos. | Perguntar “qual saída queremos?” e “quais dados podem ajudar?”. |
| 35–45 min | Abrir a introdução do site para exploração individual. | Retomar dados, modelo, treino ou consulta, previsão, classificação e agrupamento. Os instrumentos usam contextos diferentes dos exemplos das aulas para observar transferência. |
| 45–50 min | Síntese oral. | Cada estudante nomeia o tipo de tarefa de uma situação. |

**Ponto de atenção:** não permanecer em debate genérico sobre IA. Chegar aos dados e à finalidade de cada situação.

### Encontro 2: Regressão linear: massa, alongamento da mola, previsão e erro

**Objetivos:** reconhecer previsão de valor numérico; interpretar tendência em gráfico de dispersão; relacionar inclinação ou mudança nos dados à alteração de previsão e erro.

**Relação curricular:** EM13CO11 e EM13CO12.

| Tempo | Ação | Mediação |
| --- | --- | --- |
| 0–7 min | Retomar dado, saída e previsão numérica. | Perguntar se prever valor é o mesmo que escolher categoria. |
| 7–12 min | Apresentar a relação entre massa aplicada e alongamento de uma mola; identificar eixos, pontos e valor a estimar. | Ligar cada eixo à massa e ao alongamento antes de mostrar fórmula. |
| 12–18 min | Cada estudante antecipa o efeito de alterar a inclinação. | Solicitar previsão específica: aumenta, diminui ou não muda? |
| 18–33 min | Explorar aula guiada: inclinação, reta, previsão, resíduo e MSE; se houver tempo, um passo de treino. | Comparar valor observado, previsto e diferença entre eles. |
| 33–43 min | Confrontar previsões com o gráfico. | Explicar resíduo como diferença, sem exigir cálculo geral. |
| 43–50 min | Síntese. | Retomar como a inclinação ou um dado atípico altera a reta e a previsão do alongamento. |

**Questão formativa:** “Se a inclinação aumentar, o que tende a ocorrer com a previsão de um ponto à direita do gráfico? Explique com o desenho.”

**Ponto de atenção:** o cenário usado em aula deve coincidir com os dados efetivamente visíveis no módulo antes da aplicação.

### Encontro 3: Regressão logística: chance, limiar e classificação

**Objetivos:** distinguir probabilidade de classe final; identificar limiar como regra de decisão; reconhecer que o limiar pode mudar a classificação sem mudar a chance calculada.

**Relação curricular:** EM13CO10, EM13CO11 e EM13CO12.

| Tempo | Ação | Mediação |
| --- | --- | --- |
| 0–7 min | Contrastar previsão numérica e decisão entre categorias. | Recuperar a aula de regressão linear. |
| 7–12 min | Apresentar cenário de alerta sintético e chance em porcentagem. | Conferir se 70% é interpretado como chance, não como decisão automática. |
| 12–18 min | Solicitar previsão sobre mudar apenas o limiar. | Perguntar se a curva, porcentagem ou categoria mudará. |
| 18–33 min | Explorar módulo guiado: mudar limiar e observar categoria, curva e exemplos. | Distinguir treino do modelo e decisão por limiar. |
| 33–43 min | Comparar 60% e 80% para a mesma probabilidade. | Solicitar justificativa de por que a classificação muda. |
| 43–50 min | Síntese e limite. | Probabilidade não é certeza e depende de dados e modelo. |

**Questão formativa:** “A chance calculada foi 70%. O que muda se o alerta passa de 60% para 80%?”

**Ponto de atenção:** não apresentar esse modelo como previsão certa de acontecimentos reais.

### Encontro 4: k-vizinhos mais próximos (k-NN): amostras, proximidade e votação

**Objetivos:** reconhecer classificação baseada em exemplos rotulados; interpretar distância como proximidade; explicar como o número de vizinhos pode alterar a votação.

**Relação curricular:** EM13CO11 e EM13CO12.

| Tempo | Ação | Mediação |
| --- | --- | --- |
| 0–7 min | Apresentar uma nova amostra sem rótulo, descrita por doçura e acidez. | Perguntar quais dados já existem e qual informação falta para classificá-la. |
| 7–13 min | Explorar no quadro a ideia de pontos próximos. | Diferenciar proximidade no plano de semelhança cotidiana. |
| 13–18 min | Cada estudante prevê se mais vizinhos mantêm a resposta. | Aceitar hipóteses distintas, pedindo justificativa. |
| 18–33 min | Usar módulo guiado: variar valor de k, observar distâncias, vizinhos e votos. | Destacar que o k-vizinhos mais próximos consulta exemplos guardados, sem treino fictício. |
| 33–43 min | Comparar dois valores de k para a mesma amostra. | Solicitar referência a doçura, acidez, distância e voto, não apenas a cores. |
| 43–50 min | Síntese. | Classificação por proximidade depende de exemplos e definição de vizinho. |

**Questão formativa:** “Uma amostra nova ficou perto de exemplos de duas categorias no plano de doçura e acidez. O que pode ocorrer com a votação quando k aumenta?”

**Ponto de atenção:** recorrer também à tabela ou descrição textual, sem depender apenas de cores.

### Encontro 5: Árvore de decisão: largura, altura, regras e caminhos

**Objetivos:** interpretar decisão como resultado de regras; percorrer caminho de decisão; reconhecer que mais profundidade cria mais regras, mas não prova melhor resultado em qualquer caso.

**Relação curricular:** EM13CO10, EM13CO11 e EM13CO12.

| Tempo | Ação | Mediação |
| --- | --- | --- |
| 0–7 min | Retomar o k-vizinhos mais próximos (k-NN) e apresentar estratégia por perguntas. | Mostrar que classificações podem ser construídas de modos diferentes. |
| 7–13 min | Apresentar objetos descritos por largura e altura. | Pedir que estudantes formulem oralmente uma regra simples para separar categorias de objetos. |
| 13–18 min | Solicitar previsão sobre aumentar profundidade. | Não introduzir cálculo de impureza como exigência. |
| 18–33 min | Explorar módulo: divisão, regra inicial, caminho e profundidade. | Relacionar ramos a condições e folhas a decisões. |
| 33–43 min | Analisar um caso específico. | Perguntar se muitas regras garantem resposta melhor e retomar limites. |
| 43–50 min | Comparar árvore e k-vizinhos mais próximos (k-NN). | Registrar: k-NN usa proximidade entre amostras; árvore usa regras e caminhos sobre características como largura e altura. |

**Questão formativa:** “Se a árvore pergunta primeiro sobre largura e depois sobre altura, que caminho pode levar à categoria atribuída a um objeto?”

**Ponto de atenção:** exemplos reservados do módulo são ilustração de uso fora do ajuste, não validação estatística.

### Encontro 6: k-means: agrupamento de amostras por doçura e acidez

**Objetivos:** diferenciar agrupamento de classificação; reconhecer ausência de rótulos prévios; interpretar centróide como centro calculado e acompanhar atualização.

**Relação curricular:** EM13CO11 e EM13CO12.

| Tempo | Ação | Mediação |
| --- | --- | --- |
| 0–7 min | Perguntar o que ocorre quando não há categorias prontas. | Destacar ausência de rótulos antes de nomear k-means. |
| 7–13 min | Apresentar amostras sintéticas em um plano de doçura e acidez, sem rótulos. | Solicitar grupos possíveis justificados por proximidade. |
| 13–18 min | Prever para onde um centro de grupo pode se mover. | Retomar noção de média de posições. |
| 18–33 min | Explorar módulo: atribuição, movimento dos centróides e WSS. | Explicar WSS como dispersão interna, sem formalização obrigatória. |
| 33–43 min | Comparar estado inicial e após atualização. | Pedir motivo do deslocamento de um centróide. |
| 43–50 min | Síntese. | Classificação usa categorias conhecidas; agrupamento forma grupos pela proximidade. |

**Questão formativa:** “Se novos pontos entram perto de um grupo, por que o centróide pode se deslocar?”

**Ponto de atenção:** não afirmar que grupos encontrados são naturalmente verdadeiros ou definitivos.

### Encontro 7: Comparar finalidades, modelos e limites

**Objetivos:** comparar regressão, classificação e agrupamento; relacionar dados e saída à escolha de modelo; reconhecer influência de dados, parâmetros e regras.

**Relação curricular:** EM13CO10, EM13CO11 e EM13CO12.

| Tempo | Ação | Mediação |
| --- | --- | --- |
| 0–8 min | Retomar cinco modelos em quadro comparativo. | Organizar: previsão numérica, classificação e agrupamento. |
| 8–18 min | Apresentar situações inéditas breves para cada estudante. | Perguntar primeiro “qual saída queremos?” e depois “qual modelo pode ajudar?”. |
| 18–33 min | Confirmar duas situações no site, em modo livre ou projeção. | Comparar inclinação, limiar, k, profundidade e centróides. |
| 33–43 min | Estudantes explicam uma escolha e um limite. | Corrigir associações decoradas, como “dois grupos sempre exigem logística”. |
| 43–50 min | Preparar desafio final. | Informar que ele pedirá explicação, não memorização de definições. |

**Produto formativo:** quadro coletivo com finalidade, entrada, saída, controle ou regra e limite de cada modelo.

### Encontro 8: Síntese e instrumento final

**Objetivos:** mobilizar individualmente conceitos para explicar situações novas; relacionar dados, modelo ou regra, representação e resultado; identificar limite de decisão automatizada.

**Relação curricular:** EM13CO10, EM13CO11 e EM13CO12.

| Tempo | Ação | Mediação |
| --- | --- | --- |
| 0–5 min | Retomar finalidade do encontro e regras de realização individual. | Informar que não haverá nota e que respostas incompletas também são importantes. |
| 5–45 min | Aplicar o instrumento final individual, com núcleo comparável, desafio de transferência e questionário breve de percepção. | Esclarecer palavras sem ensinar resposta; registrar apenas dificuldades de compreensão do enunciado. |
| 45–50 min | Encerramento pedagógico sem correção pública individual. | Reafirmar que resultados dependem de dados, modelos, regras e escolhas humanas. |

**Produções de dados principais:** núcleo final comparável, desafio de transferência e questionário de percepção, todos organizados por código anônimo. O instrumento final será consolidado após validação do orientador.

## 5. Adaptações de infraestrutura e acessibilidade

| Condição | Adaptação |
| --- | --- |
| Computadores do laboratório e Chromebooks suficientes | Garantir que cada estudante explore a plataforma individualmente. |
| Equipamentos insuficientes ou falha de rede | Executar site local no computador do professor e projetar; manter instrumentos individuais previstos em papel. |
| Dificuldade de leitura de gráfico | Usar tabela, descrição textual, regra ou caminho de decisão do módulo. |
| Preferência por menos movimento ou uso por teclado | Pausar animações decorativas e usar controles e alternativas textuais. |
| Dificuldades matemáticas acentuadas | Retomar uma ideia por vez com exemplos pequenos e desenho no quadro. |

## 6. Evidências que integrarão a pesquisa

| Material | Função | Integra o corpus principal? |
| --- | --- | --- |
| Diagnóstico inicial | Situar ideias de entrada. | Sim. |
| Previsões e respostas no site | Organizar exploração e devolutiva. | Não; não são salvas. |
| Exploração individual no site | Apoiar a elaboração de hipóteses e explicações. | Não; as interações não são salvas. |
| Registro breve do professor após cada aula | Contextualizar dificuldades e condições de uso. | Sim, como fonte contextual. |
| Desafio final individual | Examinar explicações de síntese. | Sim. |

## 7. Revisões necessárias antes do campo

- confirmar correspondência entre cenários do site e enunciados da sequência;
- adaptar tempo e linguagem à série efetivamente atribuída ao professor;
- revisar instrumentos, sequência e matriz com o orientador;
- verificar laboratório, projeção, energia e acesso local;
- confirmar procedimentos éticos e institucionais antes de produzir ou armazenar dados.
