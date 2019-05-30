import nltk
import csv
from nltk.corpus import stopwords

# Pega gírias do arquivo .csv
####### Ainda falta opção para inserir novas gírias #######
def pegaGirias():
    with open('arquivos/girias.csv', 'r', encoding="utf-8") as csvGirias:
        csv_lendo = list(csv.reader(csvGirias))
    csvGirias.close()
    return csv_lendo

# Parte principal
def tokenFrase(message):

    # Gera os tokens da frase enviada
    token_frase = nltk.word_tokenize(message)
    # Coloca tudo em minusculo
    palavras = [token_frase.lower() for token_frase in token_frase]
    
    #####
    #  
    #   Ainda falta tirar a pontuação
    #
    #####
    #table = str.maketrans('', '', string.punctuation)
    #stripped = [w.translate(table) for w in palavras]
    
    # Tira stopwords
    words = [word for word in palavras if word.isalpha()]
    stop_words = set(stopwords.words('portuguese'))
    words = [w for w in words if not w in stop_words]
    fraseTamanho = len(words)
    
    # Chama o arquivo de gírias
    csvGirias = pegaGirias()
    csv_length = len(csvGirias)
    #####
    #  
    #   Ainda falta comparar com o dicionário em português
    #
    #####
    tempo = ' '
    for i in range(fraseTamanho):
        for j in range(csv_length):
            if(csvGirias[j][0] in words[i]):
                fraseTemp = "\nNesta frase é possível que a palavra "+ csvGirias[j][0] + " seja uma gíria! \n Seu significado é: \n"+ (csvGirias[j][1])
                tempo = tempo + fraseTemp
                
    temp = '\n' + message + tempo
    return temp