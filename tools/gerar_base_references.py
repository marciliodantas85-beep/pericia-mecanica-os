from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


SOURCE_CATALOG = {
    "cpc_pericia": {
        "name": "Código de Processo Civil, arts. 91, 93, 95, 98, 148, 149, 156-158 e 464-480",
        "nature": "Norma obrigatória - lei processual",
        "application": "Nomeação, impedimento, honorários, diligências, quesitos, conteúdo mínimo do laudo, esclarecimentos e segunda perícia.",
        "rule": "Separar objeto, método, análise técnica e respostas aos quesitos; controlar prazos e não extrapolar a designação judicial.",
        "periodic": True,
        "note": "Usar texto oficial vigente; checar alterações antes de protocolo."
    },
    "cpc_documentos": {
        "name": "Código de Processo Civil, arts. 319, 320, 336, 369 e 434",
        "nature": "Norma obrigatória - lei processual",
        "application": "Leitura de inicial, contestação, prova documental e alegações das partes.",
        "rule": "Classificar narrativa sem suporte como alegação e documento juntado como elemento sujeito a pertinência, integridade e contraditório.",
        "periodic": True,
        "note": "Não converter alegação em fato técnico constatado."
    },
    "cnj_233": {
        "name": "Resolução CNJ 233/2016 - CPTEC e cadastro de peritos",
        "nature": "Norma obrigatória - governança judicial",
        "application": "Cadastro, validação documental, reavaliação, deveres, impedimentos e restrições de atuação do perito.",
        "rule": "Antes do aceite, checar cadastro, conflitos, atuação prévia como assistente técnico e deveres de sigilo, diligência e pontualidade.",
        "periodic": True,
        "note": "Marcar como fonte sujeita a alterações do CNJ."
    },
    "cnj_232": {
        "name": "Resolução CNJ 232/2016 - honorários em justiça gratuita",
        "nature": "Norma obrigatória - governança judicial",
        "application": "Critérios nacionais de arbitramento de honorários quando houver beneficiário da justiça gratuita.",
        "rule": "Fundamentar honorários por complexidade, especialização, local, tempo, zelo e peculiaridades regionais.",
        "periodic": True,
        "note": "Usar com tabela local do tribunal, quando existente."
    },
    "cnj_127": {
        "name": "Resolução CNJ 127/2011 - banco de peritos",
        "nature": "Norma institucional - governança judicial",
        "application": "Especialidade, banco de peritos e organização do cadastro judicial.",
        "rule": "Usar como reforço institucional, sem substituir CPC e normas locais do tribunal.",
        "periodic": True,
        "note": "Fonte de apoio para triagem e biblioteca."
    },
    "tjce_07_2024": {
        "name": "Resolução do Órgão Especial TJCE 07/2024",
        "nature": "Norma obrigatória local - TJCE",
        "application": "Credenciamento, nomeação, pagamento, documentação e fluxo de peritos no TJCE.",
        "rule": "Quando a perícia tramitar no TJCE, checar credenciamento, regra de pagamento, hipóteses excepcionais e documentos exigidos.",
        "periodic": True,
        "note": "Fonte local prioritária; conferir atos posteriores."
    },
    "tjce_14_2022": {
        "name": "Resolução TJCE 14/2022 - SIPER",
        "nature": "Norma operacional local - TJCE",
        "application": "Uso do SIPER no credenciamento e gestão de peritos.",
        "rule": "Tratar cadastro e manutenção de dados no SIPER como requisito operacional, não como detalhe administrativo.",
        "periodic": True,
        "note": "Checar manuais e atualizações do sistema."
    },
    "tjce_portarias": {
        "name": "Portarias e tabelas de honorários do TJCE, incluindo Portaria 1218/2025 e 968/2026",
        "nature": "Norma obrigatória local - tabela e pagamento",
        "application": "Enquadramento de honorários, datas de vigência, rubricas e majoração local.",
        "rule": "Selecionar a tabela pela data de realização da perícia e conferir a portaria vigente no portal oficial antes do uso.",
        "periodic": True,
        "note": "Fonte altamente temporal; verificar periodicamente."
    },
    "tjce_manual_pje": {
        "name": "Manual do Perito no PJe do TJCE e páginas de documentação/certidões",
        "nature": "Manual operacional oficial",
        "application": "Acesso aos autos, perfis perito e jus postulandi, protocolo de laudos, manifestações e pagamentos.",
        "rule": "Após credenciamento, conferir perfis no PJe, acesso aos autos, documentação e canal correto de protocolo.",
        "periodic": True,
        "note": "Manual orienta fluxo, mas não substitui CPC nem ato normativo."
    },
    "stj_jurisprudencia": {
        "name": "Jurisprudência oficial do STJ sobre honorários, custeio, intimação e suspeição de perito",
        "nature": "Fonte consultiva forte - jurisprudência",
        "application": "Apoio em petições, impugnações e debates sobre custeio ou posição processual do perito.",
        "rule": "Usar como reforço argumentativo, nunca para substituir lei, resolução ou ato local vigente.",
        "periodic": True,
        "note": "Checar se há tese mais recente ou distinção do caso concreto."
    },
    "lei_5194": {
        "name": "Lei 5.194/1966 - exercício profissional da engenharia",
        "nature": "Norma obrigatória - lei profissional",
        "application": "Habilitação, registro, valor jurídico de laudos e identificação profissional.",
        "rule": "Exigir compatibilidade entre objeto pericial, título, registro e atribuição profissional.",
        "periodic": True,
        "note": "Usar para regularidade profissional, não para decidir mérito do litígio."
    },
    "lei_6496": {
        "name": "Lei 6.496/1977 - ART",
        "nature": "Norma obrigatória - lei profissional",
        "application": "Responsabilidade técnica e necessidade de ART em serviços de engenharia.",
        "rule": "Tratar a ART como item de regularidade técnica, com emissão, quitação e pertinência ao escopo.",
        "periodic": True,
        "note": "Verificar orientação do CREA competente para o caso."
    },
    "confea_218": {
        "name": "Resolução Confea 218/1973",
        "nature": "Norma profissional obrigatória",
        "application": "Atividades profissionais e campo de atuação do engenheiro mecânico.",
        "rule": "Confrontar o objeto com processos mecânicos, máquinas, instalações mecânicas, sistemas térmicos, refrigeração, HVAC e serviços correlatos.",
        "periodic": True,
        "note": "Usar com Resolução Confea 1.073/2016 e registro real do profissional."
    },
    "confea_345": {
        "name": "Resolução Confea 345/1990",
        "nature": "Norma profissional obrigatória",
        "application": "Definições de vistoria, perícia, avaliação, arbitramento e laudo.",
        "rule": "Não tratar vistoria, perícia causal, avaliação patrimonial e arbitramento como sinônimos.",
        "periodic": True,
        "note": "Fonte central para terminologia interna das skills."
    },
    "confea_1073": {
        "name": "Resolução Confea 1.073/2016",
        "nature": "Norma profissional obrigatória",
        "application": "Títulos, atividades, competências, campos de atuação e extensão de atribuições.",
        "rule": "Experiência prática não substitui atribuição formal registrada no Sistema Confea/Crea.",
        "periodic": True,
        "note": "Checar eventual decisão ou anotação específica no CREA."
    },
    "confea_1137": {
        "name": "Resolução Confea 1.137/2023 e Decisão Normativa 120/2023",
        "nature": "Norma profissional obrigatória - ART e TOS",
        "application": "ART, acervo técnico, atividades de laudo, vistoria e avaliação de equipamentos mecânicos.",
        "rule": "Classificar a ART conforme atividade real, forma de participação e escopo, observando que a Resolução 1.025/2009 está revogada.",
        "periodic": True,
        "note": "Fonte sujeita a atualizações operacionais do Confea/CREA."
    },
    "confea_etica": {
        "name": "Resolução Confea 1.002/2002 - Código de Ética",
        "nature": "Norma profissional obrigatória - ética",
        "application": "Imparcialidade, diligência, responsabilidade, linguagem e postura técnica.",
        "rule": "Manter objetividade e transparência; registrar limitações, erros materiais e conflitos sem linguagem defensiva.",
        "periodic": True,
        "note": "Útil em revisões contra impugnação e petições."
    },
    "crea_operacional": {
        "name": "Manuais e páginas oficiais de CREA sobre ART, TOS, perícia judicial e atribuições mecânicas",
        "nature": "Manual operacional oficial",
        "application": "Emissão de ART, seleção de TOS, regularização, baixa, CAT e exemplos de atribuições.",
        "rule": "Usar como orientação operacional do conselho competente, sem transformar guia local em lei geral.",
        "periodic": True,
        "note": "Verificar o CREA do estado do processo/profissional."
    },
    "nr12": {
        "name": "NR-12 - Segurança no Trabalho em Máquinas e Equipamentos",
        "nature": "Norma obrigatória - segurança do trabalho",
        "application": "Conformidade de máquinas, medidas de proteção, manutenção, inspeção, adaptação e análise de acidente.",
        "rule": "Em máquina ou equipamento, checar limites, uso previsto, proteção, estado de segurança na data do fato e histórico de adequação.",
        "periodic": True,
        "note": "Portal oficial indica alterações por portaria; verificar versão."
    },
    "manual_nr12": {
        "name": "Manual de Aplicação da NR-12",
        "nature": "Manual oficial consultivo",
        "application": "Tradução operacional da NR-12 e referências cruzadas com normas ABNT/ISO.",
        "rule": "Converter requisitos em perguntas de diligência, sem tratar o manual como substituto do texto da NR.",
        "periodic": True,
        "note": "Pode ser salvo integralmente se obtido do portal oficial."
    },
    "abnt_13752": {
        "name": "ABNT NBR 13752 - perícias de engenharia",
        "nature": "Referência técnica paga - consultiva por analogia",
        "application": "Estrutura, escopo, vistoria, metodologia e apresentação de laudo.",
        "rule": "Usar como backbone metodológico por analogia; não resolver causalidade mecânica apenas por ela.",
        "periodic": True,
        "note": "Não copiar integralmente; guardar ficha, índice, notas próprias e forma de aquisição."
    },
    "abnt_14653": {
        "name": "ABNT NBR 14653-1 e 14653-5",
        "nature": "Referência técnica paga - avaliação de bens",
        "application": "Avaliação de máquinas, equipamentos, instalações e bens industriais.",
        "rule": "Acionar quando o caso exigir valor, depreciação, vida útil, custo de reposição ou quantificação econômica.",
        "periodic": True,
        "note": "Normas pagas; não reproduzir o texto integral."
    },
    "abnt_seg_maquinas": {
        "name": "ABNT NBR ISO 12100, 13849-1/2, 14153, 13850, 13855, 13857, 14118, 14119, 14120, 4413 e 4414",
        "nature": "Referência técnica paga - segurança de máquinas",
        "application": "Apreciação de riscos, funções de segurança, proteções, intertravamentos, parada de emergência, hidráulica e pneumática.",
        "rule": "Usar como referência técnica subsidiária à NR-12 e ao manual oficial, respeitando licença e edição vigente.",
        "periodic": True,
        "note": "Não armazenar íntegra sem licença; manter checklists derivados."
    },
    "abnt_metrologia": {
        "name": "ABNT NBR ISO/IEC 17025, ISO 10012 e ISO 5725",
        "nature": "Referência técnica paga - metrologia e ensaios",
        "application": "Competência de laboratórios, gestão de medição, repetibilidade, precisão e avaliação de resultados.",
        "rule": "Nenhuma medição crítica deve ser usada sem checar instrumento, certificado, rastreabilidade, escopo e incerteza.",
        "periodic": True,
        "note": "Guardar ficha e checklist, não a íntegra."
    },
    "gum_vim_inmetro": {
        "name": "GUM, VIM, RBC/Inmetro, NIT-DICLA e DOQ-Cgcre correlatos",
        "nature": "Referência técnica institucional",
        "application": "Terminologia metrológica, expressão de incerteza, rastreabilidade e acreditação.",
        "rule": "Registrar unidade, método, instrumento, calibração, laboratório e incerteza sempre que a conclusão depender de medição.",
        "periodic": True,
        "note": "Materiais públicos devem manter versão e procedência."
    },
    "abnt_27037": {
        "name": "ABNT NBR ISO/IEC 27037:2013",
        "nature": "Referência técnica paga - evidência digital",
        "application": "Identificação, coleta, aquisição e preservação de evidência digital.",
        "rule": "Tratar fotos, vídeos, planilhas, logs e PDFs nativos como evidências digitais quando integridade e temporalidade importarem.",
        "periodic": True,
        "note": "Não copiar integralmente; usar metadados, escopo e instrução de aquisição."
    },
    "cpp_cadeia": {
        "name": "CPP, arts. 158-A e seguintes - cadeia de custódia",
        "nature": "Norma legal - uso analógico metodológico",
        "application": "Rastreabilidade, documentação de origem e preservação de vestígios.",
        "rule": "Usar por analogia em perícia cível/mecânica para reforçar procedência e integridade, sem converter em regra penal automática.",
        "periodic": True,
        "note": "Diferenciar aplicação direta criminal de boa prática cível."
    },
    "pop_mjsp": {
        "name": "POPs nacionais de perícia criminal e POP de Informática Forense/MJSP",
        "nature": "Manual técnico consultivo por analogia",
        "application": "Estrutura de laudo, registro de datas, integridade de anexos eletrônicos, hash e origem.",
        "rule": "Usar como boa prática para anexos digitais e documentação de evidências, não como obrigação legal de perícia cível.",
        "periodic": True,
        "note": "Salvar somente materiais públicos e oficiais."
    },
    "ibape_cartilha": {
        "name": "IBAPE/SP - Cartilha Perícias Judiciais de Engenharia e Arquitetura",
        "nature": "Fonte consultiva institucional",
        "application": "Pontos controvertidos, estrutura do laudo, fotos, parecer de assistente, esclarecimentos e linguagem.",
        "rule": "Usar como guia de método e redação, sem transformar cartilha em obrigação legal.",
        "periodic": True,
        "note": "Citar edição e preservar procedência."
    },
    "ibape_norma": {
        "name": "IBAPE/SP - Norma Básica para Perícias de Engenharia e versões históricas",
        "nature": "Fonte consultiva institucional/histórica",
        "application": "Terminologia, metodologia, objetividade, respostas a quesitos e estrutura de laudos.",
        "rule": "Usar como apoio metodológico; conferir status, edição e compatibilidade com CPC 2015.",
        "periodic": True,
        "note": "Não usar versão histórica como fundamento isolado."
    },
    "ibape_honorarios": {
        "name": "IBAPE/SP - Regulamento de Honorários",
        "nature": "Fonte consultiva profissional",
        "application": "Composição técnica de horas, complexidade, deslocamentos e insumos.",
        "rule": "Usar para decompor custos e justificar esforço, sem substituir tabela judicial aplicável.",
        "periodic": True,
        "note": "Tratamento consultivo, não legal obrigatório."
    },
    "ibape_etica": {
        "name": "IBAPE - Código de Ética e publicações institucionais",
        "nature": "Fonte consultiva institucional",
        "application": "Imparcialidade, linguagem técnica, postura em diligência e vedação de conclusões tendenciosas.",
        "rule": "Reforçar neutralidade e registro de interferências, sem confundir com norma do Confea.",
        "periodic": True,
        "note": "Citar edição quando usado."
    },
    "cnj_linguagem": {
        "name": "CNJ - Linguagem Simples e Manual de Padronização de Atos",
        "nature": "Fonte consultiva institucional",
        "application": "Clareza, coesão, inteligibilidade e objetividade em laudos e petições.",
        "rule": "Escrever em linguagem simples sem perder precisão técnica.",
        "periodic": True,
        "note": "Aderente ao CPC, art. 473, parágrafo 1º."
    },
    "manual_redacao": {
        "name": "Manual de Redação da Presidência da República",
        "nature": "Fonte consultiva de redação oficial",
        "application": "Impessoalidade, concisão, padronização e clareza.",
        "rule": "Usar para petições e manifestações formais, evitando excesso retórico.",
        "periodic": True,
        "note": "Não é fonte técnica de engenharia."
    },
    "lit_mecanica": {
        "name": "ASM Handbook Vol. 11, Bloch, Mobley, SKF, Shigley, Fluid Power, Pump User's Handbook, Dudley, RCM e vibração",
        "nature": "Referência técnica consultiva - literatura especializada",
        "application": "Análise de falhas, fadiga, fratura, desgaste, rolamentos, bombas, compressores, redutores, hidráulica e manutenção.",
        "rule": "Usar como apoio técnico de causalidade, sempre com ficha bibliográfica, edição e licença quando aplicável.",
        "periodic": True,
        "note": "Não copiar livros comerciais; guardar metadados e notas próprias."
    },
    "visual_evidence": {
        "name": "Guias de evidência visual e boas práticas de documentação fotográfica",
        "nature": "Fonte secundária consultiva",
        "application": "Contexto, autoria, data, local, metadados, sequência e preservação de fotos/vídeos.",
        "rule": "Registrar quem, o quê, onde, quando e por que de cada imagem; preservar original.",
        "periodic": True,
        "note": "Não substituir CPC, IBAPE ou referência oficial."
    }
}


