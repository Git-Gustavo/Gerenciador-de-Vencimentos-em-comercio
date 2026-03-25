from cadastro import cadastrar_produto, editar_produto, excluir_produto
from vencimento import mostrar_proximos, mostrar_vencidos, carregar_dados, dias_venc, mostrar_todos
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO = os.path.abspath(os.path.join(BASE_DIR, "..", "data", "produtos.xlsx"))

df = pd.read_excel(CAMINHO)

def menu():
    while True:
        print("\n===== GERENCIADOR DE VENCIMENTOS =====")
        print("1 - Cadastrar produto")
        print("2 - Ver vencidos")
        print("3 - Próximos 30 dias")
        print("4 - Dias personalizados")
        print("5 - Editar produto")
        print("6 - Excluir produto")
        print("7 - Ver todos os produtos")  # 🔥 NOVO
        print("8 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            df = carregar_dados()
            mostrar_vencidos(df)

        elif opcao == "3":
            df = carregar_dados()
            mostrar_proximos(df)

        elif opcao == "4":
            df = carregar_dados()
            dias_venc(df)

        elif opcao == "5":
            editar_produto()

        elif opcao == "6":
            excluir_produto()

        elif opcao == "7":
            df = carregar_dados()
            mostrar_todos(df)

        elif opcao == "8":
            break

        else:
            print("❌ Opção inválida!")

menu()