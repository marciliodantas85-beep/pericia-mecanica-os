# Tabelas - Inventário de Evidências

## Schema do inventário
| Campo | Descrição | Exemplo |
| --- | --- | --- |
| id_evidencia | Código único | EV-001 |
| tipo | foto, vídeo, documento, medição, peça, log | foto |
| origem | perito, parte, terceiro, autos | perito |
| data_hora_coleta | momento da coleta | 2026-05-16 09:15 |
| equipamento_relacionado | ativo, TAG, série | motobomba BC-01 |
| condicao_preservacao | original, cópia, indisponível | original preservado |
| quesitos_relacionados | IDs dos quesitos | Q1;Q3 |
| limitacoes | restrições de uso | sem escala |

## Status de evidência
| Status | Uso permitido | Exemplo |
| --- | --- | --- |
| válida | Pode fundamentar achado com demais elementos | foto original, medição calibrada |
| válida com ressalva | Usar com limitação explícita | foto com reflexo, mas contexto suficiente |
| em análise | Aguardar confirmação | documento sem assinatura verificável |
| indisponível | Registrar lacuna | peça removida não apresentada |
| não conclusiva isoladamente | Apoio contextual | screenshot sem arquivo nativo |
