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
    "ÁGUAS DE GUARIROBA",
    "CASSEMS",
    "COMPESA",
    "ÓTICA DINIZ",
    "LIBERDADE MÉDICA"
]

# Tipos de acionamento disponíveis
TIPOS_ACIONAMENTO = [
    "ACD - ACORDO",
    "ACP - PARCELADO"
]

# Campos de informação padrão
CAMPOS_INFO = {
    "Nome do Devedor": "",
    "CPF/CNPJ": "",
    "Data de Vencimento": "",
    "Valor da Dívida": "",
    "Número do Contrato": "",
    "Títulos": "",
    "Valor Total Atualizado": "",
    "Desconto": "",
    "Valor Proposto": "",
    "Parcelamento": "",
    "Enviar pelo WhatsApp/E-mail": "",
    "Observações": "",
    "CRE/Contrato": "",
    "Valor Confirmado": "",
    "Horário da Ligação": "",
    "Contrato": "",
    "Entrada de": "",
    "Quant. P": "",
    "Valor das Parcelas": "",
    "Empresa": "",
    "Cliente": "",
    "Telefone": "",
    "E-mail": "",
    "Total da Dívida": "",
    "Acordo Realizado": "",
    "Valor Total Negociado": "",
    "Nº de Parcelas no Cartão": "",
    "Número e Valores dos Títulos": "",
    "Unidade": "",
    "Referência": "",
    "Valor Original": "",
    "Forma de Pagamento": "",
    "Contratante": "",
    "Faturas a Pagar": "",
    "Dias em Atraso": "",
    "Data de Pagamento": "",
    "Matrícula": "",
    "Gravação (Telefone)": "",
    "Valor Proposto para Parcelamento": "",
    "Entrada (Boleto)": "",
    "Qtd de Parcelas": "",
    "Valor de Cada Parcela": "",
    "Fatura Vencida": "",
    "Novo Vencimento": "",
    "Email": "",
    "Unidade": "",
    "Titular": "",
    "Valor Débito Original": "",
    "Vencimento das Faturas": "",
    "Vencimento Acordo": "",
    "Valor de Entrada": "",
    "Quantidade de Parcelas": "",
    "Valor de Cada Parcela": "",
    "Valor Total Atualizado": "",
    "Valor Debito Original": "",
    "Matrícula Inativa": "",
    "Valor Original": "",
    "De Desconto": "",
    "Valor Negociado": "",
    "Matrícula para Transferência": "",
    "Religação": "",
    "Entrada Negociação": "",
    "Valor da Parcelas": "",
    "Vencimento da Entrada": "",
    "Ativo - Religação": "",
    "Titulo": "",
    "Valor Total": "",
    "Valor Desconto": "",
    "Valor da Entrada": "",
    "Valor de Cada Parcela": "",
    "Parcelas": "",
    "Valor da Parcela": ""
}

