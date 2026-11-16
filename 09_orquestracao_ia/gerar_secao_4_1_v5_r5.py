#!/usr/bin/env python3
"""Rodada 5 para Seção 4.1 usando notas telegráficas (estilo Bloco 4 da 3.5 que atingiu 86% Human)
e temperature=0.72 para evitar colagem de estruturas paralelas ou sintaxe de LLM comercial."""
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

CANDIDATES_R5 = [
    (
        "B1_t1",
        0,
        """- Produto educacional para Ensino Médio: plataforma interativa em português brasileiro + sequência didática.
- Execução direta no navegador, cenários sintéticos, cálculos locais no próprio computador.
- Dispensa de conta ou cadastro; sem envio de respostas nem coleta de dados pessoais.
- Funcionamento viável com internet limitada nos computadores ou no projetor; apoio à mediação docente em Computação preservando explicação e diálogo do professor.""",
    ),
    (
        "B1_t2",
        0,
        """- Junção de plataforma web em português brasileiro e sequência didática voltada ao Ensino Médio.
- Processamento local no navegador a partir de cenários sintéticos, sem exigir cadastro, envio de respostas ou coleta de dados pessoais.
- Uso prático em computadores ou projetor mesmo sob conectividade restrita, apoiando o professor de Computação sem tirar espaço da fala e do diálogo em aula.""",
    ),
    (
        "B2_t1",
        1,
        """- Cinco módulos introdutórios de machine learning na proposta: regressão linear, máquina de vetores de suporte (SVM), k-vizinhos mais próximos (k-NN), árvore de decisão e k-means.
- Articulação de previsão numérica, classificação e formação de grupos para comparação em turma, distante de catálogo solto de comandos.
- Lugar central dos cinco módulos e camadas matemáticas próprias: função, linha de tendência e cálculo de resíduos ou erros na regressão linear; fronteira com margem separando classes na SVM.
- Distância entre pontos no k-NN, recálculo de centroides pela média no k-means e condições encadeadas na árvore; diferença de formalismo ligada ao repertório de estudantes iniciantes para exibir relações no gráfico ou na regra em debate na aula, sem rebaixar nenhum módulo.""",
    ),
    (
        "B2_t2",
        1,
        """- Cinco módulos de iniciação a machine learning (regressão linear, máquina de vetores de suporte - SVM, k-vizinhos mais próximos - k-NN, árvore de decisão e k-means) cobrindo tarefas de previsão numérica, classificação e agrupamento, sem virar lista isolada de comandos.
- Importância central de todos na sequência por trazerem noções matemáticas próprias: função, reta de tendência e resíduos ou erros na regressão linear; divisão de classes por fronteira com margem na SVM.
- Trabalho com distância entre pontos no k-NN, média para recalcular centroides no k-means e encadeamento de condições na árvore de decisão.
- Menor formalismo em certas etapas não diminui módulo algum, mas respeita alunos iniciantes tornando visíveis relações matemáticas no gráfico ou na regra durante a aula.""",
    ),
    (
        "B3_t1",
        2,
        """- Conexão entre os módulos além da mesma plataforma mediante perguntas recorrentes nas atividades.
- Identificação pela turma da origem do dado disponível e da saída esperada antes de testar ajustes alteradores do resultado.
- Variação das saídas conforme o modelo: previsão numérica pela reta, fronteira posicionada pela SVM para separar exemplos rotulados, consulta a exemplos próximos no k-NN, percurso de regras condicionais na árvore e reorganização de pontos no k-means mesmo sem categorias prévias.""",
    ),
    (
        "B3_t2",
        2,
        """- Articulação dos cinco módulos por questões repetidas durante toda a sequência, superando uso isolado na mesma página.
- Verificação prévia pelos alunos de onde vêm os dados e qual resposta se espera antes de alterar ajustes no modelo.
- Diferença nos resultados produzidos: reta estima valor numérico; SVM coloca fronteira entre casos rotulados; k-NN observa vizinhos próximos; árvore segue regras condicionais; k-means agrupa pontos na falta de categorias anteriores.""",
    ),
    (
        "B4_t1",
        3,
        """- Uso das mesmas perguntas em cada módulo permitindo comparação dos modelos pelos estudantes sem reduzi-los a lista de nomes.
- Indicação para o professor sobre dificuldade ligada a conceito específico ou à leitura de dados e gráficos comum a todos os módulos.
- Apresentação da tela inicial da plataforma na Figura 1, reunindo percurso de aulas, módulos e materiais de apoio previstos na sequência.""",
    ),
    (
        "B4_t2",
        3,
        """- Padronização das perguntas guiando a turma na comparação entre abordagens além da memorização de nomes soltos.
- Percepção docente entre entrave em conceito particular e dificuldade transversal de leitura de gráficos e dados ao longo dos módulos.
- Ilustração pela Figura 1 da tela inicial da plataforma com o roteiro de aulas, os cinco módulos e os materiais de apoio empregados na sequência didática.""",
    ),
]


def fourgram_overlap(a: str, b: str) -> int:
    ta = re.findall(r"[a-zà-ú0-9-]+", a.lower())
    tb = re.findall(r"[a-zà-ú0-9-]+", b.lower())
    if len(ta) < 4 or len(tb) < 4:
        return 0
    sa = {tuple(ta[i : i + 4]) for i in range(len(ta) - 3)}
    sb = {tuple(tb[i : i + 4]) for i in range(len(tb) - 3)}
    return len(sa & sb)


def main() -> None:
    results = []
    for i, (name, orig_idx, top) in enumerate(CANDIDATES_R5, 1):
        ka = "0s" if i == len(CANDIDATES_R5) else "5m"
        t0 = time.time()
        out = ask_raw(top, temp=0.72, keep_alive=ka)
        t_clean = re.sub(r"(?m)^-\s*", "", top).replace("\n", " ")
        topic_sim = difflib.SequenceMatcher(None, t_clean, out).ratio()
        ng4 = fourgram_overlap(t_clean, out)
        copied, total_s, worst_s = sentence_audit(ORIG_PARAS[orig_idx], out)
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

    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_1_v5_r5.txt")
    out_path.write_text(
        "\n\n".join(f"{h}\n{o}" for _, h, o in results) + "\n",
        encoding="utf-8",
    )
    print(f"\nSalvo em {out_path}", flush=True)


if __name__ == "__main__":
    main()
