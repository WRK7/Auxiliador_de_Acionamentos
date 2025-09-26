# Configurações do Gerador de Acionamentos
# Edite este arquivo para modificar carteiras, tipos e campos

# Carteiras disponíveis
CARTEIRAS = [
    "SENAC RJ", 
    "SENAC BA ou MS",
    "SESC",
    "FIRJAN",
    "FIEB",
    "UNIMED",
    "CEDAE",
    "ÁGUAS DE JOINVILLE",
    "CASSEMS",
    "ÓTICA DINIZ",
    "LIBERDADE MÉDICA"
]

# Tipos de acionamento disponíveis
TIPOS_ACIONAMENTO = [
    "ACD - ACORDO",
    "ACP - PARCELADO"
]

# Campos de informação padrão - Organizados por categoria
CAMPOS_INFO = {
    # === INFORMAÇÕES BÁSICAS DO DEVEDOR ===
    "Nome do Devedor": "",
    "CPF/CNPJ": "",
    "Titular": "",
    "Empresa": "",
    "Cliente": "",
    "Contratante": "",
    
    # === INFORMAÇÕES DE CONTATO ===
    "Telefone": "",
    "E-mail": "",
    "WhatsApp": "",
    "Email": "",
    
    # === INFORMAÇÕES DE VALORES ===
    "Valor da Dívida": "",
    "Valor Total Atualizado": "",
    "Valor Proposto": "",
    "Valor Confirmado": "",
    "Valor Total Negociado": "",
    "Valor Original": "",
    "Valor Débito Original": "",
    "Valor Debito Original": "",
    "Valor Negociado": "",
    "Valor Total": "",
    "Total da Dívida": "",
    
    # === INFORMAÇÕES DE DESCONTO ===
    "Desconto Principal": "",
    "Desconto Juros": "",
    "Desconto Multa": "",
    
    # === INFORMAÇÕES DE PARCELAMENTO ===
    "Parcelamento": "",
    "Valor das Parcelas": "",
    "Valor de Cada Parcela": "",
    "Valor da Parcela": "",
    "Valor da Parcelas": "",
    "Parcelas": "",
    "Quantidade de Parcelas": "",
    "Qtd de Parcelas": "",
    "Quantidade de Parcelas": "",
    "Nº de Parcelas no Cartão": "",
    
    # === INFORMAÇÕES DE ENTRADA ===
    "Entrada de": "",
    "Valor de Entrada": "",
    "Entrada (Boleto)": "",
    "Entrada Negociação": "",
    
    # === INFORMAÇÕES DE CONTRATOS E TÍTULOS ===
    "Número do Contrato": "",
    "CRE/Contrato": "",
    "Contrato": "",
    "Unidade": "",
    "Matrícula": "",
    "Titular": "",
    "Telefone": "",
    "Valor Débito Original": "",
    "Vencimento das Faturas": "",
    "Vencimento Acordo": "",
    "Títulos": "",
    "Titulo": "",
    "Número e Valores dos Títulos": "",
    "Faturas a Pagar": "",
    "Fatura Vencida": "",
    
    # === INFORMAÇÕES DE MATRÍCULA E UNIDADE ===
    "Matrícula": "",
    "Matrícula Inativa": "",
    "Matrícula para Transferência": "",
    "Unidade": "",
    "Referência": "",
    
    # === INFORMAÇÕES DE VENCIMENTO ===
    "Data de Vencimento": "",
    "Data de Pagamento": "",
    "Vencimento das Faturas": "",
    "Vencimento Acordo": "",
    "Vencimento da Entrada": "",
    "Novo Vencimento": "",
    
    # === INFORMAÇÕES DE PAGAMENTO ===
    "Forma de Pagamento": "",
    "Acordo Realizado": "",
    "Dias em Atraso": "",
    "Horário da Ligação": "",
    "Gravação (Telefone)": "",
    
    # === INFORMAÇÕES ESPECÍFICAS ===
    "Valor Proposto para Parcelamento": "",
    "Religação": "",
    "Ativo - Religação": "",
    "Observações": ""
}

