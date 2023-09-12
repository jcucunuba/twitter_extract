# Extractor de Tweets de X (Twitter)

Este es un simple script en Python que te permite obtener los últimos 50 tweets de un usuario de Twitter y guardarlos en un archivo CSV. Utiliza la biblioteca Tweepy para interactuar con la API de Twitter.

## Requisitos

Antes de usar este script, asegúrate de tener instaladas las siguientes bibliotecas de Python:

- Tweepy: Puedes instalarlo con `pip install tweepy`.
- Pandas: Puedes instalarlo con `pip install pandas`.

## Configuración

Antes de ejecutar el script, necesitas configurar tus credenciales de Twitter. Sigue estos pasos:

1. Ve a [Twitter Developer](https://developer.twitter.com/en/apps) y crea una aplicación para obtener tus claves de API y tokens de acceso.

2. Reemplaza las siguientes variables en el código con tus propias credenciales:

   - `consumer_key`: Tu clave de consumidor de Twitter.
   - `consumer_secret`: Tu secreto de consumidor de Twitter.
   - `access_token`: Tu token de acceso de Twitter.
   - `access_token_secret`: Tu secreto de token de acceso de Twitter.

## Uso

1. Ejecuta el script `extract_tweets.py` en tu entorno de Python.

2. Ingresa el nombre de usuario de Twitter del cual deseas obtener los últimos 50 tweets cuando se lo solicite.

3. El script descargará los tweets y los guardará en un archivo CSV con el formato `username_tweets.csv`, donde `username` es el nombre de usuario de Twitter que proporcionaste.

4. Los datos de los tweets se guardarán en dos columnas en el archivo CSV: "Fecha" y "Tweet".


