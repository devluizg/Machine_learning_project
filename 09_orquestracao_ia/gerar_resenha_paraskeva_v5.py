#!/usr/bin/env python3
"""Converte os 5 parágrafos da resenha de Paraskeva, Alexiou e Panoutsos (2021)
em tópicos secos (eliminando 100% da sintaxe da IA de origem) e gera os 5 blocos
na voz do Autor 1 usando luiz-academico:latest (v5.0)."""
import json
import time
import urllib.request
from pathlib import Path

OUT_FILE = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/resenha_paraskeva_2021_v5.md")

INST_TOPICS = (
    "Escreva um texto acadêmico contínuo em português brasileiro desenvolvendo exatamente os "
    "pontos abaixo no estilo, vocabulário e construção de frases do autor de referência."
)

BLOCKS_TOPICS = [
    # Bloco 1: Apresentação e Objetivo
    """- Artigo "Computational Thinking through Creative Programming in a Computer Science Course" publicado em 2021 por Foteini Paraskeva, Aikaterini Alexiou e Stavros Emmanouil Panoutsos.
- Investiga a relação entre pensamento computacional e pensamento criativo no ensino de programação para futuros professores de Ciência da Computação no ensino superior.
- Premissa dos autores: habilidades tecnológicas e criativas são indispensáveis hoje para resolver problemas complexos, e ensinar programação não pode ficar restrito a código e técnica, devendo trabalhar diferentes capacidades cognitivas.
- Objetivo da pesquisa: criar e avaliar uma estrutura conceitual para estimular o pensamento criativo no ensino de programação usando um ambiente híbrido com ferramentas Web 2.0, unindo o modelo dos Seis Chapéus do Pensamento a uma teoria de desenvolvimento da criatividade.""",

    # Bloco 2: Fundamentação Teórica
    """- Base teórica aborda três visões sobre a criatividade: traço de personalidade, resultado do ambiente e processo cognitivo desenvolvido pela aprendizagem.
- Apoia-se em Torrance e Guilford para tratar das dimensões de fluência, elaboração, flexibilidade e originalidade.
- No pensamento computacional, baseia-se em Papert e Wing: conjunto de habilidades úteis em várias áreas além da programação (abstração, reconhecimento de padrões, decomposição de problemas, pensamento algorítmico, detecção de erros e organização de informações).
- Utiliza também o modelo dos Seis Chapéus do Pensamento, de Edward de Bono (cores branca, vermelha, preta, amarela, verde e azul), para organizar diferentes ângulos de análise, reflexão, colaboração e geração de ideias na solução de problemas.""",

    # Bloco 3: Metodologia
    """- Metodologia: estudo experimental de medidas repetidas com 33 alunos de graduação em Ciência da Computação da Universidade de Piraeus (Grécia), matriculados voluntariamente na disciplina eletiva Learning with Technology.
- Intervenção dividida em 5 fases dentro de um ambiente baseado em wiki chamado APT2C&CT, combinando as etapas criativas de Clinton e Hokanson (identificação do problema, preparação, incubação, iluminação e elaboração) com os Seis Chapéus do Pensamento.
- Alunos divididos em equipes de 2 a 3 integrantes; criaram cartazes, mapas conceituais, documentos sobre ambientes de programação educacional e planos de atividades usando Glogster, Cmaps, Scratch e Lego Mindstorms.
- Avaliação mista: parte quantitativa aplicou rubrica de 6 fatores (escala de 1 a 5) no pré e pós-teste analisada via teste t pareado no SPSS; parte qualitativa avaliou fluência, elaboração, flexibilidade e originalidade usando o teste qui-quadrado.""",

    # Bloco 4: Resultados
    """- Resultados mostraram diferenças entre a análise quantitativa e a qualitativa.
- No teste quantitativo (pré vs. pós-teste), não houve diferença estatisticamente significativa ao nível de 5% (t(32) = -0,950 e p = 0,174), não confirmando ganho estatístico de criatividade por essa rubrica.
- Já na avaliação qualitativa das produções, o teste qui-quadrado apontou diferença estatisticamente significativa na distribuição das equipes (qui-quadrado(1) = 9,308 e p = 0,002): das 13 equipes, 12 atingiram a terceira categoria e apenas 1 ficou na segunda categoria.
- A correlação de Spearman também revelou associação positiva entre fatores criativos, com destaque para imaginação e fluxo, indicando que o trabalho em equipe e os Seis Chapéus ajudaram na expressão criativa durante a aprendizagem de programação.""",

    # Bloco 5: Contribuições e Limitações Críticas
    """- Contribuição principal: proposta pedagógica que une criatividade, pensamento computacional, colaboração e ferramentas digitais na formação de futuros professores, indo além do ensino puramente técnico de programação.
- Limitações importantes do estudo: amostra pequena (apenas 33 estudantes), adesão voluntária e falta de um grupo de controle independente, o que impede generalizar os achados.
- Outros pontos críticos: o resultado quantitativo sem significância estatística pede cautela ao afirmar aumento real de criatividade, e a avaliação qualitativa ocorreu apenas no final das atividades, sem medir a evolução individual desde o início.
- Conclusão crítica: o trabalho traz boas ideias de ensino colaborativo e criativo para programação, mas exige novos estudos com amostras maiores, grupos comparativos e acompanhamento de longo prazo.""",
]


def ask_ollama(topics: str, keep_alive: str) -> tuple[str, float]:
    t0 = time.time()
    payload = {
        "model": "luiz-academico:latest",
        "messages": [{"role": "user", "content": f"{INST_TOPICS}\n\n{topics}"}],
        "stream": False,
        "keep_alive": keep_alive,
        "options": {
            "num_ctx": 1024,
            "temperature": 0.65,
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
    return data["message"]["content"].strip(), time.time() - t0


def main() -> None:
    generated_blocks = []
    t_start = time.time()
    for i, topics in enumerate(BLOCKS_TOPICS, 1):
        ka = "0s" if i == len(BLOCKS_TOPICS) else "5m"
        print(f"Gerando Bloco {i}/{len(BLOCKS_TOPICS)}...", flush=True)
        txt, dt = ask_ollama(topics, ka)
        w = len(txt.split())
        print(f"-> Bloco {i} concluído em {dt:.1f}s ({w} palavras):\n{txt}\n", flush=True)
        generated_blocks.append(txt)

    header = (
        "**PARASKEVA, Foteini; ALEXIOU, Aikaterini; PANOUTSOS, Stavros Emmanouil.** "
        "Computational Thinking through Creative Programming in a Computer Science Course. "
        "*International Journal of Innovation, Creativity and Change*, v. 15, n. 7, 2021.\n\n"
    )
    full_body = "\n\n".join(generated_blocks)
    OUT_FILE.write_text(header + full_body + "\n", encoding="utf-8")
    total_w = len(full_body.split())
    print(
        f"=== CONCLUÍDO EM {time.time() - t_start:.1f}s | TOTAL: {total_w} PALAVRAS ===",
        flush=True,
    )


if __name__ == "__main__":
    main()
