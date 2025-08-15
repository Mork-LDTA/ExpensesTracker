#Os usuários podem visualizar um resumo das despesas para um mês específico (do ano atual).
import time
import Headers
import fileService
import expensesService
import color
import os




expenses_service = expensesService.ExpensesService
file_service = fileService.FileService
teste = file_service.read_formmated()

def clear_terminal():
    if os.name == "nt": 
        os.system("cls")
    else: 
        os.system("clear")

def confirm_menu_return():
    print("\nDeseja voltar ao Menu?\n")
    print("1.Voltar\n")
    print("2.Continuar\n")
    return_choice = int(input("Opção: "))
    if return_choice == 1:
        menu()


def menu():
    expense = file_service.open()
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
            choice = expenses_service.category_user_expenses()
            expense = expenses_service.add_expense(expenses=expense ,description=description, value=value, category=choice)
            file_service.write(expense) 
            print("=="*20)
            print()
            confirm_menu_return()
            
        elif selection == 2:
            print(color.white +"=="*20 + "\n"+color.reset_color)
            idExpense = input("Digite o ID da despesa: ").strip()
            if idExpense == "":
                print("ID Nao encontrado")
            else:
                idExpense = int(idExpense)
                index = expenses_service.get_expense_index_by_id(expense, idExpense)
                if type(index) == int:
                    print("\n[Pressione enter se caso queira deixar antigo]\n")
                    expenses_service.print_expense_by_id(expenses=expense, id=idExpense)
                    description = input("Digite a nova descrição da despesa: ")
                    print()
                    value_str = input("\nDigite o valor da despesa: ")
                    print()
                    category_choice = input("Digite o Valor correspondente de uma das categorias: ").strip()
                    if category_choice == "":
                        confirm_menu_return()
                    if value_str.strip() == "":
                        value = None
                    else:
                        category_choice = int(category_choice)
                        category_choice = expenses_service.category_user_expenses()
                        value = int(value_str)
                    expense = expenses_service.edit_expense(expenses=expense, id=idExpense,description=description,value=value, category=category_choice)
                    file_service.write(expense)
                    print("=="*20+color.reset_color)
                print()
                confirm_menu_return()


        elif selection == 3:
            print("=="*20 + "\n")
            idExpense = int(input(color.white + "Digite o Id da despesa: " + color.reset_color))
            print()
            if idExpense == "":
                print("ID Nao encontrado")
            else:
                idExpense = int(idExpense)
                expenses_service.get_expense_index_by_id(expenses=expense, id=idExpense)
                confirmDelete = None
                while confirmDelete not in [1, 2]:
                    try:
                        expenses_service.print_expense_by_id(expenses=expense, id=idExpense)
                        selection = input("\nConfirme a exclusao?\n\n 1. Sim\n 2. Não\n\nResposta: ").strip()
                        confirmDelete = int(selection)
                        
                        if confirmDelete not in [1, 2]:
                            print("Por favor, digite 1 ou 2.")
                        elif confirmDelete == 2:
                            confirm_menu_return()
                        elif confirmDelete == 1:
                            expenses_service.getExpenseIndexById(expenses=expense, id=idExpense)
                            expenses_service.removeExpense(expenses=expense, id=idExpense)
                            file_service.write(expense)
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
                    expenses_service.view_summary(expense)
                    confirm_menu_return()
                elif selection == 2:
                    expenses_service.get_expense_by_month()
                    confirm_menu_return()
                elif selection == 3:
                    expenses_service.get_expense_index_by_category()
                    confirm_menu_return()
                elif selection == 4:
                    confirm_menu_return()
                    
        elif selection == 5:
            user_aswer = int(input("Deseja exportar para CSV?\n" \
                                        "1- SIM\n" \
                                        "2- NAO\n" \
                                        "Opcao: "))
            if user_aswer == 1:
                expenses_service.export_json_to_csv("expensesData.json", "expensesData.csv")
                confirm_menu_return()
            elif user_aswer == 2:
                confirm_menu_return()

            else:
                print("Valor invalido, por favor digite um número valido")
                
        elif selection == 6:
            file_service.db_uptade_from_json("expensesData.json", "expenses.db")
            confirm_menu_return()
            
        elif selection == 0:
            print("Encerrando...")
            time.sleep(2)
            print("Fim do Programa.")
            exit()

menu()