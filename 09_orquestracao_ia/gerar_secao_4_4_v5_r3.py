#!/usr/bin/env python3
"""Rodada 3 unificada da Seção 4.4 (Blocos B1, B2, B3, B4, B7, B8, B9, B11, B12)
com verbos no futuro em todos os tópicos para manter 3ª pessoa futura/presente fiel."""
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
from gerar_secao_4_4_v5_p1 import ORIG_BLOCKS_4_4_P1
from gerar_secao_4_4_v5_p2 import ORIG_BLOCKS_4_4_P2

ORIG_4_4 = {**ORIG_BLOCKS_4_4_P1, **ORIG_BLOCKS_4_4_P2}

TOPICS_4_4_R3 = [
    (
        "B1_r3",
        "B1",
        """- A sequência didática será aplicada em uma turma de Ensino Médio sob regência do pesquisador, já definida para novembro de 2026.
- O trabalho em sala acontecerá em oito encontros de cerca de cinquenta minutos dentro do componente curricular combinado com a escola.
- Os vinte computadores com internet do laboratório receberão o reforço de Chromebooks para o acesso individual quando preciso, ficando a aplicação e a produção de dados condicionadas às autorizações institucionais e éticas aplicáveis.""",
    ),
    (
        "B2_r3",
        "B2",
        """- Mesmo quando o modelo mudar de uma aula para outra, todos os encontros manterão uma mesma estrutura interna.
- Cada aula abrirá com uma situação ou pergunta que delimita o problema, pedirá o registro breve de uma previsão inicial, dará espaço à exploração autônoma dos controles na plataforma e fechará com debate coletivo e síntese docente.
- Essa rotina dará continuidade às aulas e integrará o site ao trabalho de levantar e revisar hipóteses, impedindo que seu uso funcione como mero intervalo entre explicações.""",
    ),
    (
        "B3_r3",
        "B3",
        """- O primeiro encontro servirá para nivelar noções iniciais junto aos estudantes antes de apresentar qualquer modelo específico.
- No início dessa aula ou na anterior conforme o tempo disponível, cada aluno responderá individualmente ao diagnóstico inicial, registrando ideias de partida sem antecipar os nomes técnicos das etapas seguintes.
- Em seguida, a turma discutirá aplicações cotidianas da inteligência artificial e passará a distinguir dados e regra do modelo, apontando o que entra no sistema e qual resposta dele se espera.""",
    ),
    (
        "B4_r3",
        "B4",
        """- Do 2º ao 6º encontro entrarão em sala os cinco módulos da plataforma, um por aula, avançando da regressão linear até modelos de classificação e agrupamento.
- Antes da atividade de regressão linear no 2º encontro, a turma organizará coletivamente uma pequena tabela com dados simples próprios.
- Cada encontro retomará elementos das aulas anteriores para impedir que os modelos fiquem isolados em experiências desconexas.""",
    ),
    (
        "B7_r3",
        "B7",
        """- Ao trabalhar o k-means, surgirá uma mudança importante porque os pontos exibidos na tela virão sem categorias dadas de antemão; a atividade voltará à pergunta sobre o que se pretende produzir com os dados e mostrará que formar grupos por proximidade não equivale a escolher uma classe conhecida.
- Observar a atualização dos centroides e a reorganização dos pontos poderá exigir mais tempo em aula, pois diferenciar agrupamento e classificação levará o docente a retomar a linguagem dos encontros anteriores.
- Uma síntese breve registrará ainda como todos os cinco modelos articulam dados e regras para gerar uma saída conforme a finalidade de cada tarefa.""",
    ),
    (
        "B8_r3",
        "B8",
        """- No 7º encontro, a turma comparará os cinco modelos já estudados diante de novas situações-problema, justificando com base nos dados disponíveis se cada caso exige previsão numérica, escolha de categoria ou formação de grupos.
- Já no 8º encontro, cada estudante responderá primeiro ao bloco de questões equivalentes às do diagnóstico e resolverá na sequência um desafio inédito de transferência, no qual indicará os dados necessários para ligar a tarefa a um modelo compatível e explicará o efeito esperado caso algum dado ou parâmetro varie na regra.""",
    ),
    (
        "B9_r3",
        "B9",
        """- A aula comparativa recuperará diferenças que possam ter ficado dispersas e preparará a transição para o desafio final, levando o estudante a considerar a finalidade da tarefa diante dos dados disponíveis antes de escolher o modelo.
- Enquanto o núcleo comparável permitirá examinar mudanças frente ao diagnóstico inicial, o desafio inédito de transferência mostrará como os conceitos são mobilizados em novo contexto, entrando como evidência adicional sem equiparação direta com questões mais simples.""",
    ),
    (
        "B11_r3",
        "B11",
        """- O roteiro preliminar dos oito encontros articulará objetivos de aprendizagem e tempo previsto às ações de mediação docente com perguntas formativas, indicando também adaptações de infraestrutura escolar e limites didáticos por módulo.
- Como a plataforma utilizada em sala não armazenará nenhuma resposta digitada pelos estudantes, o corpus documental da pesquisa reunirá o diagnóstico inicial, o instrumento final completo, os três registros intermediários individuais e as anotações do professor.""",
    ),
    (
        "B12_r3",
        "B12",
        """- Antes da entrada em campo, a versão do site usada nas aulas será conferida frente aos recursos previstos na sequência didática; caso os cenários da plataforma apresentem dados, textos de apoio ou representações matemáticas diferentes dos previstos no roteiro, a divergência será corrigida ou explicada aos estudantes.
- Essa conferência prévia impedirá que a pesquisa analise alunos como se tivessem passado por outro recurso e garantirá que a plataforma e os instrumentos avaliem exatamente o que foi trabalhado em classe.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_4_v5_r3.txt")
    results = []
    for name, orig_key, top in TOPICS_4_4_R3:
        orig_txt = ORIG_4_4[orig_key]
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
