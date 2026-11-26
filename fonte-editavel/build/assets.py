# Agência Tweed · gera logotipos (SVG, PNG 2000 px, PDF RGB), amostras de cor,
# versões escuras da faixa de marcas e prévias do README.
# Dependências: rsvg-convert (librsvg) e Pillow.
import os, re, subprocess
from PIL import Image
from pal import C, H, rgb

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
LOGOS = os.path.join(ROOT, 'logos')
SRC = os.path.join(LOGOS, 'logo_tweed_teal.svg')   # vetor original (Illustrator)
D = re.search(r'<path class="st1" d="([^"]+)"', open(SRC).read()).group(1)
VB = '0 0 651.97 204.02'

def logo_svg(ink):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB}" role="img" aria-label="Agência Tweed">'
            f'<title>Agência Tweed</title><path fill="{ink}" d="{D}"/></svg>\n')

VERSIONS = {'teal': H['teal'], 'azul_escuro': H['azul-escuro'], 'branco': H['branco']}

def run(*a):
    subprocess.run(a, check=True)

def main():
    # SVG novo só para a versão proposta; teal e azul-escuro continuam sendo os arquivos originais
    open(os.path.join(LOGOS, 'logo_tweed_branco.svg'), 'w').write(logo_svg(H['branco']))
    for k in VERSIONS:
        svg = os.path.join(LOGOS, f'logo_tweed_{k}.svg')
        run('rsvg-convert', '-w', '2000', svg, '-o', os.path.join(LOGOS, 'png', f'logo_tweed_{k}_2000px.png'))
        run('rsvg-convert', '-f', 'pdf', svg, '-o', os.path.join(LOGOS, 'pdf', f'logo_tweed_{k}_RGB.pdf'))
    # PNG de 700 px da versão branca, no mesmo padrão das outras duas
    run('rsvg-convert', '-w', '700', os.path.join(LOGOS, 'logo_tweed_branco.svg'), '-o', os.path.join(LOGOS, 'logo_tweed_branco.png'))
    # avatar de perfil (proposta): quadrado 512 com o logotipo centralizado
    avt = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="112" fill="{H["azul-escuro"]}"/>'
           f'<g transform="translate(56 {256 - 400 / 3.1956 / 2:.2f}) scale({400 / 651.97:.5f})"><path fill="{H["teal"]}" d="{D}"/></g></svg>\n')
    open(os.path.join(LOGOS, 'avatar_tweed.svg'), 'w').write(avt)
    run('rsvg-convert', '-w', '512', os.path.join(LOGOS, 'avatar_tweed.svg'), '-o', os.path.join(LOGOS, 'png', 'avatar_tweed_512px.png'))

    # amostras de cor
    am = os.path.join(ROOT, 'cores', 'amostras')
    os.makedirs(am, exist_ok=True)
    for k, (n, h, *_ ) in C.items():
        edge = '<rect x="0.5" y="0.5" width="159" height="99" rx="11.5" fill="none" stroke="#0b0c13" stroke-opacity=".12"/>' if k in ('branco', 'nevoa', 'gelo') else ''
        open(os.path.join(am, f'{k}.svg'), 'w').write(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="160" height="100" viewBox="0 0 160 100"><rect width="160" height="100" rx="12" fill="{h}"/>{edge}</svg>\n')

    # faixa de marcas em Azul-Escuro, para fundos claros (mesma arte, só a tinta muda)
    comp = os.path.join(ROOT, 'componentes')
    for f in ('marcas-atendidas', 'marcas-mobile'):
        im = Image.open(os.path.join(comp, f + '.png')).convert('RGBA')
        r, g, b = rgb(H['azul-escuro'])
        alpha = im.getchannel('A')
        out = Image.new('RGBA', im.size, (r, g, b, 0))
        out.putalpha(alpha)
        out.save(os.path.join(comp, f + '-escuro.png'), optimize=True)

    # prévias do README (logotipo sobre os fundos permitidos)
    pv = os.path.join(ROOT, 'assets', 'previews')
    os.makedirs(pv, exist_ok=True)
    for name, ink, bg in [('logo-teal-azul-escuro', H['teal'], H['azul-escuro']), ('logo-azul-escuro-branco', H['azul-escuro'], H['branco']),
                          ('logo-azul-escuro-teal', H['azul-escuro'], H['teal']), ('logo-branco-foto', H['branco'], '#2a2f3a'),
                          ('logo-azul-escuro-nevoa', H['azul-escuro'], H['nevoa'])]:
        edge = '<rect x="0.5" y="0.5" width="399" height="219" rx="17.5" fill="none" stroke="#0b0c13" stroke-opacity=".12"/>' if bg in (H['branco'], H['nevoa']) else ''
        open(os.path.join(pv, name + '.svg'), 'w').write(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="220" viewBox="0 0 400 220"><rect width="400" height="220" rx="18" fill="{bg}"/>{edge}'
            f'<g transform="translate(90 {110 - 220 / 3.1956 / 2:.2f}) scale({220 / 651.97:.5f})"><path fill="{ink}" d="{D}"/></g></svg>\n')
    print('ok')

if __name__ == '__main__':
    main()
