---
name: pericia-11-controle-prazos
description: Controlar prazos, marcos processuais, ciência, quesitos, assistentes, diligência, entrega do laudo, esclarecimentos, cadastro e documentos vencíveis.
---

# Controle de Prazos da Perícia

## Quando Usar

Use para transformar intimações, decisões e eventos do PJe/SIPER em uma agenda de acompanhamento da perícia.

## Entradas Esperadas

- intimações
- decisão de nomeação
- prazos indicados
- data de ciência
- eventos PJe/SIPER
- datas de diligência
- pedidos de esclarecimento

## Fluxo Operacional

1. Ler a demanda e identificar processo, objeto, partes, tribunal, datas e documentos disponíveis.
2. Separar fontes oficiais, fontes técnicas, fontes consultivas e bases internas.
3. Aplicar as regras abaixo, citando fonte e marcando itens que exigem verificação antes de uso real.
4. Gerar a saída no template da skill, registrando evidências, limitações e pendências.
5. Executar o checklist e os critérios de revisão antes de entregar qualquer texto para uso externo.

## Regras Operacionais Com Fonte

| Regra operacional | Fonte | Tipo | Verificação |
|---|---|---|---|
| Prazos devem partir da data de ciência e do teor da decisão/intimação; a skill deve marcar cálculo como conferência obrigatória. | CPC e decisão judicial concreta | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Quesitos, assistentes, laudo e esclarecimentos devem ser controlados por evento processual. | CPC arts. 465 e 477 | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Fluxos locais de cadastro, SIPER, PJe e pagamento devem ser conferidos quando aplicáveis ao TJCE. | TJCE; CNJ Res. 233/2016 | Fonte oficial local | [VERIFICAR ANTES DE USO REAL] |
| Certidões, cadastro, ART e documentos profissionais possuem validade operacional e devem entrar no controle. | Confea/Crea; TJCE | Fonte oficial/operacional | [VERIFICAR ANTES DE USO REAL] |

## Saídas Esperadas

- controle de prazos
- alertas
- eventos críticos
- pendências
- recomendações de petição

## Regras de Segurança Técnica

- Não inventar norma, artigo, decisão judicial, edição de norma técnica ou número de portaria.
- Marcar como [VERIFICAR ANTES DE USO REAL] toda fonte temporal, local, paga, substituível ou dependente do processo concreto.
- Separar fonte oficial, fonte técnica e fonte consultiva em toda saída.
- Não reproduzir integralmente normas ABNT, livros comerciais, handbooks ou standards protegidos por licença.
- Não transformar cartilha, fabricante, literatura técnica ou boa prática em obrigação legal.

## Arquivos de Apoio

- `references/REFERENCIAS.md`
- `templates/CONTROLE_PRAZOS_PERICIA.md`
- `checklists/CHECKLIST.md`
- `matrices/pericia-11-controle-prazos.csv`
- `examples/entrada.md`
- `examples/saida.md`
- `SEGURANCA_TECNICA.md`
- `LIMITACOES.md`
- `CRITERIOS_REVISAO.md`
