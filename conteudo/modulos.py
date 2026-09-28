"""Conteúdo do curso Áreas do INEMA Eventos (edição v2). Fontes lidas em 28/09/2026."""
from conteudo import trilha1, trilha2, trilha3
TRACKS=[('Gerenciar e comandar agentes','emerald','Gestão de IA, AGI-ready e IA Cultivada: o trabalho passa a ser dirigir, cultivar e avaliar agentes.'),
('Ferramentas e ambiente','blue','Claude → Codex, Codex + Claude e OSWork: onde os agentes trabalham e como não ficar preso a um só.'),
('Melhorar, decidir e abrir','purple','RSI, JEV e WebMCP: melhorar com teste, decidir com avaliação e preparar o site para agentes.')]
MODULES=[];FIGURES={}
for t,mod in enumerate([trilha1,trilha2,trilha3]):
 for (i,j),fg in mod.FIGURES.items():FIGURES[(t*3+i,j)]=fg
 MODULES.extend(mod.MODULES)
# Nota do menu do site (shared/header.json), usada no mapa da landing.
NOTES={'gestao-ia':'2027: gerenciar agentes','agi-ready':'comandar agentes','ia-cultivada':'não se programa, se cultiva',
'claude-codex':'migre ou fique agnóstico','codex-claude':'usar os dois juntos','oswork':'do chat ao seu ambiente de agentes',
'rsi':'ciclos de melhoria em IA','jev':'decisões de IA na prática','webmcp':'sites que conversam com agentes'}
