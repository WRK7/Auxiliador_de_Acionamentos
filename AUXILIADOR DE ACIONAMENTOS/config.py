# Configurações mínimas para iniciar com SENAC RJ - ACD - ACORDO

# Carteiras disponíveis
CARTEIRAS = [
    "SENAC RJ"
]
if "SENAC MS/BA" not in CARTEIRAS:
    CARTEIRAS.append("SENAC MS/BA")
if "CEDAE" not in CARTEIRAS:
    CARTEIRAS.append("CEDAE")
if "SESC" not in CARTEIRAS:
    CARTEIRAS.append("SESC")
if "CASSEMS" not in CARTEIRAS:
    CARTEIRAS.append("CASSEMS")
if "UNIMED" not in CARTEIRAS:
    CARTEIRAS.append("UNIMED")
if "FIRJAN" not in CARTEIRAS:
    CARTEIRAS.append("FIRJAN")

# Tipos de acionamento disponíveis (globais)
TIPOS_ACIONAMENTO = [
    "ACD - ACORDO",
    "ACD - ACORDO PARCELADO",
    "ACV - ACORDO À VISTA",
    "ACP - ACORDO PARCELADO",
    "VIA - SEGUNDA VIA",
    "ACC - A VISTA",
    "ACC - PARCELADO",
    "ACF - A VISTA",
    "ACF - BOLETO"
]

# Campos de informação (somente os usados nesta carteira/tipo)
CAMPOS_INFO = {
    "Nome": "",
    "Nome do Devedor": "",
    "CPF/CNPJ": "",
    "CRE/Contrato": "",
    "QUANT P": "",
    "TITULO": "",
    "Unidade": "",
    "Contratante": "",
    "Faturas a Pagar": "",
    "Títulos": "",
    "Dias em Atraso": "",
    "Data de Pagamento": "",
    "Matrícula": "",
    "Gravação (Telefone)": "",
    "Telefone": "",
    "Fatura Vencida": "",
    "Valor": "",
    "Valor Original": "",
    "Valor Total": "",
    "Entrada": "",
    "Parcelas": "",
    "Valor da Parcela": "",
    "Valor Atualizado": "",
    "Valor Total Atualizado": "",
    "Desconto Principal": "",
    "Desconto Juros": "",
    "Desconto Multa": "",
    "Valor Proposto": "",
    "Valor Proposto para Parcelamento": "",
    "Valor Confirmado": "",
    "Horário da Ligação": "",
    "Forma de Pagamento": "",
    "Entrada (Boleto)": "",
    "Entrada de": "",
    "Qtd de Parcelas": "",
    "Quantidade de Parcelas": "",
    "Valor das Parcelas": "",
    "Valor de Cada Parcela": "",
    "Novo Vencimento": "",
    "Data de Vencimento": "",
    "WhatsApp": "",
    "E-mail": "",
    "Observações": ""
}

# Campos obrigatórios (específico do cenário atual)
CAMPOS_OBRIGATORIOS = [
    "Nome",
    "Nome do Devedor",
    "CPF/CNPJ",
    "CRE/Contrato",
    "TITULO",
    "Unidade",
    "Contratante",
    "Faturas a Pagar",
    "Títulos",
    "Dias em Atraso",
    "Data de Pagamento",
    "Matrícula",
    "Gravação (Telefone)",
    "Telefone",
    "Fatura Vencida",
    "Valor",
    "Valor Original",
    "Valor Total",
    "Entrada",
    "Parcelas",
    "Valor da Parcela",
    "Valor Atualizado",
    "Valor Total Atualizado",
    "Valor Proposto",
    "Valor Proposto para Parcelamento",
    "Valor Confirmado",
    "Horário da Ligação",
    "Forma de Pagamento",
    "Entrada (Boleto)",
    "Entrada de",
    "Qtd de Parcelas",
    "Quantidade de Parcelas",
    "Valor das Parcelas",
    "Novo Vencimento",
    "Data de Vencimento",
    "WhatsApp"
]

# Prazo máximo por carteira (dias)
PRAZO_MAXIMO_POR_CARTEIRA = {
    "SENAC RJ": 7,
    "SENAC MS/BA": 7,
    "CEDAE": 7,
    "CASSEMS": 7,
    "UNIMED": 2,
    "FIRJAN": 7
}

