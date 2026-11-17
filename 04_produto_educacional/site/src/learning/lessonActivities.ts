import type { LessonActivitySpec } from './LessonActivitySheet';

export const lessonActivities: Record<string, LessonActivitySpec> = {
  'diagnostico-inicial': {
    moduleId: 'diagnostico-inicial',
    lessonTitle: 'Aula 1: Diagnóstico inicial — como computadores aprendem com dados',
    situation:
      'Este questionário NÃO é prova e NÃO vale nota. Responda do seu jeito, explicando como você pensou. Não precisa saber programação nem inteligência artificial — se não tiver certeza, escreva o que você imagina.',
    questions: [
      {
        id: 'q1-entradas-saida',
        title: 'Questão 1 — O que o sistema recebe e o que ele precisa descobrir?',
        prompt:
          'Olhe a tabela lá em cima com os 4 dias anotados na escola (temperatura, pessoas na sala e gasto de energia). A escola quer usar esses dados para prever o gasto de energia de outros dias:',
        table: {
          columns: ['Pergunta', 'Sua resposta'],
          rows: [
            {
              id: 'a-estimar',
              label: 'a) Qual coluna da tabela mostra o que a escola quer descobrir (prever)?',
              placeholder: 'Escreva o nome da coluna...',
            },
            {
              id: 'b-entradas',
              label: 'b) Quais informações da tabela ajudam o sistema a fazer essa previsão?',
              placeholder: 'Escreva quais colunas ajudam...',
            },
            {
              id: 'c-origem',
              label: 'c) Antes de confiar nesse resultado, o que você perguntaria sobre como esses dados foram anotados?',
              placeholder: 'Ex.: quem mediu, se o aparelho estava certo...',
            },
          ],
        },
      },
      {
        id: 'q2-previsao-tabela',
        title: 'Questão 2 — Fazendo uma previsão pela tabela',
        prompt:
          'Olhe a tabela de novo. Imagine um 5º dia com temperatura de 29 °C e uma quantidade de pessoas parecida com a dos dias 3 e 4. Sem fazer conta exata, você acha que o gasto de energia vai ficar mais perto de 5 ou de 10? Explique como a tabela ajudou você a pensar nisso.',
        rows: 4,
      },
      {
        id: 'q3-fronteira-classes',
        title: 'Questão 3 — Quando a regra de separação muda',
        prompt:
          'Um aplicativo separa frutas em Tipo A e Tipo B usando duas medidas: tamanho e peso. A regra do aplicativo é: se (tamanho + peso) der 12 ou mais, a fruta vai para o Tipo B; se der menos que 12, vai para o Tipo A. Chegou uma fruta nova com tamanho 6 e peso 5.',
        table: {
          columns: ['Pergunta', 'Sua resposta'],
          rows: [
            {
              id: 'a-regra-inicial',
              label: 'a) Pela regra inicial (soma 12 ou mais), essa fruta vai para o Tipo A ou Tipo B?',
              placeholder: 'Diga o tipo e explique a conta...',
            },
            {
              id: 'b-nova-fronteira',
              label: 'b) E se mudarem a regra do aplicativo para (soma 10 ou mais)? Para qual tipo ela vai agora?',
              placeholder: 'Diga o tipo e explique...',
            },
            {
              id: 'c-medidas',
              label: 'c) Quando o aplicativo mudou a regra, a fruta mudou de tamanho ou de peso? Explique.',
              placeholder: 'Sim ou não, e por quê...',
            },
          ],
        },
      },
      {
        id: 'q4-grupos-sem-rotulo',
        title: 'Questão 4 — Juntando pontos parecidos sem nome pronto',
        prompt:
          'Estudantes marcaram num mapa 6 pontos do bairro para recolher garrafas recicláveis. Alguns pontos ficam bem perto uns dos outros. Eles querem juntar os pontos próximos em grupos para organizar as rotas, mas ainda não deram nome nem categoria para nenhum grupo.',
        table: {
          columns: ['Pergunta', 'Sua resposta'],
          rows: [
            {
              id: 'a-produzir',
              label: 'a) O que eles querem descobrir olhando os pontos no mapa?',
              placeholder: 'Escreva com suas palavras...',
            },
            {
              id: 'b-distancia',
              label: 'b) Como a distância entre os pontos ajuda a montar esses grupos?',
              placeholder: 'Escreva como a proximidade ajuda...',
            },
            {
              id: 'c-definidos-antes',
              label: 'c) Eles precisam saber o nome de cada grupo antes de começar? Explique.',
              placeholder: 'Sim ou não, e por quê...',
            },
          ],
        },
      },
      {
        id: 'q5-limites-decisao',
        title: 'Questão 5 — Quando uma regra automática pode falhar',
        prompt:
          'Uma escola quer usar um sistema automático que avisa quando uma sala precisa de manutenção. A única regra do sistema é: se a temperatura passar de 30 °C, aparece o aviso "verificar manutenção". Você acha que olhar só a temperatura basta para tomar essa decisão? Explique por quê, diga mais uma informação que ajudaria e como ela poderia mudar o aviso.',
        rows: 5,
      },
    ],
  },
  'regressao-linear': {
    moduleId: 'regressao-linear',
    lessonTitle: 'Aula 2: passos e distância percorrida (Regressão Linear)',
    situation:
      'Queremos estimar a distância percorrida por uma pessoa usando apenas o número de passos. O comprimento de cada passo pode variar; por isso, os dados formam uma tendência, não uma regra exata para todas as pessoas.',
    questions: [
      {
        id: 'q1-previsao-antes',
        title: '1. Previsão antes da medição',
        prompt: 'Quando o número de passos aumenta, o que você espera que aconteça com a distância percorrida? Explique.',
        rows: 2,
      },
      {
        id: 'q2-variaveis',
        title: '2. Leitura das variáveis',
        prompt: 'Complete a tabela identificando o que entra no modelo e o que queremos prever:',
        table: {
          columns: ['Papel na tarefa', 'Sua resposta'],
          rows: [
            { id: 'entrada', label: 'Valor usado como entrada', placeholder: 'Ex.: número de passos' },
            { id: 'saida', label: 'Valor que queremos prever', placeholder: 'Ex.: distância percorrida (m)' },
          ],
        },
      },
      {
        id: 'q3-caso-novo',
        title: '3. Previsão para 28 passos',
        prompt: 'Observando os pontos da tabela (de 4 a 24 passos), estime a distância para 28 passos sem usar fórmula e explique como chegou ao valor.',
        rows: 2,
      },
      {
        id: 'q4-hipotese',
        title: '4. Hipótese antes de alterar a reta',
        prompt: 'Para 20 passos, a previsão de distância tende a aumentar, diminuir ou permanecer igual quando a inclinação da reta aumenta? Explique.',
        rows: 2,
      },
      {
        id: 'q5-registro-exploracao',
        title: '5. Registro da exploração (Antes e Depois)',
        prompt: 'Anote na tabela abaixo os valores mostrados no painel "O QUE ACONTECEU" antes e depois de aumentar a inclinação:',
        table: {
          columns: ['Situação', 'Antes da alteração', 'Depois da alteração'],
          rows: [
            { id: 'inclinacao', label: 'Inclinação da reta', placeholder: 'Ex.: 0,45 m/passo' },
            { id: 'previsao20', label: 'Previsão para 20 passos', placeholder: 'Ex.: 9,50 m' },
            { id: 'erro-medio', label: 'Erro médio mostrado (MSE)', placeholder: 'Ex.: 4,212 m²' },
          ],
        },
      },
      {
        id: 'q6-comparacao-hipotese',
        title: '6. Compare sua hipótese',
        prompt: 'O resultado confirmou ou contrariou sua previsão do item 4? Explique o que mudou no gráfico e nos quadrados dos erros.',
        rows: 2,
      },
      {
        id: 'q7-ponto-acima',
        title: '7. Ponto acima da reta',
        prompt: 'Um ponto observado ficou acima da reta. O que isso indica sobre a distância observada e a distância prevista para aquele número de passos?',
        rows: 2,
      },
      {
        id: 'q8-residuo',
        title: '8. Calcule e interprete o resíduo',
        prompt:
          'Para 20 passos, uma reta indicou 11,6 m, mas o valor observado foi 12,1 m. (a) Qual é a diferença entre o valor observado e o previsto? (b) O que essa diferença informa sobre a previsão da reta nesse ponto?',
        rows: 3,
      },
      {
        id: 'q9-explique-modelo',
        title: '9. Explique o modelo e os limites',
        prompt:
          'Um colega afirmou: "Se a reta passa perto dos pontos, ela sempre acertará a distância de qualquer pessoa". Você concorda? Responda usando o que observou na aula.',
        rows: 3,
      },
      {
        id: 'q10-sintese',
        title: 'Síntese final para completar',
        prompt: 'Preencha cada lacuna da síntese:',
        table: {
          columns: ['Trecho da frase', 'Palavra que completa'],
          rows: [
            { id: 'lacuna1', label: 'A regressão linear usa uma reta para representar uma...', placeholder: 'Digite a palavra' },
            { id: 'lacuna2', label: 'A reta produz uma ... numérica.', placeholder: 'Digite a palavra' },
            { id: 'lacuna3', label: 'A diferença entre o valor observado e o previsto é chamada de...', placeholder: 'Digite a palavra' },
          ],
        },
      },
    ],
  },
  svm: {
    moduleId: 'svm',
    lessonTitle: 'Aula 3: fronteira, margem e classificação (SVM)',
    situation:
      'Em um gráfico, exemplos da classe A ficam no lado inferior esquerdo e exemplos da classe B ficam no lado superior direito. Uma linha foi desenhada para separar as duas classes. Os pontos A4 e B1 são os mais próximos da linha.',
    questions: [
      {
        id: 'q1-vetores-suporte',
        title: 'Questão 1 — Vetores de suporte e margem',
        prompt: 'Por que A4 e B1 podem ser chamados de vetores de suporte? Explique a relação deles com a margem.',
        rows: 3,
      },
      {
        id: 'q2-deslocamento',
        title: 'Questão 2 — Movimento da fronteira',
        prompt: 'Imagine que a linha seja deslocada para mais perto de A4, mantendo a mesma inclinação. O que tende a acontecer com a margem? Explique.',
        rows: 3,
      },
      {
        id: 'q3-novo-ponto',
        title: 'Questão 3 — Classificação e limites',
        prompt:
          'Um novo ponto fica no mesmo lado da fronteira que os exemplos B. Qual classe a SVM indicará para ele? O que poderia dificultar essa classificação em outro conjunto de dados?',
        rows: 3,
      },
    ],
  },
  knn: {
    moduleId: 'knn',
    lessonTitle: 'Aula 4: proximidade, vizinhos e votação (k-NN)',
    situation:
      'Um gráfico apresenta alimentos fictícios em dois eixos: doçura e acidez. Alguns exemplos já têm rótulo de categoria A ou categoria B. Uma nova amostra ainda não tem rótulo, e o sistema observa os exemplos mais próximos para decidir.',
    questions: [
      {
        id: 'q1-proximidade',
        title: 'Questão 1 — Proximidade nas características',
        prompt: 'Por que exemplos próximos da nova amostra podem ajudar a escolher uma categoria? Explique usando as características de doçura e acidez.',
        rows: 3,
      },
      {
        id: 'q2-votacao',
        title: 'Questão 2 — Votação dos k vizinhos',
        prompt: 'Uma nova amostra tem três vizinhos próximos: dois são da categoria A e um é da categoria B. Qual categoria tende a vencer a votação quando k = 3? Explique.',
        rows: 3,
      },
      {
        id: 'q3-efeito-k',
        title: 'Questão 3 — Mudança no valor de k',
        prompt: 'Ao aumentar o valor de k, outros exemplos mais distantes podem entrar na votação. Como isso pode mudar a categoria atribuída à nova amostra?',
        rows: 3,
      },
    ],
  },
  'arvore-decisao': {
    moduleId: 'arvore-decisao',
    lessonTitle: 'Aula 5: regras e caminhos de decisão (Árvore de Decisão)',
    situation:
      'Uma árvore classifica objetos fictícios usando duas características: largura e altura. A primeira pergunta avalia a largura em relação a um limite; depois, cada ramo faz uma pergunta sobre altura antes de indicar uma categoria.',
    questions: [
      {
        id: 'q1-regra-raiz',
        title: 'Questão 1 — Primeira pergunta da árvore',
        prompt: 'Escreva uma regra possível para a primeira pergunta da árvore e indique o que acontece em cada resposta ("sim" e "não").',
        rows: 3,
      },
      {
        id: 'q2-caminho-objeto',
        title: 'Questão 2 — Caminho até a categoria',
        prompt: 'Escolha um objeto do exemplo (movendo o ponto ?) e descreva o caminho de perguntas que ele percorre até chegar a uma categoria.',
        rows: 3,
      },
      {
        id: 'q3-profundidade',
        title: 'Questão 3 — Mais perguntas e limites',
        prompt: 'Se a árvore receber mais uma pergunta antes de decidir, o que pode mudar? Isso garante uma classificação melhor em todos os casos? Explique.',
        rows: 3,
      },
    ],
  },
  kmeans: {
    moduleId: 'kmeans',
    lessonTitle: 'Aula 6: grupos e centróides (k-means)',
    situation:
      'Um gráfico apresenta alimentos fictícios em dois eixos: doçura e acidez. Nenhum alimento tem uma categoria pronta. O sistema organiza pontos próximos em grupos e calcula um centróide para cada grupo.',
    questions: [
      {
        id: 'q1-classificar-vs-agrupar',
        title: 'Questão 1 — Classificar vs. agrupar sem rótulos',
        prompt: 'Qual é a diferença entre classificar uma amostra e formar grupos sem categorias prontas? Explique com base na situação apresentada.',
        rows: 3,
      },
      {
        id: 'q2-movimento-centroide',
        title: 'Questão 2 — Deslocamento do centróide',
        prompt: 'Se novos pontos entram próximos de um grupo, por que o centróide desse grupo pode se deslocar? Explique usando a posição dos pontos.',
        rows: 3,
      },
      {
        id: 'q3-limites-grupos',
        title: 'Questão 3 — Limites do agrupamento',
        prompt: 'Os grupos encontrados pelo sistema são categorias verdadeiras e definitivas dos alimentos? Explique o que pode influenciar a organização dos grupos.',
        rows: 3,
      },
    ],
  },
  'regressao-logistica': {
    moduleId: 'regressao-logistica',
    lessonTitle: 'Aprofundamento: probabilidade e limiar de decisão',
    situation:
      'Uma curva em S transforma a entrada em uma probabilidade estimada entre 0% e 100%, e o limiar de corte define quando o modelo escolhe a classe B.',
    questions: [
      {
        id: 'q1-limiar',
        title: 'Questão 1 — Probabilidade vs. decisão',
        prompt: 'Quando você altera apenas o limiar de decisão (mantendo a curva fixa), o que muda na saída: a probabilidade calculada ou apenas a classe escolhida?',
        rows: 3,
      },
      {
        id: 'q2-sobreposicao',
        title: 'Questão 2 — Classes sobrepostas',
        prompt: 'Compare as classes separadas e as classes sobrepostas. Por que acertar os casos usados no treino não garante acerto nos casos novos?',
        rows: 3,
      },
    ],
  },
};
