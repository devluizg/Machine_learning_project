# Plano de aprendizagem para iniciantes — protótipo dos cinco modelos

## Objetivo

Permitir que um estudante do Ensino Médio sem contato prévio com *machine learning* entre no site, entenda o problema representado pelos dados, faça uma previsão, altere uma variável, acompanhe o mecanismo do modelo e explique o resultado. Este plano descreve **o protótipo**, não a lista final de modelos ou um instrumento de pesquisa aprovado.

## Sequência didática implementada

1. **Orientação inicial:** a página inicial apresenta dados, modelo, treino/consulta e teste, define termos básicos e sugere começar pela regressão linear.
2. **Contexto antes do controle:** cada módulo explica o significado dos pontos e a pergunta que o modelo tenta responder. Dados e etiquetas são fictícios.
3. **Aula guiada como padrão:** o primeiro experimento expõe poucos controles e solicita uma hipótese. O modo livre preserva todos os controles e as vistas 3D já existentes.
4. **Cálculo ligado ao estado atual:** cada aula mostra pelo menos um número obtido dos dados e parâmetros presentes na tela — resíduo, saída da curva, distância, impureza ou média de um grupo.
5. **Retorno imediato:** uma questão de escolha oferece confirmação explicada ou pista para tentar novamente. O texto livre continua como rascunho local, sem coleta.
6. **Limite do resultado:** logística e árvore comparam exemplos de construção e casos sintéticos reservados. Os números ilustram a distinção treino/teste; não demonstram desempenho geral nem aprendizagem dos estudantes.
7. **Alternativa textual:** tabelas ou regras textuais permitem consultar valores relevantes sem depender apenas de cor, posição ou vista 3D.

## Experimento essencial por modelo

| Modelo | Ação inicial | Evidência de funcionamento | Questão de compreensão |
| --- | --- | --- | --- |
| Regressão linear | Mudar inclinação; depois avançar um passo do treino | Previsão, resíduo, quadrado do erro e MSE variam | Por que aumentar a inclinação aumenta a previsão em 50 g? |
| Regressão logística | Mudar limiar; depois avançar um passo do treino | Classe pode mudar sem mudar a curva; perda muda no treino | O que o limiar altera? |
| k-NN | Mudar o número de vizinhos | Distâncias, vizinhos destacados e votos | O que acontece quando chega um exemplo novo? |
| Árvore | Mudar profundidade | Regra inicial, impureza, caminho destacado e regiões | O que permite uma árvore mais profunda? |
| k-means | Alternar atribuição e movimento | Média do centro, WSS e trocas de grupo | Para onde o centróide se move? |

## Critérios de verificação técnica

- Os cinco módulos abrem em modo guiado; o modo livre e as vistas 3D continuam acessíveis.
- Cada controle guiado altera a visualização e a explicação numérica correspondente.
- Respostas erradas recebem pista; respostas certas recebem justificativa.
- Os casos reservados da logística e da árvore não participam do ajuste.
- É possível consultar os dados de cada gráfico por texto ou tabela; a tabela do k-NN respeita a distância escolhida.
- `npm run build`, `npm run lint` e `npm run test:run` passam.

## Validação pedagógica ainda necessária

Esta implementação é uma hipótese didática. Falta observar estudantes iniciantes usando o site sem ajuda, verificar se conseguem explicar o que cada modelo aprende e revisar textos, cálculos e volume de informação com o orientador. Também faltam avaliação formal de acessibilidade (teclado, leitor de tela, contraste e uso móvel) e definição acadêmica dos instrumentos de pesquisa. Não registrar respostas identificáveis antes da definição ética e metodológica.
