# Funcion que permite recorrer una tupla y mostrarlo como menu
def menu_interactivo(tupla):
    for i in range(len(tupla)):
        print(f"{i+1}. {tupla[i]}")
