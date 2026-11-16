#!/usr/bin/env python3
"""Rodada 6 para Seção 4.1 (5 blocos naturais, temperature=0.65 estilo 3.4/3.5):
separa os 5 algoritmos em Bloco 2A (visão geral) e Bloco 2B (camadas matemáticas + formalização)
para eliminar definições rígidas tipo dicionário sinalizadas no GPTZero."""
import difflib
import re
import time
from pathlib import Path
from gerar_secao_4_1_v5 import (
    FORBIDDEN_PATTERNS,
    ask_raw,
    sentence_audit,
)

ORIG_5 = [
    (
        "O produto educacional une uma plataforma interativa em português brasileiro a uma "
        "sequência didática para o Ensino Médio. A plataforma roda direto no navegador com "
        "cenários sintéticos, executando todos os cálculos no próprio computador. Seu acesso "
        "dispensa criação de conta ou cadastro de usuário, operando sem envio de respostas ou "
        "coleta de dados pessoais. Isso facilita o uso mesmo sob conectividade limitada, "
        "bastando abrir o recurso nos computadores ou no projetor. A ferramenta apoia a "
        "mediação docente em Computação, preservando o espaço da explicação e do diálogo "
        "conduzidos pelo professor."
    ),
    (
        "A proposta tem cinco módulos introdutórios de machine learning: regressão linear, "
        "máquina de vetores de suporte (SVM), k-vizinhos mais próximos, árvore de decisão e "
        "k-means. Longe de formarem um catálogo de comandos ou conteúdos soltos, eles "
        "apresentam tarefas distintas de previsão numérica e classificação, além da formação "
        "de grupos para que a turma compare o que muda entre eles. Todos ocupam lugar central "
        "na sequência, mobilizando camadas matemáticas próprias."
    ),
    (
        "Na regressão linear, o estudo da função e da linha de tendência fundamenta a previsão "
        "e o cálculo de resíduos ou erros, enquanto a SVM separa classes por uma fronteira com "
        "sua margem. Já o k-NN destaca a distância entre pontos, o k-means recalcula centroides "
        "pela média e a árvore encadeia condições. A diferença de formalização não diminui nenhum "
        "módulo. Ela decorre do repertório de estudantes iniciantes e da necessidade de tornar "
        "visível, no gráfico ou na regra, uma relação que a turma consiga discutir durante a aula."
    ),
    (
        "Mais do que estarem na mesma plataforma, os modelos se conectam por perguntas recorrentes "
        "nos módulos. A turma identifica a origem do dado disponível e a saída esperada antes de "
        "testar qual ajuste pode alterá-la. A resposta varia em cada caso. Enquanto a reta gera "
        "uma previsão numérica, a SVM posiciona uma fronteira para separar exemplos rotulados. Por "
        "sua vez, o k-NN consulta exemplos próximos e a árvore percorre regras condicionais, ao "
        "passo que o k-means reorganiza pontos mesmo sem categorias prévias."
    ),
    (
        "Com as mesmas perguntas em cada módulo, os estudantes comparam os modelos sem reduzi-los "
        "a uma lista de nomes. O professor percebe se a dificuldade está em um conceito específico "
        "ou na leitura de dados e gráficos, que atravessa todos os módulos. A Figura 1 apresenta "
        "a tela inicial da plataforma. Ela reúne o percurso de aulas, os módulos e os materiais de "
        "apoio que serão utilizados na sequência."
    ),
]

