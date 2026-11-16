#!/usr/bin/env python3
"""Rodada 7 cirúrgica apenas para Bloco 1, Bloco 3 e Bloco 4 da Seção 4.1
(Bloco 2A e 2B já têm vencedores em B2A_a e B2B_a) visando 4g_top baixo,
tempo presente/futuro, zero vazamentos e cadência natural do Autor 1."""
import difflib
import re
import time
from pathlib import Path
from gerar_secao_4_1_v5 import (
    FORBIDDEN_PATTERNS,
    ask_raw,
    sentence_audit,
)
from gerar_secao_4_1_v5_r6 import ORIG_5, fourgram_overlap

CANDIDATES_R7 = [
    (
        "B1_c",
        0,
        """- Pensando na realidade de conectividade limitada nas escolas, o produto educacional junta uma página interativa em português brasileiro e uma sequência didática voltada ao Ensino Médio.
- Os alunos acessam os cenários sintéticos diretamente no navegador e todos os cálculos rodam localmente no computador, sem cadastro de usuário, sem envio de respostas e sem coleta de dados pessoais.
- Basta abrir a plataforma nos computadores da sala ou no projetor para apoiar a mediação do professor de Computação, garantindo tempo para explicação e diálogo com a turma.""",
    ),
    (
        "B1_d",
        0,
        """- A proposta educa com uma plataforma interativa em português brasileiro ligada a uma sequência didática de Ensino Médio, feita para funcionar bem mesmo quando a internet da escola é restrita.
- Como tudo roda no próprio navegador sobre dados sintéticos e cálculos locais na máquina, ninguém cria conta nem envia respostas ou dados pessoais.
- Esse formato prático facilita abrir o sistema no projetor ou nos computadores da turma, ajudando o docente de Computação a conduzir explicações e conversas em aula.""",
    ),
    (
        "B3_c",
        3,
        """- Para não parecerem atividades soltas dentro do mesmo endereço, os cinco modelos conectam-se por perguntas que voltam em cada aula da plataforma.
- Antes de mexer nos ajustes para ver o que muda no gráfico, a turma precisa identificar de onde vêm os dados mostrados e qual tipo de saída espera obter.
- A resposta gerada varia bastante em sala: a reta entrega uma previsão numérica, enquanto a SVM traça uma fronteira que separa os casos rotulados; já o k-NN olha exemplos próximos, a árvore segue regras condicionais e o k-means reorganiza os pontos mesmo sem haver categorias prévias.""",
    ),
    (
        "B3_d",
        3,
        """- O que liga os modelos na plataforma não é apenas dividirem a mesma página, mas responderem sempre a perguntas parecidas ao longo do percurso.
- Primeiro os estudantes observam a origem do dado disponível e o resultado esperado, e só depois testam qual ajuste altera esse comportamento.
- Cada modelo devolve uma saída distinta nessa prática: previsão numérica pela reta, fronteira divisória de exemplos rotulados na SVM, consulta a casos vizinhos no k-NN, caminho por condições na árvore de decisão e reagrupamento no k-means na ausência de categorias prévias.""",
    ),
    (
        "B4_c",
        4,
        """- Quando essas mesmas perguntas guiam todos os módulos, os estudantes conseguem comparar os modelos sem decorá-los como uma simples relação de nomes.
- Ao acompanhar as respostas da turma, o professor nota rapidamente se a dúvida surge de um conceito específico ou se decorre de dificuldade mais ampla na leitura de dados e gráficos.
- A Figura 1 exibe a tela inicial do sistema desenvolvido para o Ensino Médio, onde aparecem juntos o roteiro das aulas, os módulos interativos e os materiais de apoio que serão utilizados ao longo da sequência.""",
    ),
    (
        "B4_d",
        4,
        """- Manter perguntas semelhantes em toda a sequência leva o aluno a enxergar diferenças reais entre as abordagens, evitando transformar os algoritmos em nomes soltos.
- Essa rotina também revela ao docente se o obstáculo está em determinado tópico matemático ou na leitura geral de gráficos e dados que atravessa os cinco módulos.
- Conforme mostra a Figura 1, a página principal da plataforma concentra em um só lugar os módulos, os materiais de apoio e o caminho das aulas previstas para os participantes.""",
    ),
]


def main() -> None:
    results = []
    for i, (name, orig_idx, top) in enumerate(CANDIDATES_R7, 1):
        ka = "0s" if i == len(CANDIDATES_R7) else "5m"
        t0 = time.time()
        out = ask_raw(top, temp=0.68, keep_alive=ka)
        t_clean = re.sub(r"(?m)^-\s*", "", top).replace("\n", " ")
        topic_sim = difflib.SequenceMatcher(None, t_clean, out).ratio()
        ng4 = fourgram_overlap(t_clean, out)
        copied, total_s, worst_s = sentence_audit(ORIG_5[orig_idx], out)
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

    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_1_v5_r7.txt")
    out_path.write_text(
        "\n\n".join(f"{h}\n{o}" for _, h, o in results) + "\n",
        encoding="utf-8",
    )
    print(f"\nSalvo em {out_path}", flush=True)


if __name__ == "__main__":
    main()
