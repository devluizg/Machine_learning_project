export interface ModelComparison {
  id: 'regressao-linear' | 'svm' | 'knn' | 'arvore' | 'kmeans';
  model: string;
  purpose: string;
  input: string;
  output: string;
  mechanism: string;
  control: string;
  limit: string;
}

export const modelComparisons: readonly ModelComparison[] = [
  { id: 'regressao-linear', model: 'Regressão linear', purpose: 'Prever um valor numérico a partir de uma tendência.', input: 'Exemplos com medidas numéricas e valores conhecidos.', output: 'Um valor estimado.', mechanism: 'Ajusta uma reta que resume a relação entre as medidas.', control: 'Inclinação da reta.', limit: 'Pontos atípicos e previsões fora da faixa observada podem distorcer o resultado.' },
  { id: 'svm', model: 'SVM', purpose: 'Separar um caso entre duas classes conhecidas.', input: 'Exemplos com duas medidas e uma de duas etiquetas.', output: 'A classe indicada pelo lado da fronteira.', mechanism: 'Posiciona uma fronteira e procura ampliar a margem até os exemplos mais próximos.', control: 'Orientação e posição da fronteira.', limit: 'Dados sobrepostos ou uma divisão curva podem exigir outra estratégia.' },
  { id: 'knn', model: 'k-vizinhos mais próximos', purpose: 'Classificar um caso novo a partir de exemplos semelhantes.', input: 'Exemplos com medidas e etiquetas conhecidas.', output: 'A classe escolhida pela votação.', mechanism: 'Calcula distâncias e reúne os votos dos k exemplos mais próximos.', control: 'Número de vizinhos, k.', limit: 'Escalas inadequadas e muitos atributos podem tornar a distância pouco informativa.' },
  { id: 'arvore', model: 'Árvore de decisão', purpose: 'Classificar um caso por uma sequência de regras.', input: 'Exemplos com características e etiquetas conhecidas.', output: 'Uma classe e o caminho de regras usado.', mechanism: 'Escolhe perguntas que separam os exemplos em grupos menos misturados.', control: 'Profundidade máxima.', limit: 'Muitas divisões podem decorar os exemplos usados na construção.' },
  { id: 'kmeans', model: 'k-means', purpose: 'Formar grupos sem receber etiquetas prontas.', input: 'Exemplos com medidas, mas sem classes conhecidas.', output: 'Grupos e seus centróides.', mechanism: 'Alterna a atribuição ao centro mais próximo e o movimento dos centros para as médias.', control: 'Número e posição inicial dos centros.', limit: 'Os grupos dependem das escolhas iniciais e não possuem significado automático.' },
] as const;

export interface TeacherMeeting {
  number: number;
  title: string;
  guidingQuestion: string;
  route?: string;
  material?: string;
  phases: readonly { minutes: number; action: string }[];
  synthesis: string;
}

export interface StudentLesson {
  number: number;
  title: string;
  purpose: string;
  action: string;
  evidence: string;
  route?: string;
  siteUse: 'com-site' | 'sem-site';
}

export interface ModuleLessonContext {
  meeting: number;
  objective: string;
  before: string;
  action: string;
  explanation: string;
  next: string;
}

