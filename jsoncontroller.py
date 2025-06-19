import json

class JsonController():
    def __init__(self, dir,):
        self.dir = dir
        

    def open_file(self):

        with open(self.dir , 'r', encoding="utf-8") as file:
            data = json.load(file)
            return data
            

    def save_file(self, data):
        self.data = data

        with open(self.dir , 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

