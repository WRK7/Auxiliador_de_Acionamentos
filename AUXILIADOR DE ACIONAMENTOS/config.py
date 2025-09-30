# Configurações mínimas para iniciar com SENAC RJ - ACD - ACORDO

# Carteiras disponíveis
CARTEIRAS = [
    "SENAC RJ"
]
if "SENAC BA/RJ" not in CARTEIRAS:
    CARTEIRAS.append("SENAC BA/RJ")

# Tipos de acionamento disponíveis (globais)
TIPOS_ACIONAMENTO = [
    "ACD - ACORDO",
    "ACD - ACORDO PARCELADO"
]

# Campos de informação (somente os usados nesta carteira/tipo)
CAMPOS_INFO = {
    "Nome do Devedor": "",
    "CPF/CNPJ": "",
    "CRE/Contrato": "",
    "Valor Total Atualizado": "",
    "Desconto Principal": "",
    "Desconto Juros": "",
    "Desconto Multa": "",
    "Valor Proposto": "",
    "Valor Confirmado": "",
    "Horário da Ligação": "",
    "Entrada de": "",
    "Quantidade de Parcelas": "",
    "Valor das Parcelas": "",
    "Data de Vencimento": "",
    "WhatsApp": "",
    "E-mail": "",
    "Observações": ""
}

# Campos obrigatórios (específico do cenário atual)
CAMPOS_OBRIGATORIOS = [
    "Nome do Devedor",
    "CPF/CNPJ",
    "Valor Total Atualizado",
    "Valor Proposto",
    "Entrada de",
    "Quantidade de Parcelas",
    "Valor das Parcelas",
    "Data de Vencimento",
    "WhatsApp",
    "E-mail"
]

# Prazo máximo por carteira (dias)
PRAZO_MAXIMO_POR_CARTEIRA = {
    "SENAC RJ": 7,
    "SENAC BA/RJ": 7
}

# Tipos por carteira
TIPOS_POR_CARTEIRA = {
    "SENAC RJ": ["ACD - ACORDO", "ACD - ACORDO PARCELADO"],
    "SENAC BA/RJ": ["ACD - ACORDO", "ACD - ACORDO PARCELADO"]
}

# Formatação automática por campo
FORMATACAO_AUTOMATICA = {
    "CPF/CNPJ": "cpf_cnpj",
    "Valor Total Atualizado": "moeda",
    "Valor Proposto": "moeda",
    "Valor Confirmado": "moeda",
    "Entrada de": "moeda",
    "Valor das Parcelas": "moeda",
    "Desconto Principal": "porcentagem",
    "Desconto Juros": "porcentagem",
    "Desconto Multa": "porcentagem",
    "Data de Vencimento": "data"
}

# Campos específicos por tipo (chave específica por carteira + tipo)
CAMPOS_POR_TIPO = {
    "SENAC RJ - ACD - ACORDO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Data de Vencimento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ]
    ,
    "SENAC BA/RJ - ACD - ACORDO": [
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
    ]
    ,
    "SENAC RJ - ACD - ACORDO PARCELADO": [
        "Nome do Devedor",
        "CPF/CNPJ",
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
    ]
}

# Modelo de saída (usa descontos em linha única)
MODELOS_ACIONAMENTO = {
    "SENAC RJ - ACD - ACORDO": """
NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO:{Valor Proposto}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
"""
    ,
    "SENAC BA/RJ - ACD - ACORDO": """
NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
CRE/CONTRATO: {CRE/Contrato}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO:{Valor Proposto}
VENCIMENTO: {Data de Vencimento}
VALOR CONFIRMADO: {Valor Confirmado} SIG/planilha.
HORÁRIO DA LIGAÇÃO: {Horário da Ligação}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
"""
    ,
    "SENAC RJ - ACD - ACORDO PARCELADO": """
NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
PARCELAMENTO: ENTRADA DE {Entrada de} (DÉBITO/BOLETO) + {Quantidade de Parcelas}X {Valor das Parcelas} (BOLETO/CRÉDITO)
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
"""
}

