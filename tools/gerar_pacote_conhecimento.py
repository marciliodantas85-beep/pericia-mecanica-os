import csv
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = date.today().isoformat()


COMMON_WARNINGS = [
    "Não inventar norma, artigo, decisão judicial, edição de norma técnica ou número de portaria.",
    "Marcar como [VERIFICAR ANTES DE USO REAL] toda fonte temporal, local, paga, substituível ou dependente do processo concreto.",
    "Separar fonte oficial, fonte técnica e fonte consultiva em toda saída.",
    "Não reproduzir integralmente normas ABNT, livros comerciais, handbooks ou standards protegidos por licença.",
    "Não transformar cartilha, fabricante, literatura técnica ou boa prática em obrigação legal.",
]


GLOBAL_SOURCES = {
    "CPC": "Código de Processo Civil - Lei 13.105/2015, texto compilado no Planalto [VERIFICAR ANTES DE USO REAL]",
    "CNJ": "Atos normativos CNJ, especialmente Resoluções 232/2016 e 233/2016 [VERIFICAR ANTES DE USO REAL]",
    "TJCE": "Página oficial do TJCE sobre credenciamento, portarias, tabelas, SIPER e PJe [VERIFICAR ANTES DE USO REAL]",
    "CONFEA": "Normativos Confea, incluindo regras sobre perícia, atribuições, ART, acervo e TOS [VERIFICAR ANTES DE USO REAL]",
    "CREA-CE": "Portal e manuais operacionais do CREA-CE [VERIFICAR ANTES DE USO REAL]",
    "ABNT": "ABNT Catálogo para status, edição e aquisição legal de normas técnicas [VERIFICAR ANTES DE USO REAL]",
    "IBAPE": "Bibliotecas, cartilhas, boletins e normas institucionais do IBAPE Nacional e IBAPE/SP [VERIFICAR ANTES DE USO REAL]",
    "MTE_NR12": "Página oficial do Ministério do Trabalho e Emprego para NR-12 e normas regulamentadoras [VERIFICAR ANTES DE USO REAL]",
    "INMETRO": "INMETRO/Cgcre, GUM, VIM, organismos acreditados, RBC/RBLE e documentos técnicos [VERIFICAR ANTES DE USO REAL]",
    "FABRICANTE": "Manual, catálogo, folha técnica e boletim oficial do fabricante do equipamento ou componente [VERIFICAR POR CASO]",
    "LITERATURA": "Literatura técnica de análise de falhas, RCFA, manutenção e elementos de máquinas [VERIFICAR EDIÇÃO/LICENÇA]",
}


def rule(text, source, kind, verify="[VERIFICAR ANTES DE USO REAL]"):
    return {"regra": text, "fonte": source, "tipo": kind, "verificacao": verify}


