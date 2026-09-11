import numpy as np
import pandas as pd

# DEFS
mostra_tabela = pd.read_csv('/home/zorin/Downloads/Códigos/Celdel/gastos_pessoais.csv')
print("-"*40)
print("           Sistema CelDel")
print("-"*40)
def sair():
    exit()
def tabela():
    print(mostra_tabela)
def gastos():
    while True:
        escolha_gastos = input("""Escolha uma das opções abaixo:
    1. Soma total
    2. Valor Máximo
    3. Valor Mínimo
    4. Valor Médio
    5. Sair
    """)
        if escolha_gastos == "1":
            soma_total = mostra_tabela['valor'].sum()
            print(f"Soma total:{soma_total}")
        elif escolha_gastos == "2":
            maximo = mostra_tabela.loc[(mostra_tabela['valor'].idxmax()), ['categoria', 'valor']]
            print(f"{maximo.to_string()}")
        elif escolha_gastos == "3":
            minimo = mostra_tabela['valor'].min()
            print(f"Valor Mínimo: {minimo}")
        elif escolha_gastos == "4":
            media = mostra_tabela['valor'].mean()
            print(f"Valor médio: {media}")
        elif escolha_gastos == "5":
            inicio()
            break
        else:
            print("Digite um número das opções")
def categoria():
    while True:
        escolha_categoria = input("""Escolha uma das opções abaixo:
1. Ver categorias
2. Ver número de categorias
3. sair
""")
        if escolha_categoria == "1":
            mostra_tabela['categoria'] = mostra_tabela['categoria'].astype('category')
            cru = mostra_tabela['categoria'].cat.categories
            for formatado in cru:
                print(formatado)
        elif escolha_categoria == "2":
            categoria_crus = mostra_tabela['categoria'].value_counts()
            print(categoria_crus.to_string())
        elif escolha_categoria == "3":
            inicio()
            break
        else:
            print("Digite um número das opções")
def inicio():
    while True:
        escolha = input("""Escolha uma das opções abaixo:
        1. Área de Gastos
        2. Área de categoria
        3. Tabela completa
        4. Sair
        """)
        if escolha == "1":
            gastos()
        elif escolha == "2":
            categoria()
        elif escolha == "3":
            tabela()
        elif escolha == "4":
            print("Obrigado por usar o sistema")
            sair()
        else:
            print("Digite um número das opções")
inicio()