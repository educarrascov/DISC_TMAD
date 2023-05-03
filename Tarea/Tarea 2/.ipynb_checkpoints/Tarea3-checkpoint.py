#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Nombre y rut de los participantes

# Nombre: Eduardo Carrasco Vidal
# Rut: 17072761-4

# Nombre: Ricardo Corbinaud Antúnez
# Rut: 19522614-8

# Instrucciones del módulo 
if __name__ == "__main__":
    
    print("Módulo con 2 funciones denominadas getInfo y makeHistogram que muestran lo siguiente:","\n",
         "1.- getInfo(nombre_archivo, nombre_columna), ingresar nombre del archivo y nombre de la columna en el archivo, entregando una lista de la información completa de la columna del archivo o una lista vacía en caso de que no haya información de la columna o no haya información del archivo (En este último caso imprime un mensaje de que no se encuetra en el directorio de búsqueda).", "\n",
         "2.- makeHistogram(lista), ingresa la lista (puede ser la lista de la función getInfo) y entrega información en un formato de histograma. Entrega mínimo, promedio con desviación estándar y máximo si son datos númericos, una lista de datos ordenada si son datos de texto y lista vacía si no hay elementos.")

def getInfo(nombre_archivo, nombre_columna):

# Abrir el archivo en modo lectura y verificar si existe; sino imprime archivo que no existe
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            archivo.close()
    
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encuentra en el directorio de búsqueda")
        return []
    
# Obtener los nombres de las columnas de la primera línea del archivo
    nombres_columnas = lineas[0].strip().split(",")

# Encontrar el índice de la columna solicitada
    try:
        indice_columna = nombres_columnas.index(nombre_columna)
    except ValueError:
        return []

# Obtener la información de la columna solicitada
    informacion_columna = []
    for linea in lineas[1:]:
        datos_linea = linea.strip().split(",")
        informacion_celda = datos_linea[indice_columna]

# Convertir la información de la celda a flotante si es posible
        try:
            informacion_celda = float(informacion_celda)
        except ValueError:
            pass
        informacion_columna.append(informacion_celda)
    return informacion_columna

def makeHistogram(lista):

# Importar librería numpy para recorrer y calcular mínimo, promedio, desviación estándar y máximo
    import numpy as np

# Comprobar si la lista está vacía
    if not lista:
        print("lista vacía")
        return

# Comprobar si los datos son numéricos o de texto
    if isinstance(lista[0], (int, float)):

# Si los datos son numéricos, calcular: mínimo, promedio con desviación estándar y máximo
        lista = np.array(lista)
        print(f"minimo: {np.min(lista):.2f}")
        print(f"promedio: {np.mean(lista):.2f} +- {np.std(lista):.2f}")
        print(f"maximo: {np.max(lista):.2f}")
    else:

# Si los datos son de texto, contar cada elemento y mostrar en formato de histograma
        histograma = {}
        total = len(lista)

# Contar los eventos de cada elemento en la lista
        for i in lista:
            if i in histograma:
                histograma[i] += 1
            else:
                histograma[i] = 1

# Ordenar alfabéticamente los elementos del histograma
        elementos_ordenados = sorted(histograma.keys())

# Calcular el porcentaje de cada elemento y mostrarlo en el histograma
        for elemento in elementos_ordenados:
            porcentaje = histograma[elemento] / total * 100
            print(f"{elemento}: {porcentaje:.2f}%")


# In[ ]:




