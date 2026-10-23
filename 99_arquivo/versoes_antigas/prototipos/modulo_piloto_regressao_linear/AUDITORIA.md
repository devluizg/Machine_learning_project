# Auditoria pedagógica e matemática do módulo-piloto

## Resumo executivo

A auditoria encontrou zero problemas P0, sete P1 e três P2. Os P1 foram corrigidos: a terminologia do MSE ficou precisa, a melhor reta passou a ter critério definido, unidades e limites físicos foram explicitados, e a liberação de controles foi organizada por etapa. O módulo permanece provisório e depende de dados sintéticos, faixas de controle e validação didática/física antes de virar protótipo navegável.

## Achados

| ID | Prioridade | Arquivo | Problema | Correção |
| --- | --- | --- | --- | --- |
| A01 | P1 | MAPA, FLUXO, WIREFRAME, CRITÉRIOS | “Erro total” era impreciso para MSE. | Substituído por “média dos erros quadráticos (MSE)” e explicado o critério. |
| A02 | P1 | MAPA, FLUXO, CRITÉRIOS | A “melhor reta” não tinha critério formal nem relação entre MSE e soma dos quadrados. | Definida como minimizadora da soma dos resíduos ao quadrado; equivalência com MSE para `n` fixo registrada. |
| A03 | P1 | MAPA, FLUXO, CRITÉRIOS | Símbolos tinham definição parcial, sem unidades. | Documentadas unidades de `x`, `y`, `ŷ`, `a`, `b`, `eᵢ` e MSE. |
| A04 | P1 | WIREFRAME, FLUXO, CRITÉRIOS | Wireframe expunha todos os controles cedo, contrariando a progressão do fluxo. | T02 mostra apenas inclinação, intercepto e reinício; demais controles aparecem em etapas posteriores. |
| A05 | P1 | FLUXO, WIREFRAME, CRITÉRIOS | A previsão do ponto atípico não bloqueava a revelação do resultado. | A previsão passa a anteceder ponto, comparação e referência ajustada. |
| A06 | P1 | MAPA, FLUXO, CRITÉRIOS, PENDÊNCIAS | Relação entre ajuste estatístico e cenário físico estava pouco delimitada. | Diferenciada associação nos dados da explicação física; validação do cenário ficou pendente. |
| A07 | P1 | FLUXO, CRITÉRIOS | Preservação de respostas sugeria armazenamento indefinido. | Especificada preservação somente na sessão e em falhas recuperáveis, sem decisão tecnológica. |
| A08 | P2 | MAPA, FLUXO, CRITÉRIOS | Dados e faixas ainda não permitem conferir o efeito quantitativo do ponto atípico. | Registrado como pendência; não foram inventados valores. |
| A09 | P2 | WIREFRAME, FLUXO | O momento de abertura da tabela alternativa pode ser detalhado na navegação futura. | Mantido como acesso explícito; detalhar em protótipo navegável. |
| A10 | P2 | CRITÉRIOS | O comportamento de reinício para respostas preenchidas pode receber regra mais detalhada. | Mantido o aviso obrigatório; definir o comportamento final junto à avaliação de uso. |

## Correções aplicadas

- Ajustada a redação do terceiro objetivo por precisão matemática, sem mudar sua intenção: reduzir MSE, e não um “erro total” indefinido.
- Acrescentadas unidades, sinal do resíduo e equivalência entre minimizar MSE e a soma de quadrados com quantidade fixa de pontos.
- Explicitada a ordem: tentativa manual → reta ajustada; previsão sobre ponto atípico → revelação e comparação.
- Separados os controles necessários de T02 dos controles de resíduos, comparação e ponto atípico.
- Esclarecido que regressão ajusta uma associação observada e não comprova causalidade nem substitui explicação física.

## Recomendações P2 não aplicadas

- Definir valores sintéticos, ponto atípico e faixas dos controles antes do protótipo navegável.
- Validar com estudantes a melhor forma de abrir a tabela alternativa e detalhar o reinício após preenchimento.
- Verificar, com o cenário numérico definido, se quantidade de texto e cartões preserva a carga cognitiva adequada.

## Checklist final

- [x] Três objetivos preservados e associados a previsão, resíduos e MSE.
- [x] Há evidências observáveis e critérios verificáveis para os objetivos.
- [x] Fluxo preserva prever → alterar → observar → explicar.
- [x] Reta ajustada sucede a tentativa manual; ponto atípico sucede a previsão.
- [x] Fórmulas, sinais, unidades e critério de ajuste estão coerentes.
- [x] Controles são progressivos e têm finalidade pedagógica explícita.
- [x] Gráfico, descrição e tabela alternativa foram previstos; erros recuperáveis preservam respostas da sessão.
- [x] Não foram adicionados código, tecnologia ou elementos distintivos de referência externa.

## Veredito

**Aprovado com pendências.** O material pode avançar para um protótipo navegável somente após definir e validar os dados sintéticos, as faixas dos controles e a adequação física/pedagógica do cenário da mola.
