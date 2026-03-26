import pandas as pd
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO = os.path.abspath(os.path.join(BASE_DIR, "..", "data", "produtos.xlsx"))


def gerar_proximo_codigo(df):
    if df.empty:
        return 1
    return df["codigo"].max() + 1


def cadastrar_produto():
    try:
        df = pd.read_excel(CAMINHO)
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

            # 🔥 VALIDAÇÃO DE DATA BR
            while True:
                validade_input = input("Validade (DD/MM/AAAA): ")
                try:
                    validade = datetime.strptime(validade_input, "%d/%m/%Y")
                    break
                except ValueError:
                    print("❌ Data inválida! Ex: 25/03/2026")

            novo = {
                "codigo": codigo,
                "nome": nome,
                "quantidade": quantidade,
                "validade": validade.strftime("%Y-%m-%d")  # salva padrão interno
            }

            df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
            df.to_excel(CAMINHO, index=False)

            print("✅ Produto cadastrado!")
            break

        except ValueError:
            print("❌ Entrada inválida!")
def editar_produto():
    try:
        df = pd.read_excel(CAMINHO)
    except:
        print("Nenhum produto cadastrado.")
        return

    codigo = int(input("Código do produto: "))

    if codigo not in df["codigo"].values:
        print("❌ Produto não encontrado!")
        return

    index = df[df["codigo"] == codigo].index[0]

    print("Deixe vazio para manter o valor atual.\n")

    novo_nome = input(f"Nome ({df.loc[index, 'nome']}): ")
    nova_quantidade = input(f"Quantidade ({df.loc[index, 'quantidade']}): ")

    # 🔥 valida data também na edição
    nova_validade = input(f"Validade ({df.loc[index, 'validade']} - DD/MM/AAAA): ")

    if novo_nome:
        if novo_nome.lower() in df["nome"].astype(str).str.lower().values:
            print("❌ Nome já existe!")
            return
        df.loc[index, "nome"] = novo_nome

    if nova_quantidade:
        df.loc[index, "quantidade"] = int(nova_quantidade)

    if nova_validade:
        from datetime import datetime
        try:
            validade = datetime.strptime(nova_validade, "%d/%m/%Y")
            df.loc[index, "validade"] = validade.strftime("%Y-%m-%d")
        except ValueError:
            print("❌ Data inválida!")
            return

    df.to_excel(CAMINHO, index=False)
    print("✅ Produto atualizado!")


def excluir_produto():
    try:
        df = pd.read_excel(CAMINHO)
    except:
        print("Nenhum produto cadastrado.")
        return

    codigo = int(input("Código do produto: "))

    if codigo not in df["codigo"].values:
        print("❌ Produto não encontrado!")
        return

    confirm = input("Tem certeza que deseja excluir? (s/n): ")

    if confirm.lower() != "s":
        print("Cancelado.")
        return

    df = df[df["codigo"] != codigo]
    df.to_excel(CAMINHO, index=False)

    print("🗑️ Produto excluído!")