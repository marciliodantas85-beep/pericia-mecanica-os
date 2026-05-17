---
name: pericia-07-anexo-fotografico
description: Gerar anexo fotográfico técnico com sequência, legenda, contexto, finalidade, vínculo com quesitos e ressalvas de qualidade/integridade.
---

# Gerador de Anexo Fotográfico

## Quando Usar

Use quando houver fotos de diligência, documentos fotográficos dos autos ou imagens técnicas que precisam compor anexo do laudo.

## Entradas Esperadas

- fotos
- metadados
- inventário de evidências
- quesitos
- local/data
- descrição técnica
- limitações

## Fluxo Operacional

1. Ler a demanda e identificar processo, objeto, partes, tribunal, datas e documentos disponíveis.
2. Separar fontes oficiais, fontes técnicas, fontes consultivas e bases internas.
3. Aplicar as regras abaixo, citando fonte e marcando itens que exigem verificação antes de uso real.
4. Gerar a saída no template da skill, registrando evidências, limitações e pendências.
5. Executar o checklist e os critérios de revisão antes de entregar qualquer texto para uso externo.

## Regras Operacionais Com Fonte

| Regra operacional | Fonte | Tipo | Verificação |
|---|---|---|---|
| Fotografias podem instruir o laudo como elementos materiais, desde que contextualizadas. | CPC art. 473 §3º | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Cada foto deve ter número, legenda, contexto, pertinência e vínculo técnico. | IBAPE/SP - cartilhas e boas práticas periciais | Fonte consultiva | [VERIFICAR ANTES DE USO REAL] |
| Originais devem ser preservados e derivados identificados quando integridade digital importar. | ABNT NBR ISO/IEC 27037 [norma paga - não reproduzir integralmente] | Fonte técnica | [VERIFICAR ANTES DE USO REAL] |
| Foto sem escala, baixa nitidez, corte relevante ou origem incerta deve receber ressalva. | Base técnica interna derivada de boas práticas de evidência | Fonte técnica interna | [VERIFICAR ANTES DE USO REAL] |

## Saídas Esperadas

- anexo fotográfico
- tabela de fotos
- legendas técnicas
- alertas de fotos fracas
- vínculo foto-quesito

## Regras de Segurança Técnica

- Não inventar norma, artigo, decisão judicial, edição de norma técnica ou número de portaria.
- Marcar como [VERIFICAR ANTES DE USO REAL] toda fonte temporal, local, paga, substituível ou dependente do processo concreto.
- Separar fonte oficial, fonte técnica e fonte consultiva em toda saída.
- Não reproduzir integralmente normas ABNT, livros comerciais, handbooks ou standards protegidos por licença.
- Não transformar cartilha, fabricante, literatura técnica ou boa prática em obrigação legal.

## Arquivos de Apoio

- `references/REFERENCIAS.md`
- `templates/ANEXO_FOTOGRAFICO.md`
- `checklists/CHECKLIST.md`
- `matrices/pericia-07-anexo-fotografico.csv`
- `examples/entrada.md`
- `examples/saida.md`
- `SEGURANCA_TECNICA.md`
- `LIMITACOES.md`
- `CRITERIOS_REVISAO.md`
