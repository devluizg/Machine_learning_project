#!/usr/bin/env python3
"""Regenera Seção 3.5 com tópicos descolados da sintaxe da IA e vocabulário simples do autor."""
import re
import time
from pathlib import Path
from pipeline_v5_fiel import call_luiz_v5

OUT_FILE = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/secao_3_5_v5_fiel.md")

TOPICS_BLOCKS = [
    # Bloco 1 (Posicionamento e recorte)
    """- As diretrizes do currículo e os artigos sobre Computação mostram que ensinar machine learning no colégio não pode ser só treinar a turma a usar programas prontos; por isso, a proposta trata a matéria como um conteúdo de formação da própria Computação.
- O plano de aula não quer adiantar matérias difíceis de faculdade, mas focar nas ideias básicas e nos limites práticos que os alunos conseguem ver funcionando na tela.
- Para isso, a ferramenta combina dados sintéticos com tabelas que os próprios estudantes montaram na sala: os dados sintéticos servem para mexer nos botões e ver o resultado mudar na hora, enquanto os dados da turma mostram de onde vieram aqueles números.""",

    # Bloco 2 (Ciclo pedagógico e evidências de aprendizagem)
    """- O uso da tela apoia a ideia de pedir que o aluno faça uma previsão antes de testar, veja o gráfico mudar e depois explique com suas palavras qual regra produziu aquela decisão do computador.
- Na hora de avaliar o aprendizado dos alunos, a pesquisa não vai ficar apenas contando quem acertou ou errou mais questões de marcar X, nem quer provar regras gerais que sirvam para qualquer escola do país.
- O foco da análise será olhar com cuidado o que cada estudante escreveu e falou durante as tarefas, procurando entender como as ideias dele foram mudando dentro da realidade daquela sala de aula.""",

    # Bloco 3 (Lacunas da literatura e contribuição da pesquisa)
    """- Várias pesquisas recentes apontam que faltam explicações claras sobre como aplicar essas aulas na prática e que faltam instrumentos de avaliação bem estruturados na Educação Básica, como alertam Martins e Gresse von Wangenheim (2023), Rauber e Gresse von Wangenheim (2023) e Sanusi et al. (2023).
- É justamente para ajudar a diminuir esse problema que este trabalho foi feito, analisando a aplicação de uma sequência com cinco modelos diferentes (regressão linear, SVM, k-NN, árvore de decisão e k-means).
- O diferencial é que o próprio professor da matéria aplicou as atividades em sua turma de Ensino Médio, utilizando folhas de tarefas e critérios bem definidos para acompanhar o raciocínio dos jovens.""",

    # Bloco 4 (Alinhamento metodológico entre teoria, telas e avaliação)
    """- Para que o trabalho tenha valor científico e pedagógico, foi preciso manter uma ligação direta entre o que os autores da teoria dizem, as telas do site criado e as tarefas feitas em sala.
- Cada botão, gráfico e pergunta colocada na plataforma foi pensado para atender aos objetivos de ensino que seriam cobrados nos instrumentos de pesquisa.
- Essa organização garante que as conclusões da pesquisa não passem do ponto e mostrem exatamente aquilo que os dados das aulas conseguiram comprovar na prática escolar.""",
]

def main():
    paras = []
    for i, top in enumerate(TOPICS_BLOCKS, 1):
        ka = "0s" if i == len(TOPICS_BLOCKS) else "5m"
        t0 = time.time()
        print(f"Gerando Bloco {i}/{len(TOPICS_BLOCKS)}...", flush=True)
        txt = call_luiz_v5(top, keep_alive=ka, is_third_person=True)
        # Limpezas pontuais de vazamentos do Autor 1
        txt = re.sub(r"\bno contexto da disciplina de Língua Portuguesa\b", "no contexto da disciplina", txt)
        txt = re.sub(r"\bpróprio autor desta dissertação\b", "próprio professor-pesquisador", txt)
        txt = re.sub(r"\bna tela da computador\b", "na tela do computador", txt)
        print(f"-> Bloco {i} ({time.time()-t0:.1f}s):\n{txt}\n", flush=True)
        paras.append(txt)

    full_text = "\n\n".join(paras)
    OUT_FILE.write_text(full_text + "\n", encoding="utf-8")
    print(f"=== SALVO EM {OUT_FILE} ({len(full_text.split())} palavras) ===")

if __name__ == "__main__":
    main()
