from datetime import datetime
class ExpensesService:
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
        
    def removeExpense(expenses=dict, id=int):
        index = ExpensesService.findExpenseIndexById(expenses=expenses, id=id)
        if type(index) == int:
            expenses["expenses"].pop(index)
        return expenses
    
    def editExpense(expenses=dict, id=int, description=None, value=None):
        # 1 Encontrar
        index = ExpensesService.findExpenseIndexById(expenses=expenses, id=id)
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
               "createdAt": expense["createdAt"] 
            }
        # 3 Retornar
        return expenses
    
    def findExpenseIndexById(expenses=dict, id=int):
        try:
            listIds = []
            for item in expenses["expenses"]:
                listIds.append(item['id'])
            return listIds.index(id)
        except:
            print("Item nao encontrado!") 

    @staticmethod
    def viewSummary(expenses=dict):
        if not expenses or "expenses" not in expenses or not expenses["expenses"]:
            print("\nNenhuma Despesa encontrada.")
            return
        
        total = 0
        
        for expense in expenses["expenses"]:
            date_formatted = datetime.fromisoformat(expense["createdAt"]).strftime("%d/%m/%Y %H:%M")
            print(f"ID: {expense['id']}")
            print(f"Descrição: {expense['description']}")
            print(f"Valor: R$ {expense['value'] / 100:.2f}")
            print(f"Criado em: {date_formatted}")
            print("=" * 20)
            total += expense["value"]

        print(f"Total de despesas: R$ {total / 100:.2f}")
        
        