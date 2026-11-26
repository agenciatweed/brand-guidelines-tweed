# Agência Tweed · gera tokens/tweed-tokens.css e tokens/tweed-tokens.json a partir de pal.py
import json, os, re
from pal import C, H, SEM, TYPE

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'tokens')

SPACE = [
    ('gutter', '4rem', 'clamp(1.25rem, 5vw, 4rem)', 'Margem lateral da página e do container.'),
    ('secao', '7rem', 'clamp(4.25rem, 9.8vh, 7rem)', 'Respiro vertical de seção (metade abaixo de 720 px).'),
    ('secao-alta', '9.75rem', 'clamp(5.5rem, 14vh, 9.75rem)', 'Seção alta: abertura de capítulo, declaração.'),
    ('cabeca', '4.5rem', 'clamp(2.5rem, 6vw, 4.5rem)', 'Do bloco de título (eyebrow + h2 + lead) ao conteúdo.'),
    ('grade', '1.5rem', 'clamp(1rem, 2vw, 1.5rem)', 'Vão entre cards e colunas.'),
    ('card', '2rem', 'clamp(1.5rem, 2.5vw, 2rem)', 'Padding interno de card.'),
    ('1', '0.25rem', '0.25rem', 'Ajuste fino: ícone e rótulo colados.'),
    ('2', '0.5rem', '0.5rem', 'Entre ícone e texto, entre título e subtítulo.'),
    ('3', '0.875rem', '0.875rem', 'Entre botões lado a lado.'),
    ('4', '1rem', '1rem', 'Entre eyebrow e título; distância da navbar à borda.'),
    ('6', '1.5rem', '1.5rem', 'Entre título e lead.'),
    ('8', '2rem', '2rem', 'Entre blocos de texto.'),
    ('alvo', '44px', '44px', 'Alvo mínimo de toque e clique.'),
    ('largura-max', '1600px', '1600px', 'Largura máxima do container.'),
]
RADIUS = [
    ('foco', '4px', 'Anel de foco e selos mínimos.'),
    ('sm', '8px', 'Links da navbar, botões de ícone pequenos.'),
    ('md', '10px', 'Quadro de ícone, skip link, imagens dentro de texto.'),
    ('nav', '14px', 'Navbar flutuante.'),
    ('foto', '16px', 'Fotografia (fundadores, cases).'),
    ('card', '18px', 'Cards, números, faixa de marcas, citação.'),
    ('depoimento', '24px', 'Card de depoimento.'),
    ('pill', '999px', 'Botões, chips, setas de navegação. Botão é sempre pílula.'),
]
SHADOW = [
    ('sombra-card', 'inset 0 -16px 24px -4px rgba(255, 255, 255, 0.1)', 'inset 0 -16px 24px -4px rgba(0, 112, 77, 0.06)', 'Luz interna que sobe da base do card tingido.'),
    ('sombra-depoimento', '0 24px 48px -28px rgba(0, 0, 0, 0.9)', '0 24px 48px -28px rgba(11, 12, 19, 0.35)', 'Sombra do card de depoimento (único card com sombra externa).'),
    ('sombra-botao-hover', '0 0 0 6px rgba(8, 255, 177, 0.14)', '0 0 0 6px rgba(0, 112, 77, 0.14)', 'Anel suave do botão primário em hover.'),
]
GRADIENT = [
    ('card-tingido-escuro', 'radial-gradient(at 88% 40%, #0b0c13 0px, transparent 85%), radial-gradient(at 49% 30%, #0b0c13 0px, transparent 85%), radial-gradient(at 14% 26%, #0b0c13 0px, transparent 85%), radial-gradient(at 0% 64%, hsla(161, 100%, 52%, 0.34) 0px, transparent 85%), radial-gradient(at 41% 94%, hsla(161, 100%, 80%, 0.24) 0px, transparent 85%), radial-gradient(at 100% 99%, hsla(172, 95%, 45%, 0.38) 0px, transparent 85%)', 'Superfície do card no escuro (sobre background-color Azul-Escuro). Topo limpo para leitura, luz teal na base.'),
    ('card-tingido-claro', 'radial-gradient(at 88% 40%, #ffffff 0px, transparent 85%), radial-gradient(at 49% 30%, #ffffff 0px, transparent 85%), radial-gradient(at 14% 26%, #ffffff 0px, transparent 85%), radial-gradient(at 0% 64%, hsla(161, 100%, 52%, 0.22) 0px, transparent 85%), radial-gradient(at 41% 94%, hsla(161, 100%, 80%, 0.3) 0px, transparent 85%), radial-gradient(at 100% 99%, hsla(172, 95%, 45%, 0.24) 0px, transparent 85%)', 'Proposta. Mesma receita no claro (sobre background-color Branco): menta na base, Azul-Escuro no texto.'),
    ('halo-botao', 'radial-gradient(60% 100% at 50% 50%, rgba(8, 255, 177, 0.55), rgba(8, 255, 177, 0.28) 35%, transparent 70%)', 'Halo que acende abaixo do botão no hover (blur 11 px).'),
    ('brilho-hero', 'radial-gradient(60% 45% at 78% 74%, rgba(8, 255, 177, 0.14), transparent 70%), radial-gradient(45% 40% at 46% 28%, rgba(8, 255, 177, 0.08), transparent 72%)', 'Luz de fundo do hero quando a animação não carrega.'),
    ('veu-hero', 'linear-gradient(100deg, #0b0c13 0%, rgba(11, 12, 19, 0.82) 30%, rgba(11, 12, 19, 0.35) 52%, rgba(11, 12, 19, 0) 72%)', 'Véu que garante o contraste da headline sobre imagem ou animação à direita.'),
]
MOTION = [
    ('ease', 'cubic-bezier(0.16, 1, 0.3, 1)', 'Curva única de movimento.'),
    ('dur', '0.7s', 'Entrada de blocos (reveal).'),
    ('dur-estado', '0.3s', 'Hover, foco e troca de cor.'),
]

