#!/usr/bin/env python3
"""Gera pares (IA padrão -> 100% Humano) para os 273 blocos de marcusbraga_ouro.jsonl
e monta dataset_treino_v3_2.jsonl combinando com luiz_real_v4_gold.jsonl."""
import json
import os
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE_DIR = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia")
MARCUS_IN = BASE_DIR / "marcusbraga_ouro.jsonl"
LUIZ_GOLD = BASE_DIR / "luiz_real_v4_gold.jsonl"
PAIRED_OUT = BASE_DIR / "marcusbraga_pareado_v3_2.jsonl"
DATASET_OUT = BASE_DIR / "dataset_treino_v3_2.jsonl"

INSTRUCTION = (
    "Reescreva o texto acadêmico abaixo com a voz autoral de Luiz Gabriel, "
    "mantendo integralmente os fatos, citações e números."
)

PROMPT_TMPL = """Reescreva o trecho acadêmico abaixo no estilo formal padrão de um modelo de linguagem (linguagem acadêmica polida, conectivos formais como "nesse sentido", "além disso", "dessa forma", "portanto", orações bem encadeadas e vocabulário técnico formal), mantendo EXATAMENTE todos os fatos, números, siglas e citações do texto original, com extensão aproximada semelhante.
Retorne APENAS o texto reescrito em português, sem comentários, sem título e sem aspas.

Texto:
{TEXT}"""


def get_api_key() -> str:
    for env_path in ["/home/luiz/simuladoapp_v2/.env", os.path.expanduser("~/.env")]:
        if os.path.exists(env_path):
            with open(env_path, encoding="utf-8") as f:
                for line in f:
                    if line.startswith("DEEPSEEK_API_KEY="):
                        return line.split("=", 1)[1].strip().strip("\"'")
    raise RuntimeError("DEEPSEEK_API_KEY not found")


def call_deepseek(text: str, api_key: str) -> str:
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": PROMPT_TMPL.format(TEXT=text)}],
        "temperature": 0.7,
    }
    req = urllib.request.Request(
        "https://api.deepseek.com/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "luiz-v3_2-builder/1.0",
        },
        method="POST",
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"].strip()
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))
    raise RuntimeError("Unreachable")


def main() -> None:
    api_key = get_api_key()
    marcus_rows = [json.loads(line) for line in MARCUS_IN.read_text(encoding="utf-8").splitlines() if line.strip()]

    existing = {}
    if PAIRED_OUT.exists():
        for line in PAIRED_OUT.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                existing[r["idx"]] = r

    todo = [(i, r["text"]) for i, r in enumerate(marcus_rows) if i not in existing]
    print(f"Total Marcus blocks: {len(marcus_rows)} | Cached: {len(existing)} | To generate: {len(todo)}", flush=True)

    t0 = time.time()
    done = 0
    if todo:
        with ThreadPoolExecutor(max_workers=8) as pool:
            futs = {pool.submit(call_deepseek, txt, api_key): (i, txt) for i, txt in todo}
            with open(PAIRED_OUT, "a", encoding="utf-8") as fout:
                for fut in as_completed(futs):
                    i, orig_txt = futs[fut]
                    ai_txt = fut.result()
                    rec = {
                        "idx": i,
                        "source": "marcus_braga_paired_v3_2",
                        "instruction": INSTRUCTION,
                        "input": ai_txt,
                        "output": orig_txt,
                    }
                    fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    fout.flush()
                    existing[i] = rec
                    done += 1
                    if done % 25 == 0 or done == len(todo):
                        print(f"Progress: {done}/{len(todo)} ({time.time() - t0:.1f}s)", flush=True)

    paired_ordered = [existing[i] for i in sorted(existing.keys())]
    luiz_rows = [json.loads(line) for line in LUIZ_GOLD.read_text(encoding="utf-8").splitlines() if line.strip()]

    final_rows = []
    for r in paired_ordered:
        final_rows.append({
            "source": r["source"],
            "instruction": r["instruction"],
            "input": r["input"],
            "output": r["output"],
        })
    # Oversample Luiz's 100%-human real pairs 5x to anchor personal voice traits
    for _ in range(5):
        for r in luiz_rows:
            final_rows.append({
                "source": r["source"],
                "instruction": r["instruction"],
                "input": r["input"],
                "output": r["output"],
            })

    with open(DATASET_OUT, "w", encoding="utf-8") as fout:
        for r in final_rows:
            fout.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(
        f"DONE! Marcus paired: {len(paired_ordered)} | Luiz gold (x5): {len(luiz_rows) * 5} | "
        f"Total dataset_treino_v3_2.jsonl: {len(final_rows)} rows",
        flush=True,
    )


if __name__ == "__main__":
    main()
