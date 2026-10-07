# ADR-001 — Pilha da fatia vertical de regressão linear

## Contexto

A primeira fatia é uma experiência educacional local, determinística e estática, formada pelas etapas T01–T06. Ela precisa de estado de interface moderado, cálculos puros, SVG acessível, tabela equivalente, testes e possibilidade de novos módulos sem construir uma plataforma SaaS.

## Requisitos determinantes

- Executar inteiramente no navegador, sem transmitir respostas.
- Preservar separação entre domínio matemático, estado e interface.
- Representar controles, gráfico SVG, tabela, descrição textual e seis etapas progressivas.
- Permitir testes unitários, de componentes, fluxo, teclado, acessibilidade e responsividade.
- Manter hospedagem futura como arquivos estáticos e dependências mínimas.

## Opções comparadas

| Opção | Vantagens | Limitações e risco |
| --- | --- | --- |
| HTML, CSS e JavaScript sem framework | Menos dependências e saída estática direta. | Estado distribuído entre DOM e cálculos; etapas e testes de componentes exigem convenções próprias. Maior risco de acoplamento ao crescer para novos módulos. |
| Vite + React + TypeScript | Estado local explícito, componentes previsíveis, tipagem do domínio, ecossistema maduro de testes e acessibilidade; build estático simples. | Dependências de desenvolvimento maiores que JavaScript puro e exige disciplina para não introduzir estado global desnecessário. |
| Vite + Svelte + TypeScript | Componentes concisos e estado local simples. | Adequado tecnicamente, porém introduz uma convenção menos familiar para a continuidade prevista; vantagem de concisão não compensa o custo de adoção neste projeto. |

## Decisão

Adotar **Vite + React + TypeScript**, com **SVG nativo** para a visualização. Não usar D3, biblioteca de gráficos, Canvas ou 3D nesta fatia.

## Justificativa

React com estado local reduz a chance de sincronização divergente entre gráfico, tabela, anúncio textual e seis etapas. TypeScript protege contratos numéricos e unidades. SVG nativo permite elementos semânticos, foco, rótulos, estilos não cromáticos e resíduos como segmentos sem uma dependência de gráfico. Vite gera ativos estáticos e não exige backend.

## Consequências

- Dados, cálculos e feedback continuam locais; não haverá API, banco, autenticação, serviços externos ou telemetria.
- A visualização será composta de elementos SVG simples e a tabela será uma alternativa informacional completa.
- O estado ficará em um contêiner do módulo e em componentes locais; não usar Redux, contexto global para estado mutável ou outra biblioteca global.
- Ferramentas previstas, mas não instaladas nesta etapa: Vite, React, TypeScript, Vitest, React Testing Library, Playwright e axe-core.

## Riscos e mitigação

- **Complexidade prematura:** limitar a árvore ao único módulo e evitar abstrações multi-modelo.
- **Divergência visual/textual:** derivar SVG, tabela, descrição e feedback do mesmo resultado calculado.
- **Reta ajustada fora do intervalo manual:** tratá-la como referência independente, nunca como valor de controle.
- **Acessibilidade do SVG:** manter tabela e descrição completas; testar teclado e leitor de tela manualmente.

## Condições para rever

Rever esta decisão apenas se validação de acessibilidade mostrar que SVG não atende ao objetivo com a tabela alternativa, se forem aprovados módulos que justifiquem outra composição, ou se requisitos institucionais impuserem tecnologia incompatível. Isso não aprova a lista final de modelos, a tecnologia do produto completo ou qualquer backend.
