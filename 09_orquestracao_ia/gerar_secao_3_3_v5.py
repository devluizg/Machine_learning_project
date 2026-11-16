#!/usr/bin/env python3
"""Gera a Seção 3.3 completa no luiz-academico v5.0 (temperature=0.65)
com 100% de fidelidade às ideias e vocabulário de tópicos 100% descolado da sintaxe da IA."""
import difflib
import re
import time
from pathlib import Path
from pipeline_v5_fiel import call_luiz_v5

OUT_FILE = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/secao_3_3_v5_fiel.md")

ORIG_TEXT = """Ferramentas visuais permitem introduzir machine learning a estudantes iniciantes. Gresse von Wangenheim et al. (2021) identificaram ferramentas que favorecem a construção interativa de modelos, embora várias se concentrem na classificação de imagens e em atividades curtas. O produto proposto articula dados sintéticos e tabelas da própria turma em tarefas de regressão e classificação, além de agrupamento. Essa diferença de escopo não resolve, por si só, as limitações apontadas pela literatura. A interação ganha sentido pedagógico quando o estudante investiga uma relação. A visualização pode tornar visível algo que permaneceria abstrato em uma explicação verbal, mas também pode dar a impressão de que observar uma mudança basta para compreendê-la. Os elementos visuais precisam ter significado explícito, e a regra do modelo deve estar acessível.

Os dados sintéticos permitem controlar o que será comparado e produzir situações em que a modificação de um elemento gera uma consequência perceptível. Não servem como previsão confiável sobre pessoas reais. Os dados organizados pela própria turma no segundo encontro mostram de onde vêm os números que serão interpretados. O cenário didático leva a turma a identificar a mudança ocorrida e a explicar qual elemento do modelo produziu aquele efeito. Articular tabelas e gráficos a fórmulas, textos curtos e controles interativos mobiliza múltiplas representações. Ainsworth (2006) argumenta que representações diferentes podem cumprir funções complementares durante a aprendizagem, mas exigem tarefas de interpretação e integração. A plataforma não deve apenas reunir recursos na mesma tela. Cada representação precisa responder à pergunta examinada pela turma.

O uso de visualizações não substitui a atividade intelectual do estudante. No estudo de Vartiainen et al. (2021), a exploração de aplicações baseadas em dados foi acompanhada pela elaboração de ideias e explicações sobre o funcionamento da aprendizagem de máquina. Por isso, os controles da plataforma serão sempre ligados a uma previsão e a uma questão de explicação, evitando que a mudança percebida no gráfico seja tomada como compreensão suficiente. Qualquer ajuste nos controles da tela, seja na inclinação da reta e na posição da fronteira de decisão, seja nos parâmetros de vizinhos, condições ou centroides, pede uma questão que leve o estudante a antecipar e ler a mudança. Na regressão linear, os pares da tabela ganham forma no plano cartesiano para que a reta indique tendência ou previsão. Na SVM, a fronteira separa classes e a margem mostra quais exemplos ficam mais próximos da divisão. Já no k-NN, a posição do ponto consultado permite medir a distância até os exemplos para acompanhar a votação dos vizinhos. Enquanto nas árvores o percurso visual reflete as condições testadas, no k-means os centroides funcionam como referências móveis que reorganizam os grupos, longe de serem pontos decorativos. Em todos os módulos, a visualização vincula os dados e a regra do modelo à saída gerada.

A atividade adapta a estratégia de prever, observar e explicar proposta por White e Gunstone (1992). Antes de usar o controle, o estudante registra uma hipótese oral ou escrita e, na sequência, acompanha como o gráfico altera a medida calculada e a decisão para explicar se o resultado confirmou sua expectativa. O ciclo evita a tentativa e erro em que parâmetros são movimentados sem relação clara entre entrada e saída. A previsão torna visível uma ideia que poderia permanecer implícita. Se um estudante afirma que aumentar o número de vizinhos não alterará uma classificação e encontra decisão diferente, o professor pode perguntar quais exemplos passaram a ser considerados e por que a votação se alterou. Quando o estudante prevê que mover um centroide não terá efeito e observa a reorganização dos pontos, a explicação pode retomar a noção de proximidade. A hipótese inicial não precisa estar correta para ter valor pedagógico.

A aplicação está prevista para o laboratório de informática da escola, com acesso à internet, sujeito à confirmação das condições do campo. Planeja-se que cada estudante use um computador do laboratório ou, conforme a disponibilidade confirmada, um Chromebook, e a realização das atividades nos encontros busca reduzir as dificuldades decorrentes da restrição de acesso fora da escola. Para estudantes com insegurança no manuseio do computador, os controles deverão ser legíveis e indicar o que pode ser modificado em cada momento. Para aqueles que operam a interface com facilidade, o desafio deixa de ser o manuseio rápido do controle e passa a ser a explicação. A mediação docente, com suporte individual quando necessário, ajuda a evitar que a técnica de uso se torne obstáculo ou substitua a questão conceitual.

O controle interativo não será tratado como decoração ou recompensa após uma explicação pronta. Ele permite comparar uma consequência ao manter alguns fatores estáveis e alterar um dado ou parâmetro. A aula guiada orienta, inicialmente, uma alteração por vez, pois mudanças simultâneas dificultam atribuir uma consequência a uma causa percebida. Depois da aula guiada, a exploração livre poderá ampliar as comparações. O professor deverá retomar a finalidade do experimento e solicitar explicações que não se limitem a descrever elementos apresentados.

As representações matemáticas serão apresentadas em camadas. O percurso parte de uma situação concreta e do uso de tabelas ou gráficos na leitura dos dados, passando por cálculos simples até chegar à fórmula que resume a regra discutida. Assim, tanto a equação da reta e a posição da fronteira quanto o cálculo de distâncias, condições ou médias dos centroides entram para explicar mudanças visíveis na tela, evitando a cobrança de memorização desarticulada. Apresentar a Matemática em camadas não retira precisão dos conceitos. A organização em camadas define o que o estudante precisa para uma compreensão inicial e o momento em que cada noção passa a fazer sentido. Antes de calcular a distância entre dois pontos, o estudante precisa reconhecer por que a proximidade importa no k-NN, e antes de discutir o erro de uma reta, precisa comparar uma previsão com um valor observado. Introduzida após essas experiências, a fórmula ganha sentido prático por nomear uma relação que o estudante já conseguiu examinar visualmente durante o experimento."""