SKILLS = [
    {
        "id": "pericia-01-triagem-processual",
        "title": "Triagem Processual da Perícia",
        "description": "Triar nomeação, objeto pericial, competência técnica, riscos processuais, atribuições profissionais, ART e próximos atos do perito judicial de engenharia mecânica.",
        "use_when": "Use quando chegar uma nomeação, intimação, despacho, termo de perícia ou conjunto inicial de autos e for necessário decidir aceite, impedimento, suspeição, suficiência documental, lacunas e providências iniciais.",
        "inputs": ["decisão de nomeação ou despacho", "dados do processo e partes", "objeto da perícia", "quesitos iniciais, se houver", "documentos técnicos disponíveis", "tribunal e comarca"],
        "outputs": ["relatório de triagem", "matriz de riscos de aceite", "lista de lacunas documentais", "alertas de prazo", "recomendação técnica de aceite, ressalva ou pedido de esclarecimento"],
        "rules": [
            rule("A perícia judicial deve envolver conhecimento técnico e perito habilitado; a skill deve checar aderência do objeto às atribuições profissionais.", "CPC arts. 156-158 e 464-480; Lei 5.194/1966; Resoluções Confea sobre atribuições", "Fonte oficial"),
            rule("Impedimento, suspeição, escopo, prazo e deveres do perito devem ser triados antes de sugerir aceite.", "CPC arts. 156-158 e 464-480", "Fonte oficial"),
            rule("A necessidade de ART e compatibilidade com TOS devem ser sinalizadas antes do trabalho técnico.", "Lei 6.496/1977; Normativos Confea/Crea", "Fonte oficial"),
            rule("Cadastro, documentação e fluxo local devem ser conferidos quando a atuação for no TJCE.", "CNJ Res. 233/2016; páginas oficiais TJCE/SIPER", "Fonte oficial local"),
            rule("Boa prática de perícia não substitui regra processual; cartilhas devem ser usadas apenas como apoio metodológico.", "IBAPE Nacional/IBAPE-SP", "Fonte consultiva"),
        ],
        "checklist": ["Processo, vara, comarca e classe conferidos", "Objeto técnico delimitado", "Partes e assistentes identificados", "Prazos e data de ciência registrados", "Impedimento/suspeição avaliados", "Atribuição mecânica conferida", "ART prevista ou ressalvada", "Fontes locais do tribunal verificadas", "Lacunas documentais listadas", "Saída classificada como preliminar quando faltar documento"],
        "matrix_headers": ["item", "status", "fonte", "risco", "ação_recomendada", "verificacao"],
        "matrix_rows": [
            ["Objeto pericial", "preencher", "CPC arts. 464-480", "escopo indefinido", "pedir esclarecimento ou delimitar hipóteses", "sim"],
            ["Atribuição profissional", "preencher", "Lei 5.194/1966; Confea", "atuação fora do campo mecânico", "validar registro e atribuições", "sim"],
            ["Cadastro local", "preencher", "CNJ 233/2016; TJCE", "fluxo operacional incorreto", "conferir SIPER/PJe e portarias", "sim"],
        ],
        "template_name": "RELATORIO_TRIAGEM_PROCESSUAL.md",
        "template": "# Relatório de Triagem Processual\n\n## Identificação\n- Processo:\n- Vara/Comarca:\n- Data de ciência:\n- Objeto informado:\n\n## Síntese da Nomeação\n\n## Aderência Técnica\n\n## Fontes Consultadas\n- CPC: [VERIFICAR ANTES DE USO REAL]\n- Confea/Crea: [VERIFICAR ANTES DE USO REAL]\n- Tribunal local: [VERIFICAR ANTES DE USO REAL]\n\n## Riscos e Lacunas\n\n## Providências Recomendadas\n",
        "example_input": "Despacho nomeia engenheiro mecânico para apurar falha em elevador industrial, com quesitos das partes e prazo de 30 dias para laudo.",
        "example_output": "Triagem indica objeto compatível com engenharia mecânica, necessidade de conferir atribuições/ART, intimação das partes para diligência, documentos faltantes de manutenção e manuais do fabricante. Fontes temporais marcadas para verificação.",
        "limitations": ["Não decide impedimento ou suspeição de forma jurídica definitiva.", "Não substitui leitura integral dos autos.", "Não confirma cadastro ativo sem consulta ao tribunal.", "Não valida atribuição profissional sem consulta ao CREA competente quando houver dúvida."],
        "review": ["A fonte de cada regra está citada?", "Há marcação de verificação temporal?", "O objeto foi delimitado sem assumir fatos não comprovados?", "Há separação entre risco processual e risco técnico?"],
    },
    {
        "id": "pericia-02-analise-documental",
        "title": "Análise Documental Processual",
        "description": "Classificar documentos dos autos, vincular alegações a evidências, apontar lacunas, inconsistências, força documental e necessidade de diligência.",
        "use_when": "Use quando houver petição inicial, contestação, documentos técnicos, manuais, notas, relatórios, fotos, certificados ou histórico de manutenção a serem organizados antes do laudo.",
        "inputs": ["lista de documentos dos autos", "alegações das partes", "quesitos", "manuais e relatórios técnicos", "certificados de ensaio/calibração", "fotos e anexos"],
        "outputs": ["relatório de análise documental", "matriz documental", "lista de lacunas", "alertas de autenticidade/integridade", "documentos a solicitar"],
        "rules": [
            rule("Documento processual deve ser ligado à alegação e ao ponto controvertido; documento não prova automaticamente o fato técnico.", "CPC arts. 319, 320, 336, 369 e 434", "Fonte oficial"),
            rule("Documentos técnicos devem ser classificados por origem, data, integridade, pertinência, força e vínculo com quesitos.", "Base metodológica interna derivada de CPC e boas práticas periciais", "Fonte técnica interna"),
            rule("Certificados e relatórios de ensaio devem ser avaliados por laboratório, escopo, rastreabilidade, data e pertinência da grandeza.", "INMETRO/Cgcre; ABNT NBR ISO/IEC 17025 como referência técnica paga", "Fonte técnica"),
            rule("Fotos, PDFs nativos, logs e arquivos eletrônicos devem preservar original e cópia de trabalho quando integridade importar.", "ABNT NBR ISO/IEC 27037; POPs oficiais por analogia metodológica", "Fonte técnica"),
            rule("Materiais IBAPE ajudam a estruturar análise, mas não substituem CPC nem norma técnica aplicável.", "IBAPE Nacional/IBAPE-SP", "Fonte consultiva"),
        ],
        "checklist": ["Autos e anexos listados", "Alegações principais extraídas", "Documentos vinculados a alegações", "Quesitos associados", "Datas e autoria conferidas", "Integridade e legibilidade avaliadas", "Certificados verificados", "Manuais do fabricante identificados", "Lacunas documentais listadas", "Conclusões marcadas como preliminares quando cabível"],
        "matrix_headers": ["id_documento", "tipo", "origem", "data", "alegacao_relacionada", "quesito", "forca_documental", "integridade", "lacuna", "fonte_regra"],
        "matrix_rows": [
            ["DOC-001", "manual", "fabricante", "preencher", "uso/manutenção", "Q-01", "alta se modelo/série compatíveis", "verificar versão", "confirmar equipamento", "manual oficial do fabricante"],
            ["DOC-002", "certificado", "laboratório", "preencher", "medição", "Q-02", "depende de escopo/rastreabilidade", "verificar validade", "confirmar RBC/Cgcre", "INMETRO/Cgcre"],
            ["DOC-003", "foto", "parte/autos", "preencher", "dano", "Q-03", "média", "verificar metadados/original", "pedir original se necessário", "CPC art. 473 §3º; ISO/IEC 27037"],
        ],
        "template_name": "RELATORIO_ANALISE_DOCUMENTAL.md",
        "template": "# Relatório de Análise Documental\n\n## Escopo\n\n## Documentos Recebidos\n\n## Matriz Alegação x Documento x Quesito\n\n## Lacunas e Inconsistências\n\n## Documentos a Solicitar\n\n## Limitações\n\n## Fontes e Verificações\n",
        "example_input": "Autos contêm contrato de manutenção, fotos do dano, nota fiscal de rolamento, certificado de vibração e manual genérico do equipamento.",
        "example_output": "Matriz aponta que o manual não está vinculado ao número de série, o certificado exige verificação de escopo, e as fotos precisam de origem/data para uso como evidência técnica.",
        "limitations": ["Não autentica documento como perícia grafotécnica.", "Não substitui consulta ao arquivo original quando metadados importarem.", "Não conclui causalidade apenas por documento isolado.", "Não transforma ausência documental em fato provado."],
        "review": ["Cada documento tem origem e data?", "Há vínculo com alegação e quesito?", "Certificados foram marcados para validação?", "A conclusão separa fato documentado de inferência técnica?"],
    },
    {
        "id": "pericia-03-proposta-honorarios",
        "title": "Proposta de Honorários Periciais",
        "description": "Montar proposta de honorários, memória de cálculo, justificativa técnica, despesas, ART e alertas de regime de custeio.",
        "use_when": "Use quando o perito precisa apresentar proposta de honorários, pedir complementação, justificar complexidade ou adequar valor a tabela local.",
        "inputs": ["objeto da perícia", "decisão de nomeação", "prazo", "tabela local, se houver", "gratuidade ou custeio pelas partes", "deslocamentos", "estimativa de horas", "necessidade de ensaios ou equipe"],
        "outputs": ["proposta de honorários", "memória de cálculo", "rubricas e justificativas", "alertas de verificação CNJ/TJCE", "minuta de petição quando aplicável"],
        "rules": [
            rule("O regime de adiantamento, rateio e custeio deve partir do CPC e da decisão judicial.", "CPC art. 95", "Fonte oficial"),
            rule("Honorários em justiça gratuita devem considerar atos CNJ e tabela local aplicável quando existente.", "Resolução CNJ 232/2016; atos do tribunal local", "Fonte oficial"),
            rule("No TJCE, tabela, portaria e fluxo de pagamento devem ser conferidos antes de fixar rubrica e valor.", "Página oficial TJCE de credenciamento, resoluções e portarias", "Fonte oficial local"),
            rule("ART, deslocamento, ensaios, equipe e complexidade devem ser descritos como composição técnica, não como certeza de deferimento.", "Lei 6.496/1977; Confea/Crea; CPC art. 95", "Fonte oficial"),
            rule("Regulamentos de honorários de entidade profissional podem apoiar a memória de cálculo, sem substituir tabela judicial ou decisão.", "IBAPE/SP ou entidade profissional", "Fonte consultiva"),
        ],
        "checklist": ["Regime de custeio identificado", "Gratuidade verificada", "Tabela local conferida", "Rubrica selecionada", "Horas por etapa estimadas", "Despesas e deslocamentos discriminados", "ART prevista", "Ensaios/equipe justificados", "Pedidos claros", "Fontes temporais marcadas para verificação"],
        "matrix_headers": ["rubrica", "descricao", "quantidade", "unidade", "valor_unitario", "subtotal", "fonte", "verificacao"],
        "matrix_rows": [
            ["Estudo dos autos", "leitura e matriz documental", "preencher", "h", "preencher", "preencher", "CPC art. 95", "sim"],
            ["Diligência", "vistoria técnica e registro", "preencher", "h/deslocamento", "preencher", "preencher", "CPC arts. 466/474; TJCE se aplicável", "sim"],
            ["ART", "responsabilidade técnica", "1", "un", "preencher", "preencher", "Lei 6.496/1977; Confea/Crea", "sim"],
        ],
        "template_name": "PROPOSTA_HONORARIOS_PERICIAIS.md",
        "template": "# Proposta de Honorários Periciais\n\n## Identificação\n- Processo:\n- Perito:\n- Objeto:\n\n## Base Normativa\n- CPC art. 95: [VERIFICAR ANTES DE USO REAL]\n- CNJ/TJCE, se aplicável: [VERIFICAR ANTES DE USO REAL]\n\n## Escopo Técnico Estimado\n\n## Memória de Cálculo\n\n## Despesas e ART\n\n## Pedido\n",
        "example_input": "Nomeação para perícia em máquina industrial com análise documental, vistoria em outro município, fotos, medições e resposta a 18 quesitos.",
        "example_output": "Proposta separa horas de autos, diligência, análise técnica, elaboração do laudo, ART e deslocamento, com alerta para conferir tabela TJCE/CNJ antes do protocolo.",
        "limitations": ["Não garante deferimento do valor.", "Não calcula tabela local sem fonte vigente.", "Não substitui decisão judicial sobre custeio.", "Não inclui tributos sem regra ou orientação contábil específica."],
        "review": ["A proposta cita CPC art. 95?", "CNJ/TJCE foram marcados para conferência?", "A memória separa horas, despesas e ART?", "O pedido é claro e processualmente neutro?"],
    },
    {
        "id": "pericia-04-matriz-quesitos",
        "title": "Matriz de Quesitos",
        "description": "Organizar quesitos do juízo, partes e assistentes em matriz rastreável com tema, método, evidência, status, resposta e limitação.",
        "use_when": "Use quando houver quesitos iniciais, suplementares, pedidos de esclarecimento ou necessidade de controlar completude das respostas.",
        "inputs": ["quesitos do juízo", "quesitos das partes", "quesitos suplementares", "documentos e evidências", "limitações técnicas", "métodos disponíveis"],
        "outputs": ["matriz de quesitos", "lista de respostas pendentes", "mapa método-evidência", "alertas de quesito jurídico ou fora do escopo"],
        "rules": [
            rule("Quesitos devem ser controlados por origem, tema, status e resposta, evitando omissão no laudo.", "CPC arts. 465, 469, 470, 473 e 477", "Fonte oficial"),
            rule("Quesitos suplementares e esclarecimentos devem ser tratados como eventos rastreáveis, não como substituição informal do laudo.", "CPC arts. 469 e 477", "Fonte oficial"),
            rule("Resposta técnica deve ser objetiva, fundamentada e limitada ao campo pericial.", "CPC art. 473; IBAPE/SP como boa prática", "Fonte oficial e consultiva"),
            rule("Quesitos jurídicos, conclusivos sobre culpa/dolo ou fora da especialidade devem receber ressalva técnica.", "CPC art. 473; limites de atribuição profissional Confea/Crea", "Fonte oficial"),
        ],
        "checklist": ["Origem do quesito registrada", "Número original preservado", "Tema técnico atribuído", "Método indicado", "Evidência vinculada", "Status de resposta definido", "Limitação registrada", "Quesito jurídico marcado", "Suplementares separados", "Conferência final contra laudo realizada"],
        "matrix_headers": ["id_quesito", "origem", "texto_resumido", "tema", "metodo", "evidencia", "status", "resposta_resumida", "limitacao", "fonte_regra"],
        "matrix_rows": [
            ["QJ-01", "juízo", "preencher", "escopo", "análise documental", "DOC-001", "pendente", "preencher", "", "CPC art. 473"],
            ["QA-01", "autor", "preencher", "causa de falha", "inspeção/RCFA", "EVD-001", "pendente", "preencher", "depende de vistoria", "CPC arts. 465/469"],
            ["QR-01", "réu", "preencher", "manutenção", "documental + diligência", "DOC-002", "pendente", "preencher", "", "CPC art. 477 se esclarecimento"],
        ],
        "template_name": "MATRIZ_QUESITOS.md",
        "template": "# Matriz de Quesitos\n\n| ID | Origem | Quesito resumido | Tema | Método | Evidência | Status | Resposta | Limitação |\n|---|---|---|---|---|---|---|---|---|\n\n## Alertas\n- Quesitos jurídicos:\n- Quesitos fora do escopo:\n- Quesitos sem evidência suficiente:\n",
        "example_input": "Parte autora pergunta se a falha ocorreu por defeito de fabricação; ré pergunta se houve manutenção inadequada; juízo pede causa provável.",
        "example_output": "Matriz separa fabricação, manutenção e causa provável, exige manual do fabricante, histórico de manutenção, inspeção do componente e marca limites antes de responder.",
        "limitations": ["Não responde quesito sem fonte de evidência ou limitação clara.", "Não decide matéria jurídica.", "Não altera numeração original dos quesitos.", "Não oculta quesitos prejudicados ou sem resposta."],
        "review": ["Todos os quesitos aparecem uma vez?", "Há resposta para cada quesito deferido?", "A evidência está vinculada?", "Quesitos jurídicos foram ressalvados?"],
    },
    {
        "id": "pericia-05-roteiro-diligencia",
        "title": "Roteiro de Diligência Mecânica",
        "description": "Planejar diligência, vistoria, segurança, coleta de evidências, medições, entrevistas técnicas, fotos e ata para perícia mecânica.",
        "use_when": "Use antes de vistoria em máquina, instalação, componente, oficina, indústria, local de acidente, armazenamento de peça ou inspeção documental em campo.",
        "inputs": ["objeto pericial", "local", "partes e assistentes", "quesitos", "riscos de segurança", "máquina/componente", "documentos e manuais", "medidas necessárias"],
        "outputs": ["roteiro de diligência", "checklist de campo", "ata de vistoria", "plano fotográfico", "lista de documentos a solicitar", "alertas de segurança"],
        "rules": [
            rule("As partes devem ter ciência da diligência quando o contraditório técnico exigir participação ou acompanhamento.", "CPC art. 474", "Fonte oficial"),
            rule("O perito pode usar meios necessários, ouvir pessoas e instruir o laudo com fotos, desenhos e elementos materiais.", "CPC arts. 466 e 473 §3º", "Fonte oficial"),
            rule("Diligência em máquina deve considerar riscos, proteção, energia, operação, manutenção e condição segura.", "NR-12/MTE; normas técnicas correlatas", "Fonte oficial/técnica"),
            rule("Apreciação de riscos deve considerar limites da máquina, perigos, uso previsto, mau uso previsível e risco residual.", "ABNT NBR ISO 12100 [norma paga - não reproduzir integralmente]", "Fonte técnica"),
            rule("Manual do fabricante deve ser conferido por modelo/série quando houver instruções de instalação, operação e manutenção.", "Fabricante oficial", "Fonte técnica"),
        ],
        "checklist": ["Intimação/ciência das partes conferida", "Local, data e responsáveis confirmados", "EPI e condições de segurança avaliados", "Objeto e número de série identificados", "Manual e histórico solicitados", "Quesitos convertidos em pontos de inspeção", "Plano de fotos definido", "Medições e instrumentos planejados", "Ata de presentes preparada", "Limitações de acesso registradas"],
        "matrix_headers": ["etapa", "ponto_de_verificacao", "risco", "evidencia_esperada", "fonte", "responsavel", "status"],
        "matrix_rows": [
            ["pré-campo", "ciência das partes", "nulidade/contraditório", "comprovante de intimação", "CPC art. 474", "perito", "pendente"],
            ["campo", "proteções e energia", "acidente durante vistoria", "fotos e ata", "NR-12/MTE", "perito/local", "pendente"],
            ["campo", "identificação da máquina", "manual incompatível", "placa/modelo/série", "fabricante oficial", "perito", "pendente"],
        ],
        "template_name": "ROTEIRO_DILIGENCIA_MECANICA.md",
        "template": "# Roteiro de Diligência Mecânica\n\n## Dados\n- Processo:\n- Local:\n- Data:\n- Máquina/componente:\n\n## Objetivos Técnicos\n\n## Segurança\n\n## Pontos de Inspeção\n\n## Fotos Obrigatórias\n\n## Documentos a Solicitar\n\n## Ata de Presentes e Ocorrências\n\n## Limitações\n",
        "example_input": "Vistoria em prensa hidráulica após acidente, com discussão sobre NR-12, manutenção e possível falha de comando.",
        "example_output": "Roteiro inclui ciência das partes, bloqueio/energia, identificação da prensa, proteções, comandos, histórico de manutenção, manual, fotos sequenciais e limitações caso a máquina esteja alterada.",
        "limitations": ["Não autoriza operação insegura de máquina.", "Não substitui profissional de segurança do trabalho quando necessário.", "Não conclui conformidade NR-12 sem análise completa.", "Não ignora alteração posterior ao fato."],
        "review": ["A diligência respeita ciência das partes?", "Riscos de segurança foram tratados?", "Há plano de fotos e medições?", "Manual específico foi solicitado?"],
    },
    {
        "id": "pericia-06-inventario-evidencias",
        "title": "Inventário de Evidências",
        "description": "Criar inventário rastreável de evidências físicas, documentais, digitais, fotográficas e metrológicas usadas na perícia.",
        "use_when": "Use quando houver fotos, vídeos, peças, documentos, certificados, medições, logs, e-mails, manuais ou anexos que precisam ser controlados.",
        "inputs": ["arquivos", "fotos", "documentos", "peças", "medições", "origem", "data", "autor", "quesitos vinculados"],
        "outputs": ["inventário de evidências", "manifesto de arquivos", "hashes quando cabíveis", "vínculo evidência-quesito-laudo", "alertas de integridade"],
        "rules": [
            rule("O laudo pode ser instruído por fotografias, desenhos e elementos materiais necessários.", "CPC art. 473 §3º", "Fonte oficial"),
            rule("Origem, data, autoria, integridade e cópia de trabalho devem ser registradas quando evidência digital for relevante.", "ABNT NBR ISO/IEC 27037 [norma paga - não reproduzir integralmente]", "Fonte técnica"),
            rule("A lógica de cadeia de custódia pode ser usada por analogia metodológica, sem converter regra penal em obrigação cível automática.", "CPP arts. 158-A e seguintes [uso analógico]", "Fonte oficial por analogia"),
            rule("Certificados e medições devem ser vinculados a instrumento, unidade, rastreabilidade e condição de medição.", "INMETRO/Cgcre; GUM/VIM", "Fonte técnica oficial"),
        ],
        "checklist": ["ID único atribuído", "Origem registrada", "Data/hora registrada", "Arquivo original preservado", "Cópia de trabalho separada", "Hash calculado quando útil", "Quesito vinculado", "Seção do laudo vinculada", "Limitação registrada", "Evidência descartada ou fraca justificada"],
        "matrix_headers": ["id_evidencia", "tipo", "descricao", "origem", "data_hora", "arquivo_original", "hash_sha256", "quesito", "uso_no_laudo", "limitacao"],
        "matrix_rows": [
            ["EVD-001", "foto", "vista geral da máquina", "diligência", "preencher", "IMG_0001.jpg", "calcular se cabível", "Q-01", "contexto", ""],
            ["EVD-002", "documento", "certificado de calibração", "autos", "preencher", "certificado.pdf", "calcular se cabível", "Q-02", "metrologia", "validade/escopo a verificar"],
            ["EVD-003", "peça", "rolamento danificado", "local", "preencher", "registro físico", "não aplicável", "Q-03", "análise de falha", "custódia limitada se peça ficar com parte"],
        ],
        "template_name": "INVENTARIO_EVIDENCIAS.md",
        "template": "# Inventário de Evidências\n\n| ID | Tipo | Descrição | Origem | Data/Hora | Arquivo/Peça | Hash | Quesito | Uso | Limitação |\n|---|---|---|---|---|---|---|---|---|---|\n\n## Observações de Integridade\n\n## Evidências Pendentes\n",
        "example_input": "Pasta com 60 fotos, dois vídeos, contrato de manutenção, certificado de instrumento e peça fraturada vista em campo.",
        "example_output": "Inventário cria IDs, separa originais e cópias, marca certificado para validação INMETRO/Cgcre, vincula peça aos quesitos de falha e registra limitação de custódia.",
        "limitations": ["Não garante cadeia de custódia anterior ao recebimento.", "Não altera arquivos originais.", "Não autentica digitalmente documento sem procedimento específico.", "Não usa hash como prova de autoria."],
        "review": ["Cada evidência tem ID único?", "Original foi preservado?", "Há vínculo com quesito e laudo?", "Limitações de origem e integridade estão claras?"],
    },
    {
        "id": "pericia-07-anexo-fotografico",
        "title": "Gerador de Anexo Fotográfico",
        "description": "Gerar anexo fotográfico técnico com sequência, legenda, contexto, finalidade, vínculo com quesitos e ressalvas de qualidade/integridade.",
        "use_when": "Use quando houver fotos de diligência, documentos fotográficos dos autos ou imagens técnicas que precisam compor anexo do laudo.",
        "inputs": ["fotos", "metadados", "inventário de evidências", "quesitos", "local/data", "descrição técnica", "limitações"],
        "outputs": ["anexo fotográfico", "tabela de fotos", "legendas técnicas", "alertas de fotos fracas", "vínculo foto-quesito"],
        "rules": [
            rule("Fotografias podem instruir o laudo como elementos materiais, desde que contextualizadas.", "CPC art. 473 §3º", "Fonte oficial"),
            rule("Cada foto deve ter número, legenda, contexto, pertinência e vínculo técnico.", "IBAPE/SP - cartilhas e boas práticas periciais", "Fonte consultiva"),
            rule("Originais devem ser preservados e derivados identificados quando integridade digital importar.", "ABNT NBR ISO/IEC 27037 [norma paga - não reproduzir integralmente]", "Fonte técnica"),
            rule("Foto sem escala, baixa nitidez, corte relevante ou origem incerta deve receber ressalva.", "Base técnica interna derivada de boas práticas de evidência", "Fonte técnica interna"),
        ],
        "checklist": ["Fotos numeradas", "Arquivo original identificado", "Legenda técnica escrita", "Data/local indicados", "Autoria/origem indicada", "Escala usada quando necessária", "Nitidez e enquadramento avaliados", "Quesito vinculado", "Limitações indicadas", "Sequência lógica revisada"],
        "matrix_headers": ["foto_id", "arquivo", "descricao_tecnica", "local", "data", "quesito", "qualidade", "limitacao", "uso_no_laudo"],
        "matrix_rows": [
            ["F-001", "IMG_0001.jpg", "vista geral do equipamento", "preencher", "preencher", "Q-01", "boa", "", "contexto"],
            ["F-002", "IMG_0002.jpg", "detalhe do dano", "preencher", "preencher", "Q-03", "avaliar", "sem escala, se aplicável", "análise"],
            ["F-003", "IMG_0003.jpg", "placa de identificação", "preencher", "preencher", "Q-01", "boa", "", "identificação"],
        ],
        "template_name": "ANEXO_FOTOGRAFICO.md",
        "template": "# Anexo Fotográfico\n\n## Dados\n- Processo:\n- Local:\n- Data:\n- Autor das imagens:\n\n## Fotos\n\n### Foto F-001\n- Arquivo original:\n- Legenda técnica:\n- Quesito relacionado:\n- Observações/limitações:\n\n## Controle de Integridade\n",
        "example_input": "Fotos de motor elétrico queimado, placa de identificação, acoplamento desalinhado e painel de comando.",
        "example_output": "Anexo organiza fotos gerais antes dos detalhes, legenda cada imagem com finalidade técnica e marca foto do acoplamento sem escala como válida com ressalva.",
        "limitations": ["Não melhora imagem a ponto de criar informação inexistente.", "Não remove metadados dos originais.", "Não usa foto sem origem como prova conclusiva sem ressalva.", "Não substitui inventário de evidências."],
        "review": ["A sequência conta a história técnica?", "Cada foto tem legenda e vínculo?", "Imagens fracas foram ressalvadas?", "Originais e derivados estão separados?"],
    },
    {
        "id": "pericia-08-laudo-mecanico",
        "title": "Gerador de Laudo Pericial Mecânico",
        "description": "Gerar estrutura e minuta de laudo pericial judicial de engenharia mecânica com método, análise, evidências, respostas a quesitos, conclusão e limitações.",
        "use_when": "Use para montar laudo a partir de autos, diligência, matriz documental, matriz de quesitos, inventário de evidências, medições e análise técnica.",
        "inputs": ["dados do processo", "objeto", "matriz documental", "matriz de quesitos", "inventário de evidências", "roteiro/ata de diligência", "método técnico", "anexo fotográfico"],
        "outputs": ["laudo pericial mecânico", "respostas a quesitos", "quadro de evidências", "limitações", "anexos sugeridos", "alertas anti-impugnação"],
        "rules": [
            rule("O laudo deve conter objeto, análise técnica/científica, método utilizado e resposta conclusiva a todos os quesitos.", "CPC art. 473", "Fonte oficial"),
            rule("Conclusões devem ser vinculadas a evidência, documento, medição, norma, manual ou limitação.", "CPC art. 473; boas práticas IBAPE", "Fonte oficial e consultiva"),
            rule("O laudo deve indicar habilitação profissional, registro, ART quando cabível e limites de atribuição.", "Lei 5.194/1966; Lei 6.496/1977; Confea/Crea", "Fonte oficial"),
            rule("Normas ABNT e literatura técnica podem fundamentar método, mas não devem ser copiadas integralmente.", "ABNT Catálogo; literatura técnica com licença", "Fonte técnica"),
            rule("Em segurança de máquinas, verificar NR-12 vigente e data do fato antes de concluir conformidade.", "NR-12/MTE", "Fonte oficial"),
        ],
        "checklist": ["Identificação completa", "Objeto delimitado", "Histórico processual suficiente", "Documentos analisados", "Método declarado", "Diligência descrita", "Evidências vinculadas", "Análise técnica separada de opinião jurídica", "Todos os quesitos respondidos", "Limitações e anexos incluídos"],
        "matrix_headers": ["secao_laudo", "conteudo_esperado", "fonte", "evidencia_vinculada", "status", "risco_se_ausente"],
        "matrix_rows": [
            ["Objeto", "objeto da perícia delimitado", "CPC art. 473", "decisão/quesitos", "pendente", "laudo inepto ou amplo demais"],
            ["Método", "procedimento técnico usado", "CPC art. 473; ABNT/IBAPE se aplicável", "matriz/roteiro", "pendente", "impugnação por falta de método"],
            ["Quesitos", "respostas conclusivas", "CPC arts. 473 e 477", "matriz de quesitos", "pendente", "esclarecimentos por omissão"],
        ],
        "template_name": "LAUDO_PERICIAL_MECANICO.md",
        "template": "# Laudo Pericial de Engenharia Mecânica\n\n## 1. Identificação\n\n## 2. Objeto da Perícia\n\n## 3. Síntese dos Autos\n\n## 4. Documentos e Evidências Analisados\n\n## 5. Metodologia\n\n## 6. Diligências Realizadas\n\n## 7. Análise Técnica\n\n## 8. Respostas aos Quesitos\n\n## 9. Conclusão Técnica\n\n## 10. Limitações\n\n## 11. Anexos\n\n## 12. Fontes Consultadas e Verificações Pendentes\n",
        "example_input": "Matriz documental, inventário de fotos, ata de vistoria e quesitos sobre falha em redutor industrial.",
        "example_output": "Minuta de laudo com objeto delimitado, método de análise de falhas, descrição da vistoria, evidências, respostas a todos os quesitos e conclusão com limitações de acesso ao histórico de manutenção.",
        "limitations": ["Não protocola laudo automaticamente.", "Não conclui além das evidências disponíveis.", "Não cita norma técnica sem marcar edição e verificação.", "Não assume responsabilidade jurídica, culpa ou dolo."],
        "review": ["Os quatro elementos do CPC art. 473 estão presentes?", "Todos os quesitos têm resposta?", "Cada conclusão tem fonte/evidência?", "As limitações são explícitas?"],
    },
    {
        "id": "pericia-09-revisao-impugnacao",
        "title": "Revisor de Laudo e Impugnação",
        "description": "Revisar laudo, parecer técnico, impugnação ou pedido de esclarecimentos, apontando omissões, riscos, inconsistências, falta de método e resposta a quesitos.",
        "use_when": "Use antes de protocolar laudo, ao responder impugnação, ao analisar parecer de assistente ou ao preparar esclarecimentos.",
        "inputs": ["laudo", "matriz de quesitos", "impugnação", "parecer de assistente", "evidências", "fontes citadas", "limitações"],
        "outputs": ["relatório de revisão", "matriz de achados", "riscos de impugnação", "sugestões de esclarecimento", "pontos a corrigir"],
        "rules": [
            rule("O laudo deve ser revisado contra os requisitos mínimos de objeto, método, análise e respostas a quesitos.", "CPC art. 473", "Fonte oficial"),
            rule("Pedidos de esclarecimento e omissões devem ser tratados com rastreio por quesito e evidência.", "CPC art. 477", "Fonte oficial"),
            rule("Segunda perícia só deve ser tratada como hipótese quando a matéria não estiver esclarecida; a skill não decide deferimento.", "CPC art. 480", "Fonte oficial"),
            rule("Regularidade profissional, ART e atribuição podem ser pontos de vulnerabilidade formal.", "Lei 5.194/1966; Lei 6.496/1977; Confea/Crea", "Fonte oficial"),
            rule("Normas técnicas e cartilhas devem ser classificadas corretamente para evitar uso como obrigação indevida.", "ABNT; IBAPE", "Fonte técnica/consultiva"),
        ],
        "checklist": ["CPC art. 473 conferido", "Quesitos confrontados", "Evidências vinculadas", "Método descrito", "Conclusões não jurídicas", "Normas com edição/status", "ART/CREA conferidos", "Limitações presentes", "Impugnação classificada por tema", "Resposta proposta sem tom de parte"],
        "matrix_headers": ["achado_id", "tipo", "trecho", "risco", "fonte", "correcao_sugerida", "prioridade"],
        "matrix_rows": [
            ["ACH-001", "omissão", "quesito sem resposta", "pedido de esclarecimento", "CPC arts. 473/477", "responder ou justificar impossibilidade", "alta"],
            ["ACH-002", "método", "análise sem método declarado", "impugnação técnica", "CPC art. 473", "descrever método e evidências", "alta"],
            ["ACH-003", "fonte", "norma sem edição", "citação frágil", "ABNT Catálogo", "marcar edição/status/verificação", "média"],
        ],
        "template_name": "RELATORIO_REVISAO_IMPUGNACAO.md",
        "template": "# Relatório de Revisão de Laudo/Impugnação\n\n## Documento Revisado\n\n## Achados Críticos\n\n## Quesitos e Omissões\n\n## Método e Evidências\n\n## Fontes e Verificações\n\n## Sugestão de Resposta Técnica\n\n## Limitações da Revisão\n",
        "example_input": "Impugnação afirma que o laudo não respondeu quesito sobre manutenção preventiva e usou NR-12 sem indicar texto vigente.",
        "example_output": "Revisão marca omissão parcial, recomenda resposta específica ao quesito e atualização da referência NR-12 com data de consulta, sem assumir conclusão jurídica.",
        "limitations": ["Não substitui decisão judicial sobre impugnação.", "Não cria evidência ausente.", "Não usa tom de defesa de parte.", "Não valida fonte temporal sem consulta atual."],
        "review": ["Achados estão priorizados?", "Cada achado cita fonte?", "Correção proposta é técnica?", "Há separação entre crítica formal e técnica?"],
    },
    {
        "id": "pericia-10-peticoes",
        "title": "Petições do Perito",
        "description": "Gerar minutas de petições do perito judicial: aceite, escusa, honorários, diligência, pedido de documentos, prorrogação, juntada de laudo e esclarecimentos.",
        "use_when": "Use quando o perito precisa peticionar no processo de forma impessoal, técnica e limitada ao encargo pericial.",
        "inputs": ["tipo de petição", "processo", "decisão", "prazo", "pedido", "fundamento", "anexos", "fontes aplicáveis"],
        "outputs": ["minuta de petição", "checklist de protocolo", "lista de anexos", "alertas de fundamento e prazo"],
        "rules": [
            rule("Petições do perito devem ser limitadas ao encargo, pedido processual claro e fundamento mínimo.", "CPC arts. 156-158, 465, 466, 477 e correlatos", "Fonte oficial"),
            rule("Honorários devem citar regime do CPC e, quando aplicável, CNJ/tribunal local.", "CPC art. 95; Resolução CNJ 232/2016; atos locais", "Fonte oficial"),
            rule("Diligência deve observar ciência das partes quando aplicável.", "CPC art. 474", "Fonte oficial"),
            rule("ART e regularidade profissional podem ser informadas quando relevantes ao encargo.", "Lei 6.496/1977; Confea/Crea", "Fonte oficial"),
            rule("A linguagem deve ser neutra, impessoal e técnica; não deve defender parte.", "CPC; Manual de Redação oficial como apoio", "Fonte oficial/consultiva"),
        ],
        "checklist": ["Tipo de petição definido", "Processo e juízo conferidos", "Pedido claro", "Fundamento mínimo citado", "Prazo verificado", "Anexos listados", "Tom impessoal", "Sem conclusão jurídica indevida", "Fontes temporais marcadas", "Texto revisado antes de protocolo"],
        "matrix_headers": ["tipo_peticao", "gatilho", "fonte", "pedido_principal", "anexos", "risco"],
        "matrix_rows": [
            ["aceite", "nomeação", "CPC arts. 156-158", "aceitar encargo/registrar dados", "currículo/ART se cabível", "impedimento não verificado"],
            ["honorários", "intimação para proposta", "CPC art. 95; CNJ/TJCE se aplicável", "arbitramento/depósito", "memória de cálculo", "tabela desatualizada"],
            ["diligência", "necessidade de vistoria", "CPC art. 474", "designação/intimação", "roteiro/endereços", "ciência das partes ausente"],
        ],
        "template_name": "PETICAO_PERITO_MODELO.md",
        "template": "# Minuta de Petição do Perito\n\nExcelentíssimo(a) Senhor(a) Doutor(a) Juiz(a) de Direito da ___ Vara ___\n\nProcesso nº: \n\n[Nome], perito nomeado, vem, respeitosamente, à presença de Vossa Excelência, informar/requerer:\n\n## Síntese\n\n## Fundamento\n\n## Pedido\n\n## Anexos\n\nTermos em que,\nPede deferimento.\n\n[local], [data]\n\n[assinatura]\n",
        "example_input": "Perito precisa pedir prazo adicional porque a parte ainda não apresentou manual e histórico de manutenção.",
        "example_output": "Minuta pede prorrogação fundamentada na necessidade técnica de documentos, lista os documentos pendentes e mantém linguagem neutra.",
        "limitations": ["Não peticiona como advogado da parte.", "Não promete decisão judicial.", "Não cita fundamento sem conferir texto vigente.", "Não protocola automaticamente."],
        "review": ["Pedido está claro?", "Fundamento mínimo foi citado?", "Tom é de perito?", "Anexos e prazos foram conferidos?"],
    },
    {
        "id": "pericia-11-controle-prazos",
        "title": "Controle de Prazos da Perícia",
        "description": "Controlar prazos, marcos processuais, ciência, quesitos, assistentes, diligência, entrega do laudo, esclarecimentos, cadastro e documentos vencíveis.",
        "use_when": "Use para transformar intimações, decisões e eventos do PJe/SIPER em uma agenda de acompanhamento da perícia.",
        "inputs": ["intimações", "decisão de nomeação", "prazos indicados", "data de ciência", "eventos PJe/SIPER", "datas de diligência", "pedidos de esclarecimento"],
        "outputs": ["controle de prazos", "alertas", "eventos críticos", "pendências", "recomendações de petição"],
        "rules": [
            rule("Prazos devem partir da data de ciência e do teor da decisão/intimação; a skill deve marcar cálculo como conferência obrigatória.", "CPC e decisão judicial concreta", "Fonte oficial"),
            rule("Quesitos, assistentes, laudo e esclarecimentos devem ser controlados por evento processual.", "CPC arts. 465 e 477", "Fonte oficial"),
            rule("Fluxos locais de cadastro, SIPER, PJe e pagamento devem ser conferidos quando aplicáveis ao TJCE.", "TJCE; CNJ Res. 233/2016", "Fonte oficial local"),
            rule("Certidões, cadastro, ART e documentos profissionais possuem validade operacional e devem entrar no controle.", "Confea/Crea; TJCE", "Fonte oficial/operacional"),
        ],
        "checklist": ["Data de ciência registrada", "Teor da intimação conferido", "Prazo e unidade marcados", "Feriados/forma de contagem sinalizados para conferência", "Evento PJe/SIPER vinculado", "Responsável definido", "Alertas intermediários criados", "Petições pendentes listadas", "Status atualizado", "Fontes temporais verificadas"],
        "matrix_headers": ["evento", "data_ciencia", "prazo", "unidade", "vencimento", "fonte", "status", "alerta", "acao"],
        "matrix_rows": [
            ["nomeação", "preencher", "conforme decisão", "dias", "calcular e verificar", "CPC/decisão", "pendente", "D-5", "triagem/aceite"],
            ["quesitos/assistentes", "preencher", "conforme CPC/decisão", "dias", "calcular e verificar", "CPC art. 465", "pendente", "D-3", "registrar matriz"],
            ["esclarecimentos", "preencher", "conforme decisão", "dias", "calcular e verificar", "CPC art. 477", "pendente", "D-3", "preparar resposta"],
        ],
        "template_name": "CONTROLE_PRAZOS_PERICIA.md",
        "template": "# Controle de Prazos da Perícia\n\n| Evento | Data de ciência | Prazo | Vencimento conferido | Fonte | Status | Ação |\n|---|---|---|---|---|---|---|\n\n## Alertas\n\n## Pendências Operacionais\n",
        "example_input": "Intimação em 17/05/2026 para entregar laudo em 30 dias e ciência para quesitos das partes.",
        "example_output": "Controle registra data de ciência, prazo informado, alerta para conferir forma de contagem no PJe e cria marcos para quesitos, diligência, laudo e eventual pedido de prorrogação.",
        "limitations": ["Não substitui conferência no PJe/SIPER.", "Não calcula prazo final como certeza jurídica sem conferir calendário e decisão.", "Não envia lembrete externo por si só.", "Não presume feriado local."],
        "review": ["Data de ciência está correta?", "A fonte do prazo foi registrada?", "Há alerta antes do vencimento?", "Eventos locais foram conferidos no sistema?"],
    },
    {
        "id": "pericia-12-biblioteca-normas",
        "title": "Biblioteca de Normas e Métodos",
        "description": "Manter catálogo atualizável de fontes oficiais, técnicas e consultivas para perícia judicial de engenharia mecânica.",
        "use_when": "Use para pesquisar, registrar, atualizar, classificar e auditar fontes que alimentam as demais skills.",
        "inputs": ["fonte nova", "URL oficial", "norma ou publicação", "skill afetada", "tipo de fonte", "data de consulta", "necessidade de atualização"],
        "outputs": ["ficha de fonte", "registro de atualização", "matriz de impacto", "alertas de licença", "lista de skills afetadas"],
        "rules": [
            rule("Fonte primária deve prevalecer sobre comentário, resumo, blog ou material secundário.", "Política de fontes do projeto; fontes oficiais Planalto/CNJ/TJCE/Confea/MTE/INMETRO", "Fonte oficial"),
            rule("Normas ABNT e livros comerciais devem ser cadastrados por metadados, escopo, notas próprias e forma legal de aquisição, sem cópia integral.", "ABNT Catálogo; editoras técnicas", "Fonte técnica paga"),
            rule("Fonte consultiva deve ser marcada como boa prática ou apoio, sem virar obrigação legal.", "IBAPE; literatura técnica; fabricantes", "Fonte consultiva/técnica"),
            rule("Fontes temporais devem ter frequência de verificação, impacto, procedimento de atualização e skills afetadas.", "FONTES_OFICIAIS_ATUALIZAVEIS.md", "Base interna rastreável"),
        ],
        "checklist": ["Fonte primária localizada", "Tipo classificado", "Instituição registrada", "URL oficial registrada", "Data de consulta registrada", "Status/edição conferidos", "Copyright/licença avaliado", "Skills afetadas listadas", "Impacto descrito", "Próxima verificação definida"],
        "matrix_headers": ["id_fonte", "categoria", "fonte", "tipo", "instituicao", "url", "status", "frequencia", "skill_afetada", "procedimento"],
        "matrix_rows": [
            ["FON-001", "processo", "CPC", "fonte oficial", "Planalto", "https://www.planalto.gov.br/", "verificar", "semestral", "01;04;08;09;10;11", "conferir texto compilado"],
            ["FON-002", "norma técnica", "ABNT", "fonte técnica paga", "ABNT", "https://www.abntcatalogo.com.br/", "verificar", "trimestral", "05;06;07;08;09;12", "registrar edição/status sem copiar íntegra"],
            ["FON-003", "segurança", "NR-12", "fonte oficial", "MTE", "https://www.gov.br/trabalho-e-emprego/", "verificar", "mensal/caso", "05;08;09;12", "baixar texto vigente e registrar portaria"],
        ],
        "template_name": "FICHA_FONTE_METODO.md",
        "template": "# Ficha de Fonte ou Método\n\n## Identificação\n- ID:\n- Fonte:\n- Instituição:\n- URL oficial:\n- Tipo: oficial / técnica / consultiva / interna\n- Data de consulta:\n\n## Escopo de Aplicação\n\n## Regra ou Conhecimento Extraído\n\n## Skills Afetadas\n\n## Licença e Restrições\n\n## Atualização Necessária\n\n## Procedimento de Atualização\n",
        "example_input": "Nova edição de manual do fabricante e confirmação de status de uma NBR usada em laudo.",
        "example_output": "Biblioteca cria ficha do manual por modelo/série, registra status da NBR no ABNT Catálogo, marca restrição de copyright e aponta skills 05, 08 e 09 como afetadas.",
        "limitations": ["Não baixa norma paga sem licença.", "Não confirma vigência sem acessar fonte oficial.", "Não mistura fonte técnica com obrigação legal.", "Não mantém fonte temporal sem data de consulta."],
        "review": ["Tipo da fonte está correto?", "URL oficial foi registrada?", "Há data de consulta e próxima verificação?", "Licença e impacto foram descritos?"],
    },
]


