
# --- PARTE 1: Variabili e Tipi di Dati ---

titolo = "Il Signore degli Anelli"
copie = 5
prezzo_medio = 22.50
disponibile = True

print(f"Titolo: {titolo} (Tipo: {type(titolo)})")
print(f"Copie: {copie} (Tipo: {type(copie)})")
print(f"Prezzo: {prezzo_medio} (Tipo: {type(prezzo_medio)})")
print(f"Disponibile: {disponibile} (Tipo: {type(disponibile)})")


# --- PARTE 2: Strutture Dati ---
print("\n--- Parte 2: Strutture Dati ---")


lista_titoli = [
    "Il Signore degli Anelli", 
    "1984", 
    "Il mondo nuovo", 
    "Dune", 
    "Cronache del ghiaccio e del fuoco"
]

print(f"\nLista titoli: {lista_titoli}")

# 2. Dizionario Titolo -> Copie
copie_disponibili_dict = {
    "Il Signore degli Anelli": 5,
    "1984": 3,
    "Dune": 2
}
print(f"\nDizionario copie: {copie_disponibili_dict}")

# 3. Insieme (set) di utenti
utenti_registrati = {"Alice", "Bob", "Charlie", "Alice"} # "Alice" duplicato viene ignorato
print(f"\nSet utenti: {utenti_registrati}")


# --- PARTE 3: Classi e OOP ---
print("\n--- Parte 3: Definizione Classi OOP ---")

class Libro:
    """Modello per un Libro nella biblioteca."""
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self):
        """Restituisce una stringa descrittiva del libro."""
        return f"'{self.titolo}' di {self.autore} ({self.anno}). Copie rimaste: {self.copie_disponibili}"

class Utente:
   
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):

        print(f"--- Scheda Utente ---")
        print(f"Nome: {self.nome}")
        print(f"Età: {self.eta}")
        print(f"ID: {self.id_utente}")

class Prestito:
   
    def __init__(self, utente, libro, giorni):
        self.utente = utente # Questo è un oggetto Utente
        self.libro = libro   # Questo è un oggetto Libro
        self.giorni = giorni

    def dettagli(self):
        """Stampa i dettagli completi del prestito."""
        print(f"\n--- Dettaglio Prestito ---")
        print(f"Utente: {self.utente.nome} (ID: {self.utente.id_utente})")
        print(f"Libro: {self.libro.titolo} di {self.libro.autore}")
        print(f"Durata: {self.giorni} giorni")

print("Classi 'Libro', 'Utente' e 'Prestito' definite con successo.")


# --- PARTE 4: Funzionalità e Simulazione ---
print("\n--- Parte 4: Funzionalità e Simulazione ---")

def presta_libro(utente, libro, giorni):
    """
    Funzione per gestire la logica di un prestito.
    Controlla la disponibilità, aggiorna le copie e crea un Prestito.
    """
    print(f"\n[Tentativo prestito: {utente.nome} richiede '{libro.titolo}']")
    
    # 1. Verifica disponibilità
    if libro.copie_disponibili >= 1:
        # 2. Se sì: riduci copie e crea prestito
        libro.copie_disponibili -= 1
        nuovo_prestito = Prestito(utente, libro, giorni)
        print(f"Successo! '{libro.titolo}' prestato a {utente.nome}.")
        print(f"Copie di '{libro.titolo}' rimaste: {libro.copie_disponibili}")
        return nuovo_prestito
    else:
        # 3. Se no: messaggio di errore
        print(f"Errore: '{libro.titolo}' non ha copie disponibili.")
        return None

# --- INIZIO SIMULAZIONE ---
print("\n--- Creazione Istanze per Simulazione ---")


libro1 = Libro("1984", "George Orwell", 1949, 3)
libro2 = Libro("Dune", "Frank Herbert", 1965, 2)
libro3 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 1)

utente1 = Utente("Alice", 30, "A001")
utente2 = Utente("Bob", 25, "B002")
utente3 = Utente("Charlie", 42, "C003")

print("Creati 3 libri e 3 utenti.")
utente1.scheda() 
# Lista per tenere traccia di tutti i prestiti riusciti
prestiti_attivi = [] 



# Prestito 1
p1 = presta_libro(utente1, libro1, 15)
if p1: 
    prestiti_attivi.append(p1)

# Prestito 2
p2 = presta_libro(utente2, libro2, 10)
if p2: 
    prestiti_attivi.append(p2)

# Prestito 3
p3 = presta_libro(utente3, libro3, 7)
if p3: 
    prestiti_attivi.append(p3)



# 1. L’elenco aggiornato delle copie disponibili per ciascun libro
print("\n" + "="*40)
print("--- Elenco Copie Aggiornato ---")
print(libro1.info())
print(libro2.info())
print(libro3.info())


print("\n" + "="*40)
print("--- Dettagli Prestiti Attivi ---")
if not prestiti_attivi:
    print("Nessun prestito attivo.")
else:
    for prestito in prestiti_attivi:
        prestito.dettagli()

print("\n" + "="*40)
print("Simulazione terminata.")