# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot

def loadVol():
    try:
        r = requests.get('https://apirest-covol19.herokuapp.com/voluntariarse/voluntarios')
        print('Sucess - ', r.status_code)
        return r.json()
    except:
        print("Deu Ruim Man")
        print("Error - ", r.status_code)
        return
def takeCidades(data):
    Cidades = []
    for i in data:
        Cidades.append((i['cidade']))
    return Cidades        

def ClearCidades(ListCity):
    l = []
    for i in ListCity:
        if i not in l:
            if (i != "string" and i != "Teste" and i != "teste" and i != ""):
                l.append(i)
            
    return l
        
def CountVoluntarios(ListCity,data):
    tam = int(len(ListCity))
    VolCity = []
    for i in range(tam):
        cont = int(0)
        for v in data:
            if(v['cidade'] == ListCity[i]):
                cont = int(cont + 1)
                
        VolCity.append(cont)
    return VolCity
        
def OrdenaLista(ListVolCity, ListCity):
    for i in range(len(ListVolCity)):
        aux = ListVolCity[i]
        auxC = ListCity[i]
        k = i
        while k > 0 and aux < ListVolCity[k-1]:
            ListVolCity[k] = ListVolCity[k-1]
            ListCity[k] = ListCity[k-1]
            k = k - 1
        ListVolCity[k] = aux
        ListCity[k] = auxC
    
response = loadVol()
data = np.array(response)
ListCity = takeCidades(data)
ListCity = ClearCidades(ListCity)
ListVolCity = CountVoluntarios(ListCity,data)
OrdenaLista(ListVolCity, ListCity)

matplotlib.pyplot.title('Quantidade De Voluntarios Por Cidade')
matplotlib.pyplot.xlabel('Cidades')
matplotlib.pyplot.ylabel('Quantidade de Voluntarios')
matplotlib.pyplot.plot(ListCity[50:55], ListVolCity[50:55])












