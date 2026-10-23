# Matriz preliminar de alinhamento curricular

**Projeto:** Ensino introdutório de *machine learning* no Ensino Médio por meio de uma sequência didática apoiada por uma plataforma interativa  
**Data:** 23 de outubro de 2026  
**Status:** versão de trabalho para discussão com o orientador e adequação à rede e à turma de aplicação.

## 1. Finalidade e cuidado de leitura

Esta matriz transforma o vínculo declarado com a Computação na Educação Básica em relações verificáveis entre habilidades curriculares, objetivos de aprendizagem, atividades e evidências a observar. Ela não afirma que a Base Nacional Comum Curricular determina o ensino dos cinco algoritmos previstos no protótipo. Regressão linear, regressão logística, k-NN, árvore de decisão e k-means são meios didáticos escolhidos para explorar fundamentos de inteligência artificial, modelos computacionais simples, dados e previsões.

O núcleo curricular adotado é formado por três habilidades do Ensino Médio presentes no anexo da Resolução CNE/CEB nº 1/2022:

- **EM13CO10:** conhecer fundamentos da inteligência artificial, comparando-a com a inteligência humana e analisando potencialidades, riscos e limites;
- **EM13CO11:** criar e explorar modelos computacionais simples para simular e realizar previsões, identificando sua importância no desenvolvimento científico;
- **EM13CO12:** produzir, analisar, gerir e compartilhar informações a partir de dados, utilizando princípios de ciência de dados.

As habilidades de Matemática relacionadas a leitura de gráficos, funções, probabilidade, medidas de tendência central e análise de dados poderão ser acionadas conforme a série e o componente curricular da turma. Elas sustentam a interpretação, mas não deslocam o objeto principal da proposta, que é o ensino de Computação.

## 2. Correspondência geral

| Habilidade de Computação | Objetivo de aprendizagem do projeto | Experiência didática planejada | Evidência individual esperada |
| --- | --- | --- | --- |
| EM13CO10 | Reconhecer que sistemas de IA produzem resultados a partir de dados, regras ou modelos, e discutir que seus resultados têm possibilidades e limites. | Conversa inicial sobre aplicações cotidianas, leitura de situações com IA e retomadas ao final de cada módulo. | Diferencia uma ferramenta de IA de uma pessoa; identifica ao menos uma possibilidade e um limite relacionado a dados, regras ou contexto. |
| EM13CO11 | Antecipar e interpretar como uma alteração simples em dado, parâmetro ou regra modifica uma saída do modelo. | Ciclo prever, experimentar, observar e explicar nos cinco módulos da plataforma. | Registra uma previsão coerente, compara-a com o resultado e explica a relação entre a alteração e a saída observada. |
| EM13CO12 | Identificar dados, características, rótulos quando houver e finalidade da tarefa, interpretando tabelas, gráficos e agrupamentos. | Situações sintéticas, tabelas e gráficos de dispersão, probabilidade, vizinhança, regras e centróides. | Indica quais dados são pertinentes, distingue tarefa de previsão, classificação ou agrupamento e lê a representação utilizada. |

## 3. Matriz da sequência provisória de oito encontros

| Encontro | Foco e conceitos de Computação | Habilidade curricular principal | Atividade com a plataforma e mediação | Evidência a observar | Limite didático deliberado |
| --- | --- | --- | --- | --- | --- |
| 1 | Dados, características, modelo, treinamento, previsão, classificação e agrupamento. | EM13CO10 e EM13CO12 | Partir de aplicações de IA e chegar a uma situação concreta com dados sintéticos. Solicitar que cada estudante distinga o que é dado, qual resultado se deseja produzir e se há rótulos. | Em registro individual breve, identifica dados e finalidade de uma situação simples; não precisa conhecer os cinco modelos. | Não apresentar IA como entidade autônoma ou iniciar com definições matemáticas abstratas. |
| 2 | Regressão linear: relação entre variáveis, tendência, previsão, resíduo e erro. | EM13CO11 e EM13CO12 | Prever o efeito de uma mudança nos pontos ou na reta; observar gráfico e comparar valor previsto e observado. | Relaciona alteração nos dados ou na inclinação a mudança na previsão; interpreta um resíduo em linguagem acessível. | Não derivar fórmula por cálculo nem exigir ajuste manual perfeito da reta. |
| 3 | Regressão logística: probabilidade, limiar e classificação binária. | EM13CO10, EM13CO11 e EM13CO12 | Alterar dados ou limiar de um alerta fictício e discutir diferença entre probabilidade e categoria final. | Explica que a mudança de limiar pode alterar a classe mesmo que a probabilidade não mude. | Não ensinar regressão logística como cálculo universitário ou como certeza sobre eventos reais. |
| 4 | k-NN: distância, proximidade, número de vizinhos e votação. | EM13CO11 e EM13CO12 | Prever a classe de um novo ponto, variar o número de vizinhos e observar a votação. | Justifica a classificação usando proximidade e voto dos exemplos, reconhecendo efeito de mudar o valor de *k*. | Não exigir programação ou formalização geral de métricas de distância. |
| 5 | Árvore de decisão: regras, divisões e caminhos de decisão. | EM13CO10, EM13CO11 e EM13CO12 | Explorar uma situação fictícia de irrigação; alterar uma regra ou seguir ramos da árvore até uma decisão. | Explica a saída como consequência de regras e dados de entrada; identifica que regras diferentes podem levar a resultados diferentes. | Não abordar critérios avançados de impureza ou treinamento completo de árvores. |
| 6 | k-means: agrupamento sem rótulos, centróides e atualização dos grupos. | EM13CO11 e EM13CO12 | Prever grupos possíveis em mapa fictício, mover centróides ou acompanhar a atualização dos agrupamentos. | Distingue agrupamento de classificação e relaciona proximidade ao centróide à formação de grupos. | Não exigir demonstração matemática da otimização ou justificar formalmente a convergência. |
| 7 | Comparação entre modelos: finalidades, dados, resultados e limites. | EM13CO10, EM13CO11 e EM13CO12 | Analisar novas situações e decidir se envolvem previsão de valor, classificação ou agrupamento; justificar o modelo mais compatível. | Escolhe uma finalidade adequada e justifica pelos dados e pelo tipo de saída desejada, não apenas pelo nome do algoritmo. | Não exigir que exista uma única solução para toda situação; discutir escolhas e limites. |
| 8 | Síntese e explicação individual. | EM13CO10, EM13CO11 e EM13CO12 | Realizar instrumento individual sem consulta à plataforma: núcleo comparável ao diagnóstico, desafio de transferência e breve questionário de percepção. | Produz explicação que conecte dados, procedimento ou regra, representação e saída do sistema; mobiliza conceitos em situação inédita. | Não converter o instrumento em prova classificatória nem inferir domínio profissional de IA a partir dele. |

