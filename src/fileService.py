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
    def db_create():
        with open(FileService.json_file, "r", encoding="utf-8") as file:
            data = json.load(file) 

        conn = sqlite3.connect(FileService.db_file)
        cursor = conn.cursor()
        
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    description TEXT,
                    value REAL,
                    category TEXT,
                    createdAT TEXT              
    )
    """)
        for expense in data["expenses"]:
            cursor.execute("""
                INSERT OR REPLACE INTO expenses (id, description, value, category, createdAt)
                VALUES (?, ?, ?, ?, ?)
            """, (
                expense["id"],
                expense["description"],
                expense["value"],
                expense["category"],
                expense["createdAt"]
    ))
        conn.commit()
        conn.close()

        print("JSON inserido diretamente no banco com sucesso!")
    
    @staticmethod
    def db_uptade_from_json(json_file, db_file):
        with open(FileService.json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        conn = sqlite3.connect(FileService.db_file)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    description TEXT,
                    value REAL,
                    category TEXT,
                    createdAT TEXT              
    )
    """)
        for expense in data["expenses"]:
            cursor.execute("""
                INSERT OR REPLACE INTO expenses (id, description, value, category, createdAt)
                VALUES (?, ?, ?, ?, ?)
""", (
                expense["id"],
                expense["description"],
                expense["value"],
                expense["category"],
                expense["createdAt"]
    ))
        conn.commit()
        conn.close()

        print("Banco atualizado com os dados mais recentes do JSON!")

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

