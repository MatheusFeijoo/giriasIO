#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Abrindo CSV
import csv
import pandas as pd

with open('arquivos/girias.csv', 'r', encoding="utf-8") as csvGirias:
    reader1 = csv.reader(csvGirias)
    read = []
    for row in reader1:
        if len(row) != 0:
            read = read + [row]
            
csvGirias.close()
df = pd.DataFrame(read)
df.rename(columns={'0':'giria','1':'significado','2':'sinonimos','3':'nome','4':'lugar','5':'idade'})
print(df[0])
