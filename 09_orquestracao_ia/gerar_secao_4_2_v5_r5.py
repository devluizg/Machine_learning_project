#!/usr/bin/env python3
"""Rodada 5: divide Bloco 2 da Seção 4.2 em 2A (linha 29: manipulações nos modelos)
e 2B (linha 31: Figuras 2a e 2b) para manter cadência Autor 1 natural e zero omissões."""
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

ORIG_29 = (
    "Mover a inclinação da reta leva o estudante a comparar a previsão com o valor observado, "
    "enquanto aproximar uma fronteira de uma classe permite discutir a redução da margem na SVM. "
    "A mesma lógica orienta o ajuste de vizinhos ou de divisões da árvore, assim como a posição "
    "dos centroides."
)

ORIG_31 = (
    "As Figuras 2a e 2b mostram dois módulos em uso. A primeira tela organiza a previsão numérica "
    "por meio da reta; a segunda mostra a fronteira que separa exemplos rotulados. Em ambas, a "
    "ação proposta solicita uma previsão antes da alteração do controle e uma explicação depois da "
    "exploração."
)

CANDIDATES_4_2_R5 = [
    (
        "B2A_a",
        ORIG_29,
        """- Quando muda a inclinação da reta na tela, o aluno confronta o valor calculado com o dado medido na atividade.
- Na SVM, empurrar a fronteira para perto de um grupo possibilita discutir com a turma por que a margem diminui.
- O mesmo modo de raciocinar acompanha o ajuste da quantidade de vizinhos no k-NN, as quebras condicionais da árvore de decisão e o lugar onde ficam os centroides no k-means.""",
    ),
    (
        "B2A_b",
        ORIG_29,
        """- Deslocar a inclinação da reta permite comparar a estimativa gerada com o número observado nos exemplos.
- De forma parecida, trazer a fronteira para junto de uma classe abre debate sobre o estreitamento da margem na SVM.
- Essa lógica permanece quando os estudantes alteram quantos vizinhos o k-NN considera, mudam as regras de corte da árvore ou reposicionam centroides no k-means.""",
    ),
    (
        "B2B_a",
        ORIG_31,
        """- Para ilustrar o uso prático na plataforma, as Figuras 2a e 2b trazem dois módulos abertos em atividade.
- Na primeira interface o estudante trabalha a estimativa numérica apoiada na reta, e na segunda visualiza a divisa que separa casos já rotulados.
- Em qualquer uma das duas telas, a tarefa exige que o aluno preveja o comportamento antes de tocar no controle e justifique depois o que observou na prática.""",
    ),
    (
        "B2B_b",
        ORIG_31,
        """- O funcionamento desse percurso aparece exemplificado nas Figuras 2a e 2b por meio de dois módulos da plataforma.
- Enquanto a Figura 2a mostra a tela voltada ao cálculo numérico com base na reta, a Figura 2b exibe a linha de separação entre exemplos com rótulo.
- Nos dois ambientes apresentados, solicita-se primeiro uma previsão antes de mexer nos ajustes e, após explorar o modelo, uma explicação do resultado.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_2_v5_r5.txt")
    results = []
    for i, (name, orig_txt, top) in enumerate(CANDIDATES_4_2_R5, 1):
        ka = "0s" if i == len(CANDIDATES_4_2_R5) else "5m"
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
