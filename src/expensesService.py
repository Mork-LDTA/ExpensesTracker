from datetime import datetime
import color


class ExpensesService:

    @staticmethod
    def addExpense(expenses=dict, description=str, value=int):
        tot = 0
        if expenses:
            for item in expenses["expenses"]:
                if item["id"] >= tot:
                    tot = item["id"] + 1
            expenses["expenses"].append({
                        "id": tot,
                        "description": description,
                        "value": value,
                        "createdAt": datetime.now().isoformat()
            })
            return expenses
        else:
            expenses = {
                "expenses": [
                    {   
                        "id" : tot,
                        "description": description,
                        "value": value,
                        "createdAt": datetime.now().isoformat()
                    }
                ]
            }
            return expenses
     
    @staticmethod   
    def removeExpense(expenses=dict, id=int):
        index = ExpensesService.getExpenseIndexById(expenses=expenses, id=id)
        if type(index) == int:
            expenses["expenses"].pop(index)
        return expenses
    
    @staticmethod
    def editExpense(expenses=dict, id=int, description=None, value=None):
        # 1 Encontrar
        index = ExpensesService.getExpenseIndexById(expenses=expenses, id=id)
        if type(index) == int:
        # 2 Editar
            expense = expenses["expenses"][index]
            if(description is None):
                description = expense["description"] 
            if(value is None):
                value = expense["value"] 
            expenses["expenses"][index] = {
               "id": expense["id"],
               "description": description,
               "value": value,
               "createdAt": expense["createdAt"]  # type: ignore
            }
        # 3 Retornar
        return expenses
    
    @staticmethod
    def getExpenseIndexById(expenses=dict, id=id):
        try:
            listIds = []
            for item in expenses["expenses"]:
                listIds.append(item['id'])
            return listIds.index(id)
        except ValueError:
            print(f"Item com ID {id} não encontrado!")
            return None

    @staticmethod
    def printExpenseById(expenses, id):

        index = ExpensesService.getExpenseIndexById(expenses=expenses, id=id)

        if isinstance(index, int):
            expense = expenses["expenses"][index]
            date_formatted = datetime.fromisoformat(expense["createdAt"]).strftime("%d/%m/%Y %H:%M")
            print("==" * 20)
            print(f"ID: {expense['id']}")
            print(f"Descrição: {expense['description']}")
            print(f"Valor: R$ {expense['value'] / 100:.2f}")
            print(f"Criado em: {date_formatted}")
            print("==" * 20, "\n\n")
        else:
            print(f"Despesa com ID {id} não encontrada.")

            
    @staticmethod
    def viewSummary(expenses=dict):
        if not expenses or "expenses" not in expenses or not expenses["expenses"]:
            print("\nNenhuma despesa encontrada.")
            return

        print(f"{'#':<3} {'ID':<5} {'Date':<12} {'Description':<20} {'Amount':>10}")
        print("-" * 55)

        total = 0
        for expense in expenses["expenses"]:
            date_formatted = datetime.fromisoformat(expense["createdAt"]).strftime("%Y-%m-%d")
            amount = f"R${expense['value'] / 100:.2f}"
            print(f"{'':<3} {expense['id']:<5} {date_formatted:<12} {expense['description']:<20} {amount:>10}")
            total += expense["value"]

        print("-" * 55)
        print(f"{'':<3} {'':<5} {'':<12} {'TOTAL':<20} R${total / 100:.2f}")


            