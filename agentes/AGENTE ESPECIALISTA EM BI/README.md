# AMBER — Power BI Executive Dashboard Specialist

> Agente de Business Intelligence especializado em **modelagem de dados, DAX e dashboards
> executivos em Power BI** renderizados pelo visual **HTML Content**.

---

## 1. O que é a AMBER

A AMBER transforma um pedido de dashboard em **solução pronta para colar no Power BI**:
medidas DAX auxiliares + uma medida final que devolve uma string **HTML + CSS puro**,
renderizada pelo visual *HTML Content*.

Ela **não** entrega conceito, wireframe ou exemplo genérico de mercado. Entrega código.

### Por que HTML Content e não visual nativo

| Visual nativo | Medida HTML |
|---|---|
| Layout limitado ao que o visual oferece | Layout livre: grid, cards, tabelas, barras, SVG |
| Formatação condicional por regra fixa | Qualquer lógica condicional em DAX |
| Um visual por indicador | Um painel inteiro em **uma única medida** |
| Difícil versionar | É texto — vive num `.txt` versionável |

### Escopo de atuação

- Modelagem: esquema estrela, relacionamentos, granularidade, colunas calculadas.
- DAX: medidas de KPI, comparativos temporais, ranking, agregações por dimensão.
- Diagnóstico: por que um filtro não propaga, por que a soma não fecha com o total,
  por que um slicer zera o painel.
- Apresentação: HTML/CSS com identidade visual BS2.

---

## 2. Como pedir

Quanto mais desses itens vierem no pedido, menos ida e volta:

| Item | Exemplo |
|---|---|
| **Tema / objetivo** | "produtividade do time de atendimento" |
| **Indicador principal** | "quantidade de atendimentos" |
| **Indicadores secundários** | "tempo falado médio, atendentes ativos" |
| **Cortes (dimensões)** | "por departamento e por canal" |
| **Período** | "últimos 6 meses, com comparativo mês a mês" |
| **Público** | "diretoria" ou "supervisão operacional" |
| **Tabelas e colunas disponíveis** | print do modelo, dicionário ou lista de campos |

A AMBER faz **no máximo 3 perguntas**, e só quando existe ambiguidade que realmente impede
a construção. Se o pedido é claro, ela entrega direto.

### Pedidos que funcionam bem

```
Quero um painel de TPV por estabelecimento, com chargeback e cancelamento,
em KPIs no topo e uma tabela por EC embaixo. Tema escuro.
```

```
No relatório de atendimento, remova a coluna de score da tabela de atendentes.
```

```
A soma por departamento não bate com o total de atendimentos. Corrija.
```

### Cuidado com o escopo das palavras

Pedidos como *"troque tudo que for X por Y"* são ambíguos: pode significar **renomear a
medida no modelo** (dá retrabalho no Power BI) ou apenas **mudar o texto na tela**.
Diga qual dos dois. O padrão adotado hoje é o **menor escopo — rótulo de exibição**.

---

## 3. O que você recebe

### 3.1 No chat — 8 seções fixas

```
1. Entendimento do Dashboard      tema, objetivo, público, período, indicadores, premissas
2. Mapeamento Técnico             tabelas, colunas, medidas existentes vs. novas
3. Medidas DAX Auxiliares         cada uma nomeada e isolada
4. Medida HTML Final              a string DAX com HTML + CSS
5. Implementação no Power BI      passo a passo, na ordem de dependência
6. Filtros e Slicers Sugeridos    só campos que existem, com justificativa
7. Validação Técnica              checklist executado
8. Premissas e Observações        toda PREMISSA + todo objeto pedido e não encontrado
```

### 3.2 Como arquivo — um `.txt` único

Formato padrão aprovado em **2026-08-19**:

- Cabeçalho `/* ... */` com tema, tabela fonte, paleta em hex, lista de relatórios e a
  instrução *"criar TODAS as medidas na tabela X, NA ORDEM ABAIXO"*.
- Corpo em **blocos numerados**: `/* ===== BLOCO N — TÍTULO ===== */`.
- Cada medida com a linha **`Nome da Medida =`** logo antes do corpo.
- Medidas em **ordem de dependência** — dá para colar de cima para baixo sem erro.
- Comentários inline explicando **PREMISSAS** e regras de negócio.

> Ao alterar um dashboard, a AMBER regera o **documento inteiro**, nunca um patch solto.
> No chat vem um resumo em tabela: *o quê / onde / por quê*.

---

## 4. Projetos ativos

### `BS2_Medidas_DAX_Dashboards_Atendimento.txt`

Base **`fato_genesys`** (portal Genesys via Google BigQuery). Dois relatórios:
**Consolidado** e **Sinais Vitais**, mais a medida de CSS compartilhada `[BS2 CSS]`.

- Granularidade: **1 linha = 1 segmento de conversa**.
- Colunas válidas: `conversation_id`, `conversation_start`, `conversation_end`, `Data`,
  `department`, `media_type`, `participant_name`, `segment_type`, `DepConversa`.
- `name_queue` e `purpose` **não existem mais**. `Mês` / `MêsNum` existem mas são
  **proibidas** — o eixo mensal sai sempre de `EOMONTH(fato_genesys[Data], 0)`.
- Rótulo de tela: **"Tempo Falado"** / **"Tempo Medio Falado"**. Os nomes das medidas
  no modelo continuam `TMA` — a divergência é proposital.

### `BS2_Medidas_DAX_Painel_EC.txt`

Painel de Estabelecimento em **dark mode** sobre `#090E29`. Escopo fechado nos quatro
valores transacionais, em KPIs e em linhas:

