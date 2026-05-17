---
name: pericia-09-revisao-impugnacao
description: Revisar laudo, parecer técnico, impugnação ou pedido de esclarecimentos, apontando omissões, riscos, inconsistências, falta de método e resposta a quesitos.
---

# Revisor de Laudo e Impugnação

## Quando Usar

Use antes de protocolar laudo, ao responder impugnação, ao analisar parecer de assistente ou ao preparar esclarecimentos.

## Entradas Esperadas

- laudo
- matriz de quesitos
- impugnação
- parecer de assistente
- evidências
- fontes citadas
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
| O laudo deve ser revisado contra os requisitos mínimos de objeto, método, análise e respostas a quesitos. | CPC art. 473 | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Pedidos de esclarecimento e omissões devem ser tratados com rastreio por quesito e evidência. | CPC art. 477 | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Segunda perícia só deve ser tratada como hipótese quando a matéria não estiver esclarecida; a skill não decide deferimento. | CPC art. 480 | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Regularidade profissional, ART e atribuição podem ser pontos de vulnerabilidade formal. | Lei 5.194/1966; Lei 6.496/1977; Confea/Crea | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Normas técnicas e cartilhas devem ser classificadas corretamente para evitar uso como obrigação indevida. | ABNT; IBAPE | Fonte técnica/consultiva | [VERIFICAR ANTES DE USO REAL] |

## Saídas Esperadas

- relatório de revisão
- matriz de achados
- riscos de impugnação
- sugestões de esclarecimento
- pontos a corrigir

## Regras de Segurança Técnica

- Não inventar norma, artigo, decisão judicial, edição de norma técnica ou número de portaria.
- Marcar como [VERIFICAR ANTES DE USO REAL] toda fonte temporal, local, paga, substituível ou dependente do processo concreto.
- Separar fonte oficial, fonte técnica e fonte consultiva em toda saída.
- Não reproduzir integralmente normas ABNT, livros comerciais, handbooks ou standards protegidos por licença.
- Não transformar cartilha, fabricante, literatura técnica ou boa prática em obrigação legal.

## Arquivos de Apoio

- `references/REFERENCIAS.md`
- `templates/RELATORIO_REVISAO_IMPUGNACAO.md`
- `checklists/CHECKLIST.md`
- `matrices/pericia-09-revisao-impugnacao.csv`
- `examples/entrada.md`
- `examples/saida.md`
- `SEGURANCA_TECNICA.md`
- `LIMITACOES.md`
- `CRITERIOS_REVISAO.md`
