# Critérios de aceite verificáveis

## Aprendizagem

- [ ] Há uma atividade de previsão antes de qualquer manipulação da reta.
- [ ] A síntese solicita uma explicação sobre tendência, resíduo e MSE, sem introduzir um quarto objetivo de aprendizagem; a nota sobre limites permanece contextual e não é avaliada como novo objetivo.
- [ ] O feedback das respostas explica a relação com dados, reta ou resíduos; não se limita a “certo” ou “errado”.
- [ ] Ao incluir o ponto atípico, a pessoa estudante é convidada a prever e explicar uma mudança antes de visualizar a comparação.
- [ ] A reta ajustada só é disponibilizada depois de registrada a tentativa manual da pessoa estudante.

## Conteúdo matemático

- [ ] As únicas fórmulas centrais apresentadas são `ŷ = a + bx`, `eᵢ = yᵢ − ŷᵢ` e `MSE = (1/n) Σ(yᵢ − ŷᵢ)²`.
- [ ] Cada fórmula define todos os seus símbolos em linguagem compreensível para o público previsto.
- [ ] As unidades estão documentadas: `x` em g; `y`, `ŷ`, `a` e `eᵢ` em cm; `b` em cm/g; MSE em cm².
- [ ] A fórmula de previsão aponta para a altura da reta no gráfico; a de resíduo, para a diferença vertical; e a de MSE, para o conjunto dos desvios ao quadrado.
- [ ] Alterar inclinação ou intercepto atualiza a previsão, os resíduos e a explicação textual correspondente.
- [ ] A expressão “reta ajustada” é definida como a reta que minimiza a soma dos resíduos ao quadrado; o material explica que, com número fixo de pontos, ela também minimiza MSE.
- [ ] O texto diferencia a associação ajustada aos dados sintéticos da explicação física da mola e não apresenta regressão como prova causal.
- [ ] Não há derivadas, álgebra matricial, inferência estatística ou demonstração de equação normal.
- [ ] O conjunto inicial contém exatamente seis observações sintéticas e um único ponto atípico inicialmente oculto; todos têm massa em g e alongamento em cm.
- [ ] A referência numérica usa `a=0,042667`, `b=0,098829`, SSE `0,055082` e MSE `0,009180` no conjunto-base, dentro de tolerância interna de `0,000001`.
- [ ] Com P07, a referência usa `a=1,282903`, `b=0,085540` e MSE `3,657138`, dentro da mesma tolerância.
- [ ] Cálculos internos não usam valores previamente arredondados; a exibição aplica a regra uniforme de três casas para `a`, `b`, `ŷ`, `eᵢ`, SSE e MSE.

## Interação

- [ ] O controle de inclinação modifica visivelmente a inclinação da reta e explica o efeito nas previsões.
- [ ] O controle de intercepto desloca visivelmente a reta e explica o efeito nas previsões.
- [ ] Mostrar/ocultar resíduos altera segmentos ou valores equivalentes e explica a diferença entre `y` e `ŷ`.
- [ ] Adicionar/remover o ponto atípico altera o conjunto de dados e leva a uma pergunta sobre MSE.
- [ ] Mostrar a reta ajustada permite comparação explícita com a reta manual, sem apresentar o ajuste como única resposta aceitável.
- [ ] Em T02, somente inclinação, intercepto e reinício são exibidos; resíduos, reta ajustada e ponto atípico são liberados apenas nas etapas previstas.
- [ ] Reiniciar restaura dados e controles iniciais sem apagar uma justificativa sem aviso prévio.
- [ ] Em qualquer erro recuperável, previsões, justificativas e sínteses já digitadas na sessão permanecem visíveis, sem pressupor armazenamento persistente.
- [ ] Não há taxa de aprendizagem, épocas, visualização 3D ou múltiplas métricas.
- [ ] Os controles usam `a` de `-0,5` a `1,0` em passos de `0,1` e `b` de `0,04` a `0,14` em passos de `0,01`; botões respeitam os limites e recalculam previsões, resíduos, SSE e MSE.
- [ ] O eixo horizontal vai de `0` a `70 g` e o vertical de `-0,5` a `10,0 cm`; nenhum valor permitido dos controles oculta os dados do cenário.
- [ ] Casos numéricos usam tolerância interna de `0,000001` e tolerância exibida de `0,0005`.

## Acessibilidade

- [ ] Todos os controles, campos e ações são alcançáveis e operáveis apenas por teclado, com ordem de foco lógica.
- [ ] O foco visível atende a todos os controles interativos.
- [ ] Cada controle possui rótulo textual, instrução de uso e valor/estado atual quando aplicável.
- [ ] O gráfico fornece descrição textual atualizada após cada alteração relevante.
- [ ] Uma tabela alternativa apresenta os mesmos dados necessários para interpretar pontos, previsões e resíduos.
- [ ] Informações não dependem somente de cor: retas, ponto atípico, seleção e resíduos têm rótulo, padrão, símbolo ou texto equivalente.
- [ ] Feedback e mensagens de erro usam linguagem explicativa e não apenas cor ou correção binária.
- [ ] Existe modo de redução de movimento que elimina transições não essenciais.

## Responsividade

- [ ] Em largura de celular, gráfico, descrição, tabela, atividade e controles aparecem em uma única coluna sem rolagem horizontal.
- [ ] No celular, os controles mantêm rótulos completos e área de toque adequada.
- [ ] A tabela alternativa continua acessível sem exigir o gráfico visual.

## Autoria e clean room

- [ ] O texto do módulo, o cenário da mola, os dados sintéticos e os wireframes foram elaborados para este projeto.
- [ ] Não há reprodução de nome, logotipo, textos, exemplos, paleta, ilustrações, capturas, código ou estrutura visual distintiva da plataforma de referência.
- [ ] A avaliação de qualidade verifica atendimento aos objetivos próprios; não mede paridade visual ou funcional com a referência.
- [ ] O material não declara que regressão linear, tecnologia ou desenho de pesquisa estejam definitivamente aprovados.
- [ ] Nenhum código, componente executável, framework, dependência, banco de dados, autenticação ou backend foi criado nesta etapa.
