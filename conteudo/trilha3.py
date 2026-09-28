"""Trilha 3 — Melhorar, decidir e abrir para agentes. Fontes: inemaeventos/{rsi,jev,webmcp}/index.html + shared/acesso.json + rsi/CONTEUDO.md + jev/CONTEUDO.md (lidas em 28/09/2026)."""
MODULES=[]
FIGURES={}
def M(title,goal,lab,steps,check,answer,topics,snippet,sources,slug):
    MODULES.append(dict(title=title,goal=goal,lab=lab,steps=steps,check=check,answer=answer,
                        topics=topics,snippet=snippet,sources=sources,slug=slug))
def T(title,what,why,keys,example,action):
    return dict(title=title,what=what,why=why,keys=keys,example=example,action=action)

# ---------------------------------------------------------------- 0 · RSI
M('RSI: a IA que ajuda a melhorar a IA',
  'Explicar os três níveis de melhoria em IA e transformar uma ideia de melhoria num teste verificável, com versão registrada e caminho de volta.',
  'Seu primeiro ciclo de melhoria no papel',
  ['Escolha uma tarefa pequena do seu trabalho, como extrair ações de notas de reunião, e escreva qual seria a resposta correta para três exemplos fictícios.',
   'Separe esses exemplos em dois grupos: dois para desenvolver a mudança e um reservado, que você só usa na validação.',
   'Registre a versão inicial da instrução, proponha UMA mudança e rode as duas versões nos mesmos exemplos, anotando acertos, erros, custo e tempo de revisão.',
   'Confira no exemplo reservado se a mudança se sustenta; só então adote, e anote quem decidiu e como voltar à versão anterior.'],
  'Depois de dez tentativas, a nova instrução tirou nota maior no mesmo conjunto que você usou para ajustá-la. Isso prova que ela é melhor?',
  'Não. Uma avaliação conhecida pode ser explorada; a mudança precisa se sustentar em casos reservados, com os mesmos critérios. Mais tentativas ou uma nota maior não demonstram crescimento ilimitado.',
  [T('O que é RSI',
     'RSI é a sigla em inglês para automelhoria recursiva: a ideia de uma IA que ajuda a melhorar a própria IA. A pergunta central da área é prática: como um sistema propõe mudanças, testa resultados e conserva o que funciona? A página trata o tema como área de estudo e acervo aberto, com referências, exemplos e critérios para avaliar as promessas. O ponto de partida é uma distinção: melhorar uma resposta, melhorar um agente e melhorar a capacidade de criar novos agentes são coisas diferentes. Um agente, aqui, é um sistema de IA que recebe um objetivo e executa etapas com instruções, memória e ferramentas.',
     'Promessas de IA que se melhora sozinha aparecem com frequência e costumam misturar esses três níveis. Quem entende a diferença consegue perguntar o que exatamente melhorou e qual evidência sustenta isso.',
     'automelhoria recursiva; propor, testar, conservar; três níveis diferentes; acervo aberto; critérios para avaliar promessas',
     'Um fornecedor diz que seu assistente "aprende sozinho". A gestora pergunta: ele refaz a resposta, muda as próprias instruções ou produz melhorias futuras? E como isso foi medido? A resposta define se o produto está no primeiro, no segundo ou no terceiro nível.',
     'Escreva em uma frase uma promessa de melhoria automática que você já ouviu e marque qual dos três níveis ela realmente descreve.'),
   T('Três níveis que não se confundem',
     'O primeiro nível é revisar a resposta: o modelo critica e refaz uma saída. Isso pode melhorar uma tarefa sem alterar seus parâmetros, os valores internos aprendidos no treino, nem seu processo de desenvolvimento. O segundo nível é melhorar o sistema: mudam as instruções, a memória, as ferramentas ou o código do agente, e as versões precisam ser comparadas com tarefas reservadas, preservando a possibilidade de voltar atrás. O terceiro é investigar a recursão: a melhoria passa a ajudar a produzir melhorias futuras. Esse mecanismo precisa de evidência, porque mais tentativas ou uma nota maior não demonstram crescimento ilimitado.',
     'Cada nível exige um tipo de controle diferente. Revisar uma resposta é barato e reversível; mudar o sistema pede registro de versões e testes; afirmar recursão pede evidência forte. Confundir os níveis leva a aceitar garantias que ninguém mediu.',
     'revisar a resposta; melhorar o sistema; investigar a recursão; parâmetros; tarefas reservadas; possibilidade de voltar atrás',
     'Uma equipe pede ao modelo que revise o próprio resumo antes de entregar: isso é nível 1. Depois reescreve a instrução do agente de atendimento e compara as duas versões em casos separados: nível 2. Nenhuma das duas coisas, sozinha, é uma IA criando IAs melhores.',
     'Classifique três melhorias que você já fez em prompts ou agentes nos três níveis da página e anote se alguma delas tinha caminho de volta.'),
   T('Da ideia a um teste verificável',
     'A página propõe começar com uma tarefa pequena: responder com base numa política, criar questões a partir de um texto ou extrair ações de notas. Primeiro defina a tarefa, a referência correta e os limites de dados, gasto e ações. Depois registre a versão inicial e separe casos de desenvolvimento de casos reservados para validação. Proponha uma mudança por vez e compare com os mesmos critérios, incluindo erros, custo e esforço de revisão. Por fim, valide antes de adotar: guarde resultados e versões, defina quem decide e mantenha um caminho de reversão.',
     'Uma avaliação conhecida pode ser explorada, e a página alerta para isso. Preservar a independência dos testes, conferir dados inventados e olhar resultados fora da amostra evita confundir ganho local com autonomia geral.',
     'tarefa pequena; referência correta; casos reservados; uma mudança por vez; mesmos critérios; validar antes de adotar; reversão',
     'Uma escola testa uma instrução que cria questões a partir de um texto. Usa quatro textos para ajustar e guarda dois que ninguém viu. A versão nova acerta mais nos quatro, mas erra num dos reservados; a coordenação decide manter a versão antiga até entender o erro.',
     'Escolha uma tarefa sua e escreva as quatro linhas: tarefa e referência; versão inicial e casos reservados; a única mudança; quem decide e como voltar.'),
   T('LOOP-R: o ciclo com freios',
     'LOOP-R é o framework do projeto para organizar melhorias: Executar, Medir, Criticar, Propor, Testar, Validar, Promover e Repetir. A página o descreve como pronto para usar no Claude Code, com nove assistentes de funções separadas, registro de cada versão, teto de custo e comando para reverter. A regra de segurança é explícita: nenhuma versão pior substitui a atual por decisão do sistema. No curso RSI, o LOOP-R aparece como uma proposta conceitual do projeto. Há também um curso LOOP-R com cinco trilhas e 21 aulas para donos e gestores sem base técnica.',
     'Um ciclo de melhoria sem freios pode trocar uma versão boa por uma pior sem ninguém perceber. Teto de custo, registro de versões e reversão tornam o ciclo auditável e seguro de repetir.',
     'Executar; Medir; Criticar; Propor; Testar; Validar; Promover; Repetir; nove assistentes; teto de custo; reverter',
     'Um gestor usa o ciclo para melhorar a instrução que classifica pedidos de clientes. Cada rodada gera uma versão registrada; quando a nova versão piora num teste, ela não é promovida e a atual continua valendo.',
     'Abra o guia do LOOP-R e anote em qual das oito etapas o seu processo atual de ajuste de prompts costuma parar.'),
   T('Por onde começar: curso e guia',
     'A seção "Comece por aqui" traz dois materiais. O curso RSI v6.2 tem 18 aulas em seis módulos, com exercícios, revisão e materiais para aplicar o LOOP-R e registrar conhecimento aprovado, em português, inglês e espanhol. O Guia RSI é um mapa do tema, com mecanismos, aplicações e limites, também em três idiomas. A página faz uma ressalva importante: o projeto reúne pesquisa e conteúdo educativo, e não é um sistema RSI autônomo pronto para executar. O código e os materiais ficam no repositório rsi no GitHub.',
     'Começar pelo guia dá o vocabulário e os limites; o curso transforma isso em prática com exercícios. Saber que o projeto é educativo evita esperar dele uma ferramenta que melhora sozinha.',
     'RSI v6.2; 18 aulas; seis módulos; Guia RSI; PT / EN / ES; conteúdo educativo, não sistema autônomo',
     'Uma consultora quer explicar RSI para uma diretoria. Usa o Guia RSI para montar o mapa dos três níveis e indica o curso RSI v6.2 para a pessoa do time que vai conduzir os testes de melhoria.',
     'Abra o Guia RSI, leia a parte de limites e anote uma frase que você usaria para responder a quem promete IA que se melhora sozinha.'),
   T('O acervo: Copiloto, Dream-RSI, 2028',
     'Além do guia e do curso, o acervo reúne três materiais com ressalvas claras. O RSI Copiloto é um assistente local com IA, memória, tarefas e rotinas, que compara instruções, pede revisão humana e permite reverter mudanças; a demonstração pública usa exemplos programados, sem IA, e a IA real fica só na versão local. O Dream-RSI é um guia educativo independente, não afiliado ao Google, sobre aprender com históricos de experimentos; o laboratório e os oito encontros são planos futuros, não uma implementação do artigo. O Alerta IA 2028 é um curso em três trilhas, sobre o ciclo de melhoria, as evidências e os limites da avaliação, e trata os cenários de 2028 como hipóteses, sem calendário garantido. A página ainda lista referências como Self-Refine, Reflexion, Darwin Gödel Machine e AlphaEvolve, consultadas em 25 de setembro de 2026, cujos resultados não foram reproduzidos no projeto.',
     'Cada material diz o que já está disponível e o que ainda é plano. Ler essas ressalvas é o próprio exercício da área: separar evidência de promessa.',
     'RSI Copiloto; demonstração sem IA; Dream-RSI independente; Alerta IA 2028; cenários como hipóteses; referências originais em inglês',
     'Um analista experimenta a demonstração do Copiloto e percebe que as respostas são programadas. Em vez de concluir que "a IA acertou tudo", registra que precisa da versão local para testar de verdade.',
     'Escolha um dos três materiais e escreva o que ele já entrega e o que a página diz que ainda é plano ou exemplo programado.')],
  ('Prompt: meu primeiro teste de melhoria (RSI)',
   'Leia https://eventos.inema.pro/rsi/ e o guia https://inematds.github.io/rsi/guia/.\n'
   'Quero testar uma melhoria numa tarefa do meu trabalho, sem prometer mais do que consigo medir.\n'
   'Minha tarefa: <descreva a tarefa, ex.: extrair ações de notas de reunião>.\n'
   'Minha instrução atual: <cole a instrução ou prompt que você usa hoje>.\n'
   '1. Diga em qual dos três níveis (revisar a resposta, melhorar o sistema, investigar a recursão) a minha ideia se encaixa.\n'
   '2. Monte o teste: referência correta, limites de dados/gasto/ações, casos de desenvolvimento e casos reservados.\n'
   '3. Proponha UMA única mudança na instrução e a tabela para comparar as duas versões (erros, custo, esforço de revisão).\n'
   '4. Diga quem deve decidir a adoção e como voltar à versão anterior.\n'
   'Não invente resultados: deixe os campos de resultado em branco para eu preencher.'),
  [('Área RSI · eventos.inema.pro','https://eventos.inema.pro/rsi/'),
   ('Curso RSI v6.2','https://inematds.github.io/curso-rsi/'),
   ('Guia RSI','https://inematds.github.io/rsi/guia/'),
   ('Framework LOOP-R','https://inematds.github.io/loop-r/guia/')],
  'rsi')

