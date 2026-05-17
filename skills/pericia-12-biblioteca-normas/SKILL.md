---
name: pericia-12-biblioteca-normas
description: Manter catálogo atualizável de fontes oficiais, técnicas e consultivas para perícia judicial de engenharia mecânica.
---

# Biblioteca de Normas e Métodos

## Quando Usar

Use para pesquisar, registrar, atualizar, classificar e auditar fontes que alimentam as demais skills.

## Entradas Esperadas

- fonte nova
- URL oficial
- norma ou publicação
- skill afetada
- tipo de fonte
- data de consulta
- necessidade de atualização

## Fluxo Operacional

1. Ler a demanda e identificar processo, objeto, partes, tribunal, datas e documentos disponíveis.
2. Separar fontes oficiais, fontes técnicas, fontes consultivas e bases internas.
3. Aplicar as regras abaixo, citando fonte e marcando itens que exigem verificação antes de uso real.
4. Gerar a saída no template da skill, registrando evidências, limitações e pendências.
5. Executar o checklist e os critérios de revisão antes de entregar qualquer texto para uso externo.

## Regras Operacionais Com Fonte

| Regra operacional | Fonte | Tipo | Verificação |
|---|---|---|---|
| Fonte primária deve prevalecer sobre comentário, resumo, blog ou material secundário. | Política de fontes do projeto; fontes oficiais Planalto/CNJ/TJCE/Confea/MTE/INMETRO | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Normas ABNT e livros comerciais devem ser cadastrados por metadados, escopo, notas próprias e forma legal de aquisição, sem cópia integral. | ABNT Catálogo; editoras técnicas | Fonte técnica paga | [VERIFICAR ANTES DE USO REAL] |
| Fonte consultiva deve ser marcada como boa prática ou apoio, sem virar obrigação legal. | IBAPE; literatura técnica; fabricantes | Fonte consultiva/técnica | [VERIFICAR ANTES DE USO REAL] |
| Fontes temporais devem ter frequência de verificação, impacto, procedimento de atualização e skills afetadas. | FONTES_OFICIAIS_ATUALIZAVEIS.md | Base interna rastreável | [VERIFICAR ANTES DE USO REAL] |

## Saídas Esperadas

- ficha de fonte
- registro de atualização
- matriz de impacto
- alertas de licença
- lista de skills afetadas

## Regras de Segurança Técnica

- Não inventar norma, artigo, decisão judicial, edição de norma técnica ou número de portaria.
- Marcar como [VERIFICAR ANTES DE USO REAL] toda fonte temporal, local, paga, substituível ou dependente do processo concreto.
- Separar fonte oficial, fonte técnica e fonte consultiva em toda saída.
- Não reproduzir integralmente normas ABNT, livros comerciais, handbooks ou standards protegidos por licença.
- Não transformar cartilha, fabricante, literatura técnica ou boa prática em obrigação legal.

## Arquivos de Apoio

- `references/REFERENCIAS.md`
- `templates/FICHA_FONTE_METODO.md`
- `checklists/CHECKLIST.md`
- `matrices/pericia-12-biblioteca-normas.csv`
- `examples/entrada.md`
- `examples/saida.md`
- `SEGURANCA_TECNICA.md`
- `LIMITACOES.md`
- `CRITERIOS_REVISAO.md`
