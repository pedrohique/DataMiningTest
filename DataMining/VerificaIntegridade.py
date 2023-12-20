import pickle

class VerificaIntegridade:
    def __init__(self, tweets):
        self.tweets = tweets
        self.verifica_user()

    def __iter__(self):
        tweet_tuple = tuple(self.tweets)
        for i in tweet_tuple:
            yield i

    def __call__(self, *args, **kwargs):
        return tuple(self.tweets)

    def __len__(self):
        return len(self.tweets)

    def verifica_user(self):
        for tweet in self.tweets:
            total = 0
            if tweet.get('retweet_count', 0) < 50:
                # Se o numero de retweets for maior que X
                nota = 2  
                total += nota


            if not tweet.get('default_profile_image', False):
                # Se não tiver imagem de perfil
                nota = 1
                total += nota


            if not tweet.get('default_profile', False):
                # Se o profile por padrão
                nota = 1
                total += nota

            if not tweet.get('fast_followers_count', False):
                # Se ganhou segdores muito rapido
                nota = 1
                total += nota

            if tweet.get('is_blue_verified', False):
                nota = 3
                total += nota

            if tweet.get('normal_followers_count') != tweet.get('followers_count'):
                nota = 2
                total += nota

            tweet['integridade_usuario'] = total

