FIGURES[(0,2)] = dict(kind='timeline',
  caption='Os três níveis sobem em ambição e em exigência de prova: revisar uma resposta não altera o sistema, e só o terceiro nível fala em melhorias que geram melhorias.',
  items=[('Revisar','nível 1'),('Sistema','nível 2'),('Recursão','nível 3')])
FIGURES[(0,3)] = dict(kind='flow',
  caption='Um teste verificável separa ajuste de validação: a mudança só é adotada depois de passar nos casos reservados, com reversão possível.',
  items=['Definir tarefa','Versão inicial','Uma mudança','Mesmos critérios','Validar e decidir'])
FIGURES[(0,4)] = dict(kind='grid',
  caption='As oito etapas do LOOP-R repetem o ciclo, mas Validar e Promover funcionam como portões: versão pior não substitui a atual.',
  items=['Executar','Medir','Criticar','Propor','Testar','Validar','Promover','Repetir'])
FIGURES[(0,6)] = dict(kind='columns',
  caption='Cada material do acervo traz sua ressalva: leia o subtítulo antes de tirar conclusões sobre o que ele entrega.',
  items=[('RSI Copiloto','demo sem IA'),('Dream-RSI','independente'),('Alerta IA 2028','cenários = hipóteses'),('LOOP-R','versão pior não entra')])

