import pandas as pd

def gerar_proximo_codigo(df):
    if df.empty:
        return 1
    return df["codigo"].max() + 1


def cadastrar_produto():
    try:
        df = pd.read_excel("produtos.xlsx")
    except:
        df = pd.DataFrame(columns=["codigo", "nome", "quantidade", "validade"])

    while True:
        try:
            codigo = input("Código (ou ENTER para automático): ")

            if codigo == "":
                codigo = gerar_proximo_codigo(df)
                print(f"Código gerado automaticamente: {codigo}")
            else:
                codigo = int(codigo)
            
            if codigo in df["codigo"].values:
                print("❌ Código já cadastrado!")
                continue

            nome = input("Nome: ")

            if nome.lower() in df["nome"].astype(str).str.lower().values:
                print("❌ Nome já cadastrado!")
                continue

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

            print("✅ Produto cadastrado com sucesso!")
            break

        except ValueError:
            print("❌ Entrada inválida! Tente novamente.")