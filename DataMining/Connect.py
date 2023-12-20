import tweepy


class ConnectX:
    def __init__(self):
        self.chave_api = 'Yp3ezjMWJC9OCfZFJjlf9tjU9'
        self.secret_api = 'WF1rmMoH65uH9KvfcV9QpSrwyv8DR8Wd9aU53Mx3xXfeR0kaOq'
        self.acess_token = '95677431-RvfVCwXC2YvN7nz1fFmDaDmELoXgxpfJxzjiWkhPW'
        self.acess_secret = 'dFvl0hQrce9H81LyirPvcnTraxBBNKDws11X1Rg13bA3H'


    def conecta(self):
        auth = tweepy.OAuthHandler(self.chave_api, self.secret_api)
        auth.set_access_token(self.acess_token, self.acess_secret)
        api = tweepy.API(auth)
        return api
