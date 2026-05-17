---
name: pericia-04-matriz-quesitos
description: Organizar quesitos do juízo, partes e assistentes em matriz rastreável com tema, método, evidência, status, resposta e limitação.
---

# Matriz de Quesitos

## Quando Usar

Use quando houver quesitos iniciais, suplementares, pedidos de esclarecimento ou necessidade de controlar completude das respostas.

## Entradas Esperadas

- quesitos do juízo
- quesitos das partes
- quesitos suplementares
- documentos e evidências
- limitações técnicas
- métodos disponíveis

## Fluxo Operacional

1. Ler a demanda e identificar processo, objeto, partes, tribunal, datas e documentos disponíveis.
2. Separar fontes oficiais, fontes técnicas, fontes consultivas e bases internas.
3. Aplicar as regras abaixo, citando fonte e marcando itens que exigem verificação antes de uso real.
4. Gerar a saída no template da skill, registrando evidências, limitações e pendências.
5. Executar o checklist e os critérios de revisão antes de entregar qualquer texto para uso externo.

## Regras Operacionais Com Fonte

| Regra operacional | Fonte | Tipo | Verificação |
|---|---|---|---|
| Quesitos devem ser controlados por origem, tema, status e resposta, evitando omissão no laudo. | CPC arts. 465, 469, 470, 473 e 477 | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Quesitos suplementares e esclarecimentos devem ser tratados como eventos rastreáveis, não como substituição informal do laudo. | CPC arts. 469 e 477 | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Resposta técnica deve ser objetiva, fundamentada e limitada ao campo pericial. | CPC art. 473; IBAPE/SP como boa prática | Fonte oficial e consultiva | [VERIFICAR ANTES DE USO REAL] |
| Quesitos jurídicos, conclusivos sobre culpa/dolo ou fora da especialidade devem receber ressalva técnica. | CPC art. 473; limites de atribuição profissional Confea/Crea | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |

## Saídas Esperadas

- matriz de quesitos
- lista de respostas pendentes
- mapa método-evidência
- alertas de quesito jurídico ou fora do escopo

## Regras de Segurança Técnica

- Não inventar norma, artigo, decisão judicial, edição de norma técnica ou número de portaria.
- Marcar como [VERIFICAR ANTES DE USO REAL] toda fonte temporal, local, paga, substituível ou dependente do processo concreto.
- Separar fonte oficial, fonte técnica e fonte consultiva em toda saída.
- Não reproduzir integralmente normas ABNT, livros comerciais, handbooks ou standards protegidos por licença.
- Não transformar cartilha, fabricante, literatura técnica ou boa prática em obrigação legal.

## Arquivos de Apoio

- `references/REFERENCIAS.md`
- `templates/MATRIZ_QUESITOS.md`
- `checklists/CHECKLIST.md`
- `matrices/pericia-04-matriz-quesitos.csv`
- `examples/entrada.md`
- `examples/saida.md`
- `SEGURANCA_TECNICA.md`
- `LIMITACOES.md`
- `CRITERIOS_REVISAO.md`
