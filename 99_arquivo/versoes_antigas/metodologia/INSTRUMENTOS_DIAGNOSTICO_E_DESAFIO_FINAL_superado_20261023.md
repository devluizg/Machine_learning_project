# Instrumentos preliminares: diagnóstico inicial e desafio final

**Projeto:** Ensino introdutório de *machine learning* no Ensino Médio por meio de uma sequência didática apoiada por uma plataforma interativa  
**Status:** versão de trabalho. Requer revisão do orientador, adequação à turma e verificação ética e institucional antes de qualquer aplicação.

## 1. Princípios comuns de aplicação

Os dois instrumentos são individuais, identificados apenas por um código atribuído pelo pesquisador, por exemplo, `E01`. Eles não compõem nota escolar e não devem ser apresentados como prova. Sua função é produzir evidências sobre as explicações dos estudantes antes e depois da sequência.

O diagnóstico deve ocorrer antes do primeiro contato orientado com a plataforma e durar cerca de 15 a 20 minutos. O desafio final deve ocorrer no oitavo encontro e durar cerca de 35 a 45 minutos. Durante a realização, não haverá consulta à plataforma, à internet ou a materiais de aula. O professor poderá esclarecer o significado de uma palavra do enunciado, sem indicar qual resposta é esperada.

As questões foram organizadas para serem comparáveis em quatro dimensões: dados e finalidade da tarefa; previsão sobre uma alteração; leitura de representação; e possibilidade ou limite de uma decisão automatizada. O diagnóstico não cobra os nomes dos cinco modelos, pois os estudantes ainda não os estudaram. O desafio final solicita a mobilização desses conceitos depois da sequência.

## 2. Diagnóstico inicial

**Tempo previsto:** 15 a 20 minutos  
**Orientação ao estudante:** “Este não é um teste com nota. Responda com suas palavras. Se não souber, escreva o que você imagina.”

### Situação A

Uma escola deseja criar um sistema para estimar quanto de energia uma sala pode consumir em um dia. Para cada dia, a escola registra a temperatura, o número de pessoas na sala, o tempo de uso do ar-condicionado e o consumo de energia.

**D1.** Quais dessas informações poderiam ajudar o sistema a fazer uma estimativa? Qual seria o resultado que ele tentaria estimar?

**D2.** A tarefa da Situação A é mais parecida com:  
a) prever um valor numérico;  
b) escolher entre duas categorias;  
c) formar grupos de elementos parecidos.  
Explique brevemente sua escolha.

### Situação B

Um mapa mostra vários pontos de coleta de materiais recicláveis. Uma equipe quer organizar os pontos em grupos de locais próximos, sem definir os grupos antes.

**D3.** O que a equipe deseja fazer com os pontos? Marque uma opção e explique:  
a) prever um número;  
b) colocar cada ponto em uma categoria já definida;  
c) formar grupos a partir da proximidade.

### Situação C

Em um gráfico, cada ponto representa um dia. No eixo horizontal está a temperatura e, no eixo vertical, o consumo de energia. Em geral, os pontos mais à direita aparecem mais altos.

**D4.** Sem fazer contas, o que você espera que aconteça com a estimativa de consumo se a temperatura aumentar? Por quê?

### Situação D

Dois sistemas recebem informações parecidas, mas um deles classifica uma situação como “alerta” e o outro como “sem alerta”.

**D5.** Dê uma possível explicação para os dois sistemas produzirem respostas diferentes.

### Questão de fechamento

**D6.** Uma inteligência artificial sempre produz a melhor resposta? Explique sua opinião usando a ideia de dados, regras ou informações que ela recebe.

## 3. Desafio final individual

**Tempo previsto:** 35 a 45 minutos  
**Orientação ao estudante:** “Responda com suas palavras e use os conceitos trabalhados quando eles ajudarem sua explicação. Não basta escrever apenas o nome de um modelo.”

### Situação 1: prever consumo

Em uma sala fictícia, foi montada uma tabela com temperatura, número de pessoas, tempo de ar-condicionado e consumo de energia. Um gráfico de temperatura e consumo mostra uma tendência crescente. Um modelo de regressão linear foi usado para estimar o consumo.

**F1.** Qual é a finalidade desse modelo: prever um valor numérico, escolher uma categoria ou formar grupos? Justifique usando a situação.

**F2.** Se forem incluídos no conjunto de dados vários dias muito quentes, com alto consumo de energia, o que pode mudar na reta e nas estimativas? Explique relacionando os dados ao gráfico e à previsão.

### Situação 2: probabilidade e alerta

Um sensor fictício informa a chance de uma estufa precisar de irrigação. Em uma leitura, o modelo calcula 70%. O responsável pode definir que o alerta aparece a partir de 60% ou apenas a partir de 80%.

