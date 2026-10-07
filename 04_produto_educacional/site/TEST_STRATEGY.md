# Estratégia de testes

## Ferramentas previstas

Na implementação, usar Vitest para domínio e componentes, React Testing Library para interações e semântica, Playwright para fluxo/responsividade e axe-core para verificação automatizada básica. Esta etapa não instala dependências nem escreve testes.

## Níveis e contratos

| Nível | Automatizar | Verificação manual |
| --- | --- | --- |
| Domínio matemático | `prever`, resíduos, SSE, MSE, OLS, arredondamento e comparações; casos N01–N10 com tolerâncias `0,000001`/`0,0005`. | Conferência independente das fórmulas e unidades apresentadas. |
| Componentes | Limites e passos dos controles, tabela/descrição derivadas, seleção, liberações de T05, reinício preservável e erro recuperável. | Leitura pedagógica dos feedbacks. |
| Fluxo | T01–T06, registro de previsão antes de P07, referência só após reta manual, remoção de P07 e síntese. | Compreensão da sequência por estudantes representativos, posteriormente. |
| Acessibilidade | Nome/valor dos controles, foco, região de status, regras axe e redução de movimento. | Navegação só por teclado, leitor de tela e clareza da tabela/SVG. |
| Visual/responsivo | Eixos, P07, referência `a>1,0`, e layout de uma coluna em viewport móvel. | Legibilidade, contraste e equivalência entre gráfico, tabela e descrição. |

## Casos obrigatórios

- Executar N01–N10 de `CASOS_DE_TESTE_NUMERICOS.md` sem reutilizar valores formatados em cálculos.
- Confirmar que OLS base (`0,042667`, `0,098829`) tem MSE menor ou igual às retas manuais testadas e que P07 altera OLS para (`1,282903`, `0,085540`).
- Confirmar que a reta ajustada não altera sliders nem é limitada por `aManual ≤ 1,0`; deve aparecer completa no eixo de `-0,5` a `10 cm`.
- Confirmar seleção de resíduo positivo e negativo, descrição coerente e tabela completa se o SVG falhar.
- Confirmar foco, teclado, contraste, rótulos, redução de movimento e ausência de dependência exclusiva de cor.

## Critério de aprovação da fatia

Todos os testes numéricos e de fluxo passam; não há falha crítica de teclado ou alternativa textual; os dados exibidos por SVG, tabela e descrição vêm da mesma série calculada; nenhum estado libera referência ou P07 antes da ação prevista. Avaliação pedagógica com público e validações humanas continuam fora deste critério técnico.
