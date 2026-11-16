#!/usr/bin/env python3
"""Gera candidatos (a/b) para os 3 blocos da Seção 4.3 (Cenários e dados dos experimentos)
no luiz-academico v5.0 (temperature=0.68), com salvamento incremental e auditoria contra capitulo4.tex."""
import difflib
import re
import time
from pathlib import Path
from gerar_secao_4_1_v5 import (
    FORBIDDEN_PATTERNS,
    ask_raw,
    sentence_audit,
)
from gerar_secao_4_1_v5_r6 import fourgram_overlap

ORIG_54 = (
    "Os dados das atividades serão quase todos sintéticos. No segundo encontro, a turma poderá "
    "montar uma pequena tabela anônima com informações simples e voluntárias, ou mesmo medir "
    "objetos da sala. Essa tabela servirá apenas ao ensino, ficando fora do corpus. Os demais "
    "cenários descartam o uso de notas escolares, registros de comportamento ou qualquer dado "
    "pessoal dos estudantes."
)

ORIG_56A = (
    "Os cenários foram definidos para a turma prevista e poderão receber ajustes pontuais após "
    "a conferência das condições de aplicação. Para a regressão linear, a ideia é relacionar "
    "número de passos e distância percorrida, enquanto a SVM usará medidas simuladas de sementes "
    "na separação de duas classes. Já o k-NN classificará alimentos fictícios segundo a doçura e "
    "a acidez, mesmo par de medidas retomado depois pelo k-means para formar grupos sem categorias "
    "prévias, ao passo que a árvore de decisão organizará objetos por largura e altura."
)

ORIG_56B = (
    "Cada contexto deve tornar visível o efeito de alterar dados ou parâmetros com a Matemática "
    "da série. Antes da aplicação, os exemplos serão revistos para adequar a linguagem e o tempo "
    "previsto à turma."
)

CANDIDATES_4_3 = [
    (
        "B1_a",
        ORIG_54,
        """- Praticamente todo o conjunto de informações usado nas atividades práticas será gerado de forma sintética na plataforma.
- Apenas no segundo encontro cogita-se construir em grupo uma tabela simples e anônima com informações voluntárias dos jovens ou medições de objetos presentes na própria sala.
- Esse levantamento pontual apoiará exclusivamente o ensino em aula e ficará fora do material analisado na pesquisa.
- Em todos os outros cenários descarta-se recorrer a notas escolares, registros de comportamento ou quaisquer dados pessoais dos estudantes.""",
    ),
    (
        "B1_b",
        ORIG_54,
        """- Os dados trabalhados nos experimentos em aula serão quase todos artificiais para resguardar os participantes.
- Como possibilidade pontual na segunda aula, os estudantes poderão preencher em turma um quadro anônimo com informações voluntárias simples ou medir objetos da sala.
- Essa tabela atenderá apenas à atividade pedagógica daquele momento, permanecendo fora do material recolhido para análise da pesquisa.
- Os demais cenários descartam qualquer uso de boletins de notas, registros disciplinares de conduta ou informações pessoais dos alunos.""",
    ),
    (
        "B2_a",
        ORIG_56A,
        """- As situações propostas foram pensadas para a turma prevista, podendo passar por pequenos acertos depois que forem conferidas as condições reais de aplicação.
- Os primeiros módulos trazem contextos simples: passos dados ligados à distância caminhada na regressão linear e medidas simuladas de sementes divididas em duas classes na SVM.
- Nos demais cenários, alimentos fictícios descritos por doçura e acidez servem para o k-NN classificar e depois para o k-means criar grupos sem rótulos anteriores, enquanto objetos com largura e altura organizam a árvore de decisão.""",
    ),
    (
        "B2_b",
        ORIG_56A,
        """- Definidos para a turma esperada, os casos práticos admitem ajustes pontuais após a checagem das condições escolares de realização.
- Na regressão linear trabalha-se a relação entre número de passos e distância percorrida, enquanto na SVM duas classes se separam usando dimensões simuladas de sementes.
- O k-NN classifica comidas imaginárias pela doçura e pela acidez — mesmo par retomado adiante pelo k-means para agrupar sem categorias prévias — e a árvore de decisão organiza objetos segundo largura e altura.""",
    ),
    (
        "B3_a",
        ORIG_56B,
        """- Todos esses contextos buscam deixar evidente na tela de que modo mudar dados ou parâmetros altera o resultado usando a Matemática correspondente à série dos estudantes.
- Antes do início dos encontros em sala, os exemplos preparados passarão por revisão para tornar a linguagem acessível à turma.
- Essa conferência prévia também verificará se a exploração cabe adequadamente no tempo reservado para cada atividade.""",
    ),
    (
        "B3_b",
        ORIG_56B,
        """- Em cada contexto escolhido, pretende-se mostrar com clareza o efeito de alterar dados ou parâmetros empregando recursos matemáticos compatíveis com a série escolar.
- Antes de levar as tarefas para a sala, os exemplos serão revistos para ajustar o vocabulário utilizado às características da turma.
- Tal revisão anterior à aplicação confirma igualmente se o ritmo das propostas se ajusta ao tempo previsto das aulas.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_3_v5.txt")
    results = []
    for i, (name, orig_txt, top) in enumerate(CANDIDATES_4_3, 1):
        ka = "0s" if i == len(CANDIDATES_4_3) else "5m"
        t0 = time.time()
        out = ask_raw(top, temp=0.68, keep_alive=ka)
        t_clean = re.sub(r"(?m)^-\s*", "", top).replace("\n", " ")
        topic_sim = difflib.SequenceMatcher(None, t_clean, out).ratio()
        ng4 = fourgram_overlap(t_clean, out)
        copied, total_s, worst_s = sentence_audit(orig_txt, out)
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
        out_path.write_text(
            "\n\n".join(f"{h}\n{o}" for _, h, o in results) + "\n",
            encoding="utf-8",
        )
    print(f"\nSalvo em {out_path}", flush=True)


if __name__ == "__main__":
    main()
