"""
Módulo de componentes de interface reutilizáveis
"""

import tkinter as tk
from tkinter import ttk, messagebox
from theme import DARK_THEME

class UIComponents:
    """Classe com componentes de interface reutilizáveis"""
    
    @staticmethod
    def create_minimal_button(parent, text, command, color, width=None, height=None):
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
    
    @staticmethod
    def create_tooltip(widget, texto):
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
    
    @staticmethod
    def create_help_window(parent, title="Ajuda"):
        """Cria janela de ajuda com atalhos"""
        ajuda_janela = tk.Toplevel(parent)
        ajuda_janela.title(f"{title} - Atalhos de Teclado")
        ajuda_janela.geometry("500x400")
        ajuda_janela.configure(bg=DARK_THEME['bg_primary'])
        ajuda_janela.resizable(False, False)
        
        # Centralizar janela
        ajuda_janela.transient(parent)
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
        
        return ajuda_janela
