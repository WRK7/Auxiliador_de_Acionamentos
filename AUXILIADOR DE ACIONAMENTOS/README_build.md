Build do executável (Windows)

1) Instalar dependências de build:
   - Python 3.10+
   - pip install -U pip
   - pip install pyinstaller

2) Rodar o build no diretório do projeto (onde está main.py):
   pyinstaller --noconfirm --onefile --windowed --name AuxiliadorAcionamentos \
     --add-data "historico;historico" \
     --add-data "config.py;." \
     --add-data "theme.py;." \
     --add-data "ui_components.py;." \
     --add-data "validators.py;." \
     --hidden-import tkinter \
     main.py

3) O executável ficará em dist/AuxiliadorAcionamentos.exe

4) Copiar a pasta "historico" inicial (se necessário) para junto do .exe.

Observação: O código de histórico resolve a pasta ao lado do .exe automaticamente.


