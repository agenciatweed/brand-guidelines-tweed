# Agência Tweed · gera o HTML do Manual de Identidade Visual v2.0 (A4 paisagem)
# Uso: python3 manual.py [saida.html]   (o HTML referencia ../tipografia e ../componentes)
import os, re, sys
from pal import C, H, SEM, PAIRS, TYPE, cr, fmt, rgb, cmyk, L

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'fonte-editavel', 'Manual_de_Identidade_Visual_Tweed.html')
D = re.search(r'<path class="st1" d="([^"]+)"', open(os.path.join(ROOT, 'logos', 'logo_tweed_teal.svg')).read()).group(1)
VB = '0 0 651.97 204.02'
RATIO = 651.97 / 204.02
VERSION = 'Versão 2.0 · Novembro 2026'
R = '..'  # raiz do repositório, relativa ao HTML

def logo(h, ink=None, extra=''):
    ink = ink or H['teal']
    return f'<svg class="lg" viewBox="{VB}" height="{h}" width="{h * RATIO:.1f}" role="img" aria-label="Agência Tweed" {extra}><path fill="{ink}" d="{D}"/></svg>'

ICON = {
    'seta': '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    'seta-esq': '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>',
    'tela': '<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 22h8M12 18v4M7 9h6M7 13h4"/>',
    'alvo': '<path d="M12 3v18M3 12h18"/><circle cx="12" cy="12" r="9"/>',
    'canais': '<path d="M4 6h16M4 12h10M4 18h6"/><path d="M17 15l3 3-3 3"/>',
    'check': '<path d="m5 12 5 5 9-10"/>',
    'x': '<path d="M6 6l12 12M18 6 6 18"/>',
    'alerta': '<circle cx="12" cy="12" r="9"/><path d="M12 7.5v5.5M12 16.2v.3"/>',
    'mais': '<path d="M12 5v14M5 12h14"/>',
}
def icon(n, s=22, sw=1.75, c='currentColor'):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[n]}</svg>'

SECTION_ICONS = {k: open(os.path.join(ROOT, 'componentes', f'{k}.svg')).read() for k in ('lowest-price', 'overload', 'handoff', 'formula')}
def sicon(k, s=44, c=H['teal']):
    t = SECTION_ICONS[k]
    t = re.sub(r'<\?xml[^>]*>', '', t)
    t = re.sub(r'<svg', f'<svg width="{s}" height="{s}" fill="{c}"', t, count=1)
    t = re.sub(r'\s(width|height)="512"', '', t)
    return t

def tag(t):
    cls = {'Original': 'o', 'Site': 's', 'Proposta': 'p'}[t]
    return f'<span class="tag tag-{cls}">{t}</span>'

def ok(t='Correto'):
    return f'<span class="mk mk-ok">{icon("check", 11, 2.4)}{t}</span>'
def no(t='Incorreto'):
    return f'<span class="mk mk-no">{icon("x", 11, 2.4)}{t}</span>'

pages = []
def page(chapter, body, theme='dark', cls=''):
    pages.append((chapter, body, theme, cls))

def head(eb, title, lede=None):
    return f'<p class="eb">{eb}</p><h2>{title}</h2>' + (f'<p class="lede">{lede}</p>' if lede else '')

def sw(k, big=False):
    n, h, orig, g, u = C[k]
    r, gg, b = rgb(h)
    ink = H['branco'] if L(h) < 0.2 else H['azul-escuro']
    edge = ' edge' if L(h) > 0.8 else ''
    return (f'<div class="sw{" big" if big else ""}"><div class="chip{edge}" style="background:{h};color:{ink}"><b>{n}</b>{tag(orig)}</div>'
            f'<div class="swm"><span class="mono">{h.upper()}</span><span>RGB {r} · {gg} · {b}</span><span>CMYK ind. {cmyk(h)}</span><p>{u}</p></div></div>')

# =============================================================== 01 FUNDAMENTOS
page('', f'''
<div class="grid-lines"></div><div class="glow gl1"></div><div class="glow gl2"></div>
<div class="cover">
  <div class="cover-top">{logo(64)}</div>
  <div class="cover-txt">
    <p class="eb">Agência Tweed · Porto Alegre · desde 2017</p>
    <h1>Manual de<br>Identidade <em>Visual</em></h1>
    <p class="lede">Logotipo, cores, tipografia, linguagem visual, tom de voz e aplicações, em tema escuro e tema claro.</p>
    <p class="cap">{VERSION}</p>
  </div>
</div>''', 'dark', 'p-cover')

page('01 Fundamentos', f'''
<div class="chapter-mark">01</div>
<div class="g2 top">
  <div>
    {head('Apresentação', 'Para que serve<br>este manual')}
    <p class="body">Este manual reúne as regras que fazem a Tweed ser reconhecida do mesmo jeito em qualquer lugar: no site, numa proposta comercial, num slide, num post, numa assinatura de e-mail.</p>
    <p class="body">A versão 1.0 definia três cores, uma família tipográfica, dois logotipos e o tom de voz. Esta edição mantém tudo isso e acrescenta o que faltava para aplicar a marca com segurança: medidas, escala tipográfica, superfícies, componentes, contraste e um <b>tema claro</b> completo.</p>
  </div>
  <div>
    <p class="eb">De onde vem cada regra</p>
    <div class="origins">
      <div>{tag('Original')}<p>Herdado do guia de marca v1.0: Teal Tweed, Azul-Escuro, Branco, Inter, os dois logotipos, ícones de seção, fotos e tom de voz.</p></div>
      <div>{tag('Site')}<p>Medido no CSS de produção do agenciatweed.com.br: tons de apoio do escuro, escala de tipo, espaçamentos, raios, botões, cards e movimento.</p></div>
      <div>{tag('Proposta')}<p>Criado nesta edição: o tema claro, o logotipo branco, o avatar, a área de proteção e os tamanhos mínimos. Vale como recomendação até a aprovação.</p></div>
    </div>
    <p class="cap">Quem usa: equipe da Tweed, fornecedores, parceiros de tráfego, desenvolvedores do site e qualquer pessoa que produza material com a marca.</p>
  </div>
</div>''')

page('01 Fundamentos', f'''
<div class="g2 top">
  <div>
    {head('A crença central', 'Marcas não crescem por barulho. Crescem por <em>clareza</em>, <em>consistência</em> e <em>confiança</em>.')}
    <p class="body">A frase não é slogan: é premissa de trabalho. O sistema visual obedece à mesma regra. Poucas cores, uma família tipográfica, muito espaço negativo e o teal guardado para o que precisa ser visto.</p>
  </div>
  <div class="words">
    <div><span class="num">01</span><h4>Clareza</h4><p>Cada peça diz uma coisa só, e diz bem. Hierarquia por escala e peso, nunca por enfeite.</p></div>
    <div><span class="num">02</span><h4>Consistência</h4><p>O mesmo azul-escuro, o mesmo teal, a mesma Inter em todo lugar. Variação só dentro das regras deste manual.</p></div>
    <div><span class="num">03</span><h4>Confiança</h4><p>Acabamento de designer: alinhamento, respiro, contraste verificado. O cuidado é visível antes de qualquer palavra.</p></div>
  </div>
</div>
<p class="sign">Somos pequenos por escolha. Próximos por método. Completos por visão.</p>''')

TOC = [('01', 'Fundamentos', 'Apresentação, crença, sumário, os dois temas', '02'),
       ('02', 'Logotipo', 'Assinatura, versões, proteção, fundos, usos incorretos, avatar', '06'),
       ('03', 'Cores', 'Institucionais, sistema escuro, sistema claro, tokens, contraste, proporção', '12'),
       ('04', 'Tipografia', 'Inter em três cortes, hierarquia digital, apresentações e documentos', '18'),
       ('05', 'Linguagem visual', 'Grid, componentes, superfícies, ícones, imagem, movimento', '21'),
       ('06', 'Tom de voz', 'Personalidade, atributos, palavras, teste do espelho', '27'),
       ('07', 'Aplicações', 'Site, proposta, slides, redes sociais, checklist', '28')]
page('01 Fundamentos', f'''
{head('Sumário', 'Sete capítulos')}
<div class="toc">''' + ''.join(f'<div><span class="n">{n}</span><div><h4>{t}</h4><p>{d}</p></div><span class="pg">{p}</span></div>' for n, t, d, p in TOC) + '</div>')

def mini(theme):
    lt = theme == 'claro'
    ink = H['azul-escuro'] if lt else H['branco']
    return f'''<div class="mini {'mini-l' if lt else 'mini-d'}">
  <div class="mini-nav">{logo(18, H['azul-escuro'] if lt else H['teal'])}<span class="btnp sm">Falar com a Tweed</span></div>
  <p class="eb">Capítulo 01 · O diagnóstico</p>
  <h3 class="mini-h">O problema quase nunca é o <em>marketing</em>.</h3>
  <p class="mini-p">É a distância entre o que a empresa é e a forma como o mercado percebe ela.</p>
  <div class="mini-row"><span class="btnp">Começar uma conversa {icon('seta', 16)}</span><span class="btng">Ver como trabalhamos</span></div>
  <div class="mini-cards"><div class="ct"><span class="ic">{icon('tela', 18)}</span><b>O site parece antigo.</b></div><div class="ct"><span class="ic">{icon('alvo', 18)}</span><b>A identidade não sustenta o preço.</b></div></div>
</div>'''
page('01 Fundamentos', f'''
{head('Visão geral', 'Um sistema, dois temas', 'O escuro é a casa da marca: site, apresentações, redes. O claro existe para documentos, propostas impressas, e-mail e qualquer superfície onde o fundo branco é o padrão. As peças são as mesmas; só os papéis das cores se invertem.')}
<div class="g2 mt">
  <div>{mini('escuro')}<p class="cap"><b>Escuro (padrão)</b> · Azul-Escuro no fundo, Branco no texto, Teal Tweed no acento.</p></div>
  <div class="th-l">{mini('claro')}<p class="cap"><b>Claro</b> {tag('Proposta')} · Branco no fundo, Azul-Escuro no texto, Teal Tinta no acento de texto e Teal Tweed só em superfícies.</p></div>
</div>''')

