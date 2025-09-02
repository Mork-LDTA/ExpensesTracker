import color
import datetime
import Headers
import expensesService
import fileService
# Headers.header()
expenses_service = expensesService.ExpensesService

# expenses_service = expensesService.ExpensesService
# file_service = fileService.FileService
# teste = fileService.read_formmated()
# expense = fileService.read()
# fileService.write(expense)


# @staticmethod
# #filtro
# def filter_by_user_choise(expenses=dict):
#     current_year = datetime.now().year
#     current_month = datetime.now().month
#     print("Informe o ano e o mês para obter o resumo das despesas:")
#     year_selection = int(input("Insira o ano: "))
#     month_selection = int(input("insira o mês: "))
#     try:
#         listDate = []
#         for dates in expenses["expenses"]:
#             if dates == year_selection and dates == month_selection:
#                 listDate.append(dates)
#                 return listDate
#             else:
#                 print("Nenhuma despesa encontrada para o ano e mês informados.")
#                 return None
#     except ValueError:
#         print(f"Item com ID {id} não encontrado!")
#         return None
print
choice = expenses_service.category_user_expenses()