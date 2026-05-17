---
name: pericia-08-laudo-mecanico
description: Gerar estrutura e minuta de laudo pericial judicial de engenharia mecânica com método, análise, evidências, respostas a quesitos, conclusão e limitações.
---

# Gerador de Laudo Pericial Mecânico

## Quando Usar

Use para montar laudo a partir de autos, diligência, matriz documental, matriz de quesitos, inventário de evidências, medições e análise técnica.

## Entradas Esperadas

- dados do processo
- objeto
- matriz documental
- matriz de quesitos
- inventário de evidências
- roteiro/ata de diligência
- método técnico
- anexo fotográfico

## Fluxo Operacional

1. Ler a demanda e identificar processo, objeto, partes, tribunal, datas e documentos disponíveis.
2. Separar fontes oficiais, fontes técnicas, fontes consultivas e bases internas.
3. Aplicar as regras abaixo, citando fonte e marcando itens que exigem verificação antes de uso real.
4. Gerar a saída no template da skill, registrando evidências, limitações e pendências.
5. Executar o checklist e os critérios de revisão antes de entregar qualquer texto para uso externo.

## Regras Operacionais Com Fonte

| Regra operacional | Fonte | Tipo | Verificação |
|---|---|---|---|
| O laudo deve conter objeto, análise técnica/científica, método utilizado e resposta conclusiva a todos os quesitos. | CPC art. 473 | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Conclusões devem ser vinculadas a evidência, documento, medição, norma, manual ou limitação. | CPC art. 473; boas práticas IBAPE | Fonte oficial e consultiva | [VERIFICAR ANTES DE USO REAL] |
| O laudo deve indicar habilitação profissional, registro, ART quando cabível e limites de atribuição. | Lei 5.194/1966; Lei 6.496/1977; Confea/Crea | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Normas ABNT e literatura técnica podem fundamentar método, mas não devem ser copiadas integralmente. | ABNT Catálogo; literatura técnica com licença | Fonte técnica | [VERIFICAR ANTES DE USO REAL] |
| Em segurança de máquinas, verificar NR-12 vigente e data do fato antes de concluir conformidade. | NR-12/MTE | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |

## Saídas Esperadas

- laudo pericial mecânico
- respostas a quesitos
- quadro de evidências
- limitações
- anexos sugeridos
- alertas anti-impugnação

## Regras de Segurança Técnica

- Não inventar norma, artigo, decisão judicial, edição de norma técnica ou número de portaria.
- Marcar como [VERIFICAR ANTES DE USO REAL] toda fonte temporal, local, paga, substituível ou dependente do processo concreto.
- Separar fonte oficial, fonte técnica e fonte consultiva em toda saída.
- Não reproduzir integralmente normas ABNT, livros comerciais, handbooks ou standards protegidos por licença.
- Não transformar cartilha, fabricante, literatura técnica ou boa prática em obrigação legal.

## Arquivos de Apoio

- `references/REFERENCIAS.md`
- `templates/LAUDO_PERICIAL_MECANICO.md`
- `checklists/CHECKLIST.md`
- `matrices/pericia-08-laudo-mecanico.csv`
- `examples/entrada.md`
- `examples/saida.md`
- `SEGURANCA_TECNICA.md`
- `LIMITACOES.md`
- `CRITERIOS_REVISAO.md`
