"""Catálogo de tradução: extrai as unidades de texto do conteúdo autoral (PT) e aplica EN/ES por chave.
Código, IDs, URLs e slugs nunca vão para tradução."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];I18N=ROOT/'i18n'

def content_units(MODULES,TRACKS,FIGURES,NOTES):
 u={}
 for t,tr in enumerate(TRACKS):u[f'track.{t}.name']=tr[0];u[f'track.{t}.desc']=tr[2]
 for s,n in NOTES.items():u[f'note.{s}']=n
 for i,m in enumerate(MODULES):
  p=f'm{i}.'
  for k in ('title','goal','lab','check','answer'):u[p+k]=m[k]
  for k,s in enumerate(m['steps']):u[p+f'step.{k}']=s
  u[p+'snippet.title']=m['snippet'][0];u[p+'snippet.body']=m['snippet'][1]
  for k,(label,_) in enumerate(m['sources']):u[p+f'source.{k}']=label
  for j,tp in enumerate(m['topics']):
   for f in ('title','what','why','keys','example','action'):u[p+f'topic.{j}.{f}']=tp[f]
 for (i,j),fg in FIGURES.items():
  p=f'fig.{i}.{j}.';u[p+'caption']=fg['caption']
  for k,it in enumerate(fg['items']):
   if isinstance(it,str):u[p+f'item.{k}']=it
   elif isinstance(it[1],int):u[p+f'item.{k}']=it[0]      # tree: (rótulo, profundidade)
   else:u[p+f'item.{k}.0']=it[0];u[p+f'item.{k}.1']=it[1]
  for k,b in enumerate(fg.get('base',[])):u[p+f'base.{k}']=b
 return u

def load(lang):
 f=I18N/f'{lang}.json'
 return json.loads(f.read_text()) if f.exists() else {}

def apply(lang,MODULES,TRACKS,FIGURES,NOTES):
 tr=load(lang);g=lambda k,d:tr.get(k,d)
 TR=[(g(f'track.{t}.name',a),c,g(f'track.{t}.desc',b)) for t,(a,c,b) in enumerate(TRACKS)]
 NT={s:g(f'note.{s}',n) for s,n in NOTES.items()}
 MS=[]
 for i,m in enumerate(MODULES):
  p=f'm{i}.';m=copy.deepcopy(m)
  for k in ('title','goal','lab','check','answer'):m[k]=g(p+k,m[k])
  m['steps']=[g(p+f'step.{k}',s) for k,s in enumerate(m['steps'])]
  m['snippet']=(g(p+'snippet.title',m['snippet'][0]),g(p+'snippet.body',m['snippet'][1]))
  m['sources']=[(g(p+f'source.{k}',a),u) for k,(a,u) in enumerate(m['sources'])]
  m['topics']=[{f:g(p+f'topic.{j}.{f}',tp[f]) for f in tp} for j,tp in enumerate(m['topics'])]
  MS.append(m)
 FG={}
 for (i,j),fg in FIGURES.items():
  p=f'fig.{i}.{j}.';fg=copy.deepcopy(fg);fg['caption']=g(p+'caption',fg['caption']);items=[]
  for k,it in enumerate(fg['items']):
   if isinstance(it,str):items.append(g(p+f'item.{k}',it))
   elif isinstance(it[1],int):items.append((g(p+f'item.{k}',it[0]),it[1]))
   else:items.append((g(p+f'item.{k}.0',it[0]),g(p+f'item.{k}.1',it[1])))
  fg['items']=items
  if 'base' in fg:fg['base']=[g(p+f'base.{k}',b) for k,b in enumerate(fg['base'])]
  FG[(i,j)]=fg
 return MS,TR,FG,NT,tr
