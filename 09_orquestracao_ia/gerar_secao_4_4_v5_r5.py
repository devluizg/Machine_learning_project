#!/usr/bin/env python3
"""Rodada 5 cirúrgica da Seção 4.4 para os 4 blocos restantes (B7, B9, B11, B12)."""
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
from gerar_secao_4_4_v5_p2 import ORIG_BLOCKS_4_4_P2

TOPICS_4_4_R5 = [
    (
        "B7_r5",
        "B7",
        """- Na sexta aula da sequência, o módulo de k-means trará uma mudança porque os pontos exibidos não virão com categorias prévias, retomando a pergunta sobre o que se quer produzir com os dados para mostrar que formar grupos por proximidade difere de escolher uma classe conhecida.
- Como acompanhar a atualização dos centroides e a reorganização dos pontos poderá exigir mais tempo, o professor retomará termos dos encontros anteriores para esclarecer agrupamento frente à classificação, encerrando com uma síntese breve sobre como os cinco modelos articulam dados e regras segundo a finalidade de cada tarefa.""",
    ),
    (
        "B9_r5",
        "B9",
        """- Esse encontro comparativo servirá para recuperar diferenças que tenham ficado dispersas e preparar o desafio final, levando o estudante a examinar a finalidade da tarefa diante dos dados disponíveis antes de escolher o modelo.
- Na etapa de encerramento, enquanto o núcleo comparável permitirá verificar avanços frente ao diagnóstico inicial, o desafio de transferência mostrará como os conceitos são mobilizados em novo contexto como evidência adicional sem equiparação direta com questões mais simples.""",
    ),
    (
        "B11_r4",
        "B11",
        """- O plano provisório dos oito encontros articula objetivos de aprendizagem e tempo estimado às ações de mediação docente e questões formativas, indicando também adaptações de infraestrutura escolar e limites didáticos por módulo.
- Como a plataforma não guarda nenhuma resposta digitada pelos estudantes no navegador, o corpus de análise reunirá o diagnóstico inicial, o instrumento final completo, os três registros individuais intermediários feitos em sala e as anotações docentes.""",
    ),
    (
        "B12_r4",
        "B12",
        """- Antes do início da intervenção escolar, a versão do site empregada no campo passará por conferência diante de tudo o que consta na sequência didática, corrigindo ou explicando à turma eventual diferença nos conjuntos de dados, nos textos de apoio ou nas representações matemáticas.
- Essa checagem prévia impede analisar os alunos como se tivessem vivenciado outra proposta e assegura que a plataforma e os instrumentos avaliem exatamente o que foi ensinado nas aulas.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_4_v5_r5.txt")
    results = []
    for i, (name, orig_key, top) in enumerate(TOPICS_4_4_R5, 1):
        orig_txt = ORIG_BLOCKS_4_4_P2[orig_key]
        ka = "0s" if i == len(TOPICS_4_4_R5) else "5m"
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
