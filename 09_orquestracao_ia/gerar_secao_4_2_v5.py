#!/usr/bin/env python3
"""Gera candidatos para os 3 blocos da Seção 4.2 (Organização pedagógica da plataforma)
no luiz-academico v5.0 (temperature=0.68), com salvamento incremental e auditoria contra capitulo4.tex."""
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

ORIG_4_2 = [
    (
        "Cada módulo parte de uma situação-problema e da origem dos dados para questionar o que o "
        "modelo tenta aprender. Antes de usar os controles, o estudante prevê uma consequência. Em "
        "seguida, modifica dados ou parâmetros definidos para o experimento, observando o efeito gerado "
        "no gráfico e na saída do modelo para explicar o que ocorreu. Esse movimento da previsão ao "
        "experimento, seguido pela observação e pela explicação, repete-se nos módulos para explicitar "
        "o raciocínio por trás de cada manipulação."
    ),
    (
        "Mover a inclinação da reta leva o estudante a comparar a previsão com o valor observado, "
        "enquanto aproximar uma fronteira de uma classe permite discutir a redução da margem na SVM. "
        "A mesma lógica orienta o ajuste de vizinhos ou de divisões da árvore, assim como a posição "
        "dos centroides. As Figuras 2a e 2b mostram dois módulos em uso. A primeira tela organiza a "
        "previsão numérica por meio da reta; a segunda mostra a fronteira que separa exemplos "
        "rotulados. Em ambas, a ação proposta solicita uma previsão antes da alteração do controle e "
        "uma explicação depois da exploração."
    ),
    (
        "A sequência abre com recursos de inteligência artificial que os estudantes já usam e chega "
        "logo a um problema concreto com dados. A Matemática entra à medida que a leitura do gráfico "
        "e a decisão do modelo na situação exigem. Toda representação visual é acompanhada por tabelas "
        "e textos que explicitam a regra, evitando que a compreensão dependa apenas da imagem. As "
        "visualizações em 3D do protótipo entram como recurso complementar dispensável ao conceito "
        "central, mantendo na interface o uso por teclado e a opção de reduzir movimentos."
    ),
]

CANDIDATES_4_2 = [
    (
        "B1_c",
        0,
        """- Cada módulo começa mostrando uma situação-problema e de onde vêm os dados para os alunos pensarem no que o modelo tenta aprender.
- Antes de mexer em qualquer botão ou controle da tela, o aluno tenta prever uma consequência.
- Depois ele altera valores dos dados ou parâmetros do experimento, observa o efeito no gráfico e na saída do modelo e explica o que ocorreu.
- Repetir esse passo a passo da previsão ao experimento e da observação à explicação em todos os módulos deixa visível o raciocínio por trás de cada ajuste feito.""",
    ),
    (
        "B1_d",
        0,
        """- O início de todo módulo traz uma situação-problema ligada à origem dos dados, perguntando à turma o que o algoritmo procura aprender ali.
- Primeiro o estudante prevê uma consequência sem tocar ainda nos controles da página.
- Em seguida, troca dados ou ajusta parâmetros no experimento e acompanha o resultado no gráfico e na resposta do modelo para explicar o que aconteceu.
- Esse movimento contínuo de prever, testar, observar e explicar repete-se ao longo dos módulos revelando o raciocínio de cada manipulação.""",
    ),
    (
        "B2_a",
        1,
        """- Mudar a inclinação da reta faz o estudante comparar o valor previsto com o valor observado, enquanto aproximar uma fronteira de uma classe leva a discutir como a margem diminui na SVM.
- Raciocínio parecido vale quando se ajusta a quantidade de vizinhos, as divisões da árvore ou o lugar dos centroides.
- As Figuras 2a e 2b exibem duas telas em funcionamento na plataforma: uma organiza a previsão numérica usando a reta e a outra separa exemplos rotulados por uma fronteira.
- Em ambas as telas, pede-se ao aluno prever antes de mexer no controle e explicar depois da exploração.""",
    ),
    (
        "B2_b",
        1,
        """- Quando mexe na inclinação da reta, a turma confronta a previsão com o dado observado; já ao chegar com a fronteira perto de uma classe na SVM, debate-se a redução da margem.
- Esse mesmo raciocínio orienta testes com vizinhos, divisões da árvore e posição dos centroides.
- Na Figura 2a aparece o módulo da previsão numérica pela reta, enquanto a Figura 2b mostra a fronteira dividindo exemplos rotulados.
- Nos dois módulos ilustrados, o estudante primeiro prevê o efeito antes de alterar o controle e depois explica o que viu na exploração.""",
    ),
    (
        "B3_a",
        2,
        """- A sequência começa lembrando recursos de inteligência artificial que os estudantes já usam e chega rápido a um problema concreto com dados.
- A Matemática aparece na aula conforme a leitura do gráfico e a decisão do modelo naquela situação exigem.
- Toda visualização na tela traz junto tabelas e textos deixando a regra explícita, para a compreensão não depender apenas da imagem.
- Os recursos em 3D do protótipo ficam apenas como apoio complementar dispensável ao conceito central, enquanto a interface mantém uso pelo teclado e opção de reduzir movimentos.""",
    ),
    (
        "B3_b",
        2,
        """- As aulas abrem com recursos de inteligência artificial que os jovens já utilizam no dia a dia e logo partem para um problema prático com dados.
- A Matemática entra conforme a leitura gráfica e a decisão do modelo exigem no decorrer do problema.
- Para o entendimento não depender só da imagem, toda representação visual vem acompanhada de tabelas e textos que deixam a regra clara.
- As visualizações em 3D presentes no protótipo entram como complemento dispensável ao conceito central, preservando na interface o controle pelo teclado e a escolha de reduzir movimentos.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_2_v5.txt")
    results = []
    for i, (name, orig_idx, top) in enumerate(CANDIDATES_4_2, 1):
        ka = "0s" if i == len(CANDIDATES_4_2) else "5m"
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
