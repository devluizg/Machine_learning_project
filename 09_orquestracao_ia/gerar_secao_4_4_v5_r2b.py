#!/usr/bin/env python3
"""Rodada 2 para os Blocos 7 a 12 da Seção 4.4 corrigindo inversões causais, omissões,
alucinações ('teste piloto'/'prova') e 1ª pessoa plural de p2."""
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
from gerar_secao_4_4_v5_p2 import ORIG_BLOCKS_4_4_P2

TOPICS_4_4_R2B = [
    (
        "B7_r2",
        "B7",
        """- Ao introduzir o k-means, ocorre uma mudança na dinâmica da aula porque, diferentemente dos modelos anteriores, os pontos na tela vêm sem categorias prévias; a atividade retorna à pergunta sobre o que se deseja produzir com os dados e esclarece que agrupar por proximidade não equivale a escolher uma classe conhecida.
- Observar a atualização dos centroides e os pontos se reorganizando poderá exigir tempo maior de aula, pois o professor poderá precisar retomar termos dos encontros anteriores para esclarecer agrupamento diante de classificação.
- Fechando essa etapa dos módulos, uma síntese breve documentará como os cinco modelos combinam dados e regras para gerar uma saída conforme a finalidade de cada tarefa.""",
    ),
    (
        "B8_r2",
        "B8",
        """- No 7º encontro a turma compara os cinco modelos já trabalhados, analisando novas situações-problema para justificar a partir dos dados disponíveis se o caso demanda previsão numérica, escolha de categoria ou formação de grupos.
- Já no 8º encontro cada aluno responde inicialmente ao bloco de questões equivalentes ao diagnóstico e resolve em seguida um desafio inédito de transferência, devendo apontar que dados ligam o problema a um modelo compatível e explicar qual efeito se espera quando um dado ou parâmetro muda na regra.""",
    ),
    (
        "B9_r2",
        "B9",
        """- Do ponto de vista pedagógico, a aula comparativa resgata diferenças que tenham ficado dispersas entre os encontros e prepara os alunos para o desafio final, habituando o estudante a examinar primeiro a finalidade da tarefa diante dos dados antes de escolher qualquer modelo.
- No último encontro, o bloco comparável servirá para observar mudanças em relação ao diagnóstico inicial, ao passo que o desafio inédito funciona como evidência adicional sobre o uso dos conceitos em novo contexto, sem equiparação direta com itens mais simples.""",
    ),
    (
        "B10_r2",
        "B10",
        """- Na prática de aula, cada estudante acessará a plataforma individualmente pelos computadores do laboratório e com auxílio de Chromebooks conforme disponibilidade confirmada na escola.
- Nos encontros 2, 4 e 6, cada aluno preencherá também um registro curto antes e após manipular o site, contemplando assim um exemplo de regressão, um de classificação e um de agrupamento.
- O instrumento avaliativo final ocorrerá inteiramente de forma individual; se em algum dia o laboratório estiver indisponível, o docente projetará os experimentos à turma mantendo pausas individuais para previsão e explicação.""",
    ),
    (
        "B11_r2",
        "B11",
        """- O roteiro provisório previsto para as oito aulas articula objetivos de aprendizagem e tempo estimado às ações de mediação docente com perguntas formativas, prevendo ainda adaptações de infraestrutura escolar e limites didáticos de cada módulo.
- Dado que o site não guarda nenhuma resposta digitada pelos estudantes, o corpus documental desta pesquisa reunirá o diagnóstico inicial, o instrumento final completo aplicado no encerramento, os três registros intermediários individuais de aula e as anotações do professor.""",
    ),
    (
        "B12_r2",
        "B12",
        """- Antes de iniciar a intervenção na turma, o pesquisador conferirá a versão efetiva do site que irá a campo frente aos recursos descritos na sequência didática.
- Se algum cenário do ambiente digital exibir conjuntos de dados, textos de apoio ou representações matemáticas divergentes do roteiro previsto em aula, a diferença será corrigida na plataforma ou explicada aos estudantes.
- Essa verificação prévia assegura que a pesquisa não avalie alunos como se tivessem vivenciado outra sequência, garantindo sintonia exata entre o recurso usado nas aulas e os instrumentos avaliativos.""",
    ),
]


def main() -> None:
    out_path = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/candidatos_4_4_v5_r2b.txt")
    results = []
    for i, (name, orig_key, top) in enumerate(TOPICS_4_4_R2B, 1):
        orig_txt = ORIG_BLOCKS_4_4_P2[orig_key]
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
