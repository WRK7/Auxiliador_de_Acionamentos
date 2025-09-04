# Teste da validação de data
from datetime import datetime, timedelta
from validators import Validator

# Configuração de prazos
PRAZO_MAXIMO_POR_CARTEIRA = {
    "SENAC RJ": 7,
    "CEDAEE": 5,
    "PREFEITURA RJ": 7,
    "ESTADO RJ": 10,
    "UNIÃO": 15,
    "OUTROS": 7
}

def testar_datas():
    print("=== TESTE DE VALIDAÇÃO DE DATAS ===")
    print(f"Data atual: {datetime.now().date()}")
    print()
    
    # Datas para testar
    datas_teste = [
        "25/12/2024",  # Hoje
        "26/12/2024",  # Amanhã
        "01/01/2025",  # 7 dias no futuro
        "02/01/2025",  # 8 dias no futuro
        "24/12/2024",  # Ontem
    ]
    
    carteira = "SENAC RJ"  # 7 dias de prazo
    
    for data in datas_teste:
        valido, mensagem = Validator.validar_data_vencimento(data, carteira, PRAZO_MAXIMO_POR_CARTEIRA)
        status = "✅ VÁLIDA" if valido else "❌ INVÁLIDA"
        print(f"{data}: {status} - {mensagem}")

if __name__ == "__main__":
    testar_datas()
