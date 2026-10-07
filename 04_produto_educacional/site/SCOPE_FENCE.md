# Cerca de escopo da arquitetura

> Atualização de 03/10/2026: a cerca abaixo descrevia a primeira fatia de regressão linear. Luiz ampliou explicitamente o protótipo para cinco modelos. A expansão mantém os limites técnicos de execução local, dados sintéticos, sem serviços externos e sem coleta de respostas; não define a lista final do produto acadêmico.

## Incluído na versão simplificada

- Cinco experimentos locais, um para cada modelo escolhido para o protótipo. As etapas completas T01–T06 da regressão linear continuam planejadas, não concluídas.
- Dados sintéticos locais, cálculos puros, estado de sessão, SVG, textos alternativos, tabela na regressão linear, feedback determinístico e testes de domínio.
- Vite + React + TypeScript e hospedagem futura como site estático.

## Não incluído — não agora

- Página inicial definitiva e catálogo além dos cinco experimentos simplificados autorizados.
- Contas, autenticação, banco, backend, API, webhooks, pagamentos, painel administrativo ou microserviços.
- Nuvem, acompanhamento docente, exportação de resultados, analytics ou transmissão de respostas.
- Internacionalização, motor 3D externo/WebGL, Canvas para gráficos didáticos, deploy público e identidade visual final. As vistas 3D matemáticas são projeções em SVG; Canvas é usado somente no fundo decorativo solicitado, sem nova dependência.

## Hipóteses

- O navegador moderno suporta SVG, JavaScript e recursos de acessibilidade padrão.
- O uso é individual, local e sem retenção de respostas entre sessões.
- Os exemplos sintéticos e os eixos são provisórios e precisam de validação didática antes de uso com estudantes.

## Pendências humanas

- Validação com professor Marcos Braga, validação didática e física do cenário.
- Série, duração, instrumento de avaliação, critérios institucionais de hospedagem, identidade visual e lista final de modelos.

## Gatilhos que impedem expansão automática

Não adicionar dependência, serviço, sexto modelo, coleta de dados ou persistência sem decisão registrada. Pausar e reavaliar a arquitetura se validação humana exigir acessibilidade não atendida por SVG + alternativas textuais, armazenamento de respostas ou funcionamento offline específico.
