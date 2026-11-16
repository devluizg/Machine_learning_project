#!/usr/bin/env python3
"""Rodada 6 cirúrgica da Seção 4.4 para os últimos 3 blocos (B9, B11, B12),
evitando numeração (i)/(ii)/(iii) em B11, garantindo futuro em B12 e preservação integral de B9."""
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

TOPICS_4_4_R6 = [
    (
        "B9_r6",
        "B9",
        """- A aula comparativa resgatará diferenças que possam ter ficado dispersas e preparará os estudantes para o desafio final, habituando a turma a examinar a finalidade da tarefa diante dos dados disponíveis antes de optar por um modelo.
- Ao final da sequência, o bloco equivalente ao diagnóstico permitirá acompanhar mudanças de entendimento em relação ao ponto de partida.
- O desafio inédito de transferência mostrará em paralelo como os conceitos são aplicados em novo contexto, servindo de evidência complementar sem equiparação direta com as questões mais simples.""",
    ),
    (
        "B11_r5",
        "B11",
        """- O planejamento preliminar das oito aulas ligará objetivos de aprendizagem e duração estimada à mediação com perguntas formativas, registrando ainda ajustes de infraestrutura e limites didáticos próprios de cada módulo.
- Como a plataforma não armazena nenhuma resposta digitada no navegador, o material empírico da investigação reunirá, além das anotações do professor e dos três registros individuais intermediários de aula, tanto o diagnóstico inicial quanto o instrumento avaliativo final completo.""",
    ),
    (
        "B12_r5",
        "B12",
        """- A versão da página web levada às aulas passará por checagem prévia frente aos roteiros da sequência didática antes do início do trabalho em campo.
- Caso haja qualquer diferença entre os dados, textos de apoio ou representações matemáticas exibidos no site e o plano de aula, o ponto será corrigido ou esclarecido aos estudantes.
- Essa verificação prática impedirá analisar os alunos como se tivessem passado por outro recurso, assegurando que a plataforma e os instrumentos avaliem exatamente o que foi trabalhado em sala.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_4_v5_r6.txt")
    results = []
    for i, (name, orig_key, top) in enumerate(TOPICS_4_4_R6, 1):
        orig_txt = ORIG_BLOCKS_4_4_P2[orig_key]
        ka = "0s" if i == len(TOPICS_4_4_R6) else "5m"
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
