#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

if [ -f "luiz-academico-v2-q4_k_m.gguf" ]; then
    mv -f "luiz-academico-v2-q4_k_m.gguf" "luiz-academico-q4_k_m.gguf"
fi

if [ ! -f "luiz-academico-q4_k_m.gguf" ]; then
    echo "ERRO: Coloque o arquivo 'luiz-academico-v2-q4_k_m.gguf' (ou 'luiz-academico-q4_k_m.gguf') dentro da pasta:"
    echo "  $DIR"
    exit 1
fi

echo "Criando o modelo 'luiz-academico' no Ollama..."
ollama create luiz-academico -f Modelfile
echo ""
echo "================================================================"
echo "SUCESSO! Seu modelo especialista está instalado."
echo "Para usar no terminal, basta rodar:"
echo "  ollama run luiz-academico"
echo "E colar diretamente o parágrafo que deseja reescrever (sem precisar de prompt!)."
echo "================================================================"
