#!/usr/bin/env python3
"""Parte 1 (Blocos 1 a 6) da Seção 4.4 no luiz-academico v5.0 (temp=0.67)."""
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

ORIG_BLOCKS_4_4_P1 = {
    "B1": (
        "A sequência será aplicada em uma turma de Ensino Médio sob docência do pesquisador, "
        "já definida para o período de novembro de 2026. Serão oito encontros de cerca de "
        "cinquenta minutos, dentro do componente curricular acordado com a escola. O laboratório "
        "de informática dispõe de 20 computadores conectados à internet, e Chromebooks completarão "
        "o acesso individual quando necessário. A aplicação e a produção de dados dependerão "
        "das autorizações institucionais e éticas aplicáveis."
    ),
    "B2": (
        "Todo encontro mantém a mesma estrutura, mesmo quando o modelo muda. A aula abre com "
        "uma situação ou pergunta que delimita o problema. Após registrar uma breve previsão "
        "inicial, cada estudante explora os controles de forma autônoma antes do debate coletivo "
        "e da síntese docente no fechamento. Essa rotina dá continuidade às aulas e integra a "
        "plataforma ao trabalho de construir e revisar hipóteses, evitando que o uso do site "
        "funcione como simples intervalo entre explicações."
    ),
    "B3": (
        "O primeiro encontro serve para nivelar conceitos. Antes de qualquer modelo, a turma "
        "discute aplicações cotidianas de inteligência artificial. Depois distingue os dados e a "
        "regra do modelo, até apontar o que seria entregue ao sistema e o que se espera dele. O "
        "diagnóstico inicial é individual e acontece no começo desse encontro, antes da discussão, "
        "ou na aula anterior, conforme o tempo. Registra ideias de partida, sem antecipar os "
        "nomes técnicos que aparecem depois."
    ),
    "B4": (
        "Do segundo ao sexto encontro entram, um por aula, os cinco módulos da plataforma, da "
        "regressão linear aos modelos de classificação e agrupamento. No segundo encontro, a "
        "organização da tabela da turma antecede a regressão linear. Cada aula retoma elementos "
        "anteriores para evitar que os modelos fiquem isolados em uma única experiência."
    ),
    "B5": (
        "A regressão linear e a SVM abrem a parte dos modelos supervisionados. Na linear, a "
        "turma identifica a linha de tendência no plano cartesiano para fazer previsões e "
        "compará-las aos valores observados, introduzindo a noção de erro. A SVM retoma o uso "
        "de exemplos conhecidos e direciona o debate para a fronteira que separa classes e para "
        "a margem em torno dessa divisão. Essa sequência imediata permite contrastar a previsão "
        "de um valor numérico com a definição de uma categoria, mostrando que ambas dependem "
        "dos dados e das escolhas do modelo."
    ),
    "B6": (
        "O k-NN e a árvore de decisão são duas maneiras de chegar a uma classificação. No k-NN, "
        "os estudantes observam o papel da distância e do número de vizinhos na votação; na "
        "árvore, acompanham regras condicionais e os caminhos até uma decisão. Comparar os dois "
        "afasta a ideia de que exista um algoritmo melhor que os outros. Ambos usam dados e "
        "regras, cada um à sua maneira, e entregam saídas que precisam ser lidas à luz do "
        "problema e dos exemplos disponíveis."
    ),
}

TOPICS_4_4_P1 = [
    (
        "B1",
        """- A aplicação dessa sequência didática ocorrerá em uma turma do Ensino Médio regida pelo próprio pesquisador, estando o período definido para novembro de 2026.
- O planejamento prevê oito encontros com duração aproximada de cinquenta minutos cada, inseridos no componente curricular combinado com a escola.
- No laboratório de informática há vinte computadores ligados à internet, e Chromebooks serão acrescentados para assegurar o acesso individual sempre que necessário.
- Tanto a realização das aulas quanto a produção de dados dependerão das autorizações institucionais e éticas exigidas.""",
    ),
    (
        "B2",
        """- Mesmo mudando o modelo estudado a cada dia, todos os encontros seguem uma organização pedagógica constante.
- Cada aula começa com uma situação ou questão que delimita o problema, seguida pelo registro de uma previsão inicial breve e pela exploração autônoma dos controles pelos alunos, encerrando com debate em grupo e síntese conduzida pelo professor.
- Manter essa rotina confere unidade às aulas e integra a ferramenta à formulação e revisão de hipóteses, evitando que o site se torne apenas uma pausa entre explicações teóricas.""",
    ),
    (
        "B3",
        """- A primeira aula cumpre o papel de nivelar noções básicas junto à turma antes de introduzir qualquer técnica específica.
- No início desse encontro ou já na aula anterior dependendo do tempo disponível, os estudantes respondem individualmente ao diagnóstico inicial, levantando concepções de partida sem antecipar os nomes técnicos das etapas seguintes.
- Depois do diagnóstico, a turma conversa sobre aplicações cotidianas da inteligência artificial e passa a diferenciar dados e regra, apontando o que entra no sistema e qual resposta dele se espera.""",
    ),
    (
        "B4",
        """- Entre a segunda e a sexta aula entram em cena os cinco módulos do ambiente web, trabalhados um por encontro da regressão linear até as técnicas de classificação e agrupamento.
- Especificamente no segundo encontro, a organização coletiva da tabela da turma acontece antes de iniciar a regressão linear.
- Para impedir que cada técnica fique isolada em uma atividade solta, toda aula retoma noções vistas nos encontros precedentes.""",
    ),
    (
        "B5",
        """- Os módulos iniciais dedicados à aprendizagem supervisionada trazem a regressão linear e em seguida a SVM.
- Na etapa da regressão linear, os alunos localizam a linha de tendência no plano cartesiano para gerar estimativas e confrontá-las aos valores observados, introduzindo a ideia de erro.
- Já com a SVM a discussão retoma exemplos já conhecidos para observar a fronteira que divide classes e a margem em volta dessa separação, contrastando em aulas seguidas a previsão numérica e a definição de categorias como escolhas ligadas aos dados e ao modelo.""",
    ),
    (
        "B6",
        """- Como caminhos alternativos para tarefas de classificação surgem posteriormente o k-NN e a árvore de decisão.
- Enquanto no k-NN a turma investiga como a distância entre pontos e a quantidade de vizinhos definem a votação, na árvore de decisão acompanha regras condicionais pelos ramos até alcançar uma decisão.
- Colocar as duas estratégias lado a lado desfaz a noção de existir um algoritmo superior a todos os outros, já que ambas combinam dados e regras ao seu modo e fornecem saídas dependentes do problema e dos exemplos disponíveis.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_4_v5_p1.txt")
    results = []
    for name, top in TOPICS_4_4_P1:
        orig_txt = ORIG_BLOCKS_4_4_P1[name]
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
