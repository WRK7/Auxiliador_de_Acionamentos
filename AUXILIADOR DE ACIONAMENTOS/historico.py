# Sistema de Histórico para o Gerador de Acionamentos
import json
import os
import sys
from datetime import datetime
import getpass
import socket

class HistoricoManager:
    """Gerenciador do histórico de acionamentos"""
    
    def __init__(self, pasta_historico="historico"):
        # Resolver pasta base ao lado do executável quando congelado (PyInstaller)
        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))

        # Sempre usar a pasta de histórico ao lado do app/exe
        self.pasta_historico = os.path.join(base_dir, pasta_historico)
        self.arquivo_historico = os.path.join(self.pasta_historico, "acionamentos.json")
        self.arquivo_contador = os.path.join(self.pasta_historico, "contador.json")
        
        # Criar estrutura de pastas organizadas
        self.criar_estrutura_pastas()
    
    def criar_estrutura_pastas(self):
        """Cria estrutura de pastas organizadas para o histórico"""
        # Pasta principal
        if not os.path.exists(self.pasta_historico):
            os.makedirs(self.pasta_historico)
        
        # Pastas por ano
        ano_atual = datetime.now().year
        pasta_ano = os.path.join(self.pasta_historico, str(ano_atual))
        if not os.path.exists(pasta_ano):
            os.makedirs(pasta_ano)
        
        # Pastas por mês dentro do ano
        mes_atual = datetime.now().month
        pasta_mes = os.path.join(pasta_ano, f"{mes_atual:02d}")
        if not os.path.exists(pasta_mes):
            os.makedirs(pasta_mes)
        
        # Pasta de backups
        pasta_backup = os.path.join(self.pasta_historico, "backups")
        if not os.path.exists(pasta_backup):
            os.makedirs(pasta_backup)
    
    def obter_proximo_id(self, tipo_acionamento):
        """Obtém o próximo ID sequencial para o tipo de acionamento"""
        try:
            if os.path.exists(self.arquivo_contador):
                with open(self.arquivo_contador, 'r', encoding='utf-8') as f:
                    contadores = json.load(f)
            else:
                contadores = {}
            
            # Obter prefixo do tipo (ACV, VIA, ACP, etc.)
            prefixo = tipo_acionamento.split(' - ')[0] if ' - ' in tipo_acionamento else tipo_acionamento[:3].upper()
            ano_atual = datetime.now().year
            
            chave = f"{prefixo}_{ano_atual}"
            
            if chave not in contadores:
                contadores[chave] = 0
            
            contadores[chave] += 1
            
            # Salvar contador atualizado
            with open(self.arquivo_contador, 'w', encoding='utf-8') as f:
                json.dump(contadores, f, ensure_ascii=False, indent=2)
            
            return f"{prefixo}-{ano_atual}-{contadores[chave]:03d}"
            
        except Exception as e:
            print(f"Erro ao obter próximo ID: {e}")
            return f"{tipo_acionamento[:3].upper()}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def salvar_acionamento(self, carteira, tipo, informacoes, modelo_gerado):
        """Salva um acionamento no histórico"""
        try:
            # Carregar histórico existente
            historico = self.carregar_historico()
            
            # Criar novo acionamento
            novo_acionamento = {
                "id": self.obter_proximo_id(tipo),
                "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "carteira": carteira,
                "tipo": tipo,
                "informacoes": informacoes,
                "modelo_gerado": modelo_gerado,
                "usuario": getpass.getuser(),
                "computador": socket.gethostname(),
                "ip": socket.gethostbyname(socket.gethostname())
            }
            
            # Adicionar ao histórico
            historico.append(novo_acionamento)
            
            # Salvar histórico
            self.salvar_historico(historico)
            
            return novo_acionamento["id"]
            
        except Exception as e:
            print(f"Erro ao salvar acionamento: {e}")
            return None
    
    def carregar_historico(self):
        """Carrega o histórico de acionamentos"""
        try:
            if os.path.exists(self.arquivo_historico):
                with open(self.arquivo_historico, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return []
        except Exception as e:
            print(f"Erro ao carregar histórico: {e}")
            return []
    
    def salvar_historico(self, historico):
        """Salva o histórico de acionamentos"""
        try:
            with open(self.arquivo_historico, 'w', encoding='utf-8') as f:
                json.dump(historico, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Erro ao salvar histórico: {e}")
    
    def buscar_acionamentos(self, filtros=None):
        """Busca acionamentos com filtros"""
        historico = self.carregar_historico()
        
        if not filtros:
            return historico
        
        resultado = []
        for acionamento in historico:
            incluir = True
            
            # Filtro por carteira
            if filtros.get('carteira') and filtros['carteira'] != acionamento['carteira']:
                incluir = False
            
            # Filtro por tipo
            if filtros.get('tipo') and filtros['tipo'] not in acionamento['tipo']:
                incluir = False
            
            # Filtro por usuário
            if filtros.get('usuario') and filtros['usuario'] != acionamento['usuario']:
                incluir = False
            
            # Filtro por período
            if filtros.get('data_inicio') or filtros.get('data_fim'):
                data_acionamento = datetime.strptime(acionamento['data_criacao'].split(' ')[0], '%d/%m/%Y')
                
                if filtros.get('data_inicio'):
                    data_inicio = datetime.strptime(filtros['data_inicio'], '%d/%m/%Y')
                    if data_acionamento < data_inicio:
                        incluir = False
                
                if filtros.get('data_fim'):
                    data_fim = datetime.strptime(filtros['data_fim'], '%d/%m/%Y')
                    if data_acionamento > data_fim:
                        incluir = False
            
            # Filtro por texto (busca avançada inteligente)
            if filtros.get('texto'):
                if not self._busca_avancada_match(acionamento, filtros['texto']):
                    incluir = False
            
            # Filtro por valor mínimo
            if filtros.get('valor_minimo'):
                try:
                    valor_minimo = float(filtros['valor_minimo'].replace('R$', '').replace('.', '').replace(',', '.'))
                    valor_acionamento = acionamento['informacoes'].get('Valor da Dívida', '0')
                    # Extrair valor numérico do campo de moeda
                    import re
                    valor_num = float(re.sub(r'[^\d,.]', '', valor_acionamento).replace(',', '.'))
                    if valor_num < valor_minimo:
                        incluir = False
                except (ValueError, TypeError):
                    pass  # Ignorar se não conseguir converter
            
            if incluir:
                resultado.append(acionamento)
        
        return resultado
    
    def obter_estatisticas(self):
        """Obtém estatísticas do histórico"""
        historico = self.carregar_historico()
        
        if not historico:
            return {
                "total": 0,
                "por_carteira": {},
                "por_tipo": {},
                "por_usuario": {},
                "por_mes": {}
            }
        
        stats = {
            "total": len(historico),
            "por_carteira": {},
            "por_tipo": {},
            "por_usuario": {},
            "por_mes": {}
        }
        
        for acionamento in historico:
            # Por carteira
            carteira = acionamento['carteira']
            stats["por_carteira"][carteira] = stats["por_carteira"].get(carteira, 0) + 1
            
            # Por tipo
            tipo = acionamento['tipo'].split(' - ')[0]
            stats["por_tipo"][tipo] = stats["por_tipo"].get(tipo, 0) + 1
            
            # Por usuário
            usuario = acionamento['usuario']
            stats["por_usuario"][usuario] = stats["por_usuario"].get(usuario, 0) + 1
            
            # Por mês
            data = acionamento['data_criacao'].split(' ')[0]
            mes_ano = '/'.join(data.split('/')[1:])  # MM/AAAA
            stats["por_mes"][mes_ano] = stats["por_mes"].get(mes_ano, 0) + 1
        
        return stats
    
    def duplicar_acionamento(self, id_acionamento):
        """Duplica um acionamento existente"""
        historico = self.carregar_historico()
        
        for acionamento in historico:
            if acionamento['id'] == id_acionamento:
                # Criar cópia sem ID e data
                copia = acionamento.copy()
                copia.pop('id', None)
                copia.pop('data_criacao', None)
                copia.pop('usuario', None)
                copia.pop('computador', None)
                copia.pop('ip', None)
                copia.pop('modelo_gerado', None)
                
                return copia
        
        return None
    
    def excluir_acionamento(self, id_acionamento):
        """Exclui um acionamento do histórico"""
        historico = self.carregar_historico()
        
        historico_filtrado = [a for a in historico if a['id'] != id_acionamento]
        
        if len(historico_filtrado) < len(historico):
            self.salvar_historico(historico_filtrado)
            return True
        
        return False
    
    def fazer_backup(self):
        """Faz backup do histórico atual"""
        try:
            historico = self.carregar_historico()
            if not historico:
                return False, "Nenhum dado para fazer backup"
            
            # Nome do arquivo de backup com timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            arquivo_backup = os.path.join(self.pasta_historico, "backups", f"backup_{timestamp}.json")
            
            # Salvar backup
            with open(arquivo_backup, 'w', encoding='utf-8') as f:
                json.dump(historico, f, ensure_ascii=False, indent=2)
            
            return True, f"Backup criado: {arquivo_backup}"
            
        except Exception as e:
            return False, f"Erro ao criar backup: {str(e)}"
    
    def restaurar_backup(self, arquivo_backup):
        """Restaura histórico de um backup"""
        try:
            if not os.path.exists(arquivo_backup):
                return False, "Arquivo de backup não encontrado"
            
            # Carregar backup
            with open(arquivo_backup, 'r', encoding='utf-8') as f:
                historico_backup = json.load(f)
            
            # Fazer backup do atual antes de restaurar
            self.fazer_backup()
            
            # Restaurar
            self.salvar_historico(historico_backup)
            
            return True, "Backup restaurado com sucesso"
            
        except Exception as e:
            return False, f"Erro ao restaurar backup: {str(e)}"
    
    def obter_lista_backups(self):
        """Obtém lista de backups disponíveis"""
        try:
            pasta_backups = os.path.join(self.pasta_historico, "backups")
            if not os.path.exists(pasta_backups):
                return []
            
            backups = []
            for arquivo in os.listdir(pasta_backups):
                if arquivo.startswith("backup_") and arquivo.endswith(".json"):
                    caminho_completo = os.path.join(pasta_backups, arquivo)
                    tamanho = os.path.getsize(caminho_completo)
                    data_modificacao = os.path.getmtime(caminho_completo)
                    
                    backups.append({
                        'arquivo': arquivo,
                        'caminho': caminho_completo,
                        'tamanho': tamanho,
                        'data': datetime.fromtimestamp(data_modificacao).strftime("%d/%m/%Y %H:%M:%S")
                    })
            
            # Ordenar por data (mais recente primeiro)
            backups.sort(key=lambda x: x['data'], reverse=True)
            return backups
            
        except Exception as e:
            print(f"Erro ao obter lista de backups: {e}")
            return []
    
    def _busca_avancada_match(self, acionamento, texto_busca):
        """Busca avançada inteligente em múltiplos campos"""
        import re
        from difflib import SequenceMatcher
        
        # Normalizar texto de busca
        texto_busca = texto_busca.strip().lower()
        
        if not texto_busca:
            return True
        
        # 1. BUSCA POR ID DO ACIONAMENTO
        if self._eh_busca_por_id(texto_busca):
            return self._buscar_por_id(acionamento, texto_busca)
        
        # 2. BUSCA POR CPF/CNPJ (PARCIAL OU COMPLETO)
        if self._eh_busca_por_cpf(texto_busca):
            return self._buscar_por_cpf(acionamento, texto_busca)
        
        # 3. BUSCA POR VALOR APROXIMADO
        if self._eh_busca_por_valor(texto_busca):
            return self._buscar_por_valor(acionamento, texto_busca)
        
        # 4. BUSCA TEXTUAL EM MÚLTIPLOS CAMPOS
        return self._buscar_em_campos_texto(acionamento, texto_busca)
    
    def _eh_busca_por_id(self, texto):
        """Detecta se é busca por ID (formato: ABC-2025-001)"""
        import re
        # Padrões: "ACD-2025-001", "ACD-001", "2025-001", etc.
        padroes_id = [
            r'^[A-Z]{2,4}-\d{4}-\d{3}$',  # Formato completo
            r'^[A-Z]{2,4}-\d{3}$',        # Sem ano
            r'^\d{4}-\d{3}$',             # Sem prefixo
            r'^[A-Z]{2,4}-\d{4}$'         # Sem número
        ]
        
        for padrao in padroes_id:
            if re.match(padrao, texto.upper()):
                return True
        return False
    
    def _buscar_por_id(self, acionamento, texto_busca):
        """Busca por ID do acionamento"""
        id_acionamento = acionamento['id'].lower()
        texto_busca = texto_busca.lower()
        
        # Busca exata
        if texto_busca == id_acionamento:
            return True
        
        # Busca parcial (qualquer parte do ID)
        if texto_busca in id_acionamento:
            return True
        
        # Busca por componentes (ACD, 2025, 001)
        componentes_busca = texto_busca.upper().replace('-', ' ').split()
        componentes_id = id_acionamento.upper().replace('-', ' ').split()
        
        for comp_busca in componentes_busca:
            encontrou = False
            for comp_id in componentes_id:
                if comp_busca in comp_id:
                    encontrou = True
                    break
            if not encontrou:
                return False
        
        return True
    
    def _eh_busca_por_cpf(self, texto):
        """Detecta se é busca por CPF/CNPJ"""
        import re
        # Remove formatação
        numeros = re.sub(r'[^0-9]', '', texto)
        
        # Se tem apenas números e pelo menos 3 dígitos, pode ser CPF
        if len(numeros) >= 3 and len(numeros) <= 14:
            return True
        
        # Se tem formato de CPF/CNPJ
        if re.match(r'[\d.-/]+', texto) and len(numeros) >= 3:
            return True
        
        return False
    
    def _buscar_por_cpf(self, acionamento, texto_busca):
        """Busca por CPF/CNPJ (parcial ou completo)"""
        import re
        
        cpf_acionamento = acionamento['informacoes'].get('CPF/CNPJ', '')
        
        # Extrair apenas números de ambos
        numeros_busca = re.sub(r'[^0-9]', '', texto_busca)
        numeros_cpf = re.sub(r'[^0-9]', '', cpf_acionamento)
        
        if not numeros_cpf:
            return False
        
        # Busca exata
        if numeros_busca == numeros_cpf:
            return True
        
        # Busca parcial (útil para últimos dígitos)
        if numeros_busca in numeros_cpf:
            return True
        
        # Busca por formato (com pontos e hífens)
        if texto_busca.lower() in cpf_acionamento.lower():
            return True
        
        return False
    
    def _eh_busca_por_valor(self, texto):
        """Detecta se é busca por valor monetário"""
        import re
        
        # Se contém R$ ou apenas números com vírgulas/pontos
        if 'r$' in texto.lower() or re.match(r'^[\d.,]+$', texto):
            return True
        
        # Se parece com valor (números seguidos de vírgula/ponto)
        if re.match(r'^\d+[.,]\d+$', texto):
            return True
        
        return False
    
    def _buscar_por_valor(self, acionamento, texto_busca):
        """Busca por valor aproximado (±10%)"""
        import re
        
        # Extrair valor numérico da busca
        try:
            valor_busca_str = re.sub(r'[^\d,.]', '', texto_busca)
            valor_busca = float(valor_busca_str.replace(',', '.').replace('..', '.'))
        except (ValueError, TypeError):
            return False
        
        # Margem de 10% para valores aproximados
        margem = valor_busca * 0.1
        valor_min = valor_busca - margem
        valor_max = valor_busca + margem
        
        # Buscar em campos de valor
        campos_valor = [
            'Valor da Dívida', 'Valor Total Atualizado', 'Valor Proposto',
            'Valor Confirmado', 'Valor Total Negociado', 'Total da Dívida'
        ]
        
        for campo in campos_valor:
            valor_campo = acionamento['informacoes'].get(campo, '')
            if valor_campo:
                try:
                    # Extrair valor numérico do campo
                    valor_numerico_str = re.sub(r'[^\d,.]', '', valor_campo)
                    if valor_numerico_str:
                        valor_numerico = float(valor_numerico_str.replace(',', '.').replace('..', '.'))
                        
                        # Verificar se está na faixa
                        if valor_min <= valor_numerico <= valor_max:
                            return True
                except (ValueError, TypeError):
                    continue
        
        return False
    
    def _buscar_em_campos_texto(self, acionamento, texto_busca):
        """Busca textual em múltiplos campos com busca fuzzy"""
        from difflib import SequenceMatcher
        
        # Campos para busca textual
        campos_busca = [
            'Nome do Devedor', 'Empresa', 'Cliente', 'Contratante', 'Titular',
            'Observações', 'Telefone', 'E-mail', 'WhatsApp', 'Email'
        ]
        
        for campo in campos_busca:
            valor_campo = acionamento['informacoes'].get(campo, '').lower()
            
            if not valor_campo:
                continue
            
            # 1. Busca exata
            if texto_busca in valor_campo:
                return True
            
            # 2. Busca fuzzy (tolerante a erros)
            if self._busca_fuzzy_match(texto_busca, valor_campo):
                return True
            
            # 3. Busca por palavras individuais
            palavras_busca = texto_busca.split()
            if len(palavras_busca) > 1:
                todas_encontradas = True
                for palavra in palavras_busca:
                    if len(palavra) >= 2 and palavra not in valor_campo:
                        todas_encontradas = False
                        break
                if todas_encontradas:
                    return True
        
        # Buscar também na carteira e tipo
        carteira = acionamento.get('carteira', '').lower()
        tipo = acionamento.get('tipo', '').lower()
        
        if texto_busca in carteira or texto_busca in tipo:
            return True
        
        return False
    
    def _busca_fuzzy_match(self, texto_busca, texto_campo, threshold=0.8):
        """Busca fuzzy com tolerância a erros de digitação"""
        from difflib import SequenceMatcher
        
        # Para textos muito curtos, ser mais rigoroso
        if len(texto_busca) <= 3:
            threshold = 0.9
        
        # Calcular similaridade
        similarity = SequenceMatcher(None, texto_busca, texto_campo).ratio()
        
        if similarity >= threshold:
            return True
        
        # Busca fuzzy por palavras individuais
        palavras_busca = texto_busca.split()
        palavras_campo = texto_campo.split()
        
        for palavra_busca in palavras_busca:
            if len(palavra_busca) >= 3:  # Só palavras com 3+ caracteres
                for palavra_campo in palavras_campo:
                    similarity = SequenceMatcher(None, palavra_busca, palavra_campo).ratio()
                    if similarity >= threshold:
                        return True
        
        return False
