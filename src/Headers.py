import color

def header():
    print("=="*20)
    print("Controle de despesas".center(40))
    print("=="*20)


def menu():
    print(color.white + "=="*20 + color.reset_color)
    print("Menu de Despesas".center(40), "\n")
    print("1. Adicionar despesa\n")
    print(color.red + "2. Editar despesa\n"+color.reset_color)
    print("3. Remover despesa\n")
    print("4. Sumario de despesas")
    print("=="*20)

def resume():
    print("=="*20, "\nResumo Despesas\n".center(40),"\n", "=="*20, "\n")