#!/usr/bin/env python3
"""Rodada 8 para fechar B1, B3 e B4 da Seção 4.1 com cadência orgânica Autor 1
sem traduções erradas de siglas, sem tempo passado e com baixo 4g_top."""
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

CANDIDATES_R8 = [
    (
        "B1_e",
        0,
        """- Em escolas com acesso limitado à internet, a acessibilidade da plataforma torna-se ponto central ao unir um sistema interativo em português brasileiro a uma sequência didática para o Ensino Médio.
- Os estudantes abrem cenários sintéticos direto no navegador com cálculos feitos no próprio computador, dispensando cadastro de conta, envio de respostas ou coleta de dados pessoais.
- Dessa forma, basta acessar a página nos computadores ou no projetor para apoiar a mediação do professor de Computação, garantindo espaço para explicação e diálogo com a turma.""",
    ),
    (
        "B1_f",
        0,
        """- A proposta educativa para o Ensino Médio articula uma sequência didática e uma ferramenta web em português brasileiro pensada para funcionar mesmo sob conectividade limitada.
- Executado no navegador com dados sintéticos e processamento na máquina local, o recurso dispensa login e não envia respostas nem armazena dados pessoais dos usuários.
- Por exigir apenas a abertura no projetor ou nos computadores da sala, auxilia o docente de Computação preservando o tempo de explicação e conversa em aula.""",
    ),
    (
        "B3_e",
        3,
        """- Os modelos presentes na plataforma vão além de apenas dividirem o mesmo endereço, porque questões recorrentes acompanham todas as etapas e conduzem os alunos.
- Antes de testar qual ajuste altera o gráfico ou a regra, a turma identifica de onde vem o dado disponível e qual resposta se espera dele.
- Cada técnica devolve um tipo de saída diferente nessa investigação: a reta calcula um valor numérico previsto, a SVM posiciona uma fronteira para separar exemplos rotulados, o k-NN consulta casos próximos, a árvore percorre condições e o k-means reorganiza os pontos mesmo quando faltam categorias prévias.""",
    ),
    (
        "B3_f",
        3,
        """- Mais do que coexistir no mesmo site, cada atividade dialoga com as demais por meio de perguntas parecidas ao longo do percurso.
- Os alunos primeiro conferem a origem do dado e a saída esperada antes de alterar qualquer controle na tela.
- Os resultados variam em cada abordagem, pois enquanto a regressão linear estima um número pela reta e a SVM coloca uma fronteira entre casos rotulados, o k-NN consulta vizinhos próximos, a árvore segue regras condicionais e o k-means agrupa pontos na ausência de categorias prévias.""",
    ),
    (
        "B4_e",
        4,
        """- Responder sempre às mesmas questões impede os alunos de reduzir os cinco algoritmos a uma lista decorada de nomes técnicos.
- Para o professor, essa comparação mostra se o obstáculo da turma vem de uma noção específica ou se nasce da dificuldade transversal de interpretar dados e gráficos.
- Como se observa na Figura 1, a página de entrada da plataforma junta os materiais de apoio, os cinco módulos e o trajeto das aulas previstas para a sequência.""",
    ),
    (
        "B4_f",
        4,
        """- Ao retomar o mesmo roteiro de perguntas em cada atividade, a turma enxerga diferenças conceituais entre os modelos sem se limitar a nomes isolados.
- O docente também consegue distinguir dúvidas pontuais sobre um algoritmo de dificuldades gerais na leitura de gráficos e dados em todos os módulos.
- A tela de abertura exibida na Figura 1 concentra esse trajeto de aulas, os módulos interativos e os materiais de apoio empregados pelos alunos na sequência.""",
    ),
]


def main() -> None:
    results = []
    for i, (name, orig_idx, top) in enumerate(CANDIDATES_R8, 1):
        ka = "0s" if i == len(CANDIDATES_R8) else "5m"
        t0 = time.time()
        out = ask_raw(top, temp=0.67, keep_alive=ka)
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

    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_1_v5_r8.txt")
    out_path.write_text(
        "\n\n".join(f"{h}\n{o}" for _, h, o in results) + "\n",
        encoding="utf-8",
    )
    print(f"\nSalvo em {out_path}", flush=True)


if __name__ == "__main__":
    main()
