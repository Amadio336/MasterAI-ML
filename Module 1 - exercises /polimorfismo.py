""" import math

class Forma:

    def area(self):
        raise NotImplementedError("il metodo forma va implementato nelle sottoclassi")

class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
        

    def area(self):
        return self.base * self.altezza
    


class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return self.raggio**2 * math.pi


forme = [Forma(), Cerchio(10), Rettangolo(12,3), Cerchio(4)]

for forma in forme:
    print(forma.area()) """



""" from abc import ABC, abstractmethod

class Veicolo(ABC):

    @abstractmethod
    def muovi(self):
        pass


    def __repr__(self):
        return f"Veicolo"



class Macchina(Veicolo):
    def __init__(self, modello):
        self.modello = modello

    def muovi(self):
        print("mi muovo su strada")

class Areo(Veicolo):
     def __init__(self, capienza):
        self.modello = capienza

     def muovi(self):
        print("mi muovo nel cielo")






def fai_muovere_veicolo(*veicoli):
    print(repr(list(veicoli)))
  
    for veicolo in veicoli:
        veicolo.muovi()


m1 = Macchina("fiata")
a1 = Areo(120)

fai_muovere_veicolo(m1, a1) """




class Studente():

    @classmethod
    def cls_from_string(cls, value):
        name, age, course = value.split("-")
        return cls(name, age, course)
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    @property
    def calc_age(self):
        return 2025-int(self.age)

    @calc_age.setter
    def mod_age(self, new_value):
        if value <= 0:
            raise ValueError("Modifica non valida")
        else:
            self.eta = new_value





s1 = Studente.cls_from_string("Marco-25-Matematica")
print(s1.calc_age)
s1.age = 52
print(s1.calc_age)