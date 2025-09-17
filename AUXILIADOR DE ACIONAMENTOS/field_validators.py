"""
Módulo de validação de campos e formatação automática
"""

import re
from validators import Validator
from config import CAMPOS_OBRIGATORIOS, FORMATACAO_AUTOMATICA, PRAZO_MAXIMO_POR_CARTEIRA
from theme import DARK_THEME

class FieldValidators:
    """Classe para validação e formatação de campos"""
    
    def __init__(self, carteira_var):
        self.carteira_var = carteira_var
    
    def aplicar_formatacao_automatica(self, campo, valor):
        """Aplica formatação automática baseada no tipo do campo"""
        if campo in FORMATACAO_AUTOMATICA:
            tipo_formatacao = FORMATACAO_AUTOMATICA[campo]
            
            if tipo_formatacao == "cpf_cnpj":
                return Validator.formatar_cpf_cnpj(valor)
            elif tipo_formatacao == "data":
                return Validator.formatar_data(valor)
            elif tipo_formatacao == "moeda":
                return Validator.formatar_moeda(valor)
            elif tipo_formatacao == "porcentagem":
                return Validator.formatar_porcentagem(valor)
            elif tipo_formatacao == "parcela":
                return Validator.formatar_parcela(valor)
        
        return valor
    
    def validar_campo(self, campo, valor):
        """Valida um campo específico"""
        if campo == "CPF/CNPJ":
            numeros = re.sub(r'[^0-9]', '', valor)
            if len(numeros) == 11:
                return Validator.validar_cpf(valor)
            elif len(numeros) == 14:
                return Validator.validar_cnpj(valor)
            return False
        elif campo == "Data de Vencimento":
            # Usar validação específica para data de vencimento
            carteira_atual = self.carteira_var.get()
            if carteira_atual:
                valido, mensagem = Validator.validar_data_vencimento(valor, carteira_atual, PRAZO_MAXIMO_POR_CARTEIRA)
                return valido
            else:
                # Se não há carteira selecionada, usar validação básica
                return Validator.validar_data(valor)
        elif campo == "Data de Pagamento":
            # Validação básica para data de pagamento
            return Validator.validar_data(valor)
        elif self._eh_campo_valor(campo):
            # Validação para campos de valor monetário
            return self._validar_valor_monetario(valor)
        elif campo in CAMPOS_OBRIGATORIOS:
            return len(valor.strip()) > 0
        
        return True
    
    def validar_campo_com_mensagem(self, campo, valor):
        """Valida um campo específico e retorna (valido, mensagem)"""
        if campo == "CPF/CNPJ":
            numeros = re.sub(r'[^0-9]', '', valor)
            
            if len(numeros) == 11:
                valido = Validator.validar_cpf(valor)
                if valido:
                    return True, "CPF válido"
                else:
                    return False, "CPF inválido - verifique os dígitos"
            elif len(numeros) == 14:
                valido = Validator.validar_cnpj(valor)
                if valido:
                    return True, "CNPJ válido"
                else:
                    return False, "CNPJ inválido - verifique os dígitos"
            elif len(numeros) == 0:
                return False, "Digite um CPF ou CNPJ"
            else:
                return False, f"Documento deve ter 11 (CPF) ou 14 (CNPJ) dígitos. Atual: {len(numeros)}"
        elif campo == "Data de Vencimento":
            # Usar validação específica para data de vencimento
            carteira_atual = self.carteira_var.get()
            if carteira_atual:
                return Validator.validar_data_vencimento(valor, carteira_atual, PRAZO_MAXIMO_POR_CARTEIRA)
            else:
                # Se não há carteira selecionada, usar validação básica
                if Validator.validar_data(valor):
                    return True, "Data válida"
                else:
                    return False, "Formato inválido (DD/MM/AAAA)"
        elif campo == "Data de Pagamento":
            # Validação básica para data de pagamento
            if Validator.validar_data(valor):
                return True, "Data válida"
            else:
                return False, "Formato inválido (DD/MM/AAAA)"
        elif campo == "Enviar pelo WhatsApp/E-mail":
            # Validação específica para campo de envio
            if not valor.strip():
                return False, "Campo obrigatório"
            # Verificar se contém pelo menos uma das opções
            valor_lower = valor.lower()
            if "whatsapp" in valor_lower or "email" in valor_lower or "e-mail" in valor_lower:
                return True, "Formato válido"
            else:
                return False, "Digite 'WhatsApp' ou 'E-mail'"
        elif self._eh_campo_valor(campo):
            # Validação para campos de valor monetário
            return self._validar_valor_monetario_com_mensagem(valor)
        elif campo in CAMPOS_OBRIGATORIOS:
            if len(valor.strip()) > 0:
                return True, "Campo preenchido"
            else:
                return False, "Campo obrigatório"
        
        return True, "Campo válido"
    
    def limitar_entrada(self, campo, event):
        """Limita entrada de dados baseado no tipo do campo"""
        # Permitir teclas de controle (backspace, delete, setas, etc.)
        if event.keysym in ['BackSpace', 'Delete', 'Left', 'Right', 'Up', 'Down', 'Tab', 'Return']:
            return None
        
        if campo in ["Data de Vencimento", "Data de Pagamento"]:
            # Permitir apenas números
            if not event.char.isdigit():
                return 'break'
            # Verificar se já tem 8 dígitos
            valor_atual = event.widget.get()
            numeros = re.sub(r'[^0-9]', '', valor_atual)
            if len(numeros) >= 8:
                return 'break'
        
        elif campo == "CPF/CNPJ":
            # Permitir apenas números
            if not event.char.isdigit():
                return 'break'
            # Verificar se já tem 14 dígitos
            valor_atual = event.widget.get()
            numeros = re.sub(r'[^0-9]', '', valor_atual)
            if len(numeros) >= 14:
                return 'break'
        
        elif self._eh_campo_valor(campo):
            # Permitir apenas números, vírgulas e pontos para valores monetários
            if not event.char.isdigit() and event.char not in [',', '.']:
                return 'break'
            
            # Verificar se já tem vírgula ou ponto
            valor_atual = event.widget.get()
            if event.char in [',', '.']:
                if ',' in valor_atual or '.' in valor_atual:
                    return 'break'  # Já tem separador decimal
        
        return None  # Permite entrada normal para outros campos
    
    def _eh_campo_valor(self, campo):
        """Verifica se o campo é um campo de valor monetário"""
        campos_valor = [
            "Valor da Dívida", "Valor Total Atualizado", "Valor Proposto", 
            "Valor Confirmado", "Valor das Parcelas", "Valor Total Negociado",
            "Valor Original", "Valor Proposto para Parcelamento", "Valor de Cada Parcela",
            "Valor Débito Original", "Valor de Entrada", "Valor Debito Original",
            "Valor Negociado", "Valor da Parcelas", "Valor Total", "Valor da Parcela"
        ]
        return campo in campos_valor
    
    def _validar_valor_monetario(self, valor):
        """Valida se o valor monetário é válido"""
        if not valor.strip():
            return True  # Campo vazio é válido (não obrigatório)
        
        # Remover formatação e verificar se é um número válido
        valor_limpo = re.sub(r'[^\d,.]', '', valor)
        
        if not valor_limpo:
            return False
        
        # Verificar se tem apenas números, vírgulas e pontos
        if not re.match(r'^[\d.,]+$', valor_limpo):
            return False
        
        # Verificar se não tem múltiplas vírgulas ou pontos
        if valor_limpo.count(',') > 1 or valor_limpo.count('.') > 1:
            return False
        
        # Verificar se vírgula e ponto não estão juntos
        if ',.' in valor_limpo or '.,' in valor_limpo:
            return False
        
        # Tentar converter para float
        try:
            # Substituir vírgula por ponto para conversão
            valor_float = float(valor_limpo.replace(',', '.'))
            return valor_float >= 0  # Valores negativos não são permitidos
        except ValueError:
            return False
    
    def _validar_valor_monetario_com_mensagem(self, valor):
        """Valida valor monetário e retorna (valido, mensagem)"""
        if not valor.strip():
            return True, "Campo vazio"
        
        if not self._validar_valor_monetario(valor):
            return False, "Formato inválido (ex: 1000,00 ou 1000.00)"
        
        return True, "Valor válido"