# ---------------------------------------------------------------- 1 · JEV
M('JEV: decisões de IA na prática',
  'Explicar o que é uma decisão estruturada com Jev, escolher entre Choice, Noul e Score e separar o que já foi observado do que ainda falta medir.',
  'Sua decisão estruturada, do caso ao piloto',
  ['Abra o laboratório público do JEV, escolha um dos 20 casos e anote contexto, pergunta, critérios e a resposta simulada.',
   'Escreva uma decisão parecida do seu trabalho e indique se ela é Choice, Noul ou Score, justificando pelo tipo de resposta de que você precisa.',
   'Defina a política: com que confiança a sugestão segue, quando o sistema se abstém e quando vai para revisão humana.',
   'Confira sua ficha contra a seção "O que já foi observado e o que falta medir": marque o que você conseguiria medir com dados próprios e referência humana.'],
  'O laboratório público mostrou respostas corretas em todos os casos que você abriu. Isso mede a qualidade do Jev?',
  'Não. Os 20 casos públicos e o replay são autorais e simulados; servem para estudar formulação, políticas e erros. Qualidade em português e calibração ainda precisam de dados independentes e referência humana.',
  [T('O que é o JEV',
     'Jev é o modelo de decisões estruturadas da TypeSafe. Uma decisão estruturada é uma pergunta fechada, com contexto e critérios, cuja resposta é uma escolha, uma probabilidade ou um nível, e não um texto livre. O Jev Decision Lab é o projeto educacional do INEMA para formular perguntas, comparar respostas e entender quando uma decisão precisa de revisão. O modelo recebe contexto e critérios; o seu sistema continua responsável pelas ações. O laboratório separa essa escolha da geração de texto e da execução de ferramentas.',
     'Muitas tarefas de IA no trabalho não pedem um texto, pedem uma decisão: para qual fila vai este chamado, este trecho sustenta a afirmação. Separar decidir, gerar e executar deixa claro quem responde por cada parte e facilita medir o acerto.',
     'modelo de decisões estruturadas; TypeSafe; Jev Decision Lab; contexto e critérios; o sistema responde pelas ações',
     'Uma equipe de suporte quer que a IA encaminhe chamados. Em vez de pedir um parágrafo, ela usa o Jev para escolher a fila entre opções fixas; o sistema da empresa é quem move o chamado, e casos duvidosos vão para uma pessoa.',
     'Liste duas decisões repetitivas do seu trabalho que hoje viram texto livre e reescreva cada uma como pergunta fechada com opções.'),
   T('Choice, Noul e Score',
     'A página apresenta três formas de perguntar. Choice escolhe entre alternativas explícitas, como qual fila ou qual agente. Noul estima a probabilidade de uma resposta afirmativa, como a chance de um trecho apoiar uma afirmação. Score avalia uma rubrica com níveis ordenados, como baixo, médio e alto. O curso dedica um módulo a distinguir as três a partir do tipo de resposta necessário, e outro a confiança e erro: usar incerteza sem transformá-la em autorização automática.',
     'Escolher a forma errada produz respostas difíceis de usar: uma nota quando você precisava de uma fila, ou um sim quando havia vários níveis. A forma da pergunta define como você vai medir e qual política aplicar.',
     'Choice: alternativas explícitas; Noul: probabilidade de sim; Score: níveis ordenados; confiança não é autorização',
     'Na triagem de reuniões, "a ata tem responsável e prazo?" é Noul; "qual equipe cuida disto?" é Choice; "qual a prioridade do log, de 1 a 4?" é Score. A mesma reunião pode gerar as três perguntas.',
     'Pegue uma das decisões que você listou e escreva-a nas três formas; fique com a que devolve a resposta que o seu processo consegue usar.'),
   T('20 casos no laboratório público',
     'O laboratório abre no navegador, não pede chave e não consulta nenhuma API: as respostas são simuladas. Cada um dos 20 casos inclui contexto, perguntas, critérios, resposta simulada, explicação e próximo passo, como triagem de atendimento, checklist de contratos, roteamento de agentes e revisão semântica de diff. Você pode editar as perguntas, importar uma requisição, exportar o resultado ou abrir um relatório; alterar um caso invalida sua resposta simulada anterior. Para ir além, é possível clonar o projeto e rodar o servidor local com Python 3.10 ou superior. O núcleo usa só a biblioteca padrão.',
     'O laboratório permite errar sem custo e sem risco: você aprende a formular o contexto, as opções e a política antes de gastar crédito ou tocar num sistema real.',
     'laboratório sem chave; respostas simuladas; 20 casos; contexto, perguntas, critérios; servidor local em Python',
     'Um coordenador abre o caso "Intenções simultâneas" e vê que uma conversa pode conter vendas e agendamento ao mesmo tempo. Ele percebe que a pergunta da sua empresa, com uma única opção por mensagem, precisa mudar.',
     'Abra https://inematds.github.io/jev/app/, escolha o caso mais próximo do seu trabalho e reescreva uma das perguntas dele com os seus critérios.'),
   T('O curso: 3 trilhas, 36 aulas',
     'O curso "Jev na prática" tem três trilhas, 12 módulos e 36 aulas com teoria, exemplos, exercícios e respostas. A trilha Entender cobre onde o Jev entra, os três tipos de pergunta, confiança e erro, e custo; Aplicar trata atendimento, documentos, modelos e agentes, e navegador; Construir e avaliar cobre integração, medição de qualidade, operação e o projeto final. Os módulos 1 a 8 são conceituais; os módulos 9 a 12 usam JSON, terminal e Python, e a estimativa é de 18 horas. São 12 laboratórios com dados fictícios e gabaritos, e o projeto final pede concluir se há evidência para adotar, coletar mais dados ou não automatizar. O curso HTML v2 está em português, com progresso, dúvidas e anotações.',
     'O curso leva de "entender a ideia" a "decidir a adoção" com rubrica. O projeto final aceita a resposta "não automatizar", o que treina julgamento em vez de entusiasmo.',
     'Entender; Aplicar; Construir e avaliar; 12 módulos; 36 aulas; 12 laboratórios; projeto final; 18 horas',
     'Uma analista sem programação faz os módulos 1 a 8 e resolve os laboratórios de atendimento e evidências. O colega que programa segue para os módulos 9 a 12 e monta a requisição real.',
     'Abra o curso em https://inematds.github.io/jev-curso/ e escolha o módulo que corresponde à decisão que você listou.'),
   T('17 pacotes e caminhos de uso',
     'Um pacote é um kit por área com contexto, critérios, requisição, fixture (um exemplo pronto para teste) e instruções. O acervo atual reúne 17, de atendimento e vendas a comentários do YouTube, reuniões, cortes e curadoria. Todos compartilham o executor e o núcleo Python: sem a opção --live o pacote usa a fixture simulada; com ela, faz uma consulta real, que requer chave no backend e pode consumir créditos. Há também execução em lotes com retomada, a skill jev-decidir para Codex e Claude Code e o jev-gw, um gateway com teto de gasto diário, cache, registro de custo e falha conservadora que devolve revisão humana. Os pacotes estão no repositório; ainda não há distribuição PyPI, instalador universal ou conector pronto para n8n.',
     'O caminho é gradual: começar offline, entender a saída e só depois pagar por consultas reais. O gateway mostra como proteger quem chama o Jev quando algo falha.',
     'pacote por área; fixture; --live; lotes e retomada; skill jev-decidir; jev-gw; falha conservadora',
     'Uma equipe de conteúdo usa o pacote de comentários do YouTube primeiro com a fixture. Quando a saída faz sentido, configura a consulta real no servidor e coloca o jev-gw na frente, para que um teto estourado mande o caso para revisão em vez de quebrar o sistema.',
     'Escolha, entre os 17 pacotes da página, o que mais se parece com o seu trabalho e anote em que ponto do seu processo ele entraria.'),
   T('O que foi observado e o que falta',
     'A página separa quatro situações. Simulação para aprender: os 20 casos e o replay são autorais e simulados, não medem a qualidade do modelo. Baseline de regras: 20 acertos em 24 tickets fictícios (83,33%), resultado das regras, não do Jev. Integração real testada: em 19/09/2026 os dez pacotes originais receberam respostas pelo OpenRouter com as classificações esperadas nos exemplos fictícios, o que confirma integração, não benchmark; os sete pacotes novos só têm testes controlados. Avaliação ainda necessária: qualidade em português, calibração e uso operacional pedem dados independentes e referência humana. O Laya, alternativa local em avaliação, teve 14 testes da aplicação aprovados e 13 acertos em 16 exemplos sintéticos, o que não comprova superioridade.',
     'Essa separação é o que torna a área confiável: cada número vem com o que ele prova e o que não prova. Repetir esses números fora de contexto seria inflar o resultado.',
     'simulação; baseline de regras; integração real; avaliação necessária; Laya em avaliação; não é benchmark',
     'Um gestor lê "dez consultas reais sem falhas" e quase aprova a adoção. Ao ler a seção inteira, vê que o teste confirma que a integração funciona, não que o Jev acerta com os dados da empresa, e pede um piloto com referência humana.',
     'Para a sua decisão, escreva uma linha em cada coluna: o que você já observou e o que falta medir antes de automatizar.')],
  ('Prompt: minha decisão estruturada com JEV',
   'Leia https://eventos.inema.pro/jev/ e o guia https://inematds.github.io/jev/guia/.\n'
   'Quero transformar uma decisão repetitiva do meu trabalho numa decisão estruturada, sem prometer qualidade que eu não medi.\n'
   'Minha decisão: <descreva, ex.: para qual equipe vai cada e-mail de cliente>.\n'
   'Opções ou níveis possíveis: <liste>.\n'
   '1. Diga se a pergunta é Choice, Noul ou Score e por quê.\n'
   '2. Escreva o contexto mínimo, os critérios e a pergunta.\n'
   '3. Proponha a política: quando seguir a sugestão, quando se abster e quando mandar para revisão humana.\n'
   '4. Indique qual dos 20 casos do laboratório e qual dos 17 pacotes da página mais se parecem com a minha decisão.\n'
   '5. Monte a lista "já observado x falta medir" para o meu caso. Não trate simulação como medida de qualidade.'),
  [('Área JEV · eventos.inema.pro','https://eventos.inema.pro/jev/'),
   ('Laboratório JEV','https://inematds.github.io/jev/app/'),
   ('Curso JEV','https://inematds.github.io/jev-curso/'),
   ('Guia do jev-gw','https://inematds.github.io/jev-gw/guia/')],
  'jev')