export const teacherMeetings: readonly TeacherMeeting[] = [
  { number: 1, title: 'Dados, modelos e tarefas', guidingQuestion: 'Como exemplos podem ajudar um sistema a produzir uma resposta?', route: '/', phases: [{ minutes: 20, action: 'Diagnóstico individual' }, { minutes: 15, action: 'Discussão de previsão, classificação e agrupamento' }, { minutes: 10, action: 'Introdução do site' }, { minutes: 5, action: 'Síntese oral' }], synthesis: 'Distinguir dado de entrada, resultado desejado e tipo de tarefa.' },
  { number: 2, title: 'Regressão linear', guidingQuestion: 'Como a inclinação altera uma previsão numérica?', route: '/regressao-linear', material: 'materiais-docentes/aula-02-regressao-linear.pdf', phases: [{ minutes: 8, action: 'Problema de passos e distância' }, { minutes: 7, action: 'Demonstração e leitura dos dados' }, { minutes: 5, action: 'Previsão individual' }, { minutes: 15, action: 'Experimento guiado' }, { minutes: 8, action: 'Gráfico, resíduo e erro' }, { minutes: 7, action: 'Registro individual e síntese' }], synthesis: 'Relacionar passos, distância, inclinação, previsão e erro.' },
  { number: 3, title: 'SVM', guidingQuestion: 'Como uma fronteira separa duas classes?', route: '/svm', material: 'materiais-docentes/aula-03-svm.pdf', phases: [{ minutes: 10, action: 'Duas classes e uma fronteira possível' }, { minutes: 7, action: 'Previsão individual' }, { minutes: 15, action: 'Experimento guiado' }, { minutes: 11, action: 'Margem e vetores de suporte' }, { minutes: 7, action: 'Síntese' }], synthesis: 'Relacionar fronteira, margem, vetores de suporte e classe.' },
  { number: 4, title: 'k-vizinhos mais próximos', guidingQuestion: 'Como os exemplos próximos participam da classificação?', route: '/knn', material: 'materiais-docentes/aula-04-knn.pdf', phases: [{ minutes: 13, action: 'Amostras por doçura e acidez' }, { minutes: 5, action: 'Previsão sobre k' }, { minutes: 15, action: 'Experimento guiado' }, { minutes: 10, action: 'Comparação dos votos' }, { minutes: 7, action: 'Síntese' }], synthesis: 'Relacionar distância, vizinhança, votação e classe.' },
  { number: 5, title: 'Árvore de decisão', guidingQuestion: 'Como perguntas em sequência produzem uma classe?', route: '/arvore', material: 'materiais-docentes/aula-05-arvore-decisao.pdf', phases: [{ minutes: 13, action: 'Objetos por largura e altura' }, { minutes: 5, action: 'Previsão sobre profundidade' }, { minutes: 15, action: 'Experimento guiado' }, { minutes: 10, action: 'Leitura de um caminho' }, { minutes: 7, action: 'Síntese' }], synthesis: 'Explicar a decisão por condições e reconhecer o risco de regras excessivas.' },
  { number: 6, title: 'k-means', guidingQuestion: 'Como grupos podem surgir sem etiquetas?', route: '/kmeans', material: 'materiais-docentes/aula-06-kmeans.pdf', phases: [{ minutes: 13, action: 'Amostras sem rótulos por doçura e acidez' }, { minutes: 5, action: 'Previsão sobre os centros' }, { minutes: 15, action: 'Atribuir e mover centróides' }, { minutes: 10, action: 'Comparação das rodadas' }, { minutes: 7, action: 'Síntese' }], synthesis: 'Diferenciar agrupamento de classificação e explicar o movimento do centróide.' },
  { number: 7, title: 'Comparação dos cinco modelos', guidingQuestion: 'Qual saída queremos e que mecanismo pode produzi-la?', route: '/sintese', material: 'materiais-docentes/aula-07-comparacao.pdf', phases: [{ minutes: 8, action: 'Retomada do quadro comparativo' }, { minutes: 10, action: 'Situações inéditas individuais' }, { minutes: 15, action: 'Comparação no site' }, { minutes: 10, action: 'Escolha e limite de um modelo' }, { minutes: 7, action: 'Preparação para a síntese final' }], synthesis: 'Escolher um modelo pela finalidade e justificar um limite.' },
  { number: 8, title: 'Síntese individual', guidingQuestion: 'Como explicar uma decisão sem tratar o modelo como infalível?', phases: [{ minutes: 5, action: 'Orientações' }, { minutes: 40, action: 'Instrumento final individual, sem consulta ao site' }, { minutes: 5, action: 'Encerramento' }], synthesis: 'Produzir a evidência final individual prevista na pesquisa.' },
] as const;

