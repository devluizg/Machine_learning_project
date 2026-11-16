#!/usr/bin/env python3
"""Gera apenas os Blocos 3 e 4 da Seção 3.5 em duas variações de notas curtas
no luiz-academico v5.0 (sem reescritas manuais de orações depois)."""
import difflib
import re
import time
from pathlib import Path
from pipeline_v5_fiel import INST_TOPICS
import json, urllib.request

def ask_raw(topics: str, temp: float = 0.68, keep_alive: str = "5m") -> str:
    payload = {
        "model": "luiz-academico:latest",
        "messages": [{"role": "user", "content": f"{INST_TOPICS}\n\n{topics}"}],
        "stream": False,
        "keep_alive": keep_alive,
        "options": {
            "num_ctx": 1024,
            "temperature": temp,
            "top_p": 0.92,
            "min_p": 0.04,
            "repeat_penalty": 1.05,
        },
    }
    req = urllib.request.Request(
        "http://localhost:11434/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=600) as r:
        data = json.loads(r.read().decode("utf-8"))
    raw = data["message"]["content"].strip()
    t = re.sub(r"\s*\n+\s*", " ", raw).strip()
    t = re.sub(r'\s*\([A-ZÁÉÍÓÚÂÊÔÃÕÇ\s,;]+\d{4},\s*p\.\s*\d*\)?\.?\s*$', '.', t)
    return t

CANDIDATES = [
    ("B3_v1", """- Revisões sobre IA e machine learning na Educação Básica mostram que já existem ferramentas e relatos, mas cobram maior clareza nas estratégias em sala e avaliações mais rigorosas (Martins e Gresse von Wangenheim, 2023; Rauber e Gresse von Wangenheim, 2023; Sanusi et al., 2023).
- Diante dessa lacuna, a presente pesquisa busca analisar uma sequência didática aplicada em turma de Ensino Médio do próprio professor.
- O estudo junta a visualização interativa de cinco modelos (regressão linear, SVM, k-NN, árvore de decisão e k-means) com instrumentos avaliativos de critérios explícitos."""),

    ("B3_v2", """- A literatura já traz ferramentas de ensino de IA para escolas, porém estudos apontam falta de detalhamento didático nos locais de aula e de avaliações rigorosas (Martins e Gresse von Wangenheim, 2023; Rauber e Gresse von Wangenheim, 2023; Sanusi et al., 2023).
- Este projeto contribui ao investigar na prática escolar do pesquisador uma sequência para turmas do Ensino Médio.
- A proposta liga a tela interativa com cinco algoritmos (regressão linear, SVM, k-NN, árvore de decisão e k-means) a roteiros com critérios claros."""),

    ("B4_v1", """- O rigor deste projeto de mestrado depende da coerência direta entre a teoria adotada e o site educacional construído.
- As páginas, botões e gráficos da ferramenta refletirão os objetivos de aprendizagem cobrados nas tarefas escolares e na coleta de dados.
- Essa ligação garante que o texto final das análises não ultrapasse o limite real das evidências encontradas na turma."""),

    ("B4_v2", """- Qualidade científica da pesquisa ligada ao alinhamento metodológico entre referencial teórico e produto educacional.
- Planejamento dos recursos da plataforma em função direta dos objetivos presentes nas aulas e nos instrumentos avaliativos.
- Cuidado metodológico para que as conclusões do trabalho respeitem exatamente o alcance dos dados obtidos com os estudantes."""),
]

def main():
    for i, (name, top) in enumerate(CANDIDATES, 1):
        ka = "0s" if i == len(CANDIDATES) else "5m"
        t0 = time.time()
        out = ask_raw(top, temp=0.68, keep_alive=ka)
        t_clean = re.sub(r"(?m)^-\s*", "", top).replace("\n", " ")
        sim = difflib.SequenceMatcher(None, t_clean, out).ratio()
        print(f"\n=== {name} ({time.time()-t0:.1f}s | topic={len(t_clean.split())}w -> out={len(out.split())}w | sim={sim:.2f}) ===", flush=True)
        print(out, flush=True)

if __name__ == "__main__":
    main()
