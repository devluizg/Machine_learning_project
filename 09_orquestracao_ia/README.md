# Arquitetura econômica de IA

## Objetivo

Usar um modelo avançado como supervisor do projeto e modelos mais econômicos como executores de tarefas delimitadas, reduzindo tokens sem perder coerência acadêmica, segurança ou qualidade.

O padrão adotado é **Supervisor–Executor com roteamento adaptativo**.

```text
pedido de Luiz
      ↓
supervisor avançado: entende, delimita e classifica
      ↓
 ┌───────────────┬────────────────────┬──────────────────────┐
 │ ação direta   │ executor econômico │ supervisor avançado  │
 │ 1 passo       │ tarefa delimitada  │ decisão/síntese      │
 └───────────────┴────────────────────┴──────────────────────┘
      ↓                    ↓                     ↓
 verificação local   retorno estruturado   integração/validação
      └────────────────────┴─────────────────────┘
                           ↓
                 resposta final compacta
```

## Papéis

### Supervisor avançado

Responsável por:

- compreender a intenção de Luiz;
- decidir o que está e o que não está no escopo;
- decompor tarefas quando isso gerar economia real;
- tomar decisões de arquitetura, pesquisa e metodologia;
- detectar contradições e riscos importantes;
- revisar resultados de executores;
- integrar apenas o necessário na resposta final.

Configuração recomendada no ambiente atual:

- modelo: modelo avançado selecionado pelo usuário; na ausência de escolha, `gpt-6.1-sol`;
- esforço: `high` para arquitetura e decisões acadêmicas; `medium` para planejamento rotineiro.

### Executor econômico

Responsável por tarefas objetivas e verificáveis:

- buscas focadas e coleta de poucas fontes;
- inventário de arquivos;
- extração e classificação de informações;
- alterações mecânicas em arquivos;
- criação de estruturas previamente especificadas;
- execução de testes e comandos;
- pequenas implementações com critério de aceite claro;
- formatação, conversão e revisão superficial.

Configuração recomendada no ambiente atual:

- modelo: `gpt-6-luna`;
- esforço: `low` para pesquisa e operações mecânicas;
- esforço: `medium` somente para pequenas tarefas de código;
- contexto: `fork_turns: none`, recebendo apenas um pacote mínimo de tarefa.

Os nomes dos modelos são configuração operacional, não requisito permanente. Devem ser atualizados se a disponibilidade ou o custo relativo mudar.

## Regra principal de economia

Delegar apenas quando:

```text
custo estimado da execução pelo supervisor
    > custo de preparar o pacote + executor + validação
```

Uma tarefa de um único comando ou uma edição óbvia deve ser executada diretamente pelo supervisor. Criar outro agente para esse caso desperdiça contexto e tokens.

## Matriz de roteamento

| Tipo de tarefa | Rota | Exemplo |
|---|---|---|
| Um passo determinístico | Direta | Criar uma pasta já especificada |
| Busca curta e bem delimitada | Executor econômico | Encontrar até 5 artigos por critérios definidos |
| Trabalho mecânico em vários arquivos | Executor econômico | Trocar um termo e verificar ocorrências |
| Teste ou inspeção repetitiva | Executor econômico | Rodar testes e resumir falhas |
| Pequena implementação especificada | Executor econômico | Criar um componente com contrato pronto |
| Definição de arquitetura | Supervisor | Escolher a estrutura tecnológica do site |
| Síntese de literatura | Supervisor após coleta barata | Interpretar evidências e construir argumento |
| Decisão metodológica ou ética | Supervisor | Definir desenho da aplicação com estudantes |
| Pedido ambíguo com impacto amplo | Supervisor | Delimitar o que deve ser construído |

## Disciplina de escopo

O supervisor deve executar o pedido explícito e somente ampliar o trabalho quando a informação adicional:

1. impedir um erro material;
2. revelar incompatibilidade acadêmica ou normativa relevante;
3. for necessária para segurança, ética ou proteção de dados;
4. desbloquear a execução solicitada;
5. tiver benefício claro maior que o custo de investigação.

Melhorias opcionais devem ser registradas como sugestão curta, sem serem executadas automaticamente.

## Processo operacional

1. **Interpretar:** resumir internamente o resultado pedido em uma frase.
2. **Delimitar:** listar entregável, restrições e critério de conclusão.
3. **Classificar:** escolher execução direta, executor econômico ou supervisor.
4. **Delegar minimamente:** enviar somente contexto necessário, caminhos exatos e formato de saída.
5. **Executar:** o trabalhador não amplia o escopo nem lê o projeto inteiro.
6. **Validar proporcionalmente:** uma verificação suficiente, sem repetir a mesma checagem.
7. **Integrar:** remover repetições e entregar apenas resultado, decisões e pendências reais.

## Política para pesquisas na internet

- Formular uma pergunta de busca precisa antes de abrir fontes.
- Priorizar fontes primárias ou institucionais.
- Limitar normalmente a 3–5 fontes realmente úteis.
- Interromper quando houver evidência suficiente para responder.
- Não produzir revisão ampla quando o pedido exige apenas um dado.
- O executor retorna fatos, URLs, data e incertezas; o supervisor faz a síntese.

## Política para arquivos do projeto

- Informar caminhos exatos ao executor.
- Preferir trechos necessários a arquivos completos.
- Usar busca textual antes de abrir muitos documentos.
- Não reler documentação estável a cada subtarefa, salvo se obrigatória.
- Não duplicar conteúdo entre arquivos sem necessidade.
- Validar alterações com uma busca focalizada ou teste específico.

## Escalonamento

O executor econômico deve devolver a tarefa ao supervisor quando:

- houver ambiguidade que altere o resultado;
- forem encontradas fontes contraditórias;
- a mudança envolver metodologia, ética, arquitetura ou escopo acadêmico;
- o critério de aceite não puder ser verificado;
- ocorrer o mesmo bloqueio em duas tentativas curtas.

Não deve continuar explorando indefinidamente.

## Medidas de eficiência

Avaliar periodicamente:

- proporção de tarefas concluídas sem retrabalho;
- quantidade de delegações desnecessárias;
- tamanho médio dos pacotes enviados;
- quantidade de fontes abertas por resposta;
- número de vezes em que o supervisor refez trabalho do executor;
- qualidade final em relação ao esforço usado.

O objetivo não é minimizar tokens isoladamente. É minimizar **tokens por resultado correto e aproveitável**.

