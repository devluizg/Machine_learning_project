#!/usr/bin/env python3
"""Gera a Seção 3.4 completa no luiz-academico v5.0 (temperature=0.65)
com 100% de fidelidade às ideias e tópicos secos com baixa similaridade sintática."""
import difflib
import re
import time
from pathlib import Path
from pipeline_v5_fiel import call_luiz_v5

OUT_FILE = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/secao_3_4_v5_fiel.md")

ORIG_TEXT = """Avaliar o ensino de machine learning na Educação Básica permanece uma questão em aberto. Rauber e Gresse von Wangenheim (2023) levantaram avaliações que vão de questionários a tarefas baseadas em desempenho e destacaram a necessidade de abordagens mais abrangentes. Ao investigar concepções discentes sobre machine learning, Mühling et al. (2023) analisaram qualitativamente respostas abertas antes e depois de uma oficina. Embora adote outro desenho analítico, este estudo compartilha a opção por solicitar explicações curtas e lê-las segundo os conceitos mobilizados, superando a simples contagem de acertos.

Gresse von Wangenheim et al. (2022) apresentam uma rubrica baseada em desempenho para conceitos e práticas de machine learning, mostrando a importância de converter expectativas de aprendizagem em critérios observáveis. Embora voltado à classificação de imagens, esse modelo pode ser adaptado ao recorte desta pesquisa. Reconhecer o nome de um algoritmo está longe de provar que o estudante compreende a tarefa resolvida ou a ligação entre dados e saída. Como um acerto numérico pode decorrer de simples chute na leitura do gráfico ou da repetição de falas docentes, os instrumentos pedirão justificativas breves que revelem o raciocínio adotado.

A compreensão vai além do acerto em questões de múltipla escolha. O diagnóstico inicial e o núcleo comparável do instrumento final solicitarão operações cognitivas equivalentes em extensão e dificuldade. Longe de selecionar estudantes ou medir déficits, o diagnóstico inicial levantará concepções prévias. Isso ocorre quando alguém atribui decisões à inteligência artificial ignorando dados e regras, ou quando confunde previsão com classificação e supõe categorias prontas em agrupamentos. No instrumento final, o primeiro bloco retomará essas dimensões em questões equivalentes. Já o segundo bloco trará uma situação inédita para examinar a transferência conceitual, evitando equiparar essa tarefa mais complexa ao levantamento feito no início. Enquanto registros individuais no segundo, quarto e sexto encontros acompanharão as previsões e explicações da turma, as notas do professor-pesquisador situarão as dúvidas surgidas e as intervenções nas condições de uso.

Black e Wiliam (1998) discutem a avaliação formativa como parte do ensino, pois as informações produzidas pelos estudantes podem orientar decisões docentes. As perguntas na plataforma servirão para dar devolutiva imediata e organizar a conversa em sala, sem coleta digital de respostas. Durante a exploração, o professor poderá usar as previsões para identificar dificuldades que peçam retomada, dispensando o registro de cada fala como dado de pesquisa. Caso vários estudantes suponham que uma fronteira separa classes sem relação com os exemplos exibidos, a aula poderá pausar a manipulação para retomar a margem e os casos mais próximos da divisão. Da mesma forma, eventuais confusões entre k-NN e k-means serão tratadas retomando a presença ou ausência de rótulos nos exemplos. Tais intervenções pertencem ao ensino, cabendo ao registro posterior contextualizar as produções. A análise confrontará o diagnóstico e o instrumento final com registros individuais selecionados e anotações docentes.

A análise se apoia em quatro dimensões que vão do reconhecimento da origem dos dados e da tarefa até a antecipação de ajustes, passando pela leitura de representações e dos limites na decisão automatizada. Uma rubrica em três níveis separará as respostas sem relação justificável daquelas com relações parciais ou explicações consistentes com o caráter introdutório da sequência, organizando o corpus sem gerar um índice isolado de competência. Uma situação sobre caminhada, por exemplo, poderá exigir que o estudante diferencie quantidade de passos e distância percorrida, evitando tratar todos os valores apenas como dados genéricos. Outras questões pedirão que ele antecipe o que acontece ao mover pontos e centroides na tela, ou ao mudar parâmetros como a posição da fronteira, as condições e o número de vizinhos. Assim, a leitura de tabelas e gráficos nos modelos será avaliada pela justificativa dada ao acerto.

Há diferença entre escrever que “mudou porque o programa mudou” e explicar que aproximar a fronteira de uma classe reduziu sua margem em relação aos exemplos mais próximos. A rubrica registrará essa diferença por dimensão, acompanhada de justificativa curta, sem produzir rótulos fixos para caracterizar estudantes.

A apresentação dos resultados combinará sínteses por dimensão e tabelas de transição entre momentos comparáveis, apoiadas por frequências descritivas com seus denominadores e breves excertos anonimizados. A análise acompanhará o que muda ou permanece em cada participante, evitando ranquear os estudantes. Já o desafio de transferência e o questionário de percepção terão seções próprias, situando a discussão nas condições que delimitam a intervenção."""

