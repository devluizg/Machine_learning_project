#!/usr/bin/env python3
"""Pipeline Padronizado v5.0 (100% Fidelidade de Ideias + 100% Tokens Puros do luiz-academico).

Implementa as 4 travas definitivas sem contaminar o texto final com tokens de LLMs comerciais:
1. Fatiamento inteligente (parágrafos >175 palavras são divididos ao meio em 2 janelas de ~90-100 palavras, impedindo que o modelo corte o final do parágrafo).
2. Extração de Tópicos 1:1 via DeepSeek (4 tópicos densos e telegráficos por janela, cobrindo 100% das frases, ideias secundárias, justificativas e conclusões, sempre com sujeito em 3ª pessoa explícito).
3. Geração 100% via luiz-academico:latest (v5.0, temperature=0.48), unificando cada parágrafo em bloco contínuo.
4. Filtro determinístico pós-geração (clean_author1_quirks): corrige vazamentos de 1ª pessoa da dissertação da UFPA ("contamos com a parceria de", "baseamo-nos", "elaboramos", "realizamos") e deslizes morfológicos conhecidos sem injetar tokens de IA comercial.
"""
import argparse
import json
import os
import re
import time
import urllib.request
from pathlib import Path

INST_TOPICS = (
    "Escreva um texto acadêmico contínuo em português brasileiro desenvolvendo exatamente os "
    "pontos abaixo no estilo, vocabulário e construção de frases do autor de referência."
)

PROMPT_EXTRACT_1TO1 = """Converta o trecho acadêmico abaixo em EXATAMENTE 3 tópicos claros e objetivos (formato de lista com "-"), seguindo RIGOROSAMENTE estas regras:
1. Cubra 100% das ideias, exemplos técnicos, justificativas pedagógicas, limitações e conclusões do trecho na exata ordem em que aparecem (NÃO omita nenhuma informação nem referências a seções).
2. Preserve 100% dos nomes de autores e anos exatos, números e nomes dos algoritmos (regressão linear, SVM, k-NN, árvore de decisão, k-means, aprendizagem supervisionada e não supervisionada).
3. PRESERVE O TEMPO VERBAL E O SUJEITO REAIS DO TRECHO: Se o trecho descreve uma proposta ou projeto no presente/futuro, mantenha os verbos no PRESENTE/FUTURO.
4. PROIBIDO REPETIR O VOCABULÁRIO ESTILÍSTICO DA FRASE ORIGINAL: Substitua todas as expressões prontas, verbos rebuscados e metáforas da frase original por palavras simples e cotidianas (ex.: troque "porta de entrada compatível" por "início adequado para os alunos"; troque "pelo confronto com vizinhos semelhantes" por "olhando os exemplos mais parecidos ao redor"; troque "explicita condições sucessivas" por "segue passos de decisão em sequência"; troque "debate moralizante e abstrato" por "discussão distante da prática"). Nenhuma frase do tópico pode ter mais de 4 palavras seguidas iguais ao trecho original!

Trecho original:
{CHUNK}"""


def get_api_key() -> str:
    for env_path in ["/home/luiz/simuladoapp_v2/.env", os.path.expanduser("~/.env")]:
        if os.path.exists(env_path):
            with open(env_path, encoding="utf-8") as f:
                for line in f:
                    if line.startswith("DEEPSEEK_API_KEY="):
                        return line.split("=", 1)[1].strip().strip("\"'")
    raise RuntimeError("DEEPSEEK_API_KEY not found")


def call_deepseek(prompt: str, api_key: str, temp: float = 0.3) -> str:
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
            "User-Agent": "luiz-v5-fiel/1.3",
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


