import pandas as pd
import numpy as np

datos= {'Nombre':['Leonardo','Joaquin','Alex','Paula','Enrique', 'Jhon'],
        'Materias':['Lenguaje','EDF','Química','Matemáticas','Inglés','Historia'],
        'Calificaciones':['18','20','13','19','16','17'],
        'Deportes':['Fútbol','Natación','Tenis','Voley','Natación','Balón Mano']
        }
df= pd.DataFrame(datos)
print(df)
print('\n'*4)

#DATOS NO VÁLIDOS
datos2= {'Nombre':['Leonardo','Joaquin','Alex','Paula','Enrique', 'Jhon'],
        'Materias':['Lenguaje','EDF','Química','Matemáticas','Inglés','Historia'],
        'Calificaciones':['18','20',np.nan,'19','16','17'],
        'Deportes':['Fútbol','Natación','Tenis','Voley','N/A','Balón Mano']
        }
df2=pd.DataFrame(datos2)
print(df2)
print('\n'*1)
print(df2.info())

#ESTADÍSTICAS BÁSICAS
print(df2.describe())
print('n'*4)
nuevo= pd.DataFrame(df2)
nuevo=nuevo.replace(np.nan,"0")
print (nuevo)
#ELIMINAR REGISTRO POR COLUMNAS
columna= df2[df2['Nombre']!='Joaquin']
print(columna)
#CONVERTIR LOS NUMEROS A ENTEROS
df['Calificaciones']=df.Calificaciones.astype(int)
print(df.describe())

#ESTADISTICAS INDIVIDUALES
print("Promedio:", df['Calificaciones'].mean())








