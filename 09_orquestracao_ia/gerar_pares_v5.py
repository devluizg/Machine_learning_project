#!/usr/bin/env python3
"""Gera dois tipos de entrada (IA engessada/nominalizada + Tópicos secos) via DeepSeek
para cada bloco 100% puro de autor_ufpa2020_ouro.jsonl e monta dataset_treino_v5_0.jsonl."""
import difflib
import json
import os
import random
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE_DIR = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia")
IN_FILE = BASE_DIR / "autor_ufpa2020_ouro.jsonl"
CACHE_FILE = BASE_DIR / "autor_ufpa2020_v51_cache.jsonl"
OUT_DATASET = BASE_DIR / "dataset_treino_v5_0.jsonl"

INST_REWRITE = (
    "Reescreva o texto acadêmico abaixo adotando integralmente o estilo, o vocabulário "
    "e a construção de frases do autor de referência, mantendo todos os fatos, siglas e números."
)
INST_TOPICS = (
    "Escreva um texto acadêmico contínuo em português brasileiro desenvolvendo exatamente os "
    "pontos abaixo no estilo, vocabulário e construção de frases do autor de referência."
)

PROMPT_AI = """Reescreva completamente o trecho acadêmico abaixo no estilo típico e engessado de uma IA (como ChatGPT padrão):
1. Mude totalmente a estrutura das frases e a ordem das orações (NÃO copie frases nem trechos literais do original).
2. Substitua verbos em 1ª pessoa e construções diretas por voz passiva impessoal, nominalizações pesadas e jargões típicos de IA (ex.: "Observa-se que", "No âmbito de", "Cabe ressaltar que", "Evidencia-se a necessidade de", "Ademais", "Nesse contexto", "proporcionando", "configura-se como um fator preponderante", "torna-se imprescindível").
3. Mantenha 100% dos fatos, ideias, siglas, números e citações (Autor, Ano) do texto original, e mantenha a mesma quantidade de parágrafos.
4. Retorne APENAS o texto reescrito em parágrafo(s), sem títulos nem comentários.

Texto original:
{TEXT}"""

PROMPT_TOPICS = """Extraia de 3 a 5 tópicos curtos e objetivos (apenas fatos, conceitos, autores e números essenciais, em formato de lista com "-") que resumam fielmente todo o conteúdo do texto abaixo. Não escreva parágrafos corridos, apenas os tópicos diretos.

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


def call_deepseek(prompt: str, api_key: str, temp: float = 0.7) -> str:
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temp,
    }
    req = urllib.request.Request(
        "https://api.deepseek.com/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "luiz-v5-builder/1.1",
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


def process_one(idx: int, text: str, api_key: str) -> dict:
    ai_ver = call_deepseek(PROMPT_AI.format(TEXT=text), api_key, temp=0.75)
    sim = difflib.SequenceMatcher(None, ai_ver, text).ratio()
    if sim > 0.55:
        ai_ver = call_deepseek(PROMPT_AI.format(TEXT=text), api_key, temp=0.85)
    topics_ver = call_deepseek(PROMPT_TOPICS.format(TEXT=text), api_key, temp=0.5)
    return {"idx": idx, "ai": ai_ver, "topics": topics_ver, "output": text}


def main() -> None:
    api_key = get_api_key()
    rows = [json.loads(l) for l in IN_FILE.read_text(encoding="utf-8").splitlines() if l.strip()]

    cached = {}
    if CACHE_FILE.exists():
        for l in CACHE_FILE.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l)
                cached[r["idx"]] = r

    todo = [(r["idx"], r["text"]) for r in rows if r["idx"] not in cached]
    print(f"Blocos Autor 1 (layout limpo): {len(rows)} | Cache: {len(cached)} | A gerar: {len(todo)}", flush=True)

    t0 = time.time()
    done = 0
    if todo:
        with ThreadPoolExecutor(max_workers=12) as pool:
            futs = {pool.submit(process_one, idx, txt, api_key): idx for idx, txt in todo}
            with open(CACHE_FILE, "a", encoding="utf-8") as fout:
                for fut in as_completed(futs):
                    res = fut.result()
                    cached[res["idx"]] = res
                    fout.write(json.dumps(res, ensure_ascii=False) + "\n")
                    fout.flush()
                    done += 1
                    if done % 20 == 0 or done == len(todo):
                        print(f"Progresso: {done}/{len(todo)} ({time.time() - t0:.1f}s)", flush=True)

    dataset = []
    sims = []
    for r in rows:
        item = cached[r["idx"]]
        sims.append(difflib.SequenceMatcher(None, item["ai"], item["output"]).ratio())
        dataset.append(
            {
                "source": "ufpa2020_ai_to_author",
                "instruction": INST_REWRITE,
                "input": item["ai"],
                "output": item["output"],
            }
        )
        dataset.append(
            {
                "source": "ufpa2020_topics_to_author",
                "instruction": INST_TOPICS,
                "input": item["topics"],
                "output": item["output"],
            }
        )

    random.seed(42)
    random.shuffle(dataset)

    with open(OUT_DATASET, "w", encoding="utf-8") as f:
        for d in dataset:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")

    avg_sim = sum(sims) / max(len(sims), 1)
    high_sim = sum(1 for s in sims if s > 0.70)
    print(
        f"DONE! {OUT_DATASET.name} gerado com {len(dataset)} pares | "
        f"Similaridade media IA->Autor: {avg_sim:.2f} (pares >70% iguais: {high_sim}/{len(sims)})",
        flush=True,
    )


if __name__ == "__main__":
    main()
