#!/usr/bin/env python3
"""Rodada 6 rápida apenas para Bloco 2A da Seção 4.2 buscando menor colagem ao tópico
(<0.65 topic_sim e <25 4g_top) sem alucinar termos de hiperparâmetro."""
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
from gerar_secao_4_2_v5_r5 import ORIG_29

CANDIDATES_4_2_R6 = [
    (
        "B2A_c",
        ORIG_29,
        """- Quando mexe na reta inclinando seu ângulo, a turma enxerga logo a diferença entre o valor calculado e o dado real.
- Na tela da SVM, puxar a fronteira até perto dos exemplos de uma classe ajuda o professor a debater por que a margem encolhe.
- A mesma ideia de investigar causa e efeito vale quando os alunos trocam os vizinhos no k-NN, ajustam divisões da árvore ou mudam centroides de lugar no k-means.""",
    ),
    (
        "B2A_d",
        ORIG_29,
        """- Cada manipulação visual provoca perguntas diretas: inclinar a reta coloca em confronto previsão e dado observado, ao passo que empurrar a linha da SVM junto a uma classe mostra a margem diminuir.
- Igual cuidado conceitual rege os ajustes no número de vizinhos do k-NN, nas regras da árvore de decisão e na posição dos centroides do k-means.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_2_v5_r6.txt")
    results = []
    for i, (name, orig_txt, top) in enumerate(CANDIDATES_4_2_R6, 1):
        ka = "0s" if i == len(CANDIDATES_4_2_R6) else "5m"
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