CANDIDATES_R6 = [
    (
        "B1_a",
        0,
        """- O produto educacional do projeto combina uma plataforma interativa em português brasileiro com uma sequência didática voltada ao Ensino Médio.
- A ferramenta roda direto no navegador com cenários sintéticos e realiza todos os cálculos no computador do próprio aluno, dispensando criação de conta ou cadastro e evitando envio de respostas ou coleta de dados pessoais.
- Bastando abrir a página nos computadores ou no projetor, seu uso continua viável até com conectividade limitada e apoia a mediação docente em Computação sem tirar o espaço da explicação e do diálogo conduzidos pelo professor.""",
    ),
    (
        "B1_b",
        0,
        """- Este trabalho une uma sequência didática para o Ensino Médio a uma plataforma interativa construída em português brasileiro.
- Como todos os cálculos acontecem localmente no computador por meio de cenários sintéticos no navegador, ninguém precisa fazer login nem cadastrar conta, tampouco há transmissão de respostas ou coleta de informações pessoais.
- Por isso a aula flui mesmo quando a internet da escola é limitada, bastando acessar o site nos equipamentos da sala ou no projetor para fortalecer a mediação, a fala e o diálogo do professor de Computação.""",
    ),
    (
        "B2A_a",
        1,
        """- A proposta conta com cinco módulos introdutórios de machine learning, que são regressão linear, máquina de vetores de suporte (SVM), k-vizinhos mais próximos, árvore de decisão e k-means.
- Esses módulos não funcionam como um catálogo de comandos ou conteúdos soltos, porque colocam em confronto tarefas diferentes de previsão numérica, classificação e formação de grupos para a turma notar o que muda de uma para outra.
- Desse modo, todos os cinco módulos ocupam lugar central na sequência didática.""",
    ),
    (
        "B2A_b",
        1,
        """- Na parte de machine learning, a plataforma apresenta cinco módulos de iniciação: regressão linear, máquina de vetores de suporte (SVM), k-vizinhos mais próximos, árvore de decisão e k-means.
- Longe de reunir comandos decorados sem relação entre si, o desenho propõe tarefas de estimativa numérica, classificação e agrupamento para que os estudantes comparem seus comportamentos.
- Por essa razão, cada um dos cinco temas assume papel central ao longo das aulas.""",
    ),
    (
        "B2B_a",
        2,
        """- Cada módulo mobiliza camadas matemáticas próprias durante a aula: a regressão linear usa o estudo da função e da linha de tendência para embasar a previsão e o cálculo de erros ou resíduos, ao passo que a SVM separa as classes traçando uma fronteira com sua margem.
- Já nos demais modelos, o k-NN dá destaque à distância entre os pontos, o k-means recalcula seus centroides com base na média e a árvore de decisão vai encadeando condições.
- Embora o nível de formalização mude entre eles, isso não rebaixa nenhum módulo, pois acompanha o repertório de alunos iniciantes e busca tornar visível no gráfico ou na regra uma relação discutível em sala.""",
    ),
    (
        "B2B_b",
        2,
        """- As atividades exploram fundamentos matemáticos específicos em cada caso, indo da função e da linha de tendência com cálculo de resíduos ou erros na regressão linear até a divisão de classes por fronteira e margem na SVM.
- De modo complementar, o k-NN trabalha com a distância entre pontos, enquanto o k-means atualiza centroides pela média e a árvore encadeia condições lógicas.
- Diferenças no grau de rigor formal não diminuem nenhum dos módulos, já que respeitam o conhecimento prévio de jovens iniciantes e tornam clara no gráfico ou na regra a ideia debatida na turma.""",
    ),
    (
        "B3_a",
        3,
        """- Mais do que ficarem hospedados na mesma página, os modelos ligam-se por perguntas que retornam em todos os módulos, levando a turma a checar de onde vem o dado e que saída esperar antes de testar qual ajuste altera o resultado.
- A resposta obtida muda bastante de um algoritmo para outro: a reta produz uma previsão numérica e a SVM posiciona uma fronteira separando exemplos rotulados.
- Ao mesmo tempo, o k-NN consulta os exemplos próximos, a árvore percorre regras condicionais e o k-means reorganiza os pontos mesmo quando não existem categorias prévias.""",
    ),
    (
        "B3_b",
        3,
        """- Perguntas recorrentes atravessam os módulos para conectá-los além do espaço compartilhado na tela, pedindo aos estudantes que identifiquem a origem do dado e a saída esperada antes de mexer em qualquer ajuste.
- Cada abordagem devolve um tipo próprio de resposta durante essa exploração, pois a reta gera previsão numérica enquanto a SVM situa uma fronteira para dividir casos já rotulados.
- Nos outros três casos, o k-NN busca apoio em exemplos próximos, a árvore segue testes condicionais e o k-means reagrupa os pontos sem dispor de categorias anteriores.""",
    ),
    (
        "B4_a",
        4,
        """- Repetir as mesmas perguntas em todos os módulos permite que a turma compare os modelos sem transformá-los em uma lista decorada de nomes.
- Esse acompanhamento ajuda o professor a perceber se a dificuldade discente decorre de um conceito específico ou da leitura geral de dados e gráficos que atravessa toda a sequência.
- Para mostrar essa entrada da plataforma, a Figura 1 apresenta sua tela inicial com o percurso de aulas, os módulos e os materiais de apoio que serão utilizados na sequência.""",
    ),
    (
        "B4_b",
        4,
        """- Quando as mesmas questões reaparecem em cada módulo, os alunos comparam os modelos de modo conceitual e não como simples enumeração de termos técnicos.
- O docente também consegue notar se certo obstáculo está ligado a uma ideia pontual ou se vem de dificuldades na leitura de gráficos e dados presentes em todos os módulos.
- Conforme ilustra a Figura 1, a página inicial do sistema concentra a trilha das aulas, os cinco módulos e os materiais de apoio empregados pelos estudantes ao longo do percurso.""",
    ),
]


def fourgram_overlap(a: str, b: str) -> int:
    ta = re.findall(r"[a-zà-ú0-9-]+", a.lower())
    tb = re.findall(r"[a-zà-ú0-9-]+", b.lower())
    if len(ta) < 4 or len(tb) < 4:
        return 0
    sa = {tuple(ta[i : i + 4]) for i in range(len(ta) - 3)}
    sb = {tuple(tb[i : i + 4]) for i in range(len(tb) - 3)}
    return len(sa & sb)


def main() -> None:
    results = []
    for i, (name, orig_idx, top) in enumerate(CANDIDATES_R6, 1):
        ka = "0s" if i == len(CANDIDATES_R6) else "5m"
        t0 = time.time()
        out = ask_raw(top, temp=0.65, keep_alive=ka)
        t_clean = re.sub(r"(?m)^-\s*", "", top).replace("\n", " ")
        topic_sim = difflib.SequenceMatcher(None, t_clean, out).ratio()
        ng4 = fourgram_overlap(t_clean, out)
        copied, total_s, worst_s = sentence_audit(ORIG_5[orig_idx], out)
        leaks = [
            m.group(0)
            for pat in FORBIDDEN_PATTERNS
            for m in re.finditer(pat, out, flags=re.IGNORECASE)
        ]
        header = (
            f"=== {name} ({time.time()-t0:.1f}s | topic={len(t_clean.split())}w -> "
            f"out={len(out.split())}w | topic_sim={topic_sim:.2f} | 4g_top={ng4} | "
            f"orig>65%={copied}/{total_s} max_s={worst_s:.2f} | leaks={leaks}) ==="
        )
        print(f"\n{header}\n{out}", flush=True)
        results.append((name, header, out))

    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_1_v5_r6.txt")
    out_path.write_text(
        "\n\n".join(f"{h}\n{o}" for _, h, o in results) + "\n",
        encoding="utf-8",
    )
    print(f"\nSalvo em {out_path}", flush=True)


if __name__ == "__main__":
    main()
