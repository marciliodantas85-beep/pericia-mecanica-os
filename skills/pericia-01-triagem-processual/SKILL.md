---
name: pericia-01-triagem-processual
description: Triar nomeação, objeto pericial, competência técnica, riscos processuais, atribuições profissionais, ART e próximos atos do perito judicial de engenharia mecânica.
---

# Triagem Processual da Perícia

## Quando Usar

Use quando chegar uma nomeação, intimação, despacho, termo de perícia ou conjunto inicial de autos e for necessário decidir aceite, impedimento, suspeição, suficiência documental, lacunas e providências iniciais.

## Entradas Esperadas

- decisão de nomeação ou despacho
- dados do processo e partes
- objeto da perícia
- quesitos iniciais, se houver
- documentos técnicos disponíveis
- tribunal e comarca

## Fluxo Operacional

1. Ler a demanda e identificar processo, objeto, partes, tribunal, datas e documentos disponíveis.
2. Separar fontes oficiais, fontes técnicas, fontes consultivas e bases internas.
3. Aplicar as regras abaixo, citando fonte e marcando itens que exigem verificação antes de uso real.
4. Gerar a saída no template da skill, registrando evidências, limitações e pendências.
5. Executar o checklist e os critérios de revisão antes de entregar qualquer texto para uso externo.

## Regras Operacionais Com Fonte

| Regra operacional | Fonte | Tipo | Verificação |
|---|---|---|---|
| A perícia judicial deve envolver conhecimento técnico e perito habilitado; a skill deve checar aderência do objeto às atribuições profissionais. | CPC arts. 156-158 e 464-480; Lei 5.194/1966; Resoluções Confea sobre atribuições | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Impedimento, suspeição, escopo, prazo e deveres do perito devem ser triados antes de sugerir aceite. | CPC arts. 156-158 e 464-480 | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| A necessidade de ART e compatibilidade com TOS devem ser sinalizadas antes do trabalho técnico. | Lei 6.496/1977; Normativos Confea/Crea | Fonte oficial | [VERIFICAR ANTES DE USO REAL] |
| Cadastro, documentação e fluxo local devem ser conferidos quando a atuação for no TJCE. | CNJ Res. 233/2016; páginas oficiais TJCE/SIPER | Fonte oficial local | [VERIFICAR ANTES DE USO REAL] |
| Boa prática de perícia não substitui regra processual; cartilhas devem ser usadas apenas como apoio metodológico. | IBAPE Nacional/IBAPE-SP | Fonte consultiva | [VERIFICAR ANTES DE USO REAL] |

## Saídas Esperadas

- relatório de triagem
- matriz de riscos de aceite
- lista de lacunas documentais
- alertas de prazo
- recomendação técnica de aceite, ressalva ou pedido de esclarecimento

## Regras de Segurança Técnica

- Não inventar norma, artigo, decisão judicial, edição de norma técnica ou número de portaria.
- Marcar como [VERIFICAR ANTES DE USO REAL] toda fonte temporal, local, paga, substituível ou dependente do processo concreto.
- Separar fonte oficial, fonte técnica e fonte consultiva em toda saída.
- Não reproduzir integralmente normas ABNT, livros comerciais, handbooks ou standards protegidos por licença.
- Não transformar cartilha, fabricante, literatura técnica ou boa prática em obrigação legal.

## Arquivos de Apoio

- `references/REFERENCIAS.md`
- `templates/RELATORIO_TRIAGEM_PROCESSUAL.md`
- `checklists/CHECKLIST.md`
- `matrices/pericia-01-triagem-processual.csv`
- `examples/entrada.md`
- `examples/saida.md`
- `SEGURANCA_TECNICA.md`
- `LIMITACOES.md`
- `CRITERIOS_REVISAO.md`
