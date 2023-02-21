# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import train_test_split

import gc #garbage collector

df = pd.read_parquet('df_pcr.parquet')
df.info()

df.head()

df2 = df.loc[:, ["show_id", "userId", "score","title"]]

df2.head()

# Utilizar factorize para asignar valores numéricos a cada valor único de ID
df2['id'] = pd.factorize(df['show_id'])[0]

df2.head()

"""Genero los dos df para trabajar con el modelo de reomendacion"""

df1 = df2.loc[:,['userId','score','id']]

df_title = df2.loc[:,['id','title']]

df_title.drop_duplicates(inplace=True)

df_title.head(10)

movie_id = 5
titulo = df_title.loc[df_title['id'] == movie_id, 'title'].iloc[0]
print(titulo)

df1.info()

df_title.info()

# Usuarios únicos

print(len(df1['userId'].unique()))

# Calificaciones de películas por usuario

df1_by_users = df1.groupby(['userId']).count()
df1_by_users.head()

#conteo de calificaciones por pelicula/serie

df1_by_movies = df1.groupby(['id']).count()
df1_by_movies.head()

df_title = df_title.set_index('id')

df_title.head()

#titulo mas calificado

idx_max = df1_by_movies['userId'].idxmax()
print(df_title.loc[idx_max].title)

#Cantidad de vistas de cada serie/pelicula

df1_by_movies = df1.groupby(['id']).count()
df1_by_movies.sort_values('userId', ascending = False, inplace = True)
df1_by_movies['Vistos'] = df1_by_movies['userId']
df1_by_movies.drop(columns = ['userId','score'], inplace = True)
df1_by_movies.head(10)

df_title.head(3)

#agrego el titulo a cada fila segun su id

df1_by_movies['Titulo'] = df_title.loc[df1_by_movies.index].title

df1_by_movies.head()

#filtro peliculas que consifero que se vieron poco en funcion de los datos

umbral = 420
mascara_pocos_vistos = df1_by_movies.Vistos<umbral

peliculas_pocos_vistos = mascara_pocos_vistos[mascara_pocos_vistos].index.values
print(len(peliculas_pocos_vistos), peliculas_pocos_vistos)

mascara_descartables = df1.id.isin(peliculas_pocos_vistos)

# Obsevamos cómo cambia la cantidad de registros a partir del filtrado

print(df1.shape)
df1 = df1[~mascara_descartables]
print(df1.shape)

""" Modelo de recomendacion"""

reader = Reader()

N_filas = 200000 # Limitamos el dataset a N_filas

data = Dataset.load_from_df(df1[['userId', 'id', 'score']][:N_filas], reader)

# Separamos nuestros datos

trainset, testset = train_test_split(data, test_size=.25)

# Usaremos un modelo de Singular Value Decomposition

from surprise import SVD
model = SVD()

# Entrenamos el modelo

model.fit(trainset)

# Predecimos

predictions = model.test(testset)

predictions[1]

# Hacemos una predicción al azar para usuario y película

model.predict(1328945,28)

#obtengo el promedio total de los scores 

promedio_score = df1['score'].mean()
print(promedio_score)

#creo la funcion si recomienda o no ver una pelicula en funcion del score promedio y del score predicho por el modelo para ese usuario y esa pelicula

def recomendar_pelicula(id_usuario, id_pelicula, model):


    # Realizar la predicción para el usuario y la película dados
    prediction = model.predict(id_usuario, id_pelicula)
    
    # Obtener la valoración media del usuario para todas las películas que ha visto
    media_usuario = np.array(trainset.ur[trainset.to_inner_uid(id_usuario)])
    
    # Obtener el título de la película
    titulo_pelicula = df_title.loc[id_pelicula].title
    
    # Verificar si la valoración de la película es mayor que la media del usuario
    if prediction.est >3.54:
        return f"Se recomienda ver la película {titulo_pelicula}."
    else:
        return f"No se recomienda ver la película {titulo_pelicula}."

#realizo una recomendacion al azar

recomendar_pelicula(46453,66,model)

# Tomaremos un usuario para hacerle una recomendación

usuario = 46453
rating = 4   # Tomamos películas a las que haya calificado con 4 o 5 estrellas
df_user = df1[(df1['userId'] == usuario) & (df1['score'] >= rating)]
df_user = df_user.reset_index(drop=True)
df_user['Name'] = df_title['title'].loc[df_user.id].values
df_user

recomendaciones_usuario = df_title.iloc[:22860].copy()
print(recomendaciones_usuario.shape)
recomendaciones_usuario.head()

# Debemos extraer las películas que ya ha visto

usuario_vistas = df1[df1['userId'] == usuario]
print(usuario_vistas.shape)
usuario_vistas.head()

if True: # Sacamos las que filtramos
    recomendaciones_usuario.drop(peliculas_pocos_vistos, inplace = True)

recomendaciones_usuario.drop(usuario_vistas.id, inplace = True)
recomendaciones_usuario = recomendaciones_usuario.reset_index()
recomendaciones_usuario.head()

# Recomendamos

recomendaciones_usuario['Estimate_Score'] = recomendaciones_usuario['id'].apply(lambda x: model.predict(usuario, x).est)

# resultado una lista de titulos con los score estimados para este usuarios ordenados de mayor a menor

recomendaciones_usuario = recomendaciones_usuario.sort_values('Estimate_Score', ascending=False)
print(recomendaciones_usuario.head(10))