# Tipografia

← [Voltar ao README principal](../README.md) · Capítulo 04 do [manual](../manual/Manual_de_Identidade_Visual_Tweed_v2.0.pdf)

## Fonte principal

**Inter**, e só Inter. A Inter 4 tem cortes ópticos desenhados para cada faixa de tamanho; a Tweed usa três. “18pt”, “24pt” e “28pt” são os nomes dos cortes, não tamanhos de corpo.

| Peso no CSS | Arquivo | Uso |
|---|---|---|
| 400 | Inter 18pt Regular · Inter 18pt Italic | Corpo de texto, lead, legendas, textos menores |
| 500 · 600 | Inter 24pt Medium · Inter 24pt Medium Italic | Botões, navegação, eyebrow, rótulos de interface |
| 700 · 800 | Inter 28pt Bold | Headlines, títulos, números de prova, citações |
| 700 · 800 itálico | Inter 28pt Bold Italic | A palavra em ênfase dentro de um título |

> **Mudança em relação à v1.0.** O guia original indicava a Inter 24pt Medium para o texto corpo. O site em produção usa a Inter 18pt Regular no corpo e reserva a Medium para interface, o que melhora a leitura em textos longos. A v2.0 adota a prática do site.

## Arquivos

**TTF completos** (documentos, apresentações, PDF):

- [Inter 28pt Bold](./inter-28pt-bold.ttf) · [Inter 28pt Bold Italic](./inter-28pt-bolditalic.ttf)
- [Inter 24pt Medium](./inter-24pt-medium.ttf) · [Inter 24pt Medium Italic](./inter-24pt-mediumitalic.ttf)
- [Inter 18pt Regular](./inter-18pt-regular.ttf) · [Inter 18pt Italic](./inter-18pt-italic.ttf)

**WOFF2 do site** em [`web/`](web/): as quatro faces que o site carrega, em subconjunto Latin, Latin-1, Latin Extended-A e pontuação editorial (492 glifos, ~20 KB cada).

```css
@font-face{font-family:'Inter';src:url('web/inter-18pt-regular.woff2') format('woff2');font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:'Inter';src:url('web/inter-24pt-medium.woff2') format('woff2');font-weight:500 600;font-style:normal;font-display:swap}
@font-face{font-family:'Inter';src:url('web/inter-28pt-bold.woff2') format('woff2');font-weight:700 800;font-style:normal;font-display:swap}
@font-face{font-family:'Inter';src:url('web/inter-28pt-bolditalic.woff2') format('woff2');font-weight:700 800;font-style:italic;font-display:swap}
body{font-synthesis:none}   /* nunca falsificar negrito ou itálico */
```

As faixas de peso (`500 600`, `700 800`) dizem quais pesos cada arquivo cobre; sem elas o navegador sintetizaria negrito falso nos passos 600 e 800. O [`tokens/tweed-tokens.css`](../tokens/tweed-tokens.css) já traz essas declarações.

## Hierarquia digital (Site)

1 rem = 16 px. O valor de referência é o teto do `clamp()`.

| Estilo | Peso | Tamanho | Fluido | Entrelinha | Tracking | Uso |
|---|---|---|---|---|---|---|
| `mega` | 800 | 128 px | `clamp(2.75rem, 8.5vw, 8rem)` | 0,8 | −0,05em | Numeral de capítulo, a 5,5% de opacidade, atrás do conteúdo |
| `display` | 800 | 80 px | `clamp(2.25rem, 6.2vw, 5rem)` | 1,02 | −0,045em | H1 do hero e capa. Uma vez por página |
| `h2` | 800 | 56 px | `clamp(1.875rem, 4.6vw, 3.5rem)` | 1,06 | −0,035em | Título de seção ou de slide |
| `statement` | 800 | 52 px | `clamp(1.75rem, 4.4vw, 3.25rem)` | 1,1 | −0,035em | Declaração gigante, com a palavra-chave em itálico |
| `numero` | 800 | 44 px | `clamp(1.875rem, 3.6vw, 2.75rem)` | 1,1 | −0,04em | Números de prova, em acento e algarismos tabulares |
| `citacao` | 700 | 32 px | `clamp(1.375rem, 2.8vw, 2rem)` | 1,2 | −0,03em | Citação dos fundadores |
| `h3` | 700 | 26 px | `clamp(1.25rem, 2.2vw, 1.625rem)` | 1,25 | −0,02em | Título de card, etapa, bloco |
| `lead` | 400 | 22 px | `clamp(1.0625rem, 1.7vw, 1.375rem)` | 1,65 | 0 | Lead de seção |
| `body` | 400 | 17 px | 16 px abaixo de 720 px | 1,65 | 0 | Corpo |
| `small` | 400 | 15 px | — | 1,65 | 0 | Texto de card, etapa, chip, rodapé |
| `botao` | 600 | 15 px | 17 px no botão grande | 1,2 | +0,01em | Rótulo de botão e navegação |
| `eyebrow` | 600 | 13 px | — | 1,2 | +0,16em | Caixa alta, cor de acento |
| `caption` | 400 | 13 px | — | 1,5 | +0,04em | Legendas e metadados |

## Apresentações, documentos e posts (Proposta)

| Estilo | Slide 1920 × 1080 | Documento A4 | Post 1080 × 1350 |
|---|---|---|---|
| Display · 800 | 112–128 px | 36–44 pt | 88–104 px |
| H2 · 800 | 72–80 px | 24–28 pt | 64–72 px |
| H3 · 700 | 40 px | 14–16 pt | 40 px |
| Lead · 400 | 32 px | 12–13 pt | 32 px |
| Corpo · 400 | 26–28 px | 10,5–11 pt | 28 px |
| Eyebrow · 600 | 20 px · +0,16em | 8 pt · +0,16em | 22 px · +0,16em |

## Regras

- **Ênfase em título:** itálico na cor de acento (Teal Tweed no escuro, Teal Tinta no claro). Uma ênfase por título.
- **Ênfase no corpo:** negrito na cor do texto, sem itálico colorido.
- Títulos em caixa de frase; caixa alta só no eyebrow.
- Quanto maior o texto, mais apertado o tracking (já embutido nos estilos).
- Não use outros pesos nem outras famílias.

## Fallback (Google Fonts)

Sem os arquivos, use a Inter variável do Google Fonts com `font-optical-sizing: auto`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">
```

```css
.texto { font-family: "Inter", sans-serif; font-optical-sizing: auto; }
```
