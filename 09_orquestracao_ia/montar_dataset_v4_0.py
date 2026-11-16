#!/usr/bin/env python3
"""Monta dataset_treino_v4_0.jsonl com foco principal nos 3 textos 95-100% humanos do Luiz,
seus pares por parágrafo alinhado, suas 40 frases reais e os 273 blocos pareados do Marcus Braga."""
import json
import random
from pathlib import Path

BASE = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia")


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def align_paragraphs(inp: str, out: str) -> list[tuple[str, str]]:
    in_p = [p.strip() for p in inp.split("\n\n") if p.strip()]
    out_p = [p.strip() for p in out.split("\n\n") if p.strip()]
    if len(in_p) == len(out_p) and len(in_p) > 1:
        return list(zip(in_p, out_p))
    # Se o número de parágrafos diferir (ex.: 6 vs 7 no texto 1), agrupa em janelas proporcionais
    pairs = []
    if len(in_p) >= 2 and len(out_p) >= 2:
        mid_in = len(in_p) // 2
        mid_out = len(out_p) // 2
        pairs.append(("\n\n".join(in_p[:mid_in]), "\n\n".join(out_p[:mid_out])))
        pairs.append(("\n\n".join(in_p[mid_in:]), "\n\n".join(out_p[mid_out:])))
    return pairs


def main() -> None:
    luiz_texts = load_jsonl(BASE / "luiz_real_v4_gold.jsonl")
    luiz_frases = load_jsonl(BASE / "luiz_frases_gold.jsonl")
    luiz_tokens = load_jsonl(BASE / "luiz_escolhas_tokens.jsonl")
    marcus = load_jsonl(BASE / "marcusbraga_pareado_v3_2.jsonl")

    dataset: list[dict] = []

    # 1. Foco principal: os 3 textos completos (4x) + suas metades/parágrafos alinhados (4x)
    para_pairs_count = 0
    for r in luiz_texts:
        item = {
            "source": r["source"],
            "instruction": r["instruction"],
            "input": r["input"],
            "output": r["output"],
        }
        for _ in range(4):
            dataset.append(item)

        for pin, pout in align_paragraphs(r["input"], r["output"]):
            para_pairs_count += 1
            pitem = {
                "source": r["source"] + "_bloco",
                "instruction": r["instruction"],
                "input": pin,
                "output": pout,
            }
            for _ in range(4):
                dataset.append(pitem)

    # 2. As 20 frases reestruturadas à mão (2x)
    for r in luiz_frases:
        item = {
            "source": r["source"],
            "instruction": r["instruction"],
            "input": r["input"],
            "output": r["output"],
        }
        for _ in range(2):
            dataset.append(item)

    # 3. As 20 frases do construtor de próximo token (2x)
    for r in luiz_tokens:
        item = {
            "source": r["source"],
            "instruction": r["instruction"],
            "input": r["input"],
            "output": r["output"],
        }
        for _ in range(2):
            dataset.append(item)

    # 4. Alicerce 100% humano pré-LLM: 273 blocos pareados do Marcus Braga (1x)
    for r in marcus:
        dataset.append({
            "source": r["source"],
            "instruction": r["instruction"],
            "input": r["input"],
            "output": r["output"],
        })

    random.Random(42).shuffle(dataset)
    out_path = BASE / "dataset_treino_v4_0.jsonl"
    with open(out_path, "w", encoding="utf-8") as f:
        for row in dataset:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    luiz_total = (len(luiz_texts) * 4) + (para_pairs_count * 4) + (len(luiz_frases) * 2) + (len(luiz_tokens) * 2)
    print(
        f"dataset_treino_v4_0.jsonl gerado: {len(dataset)} linhas totais\n"
        f"  - Foco Luiz ({luiz_total} linhas = {luiz_total/len(dataset)*100:.1f}%): "
        f"{len(luiz_texts)} textos x4 + {para_pairs_count} blocos alinhados x4 + "
        f"{len(luiz_frases)} frases x2 + {len(luiz_tokens)} escolhas x2\n"
        f"  - Alicerce Marcus Braga ({len(marcus)} linhas = {len(marcus)/len(dataset)*100:.1f}%)"
    )


if __name__ == "__main__":
    main()
