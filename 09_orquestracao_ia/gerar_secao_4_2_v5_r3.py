#!/usr/bin/env python3
"""Rodada 3 para Bloco 1 e Bloco 2 da Seção 4.2 (Bloco 3 já tem B3_r2a aprovado)
visando cobertura completa das Figuras 2a e 2b, tempo presente/futuro e baixo 4g_top."""
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

CANDIDATES_4_2_R3 = [
    (
        "B1_r3a",
        0,
        """- Em cada módulo, a aula parte de um cenário aplicado e esclarece a procedência dos dados para perguntar o que o algoritmo busca aprender ali.
- Primeiro o estudante antecipa o que deve ocorrer antes de mexer nos controles na tela.
- Em seguida ele altera valores ou parâmetros, observa os efeitos no gráfico e na saída do modelo e explica o resultado, repetindo essa sequência em toda a plataforma para explicitar seu raciocínio em cada manipulação.""",
    ),
    (
        "B1_r3b",
        0,
        """- Os módulos iniciam com uma situação-problema ligada à origem dos dados para questionar qual relação o modelo tenta aprender.
- Antes de usar os comandos da página, o aluno prevê o comportamento esperado e depois testa mudanças nos dados ou parâmetros.
- Ao conferir a mudança no gráfico e na resposta exibida e explicar o motivo do ocorrido, o estudante repete nos cinco módulos esse percurso que revela como raciocina ao manipular o sistema.""",
    ),
    (
        "B2_r3a",
        1,
        """- Ao mexer na inclinação da reta, o aluno contrasta previsão e valor medido, assim como aproximar a fronteira de uma classe abre debate sobre redução da margem na SVM, seguindo o mesmo raciocínio no ajuste de vizinhos, divisões da árvore e posição dos centroides.
- As Figuras 2a e 2b ilustram dois desses módulos em uso na plataforma: a primeira mostra a previsão numérica pela reta e a segunda exibe a fronteira que separa exemplos rotulados.
- Em ambas as telas mostradas, o aluno precisa prever o efeito antes de alterar o controle e registrar uma explicação ao final da exploração.""",
    ),
    (
        "B2_r3b",
        1,
        """- Deslocar a inclinação da reta permite comparar a saída prevista com o dado observado, enquanto levar a fronteira até perto de uma classe mostra a margem diminuindo na SVM; a mesma lógica orienta testes de vizinhos, cortes da árvore e lugar dos centroides.
- Esse funcionamento aparece nas Figuras 2a e 2b com dois exemplos da plataforma: uma tela trata da previsão numérica pela reta e a outra separa exemplos rotulados por fronteira.
- Nos dois casos ilustrados, a atividade pede uma hipótese antes do ajuste nos comandos e uma explicação depois do teste.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_2_v5_r3.txt")
    results = []
    for i, (name, orig_idx, top) in enumerate(CANDIDATES_4_2_R3, 1):
        ka = "0s" if i == len(CANDIDATES_4_2_R3) else "5m"
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
