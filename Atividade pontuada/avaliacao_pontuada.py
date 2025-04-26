import os
os.system("cls||clear")
total = 0.0

while True:
    print("\nCardápio:")
    print("1 - Picanha - R$25,00")
    print("2 - Lasanha - R$20,00")
    print("3 - Strogonoff - R$18,00")
    print("4 - Bife Acebolado - R$15,00")
    print("5 - Pão com ovo - R$5,00")
    print("6 - Refrigerante 1L - R$8,00")
    print("7 - Café com leite 150ml - R$3,00")
    print("0 - Finalizar compra")
    
    opcao = input("\nEscolha o número do prato desejado: ")
    
    if opcao == '1':
        total += 25.00
        print("Picanha adicionada ao pedido!")
    elif opcao == '2':
        total += 20.00
        print("Lasanha adicionada ao pedido!")
    elif opcao == '3':
        total += 18.00
        print("Strogonoff adicionado ao pedido!")
    elif opcao == '4':
        total += 15.00
        print("Bife Acebolado adicionado ao pedido!")
    elif opcao == '5':
        total += 5.00
        print("Pão com ovo adicionado ao pedido!")
    elif opcao == '6':
        total += 8.00
        print("Refrigerante 1L adicionado ao pedido!")
    elif opcao == '7':
        total += 3.00
        print("Café com leite adicionado ao pedido!")
    elif opcao == '0':
        break
    else:
        print("Inválido! Escolha um número de 1 a 7 ou 0 para finalizar.")
    
    print(f"Subtotal atual: R${total:.2f}")

print(f"\nTotal do pedido: R${total:.2f}")


while True:
    print("\nFormas de pagamento:")
    print("1 - Pagamento à vista (10% de desconto)")
    print("2 - Pagamento à prazo (10% de acréscimo)")
    pagamento = input("Digite o código do pagamento: ")
    
    match pagamento:
        case '1':
            desconto = total * 0.1
            total_final = total - desconto
            print(f"\nTotal à vista com desconto: R${total_final:.2f}")
            break
        case '2':
            acrescimo = total * 0.1
            total_final = total + acrescimo
            print(f"\nTotal a crédito com acréscimo: R${total_final:.2f}")
            break
        case _:
            print("Opção inválida! Digite 1 ou 2.")

print("\nObrigado pela preferência! Volte sempre!")