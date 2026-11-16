#!/usr/bin/env python3
"""Rodada 2 para Seção 4.2 com paráfrases frescas nos tópicos (evitando colagem do .tex
e mantendo 4g_top baixo, tempo presente e cadência orgânica Autor 1)."""
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

CANDIDATES_4_2_R2 = [
    (
        "B1_r2a",
        0,
        """- Todos os ambientes da plataforma começam contextualizando uma situação-problema e esclarecendo de onde saem os números mostrados para indagar o que o algoritmo busca aprender ali.
- O estudante precisa formular um palpite fundamentado sobre o que vai mudar antes mesmo de tocar em qualquer botão ou controle.
- Só depois ele mexe nos registros ou regula os parâmetros do teste, acompanha a mudança na imagem gráfica e na resposta devolvida pelo programa e redige o porquê daquele comportamento.
- Manter essa sequência entre antecipar, testar, observar e justificar nos cinco módulos ajuda a tornar visível como o aluno raciocina ao manipular a tela.""",
    ),
    (
        "B1_r2b",
        0,
        """- Ao abrir um módulo, a turma depara primeiro com um caso prático e identifica a fonte dos dados para entender qual padrão o sistema procura aprender.
- Antes de ajustar controles na página, cabe ao discente apontar previamente qual resultado imagina acontecer.
- Na etapa prática seguinte, altera valores de entrada ou configurações do teste e observa tanto o desenho do gráfico quanto a saída calculada, explicando então a razão da mudança vista.
- Essa rotina de previsão antecipada, experimentação, leitura visual e justificativa repete-se em toda a plataforma para evidenciar o pensamento por trás de cada ação.""",
    ),
    (
        "B2_r2a",
        1,
        """- Quando altera a inclinação da reta, o jovem confronta o número estimado com o valor real medido; de modo parecido, ao empurrar a fronteira para perto de uma classe na SVM, a turma enxerga e discute o estreitamento da margem.
- O mesmo princípio rege a troca do total de vizinhos no k-NN, as quebras condicionais da árvore e o deslocamento dos centroides no k-means.
- As Figuras 2a e 2b ilustram duas dessas páginas em operação na ferramenta: a primeira trabalha estimativa numérica via reta e a segunda exibe uma divisa entre casos rotulados.
- Nas duas telas mostradas, o aluno registra sua hipótese antes de mexer no ajuste e interpreta o resultado ao fim da experimentação.""",
    ),
    (
        "B2_r2b",
        1,
        """- Girar a inclinação da reta coloca lado a lado o valor calculado e o dado real, enquanto puxar a linha divisória para junto de um grupo na SVM leva ao debate sobre diminuição de margem.
- A lógica mantém-se idêntica ao variar vizinhos próximos, redefinir cortes da árvore de decisão ou reposicionar centroides.
- Esse funcionamento aparece nas Figuras 2a e 2b com dois exemplos abertos na plataforma, retratando primeiro a previsão contínua por reta e depois a fronteira entre exemplos rotulados.
- Tanto em uma tela quanto na outra, a atividade cobra antecipação prévia antes do toque nos comandos e explicação após o teste.""",
    ),
    (
        "B3_r2a",
        2,
        """- As primeiras aulas partem de ferramentas de inteligência artificial já presentes no cotidiano dos estudantes e avançam depressa rumo a um desafio concreto apoiado em dados.
- Conceitos matemáticos surgem sob demanda conforme a interpretação dos gráficos e o critério de decisão exigidos pela tarefa.
- Para não restringir o entendimento somente ao desenho gráfico, todas as telas exibem quadros de dados e descrições textuais que deixam a regra às claras.
- Já os gráficos em 3D disponíveis no protótipo servem apenas como recurso opcional sem afetar o conteúdo principal, garantindo na interface operação por teclado e opção para reduzir movimentos na tela.""",
    ),
    (
        "B3_r2b",
        2,
        """- O percurso didático abre dialogando com sistemas de inteligência artificial já utilizados pelos alunos e logo apresenta uma situação prática com dados.
- A abordagem matemática é trazida no momento em que ler o gráfico e compreender como o modelo decide tornam esse apoio necessário.
- Nenhuma figura aparece isolada, pois tabelas e explicações escritas acompanham cada representação para explicitar a regra além do visual.
- As vistas em 3D presentes no protótipo atuam como complemento dispensável ao conceito central, preservando na interface o acesso pelo teclado e a opção para reduzir movimentos.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_2_v5_r2.txt")
    results = []
    for i, (name, orig_idx, top) in enumerate(CANDIDATES_4_2_R2, 1):
        ka = "0s" if i == len(CANDIDATES_4_2_R2) else "5m"
        t0 = time.time()
        out = ask_raw(top, temp=0.67, keep_alive=ka)
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
