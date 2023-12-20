import tweepy


class ConnectX:
    def __init__(self):
        


    def conecta(self):
        auth = tweepy.OAuthHandler(self.chave_api, self.secret_api)
        auth.set_access_token(self.acess_token, self.acess_secret)
        api = tweepy.API(auth)
        return api
