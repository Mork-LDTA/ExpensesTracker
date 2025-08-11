import json



class FileService():
    fileName = "expensesData.json"
    
    @staticmethod
    def read():
        with open(FileService.fileName, "r") as file:
            return json.load(file)
    
    
    
    @staticmethod
    def write(data=dict):
        with open(FileService.fileName, 'w') as file:
            json.dump(data, file, indent=4) 

    @staticmethod
    def read_formmated():
        data = FileService.read()
        return json.dumps(data, indent=4, ensure_ascii=False) 
