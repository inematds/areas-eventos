#!/usr/bin/env python3
"""Traduz i18n/source.json (PT) para EN/ES pelo Codex da ASSINATURA (`codex exec -m gpt-6-luna`), sem chave de API.
Só manda texto (nunca HTML/código). Cache por chave em i18n/<lang>.json: reenvia apenas o que falta ou mudou
(hash da fonte em i18n/<lang>.hash.json). Valida chaves e placeholders {x}; unidade inválida volta na próxima rodada.
Uso: python3 scripts/traduzir.py en es"""
import sys,json,os,re,subprocess,tempfile,hashlib,time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];I=ROOT/'i18n'
MODELO=os.environ.get('CODEX_MODELO','gpt-6-luna');PARALELO=4;LOTE_CHARS=9000;RODADAS=3
NOMES={'en':'English (US)','es':'Spanish (neutral Latin American, "tú")'}
SISTEMA="""You translate a short Portuguese (Brazil) course into {nome}. The course explains the nine subject areas of the
site eventos.inema.pro (INEMA, a free AI education community). Audience: professionals and managers, plain adult language,
short sentences, address the reader as "you". No hype.
Rules:
- Input is a JSON object {{key: Portuguese text}}. Output the SAME keys with the translated text. Never add, drop or rename keys.
- Keep unchanged: URLs, file names, commands, code, product and course names (INEMA, INEMA.CLUB, INEMA.PRO, OSWork, LOOP-R,
  Gestoria, Claude Code, Codex, WebMCP, JEV/Jev, RSI, AGI-ready, Content2Video, INEMACCBOT, kit names like agente-claude-codex),
  placeholders in braces like {{data}} {{n}} {{id}}, and anything between < and > is a fill-in hint: translate the words inside
  but keep the < > marks.
- Area names: "Gestão de IA" -> {gestao}; "IA Cultivada" -> {cult}; keep "Claude → Codex", "Codex + Claude", "OSWork", "RSI",
  "JEV", "WebMCP", "AGI-ready" as they are.
- Keep quotation marks around phrases quoted from the site. Keep numbers as they are.
- Very short UI labels (buttons, kickers in CAPS): translate tersely and keep CAPS when the source is in caps.
Return ONLY the JSON object (no code fences, no comments)."""
AREA={'en':('"AI Management"','"Cultivated AI"'),'es':('"Gestión de IA"','"IA Cultivada"')}

def via_codex(lang,lote):
 s=SISTEMA.format(nome=NOMES[lang],gestao=AREA[lang][0],cult=AREA[lang][1])
 pedido=s+"\n\nINPUT JSON:\n"+json.dumps(lote,ensure_ascii=False)
 with tempfile.TemporaryDirectory() as d:
  out=os.path.join(d,'out.txt')
  r=subprocess.run(['codex','exec','-m',MODELO,'--skip-git-repo-check','--ephemeral','--sandbox','read-only','-C',d,'-o',out,'-'],
   input=pedido,capture_output=True,text=True,timeout=900)
  if r.returncode or not os.path.exists(out):raise RuntimeError(f'codex rc={r.returncode}: {r.stderr[-300:]}')
  txt=open(out,encoding='utf-8').read().strip()
 txt=re.sub(r'^```(?:json)?\s*|\s*```$','',txt)
 return json.loads(txt[txt.index('{'):txt.rindex('}')+1])

PH=re.compile(r'\{[a-z]+\}')
def valido(pt,tr):
 if not isinstance(tr,str) or not tr.strip():return False
 if sorted(PH.findall(pt))!=sorted(PH.findall(tr)):return False
 if pt.count('<')!=tr.count('<') or pt.count('>')!=tr.count('>'):return False
 for u in re.findall(r'https?://\S+',pt):
  if u.rstrip('.,;)') not in tr:return False
 return True

def lotes(d):
 out=[];cur={};n=0
 for k,v in d.items():
  if cur and n+len(v)>LOTE_CHARS:out.append(cur);cur={};n=0
  cur[k]=v;n+=len(v)
 if cur:out.append(cur)
 return out

src=json.loads((I/'source.json').read_text())
h=lambda s:hashlib.sha1(s.encode()).hexdigest()[:12]
for lang in sys.argv[1:] or ['en','es']:
 f=I/f'{lang}.json';fh=I/f'{lang}.hash.json'
 cache=json.loads(f.read_text()) if f.exists() else {};hashes=json.loads(fh.read_text()) if fh.exists() else {}
 for rodada in range(1,RODADAS+1):
  falta={k:v for k,v in src.items() if k not in cache or hashes.get(k)!=h(v)}
  if not falta:break
  ls=lotes(falta);t0=time.time()
  print(f'{lang} rodada {rodada}: {len(falta)} unidades em {len(ls)} lotes',flush=True)
  def run(l):
   try:return l,via_codex(lang,l)
   except Exception as e:print(f'  lote falhou: {e}',flush=True);return l,{}
  with ThreadPoolExecutor(PARALELO) as ex:
   for l,res in ex.map(run,ls):
    for k,v in l.items():
     if k in res and valido(v,res[k]):cache[k]=res[k];hashes[k]=h(v)
  f.write_text(json.dumps(cache,ensure_ascii=False,indent=1));fh.write_text(json.dumps(hashes,indent=1))
  print(f'  {round(time.time()-t0)} s',flush=True)
 falta=[k for k,v in src.items() if k not in cache or hashes.get(k)!=h(v)]
 print(f'{lang}: {len(src)-len(falta)}/{len(src)} traduzidas'+(f'; faltam: {falta[:10]}' if falta else ''))
