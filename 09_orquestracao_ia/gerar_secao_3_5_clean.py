#!/usr/bin/env python3
"""Gera a Seção 3.5 no luiz-academico v5.0 (temperature=0.65)
com notas de ~60-80 palavras no presente/futuro para manter sim < 0.45 e zero alucinações."""
import difflib
import re
import time
from pathlib import Path
from pipeline_v5_fiel import call_luiz_v5

OUT_FILE = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/secao_3_5_v5_fiel.md")

ORIG_TEXT = """A literatura e os documentos curriculares definem o posicionamento da proposta. Nela, o machine learning entra como conteúdo introdutório de Computação, superando o simples treinamento no uso de aplicativos. A sequência recorta ideias fundamentais e limites observáveis nas tarefas, sem antecipar uma formação universitária em algoritmos. Tanto os dados da própria turma quanto os cenários sintéticos visam mostrar a origem dos números e o efeito de alterar parâmetros. Dessa forma, a visualização sustenta comparações nas quais o estudante parte de uma hipótese para observar o gráfico e explicar como a regra do modelo transforma os dados em resultado.

A análise buscará evidências em produções individuais contextualizadas, indo além da contagem de acertos sem prometer efeitos causais generalizáveis.

Embora a literatura já reúna ferramentas e experiências no ensino de IA e machine learning na Educação Básica, os estudos cobram maior clareza sobre conteúdos e estratégias nos contextos de aplicação, ao lado de avaliações mais rigorosas (Martins e Gresse von Wangenheim, 2023; Rauber e Gresse von Wangenheim, 2023; Sanusi et al., 2023). Assim, este projeto contribui ao analisar, em uma turma de Ensino Médio do próprio pesquisador, uma sequência didática que articula a visualização de cinco modelos a instrumentos com critérios explícitos.

A qualidade da pesquisa dependerá do alinhamento metodológico entre o referencial e o produto desenvolvido. Para isso, os recursos do site refletirão objetivos de aprendizagem presentes nas atividades e nos instrumentos de coleta, garantindo que as conclusões respeitem estritamente o alcance das evidências produzidas."""

TOPICS_BLOCKS = [
    # Bloco 1 (~74w)
    """- Os documentos do currículo e os estudos de Computação mostram que ensinar machine learning no Ensino Médio significa trabalhar princípios da própria área, e não só treinar a turma para operar programas prontos.
- O plano de aula foca em noções iniciais e limites observáveis nas tarefas, sem adiantar conteúdos avançados da faculdade.
- Para mostrar de onde vêm os números e como alterações mudam o resultado na tela, a plataforma junta tabelas coletadas pela própria turma com cenários sintéticos controlados.""",

    # Bloco 2 (~72w)
    """- Nos encontros previstos, os gráficos servem para o estudante levantar uma hipótese antes de mexer no controle, observar a tela e explicar com suas palavras qual regra gerou o resultado.
- Na hora de analisar o aprendizado da turma, a pesquisa busca evidências no que cada estudante produz nas tarefas dentro do contexto da aula.
- Esse acompanhamento vai além de simplesmente contar acertos e erros em testes, sem pretender provar efeitos causais válidos para qualquer outra realidade.""",

    # Bloco 3 (~80w)
    """- Ainda que já existam ferramentas e relatos sobre IA na Educação Básica, revisões recentes cobram mais clareza sobre conteúdos e estratégias nos locais de aplicação, além de avaliações com rigor maior (Martins e Gresse von Wangenheim, 2023; Rauber e Gresse von Wangenheim, 2023; Sanusi et al., 2023).
- Diante disso, este projeto contribui ao estudar uma sequência didática aplicada pelo próprio pesquisador em sua turma de Ensino Médio.
- A proposta junta a visualização de cinco modelos (regressão linear, SVM, k-NN, árvore de decisão e k-means) com instrumentos que trazem critérios definidos.""",

    # Bloco 4 (~57w)
    """- A validade metodológica deste projeto depende do alinhamento direto entre o referencial teórico e o produto educacional construído.
- Por esse motivo, as telas e os recursos do site serão estruturados para refletir os objetivos de aprendizagem presentes nas aulas e nos instrumentos de pesquisa.
- Dessa forma, espera-se garantir que a análise e as conclusões futuras respeitem exatamente o limite das evidências coletadas na turma.""",
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
        print(
            f"-> Bloco {i} ({time.time()-t0:.1f}s | topic={len(t_clean.split())}w -> out={len(txt.split())}w | topic->out sim={t_sim:.2f}):\n{txt}\n",
            flush=True,
        )
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