# =============================================================== 02 LOGOTIPO
page('02 Logotipo', f'''
<div class="chapter-mark">02</div>
<div class="g2 top">
  <div>
    {head('Assinatura', 'Uma palavra escrita à mão')}
    <p class="body">O logotipo é a palavra <b>tweed</b> em lettering cursivo monolinha: um traço contínuo, de espessura constante, com o corte do t estendido sobre a palavra inteira. Ele carrega o lado humano e autoral da agência, e por isso não convive com outros grafismos de traço livre.</p>
    <ul class="list">
      <li>Proporção <b>3,20 : 1</b> (651,97 × 204,02 no vetor original).</li>
      <li>Uma configuração só, sem símbolo separado e sem descritor obrigatório.</li>
      <li>Use sempre os arquivos da pasta <span class="mono">logos/</span>. Nunca redesenhe, redigite em fonte cursiva ou vetorize de novo a partir de imagem.</li>
    </ul>
  </div>
  <div class="logo-stage">{logo(150)}</div>
</div>''')

page('02 Logotipo', f'''
{head('Versões', 'Três versões de cor, um único desenho', 'Teal e Azul-Escuro são os arquivos originais. A versão branca é o mesmo vetor recolorido, proposta para fotografia e para peças a uma cor.')}
<div class="g3 mt">
  <div><div class="tile" style="background:{H['azul-escuro']}">{logo(70, H['teal'])}</div><h4>Teal {tag('Original')}</h4><p class="small">Principal. Sobre Azul-Escuro, Noite e fundos escuros. É a versão do site.</p></div>
  <div><div class="tile edge" style="background:{H['branco']}">{logo(70, H['azul-escuro'])}</div><h4>Azul-Escuro {tag('Original')}</h4><p class="small">Sobre Branco, Névoa, Gelo e sobre Teal Tweed. É a versão do tema claro.</p></div>
  <div><div class="tile photo">{logo(70, H['branco'])}</div><h4>Branco {tag('Proposta')}</h4><p class="small">Sobre fotografia escurecida, vídeo e impressão a uma cor (serigrafia, gravação, bordado).</p></div>
</div>
<p class="cap mt">Arquivos: SVG para web e apresentações, PNG de 2000 px para Office e e-mail, PDF vetorial RGB para gráfica (prova de cor obrigatória: o teal é cor de tela e fica fora do gamut CMYK).</p>''')

X = 64  # altura do logotipo no diagrama
page('02 Logotipo', f'''
{head('Proteção e tamanho', 'Respiro mínimo e menor tamanho legível')}
<div class="g2 mt">
  <div class="prot-wrap">
    <div class="prot">
      <div class="prot-box">{logo(130)}</div>
      <span class="x xl">X</span><span class="x xt">X</span><span class="x xr">X</span><span class="x xb">X</span>
    </div>
    <p class="cap">X = altura da letra e (≈ 30% da altura do logotipo). Deixe 1X livre em todos os lados; em capas e peças institucionais, 2X ou mais.</p>
  </div>
  <div>
    <p class="eb">Tamanhos mínimos</p>
    <table class="tb">
      <tr><th>Meio</th><th>Mínimo</th><th>Recomendado</th></tr>
      <tr><td>Tela</td><td>72 px de largura (22 px de altura)</td><td>104 px ou mais (navbar do site)</td></tr>
      <tr><td>Impressão</td><td>25 mm de largura</td><td>35 mm ou mais</td></tr>
      <tr><td>Avatar e favicon</td><td colspan="2">Use o avatar (página 11); o logotipo inteiro some abaixo desses tamanhos.</td></tr>
    </table>
    <div class="sizes">{logo(22)}<span>72 px</span>{logo(32.5)}<span>104 px</span>{logo(41.3)}<span>132 px · rodapé</span></div>
    <p class="cap">{tag('Proposta')} Abaixo de 72 px o traço fica mais fino que 1 px e o corte do t deixa de ser lido.</p>
  </div>
</div>''')

def ftile(ink, bg, label, good=True, extra=''):
    edge = ' edge' if bg in (H['branco'], H['nevoa']) else ''
    return f'<div><div class="tile sm{edge}" style="background:{bg};{extra}">{logo(40, ink)}</div><p class="small">{ok() if good else no()} {label}</p></div>'
page('02 Logotipo', f'''
{head('Fundos', 'Qual versão sobre qual fundo', 'O logotipo precisa de 3:1 de contraste com o fundo. A regra prática: teal só sobre escuro, Azul-Escuro sobre tudo que é claro, inclusive o próprio teal.')}
<div class="g4 mt">
  {ftile(H['teal'], H['azul-escuro'], 'Teal sobre Azul-Escuro · 14,82:1')}
  {ftile(H['teal'], H['noite-alta'], 'Teal sobre Noite Alta · 13,17:1')}
  {ftile(H['azul-escuro'], H['branco'], 'Azul-Escuro sobre Branco · 19,51:1')}
  {ftile(H['azul-escuro'], H['teal'], 'Azul-Escuro sobre Teal · 14,82:1')}
  {ftile(H['azul-escuro'], H['gelo'], 'Azul-Escuro sobre Gelo · 16,81:1')}
  {ftile(H['branco'], '#2a2f3a', 'Branco sobre foto escurecida', True, 'background-image:linear-gradient(135deg,#3b4252,#151821)')}
  {ftile(H['teal'], H['branco'], 'Teal sobre Branco · 1,32:1', False)}
  {ftile(H['branco'], H['teal'], 'Branco sobre Teal · 1,32:1', False)}
</div>''')

def bad(inner, label, bg=H['azul-escuro']):
    return f'<div><div class="tile sm bad" style="background:{bg}">{inner}</div><p class="small">{no("")} {label}</p></div>'
page('02 Logotipo', f'''
{head('Usos incorretos', 'O que nunca fazer com o logotipo')}
<div class="g4 mt">
  {bad(logo(40, H['teal'], 'style="transform:scaleX(1.45)"'), 'Distorcer ou achatar')}
  {bad(logo(40, H['teal'], 'style="transform:rotate(-12deg)"'), 'Girar ou inclinar')}
  {bad(logo(40, '#ff5a8a'), 'Recolorir fora das três versões')}
  {bad(logo(40, H['teal'], 'style="filter:drop-shadow(0 0 8px #08ffb1) drop-shadow(0 6px 4px #000)"'), 'Aplicar brilho, sombra ou degradê')}
  {bad(logo(40, H['teal']), 'Teal sobre fundo claro', H['nevoa'])}
  {bad(logo(40, H['teal']), 'Fundo poluído ou sem contraste', '#0b0c13;background-image:repeating-linear-gradient(45deg,#16594a 0 10px,#08ffb1 10px 12px,#0b0c13 12px 24px)')}
  {bad('<span style="font:italic 700 34px/1 Georgia,serif;color:#08ffb1">tweed</span>', 'Redigitar o nome em fonte cursiva')}
  {bad(f'<span style="display:flex;align-items:center;gap:10px">{logo(30, H["teal"])}<span style="font:800 15px/1.1 Inter;color:#fff;text-align:left">Agência<br>de Marketing</span></span>', 'Criar lockups com textos novos')}
</div>''')

page('02 Logotipo', f'''
{head('Avatar', 'Para perfis, ícones de app e favicon', 'O logotipo é horizontal e fino: em círculos e quadrados pequenos ele precisa de uma moldura própria. O avatar coloca o traço teal centralizado sobre Azul-Escuro, com 1X de respiro lateral.')}
<div class="g3 mt av">
  <div><img src="{R}/logos/avatar_tweed.svg" width="240" height="240" alt="Avatar quadrado"><h4>Quadrado {tag('Proposta')}</h4><p class="small">Ícone de aplicativo, favicon a partir de 48 px, miniaturas.</p></div>
  <div><img src="{R}/logos/avatar_tweed.svg" width="240" height="240" style="border-radius:50%" alt="Avatar circular"><h4>Circular {tag('Proposta')}</h4><p class="small">Instagram, LinkedIn, WhatsApp Business: a plataforma recorta o mesmo arquivo em círculo.</p></div>
  <div><p class="eb">Regras</p><ul class="list"><li>Fundo sempre Azul-Escuro; traço sempre Teal Tweed.</li><li>Não troque o fundo pela cor da campanha nem acrescente borda ou anel.</li><li>Abaixo de 48 px (favicon de 16 e 32 px), o site usa o SVG do logotipo, que o navegador reduz; a legibilidade ali é limitada e aceita.</li></ul></div>
</div>''')

# =============================================================== 03 CORES
page('03 Cores', f'''
<div class="chapter-mark">03</div>
{head('Cores institucionais', 'Três cores, nenhuma a mais')}
<div class="g3 mt">{sw('azul-escuro', True)}{sw('teal', True)}{sw('branco', True)}</div>
<div class="rule mt"><b>Se tudo é teal, nada é destaque.</b> O teal é o único acento do sistema: headline-chave, CTA, número, palavra em ênfase. Nunca preenche a página, nunca é decoração. Os CMYK são indicativos; o teal está fora do gamut de impressão em quadricromia e pede prova de cor (ou tinta especial) com o fornecedor.</div>''')

