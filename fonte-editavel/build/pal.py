# Agência Tweed · paleta, temas e contraste (fonte única dos tokens e do manual)
# Origem: "Original" = guia de marca v1; "Site" = agenciatweed.com.br (CSS de produção, nov/2026);
# "Proposta" = criada nesta edição para o tema claro.

def hx(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def rgb(h):
    return hx(h)

def L(h):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = hx(h)
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)

def cr(a, b):
    la, lb = sorted([L(a), L(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)

def fmt(x):
    return f'{x:.2f}'.replace('.', ',')

def cmyk(h):
    r, g, b = [v / 255 for v in hx(h)]
    k = 1 - max(r, g, b)
    if k >= 1:
        return '0 · 0 · 0 · 100'
    c, m, y = [(1 - v - k) / (1 - k) for v in (r, g, b)]
    return ' · '.join(str(round(v * 100)) for v in (c, m, y, k))

# chave: (nome, hex, origem, grupo, função)
C = {
    'teal':          ('Teal Tweed',     '#08ffb1', 'Original', 'institucional', 'O acento da marca. Logotipo, headlines de destaque, CTAs, números e o que precisa chamar atenção sobre fundo escuro. Nunca texto sobre fundo claro.'),
    'azul-escuro':   ('Azul-Escuro',    '#0b0c13', 'Original', 'institucional', 'Fundo padrão da marca e espaço negativo. No tema claro, é a cor do texto e do logotipo.'),
    'branco':        ('Branco',         '#ffffff', 'Original', 'institucional', 'Texto sobre Azul-Escuro. No tema claro, é o fundo da página.'),
    'noite':         ('Noite',          '#11131c', 'Site',     'escuro',        'Superfície elevada sobre Azul-Escuro: chips, citações, campos.'),
    'noite-alta':    ('Noite Alta',     '#171a25', 'Site',     'escuro',        'Segundo degrau no escuro: hover de superfícies, áreas internas.'),
    'prata':         ('Prata',          '#d3d7df', 'Site',     'escuro',        'Texto secundário sobre superfícies tingidas de teal (cards, faixas com luz).'),
    'cinza':         ('Cinza',          '#a7acb9', 'Site',     'escuro',        'Texto secundário sobre Azul-Escuro: leads, parágrafos de apoio, links do rodapé.'),
    'cinza-fraco':   ('Cinza Fraco',    '#868da1', 'Site',     'escuro',        'Texto terciário: legendas, metadados, números de etapa em repouso.'),
    'teal-luz':      ('Teal Luz',       '#5cffcb', 'Site',     'escuro',        'Hover do botão teal. Só estado, nunca cor de peça.'),
    'nevoa':         ('Névoa',          '#f4f5f8', 'Proposta', 'claro',         'Superfície elevada no claro: cards, citações, blocos sobre Branco.'),
    'gelo':          ('Gelo',           '#eceef3', 'Proposta', 'claro',         'Segundo degrau no claro: faixas, tabelas, rodapé de documento.'),
    'grafite':       ('Grafite',        '#4a4f60', 'Proposta', 'claro',         'Texto secundário sobre Branco, Névoa e Gelo.'),
    'grafite-fraco': ('Grafite Fraco',  '#5f6578', 'Proposta', 'claro',         'Texto terciário no claro: legendas, metadados, notas.'),
    'teal-tinta':    ('Teal Tinta',     '#00704d', 'Proposta', 'claro',         'O teal legível no claro: eyebrow, ênfase em itálico, links, números de destaque e foco.'),
}
H = {k: v[1] for k, v in C.items()}

# tokens semânticos por tema: (nome, escuro, claro, uso)
SEM = [
    ('superficie',            '{tweed-azul-escuro}', '{tweed-branco}',        'Fundo da página no tema.'),
    ('superficie-elevada',    '{tweed-noite}',       '{tweed-nevoa}',         'Card simples, citação, chip, campo.'),
    ('superficie-elevada-2',  '{tweed-noite-alta}',  '{tweed-gelo}',          'Segundo degrau: faixas, tabelas, hover de superfície.'),
    ('texto',                 '{tweed-branco}',      '{tweed-azul-escuro}',   'Texto principal e títulos (19,51:1 sobre a superfície nos dois temas).'),
    ('texto-suave',           '{tweed-cinza}',       '{tweed-grafite}',       'Leads, parágrafos de apoio, links de navegação (8,59:1 no escuro, 8,14:1 no claro).'),
    ('texto-fraco',           '{tweed-cinza-fraco}', '{tweed-grafite-fraco}', 'Legendas, metadados, números em repouso (5,89:1 no escuro, 5,80:1 no claro).'),
    ('texto-tingido',         '{tweed-prata}',       '{tweed-grafite}',       'Texto secundário dentro de cards tingidos de teal.'),
    ('acento',                '{tweed-teal}',        '{tweed-teal-tinta}',    'Acento como TEXTO: eyebrow, ênfase em itálico, links, números de destaque (14,82:1 no escuro, 6,13:1 no claro).'),
    ('acento-forte',          '{tweed-teal}',        '{tweed-teal}',          'Acento como SUPERFÍCIE: blocos, marcador de seleção, faixas. Teal nos dois temas; sobre ele, só Azul-Escuro.'),
    ('acento-lavado',         'rgba(8, 255, 177, 0.08)',  'rgba(0, 112, 77, 0.08)',  'Fundo do quadro de ícone e realces suaves.'),
    ('acento-borda',          'rgba(8, 255, 177, 0.24)',  'rgba(0, 112, 77, 0.28)',  'Borda de destaque: navbar rolada, chip em hover, card simples ativo.'),
    ('botao-primario',        '{tweed-teal}',        '{tweed-azul-escuro}',   'Fundo do botão primário: teal no escuro; Azul-Escuro no claro.'),
    ('botao-primario-texto',  '{tweed-azul-escuro}', '{tweed-teal}',          'Rótulo do botão primário: Azul-Escuro sobre teal, teal sobre Azul-Escuro (14,82:1 nos dois).'),
    ('botao-primario-hover',  '{tweed-teal-luz}',    '{tweed-noite-alta}',    'Fundo do botão primário em hover.'),
    ('botao-ghost-fundo',     'rgba(11, 12, 19, 0.55)', 'rgba(255, 255, 255, 0.6)', 'Vidro do botão ghost (com backdrop-filter).'),
    ('fio',                   'rgba(255, 255, 255, 0.09)', 'rgba(11, 12, 19, 0.1)',  'Fio de 1 px: bordas, divisórias de etapa, rodapé.'),
    ('fio-suave',             'rgba(255, 255, 255, 0.055)', 'rgba(11, 12, 19, 0.06)', 'Fio leve: grade do hero, divisórias internas.'),
    ('fio-forte',             'rgba(255, 255, 255, 0.28)', 'rgba(11, 12, 19, 0.28)', 'Contorno do botão ghost, marcador da trilha.'),
    ('contorno-campo',        'rgba(255, 255, 255, 0.4)',  'rgba(11, 12, 19, 0.5)',   'Borda de campo de formulário: 3:1 ou mais nos dois temas.'),
    ('foco',                  '{tweed-teal}',        '{tweed-teal-tinta}',    'Anel de foco: 2 px sólido, afastado 3 px.'),
    ('logo',                  '{tweed-teal}',        '{tweed-azul-escuro}',   'Tinta do logotipo no tema: teal no escuro, Azul-Escuro no claro.'),
    ('vidro',                 'rgba(11, 12, 19, 0.72)', 'rgba(255, 255, 255, 0.8)', 'Navbar flutuante (com blur 14 px).'),
    ('anel',                  'rgba(8, 255, 177, 0.95)', 'rgba(0, 112, 77, 0.9)',  'Luz que gira na borda dos cards tingidos.'),
    ('anel-base',             'rgba(255, 255, 255, 0.13)', 'rgba(11, 12, 19, 0.1)', 'Trecho apagado do anel de borda.'),
    ('numero-capitulo',       'rgba(255, 255, 255, 0.055)', 'rgba(11, 12, 19, 0.05)', 'Numeral gigante de capítulo, atrás do conteúdo.'),
]

# pares para a tabela de contraste
PAIRS = [
    ('Branco', 'Azul-Escuro', H['branco'], H['azul-escuro']),
    ('Teal Tweed', 'Azul-Escuro', H['teal'], H['azul-escuro']),
    ('Azul-Escuro (rótulo)', 'Teal Tweed', H['azul-escuro'], H['teal']),
    ('Prata', 'Azul-Escuro', H['prata'], H['azul-escuro']),
    ('Cinza', 'Azul-Escuro', H['cinza'], H['azul-escuro']),
    ('Cinza Fraco', 'Azul-Escuro', H['cinza-fraco'], H['azul-escuro']),
    ('Cinza', 'Noite Alta', H['cinza'], H['noite-alta']),
    ('Azul-Escuro', 'Branco', H['azul-escuro'], H['branco']),
    ('Grafite', 'Branco', H['grafite'], H['branco']),
    ('Grafite', 'Gelo', H['grafite'], H['gelo']),
    ('Grafite Fraco', 'Névoa', H['grafite-fraco'], H['nevoa']),
    ('Teal Tinta', 'Branco', H['teal-tinta'], H['branco']),
    ('Teal Tinta', 'Gelo', H['teal-tinta'], H['gelo']),
    ('Teal Tweed', 'Branco', H['teal'], H['branco']),
    ('Teal Tweed', 'Névoa', H['teal'], H['nevoa']),
]

# Tipografia (valores do site; o token é o teto do clamp)
TYPE = [
    # nome, tamanho, clamp, lh, peso, tracking, uso, amostra
    ('mega',      '8rem',      'clamp(2.75rem, 8.5vw, 8rem)',      0.8,  800, '-0.05em',  'Numeral de capítulo, atrás do conteúdo, a 5,5% de opacidade.', '03'),
    ('display',   '5rem',      'clamp(2.25rem, 6.2vw, 5rem)',      1.02, 800, '-0.045em', 'H1 do hero e título de capa. Uma vez por página.', 'Sua empresa cresceu.'),
    ('h2',        '3.5rem',    'clamp(1.875rem, 4.6vw, 3.5rem)',   1.06, 800, '-0.035em', 'Título de seção ou de slide.', 'O problema quase nunca é o marketing.'),
    ('statement', '3.25rem',   'clamp(1.75rem, 4.4vw, 3.25rem)',   1.1,  800, '-0.035em', 'Declaração gigante (pull statement), com a palavra-chave em itálico teal.', 'Marcas não crescem por barulho.'),
    ('numero',    '2.75rem',   'clamp(1.875rem, 3.6vw, 2.75rem)',  1.1,  800, '-0.04em',  'Número de prova (+500, 30, 1), sempre em acento e com algarismos tabulares.', '+500'),
    ('citacao',   '2rem',      'clamp(1.375rem, 2.8vw, 2rem)',     1.2,  700, '-0.03em',  'Citação dos fundadores e frases de assinatura.', 'Somos pequenos por escolha.'),
    ('h3',        '1.625rem',  'clamp(1.25rem, 2.2vw, 1.625rem)',  1.25, 700, '-0.02em',  'Título de card, etapa e bloco.', 'Diagnóstico de percepção'),
    ('lead',      '1.375rem',  'clamp(1.0625rem, 1.7vw, 1.375rem)', 1.65, 400, '0',       'Lead de seção, logo abaixo do título.', 'Estratégia, design e execução para marcas que precisam ser percebidas à altura do que entregam.'),
    ('body',      '1.0625rem', '1.0625rem (1rem abaixo de 720 px)', 1.65, 400, '0',       'Corpo de texto.', 'Cuidamos de tudo para que sua marca apareça com coerência em todos os lugares.'),
    ('small',     '0.9375rem', '0.9375rem',                         1.65, 400, '0',       'Texto de card, etapa, rodapé e chip.', 'Uma equipe só, um interlocutor só.'),
    ('botao',     '0.9375rem', '0.9375rem (1.0625rem no botão grande)', 1.2, 600, '0.01em', 'Rótulo de botão e link de navegação. Nunca quebra linha.', 'Começar uma conversa'),
    ('eyebrow',   '0.8125rem', '0.8125rem',                         1.2,  600, '0.16em',  'Rótulo em caixa alta acima do título, em acento.', 'Capítulo 01 · O diagnóstico'),
    ('caption',   '0.8125rem', '0.8125rem',                         1.5,  400, '0.04em',  'Legenda de número, metadado, créditos.', 'marcas atendidas'),
]
