# Plano de revisão teórica após reunião de orientação

Data da revisão: 23 de outubro de 2026

Documento analisado: versão 5 do projeto de qualificação, com 36 páginas.

## Decisão sobre os modelos da sequência

A regressão logística deverá ser substituída por uma máquina de vetores de suporte, apresentada como SVM linear. Essa escolha evita duas aulas consecutivas sobre regressão e torna mais nítida a comparação entre mecanismos de aprendizagem supervisionada:

| Encontro | Modelo | Ideia que o estudante deve explicar |
|---|---|---|
| 2 | Regressão linear | Uma reta resume uma tendência e produz uma previsão numérica. |
| 3 | SVM linear | Uma fronteira separa duas classes e a margem indica o espaço entre essa fronteira e os exemplos mais próximos. |
| 4 | k-NN | A classe depende da proximidade e da votação entre exemplos rotulados. |
| 5 | Árvore de decisão | A classe resulta de uma sequência visível de condições. |
| 6 | k-means | Os grupos surgem pela proximidade com centroides, sem rótulos prévios. |

Para o Ensino Médio, a aula de SVM deve se limitar ao caso bidimensional e linearmente separável. Os conceitos centrais serão fronteira de decisão, margem e vetores de suporte. Kernels, multiplicadores de Lagrange e a dedução do problema de otimização ficam fora do escopo. Como ampliação opcional, um ponto atípico pode mostrar que separar perfeitamente os exemplos nem sempre produz uma regra adequada para casos novos.

## Diagnóstico da fundamentação da versão 5

A base atual é coerente com o desenho da pesquisa. Ela reúne currículo de Computação, ensino introdutório de machine learning, representações visuais, a estratégia de prever, observar e explicar, avaliação formativa e avaliação baseada em desempenho. O texto também evita prometer efeito causal e reconhece o papel da mediação docente.

O principal limite está na composição das fontes. O Capítulo 3 usa 17 referências distintas, mas depende bastante de diretrizes e revisões sistemáticas publicadas até 2023. Há pouca presença de estudos empíricos recentes que mostrem o que estudantes fizeram, quais dificuldades apresentaram e como a aprendizagem foi examinada em intervenções reais. Também falta uma justificativa apoiada em literatura para a progressão entre os cinco modelos escolhidos.

### O que deve ser mantido

- machine learning como conteúdo de Computação, em vez de simples uso de aplicativos;
- relação entre dados, tarefa, regra ou mecanismo, parâmetros e resultado;
- uso de problemas próximos da experiência dos estudantes;
- passagem da situação para tabela, gráfico e formalização matemática;
- ciclo de previsão, experimento, observação e explicação;
- diagnóstico, registros intermediários e instrumento final individual;
- análise qualitativa predominante com frequências descritivas de apoio;
- cautela com generalização e ausência de alegação causal.

### O que precisa ser fortalecido

1. Acrescentar estudos empíricos recentes de aplicação de currículos de IA e machine learning na Educação Básica.
2. Explicar quais dificuldades conceituais a literatura encontra na leitura de dados, treinamento, decisão, erro, generalização e limites dos modelos.
3. Justificar a progressão didática entre regressão linear, SVM, k-NN, árvore e k-means.
4. Dar base mais atual à escolha por contextos autênticos, exploração guiada e produção escrita individual.
5. Explicitar como as quatro dimensões da rubrica derivam dos objetivos de aprendizagem e serão revistas por especialistas antes da aplicação.
6. Diferenciar compreensão conceitual, percepção do estudante e habilidade de operar a interface.
7. Incluir a dimensão ética de modo concreto, ligada à origem dos dados, à representação de grupos, ao erro e ao alcance da decisão.

## Estrutura recomendada para o novo Capítulo 3

### 3.1 Computação, IA e formação na Educação Básica

Manter a Resolução CNE/CEB nº 1/2022, as diretrizes da SBC e AI4K12. Acrescentar uma definição operacional de letramento em IA compatível com o recorte do trabalho. O capítulo deve deixar claro que a pesquisa avalia compreensão conceitual de fundamentos de machine learning, e não um construto amplo de letramento em IA.

### 3.2 Como estudantes aprendem conceitos de machine learning

Organizar a discussão pelo processo de modelagem: reconhecer a tarefa, examinar os dados, compreender como o modelo produz a saída, avaliar erros e reconhecer limites. Estudos empíricos devem sustentar as dificuldades e possibilidades observadas com estudantes reais.

### 3.3 Progressão conceitual dos cinco modelos

Apresentar cada modelo pelo mecanismo que ficará visível ao estudante. A seção deverá explicar por que a sequência passa de uma saída numérica para três mecanismos de classificação e termina com agrupamento sem rótulos. A SVM entra como separação global por uma fronteira; o k-NN, como decisão local por proximidade; a árvore, como decisão por regras; o k-means, como formação de grupos.

### 3.4 Visualização, múltiplas representações e investigação guiada

Manter Ainsworth e White e Gunstone. Relacionar cada representação a uma pergunta da aula. O estudante não deve apenas mover controles: primeiro registra uma previsão, depois altera um elemento e finalmente explica a mudança observada.

### 3.5 Avaliação da compreensão e transferência

Manter Black e Wiliam, Rauber e Gresse von Wangenheim. Acrescentar estudos de instrumentos objetivos e currículos alinhados à avaliação. Explicar por que respostas abertas, tarefas de desempenho e situação inédita são adequadas à pergunta de pesquisa.

### 3.6 Síntese e lacuna da pesquisa