page('03 Cores', f'''
{head('Sistema escuro', 'Os tons de apoio que o site já usa', 'Medidos no CSS de produção do site. Todo escuro é azul-noite e todo cinza é levemente azulado: não existe preto puro nem cinza neutro na marca.')}
<div class="g3 mt">{sw('noite')}{sw('noite-alta')}{sw('teal-luz')}{sw('prata')}{sw('cinza')}{sw('cinza-fraco')}</div>''')

page('03 Cores', f'''
{head('Sistema claro', 'O mesmo DNA sobre fundo branco', 'O teal original some no claro (1,32:1 sobre Branco). Por isso o tema claro tem um teal próprio para texto, o Teal Tinta, e reserva o Teal Tweed para superfícies, onde ele volta a funcionar com texto Azul-Escuro.')}
<div class="g3 mt">{sw('branco')}{sw('nevoa')}{sw('gelo')}{sw('grafite')}{sw('grafite-fraco')}{sw('teal-tinta')}</div>''', 'light')

def semrow(n, d, c, u):
    def res(v):
        m = re.fullmatch(r'\{tweed-(.+)\}', v)
        return (H[m.group(1)], C[m.group(1)][0]) if m else (v, v.replace('rgba', '').replace(' ', ''))
    dv, dn = res(d); cv, cn = res(c)
    def dot(v, bg):
        return f'<span class="dot" style="background:{bg}"><i style="background:{v}"></i></span>'
    return f'<tr><td class="mono">--tweed-{n}</td><td>{dot(dv, H["azul-escuro"])}{dn}</td><td>{dot(cv, H["branco"])}{cn}</td><td class="u">{u}</td></tr>'
SEM_SHOW = ['superficie', 'superficie-elevada', 'superficie-elevada-2', 'texto', 'texto-suave', 'texto-fraco', 'acento', 'acento-forte', 'botao-primario', 'botao-primario-texto', 'fio', 'foco', 'logo']
page('03 Cores', f'''
{head('Tokens de tema', 'Nomeie o papel, não a cor', 'Em site, apresentação e documento, use os tokens de tema: o mesmo nome entrega a cor certa em cada fundo. Lista completa em tokens/tweed-tokens.css.')}
<table class="tb sem mt"><tr><th>Token</th><th>Escuro</th><th>Claro</th><th>Uso</th></tr>''' + ''.join(semrow(*s) for s in SEM if s[0] in SEM_SHOW) + '</table>')

def crrow(a, b, x, y):
    v = cr(x, y)
    st = 'Passa (AAA)' if v >= 7 else 'Passa' if v >= 4.5 else 'Só texto grande e ícones' if v >= 3 else 'Reprova'
    cls = 'pass' if v >= 4.5 else 'mid' if v >= 3 else 'fail'
    return f'<tr><td><span class="pair" style="background:{y};color:{x}">Aa</span>{a} sobre {b}</td><td class="num">{fmt(v)}:1</td><td class="{cls}">{st}</td></tr>'
page('03 Cores', f'''
{head('Contraste', 'Cada par verificado (WCAG 2.x)', 'Texto comum precisa de 4,5:1; texto a partir de 24 px, ícones e bordas de controle, de 3:1.')}
<div class="g2 mt"><table class="tb">{"".join(crrow(*p) for p in PAIRS[:8])}</table><table class="tb">{"".join(crrow(*p) for p in PAIRS[8:])}</table></div>
<p class="cap">Teal Tweed sobre Branco ou Névoa reprova até para texto grande: no claro, todo teal em forma de texto, linha fina ou ícone é Teal Tinta.</p>''')

page('03 Cores', f'''
{head('Proporção e superfícies', 'Muito fundo, pouco acento')}
<div class="g2 mt">
  <div>
    <p class="eb">Escuro</p>
    <div class="bar"><i style="flex:76;background:{H['azul-escuro']};box-shadow:inset 0 0 0 1px rgba(255,255,255,.12)"></i><i style="flex:10;background:{H['noite-alta']}"></i><i style="flex:9;background:{H['branco']}"></i><i style="flex:5;background:{H['teal']}"></i></div>
    <p class="cap">Azul-Escuro 76% · Noite 10% · Branco 9% · Teal 5%</p>
    <p class="eb mt2">Claro</p>
    <div class="bar"><i style="flex:70;background:{H['branco']}"></i><i style="flex:14;background:{H['nevoa']}"></i><i style="flex:11;background:{H['azul-escuro']}"></i><i style="flex:5;background:{H['teal']}"></i></div>
    <p class="cap">Branco 70% · Névoa e Gelo 14% · Azul-Escuro 11% · Teal 5%</p>
  </div>
  <div>
    <p class="eb">Card tingido {tag('Site')}</p>
    <div class="g2 tight" style="zoom:1.3">
      <div class="ct big"><span class="ic">{icon('tela')}</span><b>O site parece antigo.</b><p>A primeira impressão não é a reunião: é a página que abre antes dela.</p></div>
      <div class="th-l"><div class="ct big"><span class="ic">{icon('tela')}</span><b>O site parece antigo.</b><p>A primeira impressão não é a reunião: é a página que abre antes dela.</p></div></div>
    </div>
    <p class="cap">A única luz da marca: três radiais escuros no topo (área de leitura limpa) e três teal na base, com um anel de luz girando na borda. No claro {tag('Proposta')}, a mesma receita vira menta e o anel usa Teal Tinta. Texto secundário em Prata no escuro, Grafite no claro.</p>
  </div>
</div>''')

# =============================================================== 04 TIPOGRAFIA
page('04 Tipografia', f'''
<div class="chapter-mark">04</div>
<div class="g2 top">
  <div>
    {head('Família', 'Inter, e só Inter')}
    <p class="body">A Inter 4 tem cortes ópticos desenhados para cada faixa de tamanho. A Tweed usa três: <b>18pt</b> para texto, <b>24pt</b> para interface e <b>28pt</b> para títulos. Os nomes são dos cortes, não tamanhos de corpo.</p>
    <table class="tb">
      <tr><th>Peso no CSS</th><th>Arquivo</th><th>Uso</th></tr>
      <tr><td>400</td><td>Inter 18pt Regular (e Italic)</td><td>Corpo, lead, legendas</td></tr>
      <tr><td>500 · 600</td><td>Inter 24pt Medium (e Medium Italic)</td><td>Botão, navegação, eyebrow</td></tr>
      <tr><td>700 · 800</td><td>Inter 28pt Bold</td><td>Títulos, números, citações</td></tr>
      <tr><td>700 · 800 itálico</td><td>Inter 28pt Bold Italic</td><td>A palavra em ênfase dentro de um título</td></tr>
    </table>
    <p class="cap">No site, cada arquivo declara a faixa de pesos que cobre (font-weight: 500 600), para o navegador nunca sintetizar negrito falso. Sem os arquivos, use a Inter do Google Fonts com font-optical-sizing: auto.</p>
  </div>
  <div class="spec">
    <div class="w800">Aa</div>
    <p class="w700">Clareza consistência confiança</p>
    <p class="w500">Estratégia, design e execução</p>
    <p class="w400">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz<br>0123456789 · ãçéêíóõú · +500 · 30 · R$</p>
    <p class="w800 it">A marca ficou <em>menor</em> que o negócio.</p>
  </div>
</div>''')

def trow(t):
    n, size, cl, lh, w, ls, u, s = t
    px = float(size.replace('rem', '')) * 16
    m = re.match(r'clamp\(([\d.]+)rem', cl)
    rng = f'{float(m.group(1)) * 16:.0f}–{px:.0f} px' if m else f'{px:.0f} px'
    vis = min(px, 34)
    style = f'font-size:{vis}px;line-height:{min(lh, 1.15) if vis > 30 else 1.3};font-weight:{w};letter-spacing:{ls}'
    if n == 'eyebrow':
        style += ';text-transform:uppercase;color:var(--ac)'
    if n in ('numero', 'mega'):
        style += ';color:var(--ac)'
    sample = {'mega': '03', 'numero': '+500'}.get(n, 'Presença com propósito' if px < 30 else 'Clareza e direção')
    return f'<tr><td><b>{n}</b><span>{u}</span></td><td>{w}</td><td>{rng}</td><td>{str(lh).replace(".", ",")}</td><td>{ls.replace("-", "−").replace(".", ",")}</td><td class="smp" style="{style}">{sample}</td></tr>'
page('04 Tipografia', f'''
{head('Hierarquia digital', 'Contraste de escala e peso, nunca de família', 'Valores do site (1 rem = 16 px; faixa = mínimo e máximo do clamp). Quanto maior o texto, mais apertado o tracking. Títulos em caixa de frase; caixa alta só no eyebrow.')}
<table class="tb type">
<tr><th>Estilo</th><th>Peso</th><th>Tamanho</th><th>Entrelinha</th><th>Tracking</th><th>Amostra</th></tr>''' + ''.join(trow(t) for t in TYPE if t[0] not in ('mega', 'caption')) + '</table>')

