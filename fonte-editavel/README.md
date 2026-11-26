# Fonte editável do manual

← [Voltar ao README principal](../README.md)

O manual foi diagramado em HTML/CSS e exportado para PDF pelo Chromium (Playwright). Esta pasta contém o HTML-fonte e os scripts que geram o manual, os tokens, os logotipos derivados, as amostras de cor e as prévias.

| Caminho | Conteúdo |
|---|---|
| [`Manual_de_Identidade_Visual_Tweed.html`](Manual_de_Identidade_Visual_Tweed.html) | HTML-fonte completo (32 páginas A4 paisagem). Referencia `../tipografia` e `../componentes` |
| [`build/pal.py`](build/pal.py) | Fonte única: paleta, origem de cada cor, tokens de tema, pares de contraste e escala tipográfica |
| [`build/tokens.py`](build/tokens.py) | Gera `tokens/tweed-tokens.css` e `tokens/tweed-tokens.json` |
| [`build/assets.py`](build/assets.py) | Gera logotipo branco, PNG de 2000 px, PDF RGB, avatar, amostras de cor, faixa de marcas em Azul-Escuro e prévias do README |
| [`build/manual.py`](build/manual.py) | Gera o HTML do manual |
| [`build/print.js`](build/print.js) | Imprime o HTML em PDF e captura cada página em PNG |

## Regenerar

Dependências: Python 3 com Pillow, `rsvg-convert` (librsvg), Node.js com `playwright` e um Chromium.

```bash
cd fonte-editavel
python3 build/assets.py
python3 build/tokens.py
python3 build/manual.py
node build/print.js "$PWD/Manual_de_Identidade_Visual_Tweed.html" \
  ../manual/Manual_de_Identidade_Visual_Tweed_v2.0.pdf /tmp/paginas
```

Para mudar uma cor ou um token, edite `build/pal.py` e rode os scripts: CSS, JSON, amostras e manual saem sincronizados. Nunca edite `tokens/tweed-tokens.css` à mão.