**F3.** O que acontece com a classificação “alerta” se o limiar mudar de 60% para 80%, mantendo a chance calculada em 70%? Diferencie, em sua explicação, probabilidade e classificação.

### Situação 3: duas formas de classificação

Uma coleção fictícia possui objetos descritos por peso e tamanho. Alguns objetos já receberam as etiquetas “leve” e “pesado”. Um novo objeto ainda não tem etiqueta.

**F4a.** Se for usado o k-NN, como a proximidade e os vizinhos já etiquetados podem ajudar a classificar o novo objeto?

**F4b.** Uma árvore de decisão usa a regra: “se o peso for menor ou igual a 500 g, classificar como leve; se for maior que 500 g, classificar como pesado”. Como a árvore classificaria um objeto de 450 g? Em que essa explicação por regra é diferente da explicação por vizinhos do k-NN?

### Situação 4: formar grupos sem rótulos

Em um mapa de bairro, há locais fictícios de coleta. Não existem categorias dadas previamente. O objetivo é reunir locais próximos para planejar rotas.

**F5.** Por que o k-means pode ser adequado a essa situação? Diferencie agrupamento de classificação e explique o papel dos centróides.

### Situação 5: limites e responsabilidade

**F6.** Escolha uma das situações anteriores. Cite uma informação que poderia faltar ou estar inadequada e explique como isso poderia limitar o resultado do modelo. Sua resposta deve relacionar dados, regra ou parâmetro e resultado.

## 4. Comparabilidade entre os instrumentos

| Dimensão | Diagnóstico | Desafio final | Comparação possível |
| --- | --- | --- | --- |
| Dados e finalidade | D1, D2 e D3 | F1, F4a, F4b e F5 | Reconhecimento de dados e distinção entre previsão, classificação e agrupamento. |
| Previsão sobre alteração | D4 e D5 | F2 e F3 | Passagem de uma hipótese geral para explicação com dados, gráfico, parâmetro ou regra. |
| Limites de IA | D6 | F6 | Passagem de opinião ampla para explicação situada em um modelo e em dados concretos. |
| Linguagem computacional | Respostas espontâneas | Todas as questões F | Uso pertinente, e não obrigatório por si só, de termos como dado, modelo, parâmetro, limiar, vizinho, regra, centróide e previsão. |

Não se pretende calcular uma nota de ganho entre os instrumentos. A comparação será qualitativa e descritiva: observará mudanças nas explicações, na precisão conceitual e na capacidade de relacionar entrada, procedimento e saída.

## 5. Rubrica preliminar de análise

Cada dimensão poderá receber um código analítico de 0 a 2. Os códigos auxiliam a organizar o corpus e não substituem a leitura das respostas.

| Dimensão | 0 – inicial | 1 – em desenvolvimento | 2 – consistente para o nível introdutório |
| --- | --- | --- | --- |
| Dados e finalidade | Confunde dados, saída e tipo de tarefa, ou não justifica. | Identifica parte dos dados ou a finalidade geral. | Distingue dados, características e finalidade, com justificativa vinculada à situação. |
| Alteração e previsão | Apenas afirma que algo muda ou descreve o resultado sem relação. | Reconhece que dado, regra ou parâmetro interfere no resultado. | Antecipa ou explica a mudança conectando alteração, representação e saída do modelo. |
| Representação e conceito | Menciona gráfico, regra ou grupo isoladamente. | Relaciona uma representação a uma resposta. | Integra representação, conceito computacional e resultado de modo coerente. |
| Limites de IA | Trata a resposta como automática, humana ou infalível. | Reconhece influência de dados ou regras. | Indica possibilidade e limite situado, explicando como dado, regra ou parâmetro pode afetar a saída. |

## 6. Registro e análise

1. O instrumento será guardado com o código do estudante; a chave que associa código e nome, se necessária, ficará separada e restrita.
2. As respostas serão transcritas ou organizadas em planilha sem nomes antes da análise.
3. O pesquisador registrará os códigos analíticos e uma justificativa curta para cada dimensão.
4. Na dissertação, serão apresentadas sínteses do conjunto, frequências descritivas apenas quando úteis e poucos trechos anonimizados para ilustrar modos distintos de explicação.
5. Antes da aplicação, os enunciados devem passar por leitura crítica do orientador e, se permitido no planejamento, por uma revisão de clareza com pessoa de perfil semelhante ao público, sem produção de dados de pesquisa.

## 7. Pendências antes da versão final

- confirmar série, componente curricular, tempo efetivo disponível e forma de aplicação;
- ajustar vocabulário e extensão dos enunciados ao perfil da turma;
- verificar se algum item precisa de representação visual impressa ou projetada;
- revisar a rubrica com o orientador e definir o procedimento de dupla codificação ou revisão de uma amostra, caso seja metodologicamente viável;
- confirmar exigências éticas e institucionais antes de usar ou armazenar respostas.
