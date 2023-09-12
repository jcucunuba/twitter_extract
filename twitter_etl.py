import tweepy
import pandas as pd

# Variables de autenticación

def run_twitter_etl():
    consumer_key = "{inser_consumer_key}"
    consumer_secret = "{insert_consumer_secret}"
    access_token = "{insert_access_token}"
    access_token_secret = "{insert_access_token_secret}"

    # Autenticación de Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Creación de objeto API
    api = tweepy.API(auth)

    def get_tweets(username, num_tweets):
        tweets = api.user_timeline(screen_name=username, count=num_tweets, tweet_mode="extended")
        tweet_data = []
        for tweet in tweets:
            tweet_data.append([tweet.created_at, tweet.full_text])

        df = pd.DataFrame(tweet_data, columns=["Fecha", "Tweet"])
        return df

    # Obtener los últimos 50 tweets de un usuario y guardarlos en un archivo CSV
    user_name = input("Ingresa el nombre de usuario de Twitter: ")
    df_tweets = get_tweets(user_name, 50)

    csv_file_name = f"{user_name}_tweets.csv"
    df_tweets.to_csv(csv_file_name, index=False)
    print(f"Los últimos 50 tweets de {user_name} se han guardado en el archivo {csv_file_name}.")