FIGURES[(1,2)] = dict(kind='columns',
  caption='A forma da pergunta vem do tipo de resposta que o seu processo precisa usar: uma opção, uma chance de sim ou um nível.',
  items=[('Choice','uma alternativa'),('Noul','probabilidade de sim'),('Score','níveis ordenados')])
FIGURES[(1,4)] = dict(kind='timeline',
  caption='As três trilhas vão do conceito ao projeto final; os módulos 9 a 12 são os únicos que pedem JSON, terminal e Python.',
  items=[('Entender','módulos 1-4'),('Aplicar','módulos 5-8'),('Construir','módulos 9-12'),('Projeto final','adotar ou não')])
FIGURES[(1,5)] = dict(kind='flow',
  caption='Comece simples e avance quando precisar: a consulta real só entra depois do teste offline, e o gateway protege quem chama.',
  items=['Navegador','Servidor local','Pacote offline','Consulta --live','Lotes','jev-gw'])
FIGURES[(1,6)] = dict(kind='columns',
  caption='Cada evidência tem um alcance: só a última coluna mediria qualidade real, e ela ainda está por fazer.',
  items=[('Simulação','para aprender'),('Baseline','regras, não Jev'),('Integração','funciona, não mede'),('Avaliação','ainda necessária')])

# ---------------------------------------------------------------- 2 · WebMCP
M('WebMCP: seu site conversando com agentes',
  'Explicar o que muda quando agentes visitam sites, o que é WebMCP e qual é o primeiro passo concreto: diagnosticar o próprio site e corrigir o básico.',
  'O diagnóstico do seu site',
  ['Rode o WebMCP Readiness em webmcp.inema.pro com a URL do seu site e anote a nota geral e as quatro notas (WebMCP, SEO, GEO, AEO).',
   'Liste os bloqueadores que aparecem primeiro no plano de correção e confira se robots.txt, sitemap.xml e llms.txt existem no seu domínio.',
   'Corrija um item das seis dicas da página, como title, description ou JSON-LD, sem mexer em nada perigoso.',
   'Rode o scan de novo e compare as notas com a linha de base; registre o que subiu e o que ainda depende de revisão humana.'],
  'O scanner encontrou uma ferramenta declarada num script do seu site. Isso garante que ela está protegida e funciona para todo visitante?',
  'Não. O scanner prova o que é observável; autorização real no backend, idempotência, correspondência entre descrição e efeito e se a definição está registrada para todo visitante exigem revisão humana.',
  [T('O que é WebMCP',
     'WebMCP é uma forma de a própria página descrever o que sabe fazer para agentes de IA. Sem WebMCP, o agente precisa localizar campos, clicar, digitar e interpretar a tela, e isso quebra quando o layout muda. Com WebMCP, a página expõe ferramentas com nome, descrição, schema de argumentos e resposta, e o agente chama a ferramenta certa pelo nome. Há dois caminhos: a ferramenta declarativa, em que um formulário que já existe ganha um toolname e uma descrição, e a imperativa, em que JavaScript registra capacidades com JSON Schema, tratando estado, erros, cancelamento e fallback. É uma tecnologia experimental, hoje atrás de Origin Trial no navegador, ou seja, liberada em caráter de teste.',
     'É a diferença entre o agente adivinhar e o site dizer. O site passa a decidir o que é permitido, o que precisa de confirmação e o que pode ser cancelado.',
     'operar pixels x conversar com capacidades; ferramenta declarativa; ferramenta imperativa; JSON Schema; Origin Trial',
     'Sem WebMCP, o agente digita o nome do curso, clica no botão azul e "acha que deu certo". Com WebMCP, o site expõe verificar_vagas e iniciar_inscricao; o agente chama a primeira, confirma que há vaga, e a segunda exige confirmação humana antes de concluir.',
     'Escolha um formulário do seu site e escreva o nome e a descrição de uma linha que ele teria como ferramenta.'),
   T('O próximo visitante é um agente',
     'A página lista seis mudanças. Do lado de quem visita: agentes já operam o navegador, preenchendo formulários e concluindo tarefas; buscar virou perguntar a um assistente, o que cria o problema de GEO e AEO; e o padrão está nascendo agora. Do lado de quem publica: o site deixa de ser só uma tela e ganha um catálogo de capacidades por cima da jornada humana; descoberta vira requisito, com robots.txt, sitemap.xml, llms.txt, JSON-LD, Open Graph e uma identidade clara; e a segurança fica com o site, não com o modelo. GEO e AEO são as práticas de aparecer e ser citado nas respostas de assistentes de IA, e não só em buscadores.',
     'Se você é dono do site, as três últimas mudanças são a sua lista de trabalho. Quem entende as limitações cedo aprende com custo baixo.',
     'agentes no navegador; buscar virou perguntar; GEO e AEO; catálogo de capacidades; descoberta; segurança no site',
     'Uma escola percebe que alunos perguntam a um assistente "qual curso de agentes começa este mês" em vez de buscar no site. A resposta depende do que o modelo consegue extrair das páginas dela, e o SEO clássico sozinho não resolve.',
     'Escreva quais das três mudanças do lado de quem publica o seu site ainda não atende.'),
   T('Diagnóstico gratuito: Readiness',
     'O WebMCP Readiness, em webmcp.inema.pro, abre a URL num navegador descartável, reúne sinais observáveis e transforma o scan num plano de correção. É um scanner passivo: consulta robots.txt, sitemap.xml e llms.txt e não executa nenhuma ferramenta do site. Você recebe nota geral e quatro notas independentes, WebMCP, SEO, GEO e AEO, com evidências, alertas, bloqueadores, até 12 correções priorizadas e os cursos indicados para cada lacuna, num relatório em JSON. O scan aprofunda só a URL informada; o sitemap é inventariado, mas suas páginas não são rastreadas. Os scanners avançados por fase aparecem no relatório como planejados, não como prontos.',
     'Começar pelo diagnóstico mostra onde o seu site está antes de estudar. E a página deixa claro o limite: indexação, ranking ou citação por IA, o scanner não promete nada disso.',
     'scanner passivo; navegador descartável; nota geral + quatro notas; até 12 correções; relatório JSON; o que exige revisão humana',
     'Uma agência roda o scan na página de contato de um cliente e recebe o bloqueador "sem llms.txt" no topo do plano. Ela corrige, roda de novo e usa as duas notas para mostrar o avanço, sem prometer ranking.',
     'Rode o scan em https://webmcp.inema.pro/ com a página principal do seu site e salve o relatório JSON como linha de base.'),
   T('Oito camadas de um site pronto',
     'A página organiza a arquitetura em oito camadas, na ordem em que a formação constrói. As quatro primeiras são o site se descrevendo: descoberta (o agente acha o site?), ferramentas (o que o site sabe fazer?), contrato (como se chama e o que volta?) e estado e erros (e quando dá errado?). As quatro últimas são o site se protegendo: controle (quem confirma?), permissões (quem pode chamar?), backend e MCP (onde mora a verdade?) e evals e observabilidade (está funcionando mesmo?). A regra que atravessa todas: a LLM escolhe a ferramenta; o site decide se ela pode rodar. O diagnóstico já mede a camada 1 inteira e os sinais observáveis das camadas 2 e 5.',
     'As camadas mostram que expor uma ferramenta é só o começo. Sem confirmação, permissões e autorização no backend, um agente pode acionar algo que não deveria.',
     'descoberta; ferramentas; contrato; estado e erros; controle; permissões; backend e MCP; evals',
     'Uma loja expõe a ferramenta de consulta de pedido. A descrição diz "só consulta", o backend confere se quem chama pode ver aquele pedido, e qualquer alteração exige confirmação humana. Logs mostram depois se a ferramenta fez o que dizia.',
     'Marque, para o seu site, quais das oito camadas você já cobre e qual pergunta de camada você não saberia responder hoje.'),
   T('Seis correções para esta semana',
     'Antes de qualquer fase da formação, a página traz seis correções que o dono do site faz, cada uma ligada a um item que o scanner verifica. Primeiro, rode o scan e anote as notas como linha de base. Segundo, publique os três arquivos públicos: robots.txt, sitemap.xml atualizado e um llms.txt que apresenta o site para modelos de IA. Terceiro, arrume o básico de SEO que o agente também lê: title, description, canonical, headings em ordem, alt nas imagens, Open Graph e JSON-LD. Quarto, escreva para quem responde perguntas, com respostas diretas, definições, listas e tabelas; quinto, mostre quem está por trás, com entidade, autoria, data de atualização e evidências. Sexto, escolha como primeira ferramenta um formulário que não muda nada perigoso, como uma busca ou consulta de status.',
     'São correções que não exigem programar ferramentas e já sobem as notas. A página resume o método: corrija, rode de novo, veja a nota subir.',
     'linha de base; robots.txt, sitemap.xml, llms.txt; SEO básico; AEO: respostas diretas; GEO: autoria e evidências; primeira ferramenta segura',
     'Um consultor autônomo publica o llms.txt, acrescenta data de atualização e autoria nos artigos e cria uma seção de perguntas frequentes com respostas curtas. Na semana seguinte, as notas de GEO e AEO do scan sobem, sem nenhuma linha de JavaScript nova.',
     'Faça hoje a dica 2: confira se seu domínio responde em /robots.txt, /sitemap.xml e /llms.txt e anote o que falta.'),
   T('A formação e onde continuar',
     'A Formação WebMCP tem uma visão geral e quatro fases, todas abertas e em português: Builder (construir), Integrator (integrar), Agent Developer (orquestrar) e Expert (operar). Cada fase tem quatro módulos de seis tópicos e usa JavaScript; quem não programa começa pela visão geral e pelo diagnóstico e leva as fases para o time. As camadas 1 e 2 são ensinadas no Builder, 3 e 4 no Integrator, 5 e 6 no Agent Developer, e 7 e 8 no Expert. Ao lado, a página indica o AIV 2026 para AEO e GEO, o curso de Computer Use com o GPT-6 Astra e o Super-Agentes, além de projetos como o Kit do Arquiteto de Agentes, o INEMACCBOT e o os-agentes. O convite final é direto: o melhor primeiro módulo é o seu próprio site.',
     'Saber em qual fase cada camada é ensinada permite entrar na formação pelo ponto do seu papel, em vez de começar tudo do zero.',
     'visão geral; Builder; Integrator; Agent Developer; Expert; quatro módulos de seis tópicos; cursos ao lado',
     'Uma dona de loja virtual faz o diagnóstico e a visão geral. O desenvolvedor da equipe começa pelo Builder para transformar a busca de produtos em ferramenta declarativa, e a parte de permissões fica para quando ele chegar ao Agent Developer.',
     'Abra a visão geral em https://inematds.github.io/webmcp-1-formacao/ e escolha a fase que corresponde ao seu papel.')],
  ('Prompt: plano WebMCP para o meu site',
   'Leia https://eventos.inema.pro/webmcp/.\n'
   'Rodei o diagnóstico em https://webmcp.inema.pro/ para o meu site: <URL do seu site>.\n'
   'Resultado do scan (cole o JSON ou as notas e bloqueadores): <cole aqui>.\n'
   '1. Explique cada bloqueador em linguagem simples e diga a qual das oito camadas ele pertence.\n'
   '2. Monte a lista desta semana usando as seis correções da página, na ordem certa para o meu caso.\n'
   '3. Sugira UMA primeira ferramenta declarativa a partir de um formulário meu que não muda nada perigoso: nome, descrição e argumentos.\n'
   '4. Separe o que o scanner consegue provar do que exige revisão humana (autorização no backend, idempotência, descrição x efeito real).\n'
   '5. Indique a fase da Formação WebMCP por onde eu ou meu time devemos começar.\n'
   'Não prometa ranking, indexação ou citação por IA.'),
  [('Área WebMCP · eventos.inema.pro','https://eventos.inema.pro/webmcp/'),
   ('WebMCP Readiness','https://webmcp.inema.pro/'),
   ('Formação WebMCP','https://inematds.github.io/webmcp-1-formacao/'),
   ('WebMCP Builder','https://inematds.github.io/webmcp-2-builder/')],
  'webmcp')

