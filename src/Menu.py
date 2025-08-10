
#Os usuários podem visualizar um resumo das despesas para um mês específico (do ano atual).
from datetime import datetime
import Headers
import fileService
import expensesService
import color




expensesService = expensesService.ExpensesService
fileService = fileService.FileService

teste = fileService.read_formmated()

def menu():
    expense = fileService.read()
    Headers.menu()
    selection = int(input("\nNUM : "))
    print()
    if selection == 1:
        print("=="*20 + "\n")
        description = input("Digite a descrição da despesa: ")
        value = int(input("\nDigite o valor da despesa: "))
        expense = expensesService.addExpense(expenses=expense ,description=description, value=value)
        fileService.write(expense) 
        menu()

    elif selection == 2:
        print("=="*20 + "\n")
        idExpense = int(input("Digite o ID da despesa: "))
        print("\n[Pressione enter se caso nao queira mudar o valor ou descricao]")
        description = input("Digite a nova descrição da despesa: ")
        value = int(input("\nDigite o novo valor da despesa: "))
        expense = expensesService.editExpense(expenses=expense, id=idExpense,description=description,value=value)
        fileService.write(expense)
        menu()

    elif selection == 3:
        print("=="*20 + "\n")
        idExpense = int(input(color.white + "Digite o Id da despesa: " + color.reset_color))
        print()
        expensesService.getExpenseIndexById(expenses=expense, id=idExpense)

        confirmDelete = None
        while confirmDelete not in [1, 2]:
            try:
                expensesService.printExpenseById(expenses=expense, id=idExpense)
                selection = input("\nConfirme a exclusao?\n\n 1. Sim\n 2. Não\n\nResposta: ").strip()
                confirmDelete = int(selection)
                
                if confirmDelete not in [1, 2]:
                    print("Por favor, digite 1 ou 2.")
                elif confirmDelete == 2:
                    
                    menu()
                elif confirmDelete == 1:
                    expensesService.getExpenseIndexById(expenses=expense, id=idExpense)
                    expensesService.removeExpense(expenses=expense, id=idExpense)
                    fileService.write(expense)
                    menu()

            except ValueError:
                print(color.red + "\nEntrada invalida. Digite um numero: 1 ou 2"+color.reset_color)

    elif selection == 4:
        expensesService.viewSummary(expenses=expense)
        print("\n\n")
        menu()

    else:
        print("Valor invalido, por favor digite um número valido")

menu()
