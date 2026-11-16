#!/usr/bin/env python3
"""Gera os 2 blocos da Seção 4.6 (Alinhamento curricular preliminar) no luiz-academico v5.0 (temp=0.67)."""
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

ORIG_BLOCKS_4_6 = {
    "B1": (
        "Uma matriz explicitará o vínculo da sequência com a Computação na Educação Básica, "
        "associando cada habilidade curricular ao seu objetivo de aprendizagem, bem como à "
        "atividade proposta e às evidências observáveis. A versão preliminar apoia-se nas "
        "referências do Ensino Médio voltadas aos fundamentos da inteligência artificial com "
        "suas potencialidades e limites, articulando a análise em ciência de dados ao uso de "
        "modelos computacionais simples de simulação e previsão. Esse recorte dialoga com as "
        "habilidades EM13CO10 a EM13CO12 previstas no anexo da Resolução CNE/CEB nº 1/2022."
    ),
    "B2": (
        "Embora a norma deixe de prescrever esses cinco algoritmos nominalmente, eles oferecem "
        "situações didáticas concretas para examinar os limites de cada regra na transformação de "
        "dados em resultados. A matriz indicará ainda conexões com a Matemática, mantendo a "
        "Computação como objeto principal. O recorte definitivo das habilidades dependerá da "
        "série e da disciplina definidas, respeitando o currículo da rede estadual e as condições "
        "do campo."
    ),
}

TOPICS_4_6 = [
    (
        "B1",
        """- Uma matriz curricular detalhará a ligação da sequência didática com a Computação na Educação Básica, conectando cada habilidade prevista aos objetivos de aprendizagem correspondentes, às atividades de aula e às evidências observáveis.
- Em sua versão preliminar, esse mapeamento apoia-se nas orientações para o Ensino Médio relativas aos fundamentos da inteligência artificial, destacando potencialidades e limites ao articular ciência de dados com modelos computacionais simples de simulação e previsão.
- Tal escolha dialoga com as habilidades EM13CO10 a EM13CO12 presentes no anexo da Resolução CNE/CEB nº 1/2022 (Brasil, 2022).""",
    ),
    (
        "B2",
        """- Mesmo que o documento normativo não cite nominalmente os cinco algoritmos selecionados, eles fornecem situações de ensino concretas para investigar o alcance de cada regra quando converte dados em saídas.
- A matriz apontará também articulações possíveis com conteúdos de Matemática, preservando entretanto a Computação como foco central da proposta.
- A seleção final das habilidades ficará condicionada à definição da série e da disciplina no campo, acompanhando as diretrizes curriculares da rede estadual e a realidade da escola.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_6_v5.txt")
    results = []
    for i, (name, top) in enumerate(TOPICS_4_6, 1):
        orig_txt = ORIG_BLOCKS_4_6[name]
        ka = "0s" if i == len(TOPICS_4_6) else "5m"
        t0 = time.time()
        out = ask_raw(top, temp=0.67, keep_alive=ka)
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
