# REALM: Corporate Overview, prompt de teste (fluxo 1: Claude Design / Slides)

> Pacote: `logos/`, `fonts/`, `refs/` (contact sheets das melhores refs da Collateral).
> Este prompt é auto-suficiente: dá para colar no Claude Design junto com os arquivos, ou usar daqui da sessão.

---

## 0. Etapas

1. **Midfi (estrutura):** escala de cinza, Sentient + Geist, grid e copy reais. **Sem imagens, logos ou arcos.** Cada imagem vira um placeholder tracejado com a descrição do que vai ali (`IMAGE`, `GRAPHIC`, `LOGO`, `PORTRAIT`). Objetivo: aprovar a narrativa, a ordem e os layouts.
2. **Visual:** aplicar a seção 3 (cores, arcos, logos) sobre a estrutura aprovada. As imagens são geradas depois via MCP, a partir das descrições dos placeholders.

## 1. Tarefa

Crie um deck **Corporate Overview da REALM** com **10 slides, 16:9 (1920×1080 / 13,33×7,5 pol)**, pronto para exportar em **.pptx**.
É um deck de apresentação para famílias e seus consultores, apresentado ao vivo ou enviado depois de uma introdução.
Qualidade-alvo: os decks da Collateral em `refs/` (Certosa, Inscription, PACT, Amborella). Siga **a diagramação** deles, não o conteúdo nem as cores.

## 2. Cliente e tom

- REALM: plataforma de investimento em real estate para **capital familiar** (single, multi-family offices e famílias UHNW), sponsor e co-GP, fundada em 2019, atuação nacional nos EUA.
- Tom: **um clube sem placa**. Discreto, confiante, sem esforço. Confiança mostrada por fatos, nunca declarada.
- A REALM é "family capital", **nunca "institutional"**.
- Evite o clichê do setor: navy dominante + serifa + foto de prédio na primeira tela.

## 3. Marca, direção "Timeless"

### Cores (use só estas, mais tints delas)
| Token | Hex | Uso |
|---|---|---|
| Paper | `#F6F3EE` | **Fundo dominante** (≈70% dos slides) |
| Harbor | `#1D2430` | Texto principal; fundo dos slides âncora (capa alternativa, divisores, fechamento) |
| Slate | `#8693A6` | Arcos, acentos, números de destaque, linhas finas |
| Stone | `#B5B1AB` | Labels, legendas, rules 1px, texto terciário |

Tints permitidos: Harbor a 70% para corpo de texto em Paper; Stone a 30–40% para preenchimentos de cards sutis.
Nada de amarelo, verde-neon, gradientes vibrantes ou sombras pesadas.

### Tipografia
- **Títulos e números grandes:** Sentient (Light ou Regular), tracking levemente negativo, entrelinha 1.05–1.1.
- **Corpo, labels e UI:** Geist (Regular; Medium só para labels pequenos em caixa alta com tracking +6%).
- Escala (1920×1080): Display 120 / H1 64 / H2 40 / Número KPI 72–96 / Lede 22 / Corpo 16–18 / Label 12–13 caps.
- No .pptx, nomes de fonte: `Sentient` e `Geist`.

### Logo (`logos/`)
- `realm-logo-light-bg.svg`: wordmark Harbor + arcos Slate, **em fundo Paper**.
- `realm-logo-dark-bg.svg`: wordmark Paper + arcos Slate, **em fundo Harbor**.
- `realm-logo-mono-paper.svg`: tudo em Paper, versão monocromática para fundos escuros ou fotográficos.
- Nunca redesenhar, distorcer ou recolorir fora dessas versões. Área de respiro ≥ altura do "R".

### Grafismo: os três arcos
- O dispositivo da marca são **os arcos concêntricos do logo** (significado: estratégias trabalhando juntas, pessoas se aproximando).
- Use como grafismo **grande, recortado pela borda do slide**, com traço **fino** (1–2px a 1920), em Slate ou Stone, **silencioso**.
- No máximo 1 grafismo de arcos por slide; nunca em cor viva; nunca sobre texto.

## 4. Sistema de diagramação (extraído das refs da Collateral)