FIGURES[(2,2)] = dict(kind='grid',
  caption='As três primeiras mudanças acontecem com quem visita; as três últimas são a lista de trabalho de quem publica o site.',
  items=['Agente navega','Perguntar','Padrão novo','Catálogo','Descoberta','Segurança site'])
FIGURES[(2,3)] = dict(kind='columns',
  caption='O Readiness devolve quatro notas independentes: WebMCP mede ferramentas; SEO, GEO e AEO medem se o site é achado e citado.',
  items=[('WebMCP','ferramentas e schemas'),('SEO','title, canonical'),('GEO','entidade e autoria'),('AEO','respostas diretas')])
FIGURES[(2,4)] = dict(kind='stack',
  caption='As quatro camadas de baixo descrevem o site; as quatro de cima o protegem. Expor ferramenta sem as de cima é experimento, não operação.',
  items=[('Descoberta','o agente acha?'),('Ferramentas','o que faz?'),('Contrato','o que volta?'),('Estado e erros','e se falhar?'),('Controle e permissões','quem confirma e chama?'),('Backend, MCP, evals','onde mora a verdade?')])
FIGURES[(2,6)] = dict(kind='timeline',
  caption='A formação sobe do diagnóstico à produção: cada fase ensina duas das oito camadas.',
  items=[('Visão geral','comece aqui'),('Builder','camadas 1-2'),('Integrator','camadas 3-4'),('Agent Dev.','camadas 5-6'),('Expert','camadas 7-8')])
