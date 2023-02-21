
# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

¡Bienvenidos al primer proyecto individual de la etapa de labs! En esta ocasión, deberán hacer un trabajo situándose en el rol de un ***MLOps Engineer***.  

<hr>  



## **Propuesta de trabajo (requerimientos de aprobación)**

**`Transformaciones`**:  Para este MVP no necesitas perfección, ¡necesitas rapidez! ⏩ Vas a hacer estas, ***y solo estas***, transformaciones a los datos:


+ Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

<br/>

**`Desarrollo API`**:   Propones disponibilizar los datos de la empresa usando el framework ***FastAPI***. Las consultas que propones son las siguientes:

+ Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))

+ Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))

+ Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))


<br/>


**`Deployment`**: Tus compañeros cercanos han usado [Deta](https://www.deta.sh/?ref=fastapi) para hacer el deployment de aplicaciones, además, no necesita dockerizacion así que es el primer candidato que encuentras!

Tambien sabes sobre [Railway](https://railway.app/) y [Render](https://render.com/docs/free#free-web-services) , aunque estos necesitan dockerizacion #Decisiones 👀

<br/>

**`Análisis exploratorio de los datos`**: _(Exploratory Data Analysis-EDA)_

Ya los datos están limpios, ahora es tiempo de investigar las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías (que no tienen que ser errores necesariamente :eyes: ), y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior.  Sabes que puedes apoyarte en librerías como _pandas profiling, sweetviz, autoviz_, entre otros y sacar de allí tus conclusiones 😉

**`Sistema de recomendación`**: 

Una vez que toda la data es consumible por la API ya lista para consumir para los departamentos de Analytics y de Machine Learning, y nuestro EDA bien realizado entendiendo bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas para usuarios, donde dado un id de usuario y una película, nos diga si la recomienda o no para dicho usuario. De ser posible, este sistema de recomendación debe ser deployado para tener una interfaz gráfica amigable para ser utilizada, utilizando Gradio o Deta Space para su deployment o bien con alguna solución como Streamlit o algo similar en local (tener el deployment del sistema de recomendación o una interfaz gráfica es un plus al proyecto).

<br/>

**`Video`**: Sabes que la documentacion es una etapa importante en cualquier trabajo 👀. Hiciste diversos procesos nuevos para la empresa y no tienes tiempo de dejar un informe con toda la informacion relevante en este momento! Pero eres recursivo 🙂, asi que grabas un video donde muestras todo lo que hiciste para mostrarselo a tu equipo y asi tod@s pueden enteder todo lo que hiciste y para que lo hiciste.

<sub> **Spoiler**: El video DEBE durar no mas de ***7 minutos*** y DEBE mostrar las consultas requeridas en funcionamiento desde la API** y una breve explicacion del modelo entrenado para el sistema de recomendacion. <sub/>

<br/>

## **Criterios de evaluación**

**`Código`**: Prolijidad de código, uso de clases y/o funciones, en caso de ser necesario, código comentado. 

**`Repositorio`**: Nombres de archivo adecuados, uso de carpetas para ordenar los archivos, README.md presentando el proyecto y el trabajo realizado

**`Cumplimiento`** de los requerimientos de aprobación indicados en el apartado `Propuesta de trabajo`

NOTA: Recuerde entregar el link de acceso al video. Puede alojarse en YouTube, Drive o cualquier plataforma de almacenamiento. **Verificar que sea de acceso público**.

<br/>

## **Fuente de datos**

+ [Dataset](https://drive.google.com/drive/folders/1b49OVFJpjPPA1noRBBi1hSmMThXmNzxn): La carpeta 'ratings' tiene varios archivos con las reseñas de los usuarios, la carpeta raíz tiene un dataset por proveedor de servicios de streaming.
<br/>

## **Material de apoyo**

Imagen Docker con Uvicorn/Guinicorn para aplicaciones web de alta performance:

+ https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/ 

+ https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

FAST API Documentation:

+ https://fastapi.tiangolo.com/tutorial/
  
 Gradio:
  
+ https://gradio.app/
  
 Sistemas de Recomendación:
  
+ https://github.com/juliom86/awesome-RecSys

"Prolijidad" del codigo:

+ https://pandas.pydata.org/docs/development/contributing_docstring.html
  

  PD: Faltaron DetaSpace.
      y muchas cosas lamentablemente mi equipo dificultp muchisimo el procesamiento y transformacion de datos, junto con la pruebas de las plataformas. 
      tambien por falta de conocimiento no pude subir el archivo df_prc.parquet donde estan los 8 csv de score.
      desde ya muchas Gracias.!
