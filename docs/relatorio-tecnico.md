# Relatório técnico · Manual v2.0

← [Voltar ao README principal](../README.md)

Registro de procedência, decisões e verificações da versão 2.0 das brand guidelines da Agência Tweed (novembro de 2026).

## 1. Fontes consultadas

| Fonte | O que forneceu |
|---|---|
| Este repositório na versão 1.0 (commit `e6923b5`) | Teal Tweed, Azul-Escuro, Branco; Inter em três cortes; logotipos teal e Azul-Escuro (SVG do Illustrator); componentes decorativos; tom de voz |
| agenciatweed.com.br, CSS de produção (página inicial, blog e artigos), lido em 26/11/2026 | Tons de apoio do escuro, escala tipográfica com `clamp()`, espaçamentos, raios, botões, card tingido com anel, depoimento, navbar, ícones de interface, movimento, regras de acessibilidade; WOFF2 subconjunto das quatro faces |
| Design systems da Orbit Outsourcing e da UY3 (feitos pela Tweed) | Estrutura de referência: marcação Original/Proposta, tokens semânticos por tema, tabela de contraste, repositório com manual em PDF, amostras, tokens CSS/JSON, relatório técnico |

## 2. Itens por origem

**Original (v1.0):** as três cores institucionais, a família Inter e os seis arquivos TTF, os dois logotipos, cachorrinho, fotos dos fundadores, faixa de marcas (branca), quatro ícones de seção, cinco estrelas, tom de voz.

**Site:** Noite `#11131C`, Noite Alta `#171A25`, Prata `#D3D7DF`, Cinza `#A7ACB9`, Cinza Fraco `#868DA1`, Teal Luz `#5CFFCB`; fios em alfa (9%, 5,5%, 28%); rampa de teal em alfa (4 a 40%); escala `mega` a `caption`; `gutter`, ritmo de seção, vãos; raios 4, 8, 10, 14, 16, 18, 24 e pílula; curva `cubic-bezier(.16,1,.3,1)`; superfícies do card e do depoimento; halo do botão; véu e brilho do hero; mapeamento de pesos para os cortes ópticos.

**Proposta (v2.0):** tema claro inteiro (Névoa, Gelo, Grafite, Grafite Fraco, Teal Tinta e o mapeamento semântico), card tingido claro, logotipo branco, avatar, área de proteção, tamanhos mínimos, escalas de slide, A4 e post, grid de slide e A4, faixa de marcas em Azul-Escuro, proporções de cor.

## 3. Decisões

1. **Teal Tinta `#00704D`.** Mesmo matiz do Teal Tweed (161°), saturação total, luminosidade 22%. É o tom mais claro da rampa que passa de 5:1 sobre o Gelo, o fundo claro mais escuro do sistema (5,28:1), o que garante folga em qualquer superfície clara. Tons mais claros (`#007A54`, `#008057`) reprovam sobre Gelo.
2. **Botão primário no claro.** Teal Tweed preenchido sobre Branco teria 1,32:1 de contraste de borda e perderia presença. A pílula Azul-Escuro com rótulo teal mantém o par mais forte da marca (14,82:1) e carrega a identidade do escuro para dentro do claro.
3. **Corpo em Inter 18pt Regular.** O guia v1.0 indicava 24pt Medium para o corpo; o site usa 18pt Regular no corpo e Medium para interface. A v2.0 segue o site: o corte de 18pt foi desenhado para texto corrido e o Medium em parágrafos longos pesa demais.
4. **Neutros do claro.** Grafite e Grafite Fraco puxam o mesmo azul dos cinzas do site (matiz ~228°), para que não exista cinza neutro em nenhum dos temas.
5. **Nenhum arquivo da v1.0 foi movido ou renomeado.** Propostas, scripts e o design system no Claude apontam para `logos/logo_tweed_teal.png`, `componentes/...` e `tipografia/inter-*.ttf`; esses caminhos continuam válidos.
6. **Tokens com prefixo `--tweed-`**, para conviver sem colisão com tokens de clientes no mesmo projeto.

## 4. Verificações

- **Contraste:** todos os pares de texto dos dois temas calculados pela fórmula de luminância relativa da WCAG 2.x em `fonte-editavel/build/pal.py`. Tabela em `cores/paleta-principal.md` e na página 16 do manual. Nenhum par de texto do sistema fica abaixo de 4,5:1; os pares que reprovam (Teal Tweed sobre Branco e Névoa) estão documentados como proibidos.
- **Logotipo:** branco, PNG e PDF gerados do SVG original com `rsvg-convert`, conferindo que a geometria é idêntica entre as versões teal e Azul-Escuro (mesmo `path`, só o `fill` muda).
- **Manual:** HTML impresso em PDF pelo Chromium (Playwright), A4 paisagem, 32 páginas, fontes Inter incorporadas como subconjunto, revisado página a página em imagem.
- **Tokens:** CSS e JSON gerados pelo mesmo script a partir de `pal.py`; JSON validado.

## 5. Pendências

- Aprovar as propostas (tema claro, logotipo branco, avatar, proteção, tamanhos, escalas de slide/A4/post).
- Definir referência Pantone ou tinta especial para o Teal Tweed e validar o Azul-Escuro em prova de impressão (preto rico).
- Definir cores funcionais (sucesso, alerta, erro), hoje inexistentes.
- Banco de imagens de trabalho aprovado.
- Avaliar se o site ganha uma versão clara (por exemplo, para o blog) usando os tokens do tema claro.