def css_val(v):
    m = re.fullmatch(r'\{(.+)\}', v)
    return f'var(--{m.group(1)})' if m else v

def build_css():
    o = ['/* Agência Tweed · tokens de design · gerado por fonte-editavel/build/tokens.py — não edite à mão */',
         '/* Tema escuro é o padrão (:root). Tema claro: [data-theme="claro"] ou .tweed-claro em qualquer contêiner. */', '']
    for name, f, w, st in [('inter-18pt-regular', 'Inter', '400', 'normal'), ('inter-24pt-medium', 'Inter', '500 600', 'normal'),
                           ('inter-28pt-bold', 'Inter', '700 800', 'normal'), ('inter-28pt-bolditalic', 'Inter', '700 800', 'italic')]:
        o.append(f"@font-face{{font-family:'{f}';src:url('../tipografia/web/{name}.woff2') format('woff2');font-weight:{w};font-style:{st};font-display:swap}}")
    o += ['', ':root, [data-theme="escuro"], .tweed-escuro {', '  /* paleta */']
    for k, (n, h, orig, g, u) in C.items():
        o.append(f'  --tweed-{k}: {h};')
    o.append('  /* tema */')
    for n, d, c, u in SEM:
        o.append(f'  --tweed-{n}: {css_val(d)};')
    for n, d, c, u in SHADOW:
        o.append(f'  --tweed-{n}: {d};')
    o.append('  --tweed-card-tingido: var(--tweed-card-tingido-escuro);')
    o += ['  color-scheme: dark;', '}', '', '[data-theme="claro"], .tweed-claro {']
    for n, d, c, u in SEM:
        o.append(f'  --tweed-{n}: {css_val(c)};')
    for n, d, c, u in SHADOW:
        o.append(f'  --tweed-{n}: {c};')
    o.append('  --tweed-card-tingido: var(--tweed-card-tingido-claro);')
    o += ['  color-scheme: light;', '}', '', ':root {',
          "  --tweed-font: 'Inter', ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;"]
    for t in TYPE:
        o.append(f'  --tweed-fs-{t[0]}: {t[2] if t[2].startswith("clamp") else t[1]};')
    for n, v, fl, u in SPACE:
        o.append(f'  --tweed-space-{n}: {fl};')
    for n, v, u in RADIUS:
        o.append(f'  --tweed-radius-{n}: {v};')
    for n, v, u in GRADIENT:
        o.append(f'  --tweed-{n}: {v};')
    for n, v, u in MOTION:
        o.append(f'  --tweed-{n}: {v};')
    o += ['}', '']
    o.append('/* estilos de texto prontos */')
    for n, size, cl, lh, w, ls, u, s in TYPE:
        extra = ';text-transform:uppercase' if n == 'eyebrow' else ''
        extra += ';font-variant-numeric:tabular-nums' if n == 'numero' else ''
        o.append(f'.tweed-{n}{{font-family:var(--tweed-font);font-size:var(--tweed-fs-{n});line-height:{lh};font-weight:{w};letter-spacing:{ls}{extra}}}')
    o.append('.tweed-em, .tweed em{font-style:italic;color:var(--tweed-acento)}')
    return '\n'.join(o) + '\n'

def build_json():
    j = {
        'name': 'Agência Tweed', 'version': '2.0',
        'themes': ['escuro', 'claro'],
        'color': {
            'palette': {k: {'name': n, 'hex': h, 'origin': orig, 'group': g, 'usage': u} for k, (n, h, orig, g, u) in C.items()},
            'semantic': {n: {'escuro': d, 'claro': c, 'usage': u} for n, d, c, u in SEM},
        },
        'type': {'family': 'Inter', 'files': {
            '400': 'tipografia/web/inter-18pt-regular.woff2', '500-600': 'tipografia/web/inter-24pt-medium.woff2',
            '700-800': 'tipografia/web/inter-28pt-bold.woff2', '700-800 italic': 'tipografia/web/inter-28pt-bolditalic.woff2'},
            'styles': {t[0]: {'fontSize': t[1], 'fluid': t[2], 'lineHeight': t[3], 'fontWeight': t[4], 'letterSpacing': t[5], 'usage': t[6]} for t in TYPE}},
        'spacing': {n: {'value': v, 'fluid': fl, 'usage': u} for n, v, fl, u in SPACE},
        'radius': {n: {'value': v, 'usage': u} for n, v, u in RADIUS},
        'shadow': {n: {'escuro': d, 'claro': c, 'usage': u} for n, d, c, u in SHADOW},
        'gradient': {n: {'value': v, 'usage': u} for n, v, u in GRADIENT},
        'motion': {n: {'value': v, 'usage': u} for n, v, u in MOTION},
    }
    return json.dumps(j, ensure_ascii=False, indent=2) + '\n'

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, 'tweed-tokens.css'), 'w').write(build_css())
    open(os.path.join(OUT, 'tweed-tokens.json'), 'w').write(build_json())
    print('ok')