def clean_author1_quirks(text: str, is_third_person: bool = True) -> str:
    """Corrige vazamentos determinísticos da dissertação do Autor 1 e gatilhos amarelos do GPTZero."""
    # Une quebras internas em parágrafo contínuo
    t = re.sub(r"\s*\n+\s*", " ", text).strip()
    # Remove citações de página truncadas no final tipo (DE BONO, 2005, p.
    t = re.sub(r'\s*\([A-ZÁÉÍÓÚÂÊÔÃÕÇ\s,;]+\d{4},\s*p\.\s*\d*\)?\.?\s*$', '.', t)
    t = re.sub(r'[“"]([^”"]+)[”"]\s*\.\s*$', r'\1.', t)
    # Remove aspas falsas em torno de objetivos parafraseados ("desenvolver e avaliar...")
    t = re.sub(r':\s*[“"](desenvolver|investigar|analisar|avaliar|propor|criar)\b([^”"]+)[”"]\.', r" \1\2.", t, flags=re.I)
    # Corrige typos/deslizes conhecidos do Autor 1 / Llama 8B Q4
    t = re.sub(r"\bacredita-os ser\b", "acreditam ser", t, flags=re.I)
    t = re.sub(r"\bfoi divida\b", "foi dividida", t, flags=re.I)
    t = re.sub(r"\buma estudo\b", "um estudo", t, flags=re.I)
    t = re.sub(r"\bPara pensar computacional\b", "Quanto ao pensamento computacional", t, flags=re.I)
    t = re.sub(r"\bmais participantes\b", "mais participativas", t, flags=re.I)
    t = re.sub(r"\bcom não fosse\b", "com que não fosse", t, flags=re.I)
    t = re.sub(r"\bnão mediou\b", "não permitiu comparar", t, flags=re.I)
    t = re.sub(r"\bmediou o andamento\b", "comparou a evolução", t, flags=re.I)
    # Remove gatilhos específicos que o GPTZero 4.1m marca em amarelo
    t = re.sub(r"\bAlguns elementos incluem:\s*", "Entre esses elementos estão ", t)
    t = re.sub(r"\bAlém disso,\s+", "Outro ponto observado é que ", t)
    t = re.sub(r",\s*portanto,\s*", ", dessa maneira, ", t)

    if is_third_person:
        replacements = [
            (r"\bcontamos com a parceria de\b", "os autores apoiaram-se nas contribuições de"),
            (r"\bcontou com a parceria de\b", "apoiou-se nas contribuições de"),
            (r"\bparceria de grandes nomes\b", "contribuição de importantes autores"),
            (r"\bparceria de\b", "contribuição teórica de"),
            (r"\bbaseamo-nos em\b", "os autores basearam-se em"),
            (r"\bapoiamo-nos em\b", "os autores apoiaram-se em"),
            (r"\butilizamos\b", "utilizaram"),
            (r"\belaboramos uma rubrica\b", "foi aplicada uma rubrica"),
            (r"\belaboramos\b", "os autores elaboraram"),
            (r"\bdisponibilizamos\b", "disponibilizada"),
            (r"\blevantamos alguns pontos\b", "foram avaliados pontos"),
            (r"\blevantamos\b", "avaliaram"),
            (r"\bnão identificamos\b", "não foi identificada"),
            (r"\bidentificamos\b", "identificaram"),
            (r"\bpara chegarmos\b", "para se chegar"),
            (r"\bacreditamos que\b", "observa-se que"),
            (r"\brealizamos a análise\b", "foi realizada a análise"),
            (r"\brealizamos\b", "os autores realizaram"),
            (r"\bverificamos\b", "verificou-se"),
            (r"\bobtidemos\b", "obtiveram"),
            (r"\bobservamos\b", "observou-se"),
            (r"\bapresentamos\b", "são apresentados"),
            (r"\bdescrevemos\b", "são descritos"),
            (r"\bbuscamos\b", "os autores buscaram"),
            (r"\bpropomos\b", "os autores propõem"),
        ]
        for pat, rep in replacements:
            t = re.sub(pat, rep, t, flags=re.I)

    # Garante letra maiúscula após ponto final se alguma substituição ocorreu no início de frase
    t = re.sub(r"(^|[.!?]\s+)([a-záéíóúâêôãõç])", lambda m: m.group(1) + m.group(2).upper(), t)
    return t