## 4. Critérios preliminares para leitura das evidências

Os instrumentos individuais deverão ser construídos para permitir reconhecer diferentes níveis de explicação. A matriz abaixo é um guia inicial, não uma rubrica final.

| Dimensão | Indício inicial | Indício em desenvolvimento | Indício consistente para o nível introdutório |
| --- | --- | --- | --- |
| Dados e tarefa | Nomeia elementos isolados ou confunde dado, resultado e modelo. | Identifica parte dos dados e reconhece uma finalidade geral. | Distingue dados, características e tipo de tarefa, justificando a escolha. |
| Previsão e alteração | Descreve o que vê depois da alteração, sem antecipação ou justificativa. | Formula previsão simples ou identifica uma mudança observada. | Antecipa uma consequência e explica a relação entre alteração, modelo e saída. |
| Representações | Lê um elemento visual isolado. | Relaciona gráfico, tabela ou regra a uma resposta. | Integra representação, conceito e resultado em explicação coerente. |
| Limites e IA | Trata a saída como resposta automática ou infalível. | Reconhece que dados ou regra influenciam o resultado. | Identifica uma possibilidade e um limite do modelo, evitando atribuir intenção humana ao sistema. |

## 5. Uso da matriz na pesquisa

1. **Planejamento:** cada aula deverá indicar quais linhas da matriz mobiliza. Os registros individuais de previsão e explicação serão concentrados nos encontros 2, 4 e 6; nos demais, a mediação terá caráter formativo e poderá ser registrada pelo docente.
2. **Instrumentos:** o diagnóstico e o núcleo comparável do instrumento final deverão conter itens sobre dados, tipo de tarefa, alteração e interpretação. O desafio de transferência e o questionário de percepção terão funções próprias, sem repetir mecanicamente os exemplos do laboratório.
3. **Análise:** as respostas serão organizadas pelas dimensões da seção 4; frequências poderão apoiar a descrição, mas não substituirão a leitura qualitativa das explicações.
4. **Revisão de campo:** a seleção final de habilidades e a linguagem dos instrumentos deverão ser ajustadas à série, ao componente curricular, ao currículo da rede e às condições reais de aplicação.

## Referências normativas

BRASIL. Conselho Nacional de Educação. Câmara de Educação Básica. **Resolução CNE/CEB nº 1, de 4 de outubro de 2022.** Define normas sobre Computação na Educação Básica, complemento à Base Nacional Comum Curricular. Brasília, DF: MEC, 2022. Disponível em: <https://portal.mec.gov.br/docman/outubro-2022-pdf/241671-rceb001-22/file>. Acesso em: 9 out. 2026.

BRASIL. Conselho Nacional de Educação. Câmara de Educação Básica. **Parecer CNE/CEB nº 2, de 17 de fevereiro de 2022.** Normas sobre Computação na Educação Básica – Complemento à BNCC. Anexo. Brasília, DF: MEC, 2022. Disponível em: <https://www.gov.br/mec/pt-br/cne/pdf/normas-classificadas-por-assunto/base-nacional-comum-curricular-ensino-medio-bncc-em/pceb002_22.pdf/view>. Acesso em: 9 out. 2026.
