# Wireframe textual de baixa fidelidade

## Princípios de composição

- Identidade visual neutra e original; cores, tipografia, ícones e nome permanecem indefinidos.
- A atividade e o gráfico recebem destaque; a explicação fica próxima da consequência visual.
- O conteúdo usa uma única tarefa por etapa, sem painel técnico ou métrica concorrente.
- Controles têm rótulos textuais, equivalentes por teclado e são liberados progressivamente.

## Desktop — T02: reta manual

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ Módulo-piloto · Tendência nos dados de uma mola      Etapa 2 de 6           │
├─────────────────────────────────────────────────────────────────────────────┤
│ Pergunta da etapa: Como a sua reta representa o conjunto de pontos?        │
├───────────────────────────────────────┬─────────────────────────────────────┤
│ GRÁFICO PRINCIPAL                     │ EXPLICAÇÃO DA ETAPA                  │
│ massa (g) × alongamento (cm)          │ Ajuste a reta para representar       │
│ · pontos sintéticos                   │ a tendência do conjunto.             │
│ · reta manual                         │                                     │
│ [Descrição textual atualizada]        │ CONTROLES DESTA ETAPA                 │
│ [Abrir tabela alternativa]            │ Inclinação [ − | valor | + ] cm/g     │
│                                       │ Intercepto [ − | valor | + ] cm       │
│                                       │ [Reiniciar experimento]               │
├───────────────────────────────────────┴─────────────────────────────────────┤
│ [Voltar]                                      [Avançar para os resíduos]    │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Hierarquia visual:** pergunta da etapa → gráfico → explicação contextual → controles da etapa → descrição/tabela → navegação. A tabela alternativa está sempre acessível nos estágios que usam gráfico, sem ficar aberta obrigatoriamente.

## Desktop — T04: matemática guiada

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ Matemática guiada · Da reta ao MSE                                           │
├───────────────────────┬─────────────────────────────────────────────────────┤
│ PROGRESSO             │ CARTÃO ATUAL                                        │
│ ● Previsão            │ ŷ = a + bx (cm)                                    │
│ ○ Resíduo             │ Símbolos: ŷ, a, b, x e suas unidades                │
│ ○ MSE                 │ No gráfico: a altura da reta para uma massa x.      │
│                       │ Ao mover a reta: a previsão muda.                   │
│                       │ Por que importa: permite comparar previsto e real.  │
│                       │ [Ver no ponto selecionado] [Próximo cartão]         │
├───────────────────────┴─────────────────────────────────────────────────────┤
│ [Abrir tabela alternativa] · resumo textual sempre disponível                │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Celular — T05: previsão e ponto atípico

```text
┌───────────────────────────────┐
│ Tendência na mola · 5/6        │
├───────────────────────────────┤
│ Pergunta da etapa              │
│ O que pode mudar com uma       │
│ medida muito fora da tendência?│
├───────────────────────────────┤
│ GRÁFICO PRINCIPAL              │
│ pontos + reta manual           │
│ resultado ainda oculto          │
│ [Descrição textual]            │
├───────────────────────────────┤
│ ATIVIDADE                      │
│ [campo de previsão obrigatório]│
│ [Registrar previsão]           │
├───────────────────────────────┤
│ APÓS REGISTRAR A PREVISÃO      │
│ [Mostrar ponto atípico]         │
│ [Mostrar reta ajustada]         │
│ [Abrir tabela alternativa]      │
│ [Reiniciar experimento]         │
├───────────────────────────────┤
│ [Voltar]       [Avançar]       │
└───────────────────────────────┘
```

**Hierarquia visual no celular:** pergunta → gráfico → atividade de previsão → controles liberados pela etapa → descrição/tabela → navegação. Não há área lateral; todos os blocos ficam em coluna, com alvos de toque adequados e sem exigir rolagem horizontal.

## Estados visuais transversais

- **Foco:** contorno visível e persistente no controle ativo.
- **Carregando:** texto de estado e representação estática; não usar animação obrigatória.
- **Erro:** informar o problema em texto, preservar respostas já digitadas na sessão e disponibilizar tabela/explicação quando o gráfico falhar.
- **Redução de movimento:** transições de reta, resíduos e ponto atípico passam a atualização instantânea.
