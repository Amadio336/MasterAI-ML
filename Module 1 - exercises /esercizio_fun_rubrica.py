""" aggiungere un nuovo contatto
modficare un contatto già esistente
eliminare un contatto
cercare un contatto per nome
vedere tutti i contatti aggiunti
"""

rubrica = []

def aggiungi_contatto(nome,cognome, mail):
    """ aggiunge un nuovo contatto """
    nuovo_contatto = {"nome": nome, "cognome" : cognome, "mail":mail}
    rubrica.append(nuovo_contatto)
    print(f"il contatto {nome} è stato aggiunto")
        
def modifica_contatto(cognome_contatto_dm):
    """ modifica un contatto dato il cognome """    
    
    for contatto in rubrica:
        if contatto["cognome"] == cognome_contatto_dm:
            print("Contatto trovato")
            indice_dm = rubrica.index(contatto)
            break
    else:
        print("Nessun Contatto con quel cognome")
        
            
    option_modify = int(input("Cosa vuoi modificare? 1 Nome 2 Cognome 3 Mail ->  "))
    if option_modify == 1:
        nuovo_nome = input("Inserisci nuovo nome ")
        rubrica[indice_dm]["nome"] = nuovo_nome 
        print("Contatto modificato!")
    if option_modify == 2:
        nuovo_cognome = input("Inserisci nuovo cognome ")
        rubrica[indice_dm]["cognome"] = nuovo_cognome
        print("Contatto modificato!")
    if option_modify == 3:
        nuova_mail = input("Inserisci nuova mail ")
        rubrica[indice_dm]["mail"] = nuova_mail
        print("Contatto modificato!")
          

def rimuovi_contatto(cognome_contatto_dr):
    for contatto in rubrica:
        if contatto["cognome"] == cognome_contatto_dr:
            indice_dr = rubrica.index(contatto)
            del rubrica[indice_dr]
            print("contatto rimosso")
            
def cerca_contatto_by_cognome(cognome_contatto_dv):
    for contatto in rubrica:
        if contatto["cognome"] == cognome_contatto_dv:
            indice_dv = rubrica.index(contatto)
            print(rubrica[indice_dv])
        
            
            
        
    
            

        

while True:
    
    option = int(input("Scegli opzione: 1 Aggiungi Contatto 2 Modifica Contatto 3 Elimina Contatto 4 Ricerca contatto 5 Mostra tutti  6 esci ->  "))
    
    if option == 1:
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        mail = input("Mail: ")
        aggiungi_contatto(nome, cognome, mail)
        
    if option == 2:
        cognome_contatto_dm = input("Digita il cognome del contatto che vuoi modificare ") 
        modifica_contatto(cognome_contatto_dm)
        
    if option == 3:
        cognome_contatto_dm = input("Digita il cognome del contatto che vuoi rimuovere ") 
        rimuovi_contatto(cognome_contatto_dm)
    
    if option == 4:
        cognome_contatto_dv = input("Digita il cognome del contatto che vuoi vedere ") 
        cerca_contatto_by_cognome(cognome_contatto_dv)
        
    if option == 5:
        for contatto in rubrica:
            print(contatto)
        
        
    if option == 6:
        break 
    
    
        

    
    