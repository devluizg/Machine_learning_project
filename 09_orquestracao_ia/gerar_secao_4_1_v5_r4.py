#!/usr/bin/env python3
"""Quarta rodada cirúrgica (B3_v7, B3_v8, B4_v7) para fechar Seção 4.1
sem duplicações, sem inversões semânticas e com menor similaridade no Bloco 4."""
import difflib
import re
import time
from pathlib import Path
from gerar_secao_4_1_v5 import (
    ORIG_PARAS,
    FORBIDDEN_PATTERNS,
    ask_raw,
    sentence_audit,
)

CANDIDATES_R4 = [
    (
        "B3_v7",
        2,
        """- Os cinco módulos vão além de dividir a mesma página, pois questões recorrentes ligam as atividades e levam a turma a identificar de onde vêm os dados e qual saída se espera antes de testar ajustes.
- As respostas mudam segundo o papel de cada técnica: a reta calcula uma previsão numérica, enquanto a SVM posiciona uma fronteira para separar exemplos rotulados.
- Nos demais casos, o k-NN consulta vizinhos próximos, a árvore percorre regras condicionais e o k-means reorganiza os pontos operando sem categorias prévias.""",
    ),
    (
        "B3_v8",
        2,
        """- Em vez de apenas coexistirem no site, os modelos dialogam por meio de perguntas repetidas que fazem os alunos checar a origem do dado e o resultado esperado antes de mexer nos controles.
- Cada modelo devolve uma saída própria durante os testes em aula.
- Enquanto a regressão entrega valores numéricos pela reta e a SVM define uma divisória entre casos rotulados, o k-NN busca pontos semelhantes, a árvore segue regras condicionais e o k-means reorganiza os dados na ausência de rótulos prévios.""",
    ),
    (
        "B4_v7",
        3,
        """- Trabalhar as mesmas perguntas em todos os módulos impede que os alunos reduzam os algoritmos a uma lista decorada de nomes.
- Ao mesmo tempo, o professor consegue distinguir se a dificuldade está em certo conceito ou na leitura de dados e gráficos exigida ao longo de toda a sequência.
- Para mostrar essa entrada inicial aos estudantes, a Figura 1 exibe a tela de abertura da plataforma, juntando os materiais de apoio, os módulos interativos e a trilha de aulas previstas na intervenção.""",
    ),
]


def main() -> None:
    results = []
    for i, (name, orig_idx, top) in enumerate(CANDIDATES_R4, 1):
        ka = "0s" if i == len(CANDIDATES_R4) else "5m"
        t0 = time.time()
        out = ask_raw(top, temp=0.68, keep_alive=ka)
        t_clean = re.sub(r"(?m)^-\s*", "", top).replace("\n", " ")
        topic_sim = difflib.SequenceMatcher(None, t_clean, out).ratio()
        copied, total_s, worst_s = sentence_audit(ORIG_PARAS[orig_idx], out)
        leaks = [
            m.group(0)
            for pat in FORBIDDEN_PATTERNS
            for m in re.finditer(pat, out, flags=re.IGNORECASE)
        ]
        header = (
            f"=== {name} ({time.time()-t0:.1f}s | topic={len(t_clean.split())}w -> "
            f"out={len(out.split())}w | topic_sim={topic_sim:.2f} | "
            f"orig>65%={copied}/{total_s} max_s={worst_s:.2f} | leaks={leaks}) ==="
        )
        print(f"\n{header}\n{out}", flush=True)
        results.append((name, header, out))

    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_1_v5_r4.txt")
    out_path.write_text(
        "\n\n".join(f"{h}\n{o}" for _, h, o in results) + "\n",
        encoding="utf-8",
    )
    print(f"\nSalvo em {out_path}", flush=True)


if __name__ == "__main__":
    main()
