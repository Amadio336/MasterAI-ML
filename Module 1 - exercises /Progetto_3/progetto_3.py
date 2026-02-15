import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

np.random.seed(42)
random.seed(42)

nome = "Mario Rossi"
eta = 34
saldo = 2500.75
vip = True

destinazioni = ["Parigi", "Tokyo", "New York", "Il Cairo", "Roma"]
prezzi_medi = {
    "Parigi": 450.0,
    "Tokyo": 1200.0,
    "New York": 950.0,
    "Il Cairo": 600.0,
    "Roma": 300.0
}

class Cliente:
    def __init__(self, nome, eta, vip):
        self.nome = nome
        self.eta = eta
        self.vip = vip

    def info(self):
        print(f"Cliente: {self.nome}, Età: {self.eta}, VIP: {self.vip}")

class Viaggio:
    def __init__(self, destinazione, prezzo, durata):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata = durata

class Prenotazione:
    def __init__(self, cliente, viaggio):
        self.cliente = cliente
        self.viaggio = viaggio
        self.prezzo_finale = self.calcola_importo()

    def calcola_importo(self):
        importo = self.viaggio.prezzo
        if self.cliente.vip:
            importo *= 0.9
        return round(importo, 2)

    def dettagli(self):
        self.cliente.info()
        print(f"Destinazione: {self.viaggio.destinazione}")
        print(f"Durata: {self.viaggio.durata} giorni")
        print(f"Prezzo finale: {self.prezzo_finale} euro")

c1 = Cliente(nome, eta, vip)
v1 = Viaggio("Tokyo", prezzi_medi["Tokyo"], 14)
p1 = Prenotazione(c1, v1)
p1.dettagli()

prenotazioni_sim = np.random.uniform(200, 2000, 100)

print(f"Prezzo medio: {np.mean(prenotazioni_sim):.2f}")
print(f"Min: {np.min(prenotazioni_sim):.2f}, Max: {np.max(prenotazioni_sim):.2f}")
print(f"Deviazione standard: {np.std(prenotazioni_sim):.2f}")
print(f"Sopra media: {np.sum(prenotazioni_sim > np.mean(prenotazioni_sim))}%")

nomi_clienti = ["Mario", "Luigi", "Anna", "Sofia", "Luca"]
data = []
for _ in range(50):
    dest = random.choice(destinazioni)
    prezzo = round(prezzi_medi[dest] * random.uniform(0.9, 1.1), 2)
    data.append([
        random.choice(nomi_clienti),
        dest,
        prezzo,
        random.randint(1, 30),
        random.randint(3, 14),
        prezzo
    ])

df = pd.DataFrame(data, columns=["Cliente", "Destinazione", "Prezzo", "Giorno_Partenza", "Durata", "Incasso"])

print(f"Incasso totale: {df['Incasso'].sum():.2f}")
print(df.groupby("Destinazione")["Incasso"].mean())
print(df["Destinazione"].value_counts().head(3))

plt.figure()
df.groupby("Destinazione")["Incasso"].sum().plot(kind="bar")
plt.title("Incasso per Destinazione")
plt.show()

plt.figure()
df.groupby("Giorno_Partenza")["Incasso"].sum().sort_index().plot(kind="line", marker="o")
plt.title("Andamento Giornaliero")
plt.show()

plt.figure()
df["Destinazione"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Percentuale Vendite")
plt.show()

categorie = {
    "Parigi": "Europa", "Roma": "Europa",
    "Tokyo": "Asia", "New York": "America", "Il Cairo": "Africa"
}
df["Categoria"] = df["Destinazione"].map(categorie)

print(df.groupby("Categoria")["Incasso"].sum())
print(df.groupby("Categoria")["Durata"].mean())

df.to_csv("prenotazioni_analizzate.csv", index=False)

def top_n_clienti(dataframe, n):
    return dataframe["Cliente"].value_counts().head(n)

print("top dei clienti", top_n_clienti(df, 3))

fig, ax1 = plt.subplots()
cat_group = df.groupby("Categoria")[["Incasso", "Durata"]].mean()

ax1.bar(cat_group.index, cat_group["Incasso"], color="b", alpha=0.6)
ax1.set_ylabel("Incasso Medio", color="b")

ax2 = ax1.twinx()
ax2.plot(cat_group.index, cat_group["Durata"], color="r", marker="o")
ax2.set_ylabel("Durata Media", color="r")

plt.title("Incasso vs Durata per Categoria")
plt.show()
