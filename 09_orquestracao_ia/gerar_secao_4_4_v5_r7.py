#!/usr/bin/env python3
"""Rodada 7 cirúrgica da Seção 4.4 exclusivamente para B11 e B12."""
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
from gerar_secao_4_4_v5_p2 import ORIG_BLOCKS_4_4_P2

TOPICS_4_4_R7 = [
    (
        "B11_r6",
        "B11",
        """- O roteiro preliminar dos oito encontros articula objetivos de aprendizagem e duração prevista às ações de mediação docente e questões formativas, indicando também adaptações de infraestrutura escolar e limites didáticos próprios de cada módulo.
- Como a plataforma não armazena nenhuma resposta digitada no navegador, o corpus desta pesquisa reunirá, além das anotações do professor e dos três registros individuais intermediários de aula, o diagnóstico inicial e o instrumento avaliativo final completo.""",
    ),
    (
        "B12_r6",
        "B12",
        """- Antes do início das atividades na escola, o pesquisador conferirá a versão do site usada no campo frente a tudo o que está descrito nos roteiros da sequência didática.
- Se aparecer qualquer divergência nos conjuntos de dados, nos textos de apoio ou nas representações matemáticas da plataforma em relação ao plano de aula, o pesquisador corrigirá a plataforma ou explicará a diferença à turma.
- Essa conferência prática evitará que a pesquisa analise os estudantes como se tivessem vivenciado outro recurso, assegurando que a plataforma e os instrumentos avaliem exatamente o que foi trabalhado em sala.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_4_v5_r7.txt")
    results = []
    for name, orig_key, top in TOPICS_4_4_R7:
        orig_txt = ORIG_BLOCKS_4_4_P2[orig_key]
        t0 = time.time()
        out = ask_raw(top, temp=0.67, keep_alive="5m")
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
