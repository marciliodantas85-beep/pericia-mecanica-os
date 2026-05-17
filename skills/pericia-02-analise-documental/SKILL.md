---
name: pericia-02-analise-documental
description: Classificar documentos dos autos, vincular alegações a evidências, apontar lacunas, inconsistências, força documental e necessidade de diligência.
---

# Análise Documental Processual

## Quando Usar

Use quando houver petição inicial, contestação, documentos técnicos, manuais, notas, relatórios, fotos, certificados ou histórico de manutenção a serem organizados antes do laudo.

## Entradas Esperadas

- lista de documentos dos autos
- alegações das partes
- quesitos
- manuais e relatórios técnicos
- certificados de ensaio/calibração
- fotos e anexos

## Fluxo Operacional

1. Ler a demanda e identificar processo, objeto, partes, tribunal, datas e documentos disponíveis.
2. Separar fontes oficiais, fontes técnicas, fontes consultivas e bases internas.
3. Aplicar as regras abaixo, citando fonte e marcando itens que exigem verificação antes de uso real.
4. Gerar a saída no template da skill, registrando evidências, limitações e pendências.
5. Executar o checklist e os critérios de revisão antes de entregar qualquer texto para uso externo.

## Regras Operacionais Com Fonte

| Regra operacional | Fonte | Tipo | Verificação |
|---|---|---|---|
| Documento processual deve ser ligado à alegação e ao ponto controvertido; documento não prova automaticamente o fato técnico. | CPC arts. 319, 320, 336, 369 e 434 | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Documentos técnicos devem ser classificados por origem, data, integridade, pertinência, força e vínculo com quesitos. | Base metodológica interna derivada de CPC e boas práticas periciais | Fonte técnica interna | [VERIFICAR ANTES DE USO REAL] |
| Certificados e relatórios de ensaio devem ser avaliados por laboratório, escopo, rastreabilidade, data e pertinência da grandeza. | INMETRO/Cgcre; ABNT NBR ISO/IEC 17025 como referência técnica paga | Fonte técnica | [VERIFICAR ANTES DE USO REAL] |
| Fotos, PDFs nativos, logs e arquivos eletrônicos devem preservar original e cópia de trabalho quando integridade importar. | ABNT NBR ISO/IEC 27037; POPs oficiais por analogia metodológica | Fonte técnica | [VERIFICAR ANTES DE USO REAL] |
| Materiais IBAPE ajudam a estruturar análise, mas não substituem CPC nem norma técnica aplicável. | IBAPE Nacional/IBAPE-SP | Fonte consultiva | [VERIFICAR ANTES DE USO REAL] |

## Saídas Esperadas

- relatório de análise documental
- matriz documental
- lista de lacunas
- alertas de autenticidade/integridade
- documentos a solicitar

## Regras de Segurança Técnica

- Não inventar norma, artigo, decisão judicial, edição de norma técnica ou número de portaria.
- Marcar como [VERIFICAR ANTES DE USO REAL] toda fonte temporal, local, paga, substituível ou dependente do processo concreto.
- Separar fonte oficial, fonte técnica e fonte consultiva em toda saída.
- Não reproduzir integralmente normas ABNT, livros comerciais, handbooks ou standards protegidos por licença.
- Não transformar cartilha, fabricante, literatura técnica ou boa prática em obrigação legal.

## Arquivos de Apoio

- `references/REFERENCIAS.md`
- `templates/RELATORIO_ANALISE_DOCUMENTAL.md`
- `checklists/CHECKLIST.md`
- `matrices/pericia-02-analise-documental.csv`
- `examples/entrada.md`
- `examples/saida.md`
- `SEGURANCA_TECNICA.md`
- `LIMITACOES.md`
- `CRITERIOS_REVISAO.md`
