#!/usr/bin/env python3
"""Rodada 2 para a Seção 4.3 garantindo tempo futuro/presente em 3ª pessoa,
fidelidade estrita aos 5 cenários e nenhuma distorção ética no Bloco 1."""
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

CANDIDATES_4_3_R2 = [
    (
        "B1_c",
        ORIG_54,
        """- Quase todo o material usado nos exercícios práticos virá de dados gerados sinteticamente dentro da própria plataforma.
- Apenas no segundo encontro existe a possibilidade de a turma preencher em conjunto uma pequena tabela anônima com informações voluntárias simples ou medir objetos da sala de aula.
- Esse quadro auxiliar terá uso exclusivo para o ensino durante a aula e permanecerá fora do corpus analisado na pesquisa.
- Nos demais cenários preparados para as atividades, descarta-se por completo recorrer a notas escolares, registros de conduta ou informações pessoais dos estudantes.""",
    ),
    (
        "B1_d",
        ORIG_54,
        """- Os conjuntos numéricos trabalhados em aula serão quase integralmente sintéticos.
- Excepcionalmente na segunda aula, os estudantes poderão montar um quadro anônimo com dados simples fornecidos de modo voluntário ou tomar medidas de objetos da sala, recurso restrito ao ensino e mantido fora do corpus da pesquisa.
- Em todas as outras propostas didáticas ficam excluídos boletins de notas, anotações sobre comportamento escolar e qualquer dado pessoal da turma.""",
    ),
    (
        "B2_c",
        ORIG_56A,
        """- Os cenários experimentais definidos para a turma poderão receber acertos pontuais depois da verificação das condições locais de aplicação.
- No caso da regressão linear, a proposta relaciona quantidade de passos e distância percorrida, ao passo que a SVM emprega medidas simuladas de sementes para distinguir duas classes.
- Quanto aos outros módulos, o k-NN classifica comidas fictícias por doçura e acidez, o k-means aproveita esse mesmo par para formar grupos sem categorias anteriores e a árvore de decisão organiza objetos segundo largura e altura.""",
    ),
    (
        "B2_d",
        ORIG_56A,
        """- Pensados para a turma prevista, os contextos práticos admitem pequenos ajustes após conferência das condições da escola.
- Enquanto a regressão linear liga número de passos à distância caminhada, a SVM separa duas categorias a partir de medidas simuladas de sementes.
- Na sequência dos módulos, o k-NN classifica alimentos fictícios considerando doçura e acidez, o k-means retoma tais duas medidas para agrupar pontos sem rótulos prévios e a árvore de decisão ordena objetos por largura e altura.""",
    ),
    (
        "B3_c",
        ORIG_56B,
        """- Cada contexto escolhido precisa tornar perceptível aos jovens de que maneira mudanças em entradas ou parâmetros alteram a resposta usando a Matemática da série escolar.
- Antes da entrada em sala de aula, os exemplos passarão por uma revisão prévia conduzida para ajustar a clareza da linguagem e o ritmo das atividades ao tempo previsto para a turma.""",
    ),
    (
        "B3_d",
        ORIG_56B,
        """- Todos esses cenários procuram evidenciar como mexer em dados ou parâmetros modifica o comportamento do algoritmo em diálogo direto com a Matemática trabalhada na série.
- Antes de iniciar os encontros na escola, todos os exemplos serão revistos para adequar os termos dos enunciados e a duração prevista à realidade da turma.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_3_v5_r2.txt")
    results = []
    for i, (name, orig_txt, top) in enumerate(CANDIDATES_4_3_R2, 1):
        ka = "0s" if i == len(CANDIDATES_4_3_R2) else "5m"
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