export const studentLessons: readonly StudentLesson[] = [
  { number: 1, title: 'Dados, modelos e tarefas', purpose: 'Reconhecer o que entra em um sistema e qual resposta se espera dele.', action: 'Responder ao diagnóstico em papel e participar da introdução conduzida pelo professor.', evidence: 'Distinguir dados, resultado desejado, classificação e agrupamento.', route: '/', siteUse: 'com-site' },
  { number: 2, title: 'Regressão linear', purpose: 'Entender como uma reta pode estimar um valor numérico.', action: 'Prever o efeito da inclinação e comparar valor observado com valor previsto.', evidence: 'Explicar previsão, diferença e erro usando o gráfico.', route: '/regressao-linear', siteUse: 'com-site' },
  { number: 3, title: 'SVM', purpose: 'Compreender como uma fronteira e sua margem separam duas classes.', action: 'Comparar a fronteira posicionada pelo estudante com a sugerida pelo algoritmo.', evidence: 'Explicar o papel dos vetores de suporte e da margem.', route: '/svm', siteUse: 'com-site' },
  { number: 4, title: 'k-vizinhos mais próximos', purpose: 'Compreender uma classificação baseada em proximidade e votação.', action: 'Comparar diferentes valores de k para a mesma amostra.', evidence: 'Relacionar distância, vizinhos, votos e classe.', route: '/knn', siteUse: 'com-site' },
  { number: 5, title: 'Árvore de decisão', purpose: 'Acompanhar como regras em sequência produzem uma decisão.', action: 'Seguir um caminho da raiz até a folha e comparar profundidades.', evidence: 'Explicar a saída pelas condições verificadas.', route: '/arvore', siteUse: 'com-site' },
  { number: 6, title: 'k-means', purpose: 'Observar como grupos surgem quando não existem rótulos prontos.', action: 'Atribuir pontos e mover centróides em rodadas sucessivas.', evidence: 'Diferenciar agrupamento de classificação e explicar o movimento dos centros.', route: '/kmeans', siteUse: 'com-site' },
  { number: 7, title: 'Comparação dos modelos', purpose: 'Escolher um modelo pela finalidade da tarefa e pelo tipo de saída.', action: 'Comparar os cinco modelos em situações novas.', evidence: 'Justificar uma escolha e indicar um limite.', route: '/sintese', siteUse: 'com-site' },
  { number: 8, title: 'Síntese individual', purpose: 'Mobilizar os conceitos estudados em uma situação nova.', action: 'Responder individualmente ao material entregue pelo professor.', evidence: 'Relacionar dados, tarefa, regra, resultado e limite sem consultar o site.', siteUse: 'sem-site' },
] as const;

export const moduleLessonContexts: Record<ModelComparison['id'], ModuleLessonContext> = {
  'regressao-linear': { meeting: 2, objective: 'Relacionar inclinação, previsão numérica e erro.', before: 'Registre o que espera que aconteça com a previsão quando a inclinação aumentar.', action: 'Altere primeiro somente a inclinação da reta.', explanation: 'Explique a mudança comparando valor previsto e valor observado.', next: 'Na aula 3, uma fronteira separará duas classes.' },
  svm: { meeting: 3, objective: 'Relacionar fronteira, margem, vetores de suporte e classe.', before: 'Preveja se aproximar a fronteira de uma classe reduz a margem.', action: 'Posicione a linha e compare com a fronteira sugerida pelo algoritmo.', explanation: 'Explique quais exemplos delimitam a margem e em que lado fica o ponto novo.', next: 'Na aula 4, a classe será escolhida pela votação dos vizinhos.' },
  knn: { meeting: 4, objective: 'Relacionar proximidade, valor de k, votação e classe.', before: 'Preveja se a classe permanecerá igual quando mais vizinhos entrarem na votação.', action: 'Compare dois valores de k para a mesma amostra.', explanation: 'Explique quais vizinhos entraram e como os votos produziram a classe.', next: 'Na aula 5, a decisão seguirá regras em sequência.' },
  arvore: { meeting: 5, objective: 'Explicar uma classificação por regras e caminhos.', before: 'Preveja se uma árvore mais profunda sempre decidirá melhor em casos novos.', action: 'Siga um caso pelo caminho destacado e compare profundidades.', explanation: 'Explique quais condições levaram à folha final e indique um limite.', next: 'Na aula 6, os dados não terão categorias prontas.' },
  kmeans: { meeting: 6, objective: 'Diferenciar agrupamento de classificação.', before: 'Preveja para onde um centróide se moverá quando novos pontos próximos entrarem no grupo.', action: 'Alterne atribuição e movimento dos centróides.', explanation: 'Explique como a posição dos pontos altera os centros e os grupos.', next: 'Na aula 7, os cinco modelos serão comparados pela finalidade.' },
};
