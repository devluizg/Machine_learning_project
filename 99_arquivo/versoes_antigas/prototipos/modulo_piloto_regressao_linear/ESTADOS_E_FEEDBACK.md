# Estados e feedback determinístico

## Estados

| Estado | Condição | Interface e dados | Feedback/anúncio |
| --- | --- | --- | --- |
| Inicial | Seis pontos; `a=0,5`, `b=0,06`; sem resíduos, referência ou P07. | Mostra reta manual e tabela-base. | “Reta inicial: intercepto 0,500 cm, inclinação 0,060 cm/g; MSE 1,262 cm².” |
| Após manipulação | `a` ou `b` mudou. | Atualiza tabela, descrição, reta e MSE. | Regra de direção abaixo. |
| Resíduos visíveis | Alternância ativada. | Mostra segmentos, coluna `eᵢ` e `eᵢ²`. | “Resíduos visíveis; compare cada ponto com a reta.” |
| Reta ajustada | Tentativa manual registrada e referência revelada. | Mostra referência OLS rotulada; manual permanece. | “A referência minimiza MSE: [MSE ajustado] cm²; a sua reta: [MSE manual] cm².” |
| Previsão de P07 pendente | Antes de uma resposta sobre a nova medida. | P07 não aparece e botão de inclusão fica indisponível. | “Registre sua previsão antes de revelar a nova observação.” |
| P07 revelado | Previsão registrada e ponto adicionado. | Sete pontos, tabela e OLS de 7 pontos. | “A nova observação está acima da tendência anterior; investigue a condição antes de julgá-la.” |
| P07 removido | P07 estava revelado e foi removido. | Retorna à base e à OLS de 6 pontos. | “Conjunto-base restaurado; a previsão registrada foi preservada.” |
| Erro recuperável | Cálculo solicitado falhou. | Mantém último estado válido e controles. | “Cálculo não atualizado; valores anteriores permanecem.” |
| Gráfico indisponível | Renderização falhou. | Tabela e descrição textual são a alternativa completa. | “Gráfico indisponível; consulte a tabela com `x`, `y`, `ŷ`, `eᵢ`, `eᵢ²`, SSE e MSE.” |
| Redução de movimento | Preferência ativada. | Atualizações instantâneas, sem transição da reta/segmentos. | “Redução de movimento ativada; os valores continuam os mesmos.” |

## Regras de feedback

- Ao aumentar `b`, dizer “para a mesma massa, as previsões aumentaram”; ao reduzir, “diminuíram”. Informar `b` e MSE atuais.
- Ao aumentar `a`, dizer “a reta subiu [incremento] cm em todos os valores previstos”; ao reduzir, “desceu [incremento] cm”.
- Comparar MSE atual e anterior apenas pelo valor: “MSE passou de [anterior] para [atual] cm²; a diferença é [atual − anterior] cm².” Não qualificar como bom ou ruim.
- Ao selecionar ponto: se `eᵢ > 0`, “o observado está [eᵢ] cm acima da previsão”; se `eᵢ < 0`, “está [|eᵢ|] cm abaixo”; se `eᵢ = 0`, “coincide com a previsão”.
- Ao revelar a referência, informar ambos os MSE e a diferença absoluta, sem dizer que a reta manual está errada.
- Ao adicionar P07, informar mudança de MSE ajustado de `0,009` para `3,657 cm²` e de inclinação de `0,099` para `0,086 cm/g` (valores exibidos). Não atribuir automaticamente a origem do ponto.

## Anúncios para leitor de tela

Anunciar somente a consequência imediata de uma ação e não repetir a tabela inteira. A descrição textual persistente contém: conjunto ativo, reta manual, referência quando revelada, MSE manual, MSE de referência e ponto selecionado. A tabela é navegável por linha e tem cabeçalhos de unidade. Alertas de erro e mudança de P07 usam região de status; nenhuma mensagem depende somente de cor, posição ou animação.
