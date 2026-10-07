# Especificação funcional e numérica

## Escopo e dados

O módulo usa exclusivamente os sete registros sintéticos em `DADOS_SINTETICOS.csv`: seis pontos-base inicialmente visíveis e um ponto atípico inicialmente oculto. Eles são valores didáticos, não medições ou calibração reais de uma mola.

| Elemento | Definição e unidade |
| --- | --- |
| `x` | massa suspensa, em g |
| `y` | alongamento observado, em cm |
| `ŷ` | alongamento previsto pela reta, em cm |
| `a` | intercepto da reta, em cm |
| `b` | inclinação da reta, em cm/g |
| `eᵢ` | resíduo `yᵢ − ŷᵢ`, em cm |
| `eᵢ²`, SSE e MSE | quadrado do resíduo, soma dos quadrados e média dos quadrados, em cm² |

O conjunto-base é `(10, 1,08)`, `(20, 1,91)`, `(30, 3,12)`, `(40, 3,87)`, `(50, 5,09)` e `(60, 5,94)`, nas unidades acima. O ponto atípico é `(30, 8,50)`. Ele deve ser descrito como uma observação a investigar — por exemplo, condição experimental, leitura ou limite do modelo — nunca como dado automaticamente incorreto.

## Fórmulas e arredondamento

`ŷ = a + bx`; `eᵢ = yᵢ − ŷᵢ`; `SSE = Σeᵢ²`; `MSE = SSE/n`.

A reta ajustada é a reta de mínimos quadrados com intercepto: escolhe `a` e `b` para minimizar SSE. Com `n` fixo, a mesma reta minimiza MSE. Cálculos internos usam ao menos seis casas decimais e não usam valores já arredondados. Na interface: `a`, `b`, `ŷ`, `eᵢ`, SSE e MSE mostram três casas; `eᵢ²`, duas; massas, uma casa inteira; alongamentos observados, duas. Empregar arredondamento para o mais próximo (5 sobe) somente na exibição.

## Resultados de referência

| Conjunto | `x̄` (g) | `ȳ` (cm) | `a` (cm) | `b` (cm/g) | SSE (cm²) | MSE (cm²) | `ŷ(35 g)` (cm) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Base | 35,000000 | 3,501667 | 0,042667 | 0,098829 | 0,055082 | 0,009180 | 3,501667 |
| Base + P07 | 34,285714 | 4,215714 | 1,282903 | 0,085540 | 25,599969 | 3,657138 | 4,276815 |

## Controles e eixos

| Controle | Mínimo | Máximo | Incremento | Inicial | Justificativa |
| --- | ---: | ---: | ---: | ---: | --- |
| Intercepto `a` (cm) | -0,5 | 1,0 | 0,1 | 0,5 | Inclui a reta ajustada aproximada e deslocamentos claramente altos ou baixos sem inverter a situação. |
| Inclinação `b` (cm/g) | 0,04 | 0,14 | 0,01 | 0,06 | Mantém crescimento positivo; permite reta muito plana, próxima do ajuste (`0,10`) e mais inclinada sem centenas de acionamentos. |

Os botões de incremento/decremento alteram exatamente um incremento, respeitam o limite (sem ultrapassá-lo) e atualizam rótulo, cálculo e anúncio. Manter pressionado não é requisito. Teclas equivalentes seguem o mesmo passo. `Reiniciar` restaura `a = 0,5`, `b = 0,06`, oculta resíduos e reta ajustada, remove P07 e preserva textos da sessão após aviso antes de descartá-los.

Eixos: massa de `0` a `70 g`, com marcas a cada `10 g`; alongamento de `-0,5` a `10,0 cm`, com marcas a cada `1 cm`. Todas as combinações permitidas de `a` e `b` para os dados de `10–60 g` ficam no intervalo vertical. A tabela e a descrição textual mostram os mesmos valores relevantes do gráfico.

## Regras de atualização

| Ação | Dados e cálculos | Elementos e anúncio acessível | Respostas preservadas |
| --- | --- | --- | --- |
| Alterar `b` | Mantém dados e `a`; recalcula `ŷ`, resíduos, quadrados, SSE e MSE da reta manual. | Atualiza reta, tabela, descrição e MSE. “Inclinação agora é [b] cm/g; para a mesma massa, as previsões [aumentaram/diminuíram]. MSE atual: [valor] cm².” | Previsões, justificativas e sínteses da sessão. |
| Alterar `a` | Mantém dados e `b`; refaz os mesmos cálculos. | Desloca a reta paralelamente. “Intercepto agora é [a] cm; todas as previsões [aumentaram/diminuíram] [diferença] cm.” | As mesmas. |
| Mostrar resíduos | Não altera dados ou cálculos. | Exibe segmentos verticais e coluna de resíduos. “Resíduos visíveis: positivo significa ponto acima da reta; negativo, abaixo.” | As mesmas. |
| Selecionar ponto | Não altera cálculos. | Destaca linha/tabela e informa `x`, `y`, `ŷ`, `eᵢ`, sinal e `eᵢ²`. | As mesmas. |
| Revelar reta ajustada | Não altera reta manual; usa referência OLS do conjunto atualmente ativo. | Mostra reta rotulada e compara MSE manual/ajustada. “Referência ajustada: MSE [valor]; reta manual: [valor].” | As mesmas. |
| Registrar previsão de P07 | Guarda resposta textual; P07 segue oculto. | Libera ação de adicionar. “Previsão registrada; o resultado ainda não foi mostrado.” | Todas. |
| Adicionar P07 | Inclui P07; recalcula OLS de 7 pontos e, para a reta manual, recálcula resíduos/SSE/MSE com 7 pontos. | Atualiza gráfico, tabela, descrição e referências. “Nova observação adicionada; MSE ajustado mudou de 0,009 para 3,657 cm².” | Todas. |
| Remover P07 | Retorna aos seis pontos e recalcula referências correspondentes. | “Observação removida da comparação; conjunto-base restaurado.” | Todas, inclusive previsão de P07. |
| Reiniciar | Restaura controles e visibilidade inicial; não apaga textos sem confirmação. | “Experimento reiniciado com a reta inicial.” | Textos preservados até confirmação explícita de descarte. |
| Falha de cálculo | Não aplica valor parcial; mantém último resultado válido. | “Não foi possível atualizar o cálculo; valores anteriores foram mantidos. Tente novamente.” | Todas. |
| Gráfico indisponível | Mantém dados e cálculos; disponibiliza tabela e descrição. | “Gráfico indisponível; a tabela e a descrição textual continuam disponíveis.” | Todas. |

## Limites científicos e pedagógicos

A regressão descreve o padrão destes dados, não demonstra sozinha causa física. A lei de Hooke dá contexto apenas sob condições apropriadas; com gravidade considerada, a massa produz força peso. O cenário, os valores e a apresentação ainda exigem validação didática e física antes de qualquer aplicação real.
