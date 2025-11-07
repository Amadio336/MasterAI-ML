class Appunti:
    def __init__(self, path, content):
        self.path = path
        self.content = content
        self.write()

    def write(self):
        try:
            with open(self.path, "wt", encoding="utf-8") as file:
                file.write(self.content)
        except Exception as e: raise e
    
    def mostra(self):
        try:
            with open(self.path, "rt", encoding="utf-8") as file:
                return file.read()
        except Exception as e: raise e
    
    def cancella_file(self):
         try:
            with open(self.path, "wt", encoding="utf-8") as file:
                file.write("")
         except Exception as e: raise e

        

    

    
        


file1 = Appunti("prova.txt", "ciao come stai")
print(file1.mostra())
file1.cancella_file()