page('04 Tipografia', f'''
{head('Apresentações e documentos', 'A mesma hierarquia fora do navegador')}
<div class="g2 mt">
  <table class="tb tall">
    <tr><th>Estilo</th><th>Slide 1920 × 1080</th><th>Documento A4</th><th>Post 1080 × 1350</th></tr>
    <tr><td>Display · 800</td><td>112–128 px</td><td>36–44 pt</td><td>88–104 px</td></tr>
    <tr><td>H2 · 800</td><td>72–80 px</td><td>24–28 pt</td><td>64–72 px</td></tr>
    <tr><td>H3 · 700</td><td>40 px</td><td>14–16 pt</td><td>40 px</td></tr>
    <tr><td>Lead · 400</td><td>32 px</td><td>12–13 pt</td><td>32 px</td></tr>
    <tr><td>Corpo · 400</td><td>26–28 px</td><td>10,5–11 pt</td><td>28 px</td></tr>
    <tr><td>Eyebrow · 600</td><td>20 px · +0,16em</td><td>8 pt · +0,16em</td><td>22 px · +0,16em</td></tr>
  </table>
  <div>
    <p class="eb">Ênfase {tag('Site')}</p>
    <p class="emdemo">Somos contra o marketing que <em>ocupa espaço</em>.</p>
    <ul class="list">
      <li>A ênfase é <b>itálico na cor de acento</b>: Teal Tweed no escuro, Teal Tinta no claro. Uma ênfase por título.</li>
      <li>No corpo de texto, ênfase é negrito na cor do texto, sem itálico colorido.</li>
      <li>Números de prova usam algarismos tabulares e cor de acento.</li>
      <li>Linha de texto corrido entre 60 e 80 caracteres em documentos; no site, o texto acompanha o container.</li>
    </ul>
    <p class="cap">{tag('Proposta')} Os tamanhos de slide, A4 e post derivam da escala do site.</p>
  </div>
</div>''')

# =============================================================== 05 LINGUAGEM VISUAL
page('05 Linguagem visual', f'''
<div class="chapter-mark">05</div>
{head('Grid e espaço', 'Largura generosa, ritmo constante')}
<div class="g3 mt">
  <div class="gridbox"><div class="gb-page"><div class="gb-wrap"><i></i><i></i><i></i><i></i></div></div><h4>Site {tag('Site')}</h4><p class="small">Container de até 1600 px, margem lateral de 20 a 64 px (5vw), seção de 68 a 112 px de respiro vertical, 16 a 24 px entre cards.</p></div>
  <div class="gridbox"><div class="gb-page slide"><div class="gb-wrap s"><i></i><i></i><i></i><i></i><i></i><i></i></div></div><h4>Slide 16:9 {tag('Proposta')}</h4><p class="small">1920 × 1080 com margem de 120 px e 12 colunas de 96 px com vão de 24 px. Logotipo com 40 a 48 px de altura no rodapé ou na capa.</p></div>
  <div class="gridbox"><div class="gb-page a4"><div class="gb-wrap a"><i></i><i></i><i></i><i></i></div></div><h4>A4 e proposta {tag('Proposta')}</h4><p class="small">Margem de 18 mm, 6 colunas com vão de 5 mm. Retrato para proposta mobile (100 × 200 mm), paisagem para apresentação formal.</p></div>
</div>
<table class="tb mt"><tr><th>Token</th><th>Valor</th><th>Uso</th></tr>
<tr><td class="mono">--tweed-space-gutter</td><td>clamp(1.25rem, 5vw, 4rem)</td><td>Margem lateral</td></tr>
<tr><td class="mono">--tweed-space-secao</td><td>clamp(4.25rem, 9.8vh, 7rem)</td><td>Respiro de seção (metade no celular)</td></tr>
<tr><td class="mono">--tweed-space-cabeca</td><td>clamp(2.5rem, 6vw, 4.5rem)</td><td>Do título ao conteúdo</td></tr>
<tr><td class="mono">--tweed-space-grade</td><td>clamp(1rem, 2vw, 1.5rem)</td><td>Vão entre cards</td></tr></table>''')

page('05 Linguagem visual', f'''
{head('Componentes', 'Poucos elementos, sempre os mesmos')}
<div class="g2 mt comp" style="zoom:1.28">
  <div class="cpanel">
    <p class="eb">Botões · escuro</p>
    <div class="row"><span class="btnp lg">Começar uma conversa {icon('seta', 18)}</span><span class="btng lg">Ver como trabalhamos</span></div>
    <p class="eb mt2">Eyebrow, chips e etapa</p>
    <p class="eb ac">Capítulo 03 · O método</p>
    <div class="row chips"><span class="chp">Identidade visual</span><span class="chp">Websites</span><span class="chp">Fotografia e vídeo</span></div>
    <div class="step"><span>01</span><div><b>Diagnóstico de percepção</b><p>Antes de criar, entendemos o negócio.</p></div></div>
  </div>
  <div class="cpanel th-l">
    <p class="eb">Botões · claro {tag('Proposta')}</p>
    <div class="row"><span class="btnp lg">Começar uma conversa {icon('seta', 18)}</span><span class="btng lg">Ver como trabalhamos</span></div>
    <p class="eb mt2">Eyebrow, chips e etapa</p>
    <p class="eb ac">Capítulo 03 · O método</p>
    <div class="row chips"><span class="chp">Identidade visual</span><span class="chp">Websites</span><span class="chp">Fotografia e vídeo</span></div>
    <div class="step"><span>01</span><div><b>Diagnóstico de percepção</b><p>Antes de criar, entendemos o negócio.</p></div></div>
  </div>
</div>
<p class="cap">Botão é sempre pílula, 48 px de altura (56 px no grande), rótulo 15 px peso 600 que nunca quebra linha. No escuro, o primário é teal com rótulo Azul-Escuro; no claro, é Azul-Escuro com rótulo teal: a assinatura da marca em miniatura. Ghost: vidro com fio de 28%. Hover: halo teal abaixo do botão e 2 px de subida. Foco: anel de 2 px no acento, afastado 3 px.</p>''')

page('05 Linguagem visual', f'''
{head('Formas e superfícies', 'Cantos suaves, fios finos, luz só na base')}
<div class="g2 mt">
  <div>
    <p class="eb">Raios {tag('Site')}</p>
    <div class="radii" style="zoom:1.35">''' + ''.join(f'<div><i style="border-radius:{r}"></i><b>{n}</b><span>{r}</span></div>' for n, r in [('foco', '4px'), ('sm', '8px'), ('md', '10px'), ('nav', '14px'), ('foto', '16px'), ('card', '18px'), ('depo', '24px'), ('pill', '999px')]) + f'''</div>
    <ul class="list mt2">
      <li>Bordas são fios de 1 px em alfa (9% de branco no escuro, 10% de Azul-Escuro no claro), nunca cinza opaco.</li>
      <li>Sem sombra externa, exceto no card de depoimento. Profundidade vem de cor, fio e luz interna.</li>
      <li>Nada de faixa colorida na lateral do card, degradês multicoloridos ou glassmorphism fora da navbar e do botão ghost.</li>
    </ul>
  </div>
  <div>
    <p class="eb">Número de prova e depoimento</p>
    <div class="g2 tight" style="zoom:1.25">
      <div class="ct stat"><b class="sn">+500</b><p>marcas atendidas</p></div>
      <div class="ct stat"><b class="sn">30</b><p>anos de repertório criativo</p></div>
    </div>
    <div class="depo mt2" style="zoom:1.25"><img src="{R}/componentes/5stars.png" width="104" alt="Cinco estrelas"><p>“[Texto real do depoimento, sem editar o sentido.]”</p><b>[Nome do cliente]</b><span>[Cargo · Empresa]</span></div>
  </div>
</div>''')

page('05 Linguagem visual', f'''
{head('Iconografia', 'Dois sistemas, cada um no seu lugar')}
<div class="g2 mt">
  <div>
    <p class="eb">Ícones de interface {tag('Site')}</p>
    <div class="icons" style="zoom:1.3">''' + ''.join(f'<div><span class="ic">{icon(k, 26)}</span><small>{k}</small></div>' for k in ['seta', 'seta-esq', 'tela', 'alvo', 'canais', 'check', 'x', 'alerta', 'mais']) + f'''</div>
    <ul class="list"><li>Traço de 1,75, viewBox 24, pontas e junções arredondadas, sem preenchimento.</li><li>Em quadro de 44 px com raio 10 e fundo de acento a 8%, ou soltos em botões e setas.</li><li>Sempre acompanham texto; nunca são o único portador de sentido.</li></ul>
  </div>
  <div>
    <p class="eb">Ícones de seção {tag('Original')}</p>
    <div class="sicons" style="zoom:1.15">
      <div>{sicon('lowest-price')}<p>Não somos a opção de quem procura o menor preço.</p></div>
      <div>{sicon('overload')}<p>Não medimos marketing por quantidade de peças.</p></div>
      <div>{sicon('handoff')}<p>Não funcionamos com quem quer terceirizar a marca sem participar.</p></div>
      <div>{sicon('formula')}<p>Não vendemos fórmula pronta nem resultado garantido.</p></div>
    </div>
    <p class="cap">Exclusivos da seção “Talvez a Tweed não seja para você”, sempre nessa ordem. Desenhados em preto: recolora para Teal Tweed no escuro e Azul-Escuro ou Teal Tinta no claro. A avaliação dos depoimentos é sempre a imagem das cinco estrelas, nunca estrelas desenhadas ou emoji.</p>
  </div>
</div>''')