1. **Grid:** margens laterais 96px, topo 80px, 12 colunas, gutter 24px. Rodapé a 1020px.
2. **Faixa de título (padrão da casa):** título no canto superior esquerdo (cols 1–6) + **lede curto à direita** (cols 8–12, 2–3 linhas, Geist 18–20, Harbor 70%). Esse é o padrão mais consistente nas refs.
3. **Rodapé:** logo pequeno (altura ~22px) no canto inferior esquerdo, número da página no canto inferior direito, ambos discretos.
4. **Slides âncora em Harbor:** capa (opcional), divisores e fechamento. Título grande no canto inferior esquerdo, muito respiro.
5. **Módulos de conteúdo:**
   - Linha de KPIs: número grande em Sentient + legenda em Geist + rule 1px Stone acima.
   - Cards em 3–4 colunas: rule fina no topo ou contorno 1px; label em caps; título curto; 2–3 linhas de corpo.
   - Processo numerado 01–04 em linha horizontal.
   - Grid de equipe: retrato (placeholder retangular em Stone 30%), nome, cargo, 2 linhas de bio.
   - Split: metade do slide com painel Harbor ou grafismo de arcos, metade com conteúdo.
6. **Densidade:** deck de investidor. Mais estruturado que keynote, mas cada slide com **uma mensagem**. O título é a mensagem.
7. Alinhamento rigoroso: tudo encaixado no grid, baselines alinhadas, sem elementos "flutuando".

## 5. Conteúdo, slide a slide (copy em inglês)

**01 · Capa** (Paper)
- Logo light-bg, grande, à esquerda. Arcos grandes recortados à direita.
- Linha: *Family Capital. At Scale.* (sem ®). Label: `CORPORATE OVERVIEW · 2026`

**02 · Who we are** (Paper, faixa de título + 3 fatos)
- Título: *A real estate platform built for families.*
- Lede: *REALM brings families together to invest directly in real estate, with the principals investing alongside them.*
- 3 fatos em colunas: `FOUNDED` 2019 · `REACH` Nationwide, U.S. · `MODEL` Sponsor and co-GP

**03 · The gap** (split: esquerda Harbor com frase, direita texto)
- Título: *Families want real estate. Few want to build a team for it.*
- Corpo: *A typical REALM family has around $200M investable and wants $10M or more in real estate, without hiring an in-house team to source, underwrite and manage it.*

**04 · By the numbers** (Paper, linha de 4 KPIs)
- Título: *Trust, shown by the numbers.* Lede: *Figures provided by REALM.*
- `132` families · `~$1B` assets under management · `43` active investments · `88%` of investors introduced by another investor
- Nota de rodapé pequena: *Client-provided data as of October 2026. Subject to compliance review.*

**05 · How we work** (Paper, 3 cards)
- Título: *Aligned from the first dollar.*
- Cards: **Principals invest alongside**: our own capital sits in every deal. · **By introduction only**: opportunities are never sent to cold prospects. · **Candid reporting**: families hear what is working and what is not.

**06 · Divisor** (Harbor) · *Where and how we invest*

**07 · Where we invest** (split com grafismo de arcos)
- Título: *National reach, local conviction.*
- Lista: Bay Area · Midtown Manhattan · The Carolinas · Inland Empire · Boston

**08 · Leadership** (grid de 3)
- Travis King, Founder and CEO · Greg Drakos, COO and Co-CIO · Will Moyer, Principal, Capital
- Retratos: placeholders. Bios: 2 linhas neutras, sem números de outras firmas.

**09 · Working with REALM** (processo 01–04)
- 01 Introduction · 02 Alignment · 03 Investment · 04 Reporting (1 linha cada)

**10 · Fechamento** (Harbor)
- Logo dark-bg. Linha: *Better, together.* Placeholder de contato: `name@realmlp.com`

## 6. Regras de conteúdo (não negociáveis)
- Proibido: "institutional", "exclusive access", "tailored solutions", garantias, retornos ou metas de retorno.
- Sem ® em lugar nenhum. Sem nomes de fundos/veículos em captação. Sem nomes de famílias ou investidores.
- Não inventar números além dos listados acima.

## 7. Entrega e checagem
- Fontes e cores **exatamente** como acima; texto editável (nada de texto como imagem).
- Antes de entregar, revise cada slide: overflow de texto, alinhamento ao grid, contraste, consistência do rodapé.
- Exporte para .pptx e confirme que títulos e corpo continuam texto editável em Sentient/Geist.