A lacuna deve ser formulada com precisão: ainda são escassas as descrições de intervenções curriculares curtas, conduzidas por professor da própria turma, em escola pública brasileira, que articulem vários mecanismos de machine learning em uma plataforma visual e analisem explicações individuais ao longo da sequência.

Essa formulação deverá ser apresentada como lacuna contextual e metodológica. Ela não deve sugerir que não existam iniciativas brasileiras ou estudos internacionais próximos.

## Referências prioritárias encontradas

| Referência | Contribuição para o projeto | Uso recomendado |
|---|---|---|
| Schönbrodt e Frank (2025) | Análise didática da SVM para a educação secundária, com trajetórias de aprendizagem e equilíbrio entre caixa-preta e caixa-branca. | Fundamentar diretamente a substituição da regressão logística pela SVM linear. |
| Martins et al. (2024), *Machine Learning for All!* | Curso introdutório avaliado com 108 estudantes; combina conceitos, limites, ética e construção de modelo. | Sustentar a viabilidade do ensino introdutório e discutir aplicação com estudantes. |
| Liu e Zhong (2024) | Revisão de 45 estudos empíricos; recomenda contexto autêntico, mediação docente, andaimes e triangulação de evidências. | Atualizar a revisão e justificar o desenho pedagógico. |
| Zhang, Lee e Moore (2024) | Comparação entre 89 estudantes participantes e 69 não participantes em currículo conduzido por professores. | Sustentar a possibilidade de implementação pelo professor da turma, sem transportar seus resultados para este estudo. |
| Jiang et al. (2022) | Análise qualitativa de estudantes do Ensino Médio modelando dados textuais; mostra raciocínio sobre atributos, erros e padrões dos dados. | Apoiar a análise de explicações e o papel ativo do estudante na modelagem. |
| Sanusi et al. (2024) | Currículo com atividades conectadas e desconectadas, dados, visualização, k-NN, árvore e ética; usa produções e entrevistas. | Sustentar atividades contextualizadas, artefatos dos estudantes e triangulação. |
| Chiu et al. (2024) | Desenvolvimento e validação de teste objetivo com 2.390 estudantes; distingue percepção declarada de conhecimento avaliado. | Justificar a separação entre questionário de percepção e evidências de aprendizagem. |
| Rabinowitz et al. (2025) | Currículo de quatro semanas para jovens do Ensino Médio, com medidas antes e depois e discussão das diferenças entre grupos. | Atualizar a evidência empírica e reforçar cautela na generalização. |
| Cassidy et al. (2026) | Avaliação alinhada a um currículo de 18 aulas sobre ML em contexto de saúde; apresenta evidências iniciais de validade e limites dos itens. | Apoiar a revisão por especialistas e o alinhamento entre currículo, instrumento e construto. |

## Mudanças necessárias nos materiais após a adoção da SVM

- substituir regressão logística por SVM no resumo, objetivos, Capítulos 1, 3, 4, 5 e 6;
- incluir SVM e sua forma por extenso na lista de siglas;
- reescrever a Aula 3 e seu recurso didático;
- substituir no site o módulo de regressão logística por uma visualização de SVM linear;
- revisar a comparação de modelos da Aula 7;
- trocar no instrumento final as questões de probabilidade e limiar por itens sobre fronteira, margem e exemplos próximos;
- conferir se o diagnóstico inicial possui questão conceitualmente comparável, sem exigir que o estudante já conheça o nome SVM;
- atualizar rubrica, registros intermediários, guia metodológico, README e links dos PDFs;
- retirar exemplos e fórmulas de regressão logística das páginas gerais do produto.

## Como mostrar o produto na qualificação antes da aplicação

O Capítulo 4 pode ganhar uma subseção chamada **Estado atual do produto educacional**. Ela deve apresentar de três a cinco capturas de tela, cada uma acompanhada de uma legenda analítica que informe a ação possível e o conceito que se torna observável. Uma tabela pode relacionar encontro, problema, controle manipulado, representação, pergunta docente e evidência esperada.

Esses elementos comprovam o estágio de desenvolvimento e permitem avaliar a coerência do projeto. Não constituem dados da pesquisa, não validam a aprendizagem e não devem aparecer como resultados da intervenção.

## Ordem de execução

1. Definir o desenho didático da SVM linear.
2. Alterar a plataforma e testar a visualização.
3. Reescrever a Aula 3.
4. Atualizar os instrumentos comparáveis e a rubrica.
5. Inserir as referências recentes no Capítulo 3.
6. Atualizar a descrição da sequência nos demais capítulos.
7. Inserir as capturas do produto no Capítulo 4.
8. Compilar a nova versão e fazer uma conferência global de termos, modelos e encontros.

## Observação sobre a evidência específica para SVM

A busca encontrou uma referência diretamente alinhada à decisão do orientador. Schönbrodt e Frank (2025) propõem a SVM para introduzir machine learning orientado por dados na educação secundária. O trabalho descreve trajetórias para estudantes de 13 a 14 anos e de 16 a 18 anos, usando pontos de duas classes, retas separadoras, margem, treinamento e validação. Essa fonte permite justificar a SVM por seu valor didático, e não apenas por ser um algoritmo conhecido na área.

A proposta do projeto deve fazer uma adaptação mais curta. Em cinquenta minutos, o estudante poderá representar duas classes, comparar possíveis fronteiras e reconhecer que os pontos mais próximos limitam a margem. A etapa de validação pode aparecer como pergunta final ou aprofundamento, sem incluir o formalismo completo de otimização.
