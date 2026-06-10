
# 1. Funções matemáticas da Matriz Operacional (slide 7)
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    # Gatilho de segurança: if b != 0
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

# Etapa 1: Recepção do Cliente 
def mostrar_cardapio():
    cardapio = {
        "sushi": 49.0,
        "sashimi": 30.0,
        "tempura": 26.0,
        "yakisoba": 35.0,
        "sorvete": 15.0
    }
    print("\n--- Cardápio do Restaurante Tanoshimi ---")
    for item, preco in cardapio.items():
        print(f"{item}: R$ {preco:.2f}")
    return cardapio

mostrar_cardapio()

#Etapa 2: fazer pedido

def fazer_pedido(cardapio):
    total_mesa = 0.0
    while True:
        pedido = input("n\ Digite o nome do item(ou 'fim' para encerrar): ").lower()
        if pedido == "fim":
            break
        if pedido in cardapio:
            total_mesa = soma(total_mesa, cardapio[pedido])
            print(f"✅ {pedido} adicionado. Subtotal: R$ {total_mesa: .2f}")
        else:
            print("❌ Item não encontrado. Tente novamente.")
    return total_mesa

## 4. Etapa 3: Saída - fechar_conta (slide 12)
def fechar_conta(total_sem_taxa):
    taxa = multiplicacao(total_sem_taxa, 0.10)  # 10% de taxa de serviço
    total_com_taxa = soma(total_sem_taxa, taxa)
    
    print("\n--- CONTA FINAL ---")
    print(f"Total consumido: R$ {total_sem_taxa:.2f}")
    print(f"Taxa de serviço (10%): R$ {taxa:.2f}")
    print(f"Total a pagar: R$ {total_com_taxa:.2f}")
    return total_com_taxa

# 5. Execução principal - Integração completa (slide 12)
def main():
    print("=== Bem-vindo ao Restaurante Tanoshimi ===")
    cardapio = mostrar_cardapio()
    total_sem_taxa = fazer_pedido(cardapio)
    if total_sem_taxa > 0:
        fechar_conta(total_sem_taxa)
    else:
        print("Nenhum pedido foi realizado. Até logo!")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()