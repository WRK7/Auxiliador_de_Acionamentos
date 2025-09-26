# 🚀 Auxiliador de Acionamentos

Sistema para geração automática de modelos de acionamento com validações e histórico inteligente.

## ✨ Funcionalidades

### 🎯 **Geração de Modelos**
- 11 carteiras configuradas (SENAC, CEDAE, FIRJAN, etc.)
- Validações automáticas de CPF/CNPJ, datas, valores
- Formatação automática de moeda e porcentagens
- Descontos em linha única

### 📊 **Histórico Inteligente**
- Busca avançada por CPF, ID, valor, texto
- Filtros por carteira, tipo e período
- Interface limpa e organizada

### ✅ **Validações**
- CPF/CNPJ com formatação automática
- Datas de vencimento (DD/MM/AAAA) com prazo de 7 dias
- Porcentagens com conversão automática de ponto para vírgula
- Campos obrigatórios (exceto WhatsApp, E-mail e Observações)

## 🚀 Instalação Rápida

### **Opção 1: Execução Automática**
1. Duplo clique em `EXECUTAR.bat`
2. Aguarde a instalação das dependências
3. O programa abrirá automaticamente

### **Opção 2: Manual**
1. Abra o Prompt de Comando
2. Navegue até a pasta do programa
3. Execute: `pip install -r requirements.txt`
4. Execute: `python main.py`

## 📋 Pré-requisitos

- **Python 3.8+** (obrigatório)
- **Windows 10/11** (recomendado)
- **Conexão com internet** (apenas na primeira instalação)

## 📁 Estrutura do Projeto

```
Auxiliador_Acionamentos_Portavel/
├── main.py                    # Ponto de entrada
├── app.py                     # Interface principal
├── config.py                  # Configurações das carteiras
├── validators.py              # Validações gerais
├── field_validators.py        # Validações de campos
├── model_generator.py         # Geração de modelos
├── historico.py               # Gerenciamento do histórico
├── historico_ui.py            # Interface do histórico
├── theme.py                   # Tema visual
├── ui_components.py           # Componentes da UI
├── requirements.txt           # Dependências
├── EXECUTAR.bat               # Executor automático
├── INSTALACAO.txt             # Instruções de instalação
├── README.md                  # Este arquivo
└── historico/                 # Pasta do histórico
    ├── acionamentos.json      # Dados do histórico
    └── contador.json          # Contador de IDs
```

## 🎯 Carteiras Configuradas

| Carteira | Tipos Disponíveis |
|----------|-------------------|
| **SENAC RJ** | ACD - ACORDO, ACP - PARCELADO |
| **SENAC BA ou MS** | ACD - À VISTA, ACD - PARCELADO |
| **SESC** | ACD - À VISTA, ACD - PARCELADO |
| **FIRJAN** | ACF - À VISTA, ACF - PARCELADO |
| **FIEB** | ACD - PIX/DÉBITO/CRÉDITO, ACD - BOLETO |
| **UNIMED** | ACD - ACORDO |
| **CEDAE** | ACV - À VISTA, ACP - PARCELADO, VIA - SEGUNDA VIA |
| **ÁGUAS DE JOINVILLE** | ACV - À VISTA, ACP - PARCELADO |
| **CASSEMS** | ACC - À VISTA, ACC - PARCELADO |
| **ÓTICA DINIZ** | ACD - ACORDO |
| **LIBERDADE MÉDICA** | ACD - ACORDO |

## 🔧 Solução de Problemas

### ❌ **Erro: "ModuleNotFoundError"**
```bash
pip install -r requirements.txt
```

### ❌ **Erro: "Permission denied"**
- Execute o CMD como Administrador
- Ou use o arquivo `EXECUTAR.bat`

### ❌ **Erro: "Python not found"**
- Instale Python 3.8+ do [site oficial](https://python.org)
- Marque a opção "Add Python to PATH" durante a instalação

### ❌ **Programa não abre**
- Verifique se todos os arquivos estão na pasta
- Execute `python main.py` no terminal para ver erros

## 📞 Suporte

- **Desenvolvedor**: Wesley Cruz
- **Data**: 26/09/2025
- **Versão**: 1.0

## 📝 Changelog

### v1.0 (26/09/2025)
- ✅ Sistema completo de geração de modelos
- ✅ 11 carteiras configuradas
- ✅ Validações automáticas
- ✅ Histórico inteligente
- ✅ Interface moderna e responsiva
- ✅ Pacote portável para instalação

---

**🎯 Sistema pronto para uso em produção!**