def write_text(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_csv(path, headers, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def bullets(items):
    return "\n".join(f"- {item}" for item in items)


def numbered(items):
    return "\n".join(f"{i}. {item}" for i, item in enumerate(items, 1))


def rule_table(rules):
    lines = ["| Regra operacional | Fonte | Tipo | Verificação |", "|---|---|---|---|"]
    for item in rules:
        lines.append(f"| {item['regra']} | {item['fonte']} | {item['tipo']} | {item['verificacao']} |")
    return "\n".join(lines)


def source_sections(spec):
    official = []
    technical = []
    consultative = []
    for item in spec["rules"]:
        entry = f"- {item['fonte']}: {item['regra']} {item['verificacao']}"
        kind = item["tipo"].lower()
        added = False
        if "oficial" in kind:
            official.append(entry)
            added = True
        if "técnica" in kind or "técnico" in kind or "internal" in kind or "interna" in kind:
            technical.append(entry)
            added = True
        if "consultiva" in kind or "consultivo" in kind:
            consultative.append(entry)
            added = True
        if not added:
            consultative.append(entry)
    return (
        "## Fontes Oficiais\n\n"
        + ("\n".join(official) if official else "- Nenhuma fonte oficial específica além da matriz global.")
        + "\n\n## Fontes Técnicas\n\n"
        + ("\n".join(technical) if technical else "- Nenhuma fonte técnica específica além da matriz global.")
        + "\n\n## Fontes Consultivas\n\n"
        + ("\n".join(consultative) if consultative else "- Nenhuma fonte consultiva específica além da matriz global.")
    )


def skill_md(spec):
    return f"""---
name: {spec['id']}
description: {spec['description']}
---

# {spec['title']}

## Quando Usar

{spec['use_when']}

## Entradas Esperadas

{bullets(spec['inputs'])}

## Fluxo Operacional

{numbered([
    'Ler a demanda e identificar processo, objeto, partes, tribunal, datas e documentos disponíveis.',
    'Separar fontes oficiais, fontes técnicas, fontes consultivas e bases internas.',
    'Aplicar as regras abaixo, citando fonte e marcando itens que exigem verificação antes de uso real.',
    'Gerar a saída no template da skill, registrando evidências, limitações e pendências.',
    'Executar o checklist e os critérios de revisão antes de entregar qualquer texto para uso externo.',
])}

## Regras Operacionais Com Fonte

{rule_table(spec['rules'])}

## Saídas Esperadas

{bullets(spec['outputs'])}

## Regras de Segurança Técnica

{bullets(COMMON_WARNINGS)}

## Arquivos de Apoio

- `references/REFERENCIAS.md`
- `templates/{spec['template_name']}`
- `checklists/CHECKLIST.md`
- `matrices/{spec['id']}.csv`
- `examples/entrada.md`
- `examples/saida.md`
- `SEGURANCA_TECNICA.md`
- `LIMITACOES.md`
- `CRITERIOS_REVISAO.md`
"""


def references_md(spec):
    return f"""# Referências - {spec['title']}

Atualizado em: {TODAY}

Este arquivo organiza as fontes que alimentam a skill `{spec['id']}`. Use a fonte primária sempre que disponível e marque qualquer item temporal como `[VERIFICAR ANTES DE USO REAL]`.

{source_sections(spec)}

## Regras Extraídas

{rule_table(spec['rules'])}

## Fontes Globais do Projeto

| Fonte | Uso | Verificação |
|---|---|---|
| CPC | Base processual de perícia, prazos, quesitos, laudo e deveres | [VERIFICAR ANTES DE USO REAL] |
| CNJ | Cadastro, honorários em gratuidade, governança de peritos | [VERIFICAR ANTES DE USO REAL] |
| TJCE | Fluxo local, SIPER/PJe, portarias, tabelas e credenciamento | [VERIFICAR ANTES DE USO REAL] |
| CONFEA/CREA | Atribuições, ART, TOS, acervo e regularidade profissional | [VERIFICAR ANTES DE USO REAL] |
| ABNT | Normas técnicas, apenas por ficha, escopo e metadados quando pagas | [VERIFICAR EDIÇÃO/STATUS] |
| IBAPE | Boa prática, cartilhas, glossários e orientação institucional | [VERIFICAR EDIÇÃO/STATUS] |
| MTE/NR-12 | Segurança de máquinas e normas regulamentadoras | [VERIFICAR TEXTO VIGENTE] |
| INMETRO/Cgcre | Metrologia, acreditação, rastreabilidade e incerteza | [VERIFICAR DOCUMENTO/ESCOPO] |
| Fabricantes | Manual, catálogo e boletim por modelo/série | [VERIFICAR POR CASO] |
| Literatura técnica | Análise de falhas, manutenção, RCFA e projeto mecânico | [VERIFICAR EDIÇÃO/LICENÇA] |

## Restrições de Licença

- Não copiar integralmente normas ABNT, ISO, handbooks ou livros comerciais.
- Usar metadados, ficha bibliográfica, escopo, notas próprias e referência à aquisição legal.
- Citar apenas o necessário e sempre separar inferência técnica de obrigação normativa.
"""


def safety_md(spec):
    specific = [item["regra"] + f" Fonte: {item['fonte']}." for item in spec["rules"]]
    return f"""# Segurança Técnica - {spec['title']}

## Regras Gerais

{bullets(COMMON_WARNINGS)}

## Regras Específicas da Skill

{bullets(specific)}

## Bloqueios

- Bloquear saída quando a fonte obrigatória estiver ausente e a resposta puder ser usada em processo real.
- Bloquear conclusão causal quando faltarem evidência, método ou limitação.
- Bloquear citação de norma paga sem edição/status e aviso de não reprodução integral.
- Bloquear linguagem de culpa, dolo, ilegalidade ou responsabilidade quando a conclusão for apenas técnica.
"""


def limitations_md(spec):
    return f"""# Limitações - {spec['title']}

{bullets(spec['limitations'])}

## Regra de Uso em Processo Real

Toda saída desta skill é apoio técnico-operacional. Antes de uso em processo real, conferir autos, decisão, fonte oficial vigente, normas aplicáveis, tribunal competente, atribuição profissional e documentos originais.
"""


def review_md(spec):
    return f"""# Critérios de Revisão - {spec['title']}

## Revisão Obrigatória

{bullets(spec['review'])}

## Critérios Transversais

- Fonte de cada regra citada.
- Fonte oficial separada de fonte técnica e consultiva.
- Informação temporal marcada para verificação.
- Norma paga sem reprodução integral.
- Conclusão técnica apoiada em evidência, método ou limitação.
- Texto sem atuação como advogado da parte.
"""


def checklist_md(spec):
    return f"""# Checklist - {spec['title']}

Use antes de entregar saída da skill `{spec['id']}`.

{bullets('[ ] ' + item for item in spec['checklist'])}

## Fechamento

- [ ] Fontes temporais marcadas como `[VERIFICAR ANTES DE USO REAL]`.
- [ ] Normas pagas não reproduzidas integralmente.
- [ ] Saída revisada contra `CRITERIOS_REVISAO.md`.
- [ ] Limitações registradas.
"""


def examples(spec):
    entrada = f"""# Exemplo de Entrada - {spec['title']}

{spec['example_input']}

## Dados mínimos esperados

{bullets(spec['inputs'][:5])}
"""
    saida = f"""# Exemplo de Saída - {spec['title']}

{spec['example_output']}

## Observação

Exemplo didático. Confirmar fontes oficiais, documentos do processo e normas vigentes antes de uso real.
"""
    return entrada, saida


def render_tree():
    lines = [
        "pericia-mecanica-os/",
        "├── PACOTE_CONHECIMENTO_CODEX.md",
        "├── FONTES_OFICIAIS_ATUALIZAVEIS.md",
        "├── CHECKLIST_ATUALIZACAO_REFERENCIAS.md",
        "├── MATRIZ_MESTRA_CONHECIMENTO.md",
        "├── references/",
        "└── skills/",
    ]
    for idx, spec in enumerate(SKILLS):
        prefix = "    └──" if idx == len(SKILLS) - 1 else "    ├──"
        lines.extend([
            f"{prefix} {spec['id']}/",
            "        ├── SKILL.md",
            "        ├── references/REFERENCIAS.md",
            f"        ├── templates/{spec['template_name']}",
            "        ├── checklists/CHECKLIST.md",
            f"        ├── matrices/{spec['id']}.csv",
            "        ├── examples/entrada.md",
            "        ├── examples/saida.md",
            "        ├── SEGURANCA_TECNICA.md",
            "        ├── LIMITACOES.md",
            "        └── CRITERIOS_REVISAO.md",
        ])
    return "\n".join(lines)


def generate_skill(spec):
    base = ROOT / "skills" / spec["id"]
    files = {
        base / "SKILL.md": skill_md(spec),
        base / "references" / "REFERENCIAS.md": references_md(spec),
        base / "templates" / spec["template_name"]: spec["template"],
        base / "checklists" / "CHECKLIST.md": checklist_md(spec),
        base / "SEGURANCA_TECNICA.md": safety_md(spec),
        base / "LIMITACOES.md": limitations_md(spec),
        base / "CRITERIOS_REVISAO.md": review_md(spec),
    }
    entrada, saida = examples(spec)
    files[base / "examples" / "entrada.md"] = entrada
    files[base / "examples" / "saida.md"] = saida
    for path, content in files.items():
        write_text(path, content)
    write_csv(base / "matrices" / f"{spec['id']}.csv", spec["matrix_headers"], spec["matrix_rows"])


def build_export():
    sections = [
        "# Pacote de Conhecimento Codex - pericia-mecanica-os",
        "",
        f"Gerado em: {TODAY}",
        "",
        "## Árvore de Diretórios",
        "",
        "```text",
        render_tree(),
        "```",
        "",
        "## Conteúdo de Cada SKILL.md",
        "",
    ]
    for spec in SKILLS:
        base = ROOT / "skills" / spec["id"]
        sections.extend([f"### {spec['id']} - SKILL.md", "", "```markdown", (base / "SKILL.md").read_text(encoding="utf-8").rstrip(), "```", ""])
    sections.append("## Arquivos de Referência")
    sections.append("")
    for spec in SKILLS:
        base = ROOT / "skills" / spec["id"]
        sections.extend([f"### {spec['id']} - references/REFERENCIAS.md", "", "```markdown", (base / "references" / "REFERENCIAS.md").read_text(encoding="utf-8").rstrip(), "```", ""])
    sections.append("## Templates")
    sections.append("")
    for spec in SKILLS:
        base = ROOT / "skills" / spec["id"]
        sections.extend([f"### {spec['id']} - templates/{spec['template_name']}", "", "```markdown", (base / "templates" / spec["template_name"]).read_text(encoding="utf-8").rstrip(), "```", ""])
    sections.append("## Checklists")
    sections.append("")
    for spec in SKILLS:
        base = ROOT / "skills" / spec["id"]
        sections.extend([f"### {spec['id']} - checklists/CHECKLIST.md", "", "```markdown", (base / "checklists" / "CHECKLIST.md").read_text(encoding="utf-8").rstrip(), "```", ""])
    sections.append("## Matrizes CSV")
    sections.append("")
    for spec in SKILLS:
        base = ROOT / "skills" / spec["id"]
        sections.extend([f"### {spec['id']} - matrices/{spec['id']}.csv", "", "```csv", (base / "matrices" / f"{spec['id']}.csv").read_text(encoding="utf-8-sig").rstrip(), "```", ""])
    return "\n".join(sections)


def main():
    for spec in SKILLS:
        generate_skill(spec)
    write_text(ROOT / "PACOTE_CONHECIMENTO_CODEX.md", build_export())


if __name__ == "__main__":
    main()
