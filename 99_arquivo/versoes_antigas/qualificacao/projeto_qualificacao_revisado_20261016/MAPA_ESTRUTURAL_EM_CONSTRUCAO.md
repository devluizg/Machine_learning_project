# Mapa estrutural do projeto de qualificação

**Status:** versão de trabalho construída a partir da entrevista de concepção em 9 de outubro de 2026.  
**Uso:** orientar a redação do projeto de qualificação; não substitui orientação do professor nem confirma decisões institucionais pendentes.

## 1. Título provisório

> Ensino introdutório de *machine learning* no Ensino Médio por meio de uma sequência didática apoiada por uma plataforma interativa

O título pode ser ajustado depois da confirmação do campo, da turma e do desenho metodológico.

## 2. Contexto e justificativa

- A proposta pertence prioritariamente ao ensino de Computação: dados, características, modelos, regras, parâmetros, treinamento, previsão, classificação, agrupamento e limites de sistemas de IA são objetos de aprendizagem. A plataforma é recurso de mediação pedagógica, não a finalidade em si.
- A Computação na Educação Básica oferece um contexto curricular relevante para discutir dados, modelos e sistemas de inteligência artificial, com articulação a construir pelos eixos Pensamento Computacional, Mundo Digital e Cultura Digital.
- Estudantes convivem com aplicações de IA, mas podem utilizá-las ou receber seus resultados sem compreender como dados, treinamento, parâmetros e regras participam da produção de previsões, classificações ou agrupamentos.
- O ensino de *machine learning* pode aproximar Computação e Matemática por meio da interpretação de dados, gráficos, coordenadas, funções, probabilidade, distância, média e erro.
- O nível precisa permanecer introdutório: não se pretende antecipar uma formação universitária em IA, exigir programação prévia ou tratar formalizações matemáticas avançadas.
- A proposta não pretende demonstrar que o pensamento computacional melhora genericamente outras disciplinas. As atividades mobilizam dimensões desse pensamento, mas a investigação focaliza a compreensão de fundamentos de *machine learning*.

## 3. Problema educacional provisório

No ensino introdutório de *machine learning*, estudantes podem receber visualizações, classificações ou previsões prontas sem acompanhar como alterações nos dados e nos parâmetros modificam o comportamento de um modelo. Fórmulas e gráficos isolados também podem dificultar a relação entre a representação matemática, o experimento e a explicação do resultado.

## 4. Pergunta de pesquisa provisória

> Como estudantes do Ensino Médio demonstram compreensão sobre dados, modelos, parâmetros, treinamento, previsão, erro e decisão ao participar de uma sequência didática, apoiada por uma plataforma interativa, que aborda cinco modelos introdutórios de *machine learning*?

Esta formulação deverá ser ajustada após a discussão com o orientador e a definição do desenho metodológico.

## 5. Objetivo geral provisório

> Desenvolver e analisar uma sequência didática apoiada por uma plataforma interativa para o ensino introdutório de fundamentos de *machine learning* a estudantes do Ensino Médio.

## 6. Objetivos específicos provisórios

- identificar e discutir referências sobre ensino de inteligência artificial e *machine learning* na Educação Básica, visualização interativa, múltiplas representações e avaliação da compreensão conceitual;
- organizar uma sequência didática que trabalhe os cinco modelos da plataforma por meio do ciclo prever, experimentar, observar e explicar;
- ajustar os exemplos sintéticos, os controles e as explicações matemáticas do produto às condições do campo de aplicação;
- aplicar a sequência em uma turma de Ensino Médio sob docência do pesquisador;
- analisar indícios de compreensão presentes em diagnóstico inicial, desafio final e registros docentes breves;
- sistematizar a plataforma, a sequência e os instrumentos de aplicação como produto educacional.

## 7. Compreensões esperadas dos estudantes

Ao final da sequência, espera-se observar se os estudantes conseguem:

- distinguir dados, características, rótulos e diferentes finalidades dos modelos;
- reconhecer, em nível introdutório, as ideias de regressão, classificação e agrupamento nos cinco modelos;
- antecipar o efeito de uma alteração simples em dado, parâmetro ou regra;
- relacionar a alteração observada ao gráfico, à decisão e à matemática mobilizada;
- explicar o resultado do experimento com linguagem própria, apoiando-se nos conceitos trabalhados;
- reconhecer que resultados dependem dos dados, das regras e dos parâmetros envolvidos.

## 8. Produto educacional

O produto reúne uma plataforma interativa local, em português brasileiro, e uma sequência didática de aproximadamente oito aulas. A plataforma apresenta cinco modelos: regressão linear, regressão logística, k-vizinhos mais próximos, árvore de decisão e k-means.

