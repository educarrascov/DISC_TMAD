### Actividad 1:
#######
# Cree una función llamada getInfo que reciba dos parámetros, un argumento es el nombre de
# un archivo csv, y el segundo argumento el nombre de una columna. La función leerá el
# archivo (asuma que el nombre siempre es correcto), y devolverá una **lista** con toda la
# información de la columna solicitada. En caso que el nombre de la columna no exista se
# devolverá una lista vacía.
##########

import pandas as pd
import numpy as np
def getInfo (archivo, columna):
    """archivo en csv y nombre de columna"""
    data_frame = pd.read_csv(archivo, header=0, sep=",", encoding="utf-8")
    if columna not in data_frame.columns:
        return []
    ## Generar descripción de columna
    datos_columna = data_frame[columna]
    
    if datos_columna.dtype == "object":
        lista_valores = datos_columna.tolist()
    else:
        lista_valores = [float(i) for i in datos_columna.tolist()]
        
    return lista_valores

### Actividad 2:
#######
# Cree una función llamada makeHistogram que reciba una lista y genere información dela
# lista recibida. En caso que los datos sean numéricos, se imprimirá por pantalla: el mínimo,
# promedio y desviación estándar, y el máximo de la lista. En caso que sea una lista de strings,
# se mostrará por pantalla el histograma ordenado en forma alfabética. Si la lista está vacía,
# entonces mostrará por pantalla lista vacía..
##########

def makeHistogram(lista):
    """
    En caso valores numéricos, estadísticas básicas.
    En caso valores no numéricos (categóricos), histograma frecuencia.
    """
    if len(lista) == 0:
        print("Lista vacía")
        return
    try:
        valores_numericos = np.array(lista, dtype=float)
        minimo = np.min(valores_numericos)
        promedio = np.mean(valores_numericos)
        desv_estandar = np.std(valores_numericos)
        maximo = np.max(valores_numericos)
        
        print(f"Mínimo: {minimo:.2f}")
        print(f"Promedio: {promedio:.2f} +- {desv_estandar:.2f}")
        print(f"Máximo: {maximo:.2f}")
    except ValueError:
        # Histograma de frecuencias, por valores categóricos
        serie = pd.Series(lista).astype(str)
        frecuencia_absoluta = serie.value_counts(normalize=False).sort_index()
        frecuencia_relativa = serie.value_counts(normalize=True).sort_index() * 100
        
        for categoria, frecuencia_rel in frecuencia_relativa.items():
            print(f"{categoria:<20} {frecuencia_rel:>5.2f}%")

#### Actividad 3:
## Reúna las funciones construidas en las actividades anteriores en un módulo llamado
# “Tarea2.py”. Agregue a su módulo instrucciones que se activen solo cuando se ejecuta
# directamente el módulo (es decir, que no aparezca cuando el módulo es importado)
##

if __name__ == "__main__":
    
    archivo = "DatosT2.csv"
    columna = "workclass"
    lista = getInfo(archivo, columna)
    makeHistogram(lista)