import json, sqlite3

class dbService:
    json_file = "expensesData.json"
    db_file = "expenses.db"

    @staticmethod   
    def db_create():
        with open(dbService.json_file, "r", encoding="utf-8") as file:
            data = json.load(file) 

        conn = sqlite3.connect(dbService.db_file)
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
        with open(dbService.json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        conn = sqlite3.connect(dbService.db_file)
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