STANDARD_LIMITATIONS = [
    "A base não substitui consulta ao processo, despacho de nomeação, PJe/SIPER, texto oficial vigente nem orientação do juízo.",
    "Normas ABNT pagas e livros comerciais devem ser mantidos apenas como ficha, metadados, índice de aplicação e notas próprias, salvo licença válida.",
    "Fontes consultivas, cartilhas, manuais e literatura técnica não podem ser convertidos automaticamente em obrigação legal.",
    "Toda fonte marcada com [VP] precisa de verificação periódica de vigência, edição, revogação, atualização ou tabela aplicável."
]


STANDARD_DONTS = [
    "Não copiar integralmente normas pagas, livros comerciais ou standards protegidos por licença.",
    "Não misturar lei, resolução, manual, jurisprudência, cartilha, opinião técnica e literatura como se tivessem a mesma força normativa.",
    "Não usar fonte consultiva como obrigação legal, nem apresentar boa prática como comando judicial obrigatório.",
    "Não citar fonte não lida, repositório não oficial ou resumo de terceiros como se fosse documento oficial."
]


def table(headers, rows):
    def clean(cell):
        return str(cell).replace("\n", "<br>").replace("|", "\\|")
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        out.append("| " + " | ".join(clean(c) for c in row) + " |")
    return "\n".join(out)


def source_table(ids):
    rows = []
    for source_id in ids:
        source = SOURCE_CATALOG[source_id]
        marker = " [VP]" if source["periodic"] else ""
        rows.append([
            source["name"] + marker,
            source["nature"],
            source["application"],
            source["rule"],
            source["note"]
        ])
    return table(["Fonte", "Natureza", "Aplicação", "Regra extraída", "Observação"], rows)


