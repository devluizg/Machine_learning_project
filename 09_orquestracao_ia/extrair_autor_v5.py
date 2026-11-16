#!/usr/bin/env python3
"""Extrai prosa autoral 100% limpa de Dissertacao_Metodologia7Cs.pdf (UFPA, 2020)
usando pdftotext -layout para separar recuo de parágrafo (5..9 espaços),
continuação de linha (0 espaços, inclusive em quebras de página) e excluir
100% das citações diretas longas ABNT (>=10 espaços), tabelas e referências visuais."""
import json
import re
import subprocess
from pathlib import Path

PDF_PATH = Path("/home/luiz/Downloads/Dissertacao_Metodologia7Cs.pdf")
OUT_PATH = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia/autor_ufpa2020_ouro.jsonl")


def clean_paragraph(p: str) -> str:
    p = re.sub(r"\s+", " ", p).strip()
    # Se termina com chamada de citação ("Segundo Fulano (2007, p. 12):"), remove apenas essa última frase
    if p.endswith(":"):
        p = re.sub(r"(?:^|(?<=[.!?])\s+)[^.!?]+:\s*$", "", p).strip()
    # Remove parênteses de referência visual: (Quadro 4), (Figura 12), (Apêndice IV), etc.
    p = re.sub(
        r"\s*\((?:ver\s+|conforme\s+|vide\s+)?(?:Quadro|Figura|Tabela|Apêndice|Anexo|Gráfico|Seção)s?\s+[IVXLCDM\d]+[^)]*\)",
        "",
        p,
        flags=re.I,
    )
    # Divide em frases e remove frases que mencionam diretamente Quadro X, Figura Y, Capítulo Z, etc.
    sents = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ\"“(])", p)
    kept_sents = []
    for s in sents:
        if re.search(
            r"\b(Quadro|Figura|Tabela|Apêndice|Anexo|Gráfico|Cap[ií]tulo|Seção)\s+[IVXLCDM\d]",
            s,
            re.I,
        ):
            continue
        if re.match(r"^(Neste\s+cap[ií]tulo|O\s+presente\s+cap[ií]tulo|Na\s+próxima\s+seção)", s, re.I):
            continue
        if "[...]" in s or "http://" in s or "https://" in s:
            continue
        kept_sents.append(s.strip())
    return " ".join(kept_sents).strip()


def extract_clean_blocks() -> list[str]:
    raw = subprocess.check_output(
        ["pdftotext", "-layout", str(PDF_PATH), "-"], stderr=subprocess.DEVNULL
    ).decode("utf-8", "ignore")
    lines = raw.splitlines()

    start_idx = 365
    for i, ln in enumerate(lines):
        if i > 300 and ln.strip() == "INTRODUÇÃO":
            start_idx = i + 1
            break

    end_idx = len(lines)
    for i in range(len(lines) - 1, start_idx, -1):
        if re.match(r"^\s*REFERÊNCIAS(\s+BIBLIOGRÁFICAS)?\s*$", lines[i].strip(), re.I):
            end_idx = i
            break

    paras: list[str] = []
    cur: list[str] = []
    for ln in lines[start_idx:end_idx]:
        s = ln.strip()
        if not s or re.match(r"^\d{1,3}$", s):
            continue
        ind = len(ln) - len(ln.lstrip(" "))
        # Ignora linhas de tabela (múltiplas colunas separadas por 3+ espaços), bullets e títulos/legendas
        if (
            re.search(r"\S\s{3,}\S", s)
            or "\uf0b7" in s
            or "\uf0a7" in s
            or "•" in s
            or re.match(
                r"^(\d+(\.\d+)*\s+|CAPÍTULO|INTRODUÇÃO|CONSIDERAÇÕES|REFERÊNCIAS|Quadro\s+\d|Figura\s+\d|Tabela\s+\d|Fonte:)",
                s,
                re.I,
            )
        ):
            if cur:
                paras.append(" ".join(cur))
                cur = []
            continue

        if 5 <= ind <= 9:
            if cur:
                paras.append(" ".join(cur))
            cur = [s]
        elif ind == 0 and cur:
            if cur[-1].endswith("-") and s[0].islower():
                cur[-1] = cur[-1][:-1] + s
            else:
                cur.append(s)
        else:
            # Recuo >= 10 (citação direta longa ABNT de outros autores) ou 1..4 (tabelas/legendas)
            if cur:
                paras.append(" ".join(cur))
                cur = []
    if cur:
        paras.append(" ".join(cur))

    cleaned_paras: list[str] = []
    for p in paras:
        cp = clean_paragraph(p)
        words = cp.split()
        if len(words) < 22:
            continue
        if not cp.endswith((".", "!", "?")):
            continue
        if cp.startswith(("“", '"')) and cp.endswith(("”", '"')):
            continue
        digits = sum(c.isdigit() for c in cp)
        if digits / max(len(cp), 1) > 0.06:
            continue
        cleaned_paras.append(cp)

    # Agrupa em blocos naturais de 65 a 185 palavras (1 a 2 parágrafos)
    blocks: list[str] = []
    buf: list[str] = []
    bw = 0
    for p in cleaned_paras:
        pw = len(p.split())
        if pw > 200:
            # Se um único parágrafo for muito longo, divide em 2 na metade das frases
            sents = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ])", p)
            mid = max(1, len(sents) // 2)
            sub_paras = [" ".join(sents[:mid]), " ".join(sents[mid:])]
        else:
            sub_paras = [p]

        for sp in sub_paras:
            spw = len(sp.split())
            if spw < 20:
                continue
            if buf and bw + spw > 180:
                if bw >= 55:
                    blocks.append("\n\n".join(buf))
                    buf, bw = [sp], spw
                else:
                    buf.append(sp)
                    blocks.append("\n\n".join(buf))
                    buf, bw = [], 0
            else:
                buf.append(sp)
                bw += spw
                if bw >= 90:
                    blocks.append("\n\n".join(buf))
                    buf, bw = [], 0
    if buf and bw >= 50:
        blocks.append("\n\n".join(buf))

    return blocks


def main() -> None:
    blocks = extract_clean_blocks()
    total_w = sum(len(b.split()) for b in blocks)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        for i, b in enumerate(blocks):
            row = {"idx": i, "text": b, "words": len(b.split())}
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"Extraídos {len(blocks)} blocos 100% puros ({total_w} palavras) em {OUT_PATH.name}")
    for sample_idx in [0, len(blocks) // 3, (2 * len(blocks)) // 3, len(blocks) - 1]:
        b = blocks[sample_idx]
        print(f"\n[Amostra {sample_idx} | {len(b.split())}w]: {b[:240]}...")


if __name__ == "__main__":
    main()
