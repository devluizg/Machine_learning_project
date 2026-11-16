#!/usr/bin/env python3
"""Gera candidatos (v1/v2) por bloco para a Seção 4.1 no luiz-academico v5.0
sem reescrita manual posterior de orações, com auditoria de similaridade e vazamentos."""
import difflib
import json
import re
import time
import urllib.request
from pathlib import Path

INST_TOPICS = (
    "Escreva um texto acadêmico contínuo em português brasileiro desenvolvendo "
    "exatamente os pontos abaixo no estilo, vocabulário e construção de frases "
    "do autor de referência."
)

ORIG_PARAS = [
    (
        "O produto educacional une uma plataforma interativa em português brasileiro a uma "
        "sequência didática para o Ensino Médio. A plataforma roda direto no navegador com "
        "cenários sintéticos, executando todos os cálculos no próprio computador. Seu acesso "
        "dispensa criação de conta ou cadastro de usuário, operando sem envio de respostas ou "
        "coleta de dados pessoais. Isso facilita o uso mesmo sob conectividade limitada, "
        "bastando abrir o recurso nos computadores ou no projetor. A ferramenta apoia a "
        "mediação docente em Computação, preservando o espaço da explicação e do diálogo "
        "conduzidos pelo professor."
    ),
    (
        "A proposta tem cinco módulos introdutórios de machine learning: regressão linear, "
        "máquina de vetores de suporte (SVM), k-vizinhos mais próximos, árvore de decisão e "
        "k-means. Longe de formarem um catálogo de comandos ou conteúdos soltos, eles "
        "apresentam tarefas distintas de previsão numérica e classificação, além da formação "
        "de grupos para que a turma compare o que muda entre eles. Todos ocupam lugar central "
        "na sequência, mobilizando camadas matemáticas próprias. Na regressão linear, o "
        "estudo da função e da linha de tendência fundamenta a previsão e o cálculo de "
        "resíduos ou erros, enquanto a SVM separa classes por uma fronteira com sua margem. "
        "Já o k-NN destaca a distância entre pontos, o k-means recalcula centroides pela média "
        "e a árvore encadeia condições. A diferença de formalização não diminui nenhum módulo. "
        "Ela decorre do repertório de estudantes iniciantes e da necessidade de tornar visível, "
        "no gráfico ou na regra, uma relação que a turma consiga discutir durante a aula."
    ),
    (
        "Mais do que estarem na mesma plataforma, os modelos se conectam por perguntas "
        "recorrentes nos módulos. A turma identifica a origem do dado disponível e a saída "
        "esperada antes de testar qual ajuste pode alterá-la. A resposta varia em cada caso. "
        "Enquanto a reta gera uma previsão numérica, a SVM posiciona uma fronteira para separar "
        "exemplos rotulados. Por sua vez, o k-NN consulta exemplos próximos e a árvore percorre "
        "regras condicionais, ao passo que o k-means reorganiza pontos mesmo sem categorias prévias."
    ),
    (
        "Com as mesmas perguntas em cada módulo, os estudantes comparam os modelos sem "
        "reduzi-los a uma lista de nomes. O professor percebe se a dificuldade está em um "
        "conceito específico ou na leitura de dados e gráficos, que atravessa todos os módulos. "
        "A Figura 1 apresenta a tela inicial da plataforma. Ela reúne o percurso de aulas, os "
        "módulos e os materiais de apoio que serão utilizados na sequência."
    ),
]