page('05 Linguagem visual', f'''
{head('Imagem', 'Pessoas reais, decoração discreta, prova com nome')}
<div class="g3 mt img">
  <div><div class="ph"><img src="{R}/componentes/felipe-e-cintia-3-wide.jpg" alt="Felipe Rijo e Cintia Groenwald"></div><h4>Fundadores {tag('Original')}</h4><p class="small">Felipe e Cintia, só em peças sobre quem é a Tweed. Três proporções (4:3, quadrada, wide), raio de 16 px, sem filtros.</p></div>
  <div><div class="ph dog"><img src="{R}/componentes/tweed-cachorrinho-github.png" alt="Cachorrinho Tweed"></div><h4>Cachorrinho Tweed {tag('Original')}</h4><p class="small">Assinatura afetiva: pequeno (56 a 84 px), num canto, em opacidade cheia. Nunca protagonista, nunca recortado ou recolorido.</p></div>
  <div><div class="ph brands"><img src="{R}/componentes/marcas-atendidas.png" alt="Marcas atendidas"></div><div class="ph brands l"><img src="{R}/componentes/marcas-atendidas-escuro.png" alt="Marcas atendidas em Azul-Escuro"></div><h4>Marcas atendidas</h4><p class="small">Branca sobre escuro {tag('Original')}; Azul-Escuro sobre claro {tag('Proposta')}. Horizontal ou mobile; nunca recorte ou reordene os logotipos.</p></div>
</div>
<p class="cap mt">Fotografia de trabalho: pessoas reais, processo, bastidor e produto com luz natural ou de estúdio. Evite banco de imagem genérico, aperto de mão, engrenagens e imagens de IA que se passem por reais.</p>''')

page('05 Linguagem visual', f'''
{head('Movimento e acessibilidade', 'Movimento como resposta, não como enfeite')}
<div class="g2 mt">
  <table class="tb tall">
    <tr><th>Elemento</th><th>Comportamento {tag('Site')}</th></tr>
    <tr><td>Curva</td><td>Uma só: cubic-bezier(.16, 1, .3, 1)</td></tr>
    <tr><td>Entrada de blocos</td><td>Opacidade e 26 px de subida em 0,7 s, com atraso escalonado de 100 ms</td></tr>
    <tr><td>Card tingido</td><td>Anel de luz girando na borda em 8 s, linear</td></tr>
    <tr><td>Botão</td><td>Halo teal acende abaixo; sobe 2 px e cresce 2% em 0,3 s</td></tr>
    <tr><td>Hero</td><td>Fita de vidro animada atrás de um véu que garante o contraste</td></tr>
    <tr><td>Serviços</td><td>Esteira de chips em 38 s, pausa no hover</td></tr>
  </table>
  <div>
    <p class="eb">Regras</p>
    <ul class="list">
      <li>Com <span class="mono">prefers-reduced-motion</span>, todo deslocamento para: reveals, parallax, esteira e anel. Transições de cor de 150 a 300 ms continuam, porque são retorno de estado.</li>
      <li>Sem JavaScript, o conteúdo nasce visível.</li>
      <li>Alvo mínimo de 44 px em tudo que é clicável.</li>
      <li>Foco visível em tudo que é operável; link para pular conteúdo no topo.</li>
      <li>Modo de alto contraste do Windows: decoração some, botões e cards ganham contorno do sistema.</li>
    </ul>
  </div>
</div>''')

# =============================================================== 06 TOM DE VOZ
page('06 Tom de voz', f'''
<div class="chapter-mark">06</div>
<div class="g2 top">
  <div>
    {head('Tom de voz', 'Como um sócio muito bom: pensa junto, fala claro, entrega com acabamento')}
    <table class="tb pairs"><tr><th>Somos</th><th>E também</th></tr><tr><td>Estratégicos</td><td>Práticos</td></tr><tr><td>Completos</td><td>Próximos</td></tr><tr><td>Criativos</td><td>Executores</td></tr><tr><td>Diretos</td><td>Cuidadosos</td></tr></table>
    <p class="eb mt2">Cinco atributos</p>
    <p class="body"><b>Claro</b> · <b>Direto</b> · <b>Confiante</b> sem arrogância · <b>Humano</b> · <b>Preciso</b></p>
  </div>
  <div>
    <div class="vx"><span>{no('')}</span><p>“Utilizamos uma abordagem omnichannel integrada com foco em brand equity.”</p></div>
    <div class="vx ok"><span>{ok('')}</span><p>“Cuidamos de tudo para que sua marca apareça com coerência em todos os lugares onde o cliente vai te encontrar.”</p></div>
    <p class="eb mt2">Palavras do território</p>
    <p class="small">Use: clareza, presença, confiança, direção, coerência, estratégia, acabamento, percepção de valor, método, marca.<br>Evite como conceito central: posts, feed, artes, pacotes, barato, gestão de Instagram.</p>
    <p class="eb mt2">Teste do espelho</p>
    <p class="small">Isso poderia ter sido escrito por qualquer agência? Faz o leitor sentir que estamos no controle do assunto? Representa a Tweed que queremos ser? Um “não” e o texto volta para a mesa. Guia completo em tom-de-voz/tom-de-voz.md.</p>
  </div>
</div>''')

# =============================================================== 07 APLICAÇÕES
page('07 Aplicações', f'''
<div class="chapter-mark">07</div>
{head('Site', 'O tema escuro em casa')}
<div class="site mt">
  <div class="s-nav">{logo(22)}<span>O problema</span><span>Método</span><span>O que fazemos</span><span>A agência</span><span class="btnp sm">Falar com a Tweed</span></div>
  <div class="s-hero"><div class="s-glow"></div>
    <p class="eb ac">Agência boutique full-service · Porto Alegre · desde 2017</p>
    <h3>Sua empresa cresceu.<br><em>Sua comunicação</em><br>ainda não acompanhou.</h3>
    <p>Estratégia, design e execução para marcas que precisam ser percebidas à altura do que entregam.</p>
    <div class="row"><span class="btnp">Começar uma conversa {icon('seta', 16)}</span><span class="btng">Ver como trabalhamos</span></div>
    <div class="s-meta"><div><b>+500</b><span>marcas atendidas</span></div><div><b>30</b><span>anos de repertório criativo</span></div><div><b>1</b><span>interlocutor, do briefing à entrega</span></div></div>
  </div>
</div>''')

page('07 Aplicações', f'''
{head('Proposta comercial', 'O tema claro em documento')}
<div class="g2 mt">
  <div class="a4p">
    <div class="a4h">{logo(18, H['azul-escuro'])}<span>Proposta · Novembro 2026</span></div>
    <p class="eb ac">01 · O que percebemos</p>
    <h3>Sua empresa cresceu. Sua comunicação <em>ainda não</em> acompanhou.</h3>
    <p>Texto demonstrativo: o que percebemos sobre o momento da empresa, o que isso significa e o que propomos. Frases curtas, linguagem de parceiro, nunca de vendedor.</p>
    <div class="a4box"><b class="sn">6 etapas</b><span>do diagnóstico à otimização contínua</span></div>
    <div class="a4f"><span>agenciatweed.com.br</span><img src="{R}/componentes/tweed-cachorrinho-github.png" alt="" width="34"></div>
  </div>
  <div>
    <ul class="list">
      <li>Página Branco, blocos em Névoa e Gelo, texto Azul-Escuro e Grafite.</li>
      <li>Eyebrow, numeração e ênfase em Teal Tinta. Teal Tweed só como superfície (um bloco, um marcador), com texto Azul-Escuro.</li>
      <li>Logotipo Azul-Escuro no cabeçalho; cachorrinho opcional no rodapé.</li>
      <li>Estrutura do tom de voz: o que percebemos, o que significa, o que propomos, como trabalhamos, o que esperar.</li>
      <li>Seção “Talvez a Tweed não seja para você” com os quatro ícones em Azul-Escuro.</li>
      <li>Faixa de marcas na versão Azul-Escuro.</li>
    </ul>
    <p class="cap">{tag('Proposta')} Para propostas que vão para impressão, o claro economiza tinta e preserva o contraste; para propostas lidas no celular, o escuro continua válido.</p>
  </div>
</div>''', 'light')

page('07 Aplicações', f'''
{head('Apresentações e redes', 'Os dois temas lado a lado')}
<div class="g2 mt slides">
  <div class="sl d"><p class="eb ac">Capítulo 02 · A convicção</p><h3>Somos contra o marketing que <em>ocupa espaço</em>.</h3><div class="slf">{logo(14)}<span>03</span></div></div>
  <div class="sl l"><p class="eb ac">Capítulo 02 · A convicção</p><h3>Somos contra o marketing que <em>ocupa espaço</em>.</h3><div class="slf">{logo(14, H['azul-escuro'])}<span>03</span></div></div>
</div>
<div class="posts mt">
  <div class="po d"><p class="eb ac">Branding</p><h3>Branding não é logo. É o que o cliente sente antes de abrir a carteira.</h3>{logo(14)}</div>
  <div class="po t"><p class="eb">Branding</p><h3>Branding não é logo. É o que o cliente sente antes de abrir a carteira.</h3>{logo(14, H['azul-escuro'])}</div>
  <div class="po l"><p class="eb ac">Branding</p><h3>Branding não é logo. É o que o cliente sente antes de abrir a carteira.</h3>{logo(14, H['azul-escuro'])}</div>
  <div class="ptxt"><p class="small"><b>Slides 16:9</b>: margem de 120 px, um título por slide, logotipo pequeno no rodapé com a numeração.</p><p class="small"><b>Posts 4:5</b>: escuro como padrão; a versão teal (superfície) com texto e logotipo Azul-Escuro é o destaque da grade, no máximo uma a cada seis; a versão clara serve a carrosséis de leitura longa.</p></div>
</div>''')

