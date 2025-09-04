# Interface do Histórico de Acionamentos
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from historico import HistoricoManager

class HistoricoUI:
    """Interface para visualizar e gerenciar o histórico"""
    
    def __init__(self, parent, callback_duplicar=None):
        self.parent = parent
        self.callback_duplicar = callback_duplicar
        self.historico_manager = HistoricoManager()
        
        # Cores do tema escuro
        self.colors = {
            'bg_primary': '#1a1a1a',
            'bg_secondary': '#2d2d2d',
            'bg_tertiary': '#3a3a3a',
            'surface': '#404040',
            'border': '#555555',
            'text_primary': '#ffffff',
            'text_secondary': '#b3b3b3',
            'text_muted': '#888888',
            'accent': '#6b7280',
            'success': '#10b981',
            'warning': '#f59e0b',
            'danger': '#ef4444',
            'hover': '#4a4a4a'
        }
        
        self.criar_interface()
        self.carregar_dados()
    
    def criar_interface(self):
        """Cria a interface do histórico"""
        # Janela principal
        self.janela = tk.Toplevel(self.parent)
        self.janela.title("Histórico de Acionamentos")
        self.janela.geometry("1000x700")
        self.janela.configure(bg=self.colors['bg_primary'])
        self.janela.resizable(True, True)
        
        # Header
        header_frame = tk.Frame(self.janela, bg=self.colors['bg_secondary'], height=60)
        header_frame.pack(fill='x', pady=(0, 10))
        header_frame.pack_propagate(False)
        
        titulo = tk.Label(header_frame, text="📋 Histórico de Acionamentos", 
                         font=('Segoe UI', 16, 'bold'), 
                         bg=self.colors['bg_secondary'], 
                         fg=self.colors['text_primary'])
        titulo.pack(expand=True)
        
        # Frame principal
        main_frame = tk.Frame(self.janela, bg=self.colors['bg_primary'])
        main_frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Frame de filtros
        self.criar_frame_filtros(main_frame)
        
        # Frame da tabela
        self.criar_frame_tabela(main_frame)
        
        # Frame de botões
        self.criar_frame_botoes(main_frame)
    
    def criar_frame_filtros(self, parent):
        """Cria o frame de filtros"""
        filtros_frame = tk.LabelFrame(parent, text="🔍 Filtros e Busca", 
                                     font=('Segoe UI', 11, 'bold'), 
                                     bg=self.colors['bg_secondary'],
                                     fg=self.colors['text_primary'],
                                     relief='flat', bd=1)
        filtros_frame.pack(fill='x', pady=(0, 10))
        
        # Primeira linha de filtros
        linha1 = tk.Frame(filtros_frame, bg=self.colors['bg_secondary'])
        linha1.pack(fill='x', padx=15, pady=10)
        
        # Busca por texto
        tk.Label(linha1, text="Buscar:", font=('Segoe UI', 10), 
                bg=self.colors['bg_secondary'], fg=self.colors['text_primary']).pack(side='left')
        
        self.entry_busca = tk.Entry(linha1, font=('Segoe UI', 10), width=20,
                                   bg=self.colors['surface'], fg=self.colors['text_primary'],
                                   relief='flat', bd=1)
        self.entry_busca.pack(side='left', padx=(10, 5))
        self.entry_busca.bind('<KeyRelease>', self.aplicar_filtros)
        
        # Filtro por carteira
        tk.Label(linha1, text="Carteira:", font=('Segoe UI', 10), 
                bg=self.colors['bg_secondary'], fg=self.colors['text_primary']).pack(side='left', padx=(20, 0))
        
        self.combo_carteira = ttk.Combobox(linha1, width=15, state='readonly')
        self.combo_carteira.pack(side='left', padx=(10, 5))
        self.combo_carteira.bind('<<ComboboxSelected>>', self.aplicar_filtros)
        
        # Filtro por tipo
        tk.Label(linha1, text="Tipo:", font=('Segoe UI', 10), 
                bg=self.colors['bg_secondary'], fg=self.colors['text_primary']).pack(side='left', padx=(20, 0))
        
        self.combo_tipo = ttk.Combobox(linha1, width=15, state='readonly')
        self.combo_tipo.pack(side='left', padx=(10, 5))
        self.combo_tipo.bind('<<ComboboxSelected>>', self.aplicar_filtros)
        
        # Segunda linha de filtros
        linha2 = tk.Frame(filtros_frame, bg=self.colors['bg_secondary'])
        linha2.pack(fill='x', padx=15, pady=(0, 10))
        
        # Filtro por período
        tk.Label(linha2, text="Período:", font=('Segoe UI', 10), 
                bg=self.colors['bg_secondary'], fg=self.colors['text_primary']).pack(side='left')
        
        self.combo_periodo = ttk.Combobox(linha2, width=15, state='readonly',
                                         values=["Todos", "Hoje", "Últimos 7 dias", "Últimos 30 dias", "Este mês"])
        self.combo_periodo.pack(side='left', padx=(10, 5))
        self.combo_periodo.set("Últimos 30 dias")
        self.combo_periodo.bind('<<ComboboxSelected>>', self.aplicar_filtros)
        
        # Botões de ação
        tk.Button(linha2, text="🔄 Atualizar", command=self.carregar_dados,
                 bg=self.colors['accent'], fg=self.colors['text_primary'],
                 font=('Segoe UI', 9), relief='flat', bd=0, cursor='hand2',
                 padx=15, pady=5).pack(side='left', padx=(20, 5))
        
        tk.Button(linha2, text="📊 Estatísticas", command=self.mostrar_estatisticas,
                 bg=self.colors['success'], fg=self.colors['text_primary'],
                 font=('Segoe UI', 9), relief='flat', bd=0, cursor='hand2',
                 padx=15, pady=5).pack(side='left', padx=5)
    
    def criar_frame_tabela(self, parent):
        """Cria o frame da tabela"""
        tabela_frame = tk.LabelFrame(parent, text="📋 Lista de Acionamentos", 
                                    font=('Segoe UI', 11, 'bold'), 
                                    bg=self.colors['bg_secondary'],
                                    fg=self.colors['text_primary'],
                                    relief='flat', bd=1)
        tabela_frame.pack(fill='both', expand=True, pady=(0, 10))
        
        # Treeview para a tabela
        colunas = ('ID', 'Data', 'Carteira', 'Tipo', 'Devedor', 'Valor', 'Usuário')
        self.tree = ttk.Treeview(tabela_frame, columns=colunas, show='headings', height=15)
        
        # Configurar colunas
        self.tree.heading('ID', text='ID')
        self.tree.heading('Data', text='Data')
        self.tree.heading('Carteira', text='Carteira')
        self.tree.heading('Tipo', text='Tipo')
        self.tree.heading('Devedor', text='Devedor')
        self.tree.heading('Valor', text='Valor')
        self.tree.heading('Usuário', text='Usuário')
        
        # Configurar larguras
        self.tree.column('ID', width=100)
        self.tree.column('Data', width=120)
        self.tree.column('Carteira', width=120)
        self.tree.column('Tipo', width=150)
        self.tree.column('Devedor', width=200)
        self.tree.column('Valor', width=100)
        self.tree.column('Usuário', width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tabela_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack
        self.tree.pack(side='left', fill='both', expand=True, padx=(15, 0), pady=15)
        scrollbar.pack(side='right', fill='y', pady=15)
        
        # Bind duplo clique
        self.tree.bind('<Double-1>', self.ver_detalhes)
    
    def criar_frame_botoes(self, parent):
        """Cria o frame de botões"""
        botoes_frame = tk.Frame(parent, bg=self.colors['bg_primary'])
        botoes_frame.pack(fill='x')
        
        tk.Button(botoes_frame, text="👁️ Ver Detalhes", command=self.ver_detalhes,
                 bg=self.colors['accent'], fg=self.colors['text_primary'],
                 font=('Segoe UI', 10), relief='flat', bd=0, cursor='hand2',
                 padx=20, pady=8).pack(side='left', padx=(0, 10))
        
        tk.Button(botoes_frame, text="📋 Duplicar", command=self.duplicar_acionamento,
                 bg=self.colors['success'], fg=self.colors['text_primary'],
                 font=('Segoe UI', 10), relief='flat', bd=0, cursor='hand2',
                 padx=20, pady=8).pack(side='left', padx=(0, 10))
        
        tk.Button(botoes_frame, text="🗑️ Excluir", command=self.excluir_acionamento,
                 bg=self.colors['danger'], fg=self.colors['text_primary'],
                 font=('Segoe UI', 10), relief='flat', bd=0, cursor='hand2',
                 padx=20, pady=8).pack(side='left', padx=(0, 10))
        
        tk.Button(botoes_frame, text="📄 Exportar", command=self.exportar_historico,
                 bg=self.colors['warning'], fg=self.colors['text_primary'],
                 font=('Segoe UI', 10), relief='flat', bd=0, cursor='hand2',
                 padx=20, pady=8).pack(side='left', padx=(0, 10))
        
        tk.Button(botoes_frame, text="❌ Fechar", command=self.janela.destroy,
                 bg=self.colors['text_muted'], fg=self.colors['text_primary'],
                 font=('Segoe UI', 10), relief='flat', bd=0, cursor='hand2',
                 padx=20, pady=8).pack(side='right')
    
    def carregar_dados(self):
        """Carrega os dados do histórico"""
        # Carregar histórico
        historico = self.historico_manager.carregar_historico()
        
        # Atualizar combos
        carteiras = list(set([a['carteira'] for a in historico]))
        carteiras.sort()
        carteiras.insert(0, "Todas")
        self.combo_carteira['values'] = carteiras
        self.combo_carteira.set("Todas")
        
        tipos = list(set([a['tipo'].split(' - ')[0] for a in historico]))
        tipos.sort()
        tipos.insert(0, "Todos")
        self.combo_tipo['values'] = tipos
        self.combo_tipo.set("Todos")
        
        # Aplicar filtros
        self.aplicar_filtros()
    
    def aplicar_filtros(self, event=None):
        """Aplica os filtros selecionados"""
        # Obter filtros
        filtros = {}
        
        if self.entry_busca.get().strip():
            filtros['texto'] = self.entry_busca.get().strip()
        
        if self.combo_carteira.get() and self.combo_carteira.get() != "Todas":
            filtros['carteira'] = self.combo_carteira.get()
        
        if self.combo_tipo.get() and self.combo_tipo.get() != "Todos":
            filtros['tipo'] = self.combo_tipo.get()
        
        # Filtro por período
        periodo = self.combo_periodo.get()
        if periodo == "Hoje":
            filtros['data_inicio'] = datetime.now().strftime('%d/%m/%Y')
            filtros['data_fim'] = datetime.now().strftime('%d/%m/%Y')
        elif periodo == "Últimos 7 dias":
            data_inicio = (datetime.now() - timedelta(days=7)).strftime('%d/%m/%Y')
            filtros['data_inicio'] = data_inicio
        elif periodo == "Últimos 30 dias":
            data_inicio = (datetime.now() - timedelta(days=30)).strftime('%d/%m/%Y')
            filtros['data_inicio'] = data_inicio
        elif periodo == "Este mês":
            hoje = datetime.now()
            data_inicio = f"01/{hoje.month:02d}/{hoje.year}"
            filtros['data_inicio'] = data_inicio
        
        # Buscar com filtros
        resultado = self.historico_manager.buscar_acionamentos(filtros)
        
        # Atualizar tabela
        self.atualizar_tabela(resultado)
    
    def atualizar_tabela(self, acionamentos):
        """Atualiza a tabela com os acionamentos"""
        # Limpar tabela
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Adicionar dados
        for acionamento in acionamentos:
            valores = (
                acionamento['id'],
                acionamento['data_criacao'].split(' ')[0],  # Só a data
                acionamento['carteira'],
                acionamento['tipo'].split(' - ')[0],  # Só o tipo
                acionamento['informacoes'].get('Nome do Devedor', ''),
                acionamento['informacoes'].get('Valor da Dívida', ''),
                acionamento['usuario']
            )
            self.tree.insert('', 'end', values=valores, tags=(acionamento['id'],))
    
    def ver_detalhes(self, event=None):
        """Mostra os detalhes do acionamento selecionado"""
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um acionamento para ver os detalhes.")
            return
        
        item = self.tree.item(selecionado[0])
        id_acionamento = item['tags'][0]
        
        # Buscar acionamento completo
        historico = self.historico_manager.carregar_historico()
        acionamento = None
        for a in historico:
            if a['id'] == id_acionamento:
                acionamento = a
                break
        
        if not acionamento:
            messagebox.showerror("Erro", "Acionamento não encontrado.")
            return
        
        # Criar janela de detalhes
        self.mostrar_detalhes(acionamento)
    
    def mostrar_detalhes(self, acionamento):
        """Mostra janela com detalhes do acionamento"""
        detalhes_janela = tk.Toplevel(self.janela)
        detalhes_janela.title(f"Detalhes - {acionamento['id']}")
        detalhes_janela.geometry("600x500")
        detalhes_janela.configure(bg=self.colors['bg_primary'])
        
        # Texto com detalhes
        texto = tk.Text(detalhes_janela, font=('Consolas', 10),
                       bg=self.colors['surface'], fg=self.colors['text_primary'],
                       relief='flat', bd=1, wrap='word')
        texto.pack(fill='both', expand=True, padx=15, pady=15)
        
        # Conteúdo
        conteudo = f"""
=== DETALHES DO ACIONAMENTO ===

ID: {acionamento['id']}
Data de Criação: {acionamento['data_criacao']}
Carteira: {acionamento['carteira']}
Tipo: {acionamento['tipo']}
Usuário: {acionamento['usuario']}
Computador: {acionamento['computador']}

=== INFORMAÇÕES ===
"""
        
        for campo, valor in acionamento['informacoes'].items():
            conteudo += f"{campo}: {valor}\n"
        
        conteudo += f"\n=== MODELO GERADO ===\n{acionamento['modelo_gerado']}"
        
        texto.insert('1.0', conteudo)
        texto.config(state='disabled')
    
    def duplicar_acionamento(self):
        """Duplica o acionamento selecionado"""
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um acionamento para duplicar.")
            return
        
        item = self.tree.item(selecionado[0])
        id_acionamento = item['tags'][0]
        
        # Duplicar acionamento
        dados_duplicados = self.historico_manager.duplicar_acionamento(id_acionamento)
        
        if dados_duplicados and self.callback_duplicar:
            self.callback_duplicar(dados_duplicados)
            self.janela.destroy()
        else:
            messagebox.showerror("Erro", "Não foi possível duplicar o acionamento.")
    
    def excluir_acionamento(self):
        """Exclui o acionamento selecionado"""
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um acionamento para excluir.")
            return
        
        item = self.tree.item(selecionado[0])
        id_acionamento = item['tags'][0]
        
        if messagebox.askyesno("Confirmar", f"Deseja excluir o acionamento {id_acionamento}?"):
            if self.historico_manager.excluir_acionamento(id_acionamento):
                messagebox.showinfo("Sucesso", "Acionamento excluído com sucesso.")
                self.carregar_dados()
            else:
                messagebox.showerror("Erro", "Não foi possível excluir o acionamento.")
    
    def exportar_historico(self):
        """Exporta o histórico para arquivo"""
        # Implementar exportação
        messagebox.showinfo("Info", "Funcionalidade de exportação será implementada em breve.")
    
    def mostrar_estatisticas(self):
        """Mostra estatísticas do histórico"""
        stats = self.historico_manager.obter_estatisticas()
        
        # Criar janela de estatísticas
        stats_janela = tk.Toplevel(self.janela)
        stats_janela.title("Estatísticas do Histórico")
        stats_janela.geometry("500x400")
        stats_janela.configure(bg=self.colors['bg_primary'])
        
        # Texto com estatísticas
        texto = tk.Text(stats_janela, font=('Segoe UI', 10),
                       bg=self.colors['surface'], fg=self.colors['text_primary'],
                       relief='flat', bd=1, wrap='word')
        texto.pack(fill='both', expand=True, padx=15, pady=15)
        
        conteudo = f"""
=== ESTATÍSTICAS DO HISTÓRICO ===

Total de Acionamentos: {stats['total']}

=== POR CARTEIRA ===
"""
        for carteira, quantidade in stats['por_carteira'].items():
            conteudo += f"{carteira}: {quantidade}\n"
        
        conteudo += "\n=== POR TIPO ===\n"
        for tipo, quantidade in stats['por_tipo'].items():
            conteudo += f"{tipo}: {quantidade}\n"
        
        conteudo += "\n=== POR USUÁRIO ===\n"
        for usuario, quantidade in stats['por_usuario'].items():
            conteudo += f"{usuario}: {quantidade}\n"
        
        conteudo += "\n=== POR MÊS ===\n"
        for mes, quantidade in stats['por_mes'].items():
            conteudo += f"{mes}: {quantidade}\n"
        
        texto.insert('1.0', conteudo)
        texto.config(state='disabled')
