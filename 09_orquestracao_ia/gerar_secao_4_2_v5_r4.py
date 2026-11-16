#!/usr/bin/env python3
"""Rodada 4 cirúrgica apenas para o Bloco 2 da Seção 4.2 (parágrafo das Figuras 2a e 2b),
separando explicitamente k-NN, árvore de decisão e k-means sem fusão conceitual e com baixo 4g_top."""
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
from gerar_secao_4_2_v5 import ORIG_4_2

CANDIDATES_4_2_R4 = [
    (
        "B2_r4a",
        1,
        """- Quando a inclinação da reta muda, o estudante confronta o número previsto com o dado medido; na SVM, aproximar a fronteira de uma classe traz à tona a redução da margem.
- O mesmo raciocínio aparece ao variar o total de vizinhos no k-NN, alterar condições na árvore de decisão ou mover centroides no k-means.
- As Figuras 2a e 2b retratam dois desses módulos em uso na tela: enquanto a Figura 2a trabalha a previsão numérica pela reta, a Figura 2b apresenta a fronteira que separa exemplos rotulados.
- Nas duas atividades ilustradas, pede-se que o aluno antecipe o resultado antes de ajustar os comandos e explique o que observou ao terminar.""",
    ),
    (
        "B2_r4b",
        1,
        """- Alterar a inclinação da reta leva a turma a cotejar o valor previsto com o observado, ao passo que empurrar a fronteira junto a uma classe na SVM evidencia a diminuição da margem.
- Lógica equivalente orienta as mudanças nos vizinhos do k-NN, nas divisões da árvore de decisão e na localização dos centroides no k-means.
- Dois módulos abertos na plataforma aparecem nas Figuras 2a e 2b: o primeiro organiza a previsão numérica por meio da reta e o segundo destaca a separação de casos rotulados por uma fronteira.
- Tanto em uma figura quanto na outra, os estudantes formulam uma hipótese antes do ajuste no controle e explicam depois o efeito visto.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_2_v5_r4.txt")
    results = []
    for i, (name, orig_idx, top) in enumerate(CANDIDATES_4_2_R4, 1):
        ka = "0s" if i == len(CANDIDATES_4_2_R4) else "5m"
        t0 = time.time()
        out = ask_raw(top, temp=0.68, keep_alive=ka)
        t_clean = re.sub(r"(?m)^-\s*", "", top).replace("\n", " ")
        topic_sim = difflib.SequenceMatcher(None, t_clean, out).ratio()
        ng4 = fourgram_overlap(t_clean, out)
        copied, total_s, worst_s = sentence_audit(ORIG_4_2[orig_idx], out)
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
