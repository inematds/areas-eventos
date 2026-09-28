# Esquema do conteúdo — curso "Áreas do INEMA Eventos" (edição v2)

Curso rápido que explica **o que é cada uma das 9 áreas de assunto** do eventos.inema.pro.
3 trilhas × 3 módulos; **1 módulo = 1 área**; **6 tópicos por módulo**. PT-BR.

Cada trilha é um arquivo Python `conteudo/trilhaN.py` com exatamente este formato:

```python
"""Trilha N — <nome>. Fontes: inemaeventos/<slug>/index.html + shared/acesso.json (lidas em 28/09/2026)."""
MODULES=[]
FIGURES={}
def M(title,goal,lab,steps,check,answer,topics,snippet,sources,slug):
    MODULES.append(dict(title=title,goal=goal,lab=lab,steps=steps,check=check,answer=answer,
                        topics=topics,snippet=snippet,sources=sources,slug=slug))
def T(title,what,why,keys,example,action):
    return dict(title=title,what=what,why=why,keys=keys,example=example,action=action)

M('<título do módulo = nome da área + gancho curto>',
  '<goal: 1 frase — o que o aluno sabe explicar ao final>',
  '<lab: título do laboratório final, ex.: "Sua ficha da área">',
  ['<passo 1>','<passo 2>','<passo 3>','<passo 4>'],     # 4 passos práticos, verificáveis
  '<check: pergunta de revisão>',
  '<answer: resposta comentada, 1-2 frases>',
  [T(...), T(...), T(...), T(...), T(...), T(...)],      # EXATAMENTE 6 tópicos
  ('<título do bloco copiável>', '<texto do bloco: prompt pronto p/ Claude Code/ChatGPT ou comando; variáveis como <isto você troca>>'),
  [('<rótulo>','https://...'), ...],                     # 2-4 fontes: a página da área + curso/projeto principal (URLs reais, da página ou do acesso.json)
  '<slug>')                                              # ex.: 'gestao-ia'

FIGURES[(<índice local do módulo 0..2>, <tópico 1..6>)] = dict(kind=..., caption='...', items=[...])
```

## Campos de cada tópico `T(title, what, why, keys, example, action)`

- `title`: curto (até ~38 caracteres, cabe num cartão SVG).
- `what` (**O que é**): 4-6 frases, concretas. Define todo termo técnico na 1ª vez ("Um agente é…").
- `why` (**Por que aprender**): 2-3 frases.
- `keys` (**Conceitos-chave**): uma linha de termos separados por ";" ou frase curta. Vira o resumo do módulo.
- `example` (**Na prática**): 2-3 frases com uma situação real de trabalho (fictícia, sem nomes reais de clientes).
- `action`: 1 frase imperativa, algo que o aluno faz agora (vira "Experimente agora" / "✓ Faça").

Sugestão de sequência dos 6 tópicos (adapte ao que a página tem):
1. O que é a área (a tese / o h1 da página) · 2. Para quem é e o problema que resolve · 3-4. Os blocos centrais da página (h2) ·
5. Por onde começar (o "melhor primeiro passo" que a página traz) · 6. O que a área reúne (cursos/projetos do `acesso.json`) e onde ir.

## FIGURES (diagramas SVG gerados pelo build) — 3 a 4 por módulo

`kind` possíveis e formato de `items`:
- `grid`: lista de strings curtas (até 8; ≤14 caracteres cada, cabem em caixa de 110px).
- `columns`: lista de tuplas `(título, subtítulo)` (3-5 itens; títulos ≤16 car., subtítulos ≤22); opcional `base=['a','b']`.
- `flow`: lista de strings ou tuplas (4-6 etapas; ≤18 car.) — setas entre etapas.
- `stack`: lista de strings ou `(título, nota)` (3-6 camadas, escada).
- `tree`: lista de `(rótulo, profundidade)` — árvore de arquivos monoespaçada.
- `timeline`: lista de strings ou `(título, sobre-título)` (3-5 marcos; títulos ≤14 car.).
`caption` = 1 frase que ENSINA (o que olhar e o que significa). Tópicos diferentes por figura; não repita o tópico 1 (o hero já resume os 6 títulos).

## Regras de conteúdo (obrigatórias)

- **Só fatos, frases, números e nomes que estão na página da área** (`~/projetos/inemaeventos/<slug>/index.html`, versão PT na raiz da pasta) **e em `~/projetos/inemaeventos/shared/acesso.json`** (bloco da rota `/<slug>/`). Se houver `<slug>/CONTEUDO.md`, pode usar. Nada inventado.
- **Sem data, preço ou promessa que a página não tenha.** Claude → Codex: o painel diz "Evento: data a anunciar" — não citar data. IA Cultivada: há um vídeo em produção, NÃO publicado — não citar vídeo. Não citar vídeos do Explicavideos (nenhum foi produzido).
- Conteúdo de terceiros citado na página (ex.: vídeo externo): só referenciar, não reproduzir.
- Tom: português claro, frases curtas, sem jargão órfão, sem "revolucionário", sem emojis no texto.
- `snippet` = exemplo **copia-e-cola real**: um prompt completo que o aluno cola no Claude/ChatGPT/Codex para aplicar a área ao próprio trabalho (ex.: "Leia https://eventos.inema.pro/<slug>/ e ... Minha situação: <descreva seu processo>"), ou um comando real. O `lab.steps` deve dizer como verificar o resultado.
- Strings Python: use aspas simples e escape apóstrofos; o arquivo precisa importar sem erro (`python3 -c "import conteudo.trilhaN"` na raiz do projeto).
- Tamanho: cada módulo ≈ 6 tópicos × (what 5 frases + why 2-3 + keys + example + action). Não encurte: o módulo final precisa ter densidade parecida com `~/projetos/oswork/conteudo/modulos.py` (veja 1-2 tópicos lá como referência de estilo).
