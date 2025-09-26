"""
Módulo de geração de modelos de acionamento
"""

import pyperclip
from datetime import datetime
from tkinter import messagebox
from validators import Validator
from config import CAMPOS_OBRIGATORIOS, PRAZO_MAXIMO_POR_CARTEIRA

class ModelGenerator:
    """Classe para geração de modelos de acionamento"""
    
    def __init__(self, historico_manager):
        self.historico_manager = historico_manager
    
    def gerar_modelo(self, carteira, tipo, campos_entries, carteira_var, texto_modelo, mostrar_popup=True):
        """Gera o modelo de acionamento baseado nas seleções"""
        if not carteira or not tipo:
            texto_modelo.delete(1.0, 'end')
            texto_modelo.insert(1.0, "Por favor, selecione uma carteira e um tipo de acionamento.")
            return
        
        # Coletar informações preenchidas
        informacoes = {}
        campos_invalidos = []
        
        for campo, entry in campos_entries.items():
            valor = entry.get().strip()
            
            # Ignorar placeholder na coleta de dados
            if campo in ["Data de Vencimento", "Vencimento Acordo"] and valor in ["DD/MM/AAAA", "Ex: 26/09/2025"]:
                valor = ""
            
            informacoes[campo] = valor
            
            # Validar CPF/CNPJ, Data de Vencimento e Porcentagens - bloquear se inválidos
            if campo in ["CPF/CNPJ", "Data de Vencimento", "Vencimento Acordo"] and valor:
                if not self._validar_campo_basico(campo, valor, carteira_var):
                    if campo == "CPF/CNPJ":
                        tipo_doc = Validator.obter_tipo_documento(valor)
                        campos_invalidos.append(f"{campo} ({tipo_doc} inválido)")
                    elif campo in ["Data de Vencimento", "Vencimento Acordo"]:
                        campos_invalidos.append(f"{campo} (data inválida ou fora do prazo)")
            
            # Validar campos de porcentagem
            if self._eh_campo_porcentagem(campo) and valor:
                if not self._validar_porcentagem_basica(valor):
                    campos_invalidos.append(f"{campo} (porcentagem inválida)")
            
            # Validar campos obrigatórios
            if self._eh_campo_obrigatorio(campo) and not valor.strip():
                campos_invalidos.append(f"{campo} (campo obrigatório)")
            
        
        # Bloquear se CPF/CNPJ, Data de Vencimento, Vencimento Acordo, Porcentagens ou campos obrigatórios inválidos
        if campos_invalidos:
            mensagem = "Por favor, corrija os seguintes campos:\n\n" + "\n".join(f"• {campo}" for campo in campos_invalidos)
            texto_modelo.delete(1.0, 'end')
            texto_modelo.insert(1.0, mensagem)
            if mostrar_popup:
                messagebox.showwarning("Campos Inválidos", mensagem)
            return
        
        # Gerar modelo baseado no tipo
        modelo = self.criar_modelo_acionamento(carteira, tipo, informacoes)
        
        # Salvar no histórico
        id_acionamento = self.historico_manager.salvar_acionamento(carteira, tipo, informacoes, modelo)
        
        texto_modelo.delete(1.0, 'end')
        texto_modelo.insert(1.0, modelo)
    
    def _validar_campo_basico(self, campo, valor, carteira_var):
        """Validação básica de campo"""
        import re
        if campo == "CPF/CNPJ":
            numeros = re.sub(r'[^0-9]', '', valor)
            if len(numeros) == 11:
                return Validator.validar_cpf(valor)
            elif len(numeros) == 14:
                return Validator.validar_cnpj(valor)
            return False
        elif campo in ["Data de Vencimento", "Vencimento Acordo"]:
            carteira_atual = carteira_var.get()
            if carteira_atual:
                valido, mensagem = Validator.validar_data_vencimento(valor, carteira_atual, PRAZO_MAXIMO_POR_CARTEIRA)
                return valido
            else:
                return Validator.validar_data(valor)
        elif campo in CAMPOS_OBRIGATORIOS:
            return len(valor.strip()) > 0
        
        return True
    
    def criar_modelo_acionamento(self, carteira, tipo, informacoes):
        """Cria o modelo específico baseado no tipo de acionamento usando templates"""
        from config import MODELOS_ACIONAMENTO
        
        # Criar chave específica para carteira + tipo
        chave_template = f"{carteira} - {tipo}"
        
        # Verificar se existe template específico para esta carteira + tipo
        if chave_template in MODELOS_ACIONAMENTO:
            template = MODELOS_ACIONAMENTO[chave_template]
        elif tipo in MODELOS_ACIONAMENTO:
            # Fallback para template genérico do tipo
            template = MODELOS_ACIONAMENTO[tipo]
        else:
            # Fallback para tipos não definidos
            data_atual = datetime.now().strftime("%d/%m/%Y")
            
            modelo = f"""
=== ACIONAMENTO - {tipo} ===
Carteira: {carteira}
Data: {data_atual}

"""
            
            # Processar descontos em uma linha única
            descontos_linha = self._formatar_descontos_linha_unica(informacoes)
            
            # Adicionar apenas informações preenchidas (sem duplicação)
            for campo, valor in informacoes.items():
                if valor:  # Só adicionar campos que têm valor
                    # Pular campos de desconto individuais (já foram processados)
                    if campo in ["Desconto Principal", "Desconto Juros", "Desconto Multa"]:
                        continue
                    modelo += f"{campo}: {valor}\n"
            
            # Adicionar linha de descontos se houver
            if descontos_linha:
                modelo += f"Descontos: {descontos_linha}\n"
            
            return modelo.strip()
        
        # Processar descontos em uma linha única
        descontos_linha = self._formatar_descontos_linha_unica(informacoes)
        
        # Preparar dados para substituição no template
        dados_template = informacoes.copy()
        
        # Substituir campos de desconto individuais pela linha única
        if descontos_linha:
            dados_template["Desconto Principal"] = descontos_linha
            dados_template["Desconto Juros"] = ""  # Limpar campos individuais
            dados_template["Desconto Multa"] = ""
        else:
            # Se não há descontos, limpar todos os campos
            dados_template["Desconto Principal"] = ""
            dados_template["Desconto Juros"] = ""
            dados_template["Desconto Multa"] = ""
        
        # Substituir placeholders no template
        try:
            modelo = template.format(**dados_template)
            return modelo.strip()
        except KeyError as e:
            # Se algum campo não existir no template, usar fallback
            return f"Erro no template: campo {e} não encontrado"
    
    def copiar_modelo(self, texto_modelo):
        """Copia apenas os dados preenchidos para a área de transferência"""
        texto = texto_modelo.get(1.0, 'end').strip()
        if texto:
            try:
                # Extrair apenas a parte dos dados (após o cabeçalho)
                linhas = texto.split('\n')
                dados_linhas = []
                em_dados = False
                
                for linha in linhas:
                    if linha.startswith('Carteira:') or linha.startswith('Data:'):
                        continue  # Pular cabeçalho
                    elif linha.startswith('==='):
                        continue  # Pular linha de título
                    elif linha.strip() == '':
                        em_dados = True  # Começar a capturar dados após linha vazia
                        continue
                    elif em_dados and ':' in linha:
                        dados_linhas.append(linha)
                
                # Copiar apenas os dados
                texto_para_copiar = '\n'.join(dados_linhas)
                pyperclip.copy(texto_para_copiar)
                messagebox.showinfo("Sucesso", "Dados copiados para a área de transferência!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao copiar: {e}")
        else:
            messagebox.showwarning("Aviso", "Nenhum modelo para copiar!")
    
    def _eh_campo_porcentagem(self, campo):
        """Verifica se o campo é um campo de porcentagem"""
        campos_porcentagem = [
            "Desconto Principal", "Desconto Juros", "Desconto Multa"
        ]
        return campo in campos_porcentagem
    
    def _eh_campo_obrigatorio(self, campo):
        """Verifica se o campo é obrigatório (todos exceto WhatsApp, E-mail e Observações)"""
        campos_opcionais = ["WhatsApp", "E-mail", "Observações"]
        return campo not in campos_opcionais
    
    def _formatar_descontos_linha_unica(self, informacoes):
        """Formata os descontos em uma linha única: '34% PRINCIPAL 100% JUROS 23% MULTA'"""
        descontos = []
        
        # Processar cada tipo de desconto
        if informacoes.get("Desconto Principal", "").strip():
            valor_principal = self._limpar_porcentagem(informacoes["Desconto Principal"])
            descontos.append(f"{valor_principal}% PRINCIPAL")
        
        if informacoes.get("Desconto Juros", "").strip():
            valor_juros = self._limpar_porcentagem(informacoes["Desconto Juros"])
            descontos.append(f"{valor_juros}% JUROS")
        
        if informacoes.get("Desconto Multa", "").strip():
            valor_multa = self._limpar_porcentagem(informacoes["Desconto Multa"])
            descontos.append(f"{valor_multa}% MULTA")
        
        return " ".join(descontos)
    
    def _limpar_porcentagem(self, valor):
        """Remove formatação da porcentagem e retorna apenas o número"""
        import re
        if not valor:
            return ""
        
        # Remove % e espaços, mantém apenas números e vírgula
        valor_limpo = re.sub(r'[^\d,]', '', valor)
        
        # Se tem vírgula, converte para ponto para normalizar
        if ',' in valor_limpo:
            valor_limpo = valor_limpo.replace(',', '.')
        
        return valor_limpo
    
    def _validar_porcentagem_basica(self, valor):
        """Validação básica de porcentagem - bloqueia letras e valores negativos"""
        import re
        if not valor.strip():
            return True  # Campo vazio é válido
        
        # Remove formatação e verifica se é um número válido
        valor_limpo = re.sub(r'[^\d,]', '', valor)
        
        if not valor_limpo:
            return False
        
        # Verificar se tem apenas números e vírgulas (bloqueia letras)
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
            # Bloqueia valores negativos e acima de 100%
            return 0 <= valor_float <= 100
        except ValueError:
            return False
    
