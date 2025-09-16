""" Chieda all’utente di inserire un numero intero.
• Converta questo numero in numero decimale (float) e lo stampi. 
• Converta lo stesso numero in stringa e lo stampi insieme a un messaggio. """


int_number = input("Insert a number please? ")
print(float(int_number))
print(f"Questo è il numero inserito ${str(int_number)}")