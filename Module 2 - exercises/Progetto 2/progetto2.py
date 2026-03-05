import pandas as pd
import numpy as np

np.random.seed(42)

clienti_df = pd.DataFrame({
    'ClienteID': np.arange(1, 5001),
    'Regione': np.random.choice(['Nord', 'Centro', 'Sud', 'Isole'], 5000),
    'Segmento': np.random.choice(['Consumer', 'Corporate', 'Home Office'], 5000)
})
clienti_df.to_csv('clienti.csv', index=False)

prodotti_df = pd.DataFrame({
    'ProdottoID': np.arange(1, 21),
    'Categoria': np.random.choice(['Elettronica', 'Abbigliamento', 'Casa', 'Sport'], 20),
    'Fornitore': np.random.choice(['FornitoreA', 'FornitoreB', 'FornitoreC'], 20),
    'Prezzo': np.random.uniform(5.0, 150.0, 20).round(2)
})
prodotti_df.to_json('prodotti.json', orient='records')

ordini_df = pd.DataFrame({
    'ClienteID': np.random.randint(1, 5001, 100000),
    'ProdottoID': np.random.randint(1, 21, 100000),
    'Quantità': np.random.randint(1, 10, 100000),
    'DataOrdine': pd.to_datetime(np.random.randint(1672531200, 1704067200, 100000), unit='s')
})
ordini_df.to_csv('ordini.csv', index=False)

ordini = pd.read_csv('ordini.csv')
prodotti = pd.read_json('prodotti.json')
clienti = pd.read_csv('clienti.csv')

df_unificato = ordini.merge(prodotti, on='ProdottoID', how='inner')
df_unificato = df_unificato.merge(clienti, on='ClienteID', how='inner')

df_unificato['ClienteID'] = pd.to_numeric(df_unificato['ClienteID'], downcast='unsigned')
df_unificato['ProdottoID'] = pd.to_numeric(df_unificato['ProdottoID'], downcast='unsigned')
df_unificato['Quantità'] = pd.to_numeric(df_unificato['Quantità'], downcast='unsigned')
df_unificato['Prezzo'] = pd.to_numeric(df_unificato['Prezzo'], downcast='float')
df_unificato['DataOrdine'] = pd.to_datetime(df_unificato['DataOrdine'])

colonne_categoriche = ['Categoria', 'Fornitore', 'Regione', 'Segmento']
df_unificato[colonne_categoriche] = df_unificato[colonne_categoriche].astype('category')

df_unificato['ValoreTotale'] = df_unificato['Prezzo'] * df_unificato['Quantità']

df_filtrato = df_unificato[df_unificato['ValoreTotale'] > 100]
