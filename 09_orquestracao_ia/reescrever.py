#!/usr/bin/env python3
"""
Utilitário de reescrita acadêmica com o modelo local luiz-academico v2.0 (Ollama)
"""
import sys
import json
import urllib.request
import os
import subprocess

def reescrever(texto: str) -> str:
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "luiz-academico",
        "prompt": texto,
        "stream": False,
        "options": {
            "temperature": 0.35,
            "top_p": 0.9,
            "min_p": 0.05,
            "repeat_penalty": 1.12
        }
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        return res.get("response", "").strip()

def main():
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            texto = f.read()
    elif not sys.stdin.isatty():
        texto = sys.stdin.read()
    else:
        print("Digite ou cole o texto acadêmico (pressione Ctrl+D no final para processar):")
        texto = sys.stdin.read()

    texto = texto.strip()
    if not texto:
        print("Erro: Nenhum texto fornecido.")
        sys.exit(1)

    print("\n⏳ Processando com luiz-academico v2.0 (Ollama local)...\n")
    resultado = reescrever(texto)
    print("=" * 70)
    print("TEXTO REESCRITO:")
    print("=" * 70)
    print(resultado)
    print("=" * 70)

    # Salva temporário para verificação
    tmp_path = "/tmp/resultado_luiz_academico.txt"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(resultado)

    # Executa verificar-ia se disponível
    verificador = "/home/luiz/.local/bin/verificar-ia"
    if os.path.exists(verificador):
        print("\n📊 Rodando análise forense do GPTZero 4.1m...\n")
        subprocess.run([verificador, tmp_path])

if __name__ == "__main__":
    main()
