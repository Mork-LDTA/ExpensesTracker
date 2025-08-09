import json

class FileService():
    fileName = "expensesData.json"
    
    def read():
        with open(FileService.fileName, "r") as result:
            return json.load(result)
    
    def write(data=dict):
        with open(FileService.fileName, 'w') as result:
            json.dump(data, result, indent=4) # indent=4 formata o JSON de forma legível
