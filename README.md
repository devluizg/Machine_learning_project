# Plataforma Interativa para Ensino de Machine Learning

Projeto acadêmico de uma plataforma interativa para apoiar o ensino de fundamentos de *machine learning* a estudantes do Ensino Médio, com atenção especial a alunos iniciantes.

Este projeto será utilizado na **pré-defesa do mestrado profissional ProfComp de Luiz Gabriel**, desenvolvido sob orientação do **professor Marcos Braga**. O trabalho está situado no contexto da educação e da docência e busca articular conteúdo matemático, visualização e experimentação interativa.

## Ideia central

A plataforma deverá ajudar o estudante a compreender o que acontece por trás de alguns modelos selecionados de *machine learning*. Cada módulo deverá relacionar:

1. uma explicação intuitiva;
2. a matemática do modelo, apresentada de maneira gradual;
3. gráficos e visualizações interativas;
4. controles para experimentar parâmetros e observar seus efeitos;
5. atividades voltadas à compreensão, e não somente à execução de código.

O objetivo não é cobrir todos os algoritmos existentes. O conjunto de modelos será deliberadamente limitado e escolhido conforme sua relevância pedagógica, seu potencial de visualização e a viabilidade da pesquisa.

## Público-alvo

- Estudantes do Ensino Médio;
- alunos iniciantes em *machine learning* e conceitos de inteligência artificial;
- alunos que precisam compreender a relação entre conceitos, matemática e comportamento dos modelos;
- professores da Educação Básica interessados em utilizar recursos visuais e interativos em suas aulas.

## Referência de inspiração

O projeto tem como referência conceitual e visual a plataforma [NEURON — Machine Learning, Made Visible](https://kw1fpt-ahmet-duyar.shinyapps.io/Neuron/).

A referência deve servir como inspiração para a organização pedagógica e para a integração entre intuição, fórmulas e visualizações. Este projeto deverá possuir identidade, conteúdo, implementação e proposta de pesquisa próprios, adequados ao público brasileiro e ao contexto do ProfComp.

## Estado atual

O projeto segue em definição acadêmica. Há agora um [protótipo local do site](04_produto_educacional/site/) com cinco laboratórios didáticos: regressão linear, regressão logística, k-NN, árvore de decisão e k-means. Eles incluem um percurso inicial guiado para iniciantes, variação de dados e parâmetros, acompanhamento de treinamento quando o algoritmo realmente o possui e vistas 3D de grandezas derivadas. Essa seleção foi feita para explorar a experiência educacional e **não representa aprovação final** dos modelos pelo orientador.

Ainda precisam ser acordados com o orientador:

- problema e pergunta de pesquisa;
- objetivos geral e específicos;
- modelos de *machine learning* que farão parte da plataforma;
- tecnologias de implementação;
- desenho da avaliação com os estudantes;
- critérios de aprendizagem, usabilidade e análise dos resultados.

Consulte [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) para conhecer a organização completa, [docs/PROJECT_CONTEXT.md](docs/PROJECT_CONTEXT.md) para o contexto acadêmico e pedagógico e [docs/DECISIONS.md](docs/DECISIONS.md) para acompanhar as decisões do projeto.

O uso de modelos de IA no projeto segue a [arquitetura econômica de orquestração](09_orquestracao_ia/README.md), que separa planejamento e validação avançados de tarefas executivas de menor custo.
# Machine_learning_project
