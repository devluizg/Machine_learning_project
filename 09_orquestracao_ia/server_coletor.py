#!/usr/bin/env python3
import json
import random
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

BASE_DIR = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia")
PAIRED_FILE = BASE_DIR / "marcusbraga_pareado_v3_2.jsonl"
GOLD_FILE = BASE_DIR / "luiz_frases_gold.jsonl"
HTML_FILE = BASE_DIR / "coletor_frases.html"


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ])", text.strip())
    return [p.strip() for p in parts if 14 <= len(p.split()) <= 50]


def token_set(s: str) -> set[str]:
    return set(re.findall(r"[a-záéíóúâêôãõç0-9]+", s.lower()))


def is_similar(toks: set[str], pool: list[set[str]], thresh: float = 0.50) -> bool:
    for p in pool:
        union = len(toks | p)
        if union and (len(toks & p) / union) >= thresh:
            return True
    return False


def load_queue() -> tuple[list[str], int]:
    done_sets: list[set[str]] = []
    saved_count = 0
    if GOLD_FILE.exists():
        for line in GOLD_FILE.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                done_sets.append(token_set(r.get("input", "")))
                saved_count += 1

    queue: list[str] = []
    seen_sets: list[set[str]] = list(done_sets)
    if PAIRED_FILE.exists():
        for line in PAIRED_FILE.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            for s in split_sentences(r.get("input", "")):
                if re.match(r"^O Cap[íi]tulo \d+", s):
                    continue
                toks = token_set(s)
                if not is_similar(toks, seen_sets):
                    seen_sets.append(toks)
                    queue.append(s)
    random.Random(42).shuffle(queue)
    return queue[:200], saved_count


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def _send_json(self, code: int, data: dict):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            html = HTML_FILE.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html)))
            self.end_headers()
            self.wfile.write(html)
        elif self.path == "/api/queue":
            queue, saved_count = load_queue()
            self._send_json(200, {"queue": queue, "saved_count": saved_count})
        elif self.path == "/api/export":
            content = GOLD_FILE.read_bytes() if GOLD_FILE.exists() else b""
            self.send_response(200)
            self.send_header("Content-Type", "application/jsonl; charset=utf-8")
            self.send_header("Content-Disposition", 'attachment; filename="luiz_frases_gold.jsonl"')
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == "/api/save":
            length = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            inp = payload.get("input", "").strip()
            out = payload.get("output", "").strip()
            if not inp or not out:
                self._send_json(400, {"error": "input and output required"})
                return
            rec = {
                "source": "luiz_frase_manual",
                "instruction": "Reescreva a frase acadêmica abaixo com a voz autoral de Luiz Gabriel, mantendo os fatos e números.",
                "input": inp,
                "output": out,
            }
            with open(GOLD_FILE, "a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            _, saved_count = load_queue()
            self._send_json(200, {"ok": True, "saved_count": saved_count})
        else:
            self.send_error(404)


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8787), Handler)
    print("Coletor rodando em http://127.0.0.1:8787", flush=True)
    server.serve_forever()
