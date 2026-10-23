# Produto educacional: site interativo

O produto educacional será um site para ensino visual e interativo de conceitos selecionados de *machine learning*.

## Componentes do produto

- `site/`: código-fonte e documentação técnica do sistema;
- `design_pedagogico/`: acesso ao planejamento pedagógico atual, centralizado em `03_pesquisa/metodologia/`;
- `conteudo_dos_modulos/`: textos, fórmulas, exemplos, atividades e feedbacks;
- `prototipos/`: registro de localização dos estudos históricos; o protótipo em desenvolvimento está em `site/`;
- `identidade_visual/`: cores, tipografia, ícones e padrões visuais;
- `acessibilidade/`: requisitos e verificações de acessibilidade;
- `testes/`: testes técnicos, pedagógicos e de usabilidade;
- `avaliacao_do_produto/`: instrumentos e resultados específicos do produto;
- `manual_de_uso/`: guia para estudantes e docentes;
- `evidencias_de_desenvolvimento/`: registros de versões, decisões e ciclos de melhoria.

## Estrutura pedagógica pretendida para cada modelo

```text
contexto → intuição → exploração visual → matemática guiada
        → atividade de interpretação → síntese e limitações
```

## Decisões ainda pendentes

- Nome público da plataforma;
- público institucionalmente validado;
- modelos de *machine learning* incluídos;
- cenários sintéticos definitivos e textos de cada módulo;
- requisitos de hospedagem e funcionamento offline;
- avaliação formal de acessibilidade, responsividade e uso em sala.

O protótipo utiliza Vite, React e TypeScript, com execução local no navegador e sem coleta de respostas. Ele será empregado como recurso de mediação no ensino introdutório de Computação; os instrumentos de pesquisa permanecem externos ao site. A auditoria de aderência à sequência está em `avaliacao_do_produto/AUDITORIA_PEDAGOGICA_SITE_E_SEQUENCIA.md`.