# Configurações de validação
CAMPOS_OBRIGATORIOS = [
    "Nome do Devedor", "CPF/CNPJ", "Data de Vencimento", "Valor da Dívida", 
    "Número do Contrato", "Títulos", "Valor Total Atualizado", "Desconto", 
    "Valor Proposto", "Parcelamento", "Enviar pelo WhatsApp/E-mail", 
    "CRE/Contrato", "Valor Confirmado", "Horário da Ligação", "Contrato", 
    "Entrada de", "Quant. P", "Valor das Parcelas", "Empresa", "Cliente", 
    "Telefone", "E-mail", "Total da Dívida", "Acordo Realizado", 
    "Valor Total Negociado", "Nº de Parcelas no Cartão", 
    "Número e Valores dos Títulos", "Unidade", "Referência", "Valor Original", 
    "Forma de Pagamento", "Contratante", "Faturas a Pagar", "Dias em Atraso", 
    "Data de Pagamento", "Matrícula", "Gravação (Telefone)", 
    "Valor Proposto para Parcelamento", "Entrada (Boleto)", "Qtd de Parcelas", 
    "Valor de Cada Parcela", "Fatura Vencida", "Novo Vencimento", "Email", 
    "Titular", "Valor Débito Original", "Vencimento das Faturas", 
    "Vencimento Acordo", "Valor de Entrada", "Quantidade de Parcelas", 
    "Valor Debito Original", "De Desconto", "Valor Negociado", 
    "Matrícula para Transferência", "Religação", "Valor da Parcelas", 
    "Vencimento da Entrada", "Ativo - Religação", "Titulo", "Valor Total", 
    "Valor Desconto", "Valor da Entrada", "Parcelas", "Valor da Parcela",
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
    "ÁGUAS DE GUARIROBA": 7,
    "CASSEMS": 7,
    "COMPESA": 7,
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
        "SESC - À VISTA",
        "SESC - PARCELADO"
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
    "ÁGUAS DE GUARIROBA": [
        "ACV - MATRÍCULA ATIVA",
        "ACV - MATRÍCULA INATIVA",
        "ACP - INATIVO + ATIVO",
        "ACP - ATIVO OU INATIVO"
    ],
    "CASSEMS": [
        "ACC - À VISTA",
        "ACC - PARCELADO"
    ],
    "COMPESA": [
        "ACD - À VISTA",
        "ACP - PARCELADO"
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
    "Valor da Dívida": "moeda",
    "Valor Total Atualizado": "moeda",
    "Valor Proposto": "moeda",
    "Valor de Entrada": "moeda",
    "Valor de Cada Parcela": "parcela",
    "Valor das Parcelas": "parcela",
    "Valor da Parcela": "parcela",
    "Valor de Cada Parcela": "parcela",
}

# Campos específicos por tipo de acionamento
CAMPOS_POR_TIPO = {
    "ACD - ACORDO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Títulos",
        "Valor Total Atualizado",
        "Desconto",
        "Valor Proposto",
        "Data de Vencimento",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "ACP - PARCELADO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Títulos",
        "Valor Total Atualizado",
        "Desconto",
        "Valor Proposto",
        "Parcelamento",
        "Data de Vencimento",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "ACD - À VISTA": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "CRE/Contrato",
        "Valor Total Atualizado",
        "Desconto",
        "Valor Proposto",
        "Data de Vencimento",
        "Valor Confirmado",
        "Horário da Ligação",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "ACD - PARCELADO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "CRE/Contrato",
        "Valor Total Atualizado",
        "Desconto",
        "Valor Proposto",
        "Parcelamento",
        "Data de Vencimento",
        "Valor Confirmado",
        "Horário da Ligação",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "SESC - À VISTA": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Contrato",
        "Valor Total Atualizado",
        "Desconto",
        "Valor Proposto",
        "Data de Vencimento",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "SESC - PARCELADO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Contrato",
        "Valor Total Atualizado",
        "Desconto",
        "Valor Proposto",
        "Entrada de",
        "Quant. P",
        "Valor das Parcelas",
        "Data de Vencimento",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "ACF - À VISTA": [
        "Empresa",
        "Cliente",
        "CPF/CNPJ",
        "Telefone",
        "E-mail",
        "Total da Dívida",
        "Acordo Realizado",
        "Valor Total Negociado",
        "Nº de Parcelas no Cartão",
        "Número e Valores dos Títulos",
        "Data de Vencimento",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "ACF - PARCELADO": [
        "Empresa",
        "Cliente",
        "CPF/CNPJ",
        "Telefone",
        "E-mail",
        "Total da Dívida",
        "Acordo Realizado",
        "Valor Total Negociado",
        "Nº de Parcelas no Cartão",
        "Número e Valores dos Títulos",
        "Data de Vencimento",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "ACD - PIX/DÉBITO/CRÉDITO": [
        "Unidade",
        "Nome do Devedor",
        "CPF/CNPJ",
        "Referência",
        "Valor Original",
        "Valor Total Atualizado",
        "Desconto",
        "Valor Proposto",
        "Data de Vencimento",
        "Forma de Pagamento",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "ACD - BOLETO": [
        "Unidade",
        "Nome do Devedor",
        "CPF/CNPJ",
        "Referência",
        "Valor Original",
        "Valor Total Atualizado",
        "Desconto",
        "Valor Proposto",
        "Entrada (Boleto)",
        "Qtd de Parcelas",
        "Valor de Cada Parcela",
        "Data de Vencimento",
        "Forma de Pagamento",
        "Enviar pelo WhatsApp/E-mail",
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
        "Telefone"
    ],
    "ACV - À VISTA": [
        "Matrícula",
        "Gravação (Telefone)",
        "Valor Original",
        "Valor Total Atualizado",
        "Desconto",
        "Valor Proposto",
        "Data de Vencimento",
        "Forma de Pagamento",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "ACP - PARCELADO": [
        "Matrícula",
        "Gravação (Telefone)",
        "Valor Original",
        "Valor Total Atualizado",
        "Desconto",
        "Valor Proposto para Parcelamento",
        "Entrada (Boleto)",
        "Qtd de Parcelas",
        "Valor de Cada Parcela",
        "Data de Vencimento",
        "Forma de Pagamento",
        "Enviar pelo WhatsApp/E-mail",
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
        "Desconto",
        "Valor Proposto",
        "Vencimento das Faturas",
        "Vencimento Acordo",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "ACP - PARCELADO": [
        "Unidade",
        "Matrícula",
        "CPF/CNPJ",
        "Titular",
        "Telefone",
        "Valor Débito Original",
        "Desconto",
        "Valor Proposto",
        "Valor de Entrada",
        "Quantidade de Parcelas",
        "Valor de Cada Parcela",
        "Data de Vencimento",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "ACV - MATRÍCULA ATIVA": [
        "Matrícula",
        "CPF/CNPJ",
        "Titular",
        "Valor Total Atualizado",
        "Valor Debito Original",
        "Desconto",
        "Valor Proposto",
        "Forma de Pagamento",
        "Data de Vencimento",
        "Enviar pelo WhatsApp/E-mail"
    ],
    "ACV - MATRÍCULA INATIVA": [
        "Titular",
        "CPF/CNPJ",
        "Matrícula Inativa",
        "Valor Original",
        "Desconto",
        "Valor Proposto",
        "Forma de Pagamento",
        "Data de Vencimento",
        "Enviar pelo WhatsApp/E-mail"
    ],
    "ACP - INATIVO + ATIVO": [
        "Titular",
        "CPF/CNPJ",
        "Matrícula Inativa",
        "Valor Original",
        "De Desconto",
        "Valor Negociado",
        "Matrícula para Transferência",
        "Matrícula",
        "Religação",
        "Valor Original",
        "Desconto",
        "Valor Negociado",
        "Entrada Negociação",
        "Quantidade de Parcelas",
        "Valor da Parcelas",
        "Vencimento da Entrada"
    ],
    "ACP - ATIVO OU INATIVO": [
        "Matrícula",
        "CPF/CNPJ",
        "Ativo - Religação",
        "Titular",
        "Valor Total Atualizado",
        "Valor Debito Original",
        "Desconto",
        "Valor Negociado",
        "Entrada Negociação",
        "Quantidade de Parcelas",
        "Valor da Parcelas",
        "Vencimento da Entrada",
        "Enviar pelo WhatsApp/E-mail"
    ],
    "ACC - À VISTA": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Titulo",
        "Valor Original",
        "Valor Total",
        "Desconto",
        "Valor Proposto",
        "Data de Vencimento",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "ACC - PARCELADO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Titulo",
        "Valor Original",
        "Valor Total",
        "Desconto",
        "Valor Proposto",
        "Entrada",
        "Parcelas",
        "Valor da Parcela",
        "Data de Vencimento",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "ACD - À VISTA": [
        "Unidade",
        "Matrícula",
        "CPF/CNPJ",
        "Titular",
        "Telefone",
        "Valor Debito Original",
        "Valor Desconto",
        "Valor Proposto",
        "Data de Vencimento",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "ACP - PARCELADO": [
        "Unidade",
        "Matrícula",
        "CPF/CNPJ",
        "Titular",
        "Telefone",
        "Valor Debito Original",
        "Valor Desconto",
        "Valor da Entrada",
        "Quantidade de Parcelas",
        "Valor de Cada Parcela",
        "Data de Vencimento",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ],
    "ACD - ACORDO": [
        "Nome do Devedor",
        "CPF/CNPJ",
        "Valor Total Atualizado",
        "Desconto",
        "Valor Proposto",
        "Data de Vencimento",
        "Forma de Pagamento",
        "Enviar pelo WhatsApp/E-mail",
        "Observações"
    ]
}

# Modelos de texto para cada tipo de acionamento
MODELOS_ACIONAMENTO = {
    "ACD - ACORDO": """
SENAC RJ - Á VISTA: (ACD- ACORDO)

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
TÍTULOS: {Títulos}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto}% NO JUROS E MULTA
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACP - PARCELADO": """
SENAC RJ – PARCELADO: (ACP – ACORDO PARCELADO)

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
TÍTULOS: {Títulos}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto}% NO JUROS E MULTA
VALOR PROPOSTO: {Valor Proposto}
PARCELAMENTO: {Parcelamento}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACD - À VISTA": """
SENAC BA ou MS - À VISTA (ACD- ACORDO):

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
CRE/CONTRATO: {CRE/Contrato}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto}% NO JUROS E MULTA
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
VALOR CONFIRMADO: {Valor Confirmado}
HORÁRIO DA LIGAÇÃO: {Horário da Ligação}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACD - PARCELADO": """
SENAC BA ou MS - PARCELADO (ACD – ACORDO PARCELADO):

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
CRE/CONTRATO: {CRE/Contrato}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto}% NO JUROS E MULTA
VALOR PROPOSTO: {Valor Proposto}
PARCELAMENTO: {Parcelamento}
VENCIMENTO: {Data de Vencimento}
VALOR CONFIRMADO: {Valor Confirmado}
HORÁRIO DA LIGAÇÃO: {Horário da Ligação}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "SESC - À VISTA": """
SESC - À VISTA (ACD- ACORDO):

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
CONTRATO: {Contrato}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "SESC - PARCELADO": """
SESC - PARCELADO:

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
CONTRATO: {Contrato}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto}
VALOR PROPOSTO: {Valor Proposto}
ENTRADA DE: {Entrada de}
QUANT.P: {Quant. P}
VALOR DAS PARCELAS: {Valor das Parcelas}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACF - À VISTA": """
FIRJAN - À VISTA e PARCELADO (ACF – ACORDO FIRJAN):

EMPRESA: {Empresa}
CLIENTE: {Cliente}
CPF: {CPF/CNPJ}
TELEFONE: {Telefone}
E-MAIL: {E-mail}
TOTAL DA DÍVIDA: {Total da Dívida}
ACORDO REALIZADO: {Acordo Realizado}
VALOR TOTAL NEGOCIADO: {Valor Total Negociado}
Nº DE PARCELAS NO CARTÃO DE CRÉDITO: {Nº de Parcelas no Cartão}
NÚMERO E VALORES DOS TÍTULOS RENEGOCIADOS (Principal): {Número e Valores dos Títulos}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACF - PARCELADO": """
FIRJAN - À VISTA e PARCELADO (ACF – ACORDO FIRJAN):

EMPRESA: {Empresa}
CLIENTE: {Cliente}
CPF: {CPF/CNPJ}
TELEFONE: {Telefone}
E-MAIL: {E-mail}
TOTAL DA DÍVIDA: {Total da Dívida}
ACORDO REALIZADO: {Acordo Realizado}
VALOR TOTAL NEGOCIADO: {Valor Total Negociado}
Nº DE PARCELAS NO CARTÃO DE CRÉDITO: {Nº de Parcelas no Cartão}
NÚMERO E VALORES DOS TÍTULOS RENEGOCIADOS (Principal): {Número e Valores dos Títulos}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACD - PIX/DÉBITO/CRÉDITO": """
FIEB - PIX, DÉBITO OU CRÉDITO EM 12X (ACD – ACORDO):

UNIDADE: {Unidade}
NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
REFERENCIA: {Referência}
VALOR ORIGINAL: {Valor Original}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACD - BOLETO": """
FIEB - BOLETO (ACD – ACORDO):

UNIDADE: {Unidade}
NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
REFERENCIA: {Referência}
VALOR ORIGINAL: {Valor Original}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto}
VALOR PROPOSTO: {Valor Proposto}
VALOR DA ENTRADA: {Entrada (Boleto)}
QUANTIDADE DE PARCELAS: {Qtd de Parcelas}
VALOR DE CADA PARCELA: {Valor de Cada Parcela}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACD - ACORDO": """
UNIMED - ACD - ACORDO:

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
""",
    
    "ACV - À VISTA": """
CEDAE - À VISTA (ACV - ACORDO À VISTA):

MATRÍCULA: {Matrícula}
GRAVAÇÃO (TELEFONE): {Gravação (Telefone)}
VALOR ORIGINAL: {Valor Original}
VALOR ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACP - PARCELADO": """
CEDAE - PARCELADO (ACP - ACORDO PARCELADO):

MATRÍCULA: {Matrícula}
GRAVAÇÃO (TELEFONE): {Gravação (Telefone)}
VALOR ORIGINAL: {Valor Original}
VALOR ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto}
VALOR PROPOSTO PARA PARCELAMENTO: {Valor Proposto para Parcelamento}
ENTRADA (BOLETO): {Entrada (Boleto)}
QTD DE PARCELAS: {Qtd de Parcelas}
VALOR DAS PARCELAS: {Valor de Cada Parcela}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
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
DESCONTO: {Desconto}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO DAS FATURAS: {Vencimento das Faturas}
VENCIMENTO ACORDO: {Vencimento Acordo}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
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
DESCONTO: {Desconto}
VALOR PROPOSTO: {Valor Proposto}
VALOR DE ENTRADA: {Valor de Entrada}
QUANTIDADE DE PARCELAS: {Quantidade de Parcelas}
VALOR DE CADA PARCELA: {Valor de Cada Parcela}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACV - MATRÍCULA ATIVA": """
ÁGUAS DE GUARIROBA - À VISTA MATRÍCULA ATIVA (ACV – ACORDO À VISTA):

PORTES ADVOGADOS - ÁGUAS GUARIROBA
MATRÍCULA: {Matrícula}
CPF/CNPJ: {CPF/CNPJ}
TITULAR: {Titular}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
VALOR DEBITO ORIGINAL: {Valor Debito Original}
DESCONTO: {Desconto}
VALOR PROPOSTO: {Valor Proposto}
FORMA DE PAGAMENTO: {Forma de Pagamento}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
""",
    
    "ACV - MATRÍCULA INATIVA": """
ÁGUAS DE GUARIROBA - À VISTA MATRÍCULA INATIVA (ACV – ACORDO À VISTA):

PORTES ADVOGADOS - ÁGUAS GUARIROBA
TITULAR: {Titular}
CPF: {CPF/CNPJ}
MATRÍCULA INATIVA: {Matrícula Inativa}
VALOR ORIGINAL: {Valor Original}
DESCONTO: {Desconto}
VALOR PROPOSTO: {Valor Proposto}
FORMA DE PAGAMENTO: {Forma de Pagamento}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
""",
    
    "ACP - INATIVO + ATIVO": """
ÁGUAS DE GUARIROBA - PARCELADO INATIVO + ATIVO (ACP – ACORDO PARCELADO):

PORTES ADVOGADOS - ÁGUAS GUARIROBA
TITULAR: {Titular}
CPF: {CPF/CNPJ}
MATRÍCULA INATIVA: {Matrícula Inativa}
VALOR ORIGINAL: {Valor Original}
DE DESCONTO: {De Desconto}
VALOR NEGOCIADO: {Valor Negociado}
-
MATRÍCULA PARA TRANSFERÊNCIA DO DÉBITO: {Matrícula para Transferência}
-
MATRÍCULA ATIVA: {Matrícula}
RELIGAÇÃO: {Religação}
VALOR ORIGINAL: {Valor Original}
% DESCONTO: {Desconto}
VALOR NEGOCIADO: {Valor Negociado}
-
ENTRADA NEGOCIAÇÃO: {Entrada Negociação}
QUANTIDADE DE PARCELAS: {Quantidade de Parcelas}
VALOR DA PARCELAS: {Valor da Parcelas}
VENCIMENTO DA ENTRADA: {Vencimento da Entrada}
""",
    
    "ACP - ATIVO OU INATIVO": """
ÁGUAS DE GUARIROBA - PARCELADO ATIVO OU INATIVO (ACP – A. PARC):

PORTES ADVOGADOS - ÁGUAS GUARIROBA
MATRÍCULA: {Matrícula}
CPF/CNPJ: {CPF/CNPJ}
ATIVO - RELIGAÇÃO: {Ativo - Religação}
TITULAR: {Titular}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
VALOR DEBITO ORIGINAL: {Valor Debito Original}
DESCONTO: {Desconto}
VALOR NEGOCIADO: {Valor Negociado}
ENTRADA NEGOCIAÇÃO: {Entrada Negociação}
QUANTIDADE DE PARCELAS: {Quantidade de Parcelas}
VALOR DA PARCELAS: {Valor da Parcelas}
VENCIMENTO DA ENTRADA: {Vencimento da Entrada}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
""",
    
    "ACC - À VISTA": """
CASSEMS - À VISTA (ACC – ACORDO CASSEMS):

NOME: {Nome do Devedor}
CPF/CNPJ: {CPF/CNPJ}
TITULO: {Titulo}
VALOR ORIGINAL: {Valor Original}
VALOR TOTAL: {Valor Total}
DESCONTO: {Desconto}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACC - PARCELADO": """
CASSEMS - PARCELADO (ACC – ACORDO CASSEMS):

NOME: {Nome do Devedor}
CPF/CNPJ: {CPF/CNPJ}
TITULO: {Titulo}
VALOR ORIGINAL: {Valor Original}
VALOR TOTAL: {Valor Total}
DESCONTO: {Desconto}
VALOR PROPOSTO: {Valor Proposto}
ENTRADA: {Entrada}
PARCELAS: {Parcelas}
VALOR DA PARCELA: {Valor da Parcela}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACD - À VISTA": """
COMPESA - À VISTA (ACD – ACORDO):

UNIDADE: {Unidade}
MATRÍCULA: {Matrícula}
CPF/CNPJ: {CPF/CNPJ}
TITULAR: {Titular}
TELEFONE: {Telefone}
VALOR DEBITO ORIGINAL: {Valor Debito Original}
VALOR DESCONTO: {Valor Desconto}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACP - PARCELADO": """
COMPESA - PARCELADO (ACP – ACORDO PARCELADO):

UNIDADE: {Unidade}
MATRÍCULA: {Matrícula}
CPF/CNPJ: {CPF/CNPJ}
TITULAR: {Titular}
TELEFONE: {Telefone}
VALOR DEBITO ORIGINAL: {Valor Debito Original}
VALOR DESCONTO: {Valor Desconto}
VALOR DA ENTRADA: {Valor da Entrada}
QUANTIDADE DE PARCELAS: {Quantidade de Parcelas}
VALOR DE CADA PARCELA: {Valor de Cada Parcela}
VENCIMENTO: {Data de Vencimento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACD - ACORDO": """
ÓTICA DINIZ - ACD - ACORDO:

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
""",
    
    "ACD - ACORDO": """
LIBERDADE MÉDICA - ACD - ACORDO:

NOME: {Nome do Devedor}
CPF: {CPF/CNPJ}
VALOR TOTAL ATUALIZADO: {Valor Total Atualizado}
DESCONTO: {Desconto}
VALOR PROPOSTO: {Valor Proposto}
VENCIMENTO: {Data de Vencimento}
FORMA DE PAGAMENTO: {Forma de Pagamento}
ENVIAR PELO WHATS/E-MAIL: {Enviar pelo WhatsApp/E-mail}
OBS: {Observações}
"""
}
