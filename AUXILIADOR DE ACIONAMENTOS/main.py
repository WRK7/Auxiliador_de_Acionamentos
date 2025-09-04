import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
import re
from datetime import datetime
import pyperclip
from config import CARTEIRAS, TIPOS_ACIONAMENTO, CAMPOS_INFO, MODELOS_ACIONAMENTO, CAMPOS_OBRIGATORIOS, FORMATACAO_AUTOMATICA, PRAZO_MAXIMO_POR_CARTEIRA, TIPOS_POR_CARTEIRA, CAMPOS_POR_TIPO
from validators import Validator
from historico import HistoricoManager
from historico_ui import HistoricoUI

# Tema minimalista escuro
DARK_THEME = {
    'bg_primary': '#1a1a1a',      # Fundo principal escuro
    'bg_secondary': '#2d2d2d',    # Fundo secundário
    'bg_tertiary': '#3a3a3a',     # Fundo terciário
    'surface': '#404040',         # Superfície de elementos
    'border': '#555555',          # Bordas
    'text_primary': '#ffffff',    # Texto principal
    'text_secondary': '#b3b3b3',  # Texto secundário
    'text_muted': '#888888',      # Texto desabilitado
    'accent': '#6b7280',          # Cor de destaque
    'success': '#10b981',         # Verde sucesso
    'success_bg': '#e8f5e8',      # Fundo verde sucesso
    'warning': '#f59e0b',         # Amarelo aviso
    'danger': '#ef4444',          # Vermelho perigo
    'danger_bg': '#ffeaea',       # Fundo vermelho erro
    'hover': '#4a4a4a'            # Estado hover
}

class AcionamentoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Acionamentos")
        self.root.geometry("900x700")
        self.root.configure(bg=DARK_THEME['bg_primary'])
        self.root.resizable(True, True)
        
        # Configurar tema escuro
        self.setup_dark_theme()
        
        # Dados importados do arquivo config.py
        self.carteiras = CARTEIRAS
        self.tipos_acionamento = TIPOS_ACIONAMENTO
        self.campos_info = CAMPOS_INFO.copy()  # Usar copy() para não modificar o original
        
        # Inicializar gerenciador de histórico
        self.historico_manager = HistoricoManager()
        
        # Não carregar configurações - dados fixos
        self.criar_interface()
        
        # Configurar atalhos de teclado (após criar a interface)
        self.setup_keyboard_shortcuts()
    
    def setup_keyboard_shortcuts(self):
        """Configura atalhos de teclado para melhor produtividade"""
        # F5 - Atualizar/Regenerar modelo
        self.root.bind('<F5>', lambda e: self.gerar_modelo())
        
        # Ctrl+H - Abrir histórico
        self.root.bind('<Control-h>', lambda e: self.abrir_historico())
        
        # Ctrl+N - Novo (limpar campos)
        self.root.bind('<Control-n>', lambda e: self.limpar_campos())
        
        # Ctrl+C - Copiar modelo (apenas quando foco estiver no texto do modelo)
        self.texto_modelo.bind('<Control-c>', lambda e: self.copiar_modelo())
        
        # Ctrl+S - Salvar (gerar e copiar)
        self.root.bind('<Control-s>', lambda e: self.gerar_e_copiar())
        
        # Escape - Fechar janelas abertas
        self.root.bind('<Escape>', lambda e: self.fechar_janelas_secundarias())
        
        # F1 - Ajuda
        self.root.bind('<F1>', lambda e: self.mostrar_ajuda())
    
    def setup_dark_theme(self):
        """Configura o tema escuro minimalista"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar estilos para widgets
        style.configure('Dark.TCombobox',
                       fieldbackground=DARK_THEME['surface'],
                       background=DARK_THEME['surface'],
                       foreground=DARK_THEME['text_primary'],
                       borderwidth=1,
                       relief='solid',
                       bordercolor=DARK_THEME['border'])
        
        style.configure('Dark.TLabelframe',
                       background=DARK_THEME['bg_secondary'],
                       borderwidth=1,
                       relief='flat',
                       bordercolor=DARK_THEME['border'])
        
        style.configure('Dark.TLabelframe.Label',
                       background=DARK_THEME['bg_secondary'],
                       foreground=DARK_THEME['text_primary'],
                       font=('Segoe UI', 11, 'bold'))
    
    def create_minimal_button(self, parent, text, command, color, width=None, height=None):
        """Cria botão minimalista"""
        btn = tk.Button(parent, text=text, command=command,
                       bg=color, fg=DARK_THEME['text_primary'], 
                       font=('Segoe UI', 9),
                       relief='flat', bd=0,
                       cursor='hand2',
                       width=width, height=height,
                       activebackground=DARK_THEME['hover'])
        btn.pack(side='left', padx=2)
        return btn
        
    # Métodos de validação e formatação
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
        elif campo in CAMPOS_OBRIGATORIOS:
            if len(valor.strip()) > 0:
                return True, "Campo preenchido"
            else:
                return False, "Campo obrigatório"
        
        return True, "Campo válido"
    
    def criar_tooltip(self, widget, texto):
        """Cria um tooltip para o widget"""
        def mostrar_tooltip(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            
            label = tk.Label(tooltip, text=texto, 
                           bg=DARK_THEME['surface'], 
                           fg=DARK_THEME['text_primary'],
                           font=('Segoe UI', 9),
                           relief='solid', bd=1,
                           padx=8, pady=4)
            label.pack()
            
            # Fechar tooltip após 3 segundos
            tooltip.after(3000, tooltip.destroy)
            
            # Fechar tooltip ao mover o mouse
            def fechar_tooltip(event):
                tooltip.destroy()
            
            widget.bind('<Leave>', lambda e: tooltip.destroy())
        
        widget.bind('<Enter>', mostrar_tooltip)
    
    def revalidar_data_vencimento(self, event=None):
        """Revalida a data de vencimento e atualiza tipos quando a carteira é alterada"""
        # Atualizar label do prazo máximo
        carteira_atual = self.carteira_var.get()
        if carteira_atual and hasattr(self, 'prazo_label'):
            prazo_maximo = PRAZO_MAXIMO_POR_CARTEIRA.get(carteira_atual, 7)
            self.prazo_label.config(text=f"Máx: {prazo_maximo} dias")
        
        # Atualizar tipos de acionamento baseado na carteira
        self.atualizar_tipos_por_carteira(carteira_atual)
        
        if "Data de Vencimento" in self.campos_entries:
            entry = self.campos_entries["Data de Vencimento"]
            valor = entry.get()
            
            # Ignorar placeholder na revalidação
            if valor == "DD/MM/AAAA":
                valor = ""
            
            if valor.strip():
                # Revalidar o campo
                if self.validar_campo("Data de Vencimento", valor):
                    # Encontrar o label de status e atualizar
                    for widget in entry.master.winfo_children():
                        if isinstance(widget, tk.Label) and widget.cget('text') in ['✓', '✗']:
                            widget.config(text="✓", fg=DARK_THEME['success'])
                            break
                else:
                    # Encontrar o label de status e atualizar
                    for widget in entry.master.winfo_children():
                        if isinstance(widget, tk.Label) and widget.cget('text') in ['✓', '✗']:
                            widget.config(text="✗", fg=DARK_THEME['danger'])
                            break
            else:
                # Limpar status se campo estiver vazio
                for widget in entry.master.winfo_children():
                    if isinstance(widget, tk.Label) and widget.cget('text') in ['✓', '✗']:
                        widget.config(text="", fg=DARK_THEME['text_primary'])
                        break
    
    def atualizar_tipos_por_carteira(self, carteira):
        """Atualiza os tipos de acionamento baseado na carteira selecionada"""
        if carteira and carteira in TIPOS_POR_CARTEIRA:
            # Obter tipos específicos da carteira
            tipos_carteira = TIPOS_POR_CARTEIRA[carteira]
            
            # Atualizar valores do combobox
            self.tipo_combo['values'] = tipos_carteira
            
            # Limpar seleção atual
            self.tipo_var.set("")
            
            # Atualizar campos (mostrar todos quando não há tipo selecionado)
            self.atualizar_campos_por_tipo()
            
            # Gerar modelo se houver tipos disponíveis
            if tipos_carteira:
                self.gerar_modelo()
        else:
            # Se não há carteira selecionada, mostrar todos os tipos
            self.tipo_combo['values'] = self.tipos_acionamento
            self.tipo_var.set("")
            self.atualizar_campos_por_tipo()
            self.gerar_modelo()
    
    def atualizar_campos_por_tipo(self):
        """Atualiza os campos visíveis baseado no tipo de acionamento selecionado"""
        carteira = self.carteira_var.get()
        tipo_selecionado = self.tipo_var.get()
        
        if not carteira or not tipo_selecionado:
            self.mostrar_instrucao_campos()
            return
        
        if tipo_selecionado in CAMPOS_POR_TIPO:
            # Obter campos específicos para o tipo na ordem correta
            campos_necessarios = CAMPOS_POR_TIPO[tipo_selecionado]
            
            # Esconder todos os campos existentes
            for widget in self.campos_container.winfo_children():
                widget.pack_forget()
            
            # Mostrar apenas os campos necessários
            for campo in campos_necessarios:
                if campo in self.campos_entries:
                    # Campo já existe, apenas mostrar
                    self.campos_frames[campo].pack(fill='x', pady=4)
                else:
                    # Campo não existe, criar
                    valor_inicial = self.campos_info.get(campo, "")
                    entry, status_label = self.criar_campo_com_validacao(self.campos_container, campo, valor_inicial)
                    self.campos_entries[campo] = entry
                    self.campos_frames[campo].pack(fill='x', pady=4)
        else:
            self.mostrar_instrucao_campos()
    
    def atualizar_modelo_por_tipo(self, event=None):
        """Atualiza o modelo e campos quando o tipo de acionamento é alterado"""
        # Atualizar campos baseado no tipo selecionado
        self.atualizar_campos_por_tipo()
        # Gerar modelo automaticamente quando tipo é alterado (sem popup)
        self.gerar_modelo(mostrar_popup=False)
    
    def criar_campo_com_validacao(self, parent, campo, valor):
        """Cria um campo de entrada com validação automática"""
        row_frame = tk.Frame(parent, bg=DARK_THEME['bg_secondary'])
        row_frame.pack(fill='x', pady=4)
        
        # Armazenar referência ao frame para controle de visibilidade
        self.campos_frames[campo] = row_frame
        
        # Label do campo
        label = tk.Label(row_frame, text=f"{campo}:", width=20, anchor='w',
                        font=('Segoe UI', 10), 
                        bg=DARK_THEME['bg_secondary'], 
                        fg=DARK_THEME['text_primary'])
        label.pack(side='left')
        
        # Campo obrigatório - adicionar asterisco
        if campo in CAMPOS_OBRIGATORIOS:
            label.config(text=f"{campo} *:", fg=DARK_THEME['danger'])
        
        # Entry com validação - tamanho específico para data
        if campo == "Data de Vencimento":
            entry_width = 15  # Menor para data
        else:
            entry_width = 45  # Normal para outros campos
            
        entry = tk.Entry(row_frame, font=('Segoe UI', 10), width=entry_width,
                        bg=DARK_THEME['surface'], fg=DARK_THEME['text_primary'],
                        relief='flat', bd=1, insertbackground=DARK_THEME['text_primary'],
                        highlightthickness=1, highlightcolor=DARK_THEME['accent'],
                        highlightbackground=DARK_THEME['border'])
        entry.pack(side='left', padx=(15, 10))
        
        # Label dinâmico para prazo máximo (apenas para data de vencimento)
        if campo == "Data de Vencimento":
            self.prazo_label = tk.Label(row_frame, text="", 
                                       font=('Segoe UI', 8), 
                                       bg=DARK_THEME['bg_secondary'], 
                                       fg=DARK_THEME['warning'])
            self.prazo_label.pack(side='left', padx=(5, 0))
        
        # Adicionar placeholder para data de vencimento
        if campo == "Data de Vencimento":
            entry.insert(0, "DD/MM/AAAA")
            entry.config(fg=DARK_THEME['text_muted'])
            
            # Função para gerenciar placeholder
            def on_focus_in(event):
                if entry.get() == "DD/MM/AAAA":
                    entry.delete(0, tk.END)
                    entry.config(fg=DARK_THEME['text_primary'])
            
            def on_focus_out(event):
                if not entry.get().strip():
                    entry.insert(0, "DD/MM/AAAA")
                    entry.config(fg=DARK_THEME['text_muted'])
            
            entry.bind('<FocusIn>', on_focus_in)
            entry.bind('<FocusOut>', on_focus_out)
        else:
            entry.insert(0, valor)
        
        # Label de status da validação
        status_label = tk.Label(row_frame, text="", width=3, 
                               bg=DARK_THEME['bg_secondary'])
        status_label.pack(side='left')
        
        # Função para validar em tempo real
        def validar_tempo_real(event=None):
            valor_atual = entry.get()
            
            # Ignorar placeholder na validação
            if campo == "Data de Vencimento" and valor_atual == "DD/MM/AAAA":
                status_label.config(text="", fg=DARK_THEME['text_primary'])
                entry.config(bg=DARK_THEME['surface'], fg=DARK_THEME['text_primary'])
                label.config(fg=DARK_THEME['text_primary'])
                return
            
            # Resetar cor de fundo se campo estiver vazio
            if not valor_atual.strip():
                status_label.config(text="", fg=DARK_THEME['text_primary'])
                entry.config(bg=DARK_THEME['surface'], fg=DARK_THEME['text_primary'])
                label.config(fg=DARK_THEME['text_primary'])
                return
            
            # Validar campo e obter mensagem específica
            valido, mensagem = self.validar_campo_com_mensagem(campo, valor_atual)
            
            if valido:
                status_label.config(text="✓", fg=DARK_THEME['success'])
                # Mudar cor de fundo e texto do campo para sucesso
                entry.config(bg=DARK_THEME['success_bg'], fg='#2d5a2d')
                # Mudar cor do label para sucesso
                label.config(fg=DARK_THEME['success'])
                # Tooltip com mensagem de sucesso
                self.criar_tooltip(status_label, mensagem)
            else:
                status_label.config(text="✗", fg=DARK_THEME['danger'])
                # Mudar cor de fundo e texto do campo para erro
                entry.config(bg=DARK_THEME['danger_bg'], fg='#8b0000')
                # Mudar cor do label para erro
                label.config(fg=DARK_THEME['danger'])
                # Tooltip com mensagem de erro
                self.criar_tooltip(status_label, mensagem)
        
        # Função para aplicar formatação apenas no FocusOut
        def aplicar_formatacao(event=None):
            valor_atual = entry.get()
            
            # Não aplicar formatação no placeholder
            if campo == "Data de Vencimento" and valor_atual == "DD/MM/AAAA":
                return
            
            valor_formatado = self.aplicar_formatacao_automatica(campo, valor_atual)
            if valor_formatado != valor_atual:
                entry.delete(0, tk.END)
                entry.insert(0, valor_formatado)
            validar_tempo_real()
        
        
        # Função para limitar entrada de dados
        def limitar_entrada(event):
            # Permitir teclas de controle (backspace, delete, setas, etc.)
            if event.keysym in ['BackSpace', 'Delete', 'Left', 'Right', 'Up', 'Down', 'Tab', 'Return']:
                return None
            
            if campo == "Data de Vencimento":
                # Permitir apenas números
                if not event.char.isdigit():
                    return 'break'
                # Verificar se já tem 8 dígitos
                valor_atual = entry.get()
                numeros = re.sub(r'[^0-9]', '', valor_atual)
                if len(numeros) >= 8:
                    return 'break'
            
            elif campo == "CPF/CNPJ":
                # Permitir apenas números
                if not event.char.isdigit():
                    return 'break'
                # Verificar se já tem 14 dígitos
                valor_atual = entry.get()
                numeros = re.sub(r'[^0-9]', '', valor_atual)
                if len(numeros) >= 14:
                    return 'break'
            
            return None  # Permite entrada normal para outros campos
        
        # Bind eventos
        entry.bind('<KeyPress>', limitar_entrada)
        entry.bind('<KeyRelease>', validar_tempo_real)
        entry.bind('<FocusOut>', aplicar_formatacao)
        
        # Validar inicialmente
        validar_tempo_real()
        
        return entry, status_label
    
    def criar_interface(self):
        """Cria a interface principal com sidebar"""
        # Header minimalista
        header_frame = tk.Frame(self.root, bg=DARK_THEME['bg_secondary'], height=60)
        header_frame.pack(fill='x', pady=(0, 20))
        header_frame.pack_propagate(False)
        
        # Título minimalista
        titulo = tk.Label(header_frame, text="Gerador de Acionamentos", 
                         font=('Segoe UI', 18, 'bold'), 
                         bg=DARK_THEME['bg_secondary'], 
                         fg=DARK_THEME['text_primary'])
        titulo.pack(expand=True)
        
        # Subtítulo discreto
        subtitulo = tk.Label(header_frame, text="Interface minimalista para criação de documentos", 
                           font=('Segoe UI', 9), 
                           bg=DARK_THEME['bg_secondary'], 
                           fg=DARK_THEME['text_secondary'])
        subtitulo.pack()
        
        # Container principal com layout horizontal
        main_container = tk.Frame(self.root, bg=DARK_THEME['bg_primary'])
        main_container.pack(expand=True, fill='both', padx=20, pady=(0, 20))
        
        # SIDEBAR - Lado esquerdo
        sidebar_frame = tk.Frame(main_container, bg=DARK_THEME['bg_secondary'], 
                                relief='flat', bd=1, width=400)
        sidebar_frame.pack(side='left', fill='y', padx=(0, 15))
        sidebar_frame.pack_propagate(False)  # Manter largura fixa
        
        # Frame de seleções no sidebar
        selecoes_frame = tk.LabelFrame(sidebar_frame, text="Configurações", 
                                      font=('Segoe UI', 11, 'bold'), 
                                      bg=DARK_THEME['bg_secondary'],
                                      fg=DARK_THEME['text_primary'],
                                      relief='flat',
                                      bd=1)
        selecoes_frame.pack(fill='x', padx=15, pady=15)
        
        # Seleção de Carteira
        carteira_frame = tk.Frame(selecoes_frame, bg=DARK_THEME['bg_secondary'])
        carteira_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Label(carteira_frame, text="Carteira:", font=('Segoe UI', 10), 
                bg=DARK_THEME['bg_secondary'], fg=DARK_THEME['text_primary']).pack(side='left')
        
        self.carteira_var = tk.StringVar()
        self.carteira_combo = ttk.Combobox(carteira_frame, textvariable=self.carteira_var,
                                          values=self.carteiras, state='readonly', width=25,
                                          style='Dark.TCombobox')
        self.carteira_combo.pack(side='left', padx=(15, 10))
        self.carteira_combo.bind('<<ComboboxSelected>>', self.revalidar_data_vencimento)
        
        # Botões removidos - carteiras são fixas
        
        # Seleção de Tipo de Acionamento
        tipo_frame = tk.Frame(selecoes_frame, bg=DARK_THEME['bg_secondary'])
        tipo_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Label(tipo_frame, text="Tipo:", font=('Segoe UI', 10), 
                bg=DARK_THEME['bg_secondary'], fg=DARK_THEME['text_primary']).pack(side='left')
        
        self.tipo_var = tk.StringVar()
        self.tipo_combo = ttk.Combobox(tipo_frame, textvariable=self.tipo_var,
                                      values=self.tipos_acionamento, state='readonly', width=25,
                                      style='Dark.TCombobox')
        self.tipo_combo.pack(side='left', padx=(15, 10))
        self.tipo_combo.bind('<<ComboboxSelected>>', self.atualizar_modelo_por_tipo)
        
        # Botões removidos - tipos são fixos
        
        # Frame de campos no sidebar
        campos_frame = tk.LabelFrame(sidebar_frame, text="Campos de Entrada", 
                                   font=('Segoe UI', 11, 'bold'), 
                                   bg=DARK_THEME['bg_secondary'],
                                   fg=DARK_THEME['text_primary'],
                                   relief='flat',
                                   bd=1)
        campos_frame.pack(fill='both', expand=True, padx=15, pady=(0, 15))
        
        # Campos de entrada
        self.campos_entries = {}
        self.campos_frames = {}
        
        # Canvas para scroll no sidebar
        self.campos_canvas = tk.Canvas(campos_frame, bg=DARK_THEME['bg_secondary'], highlightthickness=0)
        self.campos_scrollbar = ttk.Scrollbar(campos_frame, orient="vertical", command=self.campos_canvas.yview)
        self.campos_scrollable_frame = tk.Frame(self.campos_canvas, bg=DARK_THEME['bg_secondary'])
        
        self.campos_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.campos_canvas.configure(scrollregion=self.campos_canvas.bbox("all"))
        )
        
        self.campos_canvas.create_window((0, 0), window=self.campos_scrollable_frame, anchor="nw")
        self.campos_canvas.configure(yscrollcommand=self.campos_scrollbar.set)
        
        # Container dos campos (agora dentro do frame scrollável)
        self.campos_container = self.campos_scrollable_frame
        
        # Pack canvas e scrollbar
        self.campos_canvas.pack(side="left", fill="both", expand=True, padx=15, pady=15)
        self.campos_scrollbar.pack(side="right", fill="y", pady=15)
        
        # Bind mouse wheel para scroll
        def _on_mousewheel(event):
            self.campos_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.campos_canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Inicializar com mensagem de instrução
        self.mostrar_instrucao_campos()
        
        # Botão removido - campos são fixos
        
        # CONTEÚDO PRINCIPAL - Lado direito
        main_content_frame = tk.Frame(main_container, bg=DARK_THEME['bg_secondary'],
                                     relief='flat', bd=1)
        main_content_frame.pack(side='right', fill='both', expand=True)
        
        # Frame de resultado
        resultado_frame = tk.LabelFrame(main_content_frame, text="Modelo de Acionamento", 
                                      font=('Segoe UI', 11, 'bold'), 
                                      bg=DARK_THEME['bg_secondary'],
                                      fg=DARK_THEME['text_primary'],
                                      relief='flat',
                                      bd=1)
        resultado_frame.pack(fill='both', expand=True, padx=15, pady=15)
        
        # Texto do modelo
        self.texto_modelo = tk.Text(resultado_frame, height=10, font=('Consolas', 10),
                                   wrap='word', bg=DARK_THEME['surface'],
                                   fg=DARK_THEME['text_primary'],
                                   relief='flat', bd=1, insertbackground=DARK_THEME['text_primary'],
                                   highlightthickness=1, highlightcolor=DARK_THEME['accent'],
                                   highlightbackground=DARK_THEME['border'])
        scrollbar = tk.Scrollbar(resultado_frame, orient='vertical', command=self.texto_modelo.yview,
                               bg=DARK_THEME['border'], troughcolor=DARK_THEME['bg_secondary'])
        self.texto_modelo.configure(yscrollcommand=scrollbar.set)
        
        self.texto_modelo.pack(side='left', fill='both', expand=True, padx=(15, 0), pady=15)
        scrollbar.pack(side='right', fill='y', pady=15)
        
        # Botões de ação
        botoes_frame = tk.Frame(main_content_frame, bg=DARK_THEME['bg_primary'])
        botoes_frame.pack(fill='x', pady=15)
        
        # Botão Gerar Modelo
        gerar_btn = tk.Button(botoes_frame, text="Gerar Modelo", command=self.gerar_modelo,
                             bg=DARK_THEME['accent'], fg=DARK_THEME['text_primary'], 
                             font=('Segoe UI', 10, 'bold'),
                             relief='flat', bd=0, cursor='hand2',
                             padx=20, pady=12,
                             activebackground=DARK_THEME['hover'])
        gerar_btn.pack(side='left', padx=(0, 12))
        
        # Botão Copiar
        copiar_btn = tk.Button(botoes_frame, text="Copiar", command=self.copiar_modelo,
                              bg=DARK_THEME['success'], fg=DARK_THEME['text_primary'], 
                              font=('Segoe UI', 10, 'bold'),
                              relief='flat', bd=0, cursor='hand2',
                              padx=20, pady=12,
                              activebackground=DARK_THEME['hover'])
        copiar_btn.pack(side='left', padx=(0, 12))
        
        # Botão Limpar
        limpar_btn = tk.Button(botoes_frame, text="Limpar", command=self.limpar_campos,
                              bg=DARK_THEME['warning'], fg=DARK_THEME['text_primary'], 
                              font=('Segoe UI', 10, 'bold'),
                              relief='flat', bd=0, cursor='hand2',
                              padx=20, pady=12,
                              activebackground=DARK_THEME['hover'])
        limpar_btn.pack(side='left', padx=(0, 12))
        
        # Botão Histórico
        historico_btn = tk.Button(botoes_frame, text="📋 Histórico", command=self.abrir_historico,
                                 bg=DARK_THEME['accent'], fg=DARK_THEME['text_primary'], 
                                 font=('Segoe UI', 10, 'bold'),
                                 relief='flat', bd=0, cursor='hand2',
                                 padx=20, pady=12,
                                 activebackground=DARK_THEME['hover'])
        historico_btn.pack(side='left', padx=(0, 12))
        
        # Botão Ajuda
        ajuda_btn = tk.Button(botoes_frame, text="❓ Ajuda", command=self.mostrar_ajuda,
                             bg=DARK_THEME['text_muted'], fg=DARK_THEME['text_primary'], 
                             font=('Segoe UI', 10, 'bold'),
                             relief='flat', bd=0, cursor='hand2',
                             padx=20, pady=8,
                             activebackground=DARK_THEME['hover'])
        ajuda_btn.pack(side='left')
        
        # Atualizar modelo inicial
        self.gerar_modelo()
    
    def mostrar_instrucao_campos(self):
        """Mostra instrução para selecionar carteira e tipo"""
        # Limpar campos existentes
        for widget in self.campos_container.winfo_children():
            widget.destroy()
        
        self.campos_entries = {}
        self.campos_frames = {}
        
        # Mostrar instrução
        instrucao = tk.Label(self.campos_container, 
                            text="Selecione uma carteira e um tipo de acionamento para ver os campos necessários.",
                            font=('Segoe UI', 11), 
                            bg=DARK_THEME['bg_secondary'], 
                            fg=DARK_THEME['text_muted'])
        instrucao.pack(expand=True)
    
    # Métodos de adicionar/remover elementos removidos - dados são fixos
    
    def gerar_modelo(self, mostrar_popup=True):
        """Gera o modelo de acionamento baseado nas seleções"""
        carteira = self.carteira_var.get()
        tipo = self.tipo_var.get()
        
        if not carteira or not tipo:
            self.texto_modelo.delete(1.0, tk.END)
            self.texto_modelo.insert(1.0, "Por favor, selecione uma carteira e um tipo de acionamento.")
            return
        
        # Coletar informações preenchidas
        informacoes = {}
        campos_invalidos = []
        
        for campo, entry in self.campos_entries.items():
            valor = entry.get().strip()
            
            # Ignorar placeholder na coleta de dados
            if campo == "Data de Vencimento" and valor == "DD/MM/AAAA":
                valor = ""
            
            informacoes[campo] = valor
            
            # Validar campos obrigatórios
            if campo in CAMPOS_OBRIGATORIOS and not valor:
                campos_invalidos.append(f"{campo} (obrigatório)")
            
            # Validar campos específicos
            elif valor and not self.validar_campo(campo, valor):
                if campo == "CPF/CNPJ":
                    tipo_doc = Validator.obter_tipo_documento(valor)
                    campos_invalidos.append(f"{campo} ({tipo_doc} inválido)")
                elif campo == "Data de Vencimento":
                    # Mensagem específica para data de vencimento
                    carteira_atual = self.carteira_var.get()
                    if carteira_atual:
                        valido, mensagem = Validator.validar_data_vencimento(valor, carteira_atual, PRAZO_MAXIMO_POR_CARTEIRA)
                        campos_invalidos.append(f"{campo} ({mensagem})")
                    else:
                        campos_invalidos.append(f"{campo} (formato inválido)")
                else:
                    campos_invalidos.append(f"{campo} (inválido)")
        
        # Verificar se há campos inválidos
        if campos_invalidos:
            mensagem = "Por favor, corrija os seguintes campos:\n\n" + "\n".join(f"• {campo}" for campo in campos_invalidos)
            self.texto_modelo.delete(1.0, tk.END)
            self.texto_modelo.insert(1.0, mensagem)
            if mostrar_popup:
                messagebox.showwarning("Campos Inválidos", mensagem)
            return
        
        # Gerar modelo baseado no tipo
        modelo = self.criar_modelo_acionamento(carteira, tipo, informacoes)
        
        # Salvar no histórico
        id_acionamento = self.historico_manager.salvar_acionamento(carteira, tipo, informacoes, modelo)
        
        self.texto_modelo.delete(1.0, tk.END)
        self.texto_modelo.insert(1.0, modelo)
    
    def criar_modelo_acionamento(self, carteira, tipo, informacoes):
        """Cria o modelo específico baseado no tipo de acionamento"""
        data_atual = datetime.now().strftime("%d/%m/%Y")
        
        modelo = f"""
