"""
Executor principal da aplicação Gerador de Acionamentos
"""

import tkinter as tk
from app import AcionamentoApp

def main():
    """Função principal que inicia a aplicação"""
    root = tk.Tk()
    app = AcionamentoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
