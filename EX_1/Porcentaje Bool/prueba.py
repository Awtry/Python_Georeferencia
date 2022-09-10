import sqlite3
import pandas as pd
import numpy as np
import json
import collections
import psycopg2

dbname = 'starbucks'
conn = sqlite3.connect(dbname+'.sqlite')
df = pd.read_excel('starbucks_world_stats.xlsx')
cur = conn.cursor()
cur.execute('DROP table IF EXISTS stats;')
df.to_sql(name='stats', con=conn)


cur.execute('SELECT * FROM stats')

listaStats = []
hasCardPayment = 0
cantidadFilas  = 0

for row in cur:
    d = collections.OrderedDict()
    cantidadFilas = cantidadFilas + 1
    d["name"] = row[1]
    d["card_payment"] = row[5]

    if row[5] == 1:  
        hasCardPayment = hasCardPayment+1
        
    listaStats.append(d)

promedio  = (hasCardPayment / cantidadFilas) * 100
porcentaje = '{:.2f}'.format(promedio)

print('El %'+porcentaje+" de los starbucks en cuentan con pago en tarjeta")

j = json.dumps(listaStats)

with open("country_objects.js", "w") as f:
    f.write(j)
    
conn.close()
