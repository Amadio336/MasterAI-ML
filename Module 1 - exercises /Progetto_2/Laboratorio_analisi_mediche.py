import numpy as np

class Analisi:
    def __init__(self, tipo, risultato):
        self.tipo = tipo.lower()
        self.risultato = risultato

    def valuta(self):
        """Stabilisce se il valore è nella norma (criteri esemplificativi)."""
        if self.tipo == "glicemia":
            return "Nella norma" if 70 <= self.risultato <= 100 else "Fuori soglia"
        elif self.tipo == "colesterolo":
            return "Nella norma" if self.risultato < 200 else "Valore elevato"
        elif self.tipo == "pressione":
            return "Nella norma" if 80 <= self.risultato <= 120 else "Monitorare"
        else:
            return "Parametri non disponibili per questo tipo"

class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, eta, peso, analisi_oggetti=None):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        
        # Lista di oggetti classe Analisi
        self.analisi_effettuate = analisi_oggetti if analisi_oggetti else []
        
        # Creiamo l'array NumPy estraendo i valori numerici dalle analisi
        self.risultati_analisi = np.array([a.risultato for a in self.analisi_effettuate])

    def scheda_personale(self):
        return (f"--- SCHEDA PAZIENTE ---\n"
                f"Paziente: {self.nome} {self.cognome}\n"
                f"CF: {self.codice_fiscale}\n"
                f"Età: {self.eta} anni | Peso: {self.peso} kg")

    def statistiche_analisi(self):
        """Calcola statistiche sui valori numerici usando NumPy."""
        if self.risultati_analisi.size == 0:
            return "Nessun dato numerico disponibile."
        
        return {
            "media": np.mean(self.risultati_analisi),
            "minimo": np.min(self.risultati_analisi),
            "massimo": np.max(self.risultati_analisi),
            "deviazione_standard": np.std(self.risultati_analisi)
        }

class Medico:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente):
        print(f"\n[VISITA] Il Dott. {self.cognome} ({self.specializzazione}) "
              f"sta visitando il paziente {paziente.nome} {paziente.cognome}.")

# --- ESEMPIO DI UTILIZZO COMPLETO ---

# 1. Creiamo una serie di analisi per un paziente
esami_rossi = [
    Analisi("Glicemia", 95),
    Analisi("Glicemia", 110),
    Analisi("Glicemia", 105),
    Analisi("Glicemia", 88)
]

# 2. Creiamo il paziente passando la lista di oggetti Analisi
paziente1 = Paziente("Mario", "Rossi", "RSSMRA80A01H501U", 44, 78.5, esami_rossi)

# 3. Creiamo il medico
medico1 = Medico("Elena", "Bianchi", "Medicina Generale")

# --- TEST DEI METODI ---

# Stampa scheda e visita
print(paziente1.scheda_personale())
medico1.visita_paziente(paziente1)

# Valutazione singole analisi
print("\nDETTAGLIO ANALISI:")
for esame in paziente1.analisi_effettuate:
    print(f"- {esame.tipo.capitalize()}: {esame.risultato} -> {esame.valuta()}")

# Calcolo statistiche con NumPy
stats = paziente1.statistiche_analisi()
print("\nSTATISTICHE NUMERICHE (NumPy):")
if isinstance(stats, dict):
    print(f"  > Media: {stats['media']:.2f}")
    print(f"  > Massimo: {stats['massimo']}")
    print(f"  > Minimo: {stats['minimo']}")
    print(f"  > Deviazione Standard: {stats['deviazione_standard']:.2f}")