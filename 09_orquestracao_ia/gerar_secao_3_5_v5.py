#!/usr/bin/env python3
"""Gera a Seção 3.5 completa no luiz-academico v5.0 (temperature=0.65)
com 100% de fidelidade às ideias e tópicos secos com baixa similaridade sintática."""
import difflib
import re
import time
from pathlib import Path
from pipeline_v5_fiel import call_luiz_v5

OUT_FILE = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/secao_3_5_v5_fiel.md")

ORIG_TEXT = """A literatura e os documentos curriculares definem o posicionamento da proposta. Nela, o machine learning entra como conteúdo introdutório de Computação, superando o simples treinamento no uso de aplicativos. A sequência recorta ideias fundamentais e limites observáveis nas tarefas, sem antecipar uma formação universitária em algoritmos. Tanto os dados da própria turma quanto os cenários sintéticos visam mostrar a origem dos números e o efeito de alterar parâmetros. Dessa forma, a visualização sustenta comparações nas quais o estudante parte de uma hipótese para observar o gráfico e explicar como a regra do modelo transforma os dados em resultado. A análise buscará evidências em produções individuais contextualizadas, indo além da contagem de acertos sem prometer efeitos causais generalizáveis.

Embora a literatura já reúna ferramentas e experiências no ensino de IA e machine learning na Educação Básica, os estudos cobram maior clareza sobre conteúdos e estratégias nos contextos de aplicação, ao lado de avaliações mais rigorosas (Martins e Gresse von Wangenheim, 2023; Rauber e Gresse von Wangenheim, 2023; Sanusi et al., 2023). Assim, este projeto contribui ao analisar, em uma turma de Ensino Médio do próprio pesquisador, uma sequência didática que articula a visualização de cinco modelos a instrumentos com critérios explícitos.

A qualidade da pesquisa dependerá do alinhamento metodológico entre o referencial e o produto desenvolvido. Para isso, os recursos do site refletirão objetivos de aprendizagem presentes nas atividades e nos instrumentos de coleta, garantindo que as conclusões respeitem estritamente o alcance das evidências produzidas."""

TOPICS_BLOCKS = [
    # Bloco 1 (Posicionamento e recorte do ML na escola)
    """- As diretrizes curriculares e os estudos da área fundamentam a proposta, em que o machine learning entra como conteúdo introdutório de Computação e não como mero treinamento prático em programas prontos.
- O percurso pedagógico foca em conceitos fundamentais e limites práticos dos algoritmos adequados ao Ensino Médio, combinando dados sintéticos e tabelas dos estudantes para ligar parâmetros aos resultados na tela.
- A visualização apoia o ciclo de levantar hipóteses, observar o gráfico e justificar a decisão do modelo, buscando evidências de aprendizagem em produções contextualizadas sem prometer efeitos causais amplos.""",

    # Bloco 2 (Lacunas da literatura e contribuição da pesquisa)
    """- Embora existam materiais e ferramentas para o ensino de machine learning na Educação Básica, as revisões da literatura apontam a carência de clareza nas estratégias e de avaliações mais rigorosas (Martins e Gresse von Wangenheim, 2023; Rauber e Gresse von Wangenheim, 2023; Sanusi et al., 2023).
- Frente a essas lacunas, este projeto traz sua contribuição ao investigar uma sequência didática com cinco modelos interativos aplicada pelo próprio professor-pesquisador em sua turma de Ensino Médio.
- A proposta busca detalhar o contexto de aplicação e estruturar instrumentos de avaliação com critérios claros de observação sobre o raciocínio dos alunos.""",

    # Bloco 3 (Alinhamento metodológico e alcance das evidências)
    """- A validade do trabalho apoia-se no alinhamento rigoroso entre a fundamentação teórica, a ferramenta interativa criada e as atividades pedagógicas realizadas.
- As telas e os botões da plataforma foram desenhados para responder diretamente aos objetivos de aprendizagem avaliados nos instrumentos de coleta.
- Esse cuidado metodológico garante que a discussão final dos resultados respeite com rigor os limites e as evidências produzidas durante as aulas na escola.""",
]


def main() -> None:
    generated_paras = []
    for i, top in enumerate(TOPICS_BLOCKS, 1):
        ka = "0s" if i == len(TOPICS_BLOCKS) else "5m"
        t0 = time.time()
        print(f"Gerando Bloco {i}/{len(TOPICS_BLOCKS)} da Seção 3.5...", flush=True)
        txt = call_luiz_v5(top, keep_alive=ka, is_third_person=True)
        print(f"-> Bloco {i} concluído em {time.time()-t0:.1f}s ({len(txt.split())}w):\n{txt}\n", flush=True)
        generated_paras.append(txt)

    OUT_FILE.write_text("\n\n".join(generated_paras) + "\n", encoding="utf-8")

    # Auditoria de similaridade frase por frase contra ORIG_TEXT
    orig_paras = ORIG_TEXT.strip().split("\n\n")
    total_s, high_s = 0, 0
    for idx, (o, g) in enumerate(zip(orig_paras, generated_paras), 1):
        os_list = [s for s in re.split(r"(?<=[.!?])\s+", o) if len(s.split()) > 4]
        gs_list = [s for s in re.split(r"(?<=[.!?])\s+", g) if len(s.split()) > 4]
        copied = sum(
            1 for gs in gs_list if max(difflib.SequenceMatcher(None, gs, os).ratio() for os in os_list) > 0.65
        )
        total_s += len(gs_list)
        high_s += copied
        print(f"Auditoria Bloco {idx}: {copied}/{len(gs_list)} frases >65% similares ao original")
    print(f"\n=== AUDITORIA FINAL SEÇÃO 3.5: {high_s}/{total_s} frases >65% similares ===", flush=True)


if __name__ == "__main__":
    main()
