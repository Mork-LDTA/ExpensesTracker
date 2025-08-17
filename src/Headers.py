import color




def header():
    print("=="*20)
    print("Controle de despesas".center(40))
    print("=="*20)

def menu():
    print(color.white + "=="*20 + color.reset_color)
    print(color.white +"Menu de Despesas".center(40) + color.reset_color)
    print(color.white +"=="*20)
    print(color.yellow + "\n1. Adicionar despesa")
    print(color.yellow + "2. Editar despesa")
    print(color.yellow + "3. Remover despesa")
    print(color.yellow + "4. Sumario de despesas")
    print(color.yellow + "5. Limite de despesas")
    print(color.yellow + "6. Converter o arquivo em CSV")
    print(color.yellow + "7. Atualizar lista de arquivos")
    print(color.yellow + "0. Sair/Fechar o programa\n")
    print(color.white + "=="*20 + color.reset_color)

def bars(string_text):
    print(color.white+"=="*20)
    print(color.green+string_text.center(40))
    print(color.white+"=="*20)

def category_expense():
    print(color.white+"=="*20)
    print(
    color.yellow+"\n     1. Fastfood\n \
    2. Alimentacao\n \
    3. Lazer\n \
    4. Contas\n \
    5. Roupas\n \
    6. Saude\n \
    7. Outros\n")
    print(color.white+"=="*20+color.reset_color)
    