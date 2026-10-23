# Casos de teste numéricos

Aplicar tolerância absoluta de `0,000001` aos valores internos e `0,0005` aos valores exibidos com três casas. Em todos os casos, o resíduo usa `eᵢ = yᵢ − ŷᵢ`.

| ID | Entrada | Cálculo e valor esperado | Feedback esperado | Tolerância |
| --- | --- | --- | --- | --- |
| N01 | Base; `a=0,5`, `b=0,06`. | `ŷ(35)=2,600000`; SSE `7,571500`; MSE `1,261917`. | “Reta inicial… MSE 1,262 cm².” | interna `0,000001`; exibida `0,0005` |
| N02 | Base; alterar somente `b` de `0,06` para `0,10`; `a=0,5`. | `ŷ(35)=4,000000`; MSE `0,257917`. | “Inclinação agora é 0,100 cm/g; para a mesma massa, as previsões aumentaram. MSE passou de 1,262 para 0,258 cm².” | mesma |
| N03 | Base; alterar somente `a` de `0,5` para `0,0`; `b=0,06`. | `ŷ(35)=2,100000`; MSE `2,413583`. | “Intercepto agora é 0,000 cm; todas as previsões desceram 0,500 cm.” | mesma |
| N04 | Base; reta manual próxima: `a=0,0`, `b=0,10`. | `ŷ(35)=3,500000`; SSE `0,057500`; MSE `0,009583`, maior que MSE OLS `0,009180`. | “MSE da sua reta: 0,010 cm²; referência ajustada: 0,009 cm².” | mesma |
| N05 | Base; revelar referência OLS. | `a=0,042667`; `b=0,098829`; SSE `0,055082`; MSE `0,009180`; `ŷ(35)=3,501667`. | “Referência ajustada: MSE 0,009 cm².” | mesma |
| N06 | Base + P07; revelar referência OLS. | `a=1,282903`; `b=0,085540`; SSE `25,599969`; MSE `3,657138`; `ŷ(35)=4,276815`. | “Nova observação adicionada; MSE ajustado mudou de 0,009 para 3,657 cm².” | mesma |
| N07 | Base; referência OLS; selecionar P03. | `ŷ=3,007524`; `e=+0,112476`; `e²=0,012651`. | “O observado está 0,112 cm acima da previsão.” | mesma |
| N08 | Base; referência OLS; selecionar P04. | `ŷ=3,995810`; `e=-0,125810`; `e²=0,015828`. | “O observado está 0,126 cm abaixo da previsão.” | mesma |
| N09 | P07 revelado, resíduos e referência visíveis, controles modificados; acionar reinício. | Seis pontos; `a=0,5`; `b=0,06`; resíduos e referência ocultos; MSE manual `1,261917`. | “Experimento reiniciado com a reta inicial.” | estado exato; MSE mesma |
| N10 | Base; gráfico indisponível após cálculo válido com `a=0,0`, `b=0,10`. | Tabela mantém seis linhas e MSE `0,009583`; não recalcular ou apagar. | “Gráfico indisponível; a tabela e a descrição textual continuam disponíveis.” | valores preservados |

## Conferências adicionais

- N05 deve ter MSE menor que N01, N02, N03 e N04.
- N06 deve alterar visivelmente `a`, `b`, MSE e previsão em 35 g em relação a N05.
- N07 e N08 verificam, respectivamente, os sinais positivo e negativo do resíduo.
- N09 preserva textos de previsão, justificativa e síntese na sessão até confirmação explícita de descarte.