# Tipos por carteira
TIPOS_POR_CARTEIRA = {
    "SENAC RJ": ["ACD - ACORDO", "ACD - ACORDO PARCELADO"],
    "SENAC MS/BA": ["ACD - ACORDO", "ACD - ACORDO PARCELADO"],
    "CEDAE": ["ACV - ACORDO À VISTA", "ACP - ACORDO PARCELADO", "VIA - SEGUNDA VIA"],
    "SESC": ["ACD - ACORDO", "ACD - PARCELADO"],
    "CASSEMS": ["ACC - A VISTA", "ACC - PARCELADO"],
    "UNIMED": ["ACD - ACORDO"],
    "FIRJAN": ["ACF - A VISTA", "ACF - BOLETO"]
}

# Formatação automática por campo
FORMATACAO_AUTOMATICA = {
    "CPF/CNPJ": "cpf_cnpj",
    "Faturas a Pagar": "data",
    "Data de Pagamento": "data",
    "Fatura Vencida": "data",
    "Valor": "moeda",
    "Valor Original": "moeda",
    "Valor Total": "moeda",
    "Entrada": "moeda",
    "Valor da Parcela": "moeda",
    "Valor Atualizado": "moeda",
    "Valor Total Atualizado": "moeda",
    "Valor Proposto": "moeda",
    "Valor Proposto para Parcelamento": "moeda",
    "Valor Confirmado": "moeda",
    "Entrada (Boleto)": "moeda",
    "Entrada de": "moeda",
    "Valor das Parcelas": "moeda",
    "Valor de Cada Parcela": "moeda",
    "Desconto Principal": "porcentagem",
    "Desconto Juros": "porcentagem",
    "Desconto Multa": "porcentagem",
    "Novo Vencimento": "data",
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
    "SENAC MS/BA - ACD - ACORDO": [
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
    ,
    "CEDAE - ACV - ACORDO À VISTA": [
        "Matrícula",
        "Gravação (Telefone)",
        "Valor Original",
        "Valor Atualizado",
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
    ,
    "CEDAE - ACP - ACORDO PARCELADO": [
        "Matrícula",
        "Gravação (Telefone)",
        "Valor Original",
        "Valor Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto para Parcelamento",
        "Entrada (Boleto)",
        "Qtd de Parcelas",
        "Valor das Parcelas",
        "Data de Vencimento",
        "Forma de Pagamento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ]
    ,
    "CEDAE - VIA - SEGUNDA VIA": [
        "Nome",
        "Matrícula",
        "Fatura Vencida",
        "Valor",
        "Novo Vencimento",
        "Telefone",
        "E-mail"
    ]
    ,
    "SESC - ACD - ACORDO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "CRE/Contrato",
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
    "SESC - ACD - PARCELADO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "CRE/Contrato",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Entrada de",
        "QUANT P",
        "Valor das Parcelas",
        "Data de Vencimento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ]
    ,
    "CASSEMS - ACC - A VISTA": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "TITULO",
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
    ]
    ,
    "CASSEMS - ACC - PARCELADO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "TITULO",
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
    ]
    ,
    "FIRJAN - ACF - A VISTA": [
        "Unidade",
        "Nome do Devedor",
        "CPF/CNPJ",
        "E-mail",
        "Telefone",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Valor Proposto",
        "Forma de Pagamento",
        "Data de Vencimento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ]
    ,
    "FIRJAN - ACF - BOLETO": [
        "Unidade",
        "Nome do Devedor",
        "CPF/CNPJ",
        "E-mail",
        "Telefone",
        "Valor Total Atualizado",
        "Desconto Principal",
        "Desconto Juros",
        "Desconto Multa",
        "Entrada",
        "Quantidade de Parcelas",
        "Valor de Cada Parcela",
        "Forma de Pagamento",
        "Data de Vencimento",
        "WhatsApp",
        "E-mail",
        "Observações"
    ]
    ,
    "UNIMED - ACD - ACORDO": [
        "Contratante",
        "CPF/CNPJ",
        "Faturas a Pagar",
        "Títulos",
        "Dias em Atraso",
        "Forma de Pagamento",
        "Data de Pagamento",
        "Valor Original",
        "Valor Atualizado",
        "Telefone"
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
    "SENAC MS/BA - ACD - ACORDO": """
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
    ,
    "CEDAE - ACV - ACORDO À VISTA": """
MATRÍCULA: {Matrícula}
GRAVAÇÃO (TELEFONE): {Gravação (Telefone)}
VALOR ORIGINAL:{Valor Original}
VALOR ATUALIZADO:{Valor Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO:{Valor Proposto}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
"""
    ,
    "CEDAE - ACP - ACORDO PARCELADO": """
MATRÍCULA: {Matrícula}
GRAVAÇÃO (TELEFONE): {Gravação (Telefone)}
VALOR ORIGINAL:{Valor Original}
VALOR ATUALIZADO:{Valor Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO PARA PARCELAMENTO:{Valor Proposto para Parcelamento}
ENTRADA (BOLETO):{Entrada (Boleto)}
QTD DE PARCELAS: {Qtd de Parcelas}
VALOR DAS PARCELAS:{Valor das Parcelas}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
"""
    ,
    "CEDAE - VIA - SEGUNDA VIA": """
NOME: {Nome}
MATRICULA: {Matrícula}
FATURA VENCIDA: {Fatura Vencida}
VALOR:{Valor}
NOVO VENCIMENTO: {Novo Vencimento}
TELEFONE: {Telefone}
EMAIL: {E-mail}
"""
    ,
    "SESC - ACD - ACORDO": """
NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
CONTRATO: {CRE/Contrato}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO:{Valor Proposto}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
"""
    ,
    "SESC - ACD - PARCELADO": """
NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
CONTRATO: {CRE/Contrato}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO:{Valor Proposto}
ENTRADA DE: {Entrada de}
QUANT.P: {QUANT P}
VALOR DAS PARCELAS:{Valor das Parcelas}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
"""
    ,
    "CASSEMS - ACC - A VISTA": """
NOME: {Nome do Devedor}
CPF/CNPJ: {CPF/CNPJ}
TITULO: {TITULO}
VALOR ORIGINAL: {Valor Original}
VALOR TOTAL:{Valor Total}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
"""
    ,
    "CASSEMS - ACC - PARCELADO": """
NOME: {Nome do Devedor}
CPF/CNPJ: {CPF/CNPJ}
TITULO: {TITULO}
VALOR ORIGINAL:{Valor Original}
VALOR TOTAL:{Valor Total}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
ENTRADA: {Entrada}
PARCELAS: {Parcelas}
VALOR DA PARCELA: {Valor da Parcela}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
"""
    ,
    "FIRJAN - ACF - A VISTA": """
UNIDADE: {Unidade}
NOME: {Nome do Devedor}
CPF/CNPJ: {CPF/CNPJ}
E-MAIL: {E-mail}
TELEFONE: {Telefone}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
VALOR PROPOSTO: {Valor Proposto}
FORMA DE PAGAMENTO: {Forma de Pagamento}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
"""
    ,
    "FIRJAN - ACF - BOLETO": """
UNIDADE: {Unidade}
NOME: {Nome do Devedor}
CPF/CNPJ: {CPF/CNPJ}
E-MAIL: {E-mail}
TELEFONE: {Telefone}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto Principal} {Desconto Juros} {Desconto Multa}
ENTRADA: {Entrada}
QUANTIDA DE PARCELAS: {Quantidade de Parcelas}
VALOR DE CADA PARCELA: {Valor de Cada Parcela}
FORMA DE PAGAMENTO: {Forma de Pagamento}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {WhatsApp} / {E-mail}
OBS: {Observações}
"""
    ,
    "UNIMED - ACD - ACORDO": """
CONTRATANTE: {Contratante}
CPF/CNPJ: {CPF/CNPJ}
FATURAS A PAGAR: {Faturas a Pagar}
TITULOS: {Títulos}
DIAS EM ATRASO: {Dias em Atraso}
FORMA DE PAGAMENTO: {Forma de Pagamento}
DATA DE PAGAMENTO:  {Data de Pagamento}
VALOR ORIGINAL:  {Valor Original}
VALOR ATUALIZADO: {Valor Atualizado}
TELEFONE: {Telefone}
"""
}

