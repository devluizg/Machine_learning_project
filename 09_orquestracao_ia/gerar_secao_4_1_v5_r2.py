#!/usr/bin/env python3
"""Segunda rodada de candidatos (v3/v4) para a Seção 4.1 no luiz-academico v5.0,
corrigindo precisão conceitual, tempo verbal presente/futuro e naturalidade."""
import time
from pathlib import Path
from gerar_secao_4_1_v5 import (
    ORIG_PARAS,
    FORBIDDEN_PATTERNS,
    ask_raw,
    sentence_audit,
)
import difflib
import re

CANDIDATES_R2 = [
    (
        "B1_v3",
        0,
        """- Este produto educacional destina-se ao Ensino Médio e junta uma sequência didática com uma plataforma interativa em português brasileiro.
- O sistema funciona direto no navegador utilizando cenários sintéticos, executando todos os cálculos no computador local sem exigir cadastro de usuário, envio de respostas ou coleta de dados pessoais.
- Como basta abrir a página nos computadores ou no projetor, seu emprego se mantém viável sob conectividade limitada e apoia a mediação do professor de Computação, preservando o espaço da explicação e do diálogo em aula.""",
    ),
    (
        "B1_v4",
        0,
        """- Voltado a turmas do Ensino Médio, o produto articula aulas planejadas em sequência didática e um ambiente web interativo escrito em português brasileiro.
- Todo o processamento ocorre na própria máquina, direto no navegador e com dados sintéticos, dispensando login, criação de contas, envio de respostas discentes ou recolhimento de dados pessoais.
- Essa estrutura favorece o acesso em escolas com internet limitada via projetor ou computadores, funcionando como suporte à mediação docente em Computação sem substituir a explicação e o debate conduzidos pelo professor.""",
    ),
    (
        "B2_v3",
        1,
        """- A plataforma traz cinco módulos iniciais de machine learning: regressão linear, máquina de vetores de suporte (SVM), k-vizinhos mais próximos (k-NN), árvore de decisão e k-means.
- Em lugar de formar uma vitrine de comandos desconexos, esses módulos confrontam previsão numérica, classificação e formação de grupos, ocupando todos lugar central na sequência.
- Cada abordagem mobiliza fundamentos matemáticos específicos: a regressão linear trabalha função e linha de tendência para prever valores e apurar erros ou resíduos, enquanto a SVM separa classes por meio de fronteira e margem.
- Completando o quadro, o k-NN examina a distância entre pontos, o k-means recalcula centroides pela média e a árvore encadeia condições, sendo que diferenças no grau de formalização apenas acompanham o repertório de estudantes iniciantes para deixar as relações visíveis no gráfico ou na regra em debate.""",
    ),
    (
        "B2_v4",
        1,
        """- O percurso reúne cinco unidades introdutórias de machine learning — regressão linear, SVM, k-vizinhos mais próximos, árvore de decisão e k-means — para comparar tarefas de estimativa numérica, classificação e agrupamento sem reduzi-las a comandos avulsos.
- Todos os módulos têm peso central na proposta por mobilizarem camadas matemáticas próprias na sala de aula.
- Na regressão linear, função e linha de tendência sustentam a previsão e o cálculo de erros ou resíduos; na SVM, uma fronteira com margem divide classes; no k-NN, destaca-se a distância entre pontos; no k-means, centroides são atualizados pela média; e na árvore, condições lógicas são encadeadas.
- Variar o nível de formalismo não rebaixa nenhum conteúdo, pois adapta a visualização no gráfico ou na regra ao perfil de jovens iniciantes para viabilizar a discussão coletiva.""",
    ),
    (
        "B3_v3",
        2,
        """- Os cinco módulos não apenas dividem o mesmo site, mas se integram por perguntas recorrentes que orientam a leitura da turma em toda atividade.
- Antes de testar qual ajuste altera o comportamento do modelo, os estudantes precisam identificar de onde provém o dado disponível e qual tipo de resposta se espera dele.
- A saída muda conforme o funcionamento de cada abordagem: a reta gera um valor numérico, a SVM posiciona uma fronteira entre exemplos rotulados, o k-NN consulta casos vizinhos, a árvore segue regras condicionais e o k-means reorganiza pontos sem contar com categorias prévias.""",
    ),
    (
        "B3_v4",
        2,
        """- Para além da convivência na mesma plataforma, questões comuns atravessam os módulos e levam os alunos a checar a origem do dado e o resultado esperado antes de mexer nos parâmetros.
- Cada modelo responde a essa investigação de maneira própria.
- Enquanto a reta entrega previsão numérica e a SVM traça fronteira separando exemplos rotulados, o k-NN busca exemplos próximos, a árvore percorre condições encadeadas e o k-means agrupa os pontos trabalhando na ausência de rótulos anteriores.""",
    ),
    (
        "B4_v3",
        3,
        """- Empregar sempre as mesmas perguntas nos módulos ajuda os estudantes a comparar modelos sem transformá-los em mera lista de nomes memorizados.
- Ao mesmo tempo, o professor passa a notar se uma eventual dúvida vem de um conceito particular ou de dificuldades mais amplas na leitura de dados e gráficos presentes em toda a sequência.
- Apresentando essa organização inicial, a Figura 1 mostra a tela principal da plataforma com o roteiro das aulas, os módulos e os materiais de apoio que serão empregados na intervenção.""",
    ),
    (
        "B4_v4",
        3,
        """- Repetir esse conjunto de questões em cada atividade permite que a turma confronte os modelos para além de uma lista decorada de designações.
- Para o docente, essa padronização evidencia quando o obstáculo dos alunos se concentra em certa noção técnica ou na leitura geral de gráficos e dados que cruza todos os módulos.
- A Figura 1 ilustra a página inicial do ambiente digital, reunindo a trilha de aulas, os cinco módulos interativos e os materiais de apoio previstos para a sequência didática.""",
    ),
]


def main() -> None:
    results = []
    for i, (name, orig_idx, top) in enumerate(CANDIDATES_R2, 1):
        ka = "0s" if i == len(CANDIDATES_R2) else "5m"
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

    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_1_v5_r2.txt")
    out_path.write_text(
        "\n\n".join(f"{h}\n{o}" for _, h, o in results) + "\n",
        encoding="utf-8",
    )
    print(f"\nSalvo em {out_path}", flush=True)


if __name__ == "__main__":
    main()
