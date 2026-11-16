#!/usr/bin/env python3
"""Rodada 3 cirúrgica para Bloco 1 e Bloco 3 da Seção 4.3 (Bloco 2 já tem B2_c fiel),
mantendo futuro/presente em 3ª pessoa, zero omissões e tamanho >= 300w na seção."""
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
from gerar_secao_4_3_v5 import ORIG_54, ORIG_56B

CANDIDATES_4_3_R3 = [
    (
        "B1_e",
        ORIG_54,
        """- Os dados empregados nas tarefas da plataforma serão quase integralmente sintéticos.
- Apenas na segunda aula a turma poderá organizar uma tabela anônima com informações simples cedidas voluntariamente ou medir objetos presentes na sala, material que apoiará somente o ensino sem entrar no corpus da pesquisa.
- Em todos os outros cenários permanecerão descartadas notas escolares, anotações disciplinares ou quaisquer dados pessoais dos alunos.""",
    ),
    (
        "B1_f",
        ORIG_54,
        """- Na maior parte das atividades, os experimentos trabalharão exclusivamente com conjuntos sintéticos de dados.
- Como única exceção prevista para o segundo encontro, os estudantes poderão preencher um quadro anônimo com dados simples e voluntários ou aferir medidas de objetos da sala, servindo esse registro apenas à condução didática fora do corpus pesquisado.
- Nos demais cenários ficarão de fora boletins de notas, registros de conduta e qualquer dado pessoal da turma.""",
    ),
    (
        "B3_e",
        ORIG_56B,
        """- Os contextos escolhidos precisam tornar visível na tela o efeito de mexer em dados ou parâmetros, dialogando sempre com os conteúdos matemáticos da série.
- Para evitar barreiras de compreensão ou falta de tempo durante as atividades, todos os exemplos passarão por uma revisão cuidadosa antes do início das aulas.
- Essa etapa preparatória ajustará a linguagem dos enunciados ao vocabulário da turma e verificará se a exploração cabe no tempo planejado.""",
    ),
    (
        "B3_f",
        ORIG_56B,
        """- Cada situação experimental procura mostrar concretamente de que forma alterações nos dados ou parâmetros modificam a saída por meio da Matemática correspondente à série cursada.
- Antes que a intervenção aconteça na escola, os conjuntos de exemplos serão revistos pelo pesquisador.
- Com essa conferência anterior à aplicação, busca-se adequar tanto a linguagem das propostas quanto a duração prevista às condições reais da turma.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_3_v5_r3.txt")
    results = []
    for i, (name, orig_txt, top) in enumerate(CANDIDATES_4_3_R3, 1):
        ka = "0s" if i == len(CANDIDATES_4_3_R3) else "5m"
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
