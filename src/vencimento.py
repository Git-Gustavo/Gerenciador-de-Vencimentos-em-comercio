import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO = os.path.abspath(os.path.join(BASE_DIR, "..", "data", "produtos.xlsx"))


def carregar_dados():
    try:
        df = pd.read_excel(CAMINHO)
    except:
        df = pd.DataFrame(columns=["codigo", "nome", "quantidade", "validade"])

    df["validade"] = pd.to_datetime(df["validade"], errors="coerce")
    hoje = pd.Timestamp.today().normalize()

    df["status"] = df["validade"].apply(
        lambda x: "VENCIDO" if pd.notna(x) and x < hoje else "OK"
    )

    df["dias_para_vencer"] = (df["validade"] - hoje).dt.days

    return df


def formatar_data(df):
    df = df.copy()
    df["validade"] = df["validade"].dt.strftime("%d/%m/%Y")
    return df


def mostrar_todos(df):
    if df.empty:
        print("📭 Nenhum produto cadastrado.")
        return

    df = formatar_data(df)

    print("\n📋 TODOS OS PRODUTOS:\n")
    print(df[["codigo", "nome", "quantidade", "validade", "status", "dias_para_vencer"]])


def mostrar_proximos(df):
    proximos = df[(df["dias_para_vencer"] <= 30) & (df["dias_para_vencer"] >= 0)]

    if not proximos.empty:
        proximos = formatar_data(proximos)
        print("\n📦 Próximos do vencimento:")
        print(proximos[["codigo", "nome", "validade", "dias_para_vencer"]])
    else:
        print("Nenhum produto próximo do vencimento.")


def mostrar_vencidos(df):
    vencidos = df[df["dias_para_vencer"] < 0]

    if not vencidos.empty:
        vencidos = formatar_data(vencidos)
        print("\n⚠️ Produtos vencidos:")
        print(vencidos[["codigo", "nome", "validade", "dias_para_vencer"]])
    else:
        print("Nenhum produto vencido.")


def dias_venc(df):
    try:
        numero = int(input("Quantos dias até o vencimento: "))
    except:
        print("❌ Número inválido!")
        return

    vai_vencer = df[(df["dias_para_vencer"] <= numero) & (df["dias_para_vencer"] >= 0)]

    if not vai_vencer.empty:
        vai_vencer = formatar_data(vai_vencer)
        print(f"\n📊 Produtos que irão vencer em até {numero} dias:")
        print(vai_vencer[["codigo", "nome", "validade", "dias_para_vencer"]])
    else:
        print("Nenhum produto nesse intervalo.")