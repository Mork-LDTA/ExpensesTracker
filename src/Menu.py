#O aplicativo deve ser executado a partir da linha de comando e deve ter os seguintes recursos:
#Os usuários podem adicionar uma despesa com uma descrição e valor. /\/\\/\/\/\//\/\/\/\/
#Os usuários podem atualizar uma despesa./\/\\/\/\/\//\/\/\/\/
#Os usuários podem excluir uma despesa. /\/\\/\/\/\//\/\/\/\/
#Os usuários podem visualizar todas as despesas. /\/\\/\/\/\//\/\/\/\/
#Os usuários podem visualizar um resumo de todas as despesas.\/\/\/\/\ Printar estilo excel
#Os usuarios podem visualizar apenas a despesa que ele deseja por id.
#Os usuários podem visualizar um resumo das despesas para um mês específico (do ano atual).
from datetime import datetime
from os import system
import Headers
system("clear")
import fileService
import expensesService




expensesService = expensesService.ExpensesService
fileService = fileService.FileService

expense = fileService.read()

#expense = expensesService.removeExpense(expenses=expense, id=0)
#expense = expensesService.editExpense(expenses=expense, id=7, description=None, value=7 )

teste = fileService.read_formmated()


#A FAZER:

# Menu para adicionar uma despesa 1
# Menu para editar uma despesa 2
# Menu para remover uma despesa 3

Headers.menu()
selection = int(input("NUM : "))
if selection == 1:
    print("=="*20 + "\n")
    description = input("Digite a descrição da despesa: ")
    value = int(input("Digite o valor da despesa: "))
    expense = expensesService.addExpense(expenses=expense ,description=description, value=value)
    fileService.write(expense) 

elif selection == 2:
    print("=="*20 + "\n")
    idExpense = int(input("Digite o ID da despesa: "))
    expense = expensesService.editExpense(expenses=expense, id=idExpense)
    print()

elif selection == 3:
    print("=="*20 + "\n")
    idExpense = int(input("Digite o Id da despesa: " + "\n"))
    #print(showExpense + "\n")
    print("Tem certeza que deseja remover?")
    print("1. Sim")
    print("2. Não" + "\n")
    confirmDelete = None
    while confirmDelete not in [1, 2]:
        try:
            selection = input("Confirme a exclusao? (1. Sim\n2. Não): ").strip()
            confirmDelete = int(selection)
            
            if confirmDelete not in [1, 2]:
                print("Por favor, digite 1 ou 2.")
        except ValueError:
        

elif selection == 4:
    expensesService.viewSummary(expenses=expense)

else:
    print("Valor invalido, por favor digite um número valido")

