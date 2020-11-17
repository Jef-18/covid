import xlrd
import pandas as pd

url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx'

df_covid = pd.read_excel(url)

df_covid.columns = ['dataRep', 'dia', 'mes', 'ano', 'casos','mortes', 
 'pais', 'geoId', 'codigoPais', 'populacao_2018', 'continente'
]

print(df_covid.info())
