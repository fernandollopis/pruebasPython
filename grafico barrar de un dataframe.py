# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:15:09 2020

@author: Fernando
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
# Estableciendo directorio de trabajo
os.chdir('C:\\Users\\Fernando\\Documents\\ejemplospython\estadistica con python')
os.getcwd()
#Leer los datos


class2020 = pd.read_excel("COVIDCYLv2.xlsx")



print (class2020.head()) #Devuelve las cinco primeras filas

print (class2020.loc[1:2000,'fecha':'provincia'])
#print(class2020.groupby('provincia').groups)

irene_mola = class2020[class2020['provincia']=='Burgos']
irene_mucho = class2020[['provincia', 'nuevos_positivos', 'fecha']]

irene_mola_mucho = class2020[['provincia', 'nuevos_positivos']][class2020['fecha']=='2020-11-02']

#plt.bar (irene_mola_mucho['provincia'],irene_mola_mucho['nuevos_positivos'])
columnas = class2020.columns

provincias = irene_mucho['provincia'].unique()

for x in range(0,len(provincias)):
    plt.plot(irene_mucho['fecha'][irene_mucho['provincia']==provincias[x]],irene_mucho['nuevos_positivos'][irene_mucho['provincia']==provincias[x]], label = provincias[x])
    

#plt.plot(irene_mucho['fecha'][irene_mucho['provincia']=='Burgos'],irene_mucho['nuevos_positivos'][irene_mucho['provincia']=='Burgos'],label='Burgos')
#plt.plot(irene_mucho['fecha'][irene_mucho['provincia']=='Burgos'],irene_mucho['nuevos_positivos'][irene_mucho['provincia']=='Segovia'], label = 'Segovia')
plt.legend()