#!/usr/bin/env python3
"""Rodada 4 para Seção 4.3 no luiz-academico v5.0: garante cobertura integral de
ORIG_54 (sem omitir descarte de notas/comportamento/dados pessoais) e ORIG_56B
(futuro/presente em 3ª pessoa, com Matemática da série e revisão de linguagem/tempo)."""
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
from gerar_secao_4_3_v5 import ORIG_54, ORIG_56A, ORIG_56B

CANDIDATES_4_3_R4 = [
    (
        "B1_g",
        ORIG_54,
        """- Quase toda a base usada nos experimentos será sintética, sem qualquer aproveitamento de boletins de notas, anotações disciplinares de conduta ou informações pessoais dos estudantes.
- Como exceção pontual na segunda aula, os jovens poderão construir juntos uma tabela anônima com dados simples e voluntários, ou então medir objetos presentes na sala.
- Esse levantamento específico apoiará unicamente a explicação didática em sala e não integrará o corpus da pesquisa.""",
    ),
    (
        "B1_h",
        ORIG_54,
        """- Os conjuntos de dados empregados nas tarefas da plataforma serão praticamente todos gerados de modo artificial.
- Na segunda aula, entretanto, a turma poderá montar uma pequena tabela anônima com informações simples cedidas voluntariamente ou aferir dimensões de objetos da sala, recurso restrito ao ensino que permanecerá fora do corpus analisado.
- Em nenhuma outra atividade entram notas escolares, registros comportamentais ou quaisquer dados pessoais dos discentes.""",
    ),
    (
        "B2_e",
        ORIG_56A,
        """- Pensados inicialmente para a turma prevista, os contextos práticos poderão receber ajustes pontuais depois que o pesquisador conferir as condições concretas de aplicação na escola.
- Nos primeiros módulos, a regressão linear relaciona contagem de passos e distância caminhada, ao passo que a SVM utiliza dimensões simuladas de sementes para distinguir duas classes.
- Na sequência, o k-NN classifica alimentos fictícios a partir de doçura e acidez, o k-means retoma esse mesmo par de atributos para agrupar sem categorias anteriores e a árvore de decisão organiza objetos segundo largura e altura.""",
    ),
    (
        "B3_g",
        ORIG_56B,
        """- Cada situação escolhida precisa tornar evidente ao estudante como a alteração nos dados ou nos parâmetros modifica a saída do modelo, apoiando-se nos conceitos matemáticos da própria série escolar.
- Antes de levar a sequência à sala de aula, os exemplos preparados passarão por uma checagem prévia por parte do docente.
- Essa conferência anterior ao campo ajustará a clareza da linguagem dos enunciados e verificará se a duração prevista cabe confortavelmente no horário da turma.""",
    ),
    (
        "B3_h",
        ORIG_56B,
        """- Todos os contextos experimentais procuram evidenciar de forma clara na interface o impacto de variar entradas ou parâmetros, mobilizando a Matemática correspondente ao ano letivo dos alunos.
- Previamente à intervenção escolar, todo o conjunto de exemplos receberá uma revisão cuidadosa.
- O objetivo dessa conferência prévia é adequar o vocabulário das atividades e calibrar o tempo previsto de exploração às características reais da turma.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_3_v5_r4.txt")
    results = []
    for i, (name, orig_txt, top) in enumerate(CANDIDATES_4_3_R4, 1):
        ka = "0s" if i == len(CANDIDATES_4_3_R4) else "5m"
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
