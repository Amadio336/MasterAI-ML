import pandas as pd
import numpy as np

# Preparazione dei dataset fittizio 
np.random.seed(42)


n_righe = 20
date = pd.date_range(start='2024-01-01', periods=n_righe, freq='D')
prodotti = ['Laptop_A', 'Mouse_B', 'Monitor_C', 'Tastiera_D']

data = {
    'Data': np.random.choice(date, n_righe),
    'Prodotto': np.random.choice(prodotti, n_righe),
    'Vendite': np.random.randint(1, 10, n_righe).astype(object), # Object per inserire errori testuali
    'Prezzo': np.random.uniform(50, 1500, n_righe)
}

df = pd.DataFrame(data)


# A. Valori Mancanti (NaN)
df.loc[2, 'Prezzo'] = np.nan
df.loc[5, 'Vendite'] = np.nan
df.loc[8, 'Prodotto'] = np.nan


# --------------------------------------------------------------------
# inizio analisi
# -------------------------------------------------------------------
# ordino df in base alla data
df = df.sort_values(by="Data", ascending=True)


# informazioni
""" print(df.head())
print(df.info())
print(df.describe()) """

# gestisco Nan delle vendite con la media
media_vendite = df["Vendite"].mean()
df["Vendite"] = df["Vendite"].fillna(media_vendite).astype("int8")

# gestisco Nan dei prezzi con la media
media_prezzi = df["Prezzo"].mean()
df["Prezzo"] = df["Prezzo"].fillna(media_prezzi)


#vendite totali per prodotto
gruppo_prodotto = df.groupby("Prodotto")
vendite_per_prodotto = gruppo_prodotto["Vendite"].sum()
print(vendite_per_prodotto)


#prodotto più e meno venduto
quantità_max_vendite = df["Vendite"].max()
print(df[df["Vendite"] == quantità_max_vendite])


#prodotto meno venduto
quantità_min_vendite = df["Vendite"].min()
print(df[df["Vendite"] == quantità_min_vendite])


# Media vendite giornaliera
# 1. Raggruppa per data e calcola il TOTALE di ogni giorno
vendite_per_giorno = df.groupby('Data')['Vendite'].sum()

# 2. Ora calcola la MEDIA di quei totali
media_giornaliera = vendite_per_giorno.mean()

