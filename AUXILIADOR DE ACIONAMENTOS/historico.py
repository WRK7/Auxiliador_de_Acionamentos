# Sistema de Histórico para o Gerador de Acionamentos
import json
import os
from datetime import datetime
import getpass
import socket

class HistoricoManager:
    """Gerenciador do histórico de acionamentos"""
    
    def __init__(self, pasta_historico="historico"):
        self.pasta_historico = pasta_historico
        self.arquivo_historico = os.path.join(pasta_historico, "acionamentos.json")
        self.arquivo_contador = os.path.join(pasta_historico, "contador.json")
        
        # Criar pasta se não existir
        if not os.path.exists(pasta_historico):
            os.makedirs(pasta_historico)
    
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
            
            # Filtro por texto (busca em nome do devedor)
            if filtros.get('texto'):
                texto_busca = filtros['texto'].lower()
                nome_devedor = acionamento['informacoes'].get('Nome do Devedor', '').lower()
                if texto_busca not in nome_devedor:
                    incluir = False
            
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