# Configurações de validação
CAMPOS_OBRIGATORIOS = [
    "Nome do Devedor", "CPF/CNPJ", "Data de Vencimento", "Valor da Dívida", 
    "Número do Contrato", "Títulos", "Valor Total Atualizado", "Valor Proposto", "Parcelamento", "WhatsApp", "E-mail", 
    "CRE/Contrato", "Valor Confirmado", "Horário da Ligação", "Contrato", 
    "Entrada de", "Quantidade de Parcelas", "Valor das Parcelas", "Empresa", "Cliente", 
    "Telefone", "E-mail", "Total da Dívida", "Acordo Realizado", 
    "Valor Total Negociado", "Nº de Parcelas no Cartão", 
    "Número e Valores dos Títulos", "Unidade", "Referência", "Valor Original", 
    "Forma de Pagamento", "Contratante", "Faturas a Pagar", "Dias em Atraso", 
    "Data de Pagamento", "Matrícula", "Gravação (Telefone)", 
    "Valor Proposto para Parcelamento", "Entrada (Boleto)", "Qtd de Parcelas", 
    "Valor de Cada Parcela", "Fatura Vencida", "Novo Vencimento", "Email", 
    "Titular", "Valor Débito Original", "Vencimento das Faturas", 
    "Vencimento Acordo", "Valor de Entrada", "Quantidade de Parcelas", 
    "Valor Debito Original", "Valor Negociado", 
    "Matrícula para Transferência", "Religação", "Valor da Parcelas", 
    "Vencimento da Entrada", "Ativo - Religação", "Titulo", "Valor Total", 
    "Valor da Entrada", "Parcelas", "Valor da Parcela",
    "Matrícula Inativa", "Valor da Parcelas"
]

# Configurações de prazo máximo por carteira (em dias)
PRAZO_MAXIMO_POR_CARTEIRA = {
    "SENAC RJ": 7,
    "SENAC BA ou MS": 7,
    "SESC": 7,
    "FIRJAN": 7,
    "FIEB": 7,
    "UNIMED": 7,
    "CEDAE": 7,
    "ÁGUAS DE JOINVILLE": 7,
    "CASSEMS": 7,
    "ÓTICA DINIZ": 7,
    "LIBERDADE MÉDICA": 7
}

# Tipos de acionamento disponíveis por carteira
TIPOS_POR_CARTEIRA = {
    "SENAC RJ": [
        "ACD - ACORDO",
        "ACP - PARCELADO"
    ],
    "SENAC BA ou MS": [
        "ACD - À VISTA",
        "ACD - PARCELADO"
    ],
    "SESC": [
        "ACD - À VISTA",
        "ACD - PARCELADO"
    ],
    "FIRJAN": [
        "ACF - À VISTA",
        "ACF - PARCELADO"
    ],
    "FIEB": [
        "ACD - PIX/DÉBITO/CRÉDITO",
        "ACD - BOLETO"
    ],
    "UNIMED": [
        "ACD - ACORDO"
    ],
    "CEDAE": [
        "ACV - À VISTA",
        "ACP - PARCELADO",
        "VIA - SEGUNDA VIA"
    ],
    "ÁGUAS DE JOINVILLE": [
        "ACV - À VISTA",
        "ACP - PARCELADO"
    ],
    "CASSEMS": [
        "ACC - À VISTA",
        "ACC - PARCELADO"
    ],
    "ÓTICA DINIZ": [
        "ACD - ACORDO"
    ],
    "LIBERDADE MÉDICA": [
        "ACD - ACORDO"
    ]
}

# Configurações de formatação automática
FORMATACAO_AUTOMATICA = {
    "CPF/CNPJ": "cpf_cnpj",
    "Data de Vencimento": "data",
    "Data de Pagamento": "data",
    "Vencimento Acordo": "data",
    "Valor da Dívida": "moeda",
    "Valor Total Atualizado": "moeda",
    "Valor Proposto": "moeda",
    "Valor de Entrada": "moeda",
    "Valor de Cada Parcela": "parcela",
    "Valor das Parcelas": "parcela",
    "Valor da Parcela": "parcela",
    "Valor de Cada Parcela": "parcela",
    "Desconto Principal": "porcentagem",
    "Desconto Juros": "porcentagem",
    "Desconto Multa": "porcentagem",
}

