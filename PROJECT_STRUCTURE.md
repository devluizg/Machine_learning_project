# Estrutura do projeto

Este projeto reúne duas frentes inseparáveis:

1. **Pesquisa acadêmica:** qualificação, fundamentação teórica, metodologia, coleta, análise e dissertação.
2. **Produto educacional:** concepção, desenvolvimento, aplicação e avaliação do site interativo.

## Mapa das pastas

```text
Machine_learning_project/
├── 00_gestao/                  # Prazos, reuniões, requisitos e modelos de trabalho
├── 01_qualificacao/            # Texto e apresentação do exame de qualificação
├── 02_referencial_teorico/     # PDFs, fichamentos, buscas e bibliografia
├── 03_pesquisa/                # Problema, método, ética, instrumentos e dados
├── 04_produto_educacional/     # Site, conteúdo, design, testes e avaliação
├── 05_dissertacao/             # Texto final, elementos gráficos e defesa
├── 06_publicacoes/             # Artigos, eventos e pôsteres
├── 07_entrega_e_deposito/      # Produto final, licenças e depósitos
├── 08_normas_e_modelos/        # Documentos oficiais do PROFCOMP, UFPA e CAPES
├── 09_orquestracao_ia/         # Roteamento econômico entre supervisor e executores
├── 99_arquivo/                 # Materiais inativos ou substituídos
└── docs/                       # Contexto e decisões gerais do projeto
```

## Função de cada área

### `00_gestao`

Armazena atas das reuniões com o orientador, cronograma, exigências institucionais e modelos reutilizáveis. Toda reunião relevante deve gerar uma ata curta com data, decisões, pendências e próximo encontro.

### `01_qualificacao`

Concentra o projeto de qualificação. O texto em elaboração permanece em `texto/`; apenas versões efetivamente enviadas ao orientador ou à banca entram em `versoes_submetidas/`. Comentários recebidos ficam em `feedback_banca/`.

### `02_referencial_teorico`

Organiza a revisão de literatura por eixo temático. PDFs baixados ficam em `pdfs/`, mas cada referência realmente utilizada deve também possuir ficha em `fichamentos/` e entrada no gerenciador bibliográfico ou arquivo de bibliografia.

### `03_pesquisa`

Guarda o desenho científico: problema, perguntas, objetivos, metodologia, instrumentos e documentação ética. Dados identificáveis ou sensíveis devem ficar em `dados_brutos_restritos/`, nunca dentro do código do site nem em repositório público.

### `04_produto_educacional`

É a área do produto. O código-fonte ficará em `site/` quando a pilha tecnológica for escolhida. Os conteúdos dos modelos, o desenho pedagógico e a avaliação permanecem separados do código para facilitar revisão acadêmica.

### `05_dissertacao`

Recebe a redação final do Trabalho de Conclusão de Mestrado, seus elementos gráficos, apêndices, anexos e apresentação de defesa. Não confundir com o projeto de qualificação.

### `06_publicacoes`

Reúne textos derivados da pesquisa destinados a periódicos, conferências, seminários e pôsteres.

### `07_entrega_e_deposito`

Contém as versões finais do produto educacional, documentação administrativa, licenças e comprovantes de depósito ou publicação.

### `08_normas_e_modelos`

Guarda cópias de regimentos, normas, formulários e modelos oficiais. Sempre registre a fonte e a data de acesso, pois esses documentos podem mudar.

### `09_orquestracao_ia`

Define quando o modelo supervisor deve executar diretamente, delegar a um modelo econômico ou manter uma tarefa complexa. Contém configuração de roteamento, prompts e pacote-padrão de delegação.

### `99_arquivo`

Recebe materiais superados que ainda precisam ser preservados. Use nomes com data e motivo do arquivamento.

## Convenções de nomes

- PDF de referência: `SOBRENOME_Ano_TituloCurto.pdf`
- Fichamento: `SOBRENOME_Ano_TituloCurto.md`
- Ata: `AAAA-MM-DD_reuniao_orientacao.md`
- Versão submetida: `AAAA-MM-DD_qualificacao_vNN.pdf`
- Instrumento: `instrumento_nome_vNN.md`
- Evite arquivos chamados `final`, `final2` ou `agora_final`.

## Fluxo geral

```text
normas + problema profissional
            ↓
 revisão teórica e desenho da pesquisa
            ↓
     projeto de qualificação
            ↓
 protótipo do site e instrumentos
            ↓
 aplicação, avaliação e análise
            ↓
 dissertação + produto educacional
            ↓
       defesa e depósito
```
