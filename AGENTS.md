# AGENTS.md — Instruções para assistentes de IA

Este arquivo orienta qualquer assistente de IA ou colaborador que trabalhe neste diretório.

## 1. Contexto obrigatório

Antes de propor, planejar ou implementar qualquer funcionalidade, leia:

1. `README.md`;
2. `docs/PROJECT_CONTEXT.md`;
3. `docs/DECISIONS.md`;
4. `PROJECT_STRUCTURE.md`;
5. `00_gestao/requisitos_profcomp/README.md`;
6. `09_orquestracao_ia/README.md`;
7. `09_orquestracao_ia/routing.config.yaml`;
8. `project.config.yaml`.

O projeto será apresentado na **pré-defesa do mestrado profissional ProfComp de Luiz Gabriel**. O orientador atual é o **professor Marcos Braga**. Trata-se de um trabalho ligado à educação e à docência.

## 2. Propósito do produto

Construir uma plataforma própria para o ensino de *machine learning* a estudantes do Ensino Médio, especialmente iniciantes. A plataforma deve favorecer compreensão conceitual e matemática por meio de visualizações, experimentos e explicações graduais, com linguagem e profundidade adequadas à Educação Básica.

Ela é inspirada na plataforma NEURON:

<https://kw1fpt-ahmet-duyar.shinyapps.io/Neuron/>

A inspiração não autoriza copiar código, textos, identidade visual ou materiais protegidos. Use-a como referência de experiência pedagógica e interação.

## 3. Princípios obrigatórios

- Priorizar aprendizagem e clareza, não quantidade de funcionalidades.
- Escrever para iniciantes sem eliminar o rigor matemático.
- Apresentar a matemática em camadas: intuição, representação visual, fórmula e interpretação.
- Relacionar cada controle interativo a uma consequência visível e explicada.
- Evitar que a experiência se limite a apertar botões ou executar código pronto.
- Usar português brasileiro na interface e na documentação destinada aos estudantes.
- Projetar com acessibilidade, responsividade e legibilidade.
- Manter o escopo reduzido: somente alguns modelos serão selecionados.
- Não declarar um modelo, tecnologia ou método de pesquisa como definitivo sem registrar a decisão em `docs/DECISIONS.md`.

## 4. Restrições atuais

- A pilha tecnológica ainda não foi escolhida.
- A lista final de modelos ainda não foi aprovada.
- O desenho da pesquisa e os instrumentos de avaliação ainda não foram definidos.
- Não invente dados institucionais, resultados de aprendizagem, validações ou decisões do orientador.
- Diferencie claramente fatos confirmados, hipóteses e sugestões.

## 5. Ao realizar alterações

- Preserve o contexto acadêmico descrito nos documentos.
- Atualize `docs/DECISIONS.md` quando uma decisão for confirmada.
- Atualize `project.config.yaml` quando metadados centrais mudarem.
- Mantenha o `README.md` coerente com o estado real do projeto.
- Documente pressupostos e pendências relevantes.
- Não adicione dependências ou serviços externos sem justificar sua função pedagógica ou técnica.
- Nunca inclua dados identificáveis de participantes no código, em documentação pública ou em repositórios abertos.

## 6. Orquestração econômica obrigatória

- O agente principal atua como supervisor e controla escopo, arquitetura, síntese e validação.
- Tarefas simples, delimitadas e verificáveis podem ser delegadas ao executor econômico definido em `09_orquestracao_ia/`.
- Ações determinísticas de um único passo devem ser executadas diretamente; não abra outra sessão quando a delegação gastar mais tokens que a ação.
- Ao delegar, use contexto mínimo e não encaminhe o histórico completo.
- No ambiente Codex atual, prefira `gpt-6-luna` com esforço `low` para execução econômica e `fork_turns: none`.
- Expansões não essenciais devem ser apenas sugeridas. Execute trabalho adicional somente para corrigir erro material, resolver bloqueio, atender segurança/ética ou tratar incompatibilidade acadêmica relevante.
- O supervisor deve validar o resultado do executor antes de incorporá-lo ao projeto.

## 7. Critério de qualidade

Uma funcionalidade é relevante quando ajuda o estudante a responder pelo menos uma destas perguntas:

- O que este modelo tenta aprender?
- Qual matemática sustenta seu funcionamento?
- O que muda quando um parâmetro é alterado?
- Como essa mudança aparece no gráfico ou na decisão do modelo?
- Em quais situações o modelo funciona bem ou apresenta limitações?
