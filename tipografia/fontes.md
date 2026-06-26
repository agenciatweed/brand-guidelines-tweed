# Fontes

## Fonte Principal
- **Inter**

## Uso
- Inter 28pt Bold: Headlines, CTAs, elementos destacados
- Inter 28pt Bold Italic: Ênfases em Headlines, CTAs, elementos destacados
- Inter 24pt Medium: Texto corpo
- Inter 24pt Medium Italic: Ênfases no Texto corpo
- Inter 18pt Regular: Textos menores
- Inter 18pt Regular Italic: Ênfase em Textos menores

## Links para os arquivos das fontes:
- [Link para a Fonte Inter 28pt Bold](./tipografia/Inter_28pt-Bold.ttf)
- [Link para a Fonte Inter 28pt Bold Italic](./tipografia/Inter_28pt-BoldItalic.ttf)
- [Link para a Fonte Inter 24pt Medium](./tipografia/Inter_24pt-Bold.ttf)
- [Link para a Fonte Inter 24pt Medium Italic](./tipografia/Inter_24pt-MediumItalic.ttf)
- [Link para a Fonte Inter 18pt Regular](./tipografia/Inter_18pt-Regular.ttf)
- [Link para a Fonte Inter 18pt Regular Italic](./tipografia/Inter_18pt-Italic.ttf)

## Embed codes para fallback caso não seja possível utilizar os arquivos TTF fornecidos:
### <link> - Embed code in the <head> of your html:
```
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">
```
### @import - Embed code in the <head> of your html:
```
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
</style>
```
### <link> - Inter: CSS class for a variable style:
```
// <weight>: Use a value from 100 to 900
// <uniquifier>: Use a unique and descriptive class name
.inter-<uniquifier> {
  font-family: "Inter", sans-serif;
  font-optical-sizing: auto;
  font-weight: <weight>;
  font-style: normal;
}
```
