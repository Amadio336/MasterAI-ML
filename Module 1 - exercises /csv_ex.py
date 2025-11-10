import csv


class CSV_Manager:
    def __init__(self, path_to_file):
        self.file = path_to_file
   

    def read_content_as_list(self):
        try:
            with open(self.file, "rt", encoding="utf8") as file:
                content = list(csv.reader(file))
                return content
        
        except Exception as e: raise e
    
    def read_content_as_dict(self):
        try:
            with open(self.file, "rt", encoding="utf8") as file:
                content = list(csv.DictReader(file))
                return content
        
        except Exception as e: raise e
    
    def print_titles(self):
        for dictionary in self.read_content_as_dict():
            print(dictionary["Titolo"])

    def print_specific_author(self, author):
        for dictionary in self.read_content_as_dict():
            if dictionary["Autore"] == author:
                print(dictionary)




file1 = CSV_Manager("libri.csv")
#file1.print_titles()
file1.print_specific_author("Jane Austen")