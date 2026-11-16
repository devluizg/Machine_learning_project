#!/usr/bin/env python3
"""Servidor local para construtor interativo de frases por escolha de palavras (próximo token)."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

BASE_DIR = Path("/home/luiz/Machine_learning_project/09_orquestracao_ia")
OUT_FILE = BASE_DIR / "luiz_escolhas_tokens.jsonl"
HTML_FILE = BASE_DIR / "construtor_tokens.html"

# Cada item tem "segments": strings fixas ou {"slot": id, "options": [...]}
TEMPLATES = [
    {
        "id": "t01",
        "ai_baseline": "Nesse sentido, o uso de ferramentas digitais na escola pública constitui um desafio significativo para os docentes.",
        "segments": [
            {"slot": "abertura", "options": ["Na escola pública,", "Dentro da escola pública,", "Nesse cenário,", "Quando olhamos para a escola pública,"]},
            " o uso de ferramentas digitais ",
            {"slot": "verbo", "options": ["é", "acaba sendo", "se mostra", "funciona como"]},
            " um desafio ",
            {"slot": "intensidade", "options": ["grande", "bem real", "importante", "significativo"]},
            " para o professor."
        ]
    },
    {
        "id": "t02",
        "ai_baseline": "Além disso, a simples entrega de computadores aos estudantes não garante, por si só, a compreensão dos conceitos.",
        "segments": [
            {"slot": "conector", "options": ["Além disso,", "Porém,", "Ou seja,", "Na prática,"]},
            " só entregar um computador para o aluno ",
            {"slot": "verbo", "options": ["não garante", "não basta para", "não resolve", "não assegura"]},
            " que ele ",
            {"slot": "acao", "options": ["entenda o conteúdo.", "compreenda o conceito.", "aprenda de verdade.", "consiga explicar o que fez."]}
        ]
    },
    {
        "id": "t03",
        "ai_baseline": "Dessa forma, torna-se indispensável que o professor planeje previamente os objetivos pedagógicos da aula.",
        "segments": [
            {"slot": "conector", "options": ["Por isso,", "Dessa forma,", "Assim,", "Logo,"]},
            " ",
            {"slot": "necessidade", "options": ["é preciso que", "fica claro que", "o professor precisa", "é fundamental que"]},
            " ",
            {"slot": "acao", "options": ["planejar antes o que a turma deve aprender.", "o professor defina antes os objetivos da aula.", "se decida com calma o foco da aula.", "o docente organize as metas antes de ir para a sala."]}
        ]
    },
    {
        "id": "t04",
        "ai_baseline": "Contudo, observa-se que muitos alunos conseguem resolver exercícios imediatos, mas enfrentam dificuldades diante de situações inéditas.",
        "segments": [
            {"slot": "conector", "options": ["Porém,", "Mesmo assim,", "Muitas vezes,", "Na sala de aula,"]},
            " o aluno acerta o exercício logo depois da explicação, ",
            {"slot": "contraste", "options": ["mas trava", "só que não consegue responder", "mas tem dificuldade", "e acaba errando"]},
            " quando aparece ",
            {"slot": "situacao", "options": ["uma pergunta diferente.", "um problema novo.", "uma situação parecida com dados trocados.", "outro exemplo fora do padrão."]}
        ]
    },
    {
        "id": "t05",
        "ai_baseline": "Portanto, avaliações baseadas apenas em questionários de opinião oferecem um retrato parcial da aprendizagem discente.",
        "segments": [
            {"slot": "conector", "options": ["Por isso,", "Desse modo,", "Então,", "Com isso,"]},
            " questionários simples e testes rápidos ",
            {"slot": "verbo", "options": ["mostram só uma parte", "dão apenas um retrato incompleto", "não revelam tudo", "captam pouco"]},
            " ",
            {"slot": "objeto", "options": ["do que o estudante aprendeu.", "da aprendizagem da turma.", "do processo de ensino.", "do entendimento real dos alunos."]}
        ]
    },
    {
        "id": "t06",
        "ai_baseline": "Sob essa perspectiva, o debate coletivo mediado pelo docente favorece a construção de justificativas consistentes pelos aprendizes.",
        "segments": [
            {"slot": "abertura", "options": ["Quando o professor conduz a conversa em sala,", "Com a mediação do professor,", "Durante o debate com a turma,", "No momento da discussão coletiva,"]},
            " os alunos ",
            {"slot": "verbo", "options": ["passam a explicar", "conseguem justificar", "começam a construir", "vão entendendo melhor"]},
            " ",
            {"slot": "fecho", "options": ["por que chegaram naquela resposta.", "o raciocínio por trás do resultado.", "como o conteúdo funciona na prática.", "as suas próprias conclusões."]}
        ]
    },
    {
        "id": "t07",
        "ai_baseline": "Ademais, fatores externos como infraestrutura precária e calendário irregular impactam diretamente a execução do planejamento escolar.",
        "segments": [
            {"slot": "abertura", "options": ["Na rotina da escola pública,", "Além do conteúdo,", "No dia a dia escolar,", "Fora da teoria,"]},
            " problemas como falta de internet, ",
            {"slot": "exemplo", "options": ["poucos computadores e tempo curto de aula", "falta de merenda e transporte irregular", "calendário apertado e salas cheias", "equipamentos antigos e ritmo diferente da turma"]},
            " ",
            {"slot": "verbo", "options": ["mudam todo o planejamento.", "pesam muito no trabalho do professor.", "acabam interferindo diretamente na aula.", "exigem adaptação constante."]}
        ]
    },
    {
        "id": "t08",
        "ai_baseline": "A revisão da literatura restringiu-se a periódicos internacionais em língua inglesa, excluindo experiências desenvolvidas no contexto brasileiro.",
        "segments": [
            {"slot": "sujeito", "options": ["Como a busca aceitou apenas artigos em inglês,", "A revisão olhou só textos em inglês, e por isso", "Por ter selecionado somente periódicos em inglês,", "Infelizmente, o levantamento deixou de fora"]},
            " ",
            {"slot": "conseq", "options": ["experiências feitas em escolas brasileiras ficaram de fora.", "muitos trabalhos publicados em português não entraram.", "a realidade das nossas escolas acabou não aparecendo.", "estudos feitos no Brasil não foram incluídos."]}
        ]
    },
    {
        "id": "t09",
        "ai_baseline": "Quando os estudantes formulam hipóteses previamente à manipulação da interface, o engajamento transforma-se em investigação ativa.",
        "segments": [
            {"slot": "tempo", "options": ["Antes de mexer nos controles da tela,", "Se o aluno anota uma hipótese antes de testar,", "Quando o estudante olha os dados primeiro,", "Ao pedir que a turma faça uma previsão inicial,"]},
            " a atividade ",
            {"slot": "verbo", "options": ["deixa de ser só um monte de cliques", "vira uma investigação de verdade", "ganha sentido pedagógico", "passa a exigir reflexão"]},
            " e o aluno ",
            {"slot": "fecho", "options": ["observa o que mudou no resultado.", "precisa explicar por que acertou ou errou.", "entende melhor o efeito de cada ajuste.", "presta mais atenção no comportamento dos dados."]}
        ]
    },
    {
        "id": "t10",
        "ai_baseline": "Em suma, a tecnologia educacional não substitui o papel orientador do professor na condução do processo formativo.",
        "segments": [
            {"slot": "fecho", "options": ["Fica claro, então, que", "No fim das contas,", "Ou seja,", "Tudo isso mostra que"]},
            " a tecnologia ",
            {"slot": "verbo", "options": ["não resolve o ensino sozinha,", "não substitui o trabalho do professor,", "sozinha não ensina ninguém,", "é apenas um apoio,"]},
            " ",
            {"slot": "compl", "options": ["pois o que gera aprendizado é a tarefa bem pensada e o diálogo em sala.", "porque quem dá sentido à aula é a mediação do docente.", "e o aprendizado depende das perguntas feitas durante a aula.", "sendo o professor quem conduz o caminho da turma."]}
        ]
    },
    {
        "id": "t11",
        "ai_baseline": "A prática regular de atividades físicas na infância atua como mecanismo preventivo contra distúrbios metabólicos precoces.",
        "segments": [
            {"slot": "abertura", "options": ["Quando a criança pratica esportes desde cedo,", "Criar o hábito de fazer atividade física na infância", "Colocar as crianças para se movimentar regularmente", "O esporte praticado ainda na infância"]},
            " ",
            {"slot": "verbo", "options": ["ajuda a evitar", "funciona como proteção contra", "reduz bastante o risco de", "previne"]},
            " ",
            {"slot": "fecho", "options": ["problemas de saúde que aparecem cada vez mais cedo.", "doenças ligadas ao sedentarismo.", "o excesso de peso e outros problemas físicos.", "complicações de saúde na vida adulta."]}
        ]
    },
    {
        "id": "t12",
        "ai_baseline": "O diagnóstico inicial permite mapear os conhecimentos prévios dos discentes antes da intervenção pedagógica.",
        "segments": [
            {"slot": "sujeito", "options": ["Começar com um diagnóstico inicial", "Aplicar uma atividade diagnóstica no primeiro dia", "Antes de iniciar as aulas, fazer um levantamento prévio", "O diagnóstico no começo da sequência"]},
            " ",
            {"slot": "verbo", "options": ["serve para mostrar", "ajuda o professor a descobrir", "permite registrar", "deixa claro"]},
            " ",
            {"slot": "fecho", "options": ["o que os alunos já sabem sobre o assunto.", "quais dúvidas a turma traz logo de início.", "de onde a aula precisa partir.", "qual é o nível real da turma."]}
        ]
    },
    {
        "id": "t13",
        "ai_baseline": "A abordagem tradicional, excessivamente focada no formalismo algébrico, frequentemente distancia os estudantes da intuição conceitual.",
        "segments": [
            {"slot": "abertura", "options": ["Quando a aula foca só em fórmula e conta pesada,", "O ensino tradicional, cheio de matemática abstrata,", "Ficar apenas na formalização matemática", "Ensinar só com fórmulas decoradas"]},
            " ",
            {"slot": "verbo", "options": ["acaba afastando o aluno", "faz o estudante se distanciar", "dificulta que a turma entenda", "desanima quem está tentando aprender"]},
            " ",
            {"slot": "fecho", "options": ["da ideia principal por trás do conteúdo.", "do funcionamento real do conceito.", "de como aquilo se aplica no dia a dia.", "do que realmente importa entender."]}
        ]
    },
    {
        "id": "t14",
        "ai_baseline": "Os registros contínuos coletados ao longo dos encontros possibilitam acompanhar a evolução argumentativa dos alunos.",
        "segments": [
            {"slot": "abertura", "options": ["Guardar registros em cada aula", "Anotar as respostas dos alunos ao longo dos oito encontros", "Acompanhar o que a turma escreve durante toda a sequência", "Os registros feitos aula após aula"]},
            " ",
            {"slot": "verbo", "options": ["permitem ver", "ajudam a acompanhar", "mostram claramente", "revelam"]},
            " ",
            {"slot": "fecho", "options": ["como as explicações dos estudantes vão mudando com o tempo.", "se o jeito de o aluno argumentar realmente evoluiu.", "onde a turma avançou e onde ainda trava.", "como o raciocínio deles foi amadurecendo."]}
        ]
    },
    {
        "id": "t15",
        "ai_baseline": "A visualização gráfica em tempo real facilita a percepção das relações entre parâmetros de entrada e resultados obtidos.",
        "segments": [
            {"slot": "sujeito", "options": ["Ver o gráfico mudar na hora na tela", "A visualização do gráfico em tempo real", "Quando o aluno mexe em um número e o desenho muda,", "Olhar a reta ou os pontos se mexendo na tela"]},
            " ",
            {"slot": "verbo", "options": ["facilita entender", "ajuda a perceber", "torna bem mais claro", "mostra na prática"]},
            " ",
            {"slot": "fecho", "options": ["como cada parâmetro altera a resposta.", "a ligação entre os dados de entrada e a saída.", "o efeito direto de cada mudança feita.", "por que o resultado final foi diferente."]}
        ]
    },
    {
        "id": "t16",
        "ai_baseline": "É imprescindível destacar que a formação docente contínua constitui elemento central para a integração crítica de tecnologias digitais.",
        "segments": [
            {"slot": "abertura", "options": ["Não dá para esquecer que", "Vale lembrar também que", "Outro ponto importante é que", "Além disso,"]},
            " o professor precisa de ",
            {"slot": "meio", "options": ["formação e tempo para estudar", "apoio contínuo na escola", "preparo prático para usar essas ferramentas", "espaço para trocar experiências com colegas"]},
            " ",
            {"slot": "fecho", "options": ["se quisermos que a tecnologia faça diferença na sala.", "antes de cobrar inovação dentro da escola.", "para usar os recursos digitais com segurança e propósito.", "sem virar apenas mais uma tarefa solta."]}
        ]
    },
    {
        "id": "t17",
        "ai_baseline": "Desse modo, o desafio final inédito verifica se os conhecimentos construídos são mobilizados em contextos distintos dos trabalhados em sala.",
        "segments": [
            {"slot": "abertura", "options": ["No fim da sequência, o desafio inédito", "Já o desafio final com dados novos", "Por isso, a atividade final", "Para fechar os encontros, o último desafio"]},
            " ",
            {"slot": "verbo", "options": ["testa se o estudante consegue usar", "ajuda a ver se a turma sabe aplicar", "verifica se o aluno realmente leva", "mostra se o aprendizado se sustenta"]},
            " ",
            {"slot": "fecho", "options": ["o que aprendeu em uma situação diferente daquela treinada em aula.", "esse raciocínio diante de um problema novo.", "os conceitos trabalhados para fora dos exemplos já vistos.", "o conhecimento sem precisar de ajuda passo a passo."]}
        ]
    },
    {
        "id": "t18",
        "ai_baseline": "A interação entre pares no ambiente esportivo fomenta o desenvolvimento da empatia, da cooperação e da resiliência emocional.",
        "segments": [
            {"slot": "abertura", "options": ["No contato diário com colegas e treinador,", "Jogando em equipe desde pequeno,", "Dentro de um time ou grupo esportivo,", "Convivendo com outras crianças no esporte,"]},
            " ",
            {"slot": "sujeito", "options": ["a criança aprende a ouvir os outros,", "os jovens treinam a paciência e o respeito,", "fica mais fácil aprender a trabalhar junto,", "cada um descobre como lidar com colegas diferentes,"]},
            " ",
            {"slot": "fecho", "options": ["a cooperar e a aceitar tanto a vitória quanto a derrota.", "seguindo regras e buscando um objetivo em comum.", "habilidades muito válidas para a vida adulta.", "construindo equilíbrio emocional dentro e fora da quadra."]}
        ]
    },
    {
        "id": "t19",
        "ai_baseline": "Todavia, diversos estudos analisados não explicitam o referencial teórico-pedagógico que fundamenta suas escolhas metodológicas.",
        "segments": [
            {"slot": "abertura", "options": ["Outro problema encontrado na revisão é que", "Mesmo assim,", "Por outro lado,", "Chama atenção o fato de que"]},
            " boa parte dos estudos ",
            {"slot": "verbo", "options": ["não deixa claro", "nem explica", "deixa de mostrar", "não explicita"]},
            " ",
            {"slot": "fecho", "options": ["qual teoria de ensino orientou as atividades em sala.", "em que ideia pedagógica a aula foi baseada.", "por que escolheu aquele caminho metodológico.", "qual base educacional sustentou a proposta."]}
        ]
    },
    {
        "id": "t20",
        "ai_baseline": "Consequentemente, a repetição mecânica de procedimentos impede que o aluno reconheça o propósito conceitual da tarefa executada.",
        "segments": [
            {"slot": "abertura", "options": ["Quando a aula vira só repetição de passos,", "Se o estudante apenas aperta botões sem pensar,", "Ficar repetindo cliques no automático", "Seguir um roteiro mecânico sem questionamento"]},
            " ",
            {"slot": "verbo", "options": ["impede o aluno de entender", "não deixa a turma perceber", "atrapalha a compreensão sobre", "faz com que o estudante não enxergue"]},
            " ",
            {"slot": "fecho", "options": ["para que serve aquela tarefa de verdade.", "o conceito que está por trás da atividade.", "o motivo de o resultado sair daquele jeito.", "a relação entre o problema e a resposta."]}
        ]
    }
]


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
        elif self.path == "/api/templates":
            done_ids = set()
            saved_count = 0
            if OUT_FILE.exists():
                for line in OUT_FILE.read_text(encoding="utf-8").splitlines():
                    if line.strip():
                        r = json.loads(line)
                        done_ids.add(r.get("template_id"))
                        saved_count += 1
            pending = [t for t in TEMPLATES if t["id"] not in done_ids]
            self._send_json(200, {"templates": pending, "saved_count": saved_count, "total": len(TEMPLATES)})
        elif self.path == "/api/export":
            content = OUT_FILE.read_bytes() if OUT_FILE.exists() else b""
            self.send_response(200)
            self.send_header("Content-Type", "application/jsonl; charset=utf-8")
            self.send_header("Content-Disposition", 'attachment; filename="luiz_escolhas_tokens.jsonl"')
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == "/api/save":
            length = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            rec = {
                "source": "luiz_token_builder",
                "template_id": payload.get("template_id"),
                "instruction": "Reescreva a frase acadêmica abaixo com a voz autoral de Luiz Gabriel, mantendo os fatos e números.",
                "input": payload.get("ai_baseline", ""),
                "output": payload.get("output", "").strip(),
                "choices": payload.get("choices", {}),
            }
            if not rec["output"]:
                self._send_json(400, {"error": "output required"})
                return
            with open(OUT_FILE, "a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            saved_count = sum(1 for l in OUT_FILE.read_text(encoding="utf-8").splitlines() if l.strip())
            self._send_json(200, {"ok": True, "saved_count": saved_count})
        else:
            self.send_error(404)


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8787), Handler)
    print("Construtor rodando em http://127.0.0.1:8787", flush=True)
    server.serve_forever()
