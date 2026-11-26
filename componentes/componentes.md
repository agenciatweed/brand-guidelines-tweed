# Componentes

← [Voltar ao README principal](../README.md) · Capítulo 05 do [manual](../manual/Manual_de_Identidade_Visual_Tweed_v2.0.pdf)

Peças que se repetem no site, nas propostas e nas apresentações. Cada uma tem versão para o tema escuro (padrão) e para o tema claro. Os valores vêm dos tokens em [`tokens/tweed-tokens.css`](../tokens/tweed-tokens.css).

## Componentes de interface (Site)

### Botão
- Sempre pílula (`--tweed-radius-pill`), 48 px de altura (56 px no grande), padding lateral de 28 px (36 px no grande).
- Rótulo 15 px, peso 600, tracking +0,01em, nunca quebra linha. Verbo no imperativo: “Começar uma conversa”, “Ver como trabalhamos”.
- **Primário:** escuro = fundo Teal Tweed, rótulo Azul-Escuro; claro = fundo Azul-Escuro, rótulo Teal Tweed (`--tweed-botao-primario`, `--tweed-botao-primario-texto`). Hover: Teal Luz no escuro, Noite Alta no claro, mais o anel `--tweed-sombra-botao-hover`.
- **Ghost:** vidro (`--tweed-botao-ghost-fundo` + blur 16 px), fio `--tweed-fio-forte`, texto `--tweed-texto`. Hover: borda e texto no acento.
- **Halo:** no hover, um brilho teal (`--tweed-halo-botao`, blur 11 px) acende abaixo do botão, que sobe 2 px e cresce 2%.
- Foco: anel de 2 px em `--tweed-foco`, afastado 3 px. Um primário por bloco.

### Eyebrow
Rótulo curto acima do título: 13 px, peso 600, caixa alta, +0,16em, cor `--tweed-acento`. Padrão do site: “Capítulo 01 · O diagnóstico”.

### Card tingido
- Raio 18 px, padding de 24 a 32 px, `background-color` da superfície + `--tweed-card-tingido` (três radiais escuros no topo, três teal na base) + `--tweed-sombra-card`.
- Borda: anel de luz girando (conic-gradient mascarado, 8 s, linear) entre `--tweed-anel-base` e `--tweed-anel`; sem suporte a máscara, borda fixa teal a 22%.
- Quadro de ícone opcional: 44 px, raio 10, fundo `--tweed-acento-lavado`, ícone em `--tweed-acento`.
- Título em `h3`, texto em `small` com `--tweed-texto-tingido`. Cards não são clicáveis: sem hover.

### Número de prova
Mesma superfície do card. Número em `numero` (800, −0,04em, algarismos tabulares) e `--tweed-acento`; rótulo em `small`. Use só números reais: +500 marcas atendidas, 30 anos de repertório criativo, 1 interlocutor.

### Etapa do método
Linha com fio superior, numeral de 28 a 44 px peso 800 em `--tweed-texto-fraco` (acento no hover), título `h3` e texto `small`. As seis etapas do método Presença com Propósito.

### Chip
Pílula com fio `--tweed-fio`, fundo `--tweed-superficie-elevada`, texto `small` em `--tweed-texto-suave`. Lista de serviços (esteira no site).

### Navbar flutuante
Fixa a 16 px das bordas, raio 14, vidro `--tweed-vidro` com blur 14 px, logotipo com 104 px de largura (72 px no celular), links de 15 px e o CTA primário à direita.

## Componentes de conteúdo (Original)

- **Cachorrinho Tweed** ([`tweed-cachorrinho-github.png`](./tweed-cachorrinho-github.png)): decoração discreta em apresentações, rodapés e propostas. Pequeno (56 a 84 px), num canto, em opacidade cheia. Funciona nos dois temas. Nunca protagonista, nunca recortado ou recolorido.
- **Felipe e Cintia**: foto dos fundadores para slides e páginas sobre quem é a Agência Tweed. Três proporções: [4:3](./felipe-e-cintia-3.jpg), [quadrada](./felipe-e-cintia-3-square.jpg) e [wide](./felipe-e-cintia-3-wide.jpg). Raio de 16 px, sem filtros. (`felipe-e-cintia.jpg` e `felipe-e-cintia-2.jpg` são versões antigas, mantidas só por compatibilidade.)
- **Marcas atendidas**: logotipos de clientes relevantes para dar autoridade a propostas e apresentações.
  - Tema escuro: [`marcas-atendidas.png`](./marcas-atendidas.png) (horizontal, 1456 × 500) e [`marcas-mobile.png`](./marcas-mobile.png) (vertical, 770 × 809), em branco.
  - Tema claro (Proposta): [`marcas-atendidas-escuro.png`](./marcas-atendidas-escuro.png) e [`marcas-mobile-escuro.png`](./marcas-mobile-escuro.png), a mesma arte em Azul-Escuro.
  - Nunca recorte, reordene ou recolora os logotipos.
- **Talvez a Tweed não seja para você**: seção das propostas com quatro afirmações, sempre nesta ordem e com o ícone correspondente:
  1. Não somos a opção de quem está procurando o menor preço do mercado. ([`lowest-price`](./lowest-price.svg))
  2. Não trabalhamos com quem mede marketing por quantidade de peças entregues. ([`overload`](./overload.svg))
  3. Não funcionamos bem com quem quer terceirizar a marca inteira sem participar da construção. ([`handoff`](./handoff.svg))
  4. Não vendemos fórmula pronta, pacote fechado nem promessa de resultado garantido. ([`formula`](./formula.svg))

  Os ícones são desenhados em preto. Recolore para Teal Tweed no escuro e para Azul-Escuro ou Teal Tinta no claro (embutindo o SVG e trocando o `fill`, ou por máscara CSS com `mask-mode: alpha`, como no site). Não use esses ícones como decoração genérica.
- **Depoimentos**: a avaliação é sempre a imagem [`5stars.png`](./5stars.png) (226 × 44, usada a 104 a 113 px de largura), nunca estrelas desenhadas ou emoji. Card com raio 24, leve rotação de ±0,5°, texto do cliente sem edição de sentido, nome em peso 700 e cargo em `caption`. Funciona nos dois temas.

## Ícones de interface (Site)

Traço 1,75, viewBox 24, pontas e junções arredondadas, sem preenchimento, `stroke="currentColor"`. Sempre acompanham texto. Os do site:

```html
<!-- tela -->   <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 22h8M12 18v4M7 9h6M7 13h4"/></svg>
<!-- alvo -->   <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M3 12h18"/><circle cx="12" cy="12" r="9"/></svg>
<!-- canais --> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16M4 12h10M4 18h6"/><path d="M17 15l3 3-3 3"/></svg>
<!-- seta -->   <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
```

## Imagens de referência

- [Cachorrinho Tweed](./tweed-cachorrinho-github.png)
- [Felipe e Cintia, 4:3](./felipe-e-cintia-3.jpg) · [quadrada](./felipe-e-cintia-3-square.jpg) · [wide](./felipe-e-cintia-3-wide.jpg)
- [Marcas atendidas horizontal](./marcas-atendidas.png) · [vertical](./marcas-mobile.png) · [horizontal em Azul-Escuro](./marcas-atendidas-escuro.png) · [vertical em Azul-Escuro](./marcas-mobile-escuro.png)
- [Ícone lowest-price](./lowest-price.svg) · [overload](./overload.svg) · [handoff](./handoff.svg) · [formula](./formula.svg)
- [Cinco estrelas](./5stars.png)
