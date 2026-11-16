#!/usr/bin/env python3
"""Terceira rodada cirúrgica apenas para Bloco 3 e Bloco 4 da Seção 4.1
no luiz-academico v5.0, corrigindo termos técnicos e eliminando vazamentos."""
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

CANDIDATES_R3 = [
    (
        "B3_v5",
        2,
        """- Os cinco módulos não ficam isolados na mesma página, pois se ligam por perguntas comuns que acompanham a turma em cada atividade.
- Antes de testar qual ajuste pode mudar o comportamento do modelo, os alunos verificam de onde vem o dado exibido e qual saída se espera obter.
- Conforme o tipo de tarefa, o retorno muda: a reta calcula um valor numérico previsto, a SVM posiciona uma fronteira que separa casos rotulados, o k-NN consulta vizinhos próximos, a árvore segue regras condicionais e o k-means reorganiza os pontos sem nenhuma categoria prévia.""",
    ),
    (
        "B3_v6",
        2,
        """- Mais do que estarem no mesmo endereço web, as atividades compartilham questões fixas que levam os jovens a checar a origem dos dados e a saída esperada antes de alterar qualquer controle.
- Como os algoritmos resolvem problemas distintos de previsão, classificação e agrupamento, cada um entrega uma resposta diferente.
- Assim, a reta gera uma estimativa numérica, a SVM divide exemplos rotulados com uma fronteira, o k-NN busca exemplos próximos, a árvore percorre condições em sequência e o k-means agrupa pontos operando sem rótulos prévios.""",
    ),
    (
        "B4_v5",
        3,
        """- Manter sempre o mesmo roteiro de perguntas faz os estudantes do Ensino Médio compararem os modelos sem tratá-los apenas como uma lista de nomes decorados.
- Esse acompanhamento ajuda o professor a perceber se eventual erro vem de um conceito específico ou da dificuldade de ler dados e gráficos presente nos cinco módulos.
- Ilustrando a entrada do sistema, a Figura 1 apresenta a tela inicial da plataforma, reunindo a trilha de aulas, os módulos interativos e os materiais de apoio previstos para a sequência didática.""",
    ),
    (
        "B4_v6",
        3,
        """- Responder às mesmas questões-guia ao longo dos cinco temas permite à turma confrontar as abordagens sem memorizar apenas nomes soltos.
- Ao mesmo tempo, o docente distingue com mais clareza quando o entrave está em uma noção matemática pontual ou na leitura geral de dados e gráficos exigida em toda a sequência.
- A Figura 1 mostra a tela inicial da plataforma web para o Ensino Médio, onde ficam reunidos o percurso das aulas, os módulos e os materiais de apoio que serão utilizados pelos participantes.""",
    ),
]


def main() -> None:
    results = []
    for i, (name, orig_idx, top) in enumerate(CANDIDATES_R3, 1):
        ka = "0s" if i == len(CANDIDATES_R3) else "5m"
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

    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_1_v5_r3.txt")
    out_path.write_text(
        "\n\n".join(f"{h}\n{o}" for _, h, o in results) + "\n",
        encoding="utf-8",
    )
    print(f"\nSalvo em {out_path}", flush=True)


if __name__ == "__main__":
    main()
