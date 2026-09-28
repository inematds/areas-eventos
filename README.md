# Áreas do INEMA Eventos — o que é cada área

Curso rápido no formato INEMA v2: explica as nove áreas de assunto do [eventos.inema.pro](https://eventos.inema.pro/).
Três trilhas, nove módulos (um por área), 54 tópicos. Português.

- Curso: https://inematds.github.io/areas-eventos/
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

Estudar localmente: `python3 -m http.server 8080` e abrir http://localhost:8080 (progresso entre páginas precisa de origem HTTP).

## Mais no INEMA.CLUB

- Ficha do curso: https://www.inema.club/cursos/307-areas-do-inema-eventos-o-que-e-cada-area/
- Guia: https://www.inema.club/aprender-inteligencia-artificial/
- Todos os cursos: https://www.inema.club/cursos/
