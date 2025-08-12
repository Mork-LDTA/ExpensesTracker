from datetime import datetime
import color
import pandas as pd
import fileService
import Headers



class ExpensesService:
    @staticmethod
    def category_user_expenses():
        category_list = ("Fastfood", "Alimentacao", "Lazer", "Contas", "Roupas", "Saude", "Outos")
        while True:
            try:
                Headers.category_expense()
                category_user_choice = int(input("Categoria: ")) - 1
                if 0 <= category_user_choice < len(category_list):
                    choice = category_list[category_user_choice]
                    print(f"Você escolheu: {choice}")
                    return choice
                else:
                    print(color.red+"\nOpção não encontrada. Por favor, digite um número válido."+color.reset_color)
            except ValueError:
                print(color.red+"\nEntrada inválida. Digite apenas números inteiros."+color.reset_color)

    file_service = fileService.FileService
    

    @staticmethod
    def add_expense(expenses=dict, description=str, value=int, category=str):

        tot = 0
        if expenses:
            for item in expenses["expenses"]:
                if item["id"] >= tot:
                    tot = item["id"] + 1
            expenses["expenses"].append({
                        "id": tot,
                        "description": description,
                        "value": value,
                        "category": category,
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
                        "category": category,
                        "createdAt": datetime.now().isoformat()
                    }
                ]
            }
            return expenses
     
    @staticmethod   
    def remove_expense(expenses=dict, id=int):
        index = ExpensesService.get_expense_index_by_id(expenses=expenses, id=id)
        if type(index) == int:
            expenses["expenses"].pop(index)
        return expenses
    
    @staticmethod
    def edit_expense(expenses=dict, id=int, description=None, value=None, category=None):
        # 1 Encontrar
        index = ExpensesService.get_expense_index_by_id(expenses=expenses, id=id)
        if type(index) == int:
        # 2 Editar
            expense = expenses["expenses"][index]
            if(description is None):
                description = expense["description"] 
            if(value is None):
                value = expense["value"]
            if(category is None):
                category = expense["category"]
            expenses["expenses"][index] = {
               "id": expense["id"],
               "description": description,
               "value": value,
               "category": category,
               "createdAt": expense["createdAt"]  # type: ignore
            }
        # 3 Retornar
        return expenses
    
    @staticmethod
    def get_expense_index_by_id(expenses=dict, id=id):
        try:
            listIds = []
            for item in expenses["expenses"]:
                listIds.append(item['id'])
            return listIds.index(id)
        except ValueError:
            print(color.red + f"Item com ID {id} não encontrado!\n"+color.reset_color)
            return None

    @staticmethod
    def print_expense_by_id(expenses, id):

        index = ExpensesService.get_expense_index_by_id(expenses=expenses, id=id)

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
    def view_summary(expenses=dict):
        if not expenses or "expenses" not in expenses or not expenses["expenses"]:
            print("\nNenhuma despesa encontrada.")
            return
        print(f"{'#':<3} {'ID':<5} {'Date':<12} {'Description':<20} {'category':<15} {'Amount':>10}")
        print("-" * 70)

        total = 0
        for expense in expenses["expenses"]:
            date_formatted = datetime.fromisoformat(expense["createdAt"]).strftime("%Y-%m-%d")
            amount = f"R${expense['value'] / 100:.2f}"
            print(f"{'':<3} {expense['id']:<5} {date_formatted:<12} {expense['description']:<20} {expense['category']:<15} {amount:>10}")
            total += expense["value"]

        print("-" * 70)
        print(f"{'':<3} {'':<5} {'':<12} {'TOTAL':<20} R${total / 100:.2f}")

    
        

    @staticmethod
    def export_json_to_csv(json_path, csv_path):
        try:
            expense = fileService.FileService.read()
            # Verifica se o json nao esta vazio ou se a chave existe
            if "expenses" not in expense or not expense["expenses"]:
                print("Nenhuma despesa encontrada para exportar.")
                return

            #converte para dataframe(coluna e linhas)
            df = pd.DataFrame(expense["expenses"])

            #exportar para CSV 
            df.to_csv(csv_path, index=False)
            print(f"Arquivo exportado para {csv_path}")

        except Exception as e:
            print(f"Erro ao exportar para CSV: {e}")



            
