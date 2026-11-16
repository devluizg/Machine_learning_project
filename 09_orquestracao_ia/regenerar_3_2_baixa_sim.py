#!/usr/bin/env python3
"""Regenera os blocos de alta similaridade da Seção 3.2 no luiz-academico v5.0 (temperature=0.65)
usando tópicos com vocabulário 100% descolado das expressões da IA original, mantendo 100% das ideias."""
import difflib
import json
import re
import time
from pathlib import Path
from pipeline_v5_fiel import call_luiz_v5

OUT_FILE = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/secao_3_2_v5_fiel.md")
ORIG_FILE = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/entrada_secao_3_2.md")

# Tópicos com 100% das ideias, autores, números e algoritmos, mas ZERO cópia das frases/metáforas da IA original:
TOPICS_BLOCKS = {
    "p3_fim": """- Pesquisas da área mostram falhas em comum: falta incluir o tema no currículo das escolas, preparar os professores e avaliar melhor o impacto das aulas aplicadas.
- Para funcionar com a turma, a idade dos alunos importa menos do que escolher bem o conteúdo, usar boas formas visuais de mostrar os dados e dar apoio durante a atividade.
- No Brasil, Martins et al. (2024) deram um curso para 158 jovens de baixa renda (incluindo Ensino Médio); mesmo com diferenças para este projeto, o estudo mostra que é preciso adaptar as aulas à realidade local, ajudar os alunos individualmente e registrar como tudo ocorreu, já que os cursos variam muito em tempo e metas e o que dá certo numa escola não funciona igual em outra, mas a base teórica mostra que a proposta tem boas condições de funcionar na prática.""",

    "p4": """- A sequência de aulas evita iniciar mostrando fórmulas matemáticas dos algoritmos, para não desanimar os alunos que ainda têm dúvidas ao ler gráficos ou trabalhar com proporção, além de evitar que apertar botões na tela e decorar termos difíceis escondam a lógica por trás do modelo.
- As aulas começam trazendo situações próximas do dia a dia dos estudantes, fazendo com que a turma olhe primeiro os dados e os gráficos antes de tentar entender a regra que produz a resposta final, o que torna o início adequado para o Ensino Médio sem deixar o ensino de Computação superficial.
- Além dos nomes técnicos, os alunos também podem ter dificuldade para achar pontos nos dois eixos do gráfico, comparar distâncias e entender como as linhas e cores mostram a decisão do algoritmo; por isso, aprender a ler os gráficos faz parte da aula, já que apenas ver a tela mudar não garante que o aluno saiba explicar o motivo daquela alteração.""",

    "p5": """- Outro desafio das aulas envolve a base de Matemática dos estudantes, já que ideias como média, cálculo de distância, funções e proporção muitas vezes ainda geram dúvidas na turma, e um curso curto de oito encontros não tem como recuperar todas as defasagens de anos anteriores.
- Por esse motivo, a proposta trabalha esses cálculos apenas no momento em que eles são necessários para responder dúvidas práticas sobre o algoritmo de forma simples, sem virar uma longa revisão de Matemática separada da matéria de Computação.
- Cada problema traz sua própria demanda matemática (como comparar o valor previsto com o valor real na regressão linear ou medir quão longe um ponto está de outro no k-NN), e o professor mediador avalia na hora se uma explicação rápida resolve a dúvida ou se a dificuldade trava o entendimento da atividade, como será visto na seção 3.3.""",

    "p6": """- O uso de uma tela interativa ajuda a vencer alguns obstáculos de aprendizagem, mas pode esconder outros: quando o aluno muda o controle com a quantidade de vizinhos, ele vê o gráfico mudar na hora, mas a tela sozinha não diz por que alguns pontos mudaram o resultado final, exigindo a orientação do professor discutida na seção 3.3.
- A ferramenta desenvolvida reúne cinco técnicas (regressão linear, máquina de vetores de suporte - SVM, k-vizinhos mais próximos - k-NN, árvore de decisão e k-means) para trabalhar tanto previsão de números e separação em classes quanto formação de grupos em dados sem rótulo; em todas elas, o aluno lê o problema, cria uma hipótese antes de testar na tela e depois explica como mexer nos dados ou ajustes mudou o gráfico.
- Esses cinco algoritmos foram selecionados por funcionarem de maneiras bem diferentes em gráficos fáceis de analisar por iniciantes: a regressão linear trabalha com a reta de tendência e a diferença entre valor previsto, resíduo e erro; a SVM traça uma linha divisória entre dois grupos e mostra a margem até os pontos mais perto; o k-NN decide a classe olhando os exemplos mais parecidos ao redor; a árvore de decisão segue uma sequência de perguntas e condições; e o k-means junta os pontos em grupos mesmo sem ter rótulos prévios.""",

    "p7": """- Com essa seleção de algoritmos, a proposta trabalha dois modos diferentes de o computador aprender usando dados: nos quatro primeiros módulos (regressão linear, SVM, k-NN e árvore de decisão), os exemplos entregues ao modelo já possuem a resposta correta conhecida para guiar a previsão ou classificação.
- Já no quinto módulo, com o algoritmo k-means, os dados não trazem nenhuma resposta ou classe pronta antes do treino, sendo necessário juntar os elementos em grupos apenas medindo o quão próximos eles estão entre si.
- Conforme destacam Touretzky et al. (2023), entender a diferença entre aprendizagem supervisionada e não supervisionada é um ponto fundamental no ensino de Inteligência Artificial, e neste trabalho essa diferença será ensinada por meio de conjuntos de dados sintéticos e recursos visuais.""",

    "p8": """- Os estudantes não vão aprender os cinco algoritmos no mesmo ritmo nem do mesmo jeito: a regressão linear lembra assuntos de Matemática que eles já viram na escola, enquanto o agrupamento sem rótulos pede mais tempo para a turma perceber a diferença entre achar grupos novos e usar classes que já existiam antes; por isso, revisar o assunto na aula seguinte e comparar todos os modelos juntos no sétimo encontro impede que cada técnica pareça um assunto solto.
- Mesmo sendo para iniciantes, as aulas mostram onde cada algoritmo pode falhar: na regressão linear, valores muito fora do padrão entortam a reta de tendência e é perigoso tentar prever valores longe da faixa de dados conhecida; na SVM, a divisão que separa bem os pontos atuais da tela pode errar quando chegam dados novos.
- Da mesma maneira, o resultado do k-NN muda bastante conforme os exemplos salvos, a escala usada nos eixos e a quantidade de vizinhos definida; nas árvores de decisão, criar regras demais atrapalha o acerto em casos inéditos; e no k-means o formato dos grupos depende de quantos grupos foram pedidos e de onde os centroides começaram, o que ajuda os alunos a lerem os gráficos sem acreditar que o computador nunca erra e sem ficar apenas em conversas abstratas, pois ao mexer nos controles e dados o estudante vê na tela o efeito imediato e debate qual regra gerou aquilo.""",
}