Cada módulo deverá oferecer situação-problema, hipótese inicial, manipulação de dados ou parâmetros, visualização, explicação matemática gradual, pergunta de verificação e discussão de limites. Os cinco modelos são conteúdos centrais da sequência, ainda que suas formalizações matemáticas tenham níveis adequados a cada conceito.

## 9. Organização pedagógica provisória

1. Abertura por aplicações cotidianas de IA, seguida rapidamente de um problema concreto com dados.
2. Trabalho em duplas durante os experimentos e registros individuais nos momentos de diagnóstico e desafio final.
3. Em cada módulo: prever → experimentar → observar → explicar.
4. Retomadas e comparações entre os cinco modelos, evitando apresentá-los como aulas isoladas sem conexão.
5. Síntese final sobre o que cada modelo tenta aprender, quais dados utiliza, quais decisões produz e quais limites possui.
6. Alinhamento explícito entre habilidade de Computação, objetivo de aprendizagem, atividade e evidência individual, conforme matriz preliminar em `03_pesquisa/MATRIZ_BNCC_OBJETIVOS_ATIVIDADES_E_EVIDENCIAS.md`.

O roteiro completo dos oito encontros, incluindo tempos, mediação, questões formativas, adaptações e limites didáticos, está em `03_pesquisa/metodologia/SEQUENCIA_DIDATICA_PRELIMINAR_OITO_ENCONTROS.md`.

## 10. Cenários sintéticos iniciais

| Modelo | Cenário a validar |
| --- | --- |
| Regressão linear | Temperatura e consumo fictício de energia em uma sala. |
| Regressão logística | Leitura fictícia de sensor e chance de alerta. |
| k-NN | Classificação de objetos ou situações fictícias por duas características mensuráveis. |
| Árvore de decisão | Irrigação simulada de uma horta escolar por umidade e temperatura. |
| k-means | Agrupamento de pontos de coleta fictícios em mapa de bairro. |

Todos os exemplos deverão usar dados sintéticos, evitar dados pessoais dos estudantes e ser revisados quanto à adequação didática.

## 11. Percurso metodológico provisório

- natureza: pesquisa aplicada;
- abordagem: predominantemente qualitativa, com apoio de dados quantitativos descritivos;
- estratégia principal: intervenção pedagógica;
- contexto: turma de Ensino Médio sob docência do pesquisador, com PPA/1º ano como cenário preferencial, porém não definitivo;
- participantes: estudantes iniciantes em *machine learning*;
- evidências: diagnóstico inicial breve, desafio final individual com questões comparáveis e registro docente breve por aula;
- análise: critérios de compreensão, sínteses das respostas, frequências descritivas quando pertinentes e excertos anonimizados;
- ética: confirmação das autorizações e procedimentos aplicáveis antes de qualquer produção de dados.

As versões preliminares dos instrumentos estão em `03_pesquisa/instrumentos/INSTRUMENTOS_DIAGNOSTICO_E_DESAFIO_FINAL.md`. Elas deverão ser revistas antes da aplicação, sem uso como prova escolar ou como medida causal isolada.

## 12. Referencial teórico a construir

1. Computação, pensamento computacional, cultura digital e normas curriculares brasileiras.
2. Ensino de IA e *machine learning* na Educação Básica.
3. Dados, modelos, visualização, múltiplas representações e experimentação guiada.
4. Aprendizagem conceitual, avaliação formativa e interpretação de explicações dos estudantes.
5. Produto educacional e intervenção no contexto de mestrado profissional.

## 13. Pendências que não devem ser disfarçadas no texto

- confirmação de turma, escola, componente curricular e calendário de aplicação;
- aprovação do orientador quanto ao recorte dos cinco modelos e à duração da sequência;
- definição mais precisa da estratégia metodológica complementar, se houver;
- seleção e leitura integral das referências;
- revisão dos instrumentos de diagnóstico e desafio final com o orientador e adequação ao perfil da turma;
- verificação ética e institucional antes da coleta;
- ajustes didáticos e de acessibilidade do site antes do uso em sala.

## 14. Contribuições, limites e cronograma

- contribuições esperadas: proposta articulada de plataforma, sequência, instrumentos, matriz curricular e análise de compreensões conceituais situadas;
- limites: intervenção curta, campo único, diversidade de repertórios matemáticos e digitais, condições de infraestrutura e impossibilidade de generalização causal ampla;
- cronograma: organizado por etapas dependentes da confirmação de campo, das autorizações aplicáveis e do calendário escolar.
