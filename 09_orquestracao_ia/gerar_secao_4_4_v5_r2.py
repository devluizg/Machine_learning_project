#!/usr/bin/env python3
"""Rodada 2 para os Blocos 1 a 6 da Seção 4.4 corrigindo tempo verbal (futuro/presente),
leituras literais ('segunda a sexta' / 'duas turmas') e vazamentos de r1."""
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
from gerar_secao_4_4_v5_p1 import ORIG_BLOCKS_4_4_P1

TOPICS_4_4_R2 = [
    (
        "B1_r2",
        "B1",
        """- Uma turma de Ensino Médio acompanhada pelo próprio pesquisador como docente receberá a sequência prevista para novembro de 2026.
- O cronograma escolar comportará oito encontros com cerca de cinquenta minutos cada dentro do componente curricular combinado com a escola.
- Os vinte computadores com internet do laboratório receberão reforço de Chromebooks para assegurar acesso individual quando necessário, ficando a aplicação e a produção de dados condicionadas às autorizações institucionais e éticas cabíveis.""",
    ),
    (
        "B2_r2",
        "B2",
        """- Todos os encontros mantêm uma estrutura pedagógica constante, mesmo quando o modelo em foco muda.
- A dinâmica de cada aula abre com uma pergunta ou situação que delimita o problema, pede o registro de uma breve previsão inicial, passa pela exploração autônoma dos controles pelos estudantes e fecha com debate coletivo e síntese docente.
- Essa rotina garante continuidade entre as aulas e integra a plataforma à construção e revisão de hipóteses, evitando que o site funcione como mero intervalo entre explicações.""",
    ),
    (
        "B3_r2",
        "B3",
        """- A aula inaugural servirá para nivelar noções básicas junto à turma antes da apresentação de qualquer algoritmo específico.
- No início desse encontro ou na aula anterior dependendo do tempo disponível, cada aluno responderá individualmente ao diagnóstico inicial, registrando ideias de partida sem antecipar os nomes técnicos das etapas seguintes.
- Em seguida, o grupo debaterá aplicações cotidianas da inteligência artificial e passará a distinguir dados e regra do modelo, apontando o que entra no sistema e qual resposta dele se espera.""",
    ),
    (
        "B4_r2",
        "B4",
        """- Do 2º ao 6º encontro da sequência, a turma trabalhará um módulo da plataforma por aula, partindo da regressão linear rumo aos modelos de classificação e agrupamento.
- Logo no 2º encontro, a organização coletiva da tabela da turma antecederá a atividade de regressão linear.
- Para impedir que cada técnica apareça isolada em uma única experiência, todas as aulas retomarão elementos trabalhados nos encontros anteriores.""",
    ),
    (
        "B5_r2",
        "B5",
        """- A sequência de modelos supervisionados abrirá com a regressão linear e com a SVM em encontros consecutivos.
- Na aula de regressão linear, a turma localizará a linha de tendência no plano cartesiano para elaborar previsões e confrontá-las aos valores observados, introduzindo a noção de erro.
- Na aula seguinte com a SVM, o grupo retomará exemplos conhecidos para discutir a fronteira que separa classes e a margem ao redor dessa divisão, contrastando estimativa numérica e escolha de categoria como decisões ligadas aos dados e ao modelo.""",
    ),
    (
        "B6_r2",
        "B6",
        """- Em aulas subsequentes, os mesmos estudantes conhecerão duas estratégias diferentes de classificação: o k-NN e a árvore de decisão.
- Ao trabalhar com o k-NN, o grupo observará o papel da distância entre pontos e da quantidade de vizinhos na votação; depois, na árvore de decisão, acompanhará regras condicionais e os caminhos percorridos até uma decisão.
- Comparar ambos os módulos ajudará a afastar a crença de que existe um algoritmo melhor que os outros, mostrando que os dois combinam dados e regras ao seu modo e fornecem saídas dependentes do problema e dos exemplos disponíveis.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_4_v5_r2.txt")
    results = []
    for i, (name, orig_key, top) in enumerate(TOPICS_4_4_R2, 1):
        orig_txt = ORIG_BLOCKS_4_4_P1[orig_key]
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
