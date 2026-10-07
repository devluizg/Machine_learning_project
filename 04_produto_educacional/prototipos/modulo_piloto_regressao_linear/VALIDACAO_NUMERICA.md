# Validação numérica

## Método

Os cálculos foram refeitos independentemente com aritmética decimal de precisão alta, sem arredondar valores intermediários. Para cada conjunto foram calculadas médias, `b = Σ[(xᵢ−x̄)(yᵢ−ȳ)] / Σ(xᵢ−x̄)²`, `a = ȳ − bx̄`, previsões, resíduos, quadrados, SSE e MSE. As tabelas exibem seis casas para auditoria; a interface usa a regra de arredondamento da especificação.

## Conjunto-base (seis pontos)

`x̄ = 35,000000 g`; `ȳ = 3,501667 cm`; `a = 0,042667 cm`; `b = 0,098829 cm/g`; SSE `= 0,055082 cm²`; MSE `= 0,009180 cm²`; `ŷ(35 g) = 3,501667 cm`.

| ID | `x` (g) | `y` (cm) | `ŷ` (cm) | `e = y−ŷ` (cm) | `e²` (cm²) |
| --- | ---: | ---: | ---: | ---: | ---: |
| P01 | 10 | 1,080000 | 1,030952 | 0,049048 | 0,002406 |
| P02 | 20 | 1,910000 | 2,019238 | -0,109238 | 0,011933 |
| P03 | 30 | 3,120000 | 3,007524 | 0,112476 | 0,012651 |
| P04 | 40 | 3,870000 | 3,995810 | -0,125810 | 0,015828 |
| P05 | 50 | 5,090000 | 4,984095 | 0,105905 | 0,011216 |
| P06 | 60 | 5,940000 | 5,972381 | -0,032381 | 0,001049 |

Soma dos resíduos: `-0,000000` cm (módulo inferior a `0,000001` cm antes do arredondamento apresentado).

## Conjunto-base mais P07

`x̄ = 34,285714 g`; `ȳ = 4,215714 cm`; `a = 1,282903 cm`; `b = 0,085540 cm/g`; SSE `= 25,599969 cm²`; MSE `= 3,657138 cm²`; `ŷ(35 g) = 4,276815 cm`.

| ID | `x` (g) | `y` (cm) | `ŷ` (cm) | `e = y−ŷ` (cm) | `e²` (cm²) |
| --- | ---: | ---: | ---: | ---: | ---: |
| P01 | 10 | 1,080000 | 2,138306 | -1,058306 | 1,120013 |
| P02 | 20 | 1,910000 | 2,993710 | -1,083710 | 1,174427 |
| P03 | 30 | 3,120000 | 3,849113 | -0,729113 | 0,531606 |
| P04 | 40 | 3,870000 | 4,704516 | -0,834516 | 0,696417 |
| P05 | 50 | 5,090000 | 5,559919 | -0,469919 | 0,220824 |
| P06 | 60 | 5,940000 | 6,415323 | -0,475323 | 0,225932 |
| P07 | 30 | 8,500000 | 3,849113 | 4,650887 | 21,630751 |

Soma dos resíduos: `0,000000` cm (módulo inferior a `0,000001` cm antes do arredondamento apresentado).

## Comparações verificadas

| Reta/conjunto | MSE (cm²) |
| --- | ---: |
| Manual inicial: `a=0,5`, `b=0,06`, base | 1,261917 |
| Manual: `a=0,5`, `b=0,10`, base | 0,257917 |
| Manual: `a=0,0`, `b=0,06`, base | 2,413583 |
| Manual próxima: `a=0,0`, `b=0,10`, base | 0,009583 |
| Ajustada OLS, base | 0,009180 |
| Ajustada OLS, base + P07 | 3,657138 |

A referência OLS da base tem MSE menor que todas as retas manuais testadas. A adição de P07 aumenta o MSE ajustado em `3,647958 cm²`, reduz a inclinação em `0,013288 cm/g`, aumenta o intercepto em `1,240237 cm` e muda a previsão em 35 g em `0,775149 cm`. O efeito é perceptível, mas permanece no eixo vertical de `-0,5` a `10,0 cm`.

## Precisão, limites e veredito

Valores internos preservam pelo menos seis casas; valores apresentados ao estudante seguem o arredondamento uniforme definido em `ESPECIFICACAO_FUNCIONAL.md`. Os números são sintéticos, não representam calibração real e não comprovam causalidade. A lei de Hooke apenas contextualiza o cenário sob condições apropriadas; a massa produz força peso quando gravidade é considerada. A validação didática e física permanece necessária.

**Veredito numérico: aprovado para orientar o protótipo navegável, condicionado à validação didática e física do cenário antes de aplicação real.**
