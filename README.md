# Áreas do INEMA Eventos — o que é cada área

Curso rápido no formato INEMA v2: explica as nove áreas de assunto do [eventos.inema.pro](https://eventos.inema.pro/).
Três trilhas, nove módulos (um por área), 54 tópicos por idioma. Português, inglês e espanhol.

- Curso: https://inematds.github.io/areas-eventos/ · English: https://inematds.github.io/areas-eventos/en/ · Español: https://inematds.github.io/areas-eventos/es/
- Versão: ver `VERSION`

| Trilha | Áreas |
|---|---|
| 1 · Gerenciar e comandar agentes | Gestão de IA · AGI-ready · IA Cultivada |
| 2 · Ferramentas e ambiente | Claude → Codex · Codex + Claude · OSWork |
| 3 · Melhorar, decidir e abrir | RSI · JEV · WebMCP |

## Fontes

O conteúdo vem só das páginas das áreas (`~/projetos/inemaeventos/<slug>/index.html`, `CONTEUDO.md` quando existe) e de
`inemaeventos/shared/acesso.json`, lidas em 28/09/2026. Mapa das áreas: `~/projetos/wifi/PLANO-VIDEOS-EXPLICAVIDEOS-EVENTOS.md`.

## Editar e gerar

Conteúdo em `conteudo/trilha1.py`, `trilha2.py`, `trilha3.py` (esquema em `conteudo/SCHEMA.md`). Gerador em `scripts/build.py`
(adaptado do OSWork v2). Depois de editar:

```bash
python3 scripts/build.py
python3 scripts/validate.py
```

## Traduções (EN/ES)

PT é a fonte. `python3 scripts/build.py pt` grava `i18n/source.json` (conteúdo + interface). `python3 scripts/traduzir.py en es`
traduz pelo Codex da assinatura (`codex exec -m gpt-6-luna`, sem chave de API), com cache e hash por chave em `i18n/<lang>.json`:
só o que mudou volta para tradução. Depois `python3 scripts/build.py` gera PT/EN/ES. `en/assets/{learn,site}.js` são as versões
traduzidas do motor, reaproveitadas do OSWork v2. Progresso e notas são separados por idioma.

Estudar localmente: `python3 -m http.server 8080` e abrir http://localhost:8080 (progresso entre páginas precisa de origem HTTP).

## Mais no INEMA.CLUB

- Ficha do curso: https://www.inema.club/cursos/307-areas-do-inema-eventos-o-que-e-cada-area/
- Guia: https://www.inema.club/aprender-inteligencia-artificial/
- Todos os cursos: https://www.inema.club/cursos/