| Indicador | Cor | Variação % |
|---|---|---|
| TPV | `#4D7CFF` | escala normal (sobe = verde) |
| Chargeback | `#FF3366` | **invertida** (sobe = rosa) |
| Cancelamento | `#E8A317` | **invertida** (sobe = rosa) |
| Agenda a Pagar | `#17A673` | **sem indicador** — é saldo, não desempenho |

---

## 5. Identidade visual

Brandbook **Banco BS2** (`BS2_guiamarca_resumido.pdf`, pág. 12):

| Cor | Hex | PANTONE |
|---|---|---|
| Azul | `#1226AA` | 2736C |
| Azul ultramarino | `#090E29` | 282C |
| Rosa | `#FF3366` | 191C |
| Branco quente | `#FAFAFA` | — |

Tipografia: `"Segoe UI", Calibri, Arial, sans-serif` (o brandbook não define fonte).
Redução mínima do logo: **60px** digital / **25mm** impresso.

---

## 6. Regras técnicas do HTML Content

**Permitido:** HTML e CSS puros, SVG inline.

**Proibido:** JavaScript, frameworks, bibliotecas externas, fontes externas (o visual
não executa script nem busca recurso na rede).

Convenções em uso:

- Escape de aspas: `VAR Q = UNICHAR ( 34 )`, concatenado com `& Q &`.
- Classes CSS curtas: `.db .hd .kpi .kv .kl .card .bar .rank .ins .ft`.
- **Decimal em CSS usa ponto.** Onde `FORMAT` puder gerar vírgula por configuração
  regional: `SUBSTITUTE ( FORMAT ( [Valor], "0.00" ), ",", "." )`.
- Todo valor injetado é **pré-formatado no VAR** — não se calcula dentro da string.
- Concatenação com `&` só para valor dinâmico; HTML/CSS estático fica fixo na string.

---

## 7. Checklist executado antes de cada entrega

```
[ ] Medidas referenciadas existem ou foram criadas nesta resposta
[ ] Todas as VAR declaradas antes do uso
[ ] Nenhuma referência DAX órfã
[ ] Divisões protegidas com DIVIDE
[ ] BLANK tratado onde necessário
[ ] Valores CSS numéricos com ponto decimal
[ ] Classes do HTML ⊆ classes do CSS
[ ] Sem JavaScript / sem bibliotecas externas
[ ] Saldo de parênteses e colchetes = 0, aspas pares
[ ] Paridade <th> × <td> e <div> abertas/fechadas
[ ] Medida final pronta para colar
```

---

## 8. Armadilhas já enfrentadas (e a regra que ficou)

| Sintoma | Causa | Regra |
|---|---|---|
| "Não é possível determinar um único valor para a coluna X" | Fórmula de **coluna** colada como **medida** | Coluna calculada tem contexto de linha; medida não |
| Soma por categoria estoura o total | `DISTINCTCOUNT` **não é aditivo** | Só somar por categoria se cada item pertencer a **uma** categoria |
| Top N não fecha com o total | Falta linha de resto | Sempre `Total - SUMX(TopN)` como "Outros" |
| Slicer de mês zera o painel | `SUMMARIZE` do cadastro filtrado junto | `CALCULATETABLE(..., REMOVEFILTERS(dim_data))` protege a **lista**, nunca os valores |
| Toda linha da tabela recebe o mesmo total | Confiança em propagação implícita no `ADDCOLUMNS` | Capturar o filtro em `VAR` e aplicar **explicitamente** em cada `CALCULATE` |
| Valores de um mês batem, dos outros não | Chave de período sem o ano | `OrdemMes = ano * 100 + mes`; mês anterior = `IF(MOD(x,100)=1, x-89, x-1)` |
| Rótulo do departamento errado | `conversation_start` é de **conversa**, não de segmento — o desempate virava ordem alfabética | Sem coluna de ordem de segmento não existe "departamento de entrada"; usar o **predominante** |
| `FORMAT(BLANK(), "#,##0")` volta vazio | Comportamento do DAX | Somar `+ 0` antes de formatar |
| `IF` retornando tabela | Não é permitido em DAX | Reestruturar com `CALCULATETABLE` / `UNION` |
| Comentário `/* */` dentro de `/* */` | Comentário DAX **não aninha** | Comentar bloco com `//` linha a linha |

---

## 9. Limites — o que a AMBER não faz

- **Não inventa objeto.** Se a coluna não está no dicionário nem foi informada por você,
  ela aparece na seção 8 como *não encontrada* — não é assumida.
- **Não cria indicador que você não pediu.** Semáforo, índice de risco, nota 0-100 e
  score sintético já foram propostos e **rejeitados**. O padrão hoje é **dado bruto bem
  formatado**; escala derivada só com **meta documentada** para comparar.
- **Não expande escopo.** Entrega o que foi pedido, no tamanho pedido.
- **Não usa JavaScript** — o visual não executa.

---

## 10. Fluxo de trabalho recomendado

```
1. Descreva o pedido (seção 2 deste README)
2. Anexe o modelo: print dos campos, dicionário ou o .txt vigente
3. Receba as 8 seções + o arquivo .txt
4. Cole as medidas no Power BI NA ORDEM do arquivo
5. Insira o visual HTML Content e atribua a medida final
6. Reporte divergência com o valor esperado — quanto mais específico, mais rápido o diagnóstico
```

Quando o número não bate, o mais útil é: **qual indicador, qual filtro aplicado, qual
valor apareceu e qual era o esperado.** Com isso o diagnóstico sai direto do código.

---

*Banco BS2 · BI & Analytics · documento gerado pela AMBER*
