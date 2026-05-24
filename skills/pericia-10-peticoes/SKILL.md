---
name: pericia-10-peticoes
description: Gerar minutas de peticoes do perito judicial: aceite, escusa, honorarios, diligencia, pedido de documentos, prorrogacao, juntada de laudo, esclarecimentos e manifestacoes para organizacao de vistoria.
---

# Peticoes do Perito

## Quando Usar

Use quando o perito precisa peticionar no processo de forma impessoal, tecnica e limitada ao encargo pericial.

Para manifestacoes de organizacao de vistoria e pecas que serao levadas a PDF, use a identidade profissional pessoal do perito no cabecalho e na assinatura, com nome completo e CREA, sem marca empresarial e sem logo.

## Entradas Esperadas

- tipo de peticao
- processo
- decisao
- prazo
- pedido
- fundamento
- anexos
- fontes aplicaveis

## Fluxo Operacional

1. Ler a demanda e identificar processo, objeto, partes, tribunal, datas e documentos disponiveis.
2. Separar fontes oficiais, fontes tecnicas, fontes consultivas e bases internas.
3. Aplicar as regras abaixo, citando fonte e marcando itens que exigem verificacao antes de uso real.
4. Gerar a saida no template da skill, registrando evidencias, limitacoes e pendencias.
5. Executar o checklist e os criterios de revisao antes de entregar qualquer texto para uso externo.

## Regras Operacionais Com Fonte

| Regra operacional | Fonte | Tipo | Verificacao |
|---|---|---|---|
| Peticoes do perito devem ser limitadas ao encargo, pedido processual claro e fundamento minimo. | CPC arts. 156-158, 465, 466, 477 e correlatos | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Honorarios devem citar regime do CPC e, quando aplicavel, CNJ/tribunal local. | CPC art. 95; Resolucao CNJ 232/2016; atos locais | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Diligencia deve observar ciencia das partes quando aplicavel. | CPC art. 474 | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| ART e regularidade profissional podem ser informadas quando relevantes ao encargo. | Lei 6.496/1977; Confea/Crea | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| A linguagem deve ser neutra, impessoal e tecnica; nao deve defender parte. | CPC; Manual de Redacao oficial como apoio | Fonte oficial/consultiva | [VERIFICAR ANTES DE USO REAL] |

## Saidas Esperadas

- minuta de peticao
- checklist de protocolo
- lista de anexos
- alertas de fundamento e prazo

## Regras de Seguranca Tecnica

- Nao inventar norma, artigo, decisao judicial, edicao de norma tecnica ou numero de portaria.
- Marcar como [VERIFICAR ANTES DE USO REAL] toda fonte temporal, local, paga, substituivel ou dependente do processo concreto.
- Separar fonte oficial, fonte tecnica e fonte consultiva em toda saida.
- Nao reproduzir integralmente normas ABNT, livros comerciais, handbooks ou standards protegidos por licenca.
- Nao transformar cartilha, fabricante, literatura tecnica ou boa pratica em obrigacao legal.

## Arquivos de Apoio

- `references/REFERENCIAS.md`
- `templates/PETICAO_PERITO_MODELO.md`
- `templates/PETICAO_MANIFESTACAO_VISTORIA_PERICIAL.md`
- `checklists/CHECKLIST.md`
- `matrices/pericia-10-peticoes.csv`
- `examples/entrada.md`
- `examples/saida.md`
- `SEGURANCA_TECNICA.md`
- `LIMITACOES.md`
- `CRITERIOS_REVISAO.md`
