#!/usr/bin/env python3
"""Rodada 4 cirúrgica da Seção 4.4 para B1, B2, B4, B7, B9, B11 e B12."""
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

TOPICS_4_4_R4 = [
    (
        "B1_r4",
        "B1",
        """- A intervenção escolar acontecerá com uma turma de Ensino Médio já definida para novembro de 2026, conduzida pelo pesquisador no papel de professor.
- Serão realizados oito encontros de aproximadamente cinquenta minutos cada no componente curricular combinado com a escola.
- O laboratório oferece vinte computadores conectados à internet e contará ainda com Chromebooks para completar o acesso individual quando necessário, dependendo tanto a aplicação quanto a produção de dados das autorizações institucionais e éticas cabíveis.""",
    ),
    (
        "B2_r4",
        "B2",
        """- Todos os encontros seguem uma organização pedagógica constante, mesmo mudando o modelo estudado em cada aula.
- A aula começa com uma pergunta ou situação que delimita o problema, solicita um breve registro inicial de previsão pelos estudantes, segue para a exploração autônoma dos controles da plataforma e fecha com debate coletivo e síntese docente.
- Essa rotina confere continuidade às aulas e integra o site ao exercício de levantar e revisar hipóteses, evitando que a ferramenta funcione como mero intervalo entre explicações.""",
    ),
    (
        "B4_r4",
        "B4",
        """- Entre o 2º e o 6º encontro entrarão em sala os cinco módulos da plataforma, um por aula, partindo da regressão linear até modelos de classificação e agrupamento.
- No 2º encontro, antes de iniciar a regressão linear, a turma montará coletivamente a tabela simples com dados próprios.
- Todas as aulas retomarão elementos construídos nos encontros precedentes para impedir que os modelos fiquem isolados em atividades pontuais desconexas.""",
    ),
    (
        "B7_r4",
        "B7",
        """- No encontro dedicado ao k-means ocorre uma mudança importante na dinâmica, pois os pontos exibidos na tela não virão com categorias prévias, fazendo a atividade retornar à pergunta sobre o que se quer produzir com os dados e mostrando que agrupar por proximidade difere de escolher uma classe conhecida.
- Observar a atualização dos centroides e os pontos se reorganizando poderá exigir mais tempo de aula, já que distinguir agrupamento de classificação pode levar o professor a retomar termos trabalhados nos encontros anteriores.
- Para fechar o ciclo de modelos, uma síntese breve registrará como as cinco abordagens combinam dados e regras na geração de uma saída conforme o objetivo de cada tarefa.""",
    ),
    (
        "B9_r4",
        "B9",
        """- Esse encontro comparativo terá o papel de resgatar diferenças que possam ter ficado dispersas e preparar os alunos para o desafio final, levando o estudante a considerar a finalidade da tarefa diante dos dados disponíveis antes de escolher qualquer modelo.
- No fechamento, enquanto o núcleo comparável permitirá examinar mudanças frente ao diagnóstico inicial, o desafio inédito de transferência evidenciará a mobilização dos conceitos em novo contexto como dado adicional sem equiparação direta com questões mais simples.""",
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
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_4_v5_r4.txt")
    results = []
    for name, orig_key, top in TOPICS_4_4_R4:
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
