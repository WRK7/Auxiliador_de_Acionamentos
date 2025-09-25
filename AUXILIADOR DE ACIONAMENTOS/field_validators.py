"""
Módulo de validação de campos e formatação automática
"""

import re
from validators import Validator
from config import CAMPOS_OBRIGATORIOS, FORMATACAO_AUTOMATICA, PRAZO_MAXIMO_POR_CARTEIRA
from theme import DARK_THEME

class FieldValidators:
    """Classe permissiva: sem formatação automática e sem bloqueios."""
    
    def __init__(self, carteira_var):
        self.carteira_var = carteira_var
    
    def aplicar_formatacao_automatica(self, campo, valor):
        return valor
    
    def validar_campo(self, campo, valor):
        """Valida CPF/CNPJ, Data de Vencimento e Porcentagens, outros campos sempre válidos"""
        if campo == "CPF/CNPJ":
            if not valor.strip():
                return True  # Campo vazio é válido
            numeros = re.sub(r'[^0-9]', '', valor)
            if len(numeros) == 11:
                return Validator.validar_cpf(valor)
            elif len(numeros) == 14:
                return Validator.validar_cnpj(valor)
            return False  # Tamanho inválido
        elif campo == "Data de Vencimento":
            if not valor.strip():
                return True  # Campo vazio é válido
            return self._validar_data_vencimento(valor)
        elif self._eh_campo_porcentagem(campo):
            if not valor.strip():
                return True  # Campo vazio é válido
            return self._validar_porcentagem(valor)
        return True
    
    def validar_campo_com_mensagem(self, campo, valor):
        """Valida CPF/CNPJ, Data de Vencimento e Porcentagens, outros campos sempre válidos"""
        if campo == "CPF/CNPJ":
            if not valor.strip():
                return True, "Campo vazio"
            numeros = re.sub(r'[^0-9]', '', valor)
            if len(numeros) == 11:
                valido = Validator.validar_cpf(valor)
                return (valido, "CPF válido" if valido else "CPF inválido")
            elif len(numeros) == 14:
                valido = Validator.validar_cnpj(valor)
                return (valido, "CNPJ válido" if valido else "CNPJ inválido")
            else:
                return False, f"Documento deve ter 11 (CPF) ou 14 (CNPJ) dígitos. Atual: {len(numeros)}"
        elif campo == "Data de Vencimento":
            if not valor.strip():
                return True, "Campo vazio"
            return self._validar_data_vencimento_com_mensagem(valor)
        elif self._eh_campo_porcentagem(campo):
            if not valor.strip():
                return True, "Campo vazio"
            return self._validar_porcentagem_com_mensagem(valor)
        return True, "Campo válido"
    
    def limitar_entrada(self, campo, event):
        return None
    
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
    
    def _eh_campo_porcentagem(self, campo):
        """Verifica se o campo é um campo de porcentagem"""
        campos_porcentagem = [
            "Desconto Principal", "Desconto Juros", "Desconto Multa"
        ]
        return campo in campos_porcentagem
    
    def _validar_valor_monetario(self, valor):
        """Valida se o valor monetário é válido"""
        if not valor.strip():
            return True  # Campo vazio é válido (não obrigatório)
        
        # Remover formatação R$ e espaços
        valor_limpo = re.sub(r'[R$\s]', '', valor)
        
        if not valor_limpo:
            return False
        
        # Verificar se tem apenas números, vírgulas e pontos
        if not re.match(r'^[\d.,]+$', valor_limpo):
            return False
        
        # Validar formato brasileiro: pode ter múltiplos pontos como separadores de milhares
        # mas apenas uma vírgula como separador decimal
        if valor_limpo.count(',') > 1:
            return False
        
        # Se tem vírgula, validar formato brasileiro (pontos como separadores de milhares, vírgula como decimal)
        if ',' in valor_limpo:
            partes = valor_limpo.split(',')
            if len(partes) != 2:
                return False
            
            parte_inteira = partes[0]
            parte_decimal = partes[1]
            
            # Parte decimal deve ter no máximo 2 dígitos
            if len(parte_decimal) > 2 or not parte_decimal.isdigit():
                return False
            
            # Parte inteira pode ter pontos como separadores de milhares
            parte_sem_pontos = parte_inteira.replace('.', '')
            if not parte_sem_pontos.isdigit():
                return False
            
            # Validar se os pontos estão nas posições corretas (a cada 3 dígitos da direita)
            if '.' in parte_inteira:
                grupos = parte_inteira.split('.')
                # Primeiro grupo pode ter 1-3 dígitos, demais devem ter exatamente 3
                if len(grupos[0]) == 0 or len(grupos[0]) > 3:
                    return False
                for grupo in grupos[1:]:
                    if len(grupo) != 3 or not grupo.isdigit():
                        return False
        else:
            # Se não tem vírgula, deve ser apenas números e pontos (separadores de milhares)
            parte_sem_pontos = valor_limpo.replace('.', '')
            if not parte_sem_pontos.isdigit():
                return False
            
            # Validar posicionamento dos pontos se existirem
            if '.' in valor_limpo:
                grupos = valor_limpo.split('.')
                if len(grupos[0]) == 0 or len(grupos[0]) > 3:
                    return False
                for grupo in grupos[1:]:
                    if len(grupo) != 3 or not grupo.isdigit():
                        return False
        
        # Tentar converter para float para validação final
        try:
            # Substituir vírgula por ponto e remover pontos dos milhares para conversão
            valor_para_conversao = valor_limpo.replace('.', '').replace(',', '.')
            valor_float = float(valor_para_conversao)
            return valor_float >= 0  # Valores negativos não são permitidos
        except ValueError:
            return False
    
    def _validar_valor_monetario_com_mensagem(self, valor):
        """Valida valor monetário e retorna (valido, mensagem)"""
        if not valor.strip():
            return True, "Campo vazio"
        
        if not self._validar_valor_monetario(valor):
            return False, "Formato inválido (ex: 5000 ou 5.000,50)"
        
        return True, "Valor válido"
    
    def _validar_porcentagem(self, valor):
        """Valida se o valor de porcentagem é válido"""
        if not valor.strip():
            return True  # Campo vazio é válido (não obrigatório)
        
        # Remove formatação e verifica se é um número válido
        valor_limpo = re.sub(r'[^\d,]', '', valor)
        
        if not valor_limpo:
            return False
        
        # Verificar se tem apenas números e vírgulas
        if not re.match(r'^[\d,]+$', valor_limpo):
            return False
        
        # Verificar se não tem múltiplas vírgulas
        if valor_limpo.count(',') > 1:
            return False
        
        # Verificar se vírgula não está no início ou fim
        if valor_limpo.startswith(',') or valor_limpo.endswith(','):
            return False
        
        # Tentar converter para float
        try:
            # Substituir vírgula por ponto para conversão
            valor_float = float(valor_limpo.replace(',', '.'))
            return 0 <= valor_float <= 100  # Valores entre 0 e 100%
        except ValueError:
            return False
    
    def _validar_porcentagem_com_mensagem(self, valor):
        """Valida valor de porcentagem e retorna (valido, mensagem)"""
        if not valor.strip():
            return True, "Campo vazio"
        
        if not self._validar_porcentagem(valor):
            return False, "Formato inválido (ex: 15,50 ou 15)"
        
        return True, "Porcentagem válida"
    
    def _validar_data_vencimento(self, valor):
        """Valida data de vencimento: DD/MM/AAAA, de hoje até +7 dias"""
        from datetime import datetime, timedelta
        
        # Verificar formato DD/MM/AAAA
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', valor):
            return False
        
        try:
            # Converter para datetime
            data_vencimento = datetime.strptime(valor, '%d/%m/%Y')
            hoje = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            data_maxima = hoje + timedelta(days=7)
            
            # Verificar se está no período permitido
            return hoje <= data_vencimento <= data_maxima
        except ValueError:
            return False
    
    def _validar_data_vencimento_com_mensagem(self, valor):
        """Valida data de vencimento e retorna (valido, mensagem)"""
        from datetime import datetime, timedelta
        
        if not valor.strip():
            return True, "Campo vazio"
        
        # Verificar formato
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', valor):
            return False, "Formato inválido (DD/MM/AAAA)"
        
        try:
            data_vencimento = datetime.strptime(valor, '%d/%m/%Y')
            hoje = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            data_maxima = hoje + timedelta(days=7)
            
            if data_vencimento < hoje:
                return False, f"Data não pode ser anterior a hoje ({hoje.strftime('%d/%m/%Y')})"
            elif data_vencimento > data_maxima:
                return False, f"Data não pode ser posterior a {data_maxima.strftime('%d/%m/%Y')} (máximo 7 dias)"
            else:
                return True, "Data válida"
        except ValueError:
            return False, "Data inválida"
