# Mapa pedagógico — módulo-piloto: tendência em dados de uma mola

## Natureza provisória

Este é um protótipo pedagógico de baixa fidelidade. A regressão linear é um tema-piloto para validar a estrutura de aprendizagem; não representa aprovação definitiva dos modelos do produto ou do escopo da dissertação.

## Público

Estudantes iniciantes do Ensino Médio. A série específica, a duração e o contexto de aplicação ainda serão definidos.

## Propósito do módulo

Permitir que o estudante investigue, com dados sintéticos de uma mola, como uma reta pode resumir uma tendência e como o afastamento entre um ponto observado e a previsão da reta contribui para avaliar o ajuste.

## Conhecimentos prévios esperados

- Plano cartesiano e leitura de eixos.
- Média e operações algébricas básicas.
- Interpretação de gráficos.
- Ideia intuitiva de relação entre duas variáveis.

## Objetivos de aprendizagem

Ao final, o estudante deverá ser capaz de:

1. Explicar que uma reta de regressão representa uma tendência nos dados.
2. Interpretar o resíduo como diferença entre valor observado e valor previsto.
3. Explicar qualitativamente por que a melhor reta procura reduzir a média dos erros quadráticos (MSE).

## Situação-problema

Em uma atividade de Física, massas diferentes são penduradas em uma mola e mede-se o seu alongamento. As medidas sintéticas mostram pequenas variações. A pergunta orientadora é: **como podemos usar uma reta para fazer uma previsão razoável do alongamento para uma nova massa, sem fingir que todas as medidas são exatamente iguais?**

Dados iniciais sugeridos: seis pares sintéticos de massa (g) e alongamento (cm), com tendência crescente e pequena variação. Os valores numéricos finais, o ponto atípico e as faixas de manipulação precisam ser definidos e revisados antes do protótipo navegável.

## Conceitos trabalhados

- Variável de entrada `x` (massa, em g) e variável observada `y` (alongamento, em cm).
- Tendência linear e reta de previsão.
- Inclinação `b` (cm/g) e intercepto `a` (cm) como formas de mover a reta.
- Valor previsto `ŷ` (cm), valor observado `y` (cm) e resíduo `eᵢ = yᵢ − ŷᵢ` (cm).
- Média dos erros quadráticos, `MSE` (cm²), como resumo que dá mais peso a afastamentos maiores; seus valores devem ser comparados apenas para o mesmo conjunto de dados e unidade.
- Ponto atípico como dado que pode alterar a reta e exige interpretação.

## Possíveis dificuldades

- Confundir a reta com uma regra perfeita para todos os pontos.
- Ler o resíduo como distância horizontal, e não diferença vertical entre observado e previsto.
- Interpretar `a` e `b` como símbolos sem vínculo com a posição da reta.
- Supor que uma reta mais próxima de um único ponto é sempre melhor.
- Concluir que um ponto atípico deve ser automaticamente apagado, sem investigar sua origem.

## Sequência didática

1. Apresentar a situação da mola e pedir uma previsão antes de qualquer alteração.
2. Mostrar os pontos no plano cartesiano e solicitar a descrição da tendência percebida.
3. Permitir mover manualmente a inclinação e o intercepto da reta; cada alteração atualiza o gráfico e uma descrição textual.
4. Exibir os resíduos como segmentos verticais e pedir que o estudante compare observado e previsto.
5. Introduzir, nessa ordem, `ŷ = a + bx`, `eᵢ = yᵢ − ŷᵢ` e `MSE = (1/n) Σ(yᵢ − ŷᵢ)²`, sempre conectando símbolo, gráfico, unidades e propósito.
6. Depois da tentativa manual, explicar que a reta ajustada é a que minimiza a **soma dos resíduos ao quadrado** no conjunto. Como o número de pontos `n` é fixo, minimizar essa soma ou o MSE produz a mesma reta; mostrar essa referência para comparação qualitativa.
7. Antes de exibir o ponto atípico, pedir previsão de seu efeito; então adicioná-lo e discutir a mudança na reta, nos resíduos e no MSE.
8. Retomar os três objetivos e registrar uma síntese curta do estudante.

## Evidências de aprendizagem

- Previsão inicial justificada em linguagem comum antes de mexer nos controles.
- Explicação de que mover a inclinação ou o intercepto altera os valores previstos e os segmentos de resíduo.
- Associação correta entre um ponto específico, seu `y`, seu `ŷ` e seu `eᵢ` na tabela alternativa e no gráfico.
- Comparação em texto entre reta manual e reta ajustada, mencionando o critério de menor MSE, e não só preferência estética.
- Explicação do efeito do ponto atípico e de que a previsão linear é uma aproximação da tendência observada.

## Limites do módulo

- Não ensina derivadas, álgebra matricial, inferência estatística, equação normal ou treinamento por épocas.
- Não apresenta múltiplas métricas, visualização 3D ou taxa de aprendizagem.
- A regressão descreve uma associação nos dados sintéticos e não demonstra, por si só, uma causa física. No cenário de uma mola ideal em pequena deformação, a lei de Hooke relaciona força e alongamento; com gravidade local constante, a massa altera a força aplicada. Essa relação física contextualiza o exemplo, mas precisa de validação didática e física antes do uso.
- Não define tecnologia, armazenamento de dados, avaliação formal ou modelos finais da plataforma.