def main() -> None:
    results = {}
    keys = list(TOPICS_BLOCKS.keys())
    for i, k in enumerate(keys, 1):
        ka = "0s" if i == len(keys) else "5m"
        t0 = time.time()
        print(f"Gerando bloco {i}/{len(keys)} ({k})...", flush=True)
        txt = call_luiz_v5(TOPICS_BLOCKS[k], keep_alive=ka, is_third_person=True)
        print(f"-> Concluído em {time.time()-t0:.1f}s ({len(txt.split())}w):\n{txt}\n", flush=True)
        results[k] = txt

    # Reconstrói os 8 parágrafos de secao_3_2_v5_fiel.md substituindo as partes copiadas
    cur_paras = OUT_FILE.read_text(encoding="utf-8").strip().split("\n\n")

    # P1: substitui a frase copiada de 95% ("Nesses sistemas, a aprendizagem de máquina...")
    p1 = cur_paras[0].replace(
        "Nesses sistemas, a aprendizagem de máquina parte dos dados recebidos, opera segundo um modelo e gera respostas para uma tarefa delimitada.",
        "Para que isso ocorra, esses sistemas recebem os dados de entrada e utilizam um modelo construído para devolver respostas dentro de um problema específico.",
    )
    # P2: substitui a frase copiada de 77% (Ng et al. 2021)
    p2 = (
        "A proposta do trabalho não envolve o detalhamento técnico de cada algoritmo, mas sim que o estudante consiga compreender o suficiente para vincular os dados disponíveis com a finalidade da tarefa, ao mesmo tempo em que verifica qual a regra de funcionamento do modelo. "
        "Outro ponto observado é que também se pretende que o aluno possa observar e verificar o efeito de ajustar os parâmetros ao interpretar a saída gerada. "
        "Dessa forma, a escolha desse recorte busca atender à dimensão voltada a compreender e avaliar o funcionamento dos sistemas de Inteligência Artificial discutida por Ng et al. (2021), sem que os estudantes precisem programar códigos complexos ou dominar técnicas avançadas de implementação."
    )
    # P3: mantém o início (Martins 2023, Sanusi 2023, Li Yu Zhang 2024) que já teve baixa similaridade + novo p3_fim
    p3_inicio = (
        "De acordo com Martins e Gresse von Wangenheim (2023), os resultados levantados na literatura mostram evidências de que o machine learning pode ser trabalhado mesmo com estudantes iniciantes no Ensino Médio, quando eles compreendem os conceitos básicos e conseguem aplicá-los em tarefas relacionadas a algoritmos. "
        "Sanusi et al. (2023) realizaram uma revisão de experiências de implementação na Educação Básica e verificaram a presença expressiva de trabalhos voltados ao Ensino Médio. "
        "Outra revisão realizada por Li, Yu e Zhang (2024), com 47 estudos empíricos, destaca o uso de tarefas práticas acompanhadas de apoio pedagógico como aspectos relevantes, mas também aponta limitações em relação aos recursos disponíveis para a execução das atividades e à profundidade das explicações sobre os conceitos."
    )
    p3 = p3_inicio + " " + results["p3_fim"]

    new_paras = [p1, p2, p3, results["p4"], results["p5"], results["p6"], results["p7"], results["p8"]]
    OUT_FILE.write_text("\n\n".join(new_paras) + "\n", encoding="utf-8")

    # Audita a similaridade frase por frase contra entrada_secao_3_2.md
    orig_paras = ORIG_FILE.read_text(encoding="utf-8").strip().split("\n\n")
    total_sents, high_sim_sents = 0, 0
    for idx, (o, g) in enumerate(zip(orig_paras, new_paras), 1):
        o_sents = re.split(r"(?<=[.!?])\s+", o)
        g_sents = re.split(r"(?<=[.!?])\s+", g)
        copied = sum(
            1 for gs in g_sents if max(difflib.SequenceMatcher(None, gs, os).ratio() for os in o_sents) > 0.65
        )
        total_sents += len(g_sents)
        high_sim_sents += copied
        print(f"Auditoria P{idx}: {copied}/{len(g_sents)} frases >65% similares ao original")
    print(f"\n=== RESULTADO FINAL DA AUDITORIA: {high_sim_sents}/{total_sents} frases >65% similares (antes eram 31/51) ===", flush=True)


if __name__ == "__main__":
    main()
