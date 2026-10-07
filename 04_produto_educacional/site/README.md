# Protótipo local — cinco modelos de machine learning

Versão simplificada e autoral, em português brasileiro, para estudantes iniciantes do Ensino Médio. Os cinco módulos são regressão linear, regressão logística, k-vizinhos mais próximos, árvore de decisão e k-means. O nome visual “plural.” é provisório; os modelos e conteúdos ainda exigem validação com o professor Marcos Braga.

## Executar

```bash
npm install
npm run dev
```

Abra o endereço local informado pelo Vite. Para verificar: `npm run test:run`, `npm run lint` e `npm run build`.

## Recorte pedagógico

Cada módulo propõe uma pergunta, hipótese, visualização 2D/3D com alternativa textual, controles, consequência visível, fórmula interpretada, explicação própria e desafio de aplicação. Há agora uma **aula guiada inicial**, com situação-problema, um controle prioritário, cálculo ligado ao estado do gráfico e uma questão com retorno imediato. O modo livre mantém os controles avançados e as vistas 3D. A abertura explica termos básicos e sugere um percurso para quem chega do zero. Consulte o [plano de aprendizagem para iniciantes](PLANO_APRENDIZAGEM_INICIANTES.md).

Os dados são sintéticos. Logística e árvore mostram resultados nos exemplos usados para ajuste e em pequenos casos reservados, sem sugerir que esses números comprovem generalização. As respostas digitadas só existem durante a sessão da página; não são enviadas ou salvas.

A abertura e os cinco módulos usam um ambiente visual autoral de azul-marinho profundo, com campo decorativo de pontos que deriva lentamente e reage à direção do cursor nas proximidades. Ele pode ser pausado, fica estático com preferência por movimento reduzido ou toque e não altera os cálculos dos modelos. Os cartões claros preservam a leitura dos experimentos. O efeito usa Canvas nativo; os gráficos de aprendizagem permanecem em SVG com descrições textuais.

- **Linear:** reta manual ou treinada por descida do gradiente, ponto atípico, resíduos, MSE, ajuste de mínimos quadrados, trajetória do erro e superfície 3D da perda.
- **Logística:** curva manual ou treinada por perda logarítmica, dois conjuntos de exemplos, limiar de decisão, acertos de treino, trajetória e superfície 3D da perda.
- **k-NN:** duas formas de dados, distância euclidiana/Manhattan, voto simples/ponderado, regiões e superfície 3D da força do voto. O algoritmo não ajusta parâmetros em um treino.
- **Árvore:** divisões aprendidas por impureza de Gini, limite de profundidade, regras/caminho, regiões e patamares 3D da proporção de cada folha.
- **k-means:** duas formas de dados e posições iniciais, `k` 2 ou 3, atribuição e atualização por etapas, WSS por rodada e superfície 3D da distância aos centros.

## Limites

Este protótipo não comprova ganho de aprendizagem, não foi validado com estudantes e não define a lista final de modelos. As projeções 3D representam métricas calculadas e preservam texto alternativo; ainda exigem auditoria de acessibilidade. A referência NEURON orientou apenas categorias gerais de navegação e interação pública; código, texto, identidade e exemplos são próprios. Não há backend, conta, banco de dados, API, telemetria ou deploy.
