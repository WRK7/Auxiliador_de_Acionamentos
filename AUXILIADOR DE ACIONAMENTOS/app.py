"""
Módulo principal da aplicação - classe AcionamentoApp
"""

import tkinter as tk
from tkinter import ttk, messagebox
from config import CARTEIRAS, TIPOS_ACIONAMENTO, CAMPOS_INFO, CAMPOS_OBRIGATORIOS, PRAZO_MAXIMO_POR_CARTEIRA, TIPOS_POR_CARTEIRA, CAMPOS_POR_TIPO
from historico import HistoricoManager
from historico_ui import HistoricoUI
from theme import DARK_THEME, setup_dark_theme
from ui_components import UIComponents
from field_validators import FieldValidators
from model_generator import ModelGenerator

class AcionamentoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Acionamentos")
        self.root.geometry("1000x650")
        self.root.configure(bg=DARK_THEME['bg_primary'])
        self.root.resizable(True, True)
        
        # Configurar tema escuro
        setup_dark_theme()
        
        # Dados importados do arquivo config.py
        self.carteiras = CARTEIRAS
        self.tipos_acionamento = TIPOS_ACIONAMENTO
        self.campos_info = CAMPOS_INFO.copy()  # Usar copy() para não modificar o original
        
        # Inicializar gerenciador de histórico
        self.historico_manager = HistoricoManager()
        
        # Inicializar validadores e gerador de modelo
        self.field_validators = None  # Será inicializado após criar a interface
        self.model_generator = ModelGenerator(self.historico_manager)
        
        # Criar interface
        self.criar_interface()
        
        # Configurar atalhos de teclado (após criar a interface)
        self.setup_keyboard_shortcuts()
    
    def setup_scroll(self):
        """Configura o sistema de scroll para os campos"""
        # Bind mouse wheel para scroll (só quando necessário)
        def _on_mousewheel(event):
            # Só permitir scroll se a scrollbar estiver visível
            if self.campos_scrollbar.winfo_viewable():
                self.campos_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        # Bind apenas no canvas, não globalmente
        self.campos_canvas.bind("<MouseWheel>", _on_mousewheel)
    
    def update_scroll_region(self, event=None):
        """Atualiza scroll region e mostra/oculta scrollbar conforme necessário"""
        self.campos_canvas.configure(scrollregion=self.campos_canvas.bbox("all"))
        # Verificar se precisa de scroll
        canvas_height = self.campos_canvas.winfo_height()
        scrollable_height = self.campos_scrollable_frame.winfo_reqheight()
        
        if scrollable_height > canvas_height:
            # Mostrar scrollbar e habilitar scroll
            self.campos_scrollbar.pack(side="right", fill="y", pady=15)
            self.campos_canvas.configure(yscrollcommand=self.campos_scrollbar.set)
        else:
            # Ocultar scrollbar e desabilitar scroll
            self.campos_scrollbar.pack_forget()
            self.campos_canvas.configure(yscrollcommand=None)
    
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
                if self.field_validators.validar_campo("Data de Vencimento", valor):
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
        
        # Tentar chave específica da carteira primeiro: "Carteira - Tipo"
        chave_especifica = f"{carteira} - {tipo_selecionado}" if carteira and tipo_selecionado else None
        if chave_especifica and chave_especifica in CAMPOS_POR_TIPO:
            campos_necessarios = CAMPOS_POR_TIPO[chave_especifica]
        elif tipo_selecionado in CAMPOS_POR_TIPO:
            campos_necessarios = CAMPOS_POR_TIPO[tipo_selecionado]
        else:
            self.mostrar_instrucao_campos()
            return

        # Esconder todos os campos existentes
        for widget in self.campos_container.winfo_children():
            widget.pack_forget()

        # Mostrar apenas os campos necessários
        for campo in campos_necessarios:
            if campo in self.campos_entries:
                # Campo já existe, apenas mostrar
                self.campos_frames[campo].pack(fill='x', pady=2)
            else:
                # Campo não existe, criar
                valor_inicial = self.campos_info.get(campo, "")
                entry, status_label = self.criar_campo_com_validacao(self.campos_container, campo, valor_inicial)
                self.campos_entries[campo] = entry
                self.campos_frames[campo].pack(fill='x', pady=2)

        # Pré-preencher UNIDADE para ÁGUAS DE JOINVILLE
        if carteira == "ÁGUAS DE JOINVILLE" and "Unidade" in self.campos_entries:
            unidade_entry = self.campos_entries["Unidade"]
            if not unidade_entry.get().strip():
                unidade_entry.insert(0, "COMPANHIA ÁGUAS DE JOINVILLE EM JOINVILLE")
                # Validar visualmente após preencher
                for widget in self.campos_frames["Unidade"].winfo_children():
                    if isinstance(widget, tk.Label) and widget.cget('text') in ['✓', '✗']:
                        widget.config(text="✓", fg=DARK_THEME['success'])
                        break
    
    def atualizar_modelo_por_tipo(self, event=None):
        """Atualiza o modelo e campos quando o tipo de acionamento é alterado"""
        # Atualizar campos baseado no tipo selecionado
        self.atualizar_campos_por_tipo()
        # Gerar modelo automaticamente quando tipo é alterado (sem popup)
        self.gerar_modelo(mostrar_popup=False)
    
    def criar_campo_com_validacao(self, parent, campo, valor):
        """Cria um campo de entrada com validação automática"""
        row_frame = tk.Frame(parent, bg=DARK_THEME['bg_secondary'])
        row_frame.pack(fill='x', pady=2)  # Reduzido de 4 para 2
        
        # Armazenar referência ao frame para controle de visibilidade
        self.campos_frames[campo] = row_frame
        
        # Label do campo com cores indicativas
        if campo == "Desconto Principal":
            label_color = '#FF6B6B'  # Vermelho para principal
        elif campo == "Desconto Juros":
            label_color = '#4ECDC4'  # Azul para juros
        elif campo == "Desconto Multa":
            label_color = '#FFE66D'  # Amarelo para multa
        elif campo == "WhatsApp":
            label_color = '#45B7D1'  # Azul para WhatsApp
        elif campo == "E-mail":
            label_color = '#96CEB4'  # Verde para E-mail
        elif campo == "Data de Vencimento":
            label_color = DARK_THEME['text_primary']  # Cor padrão para data
        elif campo in ["Valor da Dívida", "Valor Total Atualizado", "Valor Proposto", "Valor Confirmado", 
                      "Valor Total Negociado", "Valor Original", "Valor Débito Original", 
                      "Valor Debito Original", "Valor Negociado", "Valor Total", "Total da Dívida"]:
            label_color = '#DDA0DD'  # Roxo para valores
        else:
            label_color = DARK_THEME['text_primary']
            
        label = tk.Label(row_frame, text=f"{campo}:", width=18, anchor='w',
                        font=('Segoe UI', 9, 'bold'), 
                        bg=DARK_THEME['bg_secondary'], 
                        fg=label_color)
        label.pack(side='left')
        
        # Campo obrigatório - adicionar asterisco
        if campo in CAMPOS_OBRIGATORIOS:
            label.config(text=f"{campo} *:", fg=DARK_THEME['danger'])
        
        # Entry com validação - tamanho padronizado para consistência visual
        entry_width = 30  # Tamanho único para todos os campos
        
        # Cores específicas por tipo de campo
        if campo == "Data de Vencimento":
            bg_color = DARK_THEME['surface']  # Cor padrão para data
            fg_color = DARK_THEME['text_primary']  # Cor padrão para texto
        elif campo == "Desconto Principal":
            bg_color = '#4a2d2d'  # Vermelho escuro para principal
            fg_color = '#FFB6C1'  # Rosa claro para texto
        elif campo == "Desconto Juros":
            bg_color = '#2d2d4a'  # Azul escuro para juros
            fg_color = '#ADD8E6'  # Azul claro para texto
        elif campo == "Desconto Multa":
            bg_color = '#4a4a2d'  # Amarelo escuro para multa
            fg_color = '#FFFFE0'  # Amarelo claro para texto
        elif campo == "WhatsApp":
            bg_color = '#2d4a2d'  # Verde escuro para WhatsApp
            fg_color = '#90EE90'  # Verde claro para texto
        elif campo == "E-mail":
            bg_color = '#2d2d4a'  # Azul escuro para E-mail
            fg_color = '#ADD8E6'  # Azul claro para texto
        elif campo in ["Valor da Dívida", "Valor Total Atualizado", "Valor Proposto", "Valor Confirmado", 
                      "Valor Total Negociado", "Valor Original", "Valor Débito Original", 
                      "Valor Debito Original", "Valor Negociado", "Valor Total", "Total da Dívida"]:
            bg_color = '#4a2d4a'  # Roxo escuro para valores
            fg_color = '#DDA0DD'  # Roxo claro para texto
        else:
            bg_color = DARK_THEME['surface']
            fg_color = DARK_THEME['text_primary']
            
        entry = tk.Entry(row_frame, font=('Segoe UI', 9), width=entry_width,
                        bg=bg_color, fg=fg_color,
                        relief='flat', bd=1, insertbackground=fg_color,
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
        
        # Adicionar placeholder para campos de data
        if campo in ["Data de Vencimento", "Data de Pagamento"]:
            if campo == "Data de Vencimento":
                placeholder_text = "Ex: 26/09/2025"
            else:
                placeholder_text = "DD/MM/AAAA"
            
            entry.insert(0, placeholder_text)
            entry.config(fg=DARK_THEME['text_muted'])
            
            # Função para gerenciar placeholder
            def on_focus_in(event):
                if entry.get() == placeholder_text:
                    entry.delete(0, tk.END)
                    entry.config(fg=DARK_THEME['text_primary'])
            
            def on_focus_out(event):
                if not entry.get().strip():
                    entry.insert(0, placeholder_text)
                    entry.config(fg=DARK_THEME['text_muted'])
            
            entry.bind('<FocusIn>', on_focus_in)
            entry.bind('<FocusOut>', on_focus_out)
        else:
            # Placeholders contextuais para FIRJAN
            carteira_atual = self.carteira_var.get()
            tipo_atual = self.tipo_var.get()
            if carteira_atual == 'FIRJAN' and tipo_atual == 'ACF - À VISTA' and campo in ['Valor Total Atualizado', 'Forma de Pagamento']:
                if campo == 'Valor Total Atualizado':
                    entry.insert(0, '(se encontra no campo como valor ORIGINAL)')
                elif campo == 'Forma de Pagamento':
                    entry.insert(0, '(Pix, deposito em conta corrente, Nº de Parcelas no cartão de crédito: 3X)')
                entry.config(fg=DARK_THEME['text_muted'])
                def on_focus_in_generic(event, default_text=entry.get()):
                    if entry.get() == default_text:
                        entry.delete(0, tk.END)
                        entry.config(fg=DARK_THEME['text_primary'])
                def on_focus_out_generic(event, default_text=entry.get()):
                    if not entry.get().strip():
                        entry.insert(0, default_text)
                        entry.config(fg=DARK_THEME['text_muted'])
                entry.bind('<FocusIn>', on_focus_in_generic)
                entry.bind('<FocusOut>', on_focus_out_generic)
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
            if campo in ["Data de Vencimento", "Data de Pagamento"] and valor_atual == "DD/MM/AAAA":
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
            valido, mensagem = self.field_validators.validar_campo_com_mensagem(campo, valor_atual)
            
            if valido:
                status_label.config(text="✓", fg='#00FF00', font=('Segoe UI', 10, 'bold'))
                # Manter cores específicas do campo mas com borda de sucesso
                entry.config(highlightcolor='#00FF00', highlightthickness=2)
                # Tooltip com mensagem de sucesso
                UIComponents.create_tooltip(status_label, mensagem)
            else:
                status_label.config(text="✗", fg='#FF0000', font=('Segoe UI', 10, 'bold'))
                # Manter cores específicas do campo mas com borda de erro
                entry.config(highlightcolor='#FF0000', highlightthickness=2)
                # Tooltip com mensagem de erro
                UIComponents.create_tooltip(status_label, mensagem)
        
        # Função para aplicar formatação apenas no FocusOut
        def aplicar_formatacao(event=None):
            valor_atual = entry.get()
            
            # Não aplicar formatação no placeholder
            if campo in ["Data de Vencimento", "Data de Pagamento"] and valor_atual == "DD/MM/AAAA":
                return
            
            valor_formatado = self.field_validators.aplicar_formatacao_automatica(campo, valor_atual)
            if valor_formatado != valor_atual:
                entry.delete(0, tk.END)
                entry.insert(0, valor_formatado)
            validar_tempo_real()
        
        # Função para limitar entrada de dados
        def limitar_entrada(event):
            return self.field_validators.limitar_entrada(campo, event)
        
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
                                relief='flat', bd=1, width=450)
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
        
        # Canvas para scroll no sidebar (só quando necessário)
        self.campos_canvas = tk.Canvas(campos_frame, bg=DARK_THEME['bg_secondary'], highlightthickness=0)
        self.campos_scrollbar = ttk.Scrollbar(campos_frame, orient="vertical", command=self.campos_canvas.yview)
        self.campos_scrollable_frame = tk.Frame(self.campos_canvas, bg=DARK_THEME['bg_secondary'])
        
        # Configurar scroll
        self.setup_scroll()
        
        self.campos_scrollable_frame.bind("<Configure>", self.update_scroll_region)
        
        self.campos_canvas.create_window((0, 0), window=self.campos_scrollable_frame, anchor="nw")
        self.campos_canvas.configure(yscrollcommand=self.campos_scrollbar.set)
        
        # Container dos campos (agora dentro do frame scrollável)
        self.campos_container = self.campos_scrollable_frame
        
        # Pack canvas (scrollbar será mostrado apenas quando necessário)
        self.campos_canvas.pack(side="left", fill="both", expand=True, padx=15, pady=15)
        
        # Inicializar com mensagem de instrução
        self.mostrar_instrucao_campos()
        
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
        self.texto_modelo = tk.Text(resultado_frame, height=5, font=('Consolas', 9),
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
        
        # Inicializar validadores após criar a interface
        self.field_validators = FieldValidators(self.carteira_var)
        
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
        
        # Atualizar scroll region após adicionar conteúdo
        self.campos_canvas.after(10, self.update_scroll_region)
    
    def gerar_modelo(self, mostrar_popup=True):
        """Gera o modelo de acionamento baseado nas seleções"""
        carteira = self.carteira_var.get()
        tipo = self.tipo_var.get()
        
        self.model_generator.gerar_modelo(carteira, tipo, self.campos_entries, 
                                         self.carteira_var, self.texto_modelo, mostrar_popup)
    
    def copiar_modelo(self):
        """Copia apenas os dados preenchidos para a área de transferência"""
        self.model_generator.copiar_modelo(self.texto_modelo)
    
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
        UIComponents.create_help_window(self.root)
