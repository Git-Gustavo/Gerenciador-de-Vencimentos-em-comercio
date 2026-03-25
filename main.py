from cadastro import cadastrar_produto
from vencimento import mostrar_proximos, mostrar_vencidos, carregar_dados, dias_venc
def menu():
    while True:
        try:
            print("\n1 - Cadastrar produto")
            print("2 - Ver vencimentos")
            print("3 - Proximos 30 dias")

            opcao = int(input("Escolha: "))
            if opcao == "1":
                cadastrar_produto()
            elif opcao == "2":
                df= carregar_dados()
                mostrar_vencidos(df)
            elif opcao == "3":
                df= carregar_dados()
                mostrar_proximos(df)
            elif opcao == "4":
                df= carregar_dados()
                dias_venc(df)
            elif opcao == "5":
                break
        except ValueError:
            print("Digite apenas numeros. ")
menu()