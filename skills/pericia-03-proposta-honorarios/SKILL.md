---
name: pericia-03-proposta-honorarios
description: Montar proposta de honorários, memória de cálculo, justificativa técnica, despesas, ART e alertas de regime de custeio.
---

# Proposta de Honorários Periciais

## Quando Usar

Use quando o perito precisa apresentar proposta de honorários, pedir complementação, justificar complexidade ou adequar valor a tabela local.

## Entradas Esperadas

- objeto da perícia
- decisão de nomeação
- prazo
- tabela local, se houver
- gratuidade ou custeio pelas partes
- deslocamentos
- estimativa de horas
- necessidade de ensaios ou equipe

## Fluxo Operacional

1. Ler a demanda e identificar processo, objeto, partes, tribunal, datas e documentos disponíveis.
2. Separar fontes oficiais, fontes técnicas, fontes consultivas e bases internas.
3. Aplicar as regras abaixo, citando fonte e marcando itens que exigem verificação antes de uso real.
4. Gerar a saída no template da skill, registrando evidências, limitações e pendências.
5. Executar o checklist e os critérios de revisão antes de entregar qualquer texto para uso externo.

## Regras Operacionais Com Fonte

| Regra operacional | Fonte | Tipo | Verificação |
|---|---|---|---|
| O regime de adiantamento, rateio e custeio deve partir do CPC e da decisão judicial. | CPC art. 95 | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Honorários em justiça gratuita devem considerar atos CNJ e tabela local aplicável quando existente. | Resolução CNJ 232/2016; atos do tribunal local | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| No TJCE, tabela, portaria e fluxo de pagamento devem ser conferidos antes de fixar rubrica e valor. | Página oficial TJCE de credenciamento, resoluções e portarias | Fonte oficial local | [VERIFICAR ANTES DE USO REAL] |
| ART, deslocamento, ensaios, equipe e complexidade devem ser descritos como composição técnica, não como certeza de deferimento. | Lei 6.496/1977; Confea/Crea; CPC art. 95 | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Regulamentos de honorários de entidade profissional podem apoiar a memória de cálculo, sem substituir tabela judicial ou decisão. | IBAPE/SP ou entidade profissional | Fonte consultiva | [VERIFICAR ANTES DE USO REAL] |

## Saídas Esperadas

- proposta de honorários
- memória de cálculo
- rubricas e justificativas
- alertas de verificação CNJ/TJCE
- minuta de petição quando aplicável

## Regras de Segurança Técnica

- Não inventar norma, artigo, decisão judicial, edição de norma técnica ou número de portaria.
- Marcar como [VERIFICAR ANTES DE USO REAL] toda fonte temporal, local, paga, substituível ou dependente do processo concreto.
- Separar fonte oficial, fonte técnica e fonte consultiva em toda saída.
- Não reproduzir integralmente normas ABNT, livros comerciais, handbooks ou standards protegidos por licença.
- Não transformar cartilha, fabricante, literatura técnica ou boa prática em obrigação legal.

## Arquivos de Apoio

- `references/REFERENCIAS.md`
- `templates/PROPOSTA_HONORARIOS_PERICIAIS.md`
- `checklists/CHECKLIST.md`
- `matrices/pericia-03-proposta-honorarios.csv`
- `examples/entrada.md`
- `examples/saida.md`
- `SEGURANCA_TECNICA.md`
- `LIMITACOES.md`
- `CRITERIOS_REVISAO.md`