page('07 Aplicações', f'''
{head('Checklist', 'Antes de publicar ou enviar')}
<div class="g2 mt check">
  <ul>
    <li>{icon('check', 16, 2.2)} Logotipo de um arquivo oficial, na versão certa para o fundo, com 1X de respiro.</li>
    <li>{icon('check', 16, 2.2)} Fundo Azul-Escuro (escuro) ou Branco (claro), sem preto puro nem cinza neutro.</li>
    <li>{icon('check', 16, 2.2)} Teal só no que precisa de destaque; no claro, teal de texto é Teal Tinta.</li>
    <li>{icon('check', 16, 2.2)} Só Inter, nos pesos 400, 500/600 e 700/800; uma ênfase em itálico por título.</li>
    <li>{icon('check', 16, 2.2)} Contraste de 4,5:1 no texto e 3:1 em ícones e bordas de controle.</li>
  </ul>
  <ul>
    <li>{icon('check', 16, 2.2)} Botões em pílula; cards com raio 18 e fio de 1 px; sem sombras inventadas.</li>
    <li>{icon('check', 16, 2.2)} Ícones de seção só na seção deles; cinco estrelas só como imagem.</li>
    <li>{icon('check', 16, 2.2)} Fotos reais, sem filtro; cachorrinho pequeno e num canto.</li>
    <li>{icon('check', 16, 2.2)} Texto passa no teste do espelho: sem superlativo, sem promessa que não controlamos.</li>
    <li>{icon('check', 16, 2.2)} Depoimentos e números são reais, com nome e fonte.</li>
  </ul>
</div>
<p class="cap mt">Governança: itens marcados como Proposta valem como recomendação até a aprovação de Felipe Rijo e Cintia Groenwald. Arquivos, tokens e o histórico de versões estão no repositório github.com/agenciatweed/brand-guidelines-tweed.</p>''')

page('', f'''
<div class="grid-lines"></div><div class="glow gl1"></div>
<div class="back">
  {logo(84)}
  <p class="statement">Marcas não crescem por barulho.<br>Crescem por <em>clareza</em>, <em>consistência</em> e <em>confiança</em>.</p>
  <p class="cap">agenciatweed.com.br · contato@agenciatweed.com.br · Porto Alegre<br>{VERSION}</p>
  <img class="dogb" src="{R}/componentes/tweed-cachorrinho-github.png" alt="" width="72">
</div>''', 'dark', 'p-cover')

