import csv

class ToCSV:
    def __init__(self, tweets, nome_arquivo='Tweets.csv'):
        self.nome_arquivo = nome_arquivo
        self.tweets = tuple(tweets)
        self.cria_arquivo()

    def cria_arquivo(self):
        with open(self.nome_arquivo, 'a', encoding='UTF-8', newline='\n') as myfile:
            fieldnames = self.tweets[0].keys()

            writer = csv.DictWriter(myfile, fieldnames)
            writer.writeheader()
            for tweet in self.tweets:
                writer.writerow(tweet)

