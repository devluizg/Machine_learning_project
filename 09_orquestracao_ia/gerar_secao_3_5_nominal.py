#!/usr/bin/env python3
"""Gera a Seção 3.5 no formato telegráfico ultra-curto (50-70w por bloco)
para forçar expansão 2x+ no luiz-academico v5.0 (topic->out sim < 0.35)."""
import difflib
import re
import time
from pathlib import Path
from pipeline_v5_fiel import call_luiz_v5

OUT_FILE = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/secao_3_5_v5_fiel.md")

ORIG_TEXT = """A literatura e os documentos curriculares definem o posicionamento da proposta. Nela, o machine learning entra como conteúdo introdutório de Computação, superando o simples treinamento no uso de aplicativos. A sequência recorta ideias fundamentais e limites observáveis nas tarefas, sem antecipar uma formação universitária em algoritmos. Tanto os dados da própria turma quanto os cenários sintéticos visam mostrar a origem dos números e o efeito de alterar parâmetros. Dessa forma, a visualização sustenta comparações nas quais o estudante parte de uma hipótese para observar o gráfico e explicar como a regra do modelo transforma os dados em resultado.

A análise buscará evidências em produções individuais contextualizadas, indo além da contagem de acertos sem prometer efeitos causais generalizáveis. Embora a literatura já reúna ferramentas e experiências no ensino de IA e machine learning na Educação Básica, os estudos cobram maior clareza sobre conteúdos e estratégias nos contextos de aplicação, ao lado de avaliações mais rigorosas (Martins e Gresse von Wangenheim, 2023; Rauber e Gresse von Wangenheim, 2023; Sanusi et al., 2023). Assim, este projeto contribui ao analisar, em uma turma de Ensino Médio do próprio pesquisador, uma sequência didática que articula a visualização de cinco modelos a instrumentos com critérios explícitos.

A qualidade da pesquisa dependerá do alinhamento metodológico entre o referencial e o produto desenvolvido. Para isso, os recursos do site refletirão objetivos de aprendizagem presentes nas atividades e nos instrumentos de coleta, garantindo que as conclusões respeitem estritamente o alcance das evidências produzidas."""

TOPICS_BLOCKS = [
    # Bloco 1 (~65w)
    """- Posicionamento teórico e curricular: ensino de machine learning na escola básica como conteúdo formativo de Computação, distinto de treino em aplicativos.
- Recorte previsto para o Ensino Médio: conceitos centrais e limites práticos nas tarefas, sem adiantar formação universitária.
- Papel dos dados na proposta: dados da turma mostram origem dos números, enquanto cenários sintéticos evidenciam efeito de parâmetros.
- Visualização em aula: estudante formula hipótese, observa gráfico e explica transformação de entrada em resultado pela regra.""",

    # Bloco 2 (~68w)
    """- Abordagem analítica futura: busca de evidências em produções individuais contextualizadas, além de contagem de acertos, sem prometer causalidade geral.
- Panorama da literatura: falta clareza de estratégias em sala e avaliações rigorosas em IA escolar (Martins e Gresse von Wangenheim, 2023; Rauber e Gresse von Wangenheim, 2023; Sanusi et al., 2023).
- Contribuição deste projeto: sequência didática com cinco modelos (regressão linear, SVM, k-NN, árvore de decisão e k-means) e critérios explícitos na turma do pesquisador.""",

    # Bloco 3 (~43w)
    """- Qualidade da investigação futura: alinhamento entre referencial teórico e produto educacional desenvolvido.
- Coerência da plataforma: telas do site refletem objetivos das atividades e dos instrumentos de coleta.
- Alcance das conclusões: resultados respeitarão rigorosamente as evidências geradas na turma participante.""",
]


def main() -> None:
    paras = []
    for i, top in enumerate(TOPICS_BLOCKS, 1):
        ka = "0s" if i == len(TOPICS_BLOCKS) else "5m"
        t0 = time.time()
        print(f"Gerando Bloco {i}/{len(TOPICS_BLOCKS)} da Seção 3.5...", flush=True)
        txt = call_luiz_v5(top, keep_alive=ka, is_third_person=True)
        t_clean = re.sub(r"(?m)^-\s*", "", top).replace("\n", " ")
        t_sim = difflib.SequenceMatcher(None, t_clean, txt).ratio()
        print(f"-> Bloco {i} ({time.time()-t0:.1f}s | topic={len(t_clean.split())}w -> out={len(txt.split())}w | topic->out sim={t_sim:.2f}):\n{txt}\n", flush=True)
        paras.append(txt)

    full_text = "\n\n".join(paras)
    OUT_FILE.write_text(full_text + "\n", encoding="utf-8")

    # Auditoria frase a frase contra ORIG_TEXT
    orig_paras = ORIG_TEXT.strip().split("\n\n")
    total_s, high_s = 0, 0
    for idx, (o, g) in enumerate(zip(orig_paras, paras), 1):
        os_list = [s for s in re.split(r"(?<=[.!?])\s+", o) if len(s.split()) > 4]
        gs_list = [s for s in re.split(r"(?<=[.!?])\s+", g) if len(s.split()) > 4]
        copied = sum(
            1 for gs in gs_list if max(difflib.SequenceMatcher(None, gs, os).ratio() for os in os_list) > 0.65
        )
        total_s += len(gs_list)
        high_s += copied
        print(f"Auditoria Bloco {idx}: {copied}/{len(gs_list)} frases >65% similares ao original")
    print(f"\n=== AUDITORIA FINAL SEÇÃO 3.5: {high_s}/{total_s} frases >65% similares | Total: {len(full_text.split())}w ===", flush=True)


if __name__ == "__main__":
    main()