# =============================================================== CSS
CSS = f'''
@font-face{{font-family:Inter;src:url({R}/tipografia/inter-18pt-regular.ttf);font-weight:400;font-style:normal}}
@font-face{{font-family:Inter;src:url({R}/tipografia/inter-18pt-italic.ttf);font-weight:400;font-style:italic}}
@font-face{{font-family:Inter;src:url({R}/tipografia/inter-24pt-medium.ttf);font-weight:500 600;font-style:normal}}
@font-face{{font-family:Inter;src:url({R}/tipografia/inter-24pt-mediumitalic.ttf);font-weight:500 600;font-style:italic}}
@font-face{{font-family:Inter;src:url({R}/tipografia/inter-28pt-bold.ttf);font-weight:700 800;font-style:normal}}
@font-face{{font-family:Inter;src:url({R}/tipografia/inter-28pt-bolditalic.ttf);font-weight:700 800;font-style:italic}}
@page{{size:297mm 210mm;margin:0}}
*{{box-sizing:border-box}}
html,body{{margin:0;padding:0}}
body{{font-family:Inter,sans-serif;font-synthesis:none;-webkit-font-smoothing:antialiased;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
h1,h2,h3,h4,p,ul{{margin:0}}
.page{{width:297mm;height:210mm;position:relative;overflow:hidden;isolation:isolate;page-break-after:always;padding:24mm 20mm 20mm;
  --bg:{H['azul-escuro']};--bg2:{H['noite']};--bg3:{H['noite-alta']};--tx:{H['branco']};--tx2:{H['cinza']};--tx3:{H['cinza-fraco']};--tin:{H['prata']};
  --ac:{H['teal']};--line:rgba(255,255,255,.09);--line2:rgba(255,255,255,.28);--bp:{H['teal']};--bpt:{H['azul-escuro']};--gf:rgba(11,12,19,.55);
  --cardbg:{H['azul-escuro']};--cardimg:radial-gradient(at 88% 40%,#0b0c13 0,transparent 85%),radial-gradient(at 49% 30%,#0b0c13 0,transparent 85%),radial-gradient(at 14% 26%,#0b0c13 0,transparent 85%),radial-gradient(at 0% 64%,hsla(161,100%,52%,.34) 0,transparent 85%),radial-gradient(at 41% 94%,hsla(161,100%,80%,.24) 0,transparent 85%),radial-gradient(at 100% 99%,hsla(172,95%,45%,.38) 0,transparent 85%);
  --ring:rgba(8,255,177,.6);--shin:inset 0 -16px 24px -4px rgba(255,255,255,.10);--mark:rgba(255,255,255,.055);
  background:var(--bg);color:var(--tx)}}
.page.light,.th-l{{--bg:{H['branco']};--bg2:{H['nevoa']};--bg3:{H['gelo']};--tx:{H['azul-escuro']};--tx2:{H['grafite']};--tx3:{H['grafite-fraco']};--tin:{H['grafite']};
  --ac:{H['teal-tinta']};--line:rgba(11,12,19,.10);--line2:rgba(11,12,19,.28);--bp:{H['azul-escuro']};--bpt:{H['teal']};--gf:rgba(255,255,255,.6);
  --cardbg:#fff;--cardimg:radial-gradient(at 88% 40%,#fff 0,transparent 85%),radial-gradient(at 49% 30%,#fff 0,transparent 85%),radial-gradient(at 14% 26%,#fff 0,transparent 85%),radial-gradient(at 0% 64%,hsla(161,100%,52%,.22) 0,transparent 85%),radial-gradient(at 41% 94%,hsla(161,100%,80%,.30) 0,transparent 85%),radial-gradient(at 100% 99%,hsla(172,95%,45%,.24) 0,transparent 85%);
  --ring:rgba(0,112,77,.45);--shin:inset 0 -16px 24px -4px rgba(0,112,77,.06);--mark:rgba(11,12,19,.05)}}
.th-l{{color:var(--tx)}}
.hdr,.ftr{{position:absolute;left:20mm;right:20mm;display:flex;justify-content:space-between;font-size:9px;letter-spacing:.04em;color:var(--tx3)}}
.hdr{{top:10mm}} .ftr{{bottom:9mm;border-top:1px solid var(--line);padding-top:3mm}}
.eb{{font-size:11px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--ac);margin-bottom:8px}}
h1{{font-size:76px;line-height:.98;font-weight:800;letter-spacing:-.045em}}
h2{{font-size:40px;line-height:1.06;font-weight:800;letter-spacing:-.035em;max-width:250mm}}
em{{font-style:italic;color:var(--ac);font-weight:inherit}}
.lede{{font-size:15px;line-height:1.6;color:var(--tx2);margin-top:14px;max-width:215mm}}
.body{{font-size:13.5px;line-height:1.65;color:var(--tx2);margin-top:12px}}
.body b,.list b,.small b{{color:var(--tx);font-weight:700}}
.small{{font-size:11.5px;line-height:1.55;color:var(--tx2);margin-top:6px}}
.cap{{font-size:10.5px;line-height:1.55;color:var(--tx3);margin-top:10px}}
.cap b{{color:var(--tx2)}}
.mono{{font-family:ui-monospace,Menlo,monospace;font-size:.92em}}
.mt{{margin-top:9mm}} .mt2{{margin-top:6mm}}
.g2{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:12mm}} .g2.top{{align-items:start}} .g2.tight{{gap:4mm}}
.g3{{display:grid;grid-template-columns:repeat(3,1fr);gap:8mm}}
.g4{{display:grid;grid-template-columns:repeat(4,1fr);gap:8mm 6mm}}
.list{{padding-left:14px;margin-top:10px}} .list li{{font-size:12.5px;line-height:1.55;color:var(--tx2);margin-bottom:6px}} .list li::marker{{color:var(--ac)}}
.tag{{display:inline-block;vertical-align:middle;font-size:7.5px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;padding:2.5px 7px;border-radius:999px;margin-left:4px;border:1px solid}}
.tag-o{{color:var(--ac);border-color:var(--ac)}} .tag-s{{color:var(--tx2);border-color:var(--line2)}} .tag-p{{color:var(--tx);border-color:var(--line2);background:var(--bg3)}}
.mk{{display:inline-flex;align-items:center;gap:3px;font-size:8px;font-weight:700;padding:2px 7px 2px 5px;border-radius:999px;vertical-align:middle}}
.mk-ok{{background:var(--ac);color:var(--bg)}} .mk-no{{border:1.2px solid #ff6b81;color:#ff8597}}
.page.light .mk-no{{color:#b3263c;border-color:#b3263c}}
.chapter-mark{{position:absolute;bottom:13mm;right:16mm;z-index:-1;font-size:170px;font-weight:800;letter-spacing:-.05em;line-height:.8;color:var(--mark);pointer-events:none}}
/* capa */
.p-cover{{padding:0}}
.grid-lines{{position:absolute;inset:0;background-image:linear-gradient(to right,rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(to bottom,rgba(255,255,255,.05) 1px,transparent 1px);background-size:90px 90px;-webkit-mask-image:radial-gradient(ellipse 70% 70% at 70% 45%,#000 20%,transparent 78%)}}
.glow{{position:absolute;border-radius:50%;filter:blur(70px)}} .gl1{{width:560px;height:420px;right:-80px;bottom:-60px;background:radial-gradient(circle,rgba(8,255,177,.30),transparent 70%)}} .gl2{{width:380px;height:320px;right:260px;top:40px;background:radial-gradient(circle,rgba(8,255,177,.12),transparent 70%)}}
.cover{{position:relative;height:100%;padding:22mm 22mm 20mm;display:flex;flex-direction:column;justify-content:space-between}}
.cover .lede{{max-width:150mm;color:{H['prata']}}}
.cover .cap{{margin-top:22px;color:{H['cinza']}}}
.origins>div{{display:flex;gap:10px;align-items:flex-start;padding:10px 0;border-top:1px solid var(--line)}} .origins .tag{{margin:2px 0 0;min-width:64px;text-align:center}} .origins p{{font-size:12px;line-height:1.55;color:var(--tx2)}}
.words>div{{padding:14px 0;border-top:1px solid var(--line)}} .words .num{{font-size:10px;font-weight:700;color:var(--ac)}} .words h4{{font-size:24px;font-weight:700;letter-spacing:-.02em;margin:4px 0}} .words p{{font-size:12.5px;line-height:1.55;color:var(--tx2)}}
.sign{{position:absolute;left:20mm;bottom:22mm;font-size:21px;font-weight:700;letter-spacing:-.03em;color:var(--tx)}}
.toc{{margin-top:12mm;columns:2;column-gap:14mm}} .toc>div{{display:flex;gap:14px;align-items:baseline;padding:11px 0;border-top:1px solid var(--line);break-inside:avoid}}
.toc .n{{font-size:24px;font-weight:800;color:var(--ac);letter-spacing:-.04em;min-width:36px}} .toc h4{{font-size:18px;font-weight:700}} .toc p{{font-size:11px;color:var(--tx2);margin-top:2px}} .toc .pg{{margin-left:auto;font-size:10px;color:var(--tx3)}} .toc>div>div{{flex:1}}
/* botões e peças */
.btnp,.btng{{display:inline-flex;align-items:center;gap:7px;height:30px;padding:0 15px;border-radius:999px;font-size:10px;font-weight:600;letter-spacing:.01em;white-space:nowrap}}
.btnp{{background:var(--bp);color:var(--bpt)}} .btng{{border:1px solid var(--line2);color:var(--tx);background:var(--gf)}}
.btnp.sm{{height:22px;padding:0 10px;font-size:8px}} .btnp.lg,.btng.lg{{height:40px;padding:0 20px;font-size:12px}}
.row{{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-top:10px}}
.ct{{position:relative;border-radius:14px;padding:14px;background-color:var(--cardbg);background-image:var(--cardimg);box-shadow:var(--shin);border:1px solid var(--ring)}}
.ct b{{display:block;font-size:12px;font-weight:700;letter-spacing:-.01em;color:var(--tx);margin-top:8px}} .ct p{{font-size:9.5px;line-height:1.5;color:var(--tin);margin-top:4px}}
.ct .ic{{display:inline-flex;width:30px;height:30px;border-radius:8px;align-items:center;justify-content:center;background:color-mix(in srgb,var(--ac) 10%,transparent);color:var(--ac)}}
.ct.big{{padding:18px;border-radius:18px}} .ct.big b{{font-size:15px}}
.ct.stat{{padding:16px}} .sn{{font-size:30px!important;font-weight:800;letter-spacing:-.04em;color:var(--ac)!important;font-variant-numeric:tabular-nums;margin:0!important}}
.mini{{border-radius:16px;padding:16px 18px;background:var(--bg);border:1px solid var(--line)}} .mini-d{{--bg:{H['azul-escuro']}}}
.mini-nav{{display:flex;justify-content:space-between;align-items:center;padding:7px 8px 7px 12px;border:1px solid var(--line);border-radius:10px;margin-bottom:16px}}
.mini-h{{font-size:27px;line-height:1.06;font-weight:800;letter-spacing:-.035em;max-width:95%}} .mini-p{{font-size:10.5px;line-height:1.55;color:var(--tx2);margin-top:8px}}
.mini-row{{display:flex;gap:7px;margin-top:12px}} .mini-cards{{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:14px}}
.th-l .mini{{border-color:rgba(11,12,19,.12)}}
/* logotipo */
.logo-stage{{display:flex;align-items:center;justify-content:center;height:128mm;border-radius:18px;border:1px solid var(--line);background:radial-gradient(60% 60% at 50% 60%,rgba(8,255,177,.08),transparent 70%)}}
.tile{{height:62mm;box-shadow:inset 0 0 0 1px var(--line);border-radius:16px;display:flex;align-items:center;justify-content:center;margin-bottom:10px;overflow:hidden}}
.tile.sm{{height:40mm;margin-bottom:6px}} .tile.edge{{box-shadow:inset 0 0 0 1px rgba(11,12,19,.12)}} .tile.photo{{background:linear-gradient(135deg,#3b4252,#151821)}}
.tile.bad{{position:relative}}
h4{{font-size:14px;font-weight:700;letter-spacing:-.01em;color:var(--tx)}}
.prot-wrap{{display:flex;flex-direction:column;align-items:center}}
.prot{{position:relative;padding:46px;border:1px dashed var(--line2);border-radius:6px;background:repeating-linear-gradient(45deg,rgba(8,255,177,.06) 0 6px,transparent 6px 12px)}}
.prot-box{{background:var(--bg);padding:0;line-height:0;outline:1px solid rgba(8,255,177,.35)}}
.x{{position:absolute;font-size:10px;font-weight:700;color:var(--ac)}} .xl{{left:12px;top:50%;transform:translateY(-50%)}} .xr{{right:12px;top:50%;transform:translateY(-50%)}} .xt{{top:10px;left:50%}} .xb{{bottom:10px;left:50%}}
.tb{{width:100%;border-collapse:collapse;font-size:11.5px}} .tb th{{text-align:left;font-weight:500;color:var(--tx3);font-size:9px;padding:6px 8px 6px 0;border-bottom:1px solid var(--line2)}}
.tb td{{padding:8px 8px 8px 0;border-bottom:1px solid var(--line);color:var(--tx2);vertical-align:middle}} .tb td:first-child{{color:var(--tx)}}
.tb.tall td{{padding:13px 8px 13px 0;font-size:12.5px}} .tb td.num{{font-variant-numeric:tabular-nums;font-weight:600;color:var(--tx)}} .tb td.pass{{color:var(--ac);font-weight:600}} .tb td.mid{{color:var(--tx2)}} .tb td.fail{{color:#ff8597;font-weight:600}}
.page.light .tb td.fail{{color:#b3263c}}
.pair{{display:inline-flex;width:26px;height:20px;border-radius:5px;align-items:center;justify-content:center;font-size:10px;font-weight:700;margin-right:8px;box-shadow:inset 0 0 0 1px var(--line)}}
.sizes{{display:flex;align-items:flex-end;gap:10px;margin:16px 0 4px}} .sizes span{{font-size:9px;color:var(--tx3);margin-right:12px}}
.av img{{display:block;margin-bottom:12px;box-shadow:0 0 0 1px rgba(255,255,255,.14);border-radius:44px}}
/* cores */
.sw .chip{{height:34mm;border-radius:14px;box-shadow:inset 0 0 0 1px var(--line);padding:12px;display:flex;justify-content:space-between;align-items:flex-start}} .sw .chip b{{font-size:13px;font-weight:700}} .sw .chip .tag{{border-color:currentColor;color:inherit;background:transparent}}
.sw.big .chip{{height:74mm}} .sw .chip.edge{{box-shadow:inset 0 0 0 1px rgba(11,12,19,.14)}}
.swm{{display:flex;flex-direction:column;gap:1px;margin-top:7px}} .swm span{{font-size:10.5px;color:var(--tx2);font-variant-numeric:tabular-nums}} .swm span.mono{{font-size:12.5px;color:var(--tx);font-weight:600}} .swm p{{font-size:10.5px;line-height:1.5;color:var(--tx3);margin-top:4px}}
.g3 .sw:not(.big) .chip{{height:32mm}}
.rule{{padding:14px 18px;border-radius:14px;background:var(--bg2);border:1px solid var(--line);font-size:11px;line-height:1.6;color:var(--tx2)}} .rule b{{color:var(--ac)}}
.sem td{{font-size:9.5px;padding:5px 8px 5px 0}} .sem td.u{{color:var(--tx3)}} .dot{{display:inline-flex;width:18px;height:14px;border-radius:4px;align-items:center;justify-content:center;margin-right:6px;vertical-align:middle;box-shadow:inset 0 0 0 1px rgba(128,128,128,.35)}} .dot i{{width:8px;height:8px;border-radius:50%;box-shadow:0 0 0 1px rgba(128,128,128,.4)}}
.bar{{display:flex;height:32mm;border-radius:12px;overflow:hidden;box-shadow:0 0 0 1px var(--line2)}} .bar i{{display:block}}
/* tipografia */
.spec{{border-radius:18px;padding:22px 24px;background:var(--bg2);border:1px solid var(--line)}} .spec .w800{{font-size:130px;font-weight:800;letter-spacing:-.05em;line-height:.9;color:var(--ac)}}
.spec p{{margin-top:10px;color:var(--tx)}} .spec .w700{{font-size:22px;font-weight:700;letter-spacing:-.02em}} .spec .w500{{font-size:16px;font-weight:500}} .spec .w400{{font-size:11px;line-height:1.6;color:var(--tx2)}} .spec .w800.it{{font-size:22px;font-weight:800;letter-spacing:-.035em;line-height:1.1}}
.type{{margin-top:6mm}} .type td{{padding:4px 8px 4px 0}} .type td b{{display:block;font-size:11px;color:var(--tx)}} .type td span{{display:block;font-size:8.5px;color:var(--tx3);max-width:62mm;line-height:1.4}} .type td.smp{{color:var(--tx);white-space:nowrap;overflow:hidden;max-width:110mm}}
.emdemo{{font-size:40px;font-weight:800;letter-spacing:-.035em;line-height:1.1;margin:4px 0 10px}}
/* linguagem */
.gridbox .gb-page{{height:62mm;border-radius:10px;border:1px solid var(--line2);padding:8px 14px;margin-bottom:10px;background:var(--bg2)}} .gb-page.a4{{width:44mm;height:62mm;padding:6px 5px;margin-inline:auto}}
.gb-wrap{{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;height:100%}} .gb-wrap.s{{grid-template-columns:repeat(6,1fr);gap:4px}} .gb-wrap i{{background:rgba(8,255,177,.14);border-radius:2px}}
.page.light .gb-wrap i{{background:rgba(0,112,77,.12)}}
.cpanel{{border-radius:18px;padding:22px;background:var(--bg);border:1px solid var(--line)}}
.chp{{padding:5px 11px;border:1px solid var(--line);border-radius:999px;font-size:10px;color:var(--tx2);background:var(--bg2)}}
.step{{display:grid;grid-template-columns:38px 1fr;gap:12px;padding:12px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin-top:12px}} .step>span{{font-size:22px;font-weight:800;letter-spacing:-.04em;color:var(--ac)}} .step b{{font-size:13px;font-weight:700}} .step p{{font-size:9.5px;color:var(--tx2);margin-top:2px}}
.radii{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}} .radii div{{display:flex;flex-direction:column;align-items:flex-start;gap:2px}} .radii i{{width:46px;height:36px;border:1.5px solid var(--ac);border-right:0;border-bottom:0;margin-bottom:4px}} .radii b{{font-size:10px}} .radii span{{font-size:9px;color:var(--tx3)}}
.depo{{border-radius:20px;padding:18px;border:1px solid rgba(8,255,177,.2);background-color:var(--cardbg);background-image:radial-gradient(at 82% 34%,var(--cardbg) 0,transparent 82%),radial-gradient(at 6% 70%,hsla(161,100%,52%,.2) 0,transparent 84%),radial-gradient(at 96% 98%,hsla(172,95%,45%,.24) 0,transparent 84%);transform:rotate(-.5deg)}}
.depo img{{display:block;margin-bottom:10px}} .depo p{{font-size:13px;line-height:1.45;color:var(--tx);letter-spacing:-.01em}} .depo b{{display:block;margin-top:12px;font-size:10.5px}} .depo span{{font-size:9px;color:var(--tin)}}
.icons{{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-bottom:6px}} .icons div{{display:flex;flex-direction:column;align-items:center;gap:4px}} .icons .ic{{width:44px;height:44px;border-radius:10px;background:rgba(8,255,177,.08);color:var(--ac);display:flex;align-items:center;justify-content:center}} .icons small{{font-size:8.5px;color:var(--tx3)}}
.sicons{{display:grid;grid-template-columns:1fr 1fr;gap:12px 16px}} .sicons div{{display:flex;gap:10px;align-items:center}} .sicons p{{font-size:11.5px;line-height:1.45;color:var(--tx2)}} .sicons svg{{flex:none}}
.img .ph{{height:58mm;border-radius:16px;overflow:hidden;margin-bottom:10px;border:1px solid var(--line);display:flex;align-items:center;justify-content:center;background:var(--bg2)}} .img .ph img{{width:100%;height:100%;object-fit:cover}}
.img .ph.dog img{{width:auto;height:70%;object-fit:contain}} .img .ph.brands{{height:28mm;margin-bottom:4px;padding:4px}} .img .ph.brands img{{object-fit:contain}} .img .ph.brands.l{{background:#fff}}
.pairs{{margin-top:8mm}} .pairs td,.pairs th{{font-size:12px}} .vx{{display:flex;gap:10px;align-items:flex-start;padding:10px 12px;border-radius:12px;background:var(--bg2);margin-bottom:8px}} .vx p{{font-size:12.5px;line-height:1.5;color:var(--tx2)}} .vx.ok p{{color:var(--tx)}}
/* aplicações */
.site{{border-radius:18px;border:1px solid var(--line);overflow:hidden;background:{H['azul-escuro']};height:128mm;position:relative}}
.s-nav{{position:absolute;top:10px;left:10px;right:10px;display:flex;align-items:center;gap:16px;padding:8px 10px 8px 14px;border:1px solid var(--line);border-radius:12px;background:rgba(11,12,19,.72);z-index:2}} .s-nav span{{font-size:9px;color:var(--tx2)}} .s-nav .lg{{margin-right:auto}} .s-nav .btnp{{color:var(--bpt)}}
.s-hero{{position:relative;padding:64px 34px 0;height:100%}} .s-glow{{position:absolute;inset:0;background:radial-gradient(55% 60% at 80% 70%,rgba(8,255,177,.28),transparent 70%),radial-gradient(40% 45% at 60% 25%,rgba(8,255,177,.10),transparent 72%)}}
.s-hero>*:not(.s-glow){{position:relative}} .s-hero h3{{font-size:52px;line-height:1.02;font-weight:800;letter-spacing:-.045em}} .s-hero .eb{{white-space:nowrap}} .s-hero>p:not(.eb){{font-size:13px;color:var(--tx);margin-top:10px;max-width:120mm}}
.s-meta{{display:flex;gap:30px;margin-top:18px;padding-top:12px;border-top:1px solid var(--line);max-width:140mm}} .s-meta b{{display:block;font-size:17px;font-weight:700;color:var(--ac)}} .s-meta span{{font-size:8.5px;color:var(--tx3)}}
.a4p{{width:96mm;height:136mm;margin:0 auto;background:#fff;border-radius:6px;box-shadow:0 0 0 1px rgba(11,12,19,.1),0 18px 40px -24px rgba(11,12,19,.4);padding:12mm 10mm;position:relative}}
.a4h{{display:flex;justify-content:space-between;align-items:center;margin-bottom:14mm}} .a4h span{{font-size:7px;color:var(--tx3)}}
.a4p h3{{font-size:19px;line-height:1.08;font-weight:800;letter-spacing:-.035em;margin-bottom:8px}} .a4p>p{{font-size:8.5px;line-height:1.6;color:var(--tx2)}}
.a4box{{margin-top:10px;border-radius:10px;padding:10px 12px;background:{H['teal']};color:{H['azul-escuro']}}} .a4box .sn{{color:{H['azul-escuro']}!important;font-size:20px!important;display:block}} .a4box span{{font-size:8px}}
.a4f{{position:absolute;left:10mm;right:10mm;bottom:8mm;display:flex;justify-content:space-between;align-items:flex-end;font-size:7px;color:var(--tx3);border-top:1px solid var(--line);padding-top:4px}}
.slides .sl{{aspect-ratio:16/9;border-radius:12px;padding:22px 26px;position:relative;border:1px solid var(--line)}} .sl.d{{background:{H['azul-escuro']};--ac:{H['teal']};color:#fff}} .sl.l{{background:#fff;--ac:{H['teal-tinta']};color:{H['azul-escuro']};box-shadow:inset 0 0 0 1px rgba(11,12,19,.12)}}
.sl h3{{font-size:28px;line-height:1.06;font-weight:800;letter-spacing:-.035em;max-width:85%}} .slf{{position:absolute;left:26px;right:26px;bottom:16px;display:flex;justify-content:space-between;align-items:center;font-size:8px;opacity:.7}}
.posts{{display:grid;grid-template-columns:repeat(3,38mm) 1fr;gap:6mm;align-items:start}} .po{{aspect-ratio:4/5;border-radius:10px;padding:12px;display:flex;flex-direction:column;justify-content:space-between}} .po h3{{font-size:12.5px;line-height:1.12;font-weight:800;letter-spacing:-.03em}}
.po.d{{background:{H['azul-escuro']};color:#fff;--ac:{H['teal']};border:1px solid rgba(255,255,255,.1)}} .po.t{{background:{H['teal']};color:{H['azul-escuro']}}} .po.t .eb{{color:{H['azul-escuro']}}} .po.l{{background:#fff;color:{H['azul-escuro']};--ac:{H['teal-tinta']};box-shadow:inset 0 0 0 1px rgba(11,12,19,.12)}}
.ptxt p{{margin-bottom:8px}}
.check ul{{list-style:none;padding:0}} .check li{{display:flex;gap:10px;align-items:flex-start;font-size:13.5px;line-height:1.5;color:var(--tx2);padding:9px 0;border-top:1px solid var(--line)}} .check li svg{{color:var(--ac);flex:none;margin-top:2px}}
.back{{position:relative;height:100%;display:flex;flex-direction:column;justify-content:center;padding:0 24mm}} .statement{{font-size:40px;line-height:1.1;font-weight:800;letter-spacing:-.035em;margin:20mm 0 10mm;max-width:210mm}} .dogb{{position:absolute;right:22mm;bottom:18mm}}
'''

def render():
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Agência Tweed · Manual de Identidade Visual v2.0</title>',
           f'<style>{CSS}</style></head><body>']
    for i, (ch, body, theme, cls) in enumerate(pages, 1):
        hf = '' if 'p-cover' in cls else (f'<div class="hdr"><span>Agência Tweed · Manual de Identidade Visual</span><span>{ch}</span></div>'
                                          f'<div class="ftr"><span>{VERSION}</span><span>{i:02d}</span></div>')
        out.append(f'<section class="page {"light" if theme == "light" else ""} {cls}">{hf}{body}</section>')
    out.append('</body></html>')
    open(OUT, 'w').write('\n'.join(out))
    print(OUT, len(pages), 'páginas')

if __name__ == '__main__':
    render()
