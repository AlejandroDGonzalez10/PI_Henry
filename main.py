

from fastapi import FastAPI
from typing import Union
import pandas as pd

app = FastAPI(title='API',
              description='API solicitada para proyecto Data Science',
              version='1.1.1')

@app.get('/')  
async def index():
    return {'Proyecto Individual  Data Science realizado por Alejandro Gonzalez cohorte 07'}

movies = pd.read_csv('plataformas_completas.csv')
@app.get("/get_max_duration")

async def get_max_duration(year:int=None, platform:str=None, duration_type:str=None):

    # 1 Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. 
    # (la función debe llamarse get_max_duration(year, platform, duration_type))
    
    # Aplicar los filtros opcionales al dataframe
    if year:
        movies = movies[movies['release_year'] == year]
    if platform:
        movies = movies[movies['platform'] == platform]
    if duration_type:
        movies = movies[movies['duration_type'] == duration_type]
    max_duration = movies['duration_int'].max()
    titulo = movies.loc[movies['duration_int'] == max_duration, 'title'].iloc[0]
    
    return titulo

@app.get("/get_score_count")

async def get_score_count(platform:str,scored:float,year:int):
    
    # 2 Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año 
    # (la función debe llamarse get_score_count(platform, scored, year))
    
     # Filtrar las películas que pertenecen a la plataforma y al año especificados
    filtered_df = movies[(movies["platform"] == platform) & (movies["release_year"] == year)]

    # Contar la cantidad de películas con puntaje mayor al valor especificado
    count = filtered_df[filtered_df["score_mean"] > scored].shape[0]

    return int(count)


@app.get('/get_count_platform')


async def get_count_platform(platform:str):
    
    # 3 Cantidad de películas por plataforma con filtro de PLATAFORMA. 
    # (La función debe llamarse get_count_platform(platform))

    # Filtrar las películas que pertenecen a la plataforma especificada
    movies_filtered = movies[movies["platform"] == platform]

    # Contar la cantidad de películas por plataforma
    count_by_platform = movies_filtered["platform"].value_counts()

    return int(count_by_platform[platform])





@app.get('/get_actor/{platform}/{year}')

async def get_actor3(platform: str, year: int):
    
    # 4 Actor que más se repite según plataforma y año. 
    # (La función debe llamarse get_actor(platform, year))
    
    # Filtrar el DataFrame según plataforma y año
    movies_filtered = movies[(movies['platform'] == platform) & (movies['release_year'] == year)]
    # Verificar si el DataFrame filtrado no está vacío
    if len(movies_filtered) == 0:
        return f"No se encontraron resultados para la plataforma {platform} en el año {year}"
    # Crear un diccionario para contar la cantidad de veces que aparece cada actor
    actor_count = {}
    for row in movies_filtered.iterrows():
        cast = row[1]['cast']
        if isinstance(cast, str):
            actors = cast.split(',')
            for actor in actors:
                if actor in actor_count:
                    actor_count[actor] += 1
                else:
                    actor_count[actor] = 1
    # Verificar si el diccionario de conteo está vacío
    if len(actor_count) == 0:
        return f"No se encontraron actores para la plataforma {platform} en el año {year}"
    # Obtener el actor que más se repite
    max_actor = max(actor_count, key=actor_count.get)
    return max_actor