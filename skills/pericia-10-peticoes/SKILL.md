---
name: pericia-10-peticoes
description: Gerar minutas de petições do perito judicial: aceite, escusa, honorários, diligência, pedido de documentos, prorrogação, juntada de laudo e esclarecimentos.
---

# Petições do Perito

## Quando Usar

Use quando o perito precisa peticionar no processo de forma impessoal, técnica e limitada ao encargo pericial.

## Entradas Esperadas

- tipo de petição
- processo
- decisão
- prazo
- pedido
- fundamento
- anexos
- fontes aplicáveis

## Fluxo Operacional

1. Ler a demanda e identificar processo, objeto, partes, tribunal, datas e documentos disponíveis.
2. Separar fontes oficiais, fontes técnicas, fontes consultivas e bases internas.
3. Aplicar as regras abaixo, citando fonte e marcando itens que exigem verificação antes de uso real.
4. Gerar a saída no template da skill, registrando evidências, limitações e pendências.
5. Executar o checklist e os critérios de revisão antes de entregar qualquer texto para uso externo.

## Regras Operacionais Com Fonte

| Regra operacional | Fonte | Tipo | Verificação |
|---|---|---|---|
| Petições do perito devem ser limitadas ao encargo, pedido processual claro e fundamento mínimo. | CPC arts. 156-158, 465, 466, 477 e correlatos | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Honorários devem citar regime do CPC e, quando aplicável, CNJ/tribunal local. | CPC art. 95; Resolução CNJ 232/2016; atos locais | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Diligência deve observar ciência das partes quando aplicável. | CPC art. 474 | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| ART e regularidade profissional podem ser informadas quando relevantes ao encargo. | Lei 6.496/1977; Confea/Crea | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| A linguagem deve ser neutra, impessoal e técnica; não deve defender parte. | CPC; Manual de Redação oficial como apoio | Fonte oficial/consultiva | [VERIFICAR ANTES DE USO REAL] |

## Saídas Esperadas

- minuta de petição
- checklist de protocolo
- lista de anexos
- alertas de fundamento e prazo

## Regras de Segurança Técnica

- Não inventar norma, artigo, decisão judicial, edição de norma técnica ou número de portaria.
- Marcar como [VERIFICAR ANTES DE USO REAL] toda fonte temporal, local, paga, substituível ou dependente do processo concreto.
- Separar fonte oficial, fonte técnica e fonte consultiva em toda saída.
- Não reproduzir integralmente normas ABNT, livros comerciais, handbooks ou standards protegidos por licença.
- Não transformar cartilha, fabricante, literatura técnica ou boa prática em obrigação legal.

## Arquivos de Apoio

- `references/REFERENCIAS.md`
- `templates/PETICAO_PERITO_MODELO.md`
- `checklists/CHECKLIST.md`
- `matrices/pericia-10-peticoes.csv`
- `examples/entrada.md`
- `examples/saida.md`
- `SEGURANCA_TECNICA.md`
- `LIMITACOES.md`
- `CRITERIOS_REVISAO.md`
