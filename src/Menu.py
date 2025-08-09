#O aplicativo deve ser executado a partir da linha de comando e deve ter os seguintes recursos:
#Os usuários podem adicionar uma despesa com uma descrição e valor. /\/\\/\/\/\//\/\/\/\/
#Os usuários podem atualizar uma despesa.
#Os usuários podem excluir uma despesa. /\/\\/\/\/\//\/\/\/\/
#Os usuários podem visualizar todas as despesas. /\/\\/\/\/\//\/\/\/\/
#Os usuários podem visualizar um resumo de todas as despesas.
#Os usuários podem visualizar um resumo das despesas para um mês específico (do ano atual).
import json
from datetime import datetime
from os import system
system("clear")
import fileService
import expensesService





expense = fileService.FileService.read()
#expense = expensesService.ExpensesService.addExpense(expenses=expense, description="Segundo", value=22222)
#expense = expensesService.ExpensesService.removeExpense(expenses=expense, id=0)
#expense = expensesService.ExpensesService.editExpense(expenses=expense, id=7, description=None, value=7 )

fileService.FileService.write(expense)
print(expense)


print("\n\n\n")