TOPICS_BLOCKS = [
    # Bloco 1 (Rauber 2023 & Mühling 2023)
    """- Avaliar a aprendizagem de machine learning na Educação Básica ainda é um campo em aberto nas pesquisas; Rauber e Gresse von Wangenheim (2023) levantaram instrumentos como testes e tarefas práticas e apontaram a carência de formas de avaliação mais completas.
- Ao investigar as ideias dos alunos sobre inteligência artificial, Mühling et al. (2023) analisaram respostas escritas abertas antes e depois de uma oficina escolar.
- Mesmo com desenho de pesquisa diferente, esta proposta também prioriza pedir explicações curtas dos estudantes para analisar os conceitos empregados, indo além de apenas contar respostas certas e erradas.""",

    # Bloco 2 (Gresse von Wangenheim 2022 e justificativas)
    """- Gresse von Wangenheim et al. (2022) propuseram uma rubrica prática para medir conceitos e habilidades de machine learning na escola, mostrando a necessidade de transformar metas pedagógicas em critérios claros de observação.
- Embora essa rubrica tenha sido criada para classificar fotos, seus critérios podem ser adaptados para os cinco modelos deste trabalho.
- Saber de cor o nome de um algoritmo não comprova que o estudante entendeu a tarefa nem como a regra liga os dados ao resultado; como um acerto numérico pode vir de puro chute no gráfico ou de repetir falas do professor, os instrumentos cobrarão justificativas breves do raciocínio feito.""",

    # Bloco 3 (Diagnóstico inicial, núcleo comparável e desafio de transferência)
    """- A compreensão dos alunos vai além de marcar opções certas em testes de múltipla escolha; por isso, o diagnóstico inicial e a parte equivalente do teste final exigirão o mesmo nível de raciocínio e tamanho de tarefa.
- O diagnóstico do início serve para mapear as ideias prévias da turma (como achar que o computador decide sozinho sem dados, trocar previsão por classificação ou achar que agrupamento já vem com classes prontas), sem intenção de ranquear ou medir déficits.
- O instrumento final repete essas mesmas situações no primeiro bloco e acrescenta um segundo bloco com um problema novo de transferência conceitual avaliado em separado, enquanto registros dos encontros dois, quatro e seis e anotações do professor acompanham a evolução da turma.""",

    # Bloco 4 (Avaliação formativa: Black e Wiliam 1998 e intervenção docente)
    """- Black e Wiliam (1998) tratam a avaliação formativa como parte ativa do ensino, na qual as respostas dos alunos servem para guiar o rumo das explicações do docente.
- As perguntas inseridas na ferramenta servem para dar retorno rápido e puxar debates com a turma durante a aula, sem gravação de notas pelo sistema.
- Durante os testes na tela, o professor usa as hipóteses dos estudantes para notar dúvidas coletivas e intervir na hora (como retomar o papel dos dados na margem da SVM ou lembrar a presença de rótulos no k-NN contra a ausência no k-means), confrontando depois esses registros com o diagnóstico e o instrumento final.""",

    # Bloco 5 (Quatro dimensões de análise e rubrica em 3 níveis)
    """- A análise dos dados se organiza em quatro eixos principais: identificar a origem dos dados e a tarefa pedida, ler as representações visuais, prever o efeito de ajustes e reconhecer as limitações das decisões automáticas.
- Uma rubrica com três níveis de resposta organizará o material entre tentativas sem relação válida, explicações parciais e respostas consistentes com o nível introdutório, evitando reduzir o aprendizado a uma única nota numérica.
- Nas atividades práticas, como uma situação sobre caminhada, o aluno precisa separar passos dados de distância percorrida para não tratar números como dados genéricos, além de antecipar o que muda ao mover pontos, alterar a fronteira, trocar condições ou mexer no número de vizinhos.""",

    # Bloco 6 (Diferença qualitativa nas explicações e recusa a rótulos)
    """- Há uma diferença clara entre uma resposta vazia como dizer que o gráfico mudou porque o computador quis e uma explicação conceitual que mostra que puxar a linha divisória diminuiu a margem dos exemplos mais próximos.
- A rubrica de avaliação registrará essa qualidade de resposta em cada uma das quatro dimensões, acompanhada de um comentário breve sobre o raciocínio do aluno.
- O objetivo dessa análise qualitativa é acompanhar o entendimento conceitual sem carimbar os estudantes com rótulos definitivos de rendimento.""",

    # Bloco 7 (Apresentação dos resultados e contexto)
    """- A apresentação dos resultados reunirá resumos por dimensão e quadros comparando o antes e o depois dos momentos equivalentes, acompanhados de contagens percentuais claras e pequenos trechos anônimos das falas dos alunos.
- A pesquisa acompanhará o que mudou e o que permaneceu no entendimento de cada aluno ao longo das aulas, sem comparar ou classificar os participantes entre si.
- A atividade de transferência inédita e o questionário final de opinião dos estudantes serão discutidos em partes próprias, mantendo a análise fiel às condições reais em que as aulas aconteceram na escola.""",
]