def call_luiz_v5(topics: str, keep_alive: str = "5m", is_third_person: bool = True) -> str:
    payload = {
        "model": "luiz-academico:latest",
        "messages": [{"role": "user", "content": f"{INST_TOPICS}\n\n{topics}"}],
        "stream": False,
        "keep_alive": keep_alive,
        "options": {
            "num_ctx": 1024,
            "temperature": 0.65,
            "top_p": 0.92,
            "min_p": 0.04,
            "repeat_penalty": 1.05,
        },
    }
    req = urllib.request.Request(
        "http://localhost:11434/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=600) as r:
        data = json.loads(r.read().decode("utf-8"))
    raw = data["message"]["content"].strip()
    return clean_author1_quirks(raw, is_third_person=is_third_person)


def split_paragraph_smart(paragraph: str, max_words: int = 155) -> list[str]:
    """Mantém parágrafos de até 175 palavras inteiros; divide parágrafos maiores (>175w)
    em 2 metades equilibradas por frase para nunca cortar o final."""
    words = paragraph.strip().split()
    if len(words) <= max_words:
        return [paragraph.strip()]

    sents = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ\"“(])", paragraph.strip())
    if len(sents) <= 2:
        return [paragraph.strip()]

    # Divide próximo à metade das palavras
    half_w = len(words) / 2
    w1, cur_w = [], 0
    split_idx = 1
    for i, s in enumerate(sents):
        cur_w += len(s.split())
        if cur_w >= half_w or i == len(sents) - 2:
            split_idx = i + 1
            break
    part1 = " ".join(sents[:split_idx]).strip()
    part2 = " ".join(sents[split_idx:]).strip()
    return [part1, part2]


def process_document(text: str) -> str:
    import difflib
    api_key = get_api_key()
    raw_blocks = [b.strip() for b in re.split(r"\n\s*\n", text.strip()) if b.strip()]

    header_blocks = []
    prose_paras = []
    for b in raw_blocks:
        if b.startswith("#") or (b.startswith("**") and len(b.split()) < 45):
            header_blocks.append(b)
        else:
            prose_paras.append(b)

    all_windows = [split_paragraph_smart(p, max_words=155) for p in prose_paras]
    total_wins = sum(len(w) for w in all_windows)
    win_counter = 0

    final_paragraphs = list(header_blocks)
    for p_idx, windows in enumerate(all_windows, 1):
        rebuilt_windows = []
        for w_idx, win_text in enumerate(windows, 1):
            win_counter += 1
            ka = "0s" if win_counter == total_wins else "5m"
            t0 = time.time()
            topics = call_deepseek(PROMPT_EXTRACT_1TO1.format(CHUNK=win_text), api_key, temp=0.35)
            # Se o tópico copiou frases demais do original (>0.48), regenera com temp=0.6
            if difflib.SequenceMatcher(None, topics, win_text).ratio() > 0.48:
                topics = call_deepseek(PROMPT_EXTRACT_1TO1.format(CHUNK=win_text), api_key, temp=0.6)
            print(f"\n--- [P{p_idx} Janela {w_idx}/{len(windows)}] Tópicos Extraídos ---\n{topics}", flush=True)
            gen_clean = call_luiz_v5(topics, keep_alive=ka, is_third_person=True)
            print(
                f"-> [P{p_idx} Janela {w_idx}/{len(windows)} concluída em {time.time()-t0:.1f}s | {len(gen_clean.split())}w]:\n{gen_clean}",
                flush=True,
            )
            rebuilt_windows.append(gen_clean)

        final_paragraphs.append(" ".join(rebuilt_windows))

    return "\n\n".join(final_paragraphs)


def main() -> None:
    parser = argparse.ArgumentParser(description="Pipeline v5.0 com 100% de fidelidade de ideias.")
    parser.add_argument("--input", "-i", type=str, required=True, help="Arquivo de entrada (.md ou .txt)")
    parser.add_argument("--output", "-o", type=str, required=True, help="Arquivo de saída (.md ou .txt)")
    args = parser.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)
    result = process_document(in_path.read_text(encoding="utf-8"))
    out_path.write_text(result + "\n", encoding="utf-8")
    print(f"\n=== CONCLUÍDO! Salvo em: {out_path} ({len(result.split())} palavras) ===", flush=True)


if __name__ == "__main__":
    main()
