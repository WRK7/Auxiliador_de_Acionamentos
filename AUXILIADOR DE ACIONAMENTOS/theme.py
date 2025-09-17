"""
Módulo de tema e configurações visuais da aplicação
"""

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

def setup_dark_theme():
    """Configura o tema escuro minimalista"""
    import tkinter as tk
    from tkinter import ttk
    
    style = ttk.Style()
    style.theme_use('clam')
    
    # Configurar estilos para widgets
    style.configure('Dark.TCombobox',
                   fieldbackground=DARK_THEME['surface'],
                   background=DARK_THEME['surface'],
                   foreground=DARK_THEME['text_primary'],
                   borderwidth=1,
                   relief='solid',
                   bordercolor=DARK_THEME['border'],
                   arrowcolor=DARK_THEME['text_primary'],
                   selectbackground=DARK_THEME['accent'],
                   selectforeground=DARK_THEME['text_primary'])
    
    # Configurar o dropdown (lista) do Combobox
    style.map('Dark.TCombobox',
              fieldbackground=[('readonly', DARK_THEME['surface'])],
              background=[('readonly', DARK_THEME['surface'])],
              foreground=[('readonly', DARK_THEME['text_primary'])])
    
    # Configurar o dropdown listbox
    style.configure('Dark.TCombobox.Listbox',
                   background=DARK_THEME['surface'],
                   foreground=DARK_THEME['text_primary'],
                   selectbackground=DARK_THEME['accent'],
                   selectforeground=DARK_THEME['text_primary'],
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
