# REALM: linha fotográfica (piloto aprovado em teste)

## Referências (subidas no Magnific como style refs)
1. Ciprestes contra céu azul-claro: sujeito à direita, céu como espaço negativo.
2. Fachada de vidro refletindo um prédio clássico contra o céu.
3. Água com ondas concêntricas: ecoa os arcos da marca.

## Regras da linha
- Um sujeito (arquitetura em pedra ou vidro, natureza: ciprestes, oliveiras, água) **ocupando um lado do quadro, cortado pela borda**.
- Do outro lado, **céu limpo, azul-pálido, sem nuvens**, como espaço negativo para respiro ou texto.
- Luz natural suave. Tons de azul-céu, pedra quente, verde-oliva e cinza Slate: conversa com a paleta Paper/Harbor/Slate/Stone.
- Calmo, atemporal, discreto. **Sem pessoas, texto, placas ou logos.** Nada de skyline nem "prédio de banco".
- Retratos da liderança: **fotos reais da REALM**, nunca geradas.

## Prompt base (Magnific, modo auto, 3 refs como `style`)
> Vertical editorial photograph in the same line as the reference images: [SUJEITO] rises along the [right/left] side of the frame, cropped by the edge, against a clear, pale, cloudless blue sky that fills the [other] half as calm negative space. Soft natural daylight, muted tones of sky blue, warm stone and slate grey, quiet and timeless. No people, no text, no signage, no logos.

- Proporção conforme o slot: 3:4 (painel), 16:9 (full-bleed), 4:5.
- `count: 3` por slot; escolher 1.

## Rodada 2: mais saturação e realismo (versão em uso)
- **Modelo Cinematic**, com a imagem do piloto como referência `image` (mantém a composição aprovada). O Cinematic não aceita refs de `style`.
- `cinematicControls`: camera `medium-format` · lensBrand `hasselblad-planar` · focalLength `85mm` · aperture `f/8` · filmStock `fuji-velvia-50` · lighting `hard-sunlight` · grain `barely-visible-shadow-grain` · halation `none` · motionBlur `none`.
- Prompt: o mesmo sujeito, com "deep saturated blue sky", "crisp real daylight, rich natural color, true-to-life stone texture".
- Custo: 75 créditos por imagem.
- Alternativa testada: Nano Banana 2.1 com 1 ref de `style` (aceita só uma). Cor mais natural, com cara de filme, e prédio mais clássico. Custo: 65 créditos.

## Imagens no deck (todas no Cinematic com as configurações acima)
| Slide | Slot | Sujeito | Ref (`image`) | Proporção |
|---|---|---|---|---|
| 03 The gap | Painel esquerdo 860×1080, sob véu Harbor a 60% | Água rasa com ondas concêntricas, vista de cima (`shotType: birds-eye`, 50mm) | ref da água | 4:5 |
| 06 Divisor | Tela cheia | Fileira de ciprestes à direita, céu à esquerda sob o título | ref dos ciprestes | 16:9 |
| 07 Where | Painel direito 600×792 | Pedra calcária com janelas em arco e oliveiras | piloto | 3:4 |
| 08 Leadership | Retratos | **Fotos reais da REALM**, não geradas | — | — |

## Piloto
- Slot: slide 07 "Where we invest", painel direito 600×792.
- Sujeito: canto de prédio em pedra calcária com janelas em arco + oliveiras.
- Resultado escolhido: variação 3 de 3. Custo: 70 créditos por imagem.