=== ACIONAMENTO - {tipo} ===
Carteira: {carteira}
Data: {data_atual}

"""
        
        # Adicionar apenas informações preenchidas (sem duplicação)
        for campo, valor in informacoes.items():
            if valor:  # Só adicionar campos que têm valor
                modelo += f"{campo}: {valor}\n"
        
        return modelo.strip()
    
    def copiar_modelo(self):
        """Copia apenas os dados preenchidos para a área de transferência"""
        texto = self.texto_modelo.get(1.0, tk.END).strip()
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
    
    def limpar_campos(self):
        """Limpa todos os campos"""
        if messagebox.askyesno("Confirmar", "Deseja limpar todos os campos?"):
            self.carteira_var.set("")
            self.tipo_var.set("")
            
            # Limpar campos de entrada se existirem
            if hasattr(self, 'campos_entries'):
                for entry in self.campos_entries.values():
                    entry.delete(0, tk.END)
            
            # Limpar texto do modelo
            self.texto_modelo.delete(1.0, tk.END)
            
            # Mostrar instrução novamente
            self.mostrar_instrucao_campos()
    
    def abrir_historico(self):
        """Abre a janela do histórico"""
        try:
            HistoricoUI(self.root)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir histórico: {e}")
    
    def gerar_e_copiar(self):
        """Gera o modelo e copia automaticamente (Ctrl+S)"""
        self.gerar_modelo()
        self.copiar_modelo()
    
    def fechar_janelas_secundarias(self):
        """Fecha janelas secundárias abertas (Escape)"""
        # Fechar janelas de histórico se estiverem abertas
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Toplevel):
                widget.destroy()
    
    def mostrar_ajuda(self):
        """Mostra janela de ajuda com atalhos (F1)"""
        ajuda_janela = tk.Toplevel(self.root)
        ajuda_janela.title("Ajuda - Atalhos de Teclado")
        ajuda_janela.geometry("500x400")
        ajuda_janela.configure(bg=DARK_THEME['bg_primary'])
        ajuda_janela.resizable(False, False)
        
        # Centralizar janela
        ajuda_janela.transient(self.root)
        ajuda_janela.grab_set()
        
        # Frame principal
        main_frame = tk.Frame(ajuda_janela, bg=DARK_THEME['bg_primary'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Título
        titulo = tk.Label(main_frame, text="⌨️ Atalhos de Teclado", 
                         font=('Segoe UI', 16, 'bold'), 
                         bg=DARK_THEME['bg_primary'], 
                         fg=DARK_THEME['text_primary'])
        titulo.pack(pady=(0, 20))
        
        # Lista de atalhos
        atalhos = [
            ("F5", "Atualizar/Regenerar modelo"),
            ("Ctrl + H", "Abrir histórico"),
            ("Ctrl + N", "Novo (limpar campos)"),
            ("Ctrl + C", "Copiar modelo"),
            ("Ctrl + S", "Gerar e copiar automaticamente"),
            ("Escape", "Fechar janelas abertas"),
            ("F1", "Mostrar esta ajuda")
        ]
        
        for atalho, descricao in atalhos:
            frame = tk.Frame(main_frame, bg=DARK_THEME['bg_primary'])
            frame.pack(fill='x', pady=5)
            
            # Atalho
            atalho_label = tk.Label(frame, text=atalho, 
                                   font=('Consolas', 12, 'bold'), 
                                   bg=DARK_THEME['bg_primary'], 
                                   fg=DARK_THEME['accent'],
                                   width=15, anchor='w')
            atalho_label.pack(side='left')
            
            # Descrição
            desc_label = tk.Label(frame, text=descricao, 
                                 font=('Segoe UI', 11), 
                                 bg=DARK_THEME['bg_primary'], 
                                 fg=DARK_THEME['text_primary'],
                                 anchor='w')
            desc_label.pack(side='left', padx=(10, 0))
        
        # Botão fechar
        fechar_btn = tk.Button(main_frame, text="Fechar", 
                              command=ajuda_janela.destroy,
                              bg=DARK_THEME['accent'], 
                              fg=DARK_THEME['text_primary'],
                              font=('Segoe UI', 10, 'bold'),
                              relief='flat', bd=0, cursor='hand2',
                              padx=20, pady=12,
                              activebackground=DARK_THEME['hover'])
        fechar_btn.pack(pady=(20, 0))

def main():
    root = tk.Tk()
    app = AcionamentoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