def main() -> None:
    generated_paras = []
    for i, top in enumerate(TOPICS_BLOCKS, 1):
        ka = "0s" if i == len(TOPICS_BLOCKS) else "5m"
        t0 = time.time()
        print(f"Gerando Bloco {i}/{len(TOPICS_BLOCKS)} da Seção 3.4...", flush=True)
        txt = call_luiz_v5(top, keep_alive=ka, is_third_person=True)
        print(f"-> Bloco {i} concluído em {time.time()-t0:.1f}s ({len(txt.split())}w):\n{txt}\n", flush=True)
        generated_paras.append(txt)

    OUT_FILE.write_text("\n\n".join(generated_paras) + "\n", encoding="utf-8")

    # Auditoria de similaridade frase por frase contra ORIG_TEXT
    orig_paras = ORIG_TEXT.strip().split("\n\n")
    total_s, high_s = 0, 0
    for idx, (o, g) in enumerate(zip(orig_paras, generated_paras), 1):
        os_list = [s for s in re.split(r"(?<=[.!?])\s+", o) if len(s.split()) > 4]
        gs_list = [s for s in re.split(r"(?<=[.!?])\s+", g) if len(s.split()) > 4]
        copied = sum(
            1 for gs in gs_list if max(difflib.SequenceMatcher(None, gs, os).ratio() for os in os_list) > 0.65
        )
        total_s += len(gs_list)
        high_s += copied
        print(f"Auditoria Bloco {idx}: {copied}/{len(gs_list)} frases >65% similares ao original")
    print(f"\n=== AUDITORIA FINAL SEÇÃO 3.4: {high_s}/{total_s} frases >65% similares ===", flush=True)


if __name__ == "__main__":
    main()
