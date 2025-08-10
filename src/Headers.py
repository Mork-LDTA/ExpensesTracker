import color

@staticmethod
def header():
    print("=="*20)
    print("Controle de despesas".center(40))
    print("=="*20)

@staticmethod
def menu():
    print(color.white + "=="*20 + color.reset_color)
    print(color.white +"Menu de Despesas".center(40) + color.reset_color)
    print(color.white +"=="*20)
    print(color.yellow + "1. Adicionar despesa\n")
    print(color.yellow + "2. Editar despesa\n")
    print(color.yellow + "3. Remover despesa\n")
    print(color.yellow + "4. Sumario de despesas")
    print(color.white + "=="*20 + color.reset_color)

