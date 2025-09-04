# Configurações do Gerador de Acionamentos
# Edite este arquivo para modificar carteiras, tipos e campos

# Carteiras disponíveis
CARTEIRAS = [
    "SENAC RJ", 
    "CEDAEE", 
    "PREFEITURA RJ",
    "ESTADO RJ",
    "UNIÃO",
    "OUTROS"
]

# Tipos de acionamento disponíveis
TIPOS_ACIONAMENTO = [
    "ACV - Ação de Cobrança de Verba Alimentícia",
    "VIA - Aviso de Inadimplência", 
    "ACP - Ação de Cobrança Pedido",
    "ACD - Ação de Cobrança Direta",
    "OUTROS"
]

# Campos de informação padrão
CAMPOS_INFO = {
    "Nome do Devedor": "",
    "CPF/CNPJ": "",
    "Data de Vencimento": "",
    "Valor da Dívida": "",
    "Número do Contrato": "",
    "Observações": ""
}

# Configurações de validação
CAMPOS_OBRIGATORIOS = [
    "Nome do Devedor",
    "CPF/CNPJ", 
    "Data de Vencimento",
    "Valor da Dívida"
]

# Configurações de prazo máximo por carteira (em dias)
PRAZO_MAXIMO_POR_CARTEIRA = {
    "SENAC RJ": 7,
    "CEDAEE": 5,
    "PREFEITURA RJ": 7,
    "ESTADO RJ": 10,
    "UNIÃO": 15,
    "OUTROS": 7
}

# Configurações de formatação automática
FORMATACAO_AUTOMATICA = {
    "CPF/CNPJ": "cpf_cnpj",
    "Data de Vencimento": "data",
    "Valor da Dívida": "moeda"
}

# Modelos de texto para cada tipo de acionamento
MODELOS_ACIONAMENTO = {
    "ACV": """
AÇÃO DE COBRANÇA DE VERBA ALIMENTÍCIA

Prezados Senhores,

Vimos por meio desta, solicitar a cobrança da verba alimentícia em atraso, conforme dados acima.

Atenciosamente,
Equipe de Cobrança
""",
    
    "VIA": """
AVISO DE INADIMPLÊNCIA

Prezados Senhores,

Informamos que o(a) devedor(a) encontra-se em situação de inadimplência, conforme dados acima.

Solicitamos as providências cabíveis.

Atenciosamente,
Equipe de Cobrança
""",
    
    "ACP": """
AÇÃO DE COBRANÇA PEDIDO

Prezados Senhores,

Vimos por meio desta, solicitar a cobrança do valor em atraso, conforme dados acima.

Atenciosamente,
Equipe de Cobrança
""",
    
    "ACD": """
AÇÃO DE COBRANÇA DIRETA

Prezados Senhores,

Vimos por meio desta, solicitar a cobrança direta do valor em atraso, conforme dados acima.

Atenciosamente,
Equipe de Cobrança
""",
    
    "OUTROS": """
ACIONAMENTO

Prezados Senhores,

Vimos por meio desta, solicitar as providências cabíveis, conforme dados acima.

Atenciosamente,
Equipe de Cobrança
"""
}