CANDIDATES = [
    (
        "B1_v1",
        0,
        """- O produto educacional deste projeto junta um ambiente web em português brasileiro e um roteiro de aulas destinado a turmas do Ensino Médio.
- Como tudo funciona diretamente no navegador com conjuntos artificiais de dados e cálculos locais na própria máquina, não há criação de contas nem envio de respostas ou coleta de informações pessoais.
- Mesmo quando a internet da escola oscila, basta abrir o site nos computadores ou no projetor para ajudar o professor de Computação a conduzir explicações e conversas em sala.""",
    ),
    (
        "B1_v2",
        0,
        """- Pensado para o Ensino Médio, este produto educacional combina uma sequência de atividades didáticas com uma página interativa inteiramente em língua portuguesa.
- A ferramenta roda direto no navegador usando cenários simulados e executando o processamento no computador do usuário, sem pedir cadastro, login ou qualquer guarda de dados pessoais.
- Esse desenho funciona bem sob conectividade restrita e apoia a mediação do docente de Computação em sala, seja no projetor ou nos equipamentos da turma.""",
    ),
    (
        "B2_v1",
        1,
        """- O ambiente organiza cinco unidades introdutórias de machine learning: regressão linear, máquina de vetores de suporte (SVM), k-vizinhos mais próximos (k-NN), árvore de decisão e k-means.
- Longe de listar comandos soltos, as tarefas juntam previsão numérica, classificação e formação de grupos para a turma comparar o funcionamento de cada técnica.
- Cada módulo trabalha noções matemáticas próprias: função, linha de tendência e resíduos ou erros na regressão linear; fronteira com margem entre classes na SVM; distância entre pontos no k-NN; recálculo de centroides pela média no k-means; e regras encadeadas na árvore.
- Menor rigor formal em certas etapas não diminui nenhuma atividade, pois responde ao repertório de iniciantes e torna visível no gráfico ou na regra algo discutível em aula.""",
    ),
    (
        "B2_v2",
        1,
        """- A proposta reúne cinco módulos iniciais sobre machine learning sem formar uma lista técnica isolada: regressão linear, SVM, k-vizinhos mais próximos, árvore de decisão e k-means.
- O conjunto coloca lado a lado tarefas de estimativa de valores, separação em classes e agrupamento para evidenciar diferenças matemáticas entre os modelos.
- Nessa estrutura, a regressão linear aborda funções, reta de ajuste e erros ou resíduos; a SVM posiciona fronteira com margem; o k-NN observa distância entre pontos; o k-means atualiza centroides pela média; e a árvore encadeia condições.
- Adequar a formalização matemática ao perfil de jovens iniciantes busca apenas expor no gráfico ou na regra relações claras para debate em classe, mantendo igual importância entre os módulos.""",
    ),
    (
        "B3_v1",
        2,
        """- Além de compartilharem o mesmo site, os módulos ligam-se por questões repetidas que levam os alunos a identificar de onde vem cada dado e qual resposta se espera antes de alterar ajustes.
- A saída produzida varia de acordo com a lógica de cada técnica estudada.
- Enquanto a reta calcula uma estimativa numérica, a SVM posiciona uma divisória para separar casos rotulados, o k-NN consulta pontos próximos, a árvore segue testes condicionais e o k-means organiza elementos mesmo sem categorias prévias.""",
    ),
    (
        "B3_v2",
        2,
        """- Para superar módulos desconexos na página, perguntas recorrentes guiam a turma a checar a origem da informação disponível e o tipo de resultado esperado antes de testar mudanças.
- Cada modelo entrega uma resposta distinta ao final desse percurso.
- Assim, a regressão gera previsões numéricas pela reta, a SVM separa exemplos rotulados com uma fronteira, o k-NN examina vizinhos próximos, a árvore percorre regras condicionais e o k-means agrupa pontos na ausência de rótulos prévios.""",
    ),
    (
        "B4_v1",
        3,
        """- Repetir o mesmo roteiro de perguntas nos cinco módulos faz os jovens compararem modelos sem memorizar apenas nomes soltos de algoritmos.
- Essa rotina mostra ao professor se uma dificuldade pertence a um conceito específico ou à leitura de dados e gráficos que cruza todos os temas.
- Ilustrando essa organização, a Figura 1 exibe a tela inicial da plataforma, reunindo o percurso de aulas, os módulos e os materiais de apoio previstos para a sequência.""",
    ),
    (
        "B4_v2",
        3,
        """- Ao responder às mesmas questões em cada etapa, os estudantes estabelecem paralelos entre as técnicas e evitam reduzir os modelos a uma simples lista de termos.
- O docente ganha um indicador direto para diferenciar falhas num conceito específico de entraves na leitura de dados e gráficos ao longo de todo o curso.
- A Figura 1 traz a página principal da ferramenta, concentrando o trajeto das aulas, os cinco módulos e os materiais de apoio utilizados na sequência.""",
    ),
]

FORBIDDEN_PATTERNS = [
    r"\bLíngua Portuguesa\b",
    r"\bgradua[cç][aã]o\b",
    r"\bensino superior\b",
    r"\b7Cs\b",
    r"\b(buscamos|observamos|analisamos|encontramos|realizamos|utilizamos|propomos|apresentamos|construímos)\b",
]


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
    t = re.sub(r"\s*\([A-ZÁÉÍÓÚÂÊÔÃÕÇ\s,;]+\d{4},\s*p\.\s*\d*\)?\.?\s*$", ".", t)
    return t


def sentence_audit(orig: str, gen: str) -> tuple[int, int, float]:
    os_list = [s for s in re.split(r"(?<=[.!?])\s+", orig) if len(s.split()) > 4]
    gs_list = [s for s in re.split(r"(?<=[.!?])\s+", gen) if len(s.split()) > 4]
    max_sims = [
        max((difflib.SequenceMatcher(None, gs, os).ratio() for os in os_list), default=0.0)
        for gs in gs_list
    ]
    copied = sum(1 for m in max_sims if m > 0.65)
    worst = max(max_sims, default=0.0)
    return copied, len(gs_list), worst


def main() -> None:
    results = []
    for i, (name, orig_idx, top) in enumerate(CANDIDATES, 1):
        ka = "0s" if i == len(CANDIDATES) else "5m"
        t0 = time.time()
        out = ask_raw(top, temp=0.68, keep_alive=ka)
        t_clean = re.sub(r"(?m)^-\s*", "", top).replace("\n", " ")
        topic_sim = difflib.SequenceMatcher(None, t_clean, out).ratio()
        copied, total_s, worst_s = sentence_audit(ORIG_PARAS[orig_idx], out)
        leaks = [
            m.group(0)
            for pat in FORBIDDEN_PATTERNS
            for m in re.finditer(pat, out, flags=re.IGNORECASE)
        ]
        header = (
            f"=== {name} ({time.time()-t0:.1f}s | topic={len(t_clean.split())}w -> "
            f"out={len(out.split())}w | topic_sim={topic_sim:.2f} | "
            f"orig>65%={copied}/{total_s} max_s={worst_s:.2f} | leaks={leaks}) ==="
        )
        print(f"\n{header}\n{out}", flush=True)
        results.append((name, header, out))

    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_1_v5.txt")
    out_path.write_text(
        "\n\n".join(f"{h}\n{o}" for _, h, o in results) + "\n",
        encoding="utf-8",
    )
    print(f"\nSalvo em {out_path}", flush=True)


if __name__ == "__main__":
    main()
