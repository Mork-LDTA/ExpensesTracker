import json
import sqlite3




class FileService():

    limit_file = "limit_budget.json"
    json_file = "expensesData.json"
    db_file = "expenses.db"
    
    @staticmethod
    def open():
        with open(FileService.json_file, "r") as file:
            return json.load(file)
        
    
    @staticmethod
    def write(data=dict):
        with open(FileService.json_file, 'w') as file:
            json.dump(data, file, indent=4)
            

    @staticmethod
    def read_formmated():
        data = FileService.open()
        return json.dumps(data, indent=4, ensure_ascii=False)
    


    @staticmethod
    def save_limit_budget(value):
        with open(FileService.limit_file, "w") as f:
            json.dump({"limit_budget": value}, f)

    @staticmethod
    def load_limit_budget():
        try:
            with open(FileService.limit_file, "r") as f:
                data = json.load(f)
                return data.get("limit_budget", None)
        except FileNotFoundError:
            return None

