# Sistema de Validação para o Gerador de Acionamentos
import re
from datetime import datetime, timedelta

class Validator:
    """Classe para validações e formatações"""
    
    @staticmethod
    def validar_cpf(cpf):
        """Valida CPF e retorna se é válido"""
        # Remove caracteres não numéricos
        cpf = re.sub(r'[^0-9]', '', cpf)
        
        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            return False
        
        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False
        
        # Validação do primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = soma % 11
        if resto < 2:
            dv1 = 0
        else:
            dv1 = 11 - resto
        
        if int(cpf[9]) != dv1:
            return False
        
        # Validação do segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = soma % 11
        if resto < 2:
            dv2 = 0
        else:
            dv2 = 11 - resto
        
        if int(cpf[10]) != dv2:
            return False
        
        return True
    
    @staticmethod
    def validar_cnpj(cnpj):
        """Valida CNPJ e retorna se é válido"""
        # Remove caracteres não numéricos
        cnpj = re.sub(r'[^0-9]', '', cnpj)
        
        # Verifica se tem 14 dígitos
        if len(cnpj) != 14:
            return False
        
        # Verifica se todos os dígitos são iguais
        if cnpj == cnpj[0] * 14:
            return False
        
        # Validação do primeiro dígito verificador
        sequencia1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = 0
        for i in range(12):
            soma += int(cnpj[i]) * sequencia1[i]
        resto = soma % 11
        if resto < 2:
            dv1 = 0
        else:
            dv1 = 11 - resto
        
        if int(cnpj[12]) != dv1:
            return False
        
        # Validação do segundo dígito verificador
        sequencia2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = 0
        for i in range(13):
            soma += int(cnpj[i]) * sequencia2[i]
        resto = soma % 11
        if resto < 2:
            dv2 = 0
        else:
            dv2 = 11 - resto
        
        if int(cnpj[13]) != dv2:
            return False
        
        return True
    
    @staticmethod
    def formatar_cpf_cnpj(texto):
        """Formata CPF ou CNPJ automaticamente"""
        # Remove caracteres não numéricos
        numeros = re.sub(r'[^0-9]', '', texto)
        
        if len(numeros) <= 11:
            # Formatar como CPF
            if len(numeros) >= 3:
                cpf = numeros[:3]
                if len(numeros) >= 6:
                    cpf += '.' + numeros[3:6]
                    if len(numeros) >= 9:
                        cpf += '.' + numeros[6:9]
                        if len(numeros) >= 11:
                            cpf += '-' + numeros[9:11]
                return cpf
        else:
            # Formatar como CNPJ
            if len(numeros) >= 2:
                cnpj = numeros[:2]
                if len(numeros) >= 5:
                    cnpj += '.' + numeros[2:5]
                    if len(numeros) >= 8:
                        cnpj += '.' + numeros[5:8]
                        if len(numeros) >= 12:
                            cnpj += '/' + numeros[8:12]
                            if len(numeros) >= 14:
                                cnpj += '-' + numeros[12:14]
                return cnpj
        
        return texto
    
    @staticmethod
    def validar_data(data_str):
        """Valida data no formato DD/MM/AAAA"""
        try:
            # Remove espaços e caracteres extras
            data_str = data_str.strip()
            
            # Verifica se tem o formato correto
            if not re.match(r'^\d{2}/\d{2}/\d{4}$', data_str):
                return False
            
            # Tenta converter para datetime
            data_obj = datetime.strptime(data_str, '%d/%m/%Y')
            
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validar_data_vencimento(data_str, carteira, prazo_maximo_por_carteira):
        """Valida se a data de vencimento está dentro do prazo permitido para a carteira"""
        try:
            # Primeiro validar formato básico
            if not Validator.validar_data(data_str):
                return False, "Formato de data inválido (DD/MM/AAAA)"
            
            # Converter para datetime
            data_vencimento = datetime.strptime(data_str, '%d/%m/%Y')
            data_atual = datetime.now().date()  # Apenas a data, sem hora
            
            # Verificar se a data é no futuro (incluindo hoje)
            if data_vencimento.date() < data_atual:
                return False, "Data deve ser de hoje em diante"
            
            # Verificar prazo máximo da carteira
            prazo_maximo = prazo_maximo_por_carteira.get(carteira, 7)  # Default 7 dias
            data_limite = data_atual + timedelta(days=prazo_maximo)
            
            if data_vencimento.date() > data_limite:
                return False, f"Data deve ser até {prazo_maximo} dias a partir de hoje"
            
            return True, "Data válida"
            
        except Exception as e:
            return False, f"Erro na validação: {str(e)}"
    
    @staticmethod
    def formatar_data(texto):
        """Formata data automaticamente"""
        # Remove caracteres não numéricos
        numeros = re.sub(r'[^0-9]', '', texto)
        
        if len(numeros) >= 2:
            data = numeros[:2]
            if len(numeros) >= 4:
                data += '/' + numeros[2:4]
                if len(numeros) >= 8:
                    data += '/' + numeros[4:8]
            return data
        
        return texto
    
    @staticmethod
    def formatar_moeda(texto):
        """Formata valor monetário"""
        # Remove caracteres não numéricos
        numeros = re.sub(r'[^0-9]', '', texto)
        
        if numeros:
            # Converte para float e formata
            valor = float(numeros) / 100  # Assume que os últimos 2 dígitos são centavos
            return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        
        return texto
    
    @staticmethod
    def formatar_porcentagem(texto):
        """Formata porcentagem com validação específica"""
        # Remove caracteres não numéricos e vírgulas/pontos
        numeros = re.sub(r'[^0-9]', '', texto)
        
        if numeros:
            # Limitar a 4 dígitos (máximo 99,99%)
            if len(numeros) > 4:
                numeros = numeros[:4]
            
            # Se tem mais de 2 dígitos, adicionar vírgula antes dos últimos 2
            if len(numeros) > 2:
                # Inserir vírgula antes dos últimos 2 dígitos
                parte_inteira = numeros[:-2]
                parte_decimal = numeros[-2:]
                valor_formatado = f"{parte_inteira},{parte_decimal}"
            else:
                valor_formatado = numeros
            
            # Adiciona o símbolo de porcentagem
            return f"{valor_formatado}%"
        
        return texto
    
    @staticmethod
    def formatar_parcela(texto):
        """Formata valor de parcela com X no final"""
        # Remove caracteres não numéricos
        numeros = re.sub(r'[^0-9]', '', texto)
        
        if numeros:
            # Converte para float e formata como moeda + X
            valor = float(numeros) / 100  # Assume que os últimos 2 dígitos são centavos
            return f"R$ {valor:,.2f}X".replace(',', 'X').replace('.', ',').replace('X', '.')
        
        return texto
    
    @staticmethod
    def validar_campos_obrigatorios(campos, valores):
        """Valida se campos obrigatórios foram preenchidos"""
        campos_obrigatorios = ["Nome do Devedor", "CPF/CNPJ", "Data de Vencimento", "Valor da Dívida"]
        campos_vazios = []
        
        for campo in campos_obrigatorios:
            if campo in valores and not valores[campo].strip():
                campos_vazios.append(campo)
        
        return campos_vazios
    
    @staticmethod
    def obter_tipo_documento(texto):
        """Identifica se é CPF ou CNPJ baseado no tamanho"""
        numeros = re.sub(r'[^0-9]', '', texto)
        
        if len(numeros) == 11:
            return "CPF"
        elif len(numeros) == 14:
            return "CNPJ"
        else:
            return "INDEFINIDO"
