# Avaliação da replica-skill para o produto educacional

## Veredito

**Útil com adaptações.** A replica-skill pode reduzir o trabalho de observação, organização e verificação de fluxos públicos do NEURON, desde que seja usada como método de análise *clean room*, e não como roteiro para produzir um clone ou decidir a arquitetura do produto.

## Partes a utilizar

| Metodologia | Uso adaptado no projeto |
| --- | --- |
| `replica-recon` | Inventariar telas, fluxos, controles, estados e evidências públicas; separar observação de inferência; registrar funcionalidades fora de escopo. |
| `replica-architect` | Somente depois de decisão registrada: converter o recorte pedagógico aprovado em módulos, requisitos de interação, acessibilidade e uma sequência de implementação. |
| `replica-design` | Descrever papéis visuais e componentes genéricos; definir tokens e textos próprios, com contraste e legibilidade. |
| `replica-test` | Derivar testes de uso, acessibilidade e compreensão: o estudante deve conseguir prever, alterar, observar e explicar. |
| `replica-diff` | Manter uma matriz de cobertura para o escopo **próprio**: o que foi observado, adaptado, deliberadamente excluído e validado. |

## Partes a ignorar

- A meta de “clonar” ou atingir paridade visual/funcional com a referência.
- Escolhas padrão de pilha, banco de dados, APIs, autenticação, pagamentos ou SaaS.
- Comparação pixel a pixel de capturas, que induz aproximação da aparência alheia.
- Etapas de marca, lançamento e deploy desta skill nesta fase.
- Modelo de dados inferido da referência como especificação do nosso produto.

## Adaptações necessárias para um produto educacional

1. Substituir “feature parity” por uma matriz `objetivo de aprendizagem → interação → evidência visual → explicação/atividade → teste`.
2. Tratar cada tela observada como evidência de uma **categoria** de experiência, nunca como layout, texto, exemplo ou ativo a reproduzir.
3. Construir cada módulo em camadas: situação-problema, intuição, gráfico, fórmula interpretada, experimento, previsão e síntese de limites.
4. Manter interface e documentação em português brasileiro, com alternativas textuais, teclado, contraste, responsividade e atenção a gráficos não visuais.
5. Selecionar poucos modelos somente após validação acadêmica; a inspeção não aprova regressão linear, k-NN ou k-means como escopo final.

## Riscos

| Risco | Mitigação |
| --- | --- |
| Complexidade | Fixar um módulo-piloto e uma fatia pedagógica antes de qualquer arquitetura técnica. |
| Cópia | Não reutilizar nome, textos, exemplos, paleta, ilustrações, capturas, ícones, estrutura visual distintiva ou código do NEURON. Manter fontes e justificativas no levantamento. |
| Desvio pedagógico | Cada controle deve produzir consequência visível e ser acompanhado de pergunta ou explicação; conteúdo avançado só entra com andaime e justificativa. |
| Falsa equivalência | A cobertura deve medir atendimento aos objetivos próprios, não semelhança com a plataforma de referência. |

## Recomendação do próximo passo

Executar uma recon adaptada de **um único módulo candidato**, convertendo o inventário desta análise em um mapa pedagógico autoral de baixa fidelidade. Antes de escolher tecnologia, submeter o recorte de modelo, conhecimentos prévios e objetivo de aprendizagem ao orientador.

## Prompt curto para a próxima etapa

> Com base em `recon_neuron.md` e `features.csv`, proponha um mapa pedagógico autoral de baixa fidelidade para um único módulo candidato, em português brasileiro. Relacione objetivo, intuição, visualização, fórmula, controle, atividade de previsão, feedback, acessibilidade e itens fora de escopo. Não escolha tecnologia e não reproduza elementos distintivos do NEURON.

## Base da avaliação

- [Documentação pública da replica-skill](https://github.com/Jakeschincariol/replica-skill), consultada em 03 out. 2026.
- [NEURON — interface pública](https://kw1fpt-ahmet-duyar.shinyapps.io/Neuron/), observada em 03 out. 2026.

Esta avaliação é metodológica; não confirma tecnologias, modelos finais, desenho de pesquisa ou decisões do orientador.
