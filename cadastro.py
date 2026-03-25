import pandas as pd

def cadastrar_produto():
    try:
        df = pd.read_excel("produtos.xlsx")
    except:
        df = pd.DataFrame(columns=["codigo", "nome", "validade", "dias_para_vencer", "status"])

    codigo = int(input("Código: "))
    nome = input("Nome: ")
    quantidade = int(input("Quantidade: "))
    validade = input("Validade (YYYY-MM-DD): ")

    novo = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "validade": validade
    }
    df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
    df.to_excel("produtos.xlsx", index=False)

    print("Produto Cadastrado! ")