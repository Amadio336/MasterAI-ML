""" 
Scrivi una classe Studente con attributi nome e corso, e un metodo presentati() che stampa una frase di presentazione. Esempio di utilizzo: studente1  Studente("Giulia", "Informatica") studente1.presentati

 """

class Studente:
    
    def __init__(self, nome, corso):
        self.nome = nome
        self.corso = corso
      
    
    def presentati(self):
        print(f"Ciao sono {self.nome} e frequento {self.corso}")



Amadio = Studente("Amadio", "informatica")
Amadio.presentati()





''' Crea una classe Persona con attributo “nomeˮ e metodo presentati(). 
● Poi crea una sottoclasse Studente che aggiunge lʼattributo “corsoˮ e lo include nella presentazione. 
● Infine, rendi lʼattributo nome privato e permetti di leggerlo solo tramite un metodo dedicato. '''


class Persona:
  def __init__(self, nome):
    self.__nome = nome
  
  def presentati(self):
    print(f"ciao sono {self.__nome}")

  def getter_nome(self):
    return self.__nome


class Studente(Persona):
  
  def __init__(self, nome, corso):
    super().__init__(nome)
    self.__corso = corso
  
  def presentati(self):
    print(f"Ciao sono {self.getter_nome()} e studio {self.__corso} ")



  
  


studente1 = Studente("Amadio", "informatica")
studente1.presentati()






''' Crea una classe Studente con:
•Attributo di classe scuola = "Liceo Classico"
•Attributo di istanza nome
•Metodo di istanza presentati() che stampa
“Sono X e frequento Yˮ
•Metodo di classe cambia_scuola(cls, nuova_scuola)
 che modifica scuola per tutti gli studenti
 Prova a creare 2 studenti e cambiare la scuola. '''

class Studente:
  scuola = "Liceo Classico"

  def __init__(self, nome):
    self.nome = nome

  def presentati(self):
    print(f"ciao, sono {self.nome} e frequento {self.scuola}")

  @classmethod
  def cambia_scuola(cls, nuova_scuola):
    cls.scuola = nuova_scuola


Luca = Studente("Luca")
Luca.presentati()
Studente.cambia_scuola("Liceo Scientifico")
Luca.presentati()





""" Crea una classe Libro con attributi titolo e autore. •Nel __init__, inizializza i valori •Nel __str__, restituisci una frase tipo: "Titolo: X, Autore: Y" Esempio: libro = Libro("1984", "George Orwell")  print(libro) # Output: Titolo: 1984, Autore: George Orwell """

class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        
    def __str__(self):
        return f"titolo: {self.titolo}, autore: {self.autore}"
    
    
libro1 = Libro("1984", "Orwell")
print(libro1)



""" Crea una classe Automobile con: • Variabile di classe ruote = 4 • Variabile di istanza modello Crea due automobili con modelli diversi e stampa il numero di ruote e i modelli. """

class Automobile:
    numero_ruote = 4
    
    def __init__(self, modello):
        self.modello = modello
        
        
        
auto1 = Automobile("renegade")
auto2 = Automobile("panda")

Automobile.numero_ruote = 45
print(auto1.modello, auto1.numero_ruote)
print(auto2.modello, auto2.numero_ruote)





""" Crea una classe ContoBancario con: 
• Attributo privato __saldo 
• Metodo deposita(importo) che aggiunge soldi solo se > 0 
• Metodo preleva(importo) che riduce il saldo solo se sufficiente 
Simula alcune operazioni di deposito e prelievo """

class ContoBancario:
    def __init__(self, saldo):
        self.__saldo = saldo
        
    def mostra_saldo_getter(self):
        return self.__saldo
    
    def deposita(self, deposito):
        if deposito > 0:
            self.__saldo += deposito
            print("deposito effettuato")
            print(self.mostra_saldo_getter())
            
    def preleva(self, prelievo_v):
        if self.__saldo >= prelievo_v:
            self.__saldo -= prelievo_v
            print("prelievo eseguito")
            print(self.mostra_saldo_getter())
    
    

conto1 = ContoBancario(0)
conto1.deposita(10)
conto1.preleva(30)
print(conto1.__dict__)


