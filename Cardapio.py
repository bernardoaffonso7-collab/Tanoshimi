
# Etapa 1: Recepção do Cliente (slide 12)
def mostrar_cardapio():
    cardapio = {
        "sushi": 25.0,
        "sashimi": 30.0,
        "tempura": 20.0,
        "yakisoba": 28.0,
        "missoshiro": 10.0
    }
    print("\n--- Cardápio do Restaurante Tanoshimi ---")
    for item, preco in cardapio.items():
        print(f"{item}: R$ {preco:.2f}")
    return cardapio

mostrar_cardapio()