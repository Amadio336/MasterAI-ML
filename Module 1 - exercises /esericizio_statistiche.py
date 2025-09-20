""" calcola , numero totale paprole, frequenza parole, parole uniche, lunghezza media delle parole, mostrare le 5 parole più frequenti """

testo = input("Inserisci il tuo testo: ")


def text_analysis(testo):
    parole = testo.split(" ")
    print(parole)
    print(f"il numero totale di parole è: {len(parole)}")
    
    frequenze = {}
    for parola in parole:
        if parola not in frequenze:
            frequenze[parola] = 0
        frequenze[parola]+=1
    
    print(f"le frequenze di tutte le parole sono: {frequenze}")
    
    print("prime cinque parole per frequenza: ")
    n = 0
    for chiave, valore in frequenze.items():
        if n != 5:
            print(chiave, valore)
            n+=1
        elif n == 5:
            break
        
    """ lunghezza media parole """
    counter = 0
    for parola in parole:
        counter += len(parola)
    lunghezza_media = counter / len(parole)
    print(f"la lunghezza media è {lunghezza_media}")
            

        
        
    
    
    
    parole_uniche = set(parole)
    print(f"le parole uniche sono: {parole_uniche}")
    
    
       
    
        
        
text_analysis(testo)
    
