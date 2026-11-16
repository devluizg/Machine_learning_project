#!/usr/bin/env python3
"""Gera os 4 blocos da Seção 4.5 (Materiais e limites do produto) no luiz-academico v5.0 (temp=0.67)."""
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

ORIG_BLOCKS_4_5 = {
    "B1": (
        "Além da plataforma, a aplicação contará com o diagnóstico inicial e três registros "
        "curtos de aula, somados às notas docentes e ao instrumento final com seu questionário de "
        "percepção. Nos registros intermediários, um campo recolhe a previsão prévia ao "
        "experimento e outro a explicação posterior. Já o questionário final consulta a turma "
        "sobre a clareza e o nível de dificuldade no manuseio do site, sem valer como evidência "
        "de aprendizagem."
    ),
    "B2": (
        "O produto não comprova aprendizagem só por existir. Serve para que professor e "
        "estudantes discutam dados e parâmetros do modelo em sala. A adequação didática do "
        "produto só poderá ser avaliada confrontando o planejamento com as condições reais do "
        "campo e as produções da turma, longe de constituir solução pronta para qualquer escola."
    ),
    "B3": (
        "Antes das aulas, um teste prático conferirá a abertura local do site nos computadores e "
        "a legibilidade da tela, checando ainda a resposta dos controles e a visibilidade no "
        "projetor. Caso algum equipamento falhe, o experimento seguirá projetado com pausas "
        "para registro individual. A mudança de organização vai para o registro docente, porque "
        "a forma de acesso ao recurso pode alterar as interações observadas. Manter uma atividade "
        "pedagogicamente equivalente vale mais do que insistir em uma configuração técnica que "
        "a escola não consiga sustentar."
    ),
    "B4": (
        "A mesma verificação confere se os estudantes compreendem os enunciados sem domínio "
        "prévio do jargão da área. Termos que vão de característica, vizinho e centroide até "
        "fronteira ou margem entram sempre acompanhados de exemplos visíveis e explicações "
        "situadas. Caso alguma pergunta gere dúvida recorrente, a revisão do enunciado ou da "
        "mediação será tratada como ajuste necessário ao produto, afastando a ideia de falha do "
        "estudante para remover barreiras linguísticas alheias ao conteúdo."
    ),
}

TOPICS_4_5 = [
    (
        "B1",
        """- Em conjunto com a plataforma web, a aplicação reunirá diagnóstico inicial, três registros breves realizados ao longo das aulas, anotações do professor e instrumento final acompanhado de questionário de percepção.
- Cada registro intermediário reserva um espaço para a previsão feita antes da atividade no site e outro para a explicação elaborada depois da exploração.
- Ao término da sequência, o questionário de percepção consulta os jovens sobre a clareza das orientações e eventuais dificuldades no uso da ferramenta, não entrando como prova de aprendizagem.""",
    ),
    (
        "B2",
        """- A simples existência do produto educacional não garante nem comprova aprendizagem por si só, uma vez que ele atua como apoio para docente e estudantes debaterem dados e parâmetros dos modelos em sala.
- Somente será possível julgar a adequação pedagógica da proposta ao confrontar o planejamento com as condições concretas da escola e com as produções da turma, sem tomá-la como receita pronta aplicável indistintamente a qualquer realidade.""",
    ),
    (
        "B3",
        """- Antes de começar as aulas, um teste técnico prévio verificará se o site abre localmente nas máquinas do laboratório, se os elementos ficam legíveis na tela, se os controles respondem adequadamente e se o projetor exibe com nitidez.
- Se algum equipamento apresentar falha, a condução passará à projeção coletiva mantendo pausas individuais para registro escrito, ficando essa alteração anotada pelo professor porque a forma de acesso pode influenciar as interações em sala.
- Para o bom andamento do trabalho, preservar uma tarefa pedagogicamente equivalente importa mais do que forçar um arranjo técnico insustentável para a escola.""",
    ),
    (
        "B4",
        """- Essa checagem prévia abrange também verificar se os alunos conseguem entender os enunciados sem conhecer previamente o vocabulário especializado da computação.
- Noções como característica, vizinho, centroide, fronteira e margem virão sempre ligadas a exemplos visíveis na tela e explicações situadas no contexto da atividade.
- Sempre que alguma questão provocar dúvida recorrente, a reformulação do texto ou da mediação docente será encarada como melhoria necessária ao próprio produto, evitando atribuir o problema à falta de capacidade do estudante para eliminar barreiras de linguagem alheias ao conteúdo.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_5_v5.txt")
    results = []
    for i, (name, top) in enumerate(TOPICS_4_5, 1):
        orig_txt = ORIG_BLOCKS_4_5[name]
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
