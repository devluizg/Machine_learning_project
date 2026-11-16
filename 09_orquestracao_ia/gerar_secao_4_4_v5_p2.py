#!/usr/bin/env python3
"""Parte 2 (Blocos 7 a 12) da Seção 4.4 no luiz-academico v5.0 (temp=0.67),
ancorada no planejamento futuro/modal em 3ª pessoa."""
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

ORIG_BLOCKS_4_4_P2 = {
    "B7": (
        "O k-means traz uma mudança: os pontos não vêm com categorias dadas de antemão. "
        "A atividade volta à pergunta sobre o que se quer produzir com os dados e mostra que "
        "formar grupos por proximidade não é escolher uma classe conhecida. A atualização dos "
        "centroides e a observação da reorganização dos pontos poderão exigir mais tempo, pois a "
        "diferença entre agrupamento e classificação pode levar o professor a retomar a linguagem "
        "dos encontros anteriores. Uma síntese breve registra o modo como os cinco modelos "
        "articulam dados e regras para gerar uma saída, destacando o que muda conforme a "
        "finalidade de cada tarefa."
    ),
    "B8": (
        "O sétimo encontro compara os cinco modelos. Diante de novas situações-problema, a turma "
        "justifica com base nos dados disponíveis se o caso exige previsão numérica, escolha de "
        "categoria ou formação de grupos. No oitavo encontro, cada estudante responde primeiro ao "
        "bloco de questões equivalentes às do diagnóstico e, na sequência, resolve um desafio de "
        "transferência inédito. Nessa etapa final, é preciso apontar os dados necessários para "
        "associar a tarefa a um modelo compatível, explicando o efeito esperado caso um parâmetro "
        "ou dado mude na regra."
    ),
    "B9": (
        "O encontro comparativo recupera diferenças que possam ter ficado dispersas e prepara a "
        "transferência para o desafio final. Ao justificar que tipo de saída o problema demanda "
        "a partir dos dados disponíveis, o estudante considera a finalidade da tarefa antes de "
        "escolher o modelo. Enquanto o núcleo comparável permite examinar mudanças frente ao "
        "diagnóstico, o desafio de transferência mostra como os conceitos são mobilizados em "
        "novo contexto, entrando como evidência adicional sem equiparação direta com questões "
        "mais simples."
    ),
    "B10": (
        "O trabalho na plataforma ocorrerá individualmente, com os computadores do laboratório e, "
        "conforme a disponibilidade confirmada no campo, Chromebooks para completar o acesso da "
        "turma. No segundo, no quarto e no sexto encontros, cada estudante também preencherá um "
        "registro curto antes e depois de explorar o site, cobrindo assim um exemplo de regressão, "
        "um de classificação e outro de agrupamento. Já o instrumento final será inteiramente "
        "individual. Caso o laboratório fique indisponível, o professor projetará os experimentos "
        "para a turma, preservando as pausas de previsão e explicação individual."
    ),
    "B11": (
        "O roteiro preliminar dos oito encontros articula objetivos de aprendizagem e tempo "
        "previsto às ações de mediação com questões formativas, indicando ainda adaptações de "
        "infraestrutura e limites didáticos por módulo. Sem armazenamento de respostas digitadas "
        "no site, o corpus reunirá o diagnóstico inicial e o instrumento final completo, somados "
        "aos três registros individuais intermediários e às anotações docentes."
    ),
    "B12": (
        "A versão do site usada no campo será conferida, antes da intervenção, com os recursos "
        "previstos na sequência. Se o cenário da plataforma tiver dados diferentes dos discutidos "
        "no roteiro da aula, a diferença será corrigida ou explicada aos estudantes; o mesmo vale "
        "para os textos de apoio e as representações matemáticas. A pesquisa não pode analisar "
        "estudantes como se tivessem passado por uma sequência diferente do recurso usado. Essa "
        "conferência prática garante que a plataforma e os instrumentos avaliem exatamente o que "
        "foi trabalhado nas aulas."
    ),
}

TOPICS_4_4_P2 = [
    (
        "B7",
        """- Na etapa dedicada ao k-means ocorre uma mudança prevista na sequência, pois os pontos exibidos não trazem categorias dadas de antemão; a proposta retoma a pergunta sobre o que se quer produzir com os dados e busca mostrar que formar grupos por proximidade difere de escolher uma classe conhecida.
- Acompanhar na tela a atualização dos centroides e a reorganização dos pontos poderá demandar tempo maior de mediação, uma vez que a diferença entre agrupamento e classificação pode exigir que o professor retome termos dos encontros anteriores.
- Para encerrar o ciclo de módulos, uma síntese breve registrará como os cinco modelos articulam dados e regras para gerar uma saída conforme a finalidade de cada tarefa.""",
    ),
    (
        "B8",
        """- No sétimo encontro, planeja-se comparar os cinco modelos diante de novas situações-problema, levando a turma a justificar pelos dados disponíveis se cada caso exige previsão numérica, escolha de categoria ou formação de grupos.
- Já no oitavo encontro, cada aluno responderá primeiramente ao conjunto de questões equivalentes às do diagnóstico e, na sequência prevista, enfrentará um desafio inédito de transferência.
- Nesse desafio final, caberá indicar que dados são necessários para vincular a tarefa a um modelo compatível e explicar o efeito esperado caso algum dado ou parâmetro varie na regra.""",
    ),
    (
        "B9",
        """- Pedagogicamente, o encontro comparativo tem a função de recuperar diferenças dispersas entre os modelos e preparar a transferência para o desafio final, levando o estudante a considerar primeiro a finalidade da tarefa diante dos dados antes de escolher um modelo.
- No fechamento, o núcleo comparável permitirá examinar alterações em relação ao diagnóstico inicial.
- Paralelamente, o desafio de transferência evidenciará como os conceitos são mobilizados em contexto inédito, compondo evidência complementar sem equiparação direta com itens mais simples.""",
    ),
    (
        "B10",
        """- A manipulação da plataforma ocorrerá individualmente nos computadores do laboratório e, caso confirmado no campo, com o apoio de Chromebooks para atender todos os alunos.
- Durante os encontros de número dois, quatro e seis, cada estudante preencherá ainda um registro curto antes e após explorar o site, cobrindo um caso de regressão, um de classificação e outro de agrupamento.
- O instrumento avaliativo final será totalmente individual; se o laboratório ficar indisponível, o docente projetará os experimentos preservando intervalos de previsão e explicação individual.""",
    ),
    (
        "B11",
        """- O roteiro provisório dos oito encontros articula objetivos de aprendizagem e duração prevista a ações de mediação com questões formativas, indicando também adaptações de infraestrutura e limites didáticos de cada módulo.
- Como o ambiente web não armazena respostas digitadas pelos estudantes, o corpus de análise reunirá o diagnóstico inicial, o instrumento final completo, os três registros intermediários individuais e as anotações docentes.""",
    ),
    (
        "B12",
        """- Antes do início na escola, a versão do site levada a campo passará por conferência prática frente aos recursos descritos na sequência didática.
- Se algum cenário da interface apresentar dados, textos de apoio ou representações matemáticas divergentes do roteiro de aula, a diferença será ajustada ou explicada à turma.
- Tal checagem prévia impede que a análise trate os jovens como se tivessem passado por um recurso distinto do utilizado e garante que os instrumentos avaliem exatamente o conteúdo trabalhado em sala.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_4_v5_p2.txt")
    results = []
    for i, (name, top) in enumerate(TOPICS_4_4_P2, 1):
        orig_txt = ORIG_BLOCKS_4_4_P2[name]
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
