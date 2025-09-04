import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
import re
from datetime import datetime
import pyperclip
from config import CARTEIRAS, TIPOS_ACIONAMENTO, CAMPOS_INFO, MODELOS_ACIONAMENTO, CAMPOS_OBRIGATORIOS, FORMATACAO_AUTOMATICA, PRAZO_MAXIMO_POR_CARTEIRA
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
    'warning': '#f59e0b',         # Amarelo aviso
    'danger': '#ef4444',          # Vermelho perigo
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
    
    def revalidar_data_vencimento(self, event=None):
        """Revalida a data de vencimento quando a carteira é alterada"""
        # Atualizar label do prazo máximo
        carteira_atual = self.carteira_var.get()
        if carteira_atual and hasattr(self, 'prazo_label'):
            prazo_maximo = PRAZO_MAXIMO_POR_CARTEIRA.get(carteira_atual, 7)
            self.prazo_label.config(text=f"Máx: {prazo_maximo} dias")
        
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
    
    def criar_campo_com_validacao(self, parent, campo, valor):
        """Cria um campo de entrada com validação automática"""
        row_frame = tk.Frame(parent, bg=DARK_THEME['bg_secondary'])
        row_frame.pack(fill='x', pady=4)
        
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
                return
            
            # Validar campo
            if self.validar_campo(campo, valor_atual):
                status_label.config(text="✓", fg=DARK_THEME['success'])
            else:
                status_label.config(text="✗", fg=DARK_THEME['danger'])
        
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
        
        # Bind eventos
        entry.bind('<KeyRelease>', validar_tempo_real)
        entry.bind('<FocusOut>', aplicar_formatacao)
        
        # Validar inicialmente
        validar_tempo_real()
        
        return entry, status_label
    
    def criar_interface(self):
        """Cria a interface principal"""
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
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=DARK_THEME['bg_primary'])
        main_frame.pack(expand=True, fill='both', padx=30, pady=10)
        
        # Frame de seleções
        selecoes_frame = tk.LabelFrame(main_frame, text="Configurações", 
                                      font=('Segoe UI', 11, 'bold'), 
                                      bg=DARK_THEME['bg_secondary'],
                                      fg=DARK_THEME['text_primary'],
                                      relief='flat',
                                      bd=1)
        selecoes_frame.pack(fill='x', pady=(0, 15))
        
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
        
        # Botões removidos - tipos são fixos
        
        # Frame de informações
        info_frame = tk.LabelFrame(main_frame, text="Informações do Acionamento", 
                                  font=('Segoe UI', 11, 'bold'), 
                                  bg=DARK_THEME['bg_secondary'],
                                  fg=DARK_THEME['text_primary'],
                                  relief='flat',
                                  bd=1)
        info_frame.pack(fill='both', expand=True, pady=(0, 15))
        
        # Campos de entrada
        self.campos_entries = {}
        campos_container = tk.Frame(info_frame, bg=DARK_THEME['bg_secondary'])
        campos_container.pack(fill='both', expand=True, padx=15, pady=15)
        
        for i, (campo, valor) in enumerate(self.campos_info.items()):
            entry, status_label = self.criar_campo_com_validacao(campos_container, campo, valor)
            self.campos_entries[campo] = entry
        
        # Botão removido - campos são fixos
        
        # Frame de resultado
        resultado_frame = tk.LabelFrame(main_frame, text="Modelo de Acionamento", 
                                       font=('Segoe UI', 11, 'bold'), 
                                       bg=DARK_THEME['bg_secondary'],
                                       fg=DARK_THEME['text_primary'],
                                       relief='flat',
                                       bd=1)
        resultado_frame.pack(fill='both', expand=True, pady=(0, 15))
        
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
        botoes_frame = tk.Frame(main_frame, bg=DARK_THEME['bg_primary'])
        botoes_frame.pack(fill='x', pady=15)
        
        # Botão Gerar Modelo
        gerar_btn = tk.Button(botoes_frame, text="Gerar Modelo", command=self.gerar_modelo,
                             bg=DARK_THEME['accent'], fg=DARK_THEME['text_primary'], 
                             font=('Segoe UI', 10, 'bold'),
                             relief='flat', bd=0, cursor='hand2',
                             padx=20, pady=8,
                             activebackground=DARK_THEME['hover'])
        gerar_btn.pack(side='left', padx=(0, 12))
        
        # Botão Copiar
        copiar_btn = tk.Button(botoes_frame, text="Copiar", command=self.copiar_modelo,
                              bg=DARK_THEME['success'], fg=DARK_THEME['text_primary'], 
                              font=('Segoe UI', 10, 'bold'),
                              relief='flat', bd=0, cursor='hand2',
                              padx=20, pady=8,
                              activebackground=DARK_THEME['hover'])
        copiar_btn.pack(side='left', padx=(0, 12))
        
        # Botão Limpar
        limpar_btn = tk.Button(botoes_frame, text="Limpar", command=self.limpar_campos,
                              bg=DARK_THEME['warning'], fg=DARK_THEME['text_primary'], 
                              font=('Segoe UI', 10, 'bold'),
                              relief='flat', bd=0, cursor='hand2',
                              padx=20, pady=8,
                              activebackground=DARK_THEME['hover'])
        limpar_btn.pack(side='left', padx=(0, 12))
        
        # Botão Histórico
        historico_btn = tk.Button(botoes_frame, text="📋 Histórico", command=self.abrir_historico,
                                 bg=DARK_THEME['accent'], fg=DARK_THEME['text_primary'], 
                                 font=('Segoe UI', 10, 'bold'),
                                 relief='flat', bd=0, cursor='hand2',
                                 padx=20, pady=8,
                                 activebackground=DARK_THEME['hover'])
        historico_btn.pack(side='left')
        
        # Atualizar modelo inicial
        self.gerar_modelo()
    
    # Métodos de adicionar/remover elementos removidos - dados são fixos
    
    def gerar_modelo(self):
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
            messagebox.showwarning("Campos Inválidos", mensagem)
            return
        
        # Gerar modelo baseado no tipo
        modelo = self.criar_modelo_acionamento(carteira, tipo, informacoes)
        
        # Salvar no histórico
        id_acionamento = self.historico_manager.salvar_acionamento(carteira, tipo, informacoes, modelo)
        
        self.texto_modelo.delete(1.0, tk.END)
        self.texto_modelo.insert(1.0, modelo)
        
        # Mostrar mensagem de sucesso com ID
        if id_acionamento:
            messagebox.showinfo("Sucesso", f"Acionamento gerado e salvo com sucesso!\nID: {id_acionamento}")
    
    def criar_modelo_acionamento(self, carteira, tipo, informacoes):
        """Cria o modelo específico baseado no tipo de acionamento"""
        data_atual = datetime.now().strftime("%d/%m/%Y")
        
        modelo = f"""
=== ACIONAMENTO - {tipo} ===
Carteira: {carteira}
Data: {data_atual}

"""
        
        # Adicionar informações preenchidas
        for campo, valor in informacoes.items():
            modelo += f"{campo}: {valor}\n"
        
        # Usar modelo do arquivo config.py
        tipo_chave = None
        for chave in MODELOS_ACIONAMENTO.keys():
            if chave in tipo:
                tipo_chave = chave
                break
        
        if tipo_chave and tipo_chave in MODELOS_ACIONAMENTO:
            modelo += MODELOS_ACIONAMENTO[tipo_chave]
        else:
            modelo += MODELOS_ACIONAMENTO["OUTROS"]
        
        return modelo.strip()
    
    def copiar_modelo(self):
        """Copia o modelo para a área de transferência"""
        texto = self.texto_modelo.get(1.0, tk.END).strip()
        if texto:
            try:
                pyperclip.copy(texto)
                messagebox.showinfo("Sucesso", "Modelo copiado para a área de transferência!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao copiar: {e}")
        else:
            messagebox.showwarning("Aviso", "Nenhum modelo para copiar!")
    
    def limpar_campos(self):
        """Limpa todos os campos"""
        if messagebox.askyesno("Confirmar", "Deseja limpar todos os campos?"):
            self.carteira_var.set("")
            self.tipo_var.set("")
            for entry in self.campos_entries.values():
                entry.delete(0, tk.END)
            self.texto_modelo.delete(1.0, tk.END)
    
    def abrir_historico(self):
        """Abre a janela do histórico"""
        try:
            HistoricoUI(self.root, self.duplicar_acionamento_callback)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir histórico: {e}")
    
    def duplicar_acionamento_callback(self, dados_duplicados):
        """Callback para duplicar acionamento do histórico"""
        try:
            # Preencher campos com dados duplicados
            if 'carteira' in dados_duplicados:
                self.carteira_var.set(dados_duplicados['carteira'])
            
            if 'tipo' in dados_duplicados:
                self.tipo_var.set(dados_duplicados['tipo'])
            
            if 'informacoes' in dados_duplicados:
                for campo, valor in dados_duplicados['informacoes'].items():
                    if campo in self.campos_entries:
                        entry = self.campos_entries[campo]
                        entry.delete(0, tk.END)
                        entry.insert(0, valor)
            
            # Gerar modelo
            self.gerar_modelo()
            
            messagebox.showinfo("Sucesso", "Acionamento duplicado com sucesso!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao duplicar acionamento: {e}")

def main():
    root = tk.Tk()
    app = AcionamentoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
