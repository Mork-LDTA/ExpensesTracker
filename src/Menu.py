#programa esta achando id que nao existe!
#Os usuários podem visualizar um resumo das despesas para um mês específico (do ano atual).
from datetime import datetime
import Headers
import fileService
import expensesService
import color
import os

expensesService = expensesService.ExpensesService
fileService = fileService.FileService
teste = fileService.read_formmated()


def clear_terminal():
    if os.name == "nt": 
        os.system("cls")
    else: 
        os.system("clear")


def confirm_menu_return():
    print("\nDeseja voltar ao Menu?\n")
    print("1.Voltar\n")
    print("2.Continuar\n")
    return_choice = int(input("Opção: \n"))
    if return_choice == 1:
        clear_terminal()
        menu()


def menu():
    expense = fileService.read()
    Headers.menu()
    selection = int(input("\nNUM : "))
    print()
    while True:
        if selection == 1:
            print("=="*20)
            print()
            description = input("Digite a descrição da despesa: ")
            value_str = input("\nDigite o valor da despesa: ")
            if value_str.strip() == "":
                print("voce nao inseriu nenhum valor! ")
                confirm_menu_return()
                value = None
            else:
                value = int(value_str)

            expense = expensesService.add_expense(expenses=expense ,description=description, value=value)
            fileService.write(expense) 
            print("=="*20)
            print()
            confirm_menu_return()
            

        elif selection == 2:
            print("=="*20 + "\n")
            idExpense = int(input("Digite o ID da despesa: "))
            print("\n[Pressione enter se caso nao queira mudar o valor ou descricao]\n")
            description = input("Digite a nova descrição da despesa: ")
            value_str = input("\nDigite o valor da despesa: ") 
            if value_str.strip() == "":
                value = None
            else:
                value = int(value_str)

            expense = expensesService.edit_expense(expenses=expense, id=idExpense,description=description,value=value)
            fileService.write(expense)
            print("=="*20)
            print()
            confirm_menu_return()


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
                        confirm_menu_return()
                    elif confirmDelete == 1:
                        expensesService.getExpenseIndexById(expenses=expense, id=idExpense)
                        expensesService.removeExpense(expenses=expense, id=idExpense)
                        fileService.write(expense)
                        confirm_menu_return()

                except ValueError:
                    print(color.red + "\nEntrada invalida. Digite um numero: 1 ou 2"+color.reset_color)    

                            
        elif selection == 4:
            while True:
                Headers.bars("VER SUMARIO")
                print(color.white+"Filtrar por:\n")
                print(color.yellow+
                    "   1.Ver tudo\n" \
                    "   2.Filtrar por mes\n" \
                    "   3.Filtrar por categoria\n" \
                    "   4.Voltar\n"
                +color.reset_color)
                print(color.white +"=="*20 + "\n"+color.reset_color)
                selection = int(input("Opção: "))
                if selection == 1:
                    expensesService.view_summary(expense)
                    confirm_menu_return()
                if selection == 2:
                    print()#jaozin
                if selection == 4:
                    confirm_menu_return()


        elif selection == 5:
            user_aswer = int(input("Deseja exportar para CSV?\n" \
                                        "1- SIM\n" \
                                        "2- NAO\n" \
                                        "Opcao: "))

            if user_aswer == 1:
                expensesService.export_json_to_csv("expensesData.json", "expensesData.csv")
                
            else:
                print("Valor invalido, por favor digite um número valido")
            confirm_menu_return()
menu()