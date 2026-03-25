import pandas as pd
from datetime import datetime

df = pd.read_excel("produtos.xlsx")
def carregar_dados():
    df = pd.read_excel("produtos.xlsx")

    df["validade"] = pd.to_datetime(df["validade"])
    
    hoje = pd.Timestamp.today().normalize()

    df["status"] = (df["validade"] < hoje).map({True: "VENCIDO", False: "OK"})

    df["dias_para_vencer"] = (df["validade"] - hoje).dt.days

    return df

def mostrar_proximos(df):
    proximos = df[(df["dias_para_vencer"] < 30) & (df["dias_para_vencer"] >= 0)]

    if not proximos.empty:
        print("Próximos do vencimento:")
        print(proximos[["codigo", "nome", "dias_para_vencer"]])
    else:
        print("Nenhum produto próximo do vencimento.")

def mostrar_vencidos(df):
    vencidos = df[df["dias_para_vencer"] < 0]

    if not vencidos.empty:
        print("Produtos vencidos:")
        print(vencidos[["codigo", "nome", "dias_para_vencer"]])
    else:
        print("Nenhum produto vencido.")

def dias_venc(df):
    numero = int(input("Quantos dias até o vencimento: "))
    
    vai_vencer = df[(df["dias_para_vencer"] < numero) & (df["dias_para_vencer"] >= 0)]
    
    if not vai_vencer.empty:
        print(f"Produtos que irão vencer até {numero} dias:")
        print(vai_vencer)
    else: 
        print("Nenhum produto próximo do vencimento.")