TOPICS_BLOCKS = [
    # Bloco 1
    """- O uso de recursos visuais facilita o primeiro contato de alunos iniciantes com o aprendizado de máquina; Gresse von Wangenheim et al. (2021) mapearam ferramentas voltadas à criação interativa de modelos, mas notaram que grande parte delas foca só em classificar imagens e em tarefas rápidas.
- Diferentemente disso, a ferramenta desenvolvida neste projeto combina conjuntos de dados sintéticos e tabelas montadas pela própria turma para trabalhar regressão, classificação e agrupamento, embora ampliar esses temas não baste sozinho para superar todas as falhas apontadas nos estudos da área.
- O uso interativo da tela só traz ganho de ensino quando o aluno busca entender a relação entre as variáveis: o gráfico ajuda a enxergar conceitos que ficariam muito abstratos apenas falados, mas pode criar a falsa ideia de que basta olhar a tela mudando para entender o assunto; por isso, cada item visual precisa ter um sentido claro e a lógica do modelo deve ficar visível ao estudante.""",

    # Bloco 2
    """- Trabalhar com dados sintéticos ajuda a isolar o que vai ser comparado na aula e criar casos em que mexer num único valor produz uma mudança clara na tela, mesmo que esses dados artificiais não sirvam para fazer previsões reais sobre pessoas; já os dados coletados e tabulados pelos próprios alunos no segundo encontro servem para mostrar a origem concreta dos números analisados, levando a turma a notar o que mudou e explicar qual parte do algoritmo causou aquilo.
- Ao juntar tabelas, gráficos, expressões matemáticas, pequenos textos e botões de ajuste, a proposta trabalha com várias formas de representação ao mesmo tempo.
- Segundo Ainsworth (2006), diferentes formas de mostrar uma informação se completam no aprendizado, desde que os alunos façam atividades para interpretar e relacionar uma com a outra; assim, a ferramenta não pode apenas empilhar gráficos e tabelas na tela, pois cada recurso visual precisa ajudar a responder à questão que a turma está investigando.""",

    # Bloco 3
    """- Olhar para os gráficos na tela não dispensa o esforço de raciocínio do aluno: Vartiainen et al. (2021) mostraram que, ao explorarem sistemas baseados em dados, os estudantes precisavam construir ideias e explicar com suas palavras como o aprendizado de máquina funcionava; por esse motivo, cada controle da nossa plataforma estará sempre acompanhado de uma pergunta de previsão e de explicação, para que ninguém ache que só ver o gráfico se mexer significa ter entendido a matéria.
- Toda vez que o estudante altera um ajuste na tela (seja mudando a inclinação da reta, o lugar da linha divisória, a quantidade de vizinhos, as regras de condição ou a posição dos centroides), a atividade pede que ele tente prever o que vai acontecer e interprete o novo gráfico.
- Em cada módulo o gráfico liga os dados de entrada e a regra do algoritmo ao resultado final: na regressão linear, os números da tabela viram pontos no plano cartesiano onde a reta mostra a tendência ou previsão; na SVM, uma linha divide os grupos e a faixa da margem indica os pontos mais encostados na fronteira; no k-NN, o ponto testado serve para medir as distâncias até os dados vizinhos e ver como fica a votação; nas árvores de decisão, o caminho desenhado mostra as condições testadas; e no k-means os centroides agem como pontos de referência que se movem e refazem os grupos, tendo papel ativo no cálculo e não apenas ilustrativo.""",

    # Bloco 4
    """- As tarefas propostas baseiam-se no método de prever, observar e explicar desenvolvido por White e Gunstone (1992): antes de mexer em qualquer botão de ajuste, o aluno anota ou fala o que acha que vai acontecer e, logo depois de usar o controle, observa na tela como o valor calculado e a decisão mudaram para dizer se o teste confirmou ou não sua ideia inicial, o que impede que a turma fique mexendo nos botões de forma aleatória por tentativa e erro sem ligar a entrada à resposta.
- Pedir essa previsão antes do teste ajuda a colocar para fora ideias que o aluno tinha guardadas sem perceber: por exemplo, se ele acha que subir a quantidade de vizinhos no k-NN não vai mudar a classe escolhida, mas o gráfico mostra outra decisão, o professor pode questionar quais novos pontos entraram na conta e por que o placar da votação virou.
- Do mesmo modo, se o estudante imagina que mudar o lugar de um centroide no k-means não fará diferença e vê os pontos trocarem de grupo na tela, a conversa permite reforçar o conceito de distância e proximidade, mostrando que a hipótese inicial do aluno gera aprendizado mesmo quando ele erra o palpite.""",

    # Bloco 5
    """- As aulas estão planejadas para acontecer no laboratório de informática do colégio com conexão à internet, dependendo apenas de confirmar a estrutura disponível no local; a ideia é que cada aluno utilize um computador da sala ou um Chromebook (conforme o que a escola tiver disponível), fazendo todas as tarefas durante o horário dos encontros para evitar que a falta de computador ou internet em casa prejudique alguém.
- Para ajudar os estudantes que têm pouca prática ou receio ao usar o computador, os botões e ajustes da tela serão fáceis de ler e indicarão claramente o que pode ser alterado em cada etapa da tarefa.
- Já para os alunos que mexem no computador com rapidez e facilidade, o foco da tarefa deixa de ser operar a tela rapidamente e passa a ser justificar conceitualmente os resultados, cabendo ao professor mediador dar apoio individual quando preciso para que o uso da tecnologia não vire uma barreira nem esconda o conceito que está sendo ensinado.""",

    # Bloco 6
    """- Os botões interativos da plataforma não serão usados como mero enfeite visual nem como uma brincadeira livre deixada para o fim de uma aula expositiva pronta: a função deles é permitir que o aluno compare os efeitos na tela mantendo a maioria dos elementos fixos enquanto altera apenas um valor ou parâmetro de cada vez.
- Durante a etapa conduzida junto com o professor, a orientação inicial é mudar somente uma variável por vez, porque mexer em vários controles ao mesmo tempo atrapalha o estudante na hora de descobrir exatamente qual ajuste causou aquela mudança no gráfico.
- Após essa primeira etapa orientada, os estudantes terão um momento de teste livre para fazer novas comparações na tela, momento em que o professor deverá relembrar o objetivo da atividade e pedir que a turma explique o porquê dos resultados, em vez de apenas relatar o que apareceu desenhado.""",

    # Bloco 7
    """- Os conteúdos matemáticos serão introduzidos aos poucos, em níveis graduais (em camadas): a aula começa com um problema prático e com a leitura de tabelas e gráficos simples, avança para contas básicas e só no final apresenta a expressão algébrica que resume a regra estudada, fazendo com que a equação da reta, a linha da fronteira, a conta de distância, as regras de condição ou a média dos centroides sirvam para explicar o que mudou visualmente na tela, sem obrigar ninguém a decorar fórmulas soltas.
- Trabalhar a Matemática por etapas não diminui o rigor dos conceitos, mas organiza o que o aluno realmente precisa entender primeiro para que cada cálculo faça sentido no momento certo.
- Assim, antes de aplicar a fórmula da distância entre dois pontos, a turma precisa perceber na prática por que estar perto ou longe importa para o k-NN, e antes de falar sobre o erro de ajuste de uma reta, precisa comparar um valor previsto com um dado real; quando a fórmula entra depois dessa vivência visual no gráfico, ela passa a ter utilidade clara porque dá nome a uma relação que o próprio estudante já enxergou funcionando.""",
]


def main() -> None:
    generated_paras = []
    for i, top in enumerate(TOPICS_BLOCKS, 1):
        ka = "0s" if i == len(TOPICS_BLOCKS) else "5m"
        t0 = time.time()
        print(f"Gerando Bloco {i}/{len(TOPICS_BLOCKS)} da Seção 3.3...", flush=True)
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
    print(f"\n=== AUDITORIA FINAL SEÇÃO 3.3: {high_s}/{total_s} frases >65% similares ===", flush=True)


if __name__ == "__main__":
    main()