# Campos específicos por tipo de acionamento
CAMPOS_POR_TIPO = {
    "ACD - ACORDO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Títulos",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Data de Vencimento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACP - PARCELADO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Títulos",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Parcelamento",
        "Data de Vencimento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACD - À VISTA": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "CRE/Contrato",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Data de Vencimento",
        "Valor Confirmado",
        "Horário da Ligação",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACD - PARCELADO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "CRE/Contrato",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Parcelamento",
        "Data de Vencimento",
        "Valor Confirmado",
        "Horário da Ligação",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACD - À VISTA": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Contrato",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Data de Vencimento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACD - PARCELADO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Contrato",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Entrada de",
        "Quantidade de Parcelas",
        "Valor das Parcelas",
        "Data de Vencimento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACF - À VISTA": [
        "Empresa (Sesi ou Senai)",
        "Cliente",
        "CPF/CNPJ",
        "Telefone",
        "E-mail",
        "Total da Dívida",
        "Acordo Realizado (100% na multa e % no juros)",
        "Valor Total Negociado",
        "Nº de Parcelas no Cartão de Crédito",
        "Número e Valores dos Títulos Renegociados (Principal)",
        "Data de Vencimento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACF - PARCELADO": [
        "Empresa (Sesi ou Senai)",
        "Cliente",
        "CPF/CNPJ",
        "Telefone",
        "E-mail",
        "Total da Dívida",
        "Acordo Realizado (100% na multa e % no juros)",
        "Valor Total Negociado",
        "Nº de Parcelas no Cartão de Crédito",
        "Número e Valores dos Títulos Renegociados (Principal)",
        "Data de Vencimento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACD - PIX/DÉBITO/CRÉDITO": [
        "Unidade (SENAI, SESI OU IEL)",
        "Nome do Devedor",
        "CPF/CNPJ",
        "Referência (INSERIR O ANO DA DÍVIDA)",
        "Valor Original",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Data de Vencimento",
        "Forma de Pagamento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACD - BOLETO": [
        "Unidade (SENAI, SESI OU IEL)",
        "Nome do Devedor",
        "CPF/CNPJ",
        "Referência (INSERIR O ANO DA DÍVIDA)",
        "Valor Original",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Valor da Entrada",
        "Quantidade de Parcelas",
        "Valor de Cada Parcela",
        "Data de Vencimento",
        "Forma de Pagamento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACD - ACORDO": [
        "Contratante",
        "CPF/CNPJ",
        "Faturas a Pagar",
        "Títulos",
        "Dias em Atraso",
        "Forma de Pagamento",
        "Data de Pagamento",
        "Valor Original",
        "Valor Total Atualizado",
        "Telefone",
        "Forma de Envio"
    ],
    "ACV - À VISTA": [
        "Matrícula",
        "Gravação (Telefone)",
        "Valor Original",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Data de Vencimento",
        "Forma de Pagamento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACP - PARCELADO": [
        "Matrícula",
        "Gravação (Telefone)",
        "Valor Original",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto para Parcelamento",
        "Entrada (Boleto)",
        "Qtd de Parcelas",
        "Valor de Cada Parcela",
        "Data de Vencimento",
        "Forma de Pagamento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "VIA - SEGUNDA VIA": [
        "Nome do Devedor",
        "Matrícula",
        "Fatura Vencida",
        "Valor",
        "Novo Vencimento",
        "Telefone",
        "Email"
    ],
    "ACV - À VISTA": [
        "Unidade",
        "Matrícula",
        "CPF/CNPJ",
        "Titular",
        "Telefone",
        "Valor Débito Original",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Vencimento das Faturas",
        "Vencimento Acordo",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACP - PARCELADO": [
        "Unidade",
        "Matrícula",
        "CPF/CNPJ",
        "Titular",
        "Telefone",
        "Valor Débito Original",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Valor de Entrada",
        "Quantidade de Parcelas",
        "Valor de Cada Parcela",
        "Data de Vencimento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACC - À VISTA": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Titulo",
        "Valor Original",
        "Valor Total",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Data de Vencimento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACC - PARCELADO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Titulo",
        "Valor Original",
        "Valor Total",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Entrada",
        "Parcelas",
        "Valor da Parcela",
        "Data de Vencimento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACP - PARCELADO": [
        "Unidade",
        "Matrícula",
        "CPF/CNPJ",
        "Titular",
        "Telefone",
        "Valor Debito Original",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor da Entrada",
        "Quantidade de Parcelas",
        "Valor de Cada Parcela",
        "Data de Vencimento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ],
    "ACD - ACORDO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Data de Vencimento",
        "Forma de Pagamento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ]
}

# Modelos de texto para cada tipo de acionamento
MODELOS_ACIONAMENTO = {
    "ACD - ACORDO": """
SENAC RJ - Á VISTA (ACD- ACORDO):

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
""",
    
    "ACP - PARCELADO": """
SENAC RJ - PARCELADO (ACD – ACORDO PARCELADO):

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
PARCELAMENTO: {Parcelamento} ENTRADA DE R$(DÉBITO/BOLETO) + X R$ (BOLETO/CRÉDITO)
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
""",
    
    "ACD - À VISTA": """
SENAC MS/BA: Á VISTA (ACD- ACORDO):

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
CRE/CONTRATO: {CRE/Contrato}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
VALOR CONFIRMADO: {Valor Confirmado} SIG/planilha.
HORÁRIO DA LIGAÇÃO: {Horário da Ligação}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
""",
    
    "ACD - PARCELADO": """
SENAC MS/BA: PARCELADO (ACD – ACORDO PARCELADO):

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
CRE/CONTRATO: {CRE/Contrato}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
PARCELAMENTO: {Parcelamento} ENTRADA DE R$(DÉBITO/BOLETO) + X R$ (BOLETO/CRÉDITO)
VENCIMENTO: {Data de Vencimento}
VALOR CONFIRMADO: {Valor Confirmado} SIG/PLANILHA
HORÁRIO DA LIGAÇÃO: {Horário da Ligação}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
""",
    
    "ACD - À VISTA": """
À VISTA (ACD- ACORDO):

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
CONTRATO: {Contrato}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
""",
    
    "ACD - PARCELADO": """
PARCELADO:

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
CONTRATO: {Contrato}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
ENTRADA DE: {Entrada de}
QUANT.P: {Quantidade de Parcelas}
VALOR DAS PARCELAS: {Valor das Parcelas}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
""",
    
    "ACF - À VISTA": """
FIRJAN:
À VISTA e PARCELADO – (ACF – ACORDO FIRJAN)

Empresa (Sesi ou Senai): {Empresa (Sesi ou Senai)}
CLIENTE: {Cliente}
CPF: {CPF/CNPJ}
TELEFONE: {Telefone}
E-MAIL: {E-mail}
TOTAL DA DÍVIDA: {Total da Dívida}
ACORDO REALIZADO: {Acordo Realizado (100% na multa e % no juros)}
VALOR TOTAL NEGOCIADO: {Valor Total Negociado}
Nº DE PARCELAS NO CARTÃO DE CRÉDITO: {Nº de Parcelas no Cartão de Crédito}
NÚMERO E VALORES DOS TÍTULOS RENEGOCIADOS (Principal): {Número e Valores dos Títulos Renegociados (Principal)}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} {E-mail}
OBS: {Observações}
""",
    
    "ACF - PARCELADO": """
FIRJAN:
À VISTA e PARCELADO – (ACF – ACORDO FIRJAN)

Empresa (Sesi ou Senai): {Empresa (Sesi ou Senai)}
CLIENTE: {Cliente}
CPF: {CPF/CNPJ}
TELEFONE: {Telefone}
E-MAIL: {E-mail}
TOTAL DA DÍVIDA: {Total da Dívida}
ACORDO REALIZADO: {Acordo Realizado (100% na multa e % no juros)}
VALOR TOTAL NEGOCIADO: {Valor Total Negociado}
Nº DE PARCELAS NO CARTÃO DE CRÉDITO: {Nº de Parcelas no Cartão de Crédito}
NÚMERO E VALORES DOS TÍTULOS RENEGOCIADOS (Principal): {Número e Valores dos Títulos Renegociados (Principal)}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} {E-mail}
OBS: {Observações}
""",
    
    "ACD - PIX/DÉBITO/CRÉDITO": """
PIX, DÉBITO OU CRÉDITO EM 12X (ACD – ACORDO):

UNIDADE: {Unidade (SENAI, SESI OU IEL)}
NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
REFERENCIA: {Referência (INSERIR O ANO DA DÍVIDA)}
VALOR ORIGINAL: {Valor Original}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa} CONFORME NORMATIVA DO SENAI
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} {E-mail}
OBS: {Observações}
""",
    
    "ACD - BOLETO": """
BOLETO (ACD – ACORDO):

UNIDADE: {Unidade (SENAI, SESI OU IEL)}
NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
REFERENCIA: {Referência (INSERIR O ANO DA DÍVIDA)}
VALOR ORIGINAL: {Valor Original}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa} CONFORME NORMATIVA
VALOR PROPOSTO: {Valor Proposto}
VALOR DA ENTRADA: {Valor da Entrada}
QUANTIDADE DE PARCELAS: {Quantidade de Parcelas}
VALOR DE CADA PARCELA: {Valor de Cada Parcela}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
BOLETO ENVIAR PELO WHATS/E-MAIL: {WhatsApp} {E-mail}
OBS: {Observações}
""",
    
    "ACD - ACORDO": """
Acionamento: 
CONTRATANTE: {Contratante}
CPF/CNPJ: {CPF/CNPJ}
FATURAS A PAGAR: {Faturas a Pagar}
TITULOS: {Títulos}
DIAS EM ATRASO: {Dias em Atraso}
FORMA DE PAGAMENTO: {Forma de Pagamento}
DATA DE PAGAMENTO: {Data de Pagamento}
VALOR ORIGINAL: {Valor Original}
VALOR ATUALIZADO: {Valor Total Atualizado}
TELEFONE: {Telefone}
FORMA DE ENVIO: {Forma de Envio}
""",
    
    "ACV - À VISTA": """
CEDAE - À VISTA (ACV - ACORDO À VISTA):

MATRÍCULA: {Matrícula}
GRAVAÇÃO (TELEFONE): {Gravação (Telefone)}
VALOR ORIGINAL: {Valor Original}
VALOR ATUALIZADO: {Valor Total Atualizado}
DESCONTO PRINCIPAL: {Desconto Principal}
DESCONTO JUROS: {Desconto Juros}
DESCONTO MULTA: {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
WHATSAPP: {WhatsApp}
E-MAIL: {E-mail}
OBS: {Observações}
""",
    
    "ACP - PARCELADO": """
CEDAE - PARCELADO (ACP - ACORDO PARCELADO):

MATRÍCULA: {Matrícula}
GRAVAÇÃO (TELEFONE): {Gravação (Telefone)}
VALOR ORIGINAL: {Valor Original}
VALOR ATUALIZADO: {Valor Total Atualizado}
DESCONTO PRINCIPAL: {Desconto Principal}
DESCONTO JUROS: {Desconto Juros}
DESCONTO MULTA: {Desconto Multa}
VALOR PROPOSTO PARA PARCELAMENTO: {Valor Proposto para Parcelamento}
ENTRADA (BOLETO): {Entrada (Boleto)}
QTD DE PARCELAS: {Qtd de Parcelas}
VALOR DAS PARCELAS: {Valor de Cada Parcela}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
WHATSAPP: {WhatsApp}
E-MAIL: {E-mail}
OBS: {Observações}
""",
    
    "VIA - SEGUNDA VIA": """
CEDAE - SEGUNDA VIA (VIA – SEGUNDA VIA DE FATURA):

NOME: {Nome do Devedor}
MATRICULA: {Matrícula}
FATURA VENCIDA: {Fatura Vencida}
VALOR: {Valor}
NOVO VENCIMENTO: {Novo Vencimento}
TELEFONE: {Telefone}
EMAIL: {Email}
""",
    
    "ACV - À VISTA": """
ÁGUAS DE JOINVILLE - À VISTA (ACV – ACORDO À VISTA):

UNIDADE: {Unidade}
MATRÍCULA: {Matrícula}
CPF/CNPJ: {CPF/CNPJ}
TITULAR: {Titular}
TELEFONE: {Telefone}
VALOR DÉBITO ORIGINAL: {Valor Débito Original}
DESCONTO PRINCIPAL: {Desconto Principal}
DESCONTO JUROS: {Desconto Juros}
DESCONTO MULTA: {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO DAS FATURAS: {Vencimento das Faturas}
VENCIMENTO ACORDO: {Vencimento Acordo}
WHATSAPP: {WhatsApp}
E-MAIL: {E-mail}
OBS: {Observações}
""",
    
    "ACP - PARCELADO": """
ÁGUAS DE JOINVILLE - PARCELADO (ACP – ACORDO PARCELADO):

UNIDADE: {Unidade}
MATRÍCULA: {Matrícula}
CPF/CNPJ: {CPF/CNPJ}
TITULAR: {Titular}
TELEFONE: {Telefone}
VALOR DÉBITO ORIGINAL: {Valor Débito Original}
DESCONTO PRINCIPAL: {Desconto Principal}
DESCONTO JUROS: {Desconto Juros}
DESCONTO MULTA: {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
VALOR DE ENTRADA: {Valor de Entrada}
QUANTIDADE DE PARCELAS: {Quantidade de Parcelas}
VALOR DE CADA PARCELA: {Valor de Cada Parcela}
VENCIMENTO: {Data de Vencimento}
WHATSAPP: {WhatsApp}
E-MAIL: {E-mail}
OBS: {Observações}
""",
    
    
    
    
    
    "ACC - À VISTA": """
CASSEMS - À VISTA (ACC – ACORDO CASSEMS):

NOME: {Nome do Devedor}
CPF/CNPJ: {CPF/CNPJ}
TITULO: {Titulo}
VALOR ORIGINAL: {Valor Original}
VALOR TOTAL: {Valor Total}
DESCONTO PRINCIPAL: {Desconto Principal}
DESCONTO JUROS: {Desconto Juros}
DESCONTO MULTA: {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
WHATSAPP: {WhatsApp}
E-MAIL: {E-mail}
OBS: {Observações}
""",
    
    "ACC - PARCELADO": """
CASSEMS - PARCELADO (ACC – ACORDO CASSEMS):

NOME: {Nome do Devedor}
CPF/CNPJ: {CPF/CNPJ}
TITULO: {Titulo}
VALOR ORIGINAL: {Valor Original}
VALOR TOTAL: {Valor Total}
DESCONTO PRINCIPAL: {Desconto Principal}
DESCONTO JUROS: {Desconto Juros}
DESCONTO MULTA: {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
ENTRADA: {Entrada}
PARCELAS: {Parcelas}
VALOR DA PARCELA: {Valor da Parcela}
VENCIMENTO: {Data de Vencimento}
WHATSAPP: {WhatsApp}
E-MAIL: {E-mail}
OBS: {Observações}
""",
    
    
    
    "ACD - ACORDO": """
ÓTICA DINIZ: ACD - ACORDO:

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
""",
    
    "SENAC RJ - ACD - ACORDO": """
SENAC RJ - ACD - ACORDO:

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
""",
    
    "LIBERDADE MÉDICA - ACD - ACORDO": """
LIBERDADE MÉDICA: ACD - ACORDO:

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
""",
    
    "ÓTICA DINIZ - ACD - ACORDO": """
ÓTICA DINIZ: ACD - ACORDO:

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
""",
    
    "UNIMED - ACD - ACORDO": """
UNIMED: ACD - ACORDO:

CONTRATANTE: {Contratante}
CPF/CNPJ: {CPF/CNPJ}
FATURAS A PAGAR: {Faturas a Pagar}
TÍTULOS: {Títulos}
DIAS EM ATRASO: {Dias em Atraso}
FORMA DE PAGAMENTO: {Forma de Pagamento}
DATA DE PAGAMENTO: {Data de Pagamento}
VALOR ORIGINAL: {Valor Original}
VALOR ATUALIZADO: {Valor Atualizado}
TELEFONE: {Telefone}
FORMA DE ENVIO: {Forma de Envio}
""",
    
    "FIEB - ACD - PIX/DÉBITO/CRÉDITO": """
FIEB: PIX, DÉBITO OU CRÉDITO EM 12X (ACD – ACORDO):

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
""",
    
    "FIEB - ACD - BOLETO": """
FIEB: BOLETO (ACD – ACORDO):

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: BOLETO
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
"""
}