def checklist_block(checklists):
    lines = []
    for title, items in checklists:
        lines.append(f"## {title}")
        for item in items:
            lines.append(f"- [ ] {item}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def bullets(items):
    return "\n".join(f"- {item}" for item in items) + "\n"


def model_block(models):
    lines = []
    for title, body in models:
        lines.append(f"## {title}")
        lines.append("```md")
        lines.append(body.strip())
        lines.append("```")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def tables_block(tables):
    lines = []
    for title, headers, rows in tables:
        lines.append(f"## {title}")
        lines.append(table(headers, rows))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


SKILLS = [
    {
        "folder": "pericia-01-triagem-processual",
        "name": "triagem-processual-pericia",
        "title": "Triagem Processual da Perícia",
        "description": "Triar nomeações, escopo, competência técnica, impedimentos, custeio, prazos e condições de aceite em perícias judiciais de engenharia mecânica.",
        "primary": ["cpc_pericia", "cnj_233", "cnj_232", "tjce_07_2024", "tjce_14_2022", "tjce_manual_pje", "lei_5194", "lei_6496", "confea_218", "confea_1073", "confea_345", "confea_1137"],
        "secondary": ["stj_jurisprudencia", "ibape_cartilha", "cnj_linguagem", "manual_redacao", "crea_operacional"],
        "rules": [
            "Ler primeiro a decisão de nomeação, classe processual, objeto da perícia, prazo do laudo, existência de audiência, quesitos já apresentados e regime de custeio.",
            "Checar impedimento, suspeição, vínculo com partes, atuação prévia como assistente técnico e qualquer circunstância capaz de comprometer a imparcialidade.",
            "Confrontar o objeto técnico com as atribuições reais do engenheiro mecânico; se houver extrapolação, sugerir escusa, delimitação de escopo ou perícia em equipe.",
            "Diferenciar perícia gratuita, não gratuita, INSS acidentário, competência federal delegada e casos sem custeio claro.",
            "Registrar pendências operacionais: acesso ao PJe, cadastro/SIPER, certificado digital, dados bancários, ART e documentos de qualificação.",
            "Classificar o aceite como: aceitar, aceitar com ressalva, pedir esclarecimento, pedir equipe multidisciplinar, pedir prorrogação, escusar ou declarar impedimento."
        ],
        "checklists": [
            ("Aceite inicial", ["Nomeação formal localizada", "Objeto da perícia delimitado", "Prazo do laudo identificado", "Audiência futura verificada", "Quesitos e assistentes já mapeados", "Regime de custeio identificado", "Acesso ao PJe/SIPER confirmado"]),
            ("Compatibilidade profissional", ["Objeto aderente à engenharia mecânica", "Registro CREA ativo", "Atribuição compatível com o tema", "Necessidade de outra especialidade analisada", "ART prevista no fluxo", "Currículo/especialização compatível disponível"]),
            ("Conflitos e riscos", ["Impedimento ou suspeição checados", "Atuação anterior como assistente técnico verificada", "Vínculos econômicos ou pessoais declarados", "Risco de prazo exíguo avaliado", "Risco de pagamento/adiantamento avaliado"])
        ],
        "tables": [
            ("Matriz de decisão de aceite", ["Condição encontrada", "Ação sugerida", "Risco se ignorada"], [
                ["Objeto claramente mecânico e documentação mínima disponível", "Aceitar e preparar proposta/roteiro", "Baixo"],
                ["Objeto mecânico com interfaces elétrica, civil, química ou segurança complexa", "Aceitar com delimitação ou pedir equipe multidisciplinar", "Extrapolação de competência"],
                ["Objeto fora da atribuição mecânica", "Escusar ou requerer substituição/complementação", "Atuação fora de atribuição"],
                ["Conflito, vínculo ou assistência técnica prévia relevante", "Declarar impedimento/suspeição ou pedir orientação do juízo", "Incidente processual e perda de confiança"],
                ["Prazo incompatível com volume de autos e diligência", "Pedir prorrogação antes do vencimento", "Atraso e substituição"]
            ]),
            ("Campos mínimos da triagem", ["Campo", "Uso", "Obrigatório"], [
                ["Processo, vara, comarca", "Identificação do encargo", "Sim"],
                ["Objeto técnico", "Checar competência e escopo", "Sim"],
                ["Prazo do laudo", "Controle de agenda", "Sim"],
                ["Custeio", "Honorários e viabilidade", "Sim"],
                ["Quesitos", "Dimensionamento do trabalho", "Sim"],
                ["Conflitos", "Imparcialidade", "Sim"]
            ])
        ],
        "models": [
            ("RELATORIO_TRIAGEM_PROCESSUAL.md", """
# Relatório de Triagem Processual da Perícia

## Identificação
Processo:
Vara/Comarca:
Data da intimação:
Prazo do laudo:

## Objeto técnico informado pelo juízo
[descrever de forma objetiva]

## Compatibilidade com engenharia mecânica
[compatível / parcialmente compatível / não compatível]
Fundamento técnico-profissional:

## Impedimento, suspeição e conflitos
[sem conflito identificado / conflito a declarar / precisa de confirmação]

## Custeio e honorários
[justiça gratuita / não gratuita / indefinido]
Fonte local a verificar:

## Recomendação
[aceitar / aceitar com ressalva / pedir delimitação / pedir equipe / escusar / declarar conflito]

## Pendências antes do primeiro ato técnico
- [pendência 1]
- [pendência 2]
""")
        ],
        "phrases": [
            "A presente triagem limita-se às condições processuais e técnico-profissionais de aceite do encargo.",
            "O objeto descrito nos autos apresenta aderência inicial ao campo da engenharia mecânica, ressalvada a confirmação em diligência.",
            "Há interface com especialidade diversa, recomendando-se delimitação do escopo ou atuação em equipe.",
            "Não foram identificados, nesta etapa, elementos objetivos de impedimento ou suspeição, sem prejuízo de comunicação imediata caso sobrevenha fato novo.",
            "A aceitação do encargo pressupõe acesso aos autos, prazo compatível, definição de custeio e emissão da ART quando cabível."
        ],
        "risks": [
            "Aceitar objeto fora das atribuições mecânicas.",
            "Ignorar conflito de interesse, vínculo anterior ou atuação como assistente técnico.",
            "Não verificar a tabela de honorários ou regra local antes de estimar custo.",
            "Perder prazo por não registrar a data de intimação oficial.",
            "Atuar sem acesso regular ao PJe/SIPER ou sem documentação profissional mínima."
        ],
        "limitations": [
            "A triagem não decide o mérito técnico do litígio.",
            "A contagem oficial de prazos depende do PJe, calendário forense e ato de intimação.",
            "A classificação de custeio e rubrica de honorários precisa ser conferida no tribunal competente."
        ],
        "donts": [
            "Não aceitar tacitamente nomeação quando houver dúvida objetiva de impedimento, competência ou objeto.",
            "Não afirmar que a perícia é viável sem ler a decisão de nomeação e o objeto delimitado.",
            "Não tratar experiência prática como substituta de atribuição formal registrada."
        ]
    },
    {
        "folder": "pericia-02-analise-documental",
        "name": "analise-documental-processual",
        "title": "Análise Documental Processual",
        "description": "Organizar inicial, contestação, documentos técnicos, evidências, lacunas e suficiência documental em perícias judiciais de engenharia mecânica.",
        "primary": ["cpc_documentos", "cpc_pericia", "lei_5194", "lei_6496", "confea_218", "confea_345", "confea_1137", "cnj_233", "tjce_07_2024", "tjce_manual_pje"],
        "secondary": ["ibape_cartilha", "ibape_norma", "cnj_linguagem", "abnt_27037", "pop_mjsp", "gum_vim_inmetro", "abnt_metrologia"],
        "rules": [
            "Separar alegação da parte, documento juntado, fato documental convergente, fato tecnicamente provável e fato tecnicamente constatado.",
            "Classificar documentos por origem: processual, contratual/comercial, técnico originário, técnico derivado, manutenção/operação, metrológico/laboratorial, imagético/digital ou opinativo.",
            "Checar autoria, data, contexto, vínculo com ativo, assinatura, ART, integridade, legibilidade e pertinência a quesitos.",
            "Tratar laudo ou parecer anterior como documento opinativo técnico, salvo se houver contraditório, método, ART e aderência ao objeto.",
            "Recomendar diligência quando houver lacuna de nexo entre documento e ativo, baixa integridade, ausência de original ou insuficiência para responder quesitos.",
            "Não fechar causalidade na análise documental; apontar suficiência, insuficiência, contradições e providências."
        ],
        "checklists": [
            ("Triagem processual", ["Pedidos e causa de pedir identificados", "Narrativa da inicial separada da contestação", "Documentos de cada parte inventariados", "Quesitos já apresentados listados", "Decisão de nomeação e objeto conferidos"]),
            ("Triagem técnica", ["Ativo, sistema, componente, modelo, TAG, placa ou série identificados", "Manual/catálogo compatível com o equipamento localizado", "Histórico de manutenção contemporâneo mapeado", "ART, CREA, autor e método de laudos anteriores conferidos", "Certificados e relatórios vinculados às medições debatidas"]),
            ("Integridade e suficiência", ["Documento é original, cópia, scan ou reprodução", "Assinatura verificável", "Data compatível com evento", "Documento responde a qual quesito", "Há contradição com outro documento", "Exige original ou arquivo nativo"])
        ],
        "tables": [
            ("Matriz documental", ["ID", "Classe", "Origem", "Data", "Ativo vinculado", "Força", "Status probatório", "Quesito"], [
                ["DOC-001", "processual", "autor/réu/juízo", "[data]", "[ativo]", "alta/média/baixa", "alegação simples / suporte unilateral / convergente / provável / constatado", "Q..."],
                ["DOC-002", "técnico originário", "fabricante", "[data]", "[modelo/série]", "alta", "fato documental convergente", "Q..."],
                ["DOC-003", "opinativo", "assistente/perito anterior", "[data]", "[ativo]", "média", "elemento opinativo técnico", "Q..."]
            ]),
            ("Escala de força documental", ["Força", "Critério", "Uso"], [
                ["Alta", "Autoria, data, vínculo, integridade, método e contraditório fortes", "Pode sustentar achado preliminar, ainda sujeito ao escopo"],
                ["Média", "Relevante, mas unilateral, indireto, incompleto ou dependente de confirmação", "Usar com ressalva e cruzamento"],
                ["Baixa", "Sem autoria, sem contexto, sem vínculo ou sem legibilidade", "Inventariar, mas não fundamentar conclusão"]
            ])
        ],
        "models": [
            ("RELATORIO_PRELIMINAR_ANALISE_DOCUMENTAL.md", """
# Relatório Preliminar de Análise Documental

## Identificação
Processo:
Vara:
Perito:
Data:

## Escopo desta etapa
Esta análise examina suficiência, pertinência e consistência documental, sem substituir diligência, vistoria, exame ou ensaio eventualmente necessários.

## Peças processuais examinadas
- petição inicial;
- contestação;
- decisão de nomeação;
- quesitos;
- documentos técnicos anexos.

## Síntese das alegações relevantes
### Autor
[tópicos factuais]
### Réu
[tópicos factuais]

## Documentos tecnicamente mais relevantes
| Documento | Relevância | Quesitos vinculados | Ressalvas |
|---|---|---|---|

## Contradições e lacunas
[listar]

## Avaliação preliminar de suficiência
[suficiente / parcialmente suficiente / insuficiente sem diligência / exige originais]

## Providências técnicas recomendadas
[documentos, originais, diligência, ensaio, esclarecimentos]
""")
        ],
        "phrases": [
            "Nos documentos examinados até o momento, verifica-se...",
            "A alegação encontra suporte documental unilateral em...",
            "Há convergência parcial entre os documentos X, Y e Z quanto a...",
            "Não foi localizada, nos autos, documentação contemporânea suficiente para...",
            "O documento apresentado é relevante, mas não permite, isoladamente, concluir...",
            "A definição técnica do ponto demanda diligência, inspeção ou exame complementar."
        ],
        "risks": [
            "Laudo anterior sem autoria, CREA, atribuição ou ART.",
            "Manual genérico de linha usado como se fosse manual do modelo exato.",
            "Foto sem data, local, escala, autoria ou arquivo original.",
            "Certificado de calibração sem vínculo com instrumento usado no caso.",
            "Documentos produzidos após o litígio apresentados como se fossem contemporâneos ao evento."
        ],
        "limitations": [
            "A análise documental não substitui vistoria quando houver dúvida sobre estado físico do equipamento.",
            "A skill não declara falsidade documental; apenas aponta fragilidade, necessidade de original ou exame especializado.",
            "A suficiência documental pode mudar com novos documentos, diligência ou quesitos suplementares."
        ],
        "donts": [
            "Não concluir nexo causal definitivo só com base em documentos unilaterais.",
            "Não reproduzir longamente inicial e contestação; resumir, classificar e testar.",
            "Não tratar parecer de assistente como prova neutra sem checar escopo, método e responsabilidade técnica."
        ]
    },
    {
        "folder": "pericia-03-proposta-honorarios",
        "name": "proposta-honorarios-periciais",
        "title": "Proposta de Honorários Periciais",
        "description": "Preparar propostas de honorários periciais com base em CPC, CNJ, TJCE, complexidade técnica, horas, diligências, ART e custos operacionais.",
        "primary": ["cpc_pericia", "cnj_232", "tjce_07_2024", "tjce_portarias", "tjce_manual_pje", "lei_6496", "confea_1137"],
        "secondary": ["ibape_honorarios", "stj_jurisprudencia", "ibape_cartilha", "manual_redacao", "cnj_linguagem"],
        "rules": [
            "Identificar se o caso é de justiça gratuita, não gratuita, custeio por parte, rateio, Fazenda Pública, INSS acidentário ou competência federal delegada.",
            "Selecionar tabela local pela data de realização da perícia, não apenas pela data da nomeação, e verificar a portaria vigente.",
            "Compor valor por horas de estudo, análise documental, diligência, deslocamento, medições, ensaios, redação, revisão, anexos, ART e eventual equipe.",
            "Distinguir fundamento legal de arbitramento de fonte consultiva de composição econômica.",
            "Explicitar complexidade, especialização, local, tempo, peculiaridades e riscos de despesas não adiantadas.",
            "Em justiça gratuita no TJCE, considerar que o pagamento local pode não prever adiantamento de despesas; conferir regra vigente."
        ],
        "checklists": [
            ("Entradas obrigatórias", ["Regime de custeio identificado", "Data provável de realização da perícia", "Tabela/portaria vigente conferida", "Objeto e quesitos dimensionados", "Volume de autos estimado", "Diligências e deslocamentos previstos", "Necessidade de medições/ensaios/equipe avaliada", "ART considerada"]),
            ("Memória de cálculo", ["Horas por etapa descritas", "Custos diretos separados", "Custos de terceiros justificados", "Tributos/despesas operacionais tratados conforme prática local", "Rubrica da tabela indicada", "Risco de complementação previsto"]),
            ("Peças anexas", ["Currículo", "Comprovação de especialidade", "Dados de contato", "Dados bancários quando cabível", "ART ou previsão de emissão", "Planilha resumida"])
        ],
        "tables": [
            ("Composição sugerida", ["Etapa", "Horas/Unidade", "Justificativa", "Valor"], [
                ["Análise dos autos", "[h]", "Volume documental e pontos controvertidos", "[R$]"],
                ["Diligência/vistoria", "[h/diárias]", "Deslocamento, acesso, registro e coleta", "[R$]"],
                ["Medições/ensaios", "[h/serviço]", "Instrumentos, laboratório ou especialista", "[R$]"],
                ["Redação do laudo", "[h]", "Método, respostas e anexos", "[R$]"],
                ["ART e despesas regulatórias", "[unidade]", "Responsabilidade técnica", "[R$]"]
            ]),
            ("Regime de custeio", ["Situação", "Base principal", "Ação"], [
                ["Não gratuita", "CPC, proposta e arbitramento", "Pedir depósito/adiantamento conforme decisão"],
                ["Justiça gratuita com tabela local", "CNJ 232 + portaria do tribunal", "Usar rubrica e data vigente"],
                ["Justiça gratuita sem tabela local", "CNJ 232", "Justificar complexidade e parâmetros nacionais"],
                ["Custeio incerto", "Despacho e regras locais", "Pedir esclarecimento antes da diligência"]
            ])
        ],
        "models": [
            ("PROPOSTA_HONORARIOS.md", """
# Proposta de Honorários Periciais

Excelentíssimo Senhor Doutor Juiz de Direito da ___ Vara ___ da Comarca de ___

Processo nº:
Perito:

## Objeto e escopo
[descrever objeto da perícia, quesitos centrais e diligências previstas]

## Complexidade técnica
[volume documental, necessidade de vistoria, medições, ensaios, análise de falha, NR-12, avaliação patrimonial ou equipe]

## Memória resumida de honorários
| Etapa | Estimativa | Justificativa |
|---|---:|---|

## Valor proposto
Valor total: R$ ___

## Observações
O valor considera a execução do escopo atualmente delimitado. Quesitos suplementares, ensaios laboratoriais, nova diligência ou documentos supervenientes poderão justificar complementação, se autorizada pelo juízo.

Nestes termos, pede deferimento.
""")
        ],
        "phrases": [
            "A presente proposta considera a complexidade técnica, o volume documental, a necessidade de diligência e a especialização exigida pelo objeto.",
            "O enquadramento sugerido observa a tabela local vigente, sujeita à confirmação no portal oficial do tribunal.",
            "Os custos de ensaio, deslocamento extraordinário ou equipe especializada foram destacados para evitar confusão com a verba básica do trabalho pericial.",
            "A eventual ampliação do escopo por quesitos suplementares ou nova diligência poderá demandar complementação de honorários.",
            "O regulamento profissional consultivo foi utilizado apenas para decomposição de esforço, sem substituir a tabela judicial aplicável."
        ],
        "risks": [
            "Usar tabela de honorários vencida ou futura sem observar data de realização.",
            "Subestimar horas de diligência, análise de autos e respostas a quesitos.",
            "Não prever ART, ensaio, laboratório, deslocamento ou equipe necessária.",
            "Confundir justiça gratuita com obrigação de custear despesas próprias sem previsão.",
            "Apresentar proposta genérica sem memória de cálculo."
        ],
        "limitations": [
            "A skill não garante arbitramento pelo juízo.",
            "A rubrica de engenharia mecânica pode depender da tabela local e nem sempre aparecer nominalmente.",
            "A classificação tributária, fiscal ou contábil do recebimento deve ser tratada fora desta skill."
        ],
        "donts": [
            "Não substituir tabela judicial por regulamento consultivo do IBAPE.",
            "Não prometer resultado técnico em troca de valor.",
            "Não incluir despesa de terceiro sem explicar pertinência, autorização e relação com o escopo."
        ]
    },
    {
        "folder": "pericia-04-matriz-quesitos",
        "name": "matriz-quesitos",
        "title": "Matriz de Quesitos",
        "description": "Consolidar, classificar e rastrear quesitos do juízo, partes e Ministério Público, vinculando cada resposta a método, evidência, fonte e limitação.",
        "primary": ["cpc_pericia", "confea_345", "ibape_cartilha", "ibape_norma", "cnj_linguagem"],
        "secondary": ["abnt_13752", "nr12", "manual_nr12", "abnt_seg_maquinas", "gum_vim_inmetro", "lit_mecanica"],
        "rules": [
            "Transcrever cada quesito sem alterar seu sentido e manter identificação de origem: juízo, autor, réu, MP ou suplementar.",
            "Classificar quesitos como técnico-mecânicos, metrológicos, documentais, de segurança, avaliatórios, jurídicos/impertinentes ou dependentes de diligência.",
            "Vincular cada quesito a método, evidência necessária, fonte técnica aplicável e seção provável do laudo.",
            "Marcar quesitos que pedem juízo de culpa, ilicitude, dolo, contrato ou interpretação jurídica para resposta com ressalva técnica.",
            "Atualizar a matriz quando surgirem quesitos suplementares durante a diligência.",
            "Antes do laudo final, conferir se todos os quesitos deferidos têm resposta expressa."
        ],
        "checklists": [
            ("Consolidação", ["Todos os quesitos do juízo listados", "Todos os quesitos das partes listados", "Quesitos suplementares reservados", "Numeração original preservada", "Origem de cada quesito identificada"]),
            ("Classificação técnica", ["Tema técnico identificado", "Método necessário definido", "Evidência mínima vinculada", "Fonte normativa/técnica selecionada", "Quesito jurídico/impertinente marcado com ressalva"]),
            ("Pré-laudo", ["Nenhum quesito deferido sem resposta", "Respostas não contradizem análise", "Limitações vinculadas aos quesitos afetados", "Fotos/tabelas/anexos citados nas respostas"])
        ],
        "tables": [
            ("Matriz principal de quesitos", ["ID", "Origem", "Quesito resumido", "Tema", "Método", "Evidência", "Fonte", "Status"], [
                ["QJ-01", "Juízo", "[texto]", "Objeto/causalidade", "Inspeção + análise documental", "DOC/EV/MED", "CPC + técnica aplicável", "pendente/respondido"],
                ["QA-01", "Autor", "[texto]", "Falha mecânica", "Análise de falhas", "Evidências físicas/fotos/manutenção", "literatura mecânica", "pendente/respondido"],
                ["QR-01", "Réu", "[texto]", "Manutenção/operação", "Documental + diligência", "OS/logs/manuais", "manual fabricante + técnica", "pendente/respondido"]
            ]),
            ("Classificação de resposta", ["Tipo de quesito", "Resposta segura", "Risco"], [
                ["Técnico com evidência suficiente", "Responder conclusivamente com método e anexo", "Baixo"],
                ["Técnico com lacuna", "Responder com limitação e providência", "Médio"],
                ["Jurídico ou de culpa", "Responder apenas no limite técnico", "Extrapolação"],
                ["Impertinente ao objeto", "Apontar ausência de relação técnica com o objeto", "Discussão processual"]
            ])
        ],
        "models": [
            ("MATRIZ_QUESITOS.md", """
# Matriz de Quesitos

| ID | Origem | Quesito integral | Tema técnico | Método necessário | Evidência vinculada | Fonte aplicável | Resposta/Status |
|---|---|---|---|---|---|---|---|

## Quesitos que exigem ressalva
- [ID] - motivo da ressalva técnica:

## Quesitos dependentes de diligência ou documento
- [ID] - providência necessária:

## Controle de respostas no laudo
- [ ] Todos os quesitos deferidos foram respondidos.
- [ ] Quesitos suplementares foram incorporados.
- [ ] Limitações foram vinculadas aos quesitos afetados.
""")
        ],
        "phrases": [
            "O quesito é respondido no limite técnico da engenharia mecânica, sem emissão de juízo jurídico.",
            "A resposta depende da apresentação de documento ou evidência ainda não localizada nos autos.",
            "A análise técnica disponível permite responder parcialmente ao quesito, com as seguintes limitações...",
            "O quesito foi relacionado à evidência EV-___ e ao documento DOC-___.",
            "A formulação extrapola o escopo técnico pericial ao requerer conclusão sobre culpa, dolo ou responsabilidade jurídica."
        ],
        "risks": [
            "Omitir quesito deferido.",
            "Responder quesito jurídico como se fosse conclusão técnica.",
            "Alterar redação do quesito e mudar seu sentido.",
            "Responder sem evidência ou método rastreável.",
            "Não atualizar a matriz com quesitos suplementares."
        ],
        "limitations": [
            "A matriz organiza perguntas e rastreabilidade; não substitui a análise técnica do laudo.",
            "Quesitos impertinentes ou jurídicos devem ser tratados com ressalva, mas a decisão de indeferimento é do juízo.",
            "O grau de resposta pode mudar após diligência ou novos documentos."
        ],
        "donts": [
            "Não responder todos os quesitos em bloco sem identificação individual.",
            "Não usar resposta monossilábica quando o quesito exige método e fundamento.",
            "Não deixar quesito sem status claro: respondido, parcial, prejudicado, dependente ou fora do escopo."
        ]
    },
    {
        "folder": "pericia-05-roteiro-diligencia",
        "name": "roteiro-diligencia-mecanica",
        "title": "Roteiro de Diligência Mecânica",
        "description": "Planejar e executar diligência/vistoria mecânica judicial com comunicação, segurança, registro, medições, evidências, limitações e ata técnica.",
        "primary": ["cpc_pericia", "confea_345", "nr12", "manual_nr12", "abnt_seg_maquinas", "gum_vim_inmetro", "ibape_cartilha"],
        "secondary": ["abnt_13752", "visual_evidence", "ibape_etica", "abnt_27037", "pop_mjsp", "crea_operacional"],
        "rules": [
            "Planejar a diligência a partir de decisão, objeto, quesitos, riscos do local, documentos necessários, instrumentos e EPIs.",
            "Comunicar data, hora, local e finalidade técnica por via formal, preservando contraditório e acompanhamento por assistentes.",
            "Registrar abertura, presentes, condições ambientais, condições de acesso, estado da máquina e limitações iniciais.",
            "Fotografar do geral para o detalhe: local, equipamento, placa/TAG, proteções, transmissão, danos, instrumentos e medições.",
            "Registrar instrumentos, calibração, unidade, condição da máquina, método de medição e incerteza relevante.",
            "Não realizar ensaio destrutivo, desmontagem, operação insegura ou alteração de estado sem autorização, segurança e registro.",
            "Encerrar com ata, lista de evidências, documentos recebidos, pendências e limitações."
        ],
        "checklists": [
            ("Antes da saída", ["Decisão e quesitos lidos", "Documentos a solicitar listados", "Riscos e EPIs avaliados", "Instrumentos definidos e calibração conferida", "Comunicação às partes comprovada", "Plano fotográfico preparado"]),
            ("Abertura em campo", ["Data, hora e local registrados", "Presentes identificados", "Condições de acesso anotadas", "Finalidade técnica informada", "Ausências e recusas registradas", "Limitações iniciais anotadas"]),
            ("Registro do equipamento", ["Foto geral do local", "Foto geral do equipamento", "Placa, TAG e série", "Proteções e comandos", "Acoplamentos/transmissão", "Danos e anomalias", "Medições com instrumento visível", "Vídeos preservados quando úteis"]),
            ("Encerramento", ["Hora final registrada", "Evidências catalogadas", "Documentos recebidos listados", "Pendências e limitações descritas", "Providências complementares sugeridas"])
        ],
        "tables": [
            ("Dados mínimos do equipamento", ["Campo", "Exemplo", "Uso"], [
                ["Fabricante/modelo/série", "Bomba BC-01, série...", "Vincular documentos e manuais"],
                ["TAG/patrimônio/local", "ME-01/casa de máquinas", "Rastreabilidade"],
                ["Condição operacional", "ligado/desligado/desmontado", "Interpretar medições"],
                ["Histórico disponível", "OS, logs, manutenção", "Causalidade"],
                ["Proteções e segurança", "grade, intertravamento, emergência", "NR-12"]
            ]),
            ("Registro de medição", ["ID", "Grandeza", "Instrumento", "Certificado", "Valor", "Condição", "Quesito"], [
                ["MED-001", "folga radial", "relógio comparador", "válido até...", "0,20 mm", "máquina parada/fria", "Q3"],
                ["MED-002", "desalinhamento", "relógio/comparador", "válido até...", "[valor]", "[condição]", "Q4"]
            ])
        ],
        "models": [
            ("ATA_VISTORIA_TECNICA.md", """
# Ata / Termo de Vistoria Técnica

Processo nº:
Perito:
Data:
Horário de início:
Horário de término:
Local:

## Objeto da vistoria
| Equipamento/Sistema | Fabricante | Modelo | Série/TAG | Local |
|---|---|---|---|---|

## Presentes
| Nome | Qualificação | Parte/Empresa | Função | Contato |
|---|---|---|---|---|

## Condições de acesso e operação
- Acesso ao local:
- Equipamento energizado:
- Equipamento em operação:
- Restrições:

## Evidências e medições registradas
| ID | Tipo | Descrição | Quesitos relacionados |
|---|---|---|---|

## Limitações e pendências
[descrever]

As constatações registradas referem-se ao estado observado no momento da diligência. As conclusões técnicas serão apresentadas no laudo.
""")
        ],
        "phrases": [
            "A diligência teve finalidade exclusivamente técnica, voltada ao registro do estado observado e à coleta de elementos para resposta aos quesitos.",
            "No momento da vistoria, o equipamento encontrava-se...",
            "A medição foi realizada com o instrumento identificado no inventário, sob a condição operacional descrita.",
            "Não foi possível acessar o componente indicado, em razão de...",
            "A limitação registrada reduz o alcance da análise quanto a..."
        ],
        "risks": [
            "Falha de comunicação às partes e assistentes.",
            "Operar máquina em condição insegura ou alterar estado da evidência.",
            "Medição sem instrumento identificado ou calibração verificada.",
            "Fotografar apenas detalhes sem contexto geral.",
            "Não registrar recusa, ausência, limitação ou impedimento."
        ],
        "limitations": [
            "A diligência registra o estado observado; conclusões causais dependem de análise posterior.",
            "A segurança do local prevalece sobre qualquer tentativa de ensaio ou operação.",
            "Ensaios destrutivos, desmontagens e testes sob carga exigem autorização e condições controladas."
        ],
        "donts": [
            "Não debater mérito jurídico com as partes durante a diligência.",
            "Não prometer conclusão técnica no local.",
            "Não editar, renomear de forma destrutiva ou sobrescrever arquivos originais de evidência."
        ]
    },
    {
        "folder": "pericia-06-inventario-evidencias",
        "name": "inventario-evidencias",
        "title": "Inventário de Evidências",
        "description": "Catalogar documentos, fotos, vídeos, medições, peças, certificados e evidências digitais com rastreabilidade, integridade e vínculo a quesitos.",
        "primary": ["cpc_pericia", "abnt_27037", "cpp_cadeia", "pop_mjsp", "gum_vim_inmetro", "abnt_metrologia", "abnt_14653"],
        "secondary": ["ibape_cartilha", "visual_evidence", "cnj_linguagem", "confea_345", "abnt_13752"],
        "rules": [
            "Atribuir ID único e estável para cada evidência: DOC, EV, FOTO, VID, MED, PEC ou LOG.",
            "Registrar origem, autoria, data/hora, local, equipamento, descrição, arquivo, formato, preservação, relevância, quesitos e limitações.",
            "Preservar arquivo original e trabalhar em cópias quando houver necessidade de redimensionamento, anotação ou exportação.",
            "Vincular medições a instrumento, certificado, calibração, unidade, condição da máquina e incerteza relevante.",
            "Registrar evidência não disponível como item próprio, com origem da informação e efeito sobre a análise.",
            "Usar cadeia de custódia e evidência digital por analogia metodológica, sem criar obrigação criminal automática."
        ],
        "checklists": [
            ("Recebimento", ["ID atribuído", "Origem identificada", "Autoria registrada", "Data/hora registrada", "Formato e arquivo anotados", "Vínculo com ativo e quesito indicado"]),
            ("Integridade digital", ["Original preservado", "Cópia de trabalho separada", "Metadados disponíveis avaliados", "Hash registrado quando relevante", "Edição/corte/recompressão anotados", "Arquivo nativo solicitado quando necessário"]),
            ("Medições e ensaios", ["Instrumento identificado", "Certificado conferido", "Laboratório/escopo avaliados", "Unidade e incerteza registradas", "Condição operacional descrita", "Foto da medição anexada"]),
            ("Fechamento", ["Evidências usadas no laudo citadas", "Evidências descartadas justificadas", "Limitações por ausência destacadas", "Anexos numerados em ordem lógica"])
        ],
        "tables": [
            ("Schema do inventário", ["Campo", "Descrição", "Exemplo"], [
                ["id_evidencia", "Código único", "EV-001"],
                ["tipo", "foto, vídeo, documento, medição, peça, log", "foto"],
                ["origem", "perito, parte, terceiro, autos", "perito"],
                ["data_hora_coleta", "momento da coleta", "2026-05-16 09:15"],
                ["equipamento_relacionado", "ativo, TAG, série", "motobomba BC-01"],
                ["condicao_preservacao", "original, cópia, indisponível", "original preservado"],
                ["quesitos_relacionados", "IDs dos quesitos", "Q1;Q3"],
                ["limitacoes", "restrições de uso", "sem escala"]
            ]),
            ("Status de evidência", ["Status", "Uso permitido", "Exemplo"], [
                ["válida", "Pode fundamentar achado com demais elementos", "foto original, medição calibrada"],
                ["válida com ressalva", "Usar com limitação explícita", "foto com reflexo, mas contexto suficiente"],
                ["em análise", "Aguardar confirmação", "documento sem assinatura verificável"],
                ["indisponível", "Registrar lacuna", "peça removida não apresentada"],
                ["não conclusiva isoladamente", "Apoio contextual", "screenshot sem arquivo nativo"]
            ])
        ],
        "models": [
            ("INVENTARIO_EVIDENCIAS.csv", """
id_evidencia,tipo,origem,data_hora_coleta,localizacao,equipamento_relacionado,descricao,metodo_registro,arquivo_nome,formato,autor_registro,instrumento_utilizado,calibracao_verificada,condicao_preservacao,relevancia_tecnica,quesitos_relacionados,limitacoes,status,observacoes
EV-001,foto,perito,YYYY-MM-DD HH:MM,local,equipamento,descrição,foto digital,EV-001.jpg,jpg,perito,n/a,n/a,original preservado,contexto,Q1,nenhuma,válida,observação
MED-001,medicao,perito,YYYY-MM-DD HH:MM,local,equipamento,medição de...,medição direta,MED-001.pdf,pdf,perito,instrumento série...,sim,registro preservado,dado quantitativo,Q3,condição descrita,válida,unidade e incerteza registradas
""")
        ],
        "phrases": [
            "A evidência foi catalogada como válida com ressalva, pois...",
            "O arquivo original foi preservado e a versão de trabalho foi usada apenas para apresentação.",
            "A ausência do componente físico impede exame direto, razão pela qual a análise se limita aos registros disponíveis.",
            "A medição foi vinculada ao instrumento identificado e à condição operacional registrada.",
            "A fotografia contextualiza visualmente o achado, mas não define isoladamente a causa técnica."
        ],
        "risks": [
            "Sobrescrever arquivo original.",
            "Perder vínculo entre foto, local, ativo e quesito.",
            "Usar medição sem calibração, unidade ou condição operacional.",
            "Tratar screenshot como arquivo nativo.",
            "Ignorar evidência ausente que era essencial ao nexo causal."
        ],
        "limitations": [
            "Inventário não autentica juridicamente documento nem substitui perícia digital especializada.",
            "Hash e metadados só são úteis quando coletados de modo consistente e preservados.",
            "Evidências fornecidas por partes devem ser tratadas com origem e potencial unilateralidade."
        ],
        "donts": [
            "Não editar evidência original.",
            "Não apagar metadados deliberadamente.",
            "Não concluir causa de falha a partir de imagem isolada sem análise técnica."
        ]
    },
    {
        "folder": "pericia-07-anexo-fotografico",
        "name": "gerador-anexo-fotografico",
        "title": "Gerador de Anexo Fotográfico",
        "description": "Gerar anexos fotográficos periciais com sequência lógica, legenda técnica, metadados, vínculo a quesitos, limitações e preservação de originais.",
        "primary": ["cpc_pericia", "ibape_cartilha", "visual_evidence", "abnt_27037", "pop_mjsp"],
        "secondary": ["abnt_13752", "cnj_linguagem", "ibape_etica", "confea_345"],
        "rules": [
            "Ordenar fotos por sequência: visão geral do local, visão geral do equipamento, identificação, componentes, danos, medições, instrumentos e detalhes.",
            "Cada foto deve ter número, arquivo, data/hora, local, descrição técnica, finalidade, quesito relacionado e limitação quando houver.",
            "A legenda deve descrever o que a imagem mostra, não antecipar culpa, ilegalidade ou causa sem análise.",
            "Preservar originais e usar cópias para redimensionamento ou montagem do anexo.",
            "Indicar quando a foto é fraca, inconclusiva, sem escala, sem contexto, recortada, enviada por terceiro ou sem arquivo nativo.",
            "Vincular fotos ao inventário de evidências."
        ],
        "checklists": [
            ("Qualidade da foto", ["Objeto identificável", "Sequência geral antes do detalhe", "Nitidez suficiente", "Iluminação adequada", "Escala quando dimensão importa", "Arquivo original preservado", "Pertinência ao quesito"]),
            ("Legenda", ["Número sequencial", "Nome do arquivo", "Data/hora", "Local", "Descrição técnica neutra", "Finalidade", "Quesito(s)", "Limitação quando existir"]),
            ("Fechamento do anexo", ["Fotos duplicadas removidas", "Ordem lógica conferida", "Referências no laudo batem com IDs", "Imagens sensíveis tratadas conforme orientação do juízo", "Originais preservados fora do documento final"])
        ],
        "tables": [
            ("Matriz de legenda", ["Campo", "Obrigatório", "Exemplo"], [
                ["Foto", "Sim", "Foto 07 - Placa de identificação"],
                ["Arquivo", "Sim", "EV-007_placa.jpg"],
                ["Local/Data", "Sim", "Casa de máquinas, 16/05/2026"],
                ["Descrição técnica", "Sim", "Registro dos dados de fabricante, potência e série"],
                ["Finalidade", "Sim", "Confirmar identificação do equipamento"],
                ["Limitação", "Quando houver", "Reflexo parcial na área inferior"]
            ]),
            ("Foto válida x fraca", ["Critério", "Foto válida", "Foto fraca"], [
                ["Identificação", "TAG, placa ou contexto visível", "Não permite reconhecer o equipamento"],
                ["Sequência", "Panorama + detalhe", "Detalhe isolado"],
                ["Escala", "Régua/instrumento quando necessário", "Sem referência dimensional"],
                ["Integridade", "Original preservado", "Screenshot ou imagem editada"],
                ["Neutralidade", "Legenda objetiva", "Anotação induzindo culpa"]
            ])
        ],
        "models": [
            ("ANEXO_FOTOGRAFICO.md", """
# Anexo Fotográfico

As fotografias estão organizadas em sequência lógica e vinculadas ao inventário de evidências.

## Foto 01 - [objeto fotografado]
**Arquivo:** EV-001.jpg
**Data/hora:** [data]
**Local:** [local]
**Descrição técnica:** [descrição objetiva do que aparece]
**Finalidade:** [por que a imagem foi registrada]
**Quesito(s):** [Q...]
**Limitação:** [se houver]

---

## Foto 02 - [objeto fotografado]
**Arquivo:** EV-002.jpg
**Data/hora:** [data]
**Local:** [local]
**Descrição técnica:** [descrição objetiva]
**Finalidade:** [finalidade]
**Quesito(s):** [Q...]
""")
        ],
        "phrases": [
            "Foto ___ - Vista geral do equipamento, registrada para contextualização do conjunto.",
            "Foto ___ - Detalhe da placa de identificação, com fabricante, modelo e número de série visíveis.",
            "Foto ___ - Registro da medição de ___, com instrumento e leitura aparentes.",
            "A imagem documenta a condição visual observada, sem permitir, isoladamente, definição de causa.",
            "A fotografia apresenta limitação de nitidez/escala/contexto, sendo utilizada apenas como elemento auxiliar."
        ],
        "risks": [
            "Legenda conclusiva demais, convertendo imagem em prova causal isolada.",
            "Foto recortada sem preservar original.",
            "Anexo sem vínculo com IDs do inventário.",
            "Detalhes técnicos sem foto geral de contexto.",
            "Imagem sem data, local, autoria ou origem."
        ],
        "limitations": [
            "Fotografia é elemento visual de apoio e pode não bastar para concluir causa, extensão ou cronologia.",
            "Anexo fotográfico não substitui inventário de evidências nem relatório técnico.",
            "Arquivos recebidos de terceiros precisam de indicação clara de origem e ressalva de integridade."
        ],
        "donts": [
            "Não inserir setas, filtros, cortes ou marcações sobre o original sem manter arquivo intacto.",
            "Não escrever legenda que atribua culpa ou ilegalidade.",
            "Não ocultar fotos fracas usadas como apoio; declarar a limitação."
        ]
    },
    {
        "folder": "pericia-08-laudo-mecanico",
        "name": "gerador-laudo-pericial-mecanico",
        "title": "Gerador de Laudo Pericial Mecânico",
        "description": "Gerar laudos periciais judiciais de engenharia mecânica com objeto, método, análise técnica, evidências, respostas a quesitos, conclusão, anexos e limitações.",
        "primary": ["cpc_pericia", "lei_5194", "lei_6496", "confea_218", "confea_345", "confea_1137", "ibape_cartilha", "nr12", "manual_nr12", "gum_vim_inmetro"],
        "secondary": ["abnt_13752", "abnt_14653", "abnt_seg_maquinas", "abnt_metrologia", "ibape_norma", "lit_mecanica", "cnj_linguagem", "manual_redacao"],
        "rules": [
            "Cumprir o mínimo do CPC: objeto, análise técnica/científica, método utilizado e resposta conclusiva a todos os quesitos.",
            "Identificar processo, juízo, partes, perito, título, CREA, ART, ato de nomeação e objeto.",
            "Separar fatos observados, documentos examinados, métodos, inferências técnicas, limitações e conclusões.",
            "Vincular cada conclusão a evidência, medição, norma, literatura, documento ou limitação expressa.",
            "Responder quesitos individualmente, com fundamento e referência a seções, anexos ou evidências.",
            "Não decidir culpa, dolo, ilegalidade, inadimplemento contratual ou responsabilidade jurídica.",
            "Registrar limitações de acesso, ausência de documentos, impossibilidade de ensaio, estado alterado do equipamento e incertezas."
        ],
        "checklists": [
            ("Conformidade formal", ["Objeto da perícia exposto", "Metodologia descrita", "Análise técnica desenvolvida", "Todos os quesitos respondidos", "Identificação profissional e ART", "Referências e anexos listados", "Linguagem simples e impessoal"]),
            ("Anti-impugnação", ["Sem quesito omitido", "Sem salto lógico entre evidência e conclusão", "Sem juízo jurídico", "Limitações declaradas", "Fotos e medições rastreáveis", "Normas pagas citadas sem reprodução indevida", "Conclusão não traz fato novo"]),
            ("Engenharia mecânica", ["Equipamento identificado por placa/TAG/série", "Condições operacionais descritas", "Histórico de manutenção analisado", "Medições e calibração tratadas", "NR-12 avaliada quando aplicável", "Nexo técnico fundamentado"])
        ],
        "tables": [
            ("Estrutura recomendada do laudo", ["Seção", "Conteúdo mínimo", "Fonte principal"], [
                ["Identificação", "Processo, vara, partes, perito, CREA, ART", "CPC + Confea"],
                ["Objeto", "Delimitação do exame", "CPC art. 473"],
                ["Documentos e diligências", "Autos, vistoria, presentes, evidências", "CPC + IBAPE"],
                ["Metodologia", "Métodos, normas, literatura, medições", "CPC + técnica"],
                ["Análise técnica", "Dados, raciocínio, limitações", "Engenharia mecânica"],
                ["Quesitos", "Resposta individual fundamentada", "CPC art. 473"],
                ["Conclusão", "Síntese técnica sem juízo jurídico", "CPC + boas práticas"],
                ["Anexos", "Fotos, medições, planilhas, documentos", "CPC + inventário"]
            ]),
            ("Rastreabilidade conclusão-evidência", ["Conclusão", "Evidência", "Método", "Fonte", "Limitação"], [
                ["[C1]", "EV-___ / DOC-___ / MED-___", "[método]", "[fonte]", "[limitação]"]
            ])
        ],
        "models": [
            ("LAUDO_PERICIAL_MECANICO.md", """
# Laudo Pericial de Engenharia Mecânica

## 1. Identificação
Processo:
Vara/Comarca:
Partes:
Perito:
CREA:
ART:

## 2. Objeto da perícia
[descrever objeto e limites]

## 3. Documentos, diligências e evidências
[listar autos, documentos, diligência, inventário e anexos]

## 4. Metodologia
[descrever métodos, normas, medições, literatura e critérios]

## 5. Análise técnica
[separar fatos observados, inferências técnicas e limitações]

## 6. Respostas aos quesitos
### Quesito 1
**Resposta:** [objetiva e fundamentada]

## 7. Conclusão técnica
[síntese das respostas, sem introduzir fatos novos]

## 8. Limitações
[restrições e impacto técnico]

## 9. Referências e anexos
[normas, literatura, anexos e inventário]
"""),
            ("MODELO_RESPOSTA_QUESITO.md", """
**Quesito [ID]:** [transcrever]

**Resposta:** Após análise de [documentos/evidências/método], verificou-se que [achado técnico]. Essa conclusão decorre de [medição/foto/norma/literatura], conforme [seção/anexo]. Ressalva-se que [limitação], quando aplicável.
""")
        ],
        "phrases": [
            "Verificou-se que...",
            "Constatou-se a presença/ausência de...",
            "Os registros examinados indicam...",
            "Não foram identificados indícios técnicos suficientes de...",
            "A conclusão técnica restringe-se ao escopo pericial delimitado.",
            "A limitação indicada não permite afirmar, com base técnica suficiente, que...",
            "Conforme a medição MED-___ e a evidência EV-___..."
        ],
        "risks": [
            "Laudo sem método explícito.",
            "Quesito omitido ou resposta genérica.",
            "Conclusão jurídica disfarçada de conclusão técnica.",
            "Ausência de ART, CREA, assinatura ou identificação profissional.",
            "Citar norma paga reproduzindo conteúdo protegido.",
            "Medição sem rastreabilidade ou incerteza quando crítica."
        ],
        "limitations": [
            "O laudo não substitui sentença nem define responsabilidade jurídica.",
            "Conclusões dependem das evidências disponíveis e das limitações registradas.",
            "Quando o objeto envolver outra especialidade, a conclusão deve ser limitada ou demandar equipe."
        ],
        "donts": [
            "Não usar expressões absolutas como 'sem sombra de dúvida' quando houver incerteza técnica.",
            "Não introduzir conclusão nova apenas na conclusão final.",
            "Não copiar trechos integrais de normas ABNT ou livros comerciais."
        ]
    },
    {
        "folder": "pericia-09-revisao-impugnacao",
        "name": "revisor-laudo-impugnacao",
        "title": "Revisor de Laudo e Impugnação",
        "description": "Revisar laudos, impugnações e pedidos de esclarecimento, auditando omissões, método, quesitos, evidências, linguagem, competência e riscos.",
        "primary": ["cpc_pericia", "confea_345", "confea_1137", "confea_etica", "ibape_cartilha", "cnj_linguagem"],
        "secondary": ["stj_jurisprudencia", "abnt_13752", "nr12", "manual_nr12", "abnt_metrologia", "gum_vim_inmetro", "lit_mecanica", "manual_redacao"],
        "rules": [
            "Revisar primeiro aderência formal ao CPC: objeto, análise, método e respostas a todos os quesitos.",
            "Separar crítica formal, crítica metodológica, crítica de evidência, crítica de linguagem e crítica de competência profissional.",
            "Para impugnações, montar matriz ponto-a-ponto: alegação da parte, trecho do laudo, resposta técnica, necessidade de esclarecimento ou correção.",
            "Sinalizar quando a crítica exige esclarecimento pontual, complementação de anexo, nova diligência, retificação material ou segunda perícia.",
            "Manter tom técnico e não defensivo; responder com referência a páginas, anexos e evidências.",
            "Não inovar além do escopo do laudo salvo quando houver erro ou fato superveniente relevante."
        ],
        "checklists": [
            ("Revisão formal", ["Objeto claro", "Método explícito", "Quesitos completos", "Conclusão coerente", "Identificação/ART/CREA", "Anexos citados e presentes", "Linguagem impessoal"]),
            ("Revisão técnica", ["Evidência suficiente", "Medições rastreáveis", "Norma/fonte adequada", "Limitações declaradas", "Sem salto lógico", "Sem extrapolação de competência", "Sem contradição interna"]),
            ("Resposta à impugnação", ["Cada ponto da parte foi listado", "Resposta vinculada a trecho do laudo", "Correções materiais reconhecidas", "Pedidos de nova prova avaliados", "Tom neutro conferido"])
        ],
        "tables": [
            ("Matriz de impugnação", ["ID", "Ponto impugnado", "Tipo", "Trecho do laudo", "Resposta técnica", "Providência"], [
                ["IMP-01", "[alegação]", "omissão/método/evidência/linguagem", "p. __ / anexo __", "[resposta]", "esclarecer/retificar/manter/complementar"]
            ]),
            ("Grau de severidade", ["Nível", "Descrição", "Ação"], [
                ["Crítico", "Omissão de quesito, ausência de método ou extrapolação grave", "Corrigir/complementar antes de protocolo ou pedir esclarecimento"],
                ["Médio", "Rastreabilidade incompleta, linguagem ambígua ou anexo mal referenciado", "Ajustar ou esclarecer"],
                ["Baixo", "Aprimoramento de redação ou indexação", "Corrigir se houver oportunidade"]
            ])
        ],
        "models": [
            ("RELATORIO_REVISAO_LAUDO.md", """
# Relatório de Revisão Técnica do Laudo

## Escopo da revisão
[laudo / impugnação / esclarecimentos]

## Achados críticos
| ID | Achado | Base | Risco | Providência |
|---|---|---|---|---|

## Quesitos e respostas
[controle de completude]

## Evidências e anexos
[rastreabilidade e lacunas]

## Linguagem e limites
[juízo técnico x jurídico]

## Conclusão da revisão
[apto / apto com ajustes / exige complementação / risco elevado]
"""),
            ("MANIFESTACAO_ESCLARECIMENTOS.md", """
Excelentíssimo Senhor Doutor Juiz de Direito da ___ Vara ___

Processo nº:
Perito:

Em atendimento à intimação, o perito apresenta esclarecimentos aos pontos suscitados:

## Ponto 1
**Questionamento:** [transcrever]
**Esclarecimento técnico:** [responder com referência ao laudo, anexo ou evidência]

## Ponto 2
...

Nestes termos, pede deferimento.
""")
        ],
        "phrases": [
            "O ponto suscitado já se encontra tratado na seção ___ do laudo, especialmente no trecho...",
            "A crítica procede parcialmente quanto à forma de exposição, mas não altera a conclusão técnica pelos seguintes motivos...",
            "Reconhece-se erro material de referência, sem impacto no raciocínio técnico.",
            "A solicitação extrapola o escopo pericial originalmente delimitado.",
            "O esclarecimento limita-se a tornar explícito o método já aplicado, sem inovação probatória."
        ],
        "risks": [
            "Responder impugnação em tom defensivo ou pessoal.",
            "Ignorar ponto efetivamente omisso.",
            "Retificar conclusão sem explicar fundamento técnico.",
            "Adicionar nova prova sem controle do contraditório.",
            "Desqualificar assistente técnico em vez de responder ao argumento técnico."
        ],
        "limitations": [
            "A revisão não transforma laudo deficiente em robusto sem evidência ou método adicional.",
            "Nem toda crítica da parte é impugnação técnica; algumas são teses jurídicas.",
            "A decisão sobre segunda perícia ou substituição cabe ao juízo."
        ],
        "donts": [
            "Não responder com ironia, irritação ou linguagem adversarial.",
            "Não ocultar falha real do laudo.",
            "Não inovar o objeto da perícia em esclarecimentos sem autorização."
        ]
    },
    {
        "folder": "pericia-10-peticoes",
        "name": "peticoes-perito",
        "title": "Petições do Perito",
        "description": "Gerar petições e manifestações do perito judicial: aceite, escusa, honorários, diligência, documentos, prorrogação, juntada, esclarecimentos e pagamento.",
        "primary": ["cpc_pericia", "cnj_233", "cnj_232", "tjce_07_2024", "tjce_manual_pje", "tjce_portarias", "lei_6496", "confea_1137"],
        "secondary": ["stj_jurisprudencia", "manual_redacao", "cnj_linguagem", "ibape_cartilha", "crea_operacional"],
        "rules": [
            "Identificar tipo de petição, gatilho processual, prazo, pedido objetivo e documentos anexos.",
            "Usar fundamentação enxuta: CPC para atos processuais, CNJ/TJCE para cadastro e pagamento, Confea/Crea para ART e responsabilidade técnica.",
            "Manter linguagem impessoal, objetiva e respeitosa, sem discutir mérito jurídico da causa.",
            "Em pedidos de documento, relacionar item pedido ao quesito, método ou limitação técnica.",
            "Em prorrogação, pedir antes do vencimento, com motivo concreto e cronograma.",
            "Em esclarecimentos, responder ponto a ponto, com referência ao laudo e anexos."
        ],
        "checklists": [
            ("Antes de protocolar", ["Processo e vara corretos", "Tipo de petição correto", "Prazo conferido", "Pedido claro no final", "Anexos listados", "Fundamento limitado ao necessário", "Sem tese jurídica de parte"]),
            ("Petições mínimas", ["Aceite do encargo", "Escusa/impedimento/suspeição", "Proposta de honorários", "Comunicação de diligência", "Pedido de documentos", "Pedido de prorrogação", "Juntada de laudo", "Esclarecimentos", "Pagamento/regularização"]),
            ("TJCE/PJe", ["Perfil PJe confirmado", "SIPER/PAJ conferido quando aplicável", "Tabela de honorários verificada", "Fluxo excepcional SEI conferido quando houver falha sistêmica"])
        ],
        "tables": [
            ("Tipos de petição", ["Peça", "Gatilho", "Base", "Anexos comuns"], [
                ["Aceite", "Nomeação/intimação", "CPC + cadastro", "currículo, contatos, ART se cabível"],
                ["Escusa/impedimento", "Conflito ou motivo legítimo", "CPC/CNJ", "documentos comprobatórios"],
                ["Honorários", "Nomeação", "CPC + CNJ/TJCE", "planilha, currículo"],
                ["Diligência", "Necessidade de vistoria", "CPC", "roteiro e documentos necessários"],
                ["Prorrogação", "Prazo insuficiente", "CPC", "cronograma/justificativa"],
                ["Esclarecimentos", "Intimação pós-laudo", "CPC", "matriz de pontos"]
            ])
        ],
        "models": [
            ("PETICAO_ACEITE.md", """
Excelentíssimo Senhor Doutor Juiz de Direito da ___ Vara ___

Processo nº:

[Nome], engenheiro mecânico, CREA ___, perito nomeado nos autos, vem informar que aceita o encargo, ressalvada a confirmação das condições de acesso aos autos, delimitação do objeto, prazo fixado e providências operacionais necessárias à realização dos trabalhos.

Informa dados de contato:

Nestes termos, pede deferimento.
"""),
            ("PETICAO_PEDIDO_DOCUMENTOS.md", """
Excelentíssimo Senhor Doutor Juiz de Direito da ___ Vara ___

Processo nº:

O perito nomeado vem requerer a intimação das partes para apresentação dos documentos abaixo, necessários à análise técnica e à resposta aos quesitos:

1. [documento] - finalidade técnica:
2. [documento] - finalidade técnica:

Os documentos solicitados guardam relação com o objeto pericial e poderão reduzir limitações, evitar diligências complementares e permitir resposta técnica mais precisa.

Nestes termos, pede deferimento.
"""),
            ("PETICAO_PRORROGACAO.md", """
Excelentíssimo Senhor Doutor Juiz de Direito da ___ Vara ___

Processo nº:

O perito vem requerer prorrogação do prazo para entrega do laudo por [número] dias, em razão de [motivo técnico concreto: volume documental, diligência pendente, documento não apresentado, ensaio, necessidade de nova vistoria].

Cronograma proposto:
- [marco 1]
- [marco 2]

Nestes termos, pede deferimento.
""")
        ],
        "phrases": [
            "O pedido ora formulado tem finalidade estritamente técnica e visa permitir resposta adequada aos quesitos.",
            "A documentação requerida guarda relação direta com o objeto pericial.",
            "A prorrogação é requerida antes do vencimento do prazo, em razão de circunstância técnica superveniente.",
            "A manifestação limita-se aos pontos técnicos suscitados, sem incursão no mérito jurídico da demanda.",
            "Requer-se a intimação das partes para ciência da data e local da diligência."
        ],
        "risks": [
            "Pedir providência sem relação técnica com quesito ou método.",
            "Protocolar prorrogação depois do prazo.",
            "Discutir culpa, direito ou mérito da parte.",
            "Usar fundamento local do TJCE em processo de outro tribunal sem adaptação.",
            "Anexar documentos sensíveis ou incompletos sem identificação."
        ],
        "limitations": [
            "A skill redige manifestações do perito, não petições advocatícias de parte.",
            "Fluxos de pagamento, sistema e anexos variam por tribunal e devem ser conferidos no portal oficial.",
            "A decisão sobre deferimento de documentos, prazos, honorários e diligências cabe ao juízo."
        ],
        "donts": [
            "Não assumir posição de autor, réu ou assistente técnico.",
            "Não usar tom litigante ou acusatório.",
            "Não citar jurisprudência sem necessidade e sem conexão direta com o pedido."
        ]
    },
    {
        "folder": "pericia-11-controle-prazos",
        "name": "controle-prazos-pericia",
        "title": "Controle de Prazos da Perícia",
        "description": "Controlar marcos, prazos e alertas de perícia judicial: nomeação, quesitos, honorários, diligência, laudo, esclarecimentos, audiência, cadastro e pagamento.",
        "primary": ["cpc_pericia", "cnj_233", "tjce_07_2024", "tjce_manual_pje", "tjce_portarias"],
        "secondary": ["manual_redacao", "cnj_linguagem", "crea_operacional", "confea_1137"],
        "rules": [
            "Registrar data da intimação oficial, tipo de ato, prazo judicial fixado, audiência marcada e sistema de origem.",
            "Criar alertas para 15 dias das partes para quesitos/assistentes/impugnação, 5 dias para manifestação sobre honorários, prazo do laudo, 20 dias antes de audiência, 15 dias para esclarecimentos e 10 dias de antecedência de audiência quando aplicável.",
            "No TJCE, controlar prazo de cadastramento excepcional de nomeado não credenciado em justiça gratuita e prazos operacionais de pagamento/documentação.",
            "Marcar emissão de ART antes ou no início da atividade técnica e baixa/regularização ao final, quando cabível.",
            "Não fechar contagem oficial sem conferir PJe, calendário forense, feriados locais, suspensão de expediente e despacho específico.",
            "Gerar alertas progressivos: crítico, atenção, planejado e concluído."
        ],
        "checklists": [
            ("Cadastro do caso", ["Data de intimação oficial", "Prazo do laudo", "Audiência existente", "Prazo para honorários", "Data prevista de diligência", "Regime de custeio", "Tribunal/comarca"]),
            ("Alertas mínimos", ["Honorários", "Manifestação das partes", "Diligência", "Documentos pendentes", "Laudo", "Esclarecimentos", "Audiência", "Cadastro/pagamento local", "ART"]),
            ("Revisão semanal", ["PJe consultado", "Despachos novos verificados", "Prazos recalculados", "Pendências comunicadas", "Riscos de atraso tratados"])
        ],
        "tables": [
            ("Matriz de prazos", ["Marco", "Base", "Prazo de referência", "Gatilho", "Alerta"], [
                ["Quesitos/assistentes/impugnação do perito", "CPC art. 465", "15 dias", "Nomeação/intimação", "D-10/D-5/D-1"],
                ["Manifestação sobre honorários", "CPC art. 465", "5 dias", "Proposta juntada", "D-3/D-1"],
                ["Entrega do laudo", "Despacho judicial", "Prazo fixado", "Nomeação/depósito/diligência", "D-15/D-7/D-3/D-1"],
                ["Laudo antes de audiência", "CPC art. 477", "mínimo 20 dias antes", "Audiência designada", "D-30/D-25"],
                ["Esclarecimentos", "CPC art. 477", "15 dias", "Intimação", "D-10/D-5/D-1"],
                ["Audiência com perito", "CPC art. 477", "intimação mínima de 10 dias", "Designação", "D-15/D-10"]
            ]),
            ("Status do prazo", ["Status", "Critério", "Ação"], [
                ["Planejado", "Prazo registrado e sem pendência", "Monitorar"],
                ["Atenção", "Menos de 7 dias ou pendência crítica", "Executar ou pedir providência"],
                ["Crítico", "Menos de 48h ou bloqueio externo", "Comunicar/pedir prorrogação"],
                ["Concluído", "Protocolo/ato realizado", "Arquivar comprovante"]
            ])
        ],
        "models": [
            ("CONTROLE_PRAZOS.csv", """
processo,marco,base,data_gatilho,prazo_referencia,data_limite_estimada,status,responsavel,observacoes,verificado_no_pje_em
0000000-00.0000.0.00.0000,entrega_laudo,despacho judicial,YYYY-MM-DD,prazo fixado,YYYY-MM-DD,planejado,perito,,YYYY-MM-DD
"""),
            ("RESUMO_PRAZOS.md", """
# Resumo de Prazos da Perícia

Processo:
Última verificação no PJe:

| Marco | Data limite estimada | Status | Próxima ação |
|---|---|---|---|

## Alertas críticos
- [listar]

## Observações
As datas são controle operacional interno e devem ser conferidas no PJe e no calendário forense antes de qualquer protocolo.
""")
        ],
        "phrases": [
            "Prazo estimado para controle interno, sujeito à conferência no PJe e no calendário forense.",
            "Há risco de atraso por pendência documental externa, recomendando-se comunicação ao juízo antes do vencimento.",
            "O marco foi concluído em [data], conforme comprovante de protocolo arquivado.",
            "A data de audiência exige verificar se o laudo precisa ser juntado com antecedência mínima.",
            "A contagem oficial deve observar o ato de intimação, feriados locais e eventual suspensão de expediente."
        ],
        "risks": [
            "Confundir data de publicação, ciência e intimação.",
            "Contar dias corridos quando o processo exigir dias úteis, ou o inverso.",
            "Ignorar feriado local ou suspensão de expediente.",
            "Não pedir prorrogação antes do vencimento.",
            "Perder prazo de esclarecimentos após impugnação."
        ],
        "limitations": [
            "A skill não certifica contagem processual oficial.",
            "Prazos dependem do despacho específico e do sistema do tribunal.",
            "Feriados locais, indisponibilidades e regras de expediente precisam ser verificados manualmente."
        ],
        "donts": [
            "Não tratar a planilha interna como substituta do PJe.",
            "Não assumir prazo sem data de gatilho confirmada.",
            "Não apagar histórico de alterações de prazo."
        ]
    },
    {
        "folder": "pericia-12-biblioteca-normas",
        "name": "biblioteca-normas-metodos",
        "title": "Biblioteca de Normas e Métodos",
        "description": "Manter catálogo de fontes legais, normativas, técnicas e consultivas para perícias mecânicas, com classificação, vigência, licença e uso seguro.",
        "primary": ["cpc_pericia", "cnj_233", "cnj_232", "tjce_07_2024", "tjce_14_2022", "tjce_portarias", "lei_5194", "lei_6496", "confea_218", "confea_345", "confea_1073", "confea_1137", "confea_etica", "nr12"],
        "secondary": ["manual_nr12", "abnt_13752", "abnt_14653", "abnt_seg_maquinas", "abnt_metrologia", "gum_vim_inmetro", "abnt_27037", "ibape_cartilha", "ibape_norma", "ibape_honorarios", "cnj_linguagem", "manual_redacao", "lit_mecanica", "stj_jurisprudencia", "visual_evidence"],
        "rules": [
            "Classificar toda fonte por natureza: norma obrigatória, norma local, fonte profissional, referência técnica, boa prática, jurisprudência, manual operacional ou literatura consultiva.",
            "Marcar fontes sujeitas a verificação periódica de vigência, edição, revogação, tabela, portaria ou atualização de sistema.",
            "Separar material que pode ser salvo integralmente de material pago/protegido que deve ficar apenas como ficha bibliográfica e notas próprias.",
            "Registrar fonte oficial de obtenção, edição, data de consulta, aplicação nas skills e restrições de uso.",
            "Não guardar cópia integral de ABNT, livros, handbooks ou standards sem licença válida.",
            "Manter histórico de fontes revogadas, mas impedir uso como base principal sem aviso explícito."
        ],
        "checklists": [
            ("Entrada de nova fonte", ["Fonte oficial localizada", "Natureza classificada", "Edição/versão registrada", "Data de consulta anotada", "Licença/copyright avaliado", "Skills impactadas mapeadas", "Necessidade de verificação periódica marcada"]),
            ("Revisão periódica", ["CPC/CNJ conferidos", "TJCE portarias e tabelas conferidas", "Confea/Crea conferidos", "NR-12 conferida", "ABNT edição/catálogo conferidos", "IBAPE edição/status conferidos", "Jurisprudência relevante atualizada"]),
            ("Uso seguro", ["Obrigatória x consultiva diferenciado", "Norma paga não copiada", "Fonte revogada sinalizada", "Fonte local não generalizada", "Opinião/literatura não tratada como lei"])
        ],
        "tables": [
            ("Catálogo mestre de fontes", ["ID", "Fonte", "Natureza", "Uso", "Pode salvar íntegra?", "Verificação"], [
                ["LEG-001", "CPC", "Lei", "Processual", "Sim, fonte oficial pública", "Periódica"],
                ["CNJ-001", "Res. CNJ 233/2016", "Resolução", "Cadastro/deveres", "Sim, oficial", "Periódica"],
                ["TJCE-001", "Portarias de honorários", "Norma local", "Tabela/pagamento", "Sim, oficial", "Alta frequência"],
                ["ABNT-001", "NBR 13752", "Norma paga", "Método por analogia", "Não sem licença", "Edição vigente"],
                ["TEC-001", "ASM/SKF/Bloch/Mobley", "Literatura técnica", "Falhas mecânicas", "Não sem licença", "Edição"],
                ["INST-001", "IBAPE cartilha/norma", "Consultiva institucional", "Método/redação", "Se pública/oficial", "Edição/status"]
            ]),
            ("Hierarquia de uso", ["Nível", "Fontes", "Como usar"], [
                ["1", "Leis, CPC, CNJ, Confea, tribunal", "Base obrigatória quando aplicável"],
                ["2", "NR-12 e atos regulatórios técnicos", "Obrigatória em segurança de máquinas"],
                ["3", "ABNT/ISO, Inmetro, GUM/VIM", "Referência técnica, respeitando licença"],
                ["4", "IBAPE, manuais, cartilhas", "Boa prática e método consultivo"],
                ["5", "Literatura, fabricantes, jurisprudência", "Apoio técnico ou argumentativo, não substitutivo"]
            ])
        ],
        "models": [
            ("FICHA_FONTE.md", """
# Ficha de Fonte

## Identificação
Fonte:
Instituição/editora:
Tipo:
Edição/versão:
Data de consulta:
Link oficial ou forma de aquisição:

## Natureza
[obrigatória / consultiva / técnica paga / boa prática / jurisprudência / literatura]

## Aplicação
Skills impactadas:
Uso permitido:
Uso proibido:

## Regras extraídas
- [regra 1]
- [regra 2]

## Licença e armazenamento
[pode salvar integralmente / apenas ficha e notas / verificar licença]

## Verificação periódica
Periodicidade:
Responsável:
Última verificação:
""")
        ],
        "phrases": [
            "Fonte obrigatória quando aplicável ao caso concreto.",
            "Fonte consultiva utilizada como boa prática metodológica, sem força de obrigação legal autônoma.",
            "Norma técnica paga: manter apenas ficha, escopo, metadados e notas próprias, salvo licença válida.",
            "Fonte local sujeita a atualização; verificar portal oficial antes do uso.",
            "Fonte histórica ou revogada: manter apenas para contexto, nunca como fundamento principal vigente."
        ],
        "risks": [
            "Usar norma revogada ou tabela vencida.",
            "Guardar cópia integral de norma paga sem licença.",
            "Citar blog, resumo de catálogo ou repositório não oficial como fonte principal.",
            "Aplicar ato do TJCE a processo de outro tribunal sem adaptação.",
            "Tratar manual consultivo como lei."
        ],
        "limitations": [
            "A biblioteca não substitui aquisição legal de normas pagas.",
            "O catálogo não garante vigência se não houver rotina de revisão.",
            "Fontes locais refletem o tribunal pesquisado e podem não valer em outras jurisdições."
        ],
        "donts": [
            "Não armazenar PDFs pirateados ou cópias integrais de material protegido.",
            "Não apagar fonte revogada sem preservar aviso de substituição e risco.",
            "Não usar fonte secundária quando houver fonte oficial acessível."
        ]
    }
]


def write_skill(skill):
    skill_dir = ROOT / "skills" / skill["folder"]
    ref_dir = skill_dir / "references"
    ref_dir.mkdir(parents=True, exist_ok=True)

    skill_md = f"""---
name: {skill["name"]}
description: {skill["description"]} Use esta skill quando for necessário atuar no fluxo de perícia judicial de engenharia mecânica correspondente a "{skill["title"]}".
---

# {skill["title"]}

Use esta skill para {skill["description"].lower()}

## Fluxo Essencial

1. Identificar o processo, o objeto técnico, o tribunal e o estágio da perícia.
2. Ler apenas as referências necessárias em `references/`, começando por fontes principais e regras operacionais.
3. Separar norma obrigatória, norma local, boa prática, referência técnica e literatura consultiva.
4. Marcar qualquer fonte com `[VP]` para verificação de vigência, edição ou tabela antes de uso externo.
5. Produzir a saída usando os modelos da pasta `references/06_modelos-saida.md`.

## Referências Internas

- `references/01_fontes-principais.md`
- `references/02_fontes-secundarias.md`
- `references/03_regras-operacionais.md`
- `references/04_checklists.md`
- `references/05_tabelas.md`
- `references/06_modelos-saida.md`
- `references/07_frases-padrao.md`
- `references/08_alertas-risco.md`
- `references/09_limitacoes.md`
- `references/10_nao-fazer.md`
"""
    (skill_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")

    (ref_dir / "01_fontes-principais.md").write_text(
        f"# Fontes Principais - {skill['title']}\n\n"
        "Legenda: `[VP]` indica fonte que deve ser verificada periodicamente quanto a vigência, edição, revogação, portaria, tabela ou atualização operacional.\n\n"
        + source_table(skill["primary"]) + "\n",
        encoding="utf-8"
    )
    (ref_dir / "02_fontes-secundarias.md").write_text(
        f"# Fontes Secundárias - {skill['title']}\n\n"
        "Estas fontes apoiam método, linguagem, literatura técnica e boas práticas. Não substituem lei, resolução, norma local obrigatória ou fonte técnica licenciada quando aplicável.\n\n"
        + source_table(skill["secondary"]) + "\n",
        encoding="utf-8"
    )
    (ref_dir / "03_regras-operacionais.md").write_text(
        f"# Regras Operacionais - {skill['title']}\n\n" + bullets(skill["rules"]),
        encoding="utf-8"
    )
    (ref_dir / "04_checklists.md").write_text(
        f"# Checklists - {skill['title']}\n\n" + checklist_block(skill["checklists"]),
        encoding="utf-8"
    )
    (ref_dir / "05_tabelas.md").write_text(
        f"# Tabelas - {skill['title']}\n\n" + tables_block(skill["tables"]),
        encoding="utf-8"
    )
    (ref_dir / "06_modelos-saida.md").write_text(
        f"# Modelos de Saída - {skill['title']}\n\n" + model_block(skill["models"]),
        encoding="utf-8"
    )
    (ref_dir / "07_frases-padrao.md").write_text(
        f"# Frases Padrão - {skill['title']}\n\n" + bullets(skill["phrases"]),
        encoding="utf-8"
    )
    (ref_dir / "08_alertas-risco.md").write_text(
        f"# Alertas de Risco - {skill['title']}\n\n" + bullets(skill["risks"]),
        encoding="utf-8"
    )
    (ref_dir / "09_limitacoes.md").write_text(
        f"# Limitações - {skill['title']}\n\n" + bullets(skill["limitations"] + STANDARD_LIMITATIONS),
        encoding="utf-8"
    )
    (ref_dir / "10_nao-fazer.md").write_text(
        f"# O Que Esta Skill Não Deve Fazer - {skill['title']}\n\n" + bullets(skill["donts"] + STANDARD_DONTS),
        encoding="utf-8"
    )


def write_policy():
    content = """# Política Geral de Fontes

Esta base diferencia expressamente:

- **Norma obrigatória:** lei, resolução, portaria, norma regulamentadora ou ato local aplicável ao caso.
- **Boa prática:** cartilha, manual institucional, guia técnico ou padrão de conduta útil, sem força legal autônoma.
- **Referência técnica:** norma técnica, literatura, manual de fabricante, documento metrológico ou handbook usado para método e causalidade.
- **Fonte consultiva:** jurisprudência, artigo técnico, material institucional ou literatura que reforça o raciocínio, mas não substitui a fonte primária.

Regras permanentes:

- Não copiar integralmente normas pagas, livros comerciais ou standards protegidos por licença.
- Não misturar lei com opinião técnica.
- Não transformar fonte consultiva em obrigação legal.
- Diferenciar norma obrigatória, boa prática e referência técnica em toda saída.
- Marcar fontes que precisam ser verificadas periodicamente com `[VP]`.
"""
    (ROOT / "POLITICA_FONTES.md").write_text(content, encoding="utf-8")


def write_matrix():
    rows = []
    for skill in SKILLS:
        suggested_files = {
            "primary": f"/skills/{skill['folder']}/references/01_fontes-principais.md",
            "secondary": f"/skills/{skill['folder']}/references/02_fontes-secundarias.md",
            "rules": f"/skills/{skill['folder']}/references/03_regras-operacionais.md",
        }
        for source_id in skill["primary"]:
            source = SOURCE_CATALOG[source_id]
            rows.append([
                skill["folder"],
                source["name"] + (" [VP]" if source["periodic"] else ""),
                source["application"],
                source["rule"],
                suggested_files["primary"],
                "Alta" + (" - verificar periodicamente" if source["periodic"] else "")
            ])
        for source_id in skill["secondary"]:
            source = SOURCE_CATALOG[source_id]
            rows.append([
                skill["folder"],
                source["name"] + (" [VP]" if source["periodic"] else ""),
                source["application"],
                source["rule"],
                suggested_files["secondary"],
                "Média" + (" - verificar periodicamente" if source["periodic"] else "")
            ])

    content = "# Matriz Geral de Fontes e Aplicações\n\n"
    content += "Legenda: `[VP]` indica fonte sujeita a verificação periódica de vigência, edição, tabela, portaria, revogação ou atualização operacional.\n\n"
    content += table(["Skill", "Fonte", "Aplicação", "Regra extraída", "Arquivo sugerido", "Prioridade"], rows)
    content += "\n"
    (ROOT / "MATRIZ_GERAL.md").write_text(content, encoding="utf-8")


def write_tree_manifest():
    paths = []
    for path in sorted(ROOT.glob("**/*")):
        if path.is_file():
            paths.append(str(path.relative_to(ROOT)).replace("\\", "/"))
    content = "# Manifesto de Arquivos\n\n" + "\n".join(f"- `{p}`" for p in paths) + "\n"
    (ROOT / "MANIFESTO_ARQUIVOS.md").write_text(content, encoding="utf-8")


def main():
    (ROOT / "skills").mkdir(exist_ok=True)
    for skill in SKILLS:
        write_skill(skill)
    write_policy()
    write_matrix()
    write_tree_manifest()


if __name__ == "__main__":
    main()
