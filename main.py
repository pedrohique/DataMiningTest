from DataMining import DataMining
from DataMining import VerificaIntegridade
from DataMining import CreateFile

def main():
    busca = ('Dario Saadi')
    qtd_pags = 10
    tweets = DataMining.DataMining(busca, qtd_pags)
    tweets = tuple(tweets)
    tweets_verificados = VerificaIntegridade.VerificaIntegridade(tweets)
    CreateFile.ToCSV(tweets_verificados, nome_arquivo=f'{busca}_{qtd_pags}.csv')




if __name__ == '__main__':
    main()


