---
name: pericia-06-inventario-evidencias
description: Criar inventário rastreável de evidências físicas, documentais, digitais, fotográficas e metrológicas usadas na perícia.
---

# Inventário de Evidências

## Quando Usar

Use quando houver fotos, vídeos, peças, documentos, certificados, medições, logs, e-mails, manuais ou anexos que precisam ser controlados.

## Entradas Esperadas

- arquivos
- fotos
- documentos
- peças
- medições
- origem
- data
- autor
- quesitos vinculados

## Fluxo Operacional

1. Ler a demanda e identificar processo, objeto, partes, tribunal, datas e documentos disponíveis.
2. Separar fontes oficiais, fontes técnicas, fontes consultivas e bases internas.
3. Aplicar as regras abaixo, citando fonte e marcando itens que exigem verificação antes de uso real.
4. Gerar a saída no template da skill, registrando evidências, limitações e pendências.
5. Executar o checklist e os critérios de revisão antes de entregar qualquer texto para uso externo.

## Regras Operacionais Com Fonte

| Regra operacional | Fonte | Tipo | Verificação |
|---|---|---|---|
| O laudo pode ser instruído por fotografias, desenhos e elementos materiais necessários. | CPC art. 473 §3º | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Origem, data, autoria, integridade e cópia de trabalho devem ser registradas quando evidência digital for relevante. | ABNT NBR ISO/IEC 27037 [norma paga - não reproduzir integralmente] | Fonte técnica | [VERIFICAR ANTES DE USO REAL] |
| A lógica de cadeia de custódia pode ser usada por analogia metodológica, sem converter regra penal em obrigação cível automática. | CPP arts. 158-A e seguintes [uso analógico] | Fonte oficial por analogia | [VERIFICAR ANTES DE USO REAL] |
| Certificados e medições devem ser vinculados a instrumento, unidade, rastreabilidade e condição de medição. | INMETRO/Cgcre; GUM/VIM | Fonte técnica oficial | [VERIFICAR ANTES DE USO REAL] |

## Saídas Esperadas

- inventário de evidências
- manifesto de arquivos
- hashes quando cabíveis
- vínculo evidência-quesito-laudo
- alertas de integridade

## Regras de Segurança Técnica

- Não inventar norma, artigo, decisão judicial, edição de norma técnica ou número de portaria.
- Marcar como [VERIFICAR ANTES DE USO REAL] toda fonte temporal, local, paga, substituível ou dependente do processo concreto.
- Separar fonte oficial, fonte técnica e fonte consultiva em toda saída.
- Não reproduzir integralmente normas ABNT, livros comerciais, handbooks ou standards protegidos por licença.
- Não transformar cartilha, fabricante, literatura técnica ou boa prática em obrigação legal.

## Arquivos de Apoio

- `references/REFERENCIAS.md`
- `templates/INVENTARIO_EVIDENCIAS.md`
- `checklists/CHECKLIST.md`
- `matrices/pericia-06-inventario-evidencias.csv`
- `examples/entrada.md`
- `examples/saida.md`
- `SEGURANCA_TECNICA.md`
- `LIMITACOES.md`
- `CRITERIOS_REVISAO.md`
