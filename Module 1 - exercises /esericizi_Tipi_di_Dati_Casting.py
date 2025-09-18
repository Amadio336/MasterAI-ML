""" ESERCIZI • Crea una variabile con il tuo nome e stampala. 
• Chiedi all’utente la sua età e stampala raddoppiata.
 • Crea due numeri e stampa la loro somma. """


nome = "Amadio"
print(nome)

eta_utente = int(input("Età: "))
print(eta_utente*2)

x,y = 10,6
print(x+y)

""" Crea una variabile x con valore
 7 e una y con valore 3. Stampa la somma dei due numeri. 
 • Crea una variabile prezzo con valore 19.99 e una quantità con valore 
 3. Stampa il totale (prezzo × quantità). 
 • Crea una variabile numero con valore 10.
  Stampa True se il numero è maggiore di 5, altrimenti False. 
  • Prova a combinare un int e un float: assegna a a = 5 e b = 2.5,
   poi calcola la loro somma """

x,y = 3,7
print(x+y)

prezzo = 19.99
quantita = 3
print(prezzo*quantita)

var1 = 10
print(var1 > 5)

a = 5
b = 2.5

print(a+b)


""" Chieda all’utente di inserire un numero intero.
• Converta questo numero in numero decimale (float) e lo stampi. 
• Converta lo stesso numero in stringa e lo stampi insieme a un messaggio. """


int_number = input("Insert a number please? ")
print(float(int_number))
print(f"Questo è il numero inserito ${str(int_number)}")


""" Chiedi una frase e inverti l’ordine delle parole
 • Controlla se la frase è un palindromo (ignora spazi e maiuscole) """

var = input("Scrivi una frase")
var_reversed = var[::-1]

print(var == var_reversed)


""" scrivi un programma che chieda all'utente l'eta e se ha la patente. Printa se può guidare o no """
license_availability = input("Patente? [Si, No]")
eta = int(input("età: "))

judgement = (license_availability == "Si") and (eta >= 18)

print("Possibilità di guidare", judgement)


''' utente può entrare in biblioteca > se non è in ritardo con la restituzione or è premium '''



delay = input("Ritardo: [si, no]")
isPremium = input("Premium: [si, no]")


judgement = (delay == "no") or (isPremium == "si")
print(judgement)  



''' Chiede all’utente quanti euro ha. 
• Chiede il prezzo di un singolo oggetto. 
• Usa // per calcolare quante unità può comprare. 
• Usa % per calcolare quanti euro restano '''

money_av = int(input("L'articolo costa € 7. Inserire Fondi disponibili: € "))
print("Può comprare", money_av // 7, "articolo/i")
print("Resto", money_av % 7, "€")




''' Scrivi un programma che: • Ha una variabile eta. 
• Se eta < 18 stampa “Sei minorenne”.
 • Se eta è almeno 18 ma meno di 65 stampa “Sei adulto”. 
 • Altrimenti stampa “Sei anziano”. '''

eta = input("eta")

if int(eta) < 18:
    print("sei minorenne")
elif 18 <= int(eta) <=65:
  print("sei adulto")
elif int(eta) > 65:
  print("sei anziano")



""" Prova a scrivere un programma utilizzando il ciclo while che:
 Chiede all’utente di inserire un numero positivo. Continua a
  chiedere finché l’utente non inserisce un numero positivo (> 0). 
  Quando il numero è positivo, stampa: "   
  Hai inserito il numero positivo: X" e termina. """


n = int(input("Inserisci numero positivo:"))
while n <= 0:
  print(f"il numero {n} non è positivo, riprova")
  n = int(input("Inserisci numero positivo:"))
else:
  print("il numero è positivo.")




''' calcola la somma delle cifre di un numero '''

number_str = input("Inserisci un numero: ")
i = 0
counter = 0
print(int(number_str[1]))
while i < len(number_str):
  counter += int(number_str[i])
  i += 1
print(counter) 



""" Ha una lista di nomi. Stampa ogni nome preceduto
 dal proprio numero d’ordine
 (es. 1. Alice). Usa enumerate() per ottenere numero e nome """


names = ["Alice", "Bob", "Charlie", "David", "Eve"]

for index, name in enumerate(names):
    print(f"{index} {name}")




""" crea lista di 5 numeri, sostituisci il terzo e stampa """

numeri = [1,2,3,4,5]
numeri[2] = 17
print(numeri)





""" crea tupla con 3 colori, stampa primo e ultimo. conta il colore che si ripete """
color_tuple = "rosso", "giallo", "rosso"
print(f" primo elemento: {color_tuple[0]}, ultimo elemento: {color_tuple[-1]}")

for element in color_tuple:
  print(color_tuple.count(element))





''' Immaginiamo due corsi universitari: Corso A e Corso B. 
Vogliamo sapere: 
Chi frequenta entrambi i corsi. 
Chi frequenta solo il corso A. 
Chi frequenta solo il corso B. 
Chi frequenta almeno un corso. 
Quanti studenti unici ci sono in totale -> domanda mal posta'''

corsoA = {"Alice", "Bob", "Charlie", "David", "Eve"}
corsoB = {"Bob", "David", "Eve", "Frank", "Grace"}


print("chi frequenta entrambi",corsoA.intersection(corsoB))
print(f"chi frequenta solo A: {corsoA.difference(corsoB)}")
print(f"chi frequenta solo B: {corsoB.difference(corsoA)}")
print(f"chi frequenta almeno un corso: {corsoA.union(corsoB)}")
print(f"quanti studenti unici ci sono in totale: {len(corsoA.union(corsoB))}")
