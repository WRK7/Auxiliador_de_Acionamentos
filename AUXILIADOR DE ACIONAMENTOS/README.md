# Gerador de Acionamentos

Sistema para geração automática de modelos de acionamentos com interface minimalista e tema escuro.

## 📁 Arquivos do Sistema

- **`main.py`** - Programa principal (não editar)
- **`config.py`** - Configurações (editar aqui)
- **`requirements.txt`** - Dependências do Python

## ⚙️ Como Personalizar

### Editar Carteiras
Abra o arquivo `config.py` e modifique a lista `CARTEIRAS`:

```python
CARTEIRAS = [
    "SENAC RJ", 
    "CEDAEE", 
    "PREFEITURA RJ",
    "ESTADO RJ",
    "UNIÃO",
    "SUA NOVA CARTEIRA",  # Adicione aqui
    "OUTROS"
]
```

### Editar Tipos de Acionamento
Modifique a lista `TIPOS_ACIONAMENTO`:

```python
TIPOS_ACIONAMENTO = [
    "ACV - Ação de Cobrança de Verba Alimentícia",
    "VIA - Aviso de Inadimplência", 
    "ACP - Ação de Cobrança Pedido",
    "ACD - Ação de Cobrança Direta",
    "SEU NOVO TIPO - Descrição",  # Adicione aqui
    "OUTROS"
]
```

### Editar Campos de Informação
Modifique o dicionário `CAMPOS_INFO`:

```python
CAMPOS_INFO = {
    "Nome do Devedor": "",
    "CPF/CNPJ": "",
    "Data de Vencimento": "",
    "Valor da Dívida": "",
    "Número do Contrato": "",
    "Seu Novo Campo": "",  # Adicione aqui
    "Observações": ""
}
```

### Editar Modelos de Texto
Modifique o dicionário `MODELOS_ACIONAMENTO` para personalizar os textos:

```python
MODELOS_ACIONAMENTO = {
    "ACV": """
AÇÃO DE COBRANÇA DE VERBA ALIMENTÍCIA

Prezados Senhores,

Seu texto personalizado aqui...

Atenciosamente,
Equipe de Cobrança
""",
    # ... outros modelos
}
```

## 🚀 Como Executar

1. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Executar o programa:**
   ```bash
   python main.py
   ```

## 📋 Funcionalidades

- ✅ Interface minimalista com tema escuro
- ✅ Carteiras pré-definidas
- ✅ Tipos de acionamento específicos
- ✅ Campos de informação padronizados
- ✅ Geração automática de modelos
- ✅ Cópia para área de transferência
- ✅ Dados fixos (não modificáveis pelos usuários)

## 🔒 Segurança

- Os usuários não podem modificar carteiras, tipos ou campos
- Todas as configurações ficam no arquivo `config.py`
- Sistema seguro para compartilhamento entre computadores

## 📝 Notas

- Para adicionar novos elementos, edite apenas o arquivo `config.py`
- Após modificar `config.py`, reinicie o programa
- O sistema mantém consistência entre todos os computadores
