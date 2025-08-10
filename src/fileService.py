import json

class FileService():
    fileName = "expensesData.json"
    
    @staticmethod
    def read():
        with open(FileService.fileName, "r") as result:
            return json.load(result)
             #
    
    @staticmethod
    def write(data=dict):
        with open(FileService.fileName, 'w') as result:
            json.dump(data, result, indent=4) 

    @staticmethod
    def read_formmated():
        data = FileService.read()
        return json.dumps(data, indent=4, ensure_ascii=False)
