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

def pegaDic():
    with open('arquivos/dicionario.csv', 'r', encoding="utf-8", errors="ignore") as csvDic:
        csv_lendo = list(csv.reader(csvDic))
    csvDic.close()
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
    print (words)
    
    # Chama o arquivo de gírias
    girias = pegaGirias()
    giriasTamanho = len(girias)

    dicio = pegaDic()
    dicioTamanho = len(dicio)
    #####
    #  
    #   Ainda falta comparar com o dicionário em português
    #
    #####
    tempo = ' '
    for i in range(fraseTamanho):
        for j in range(giriasTamanho):
            if(girias[j][0] in words[i]):
                if(girias[j][0] == words[i]):
                    for w in range(dicioTamanho):
                        if(girias[j][0] == dicio[w]):
                            fraseTemp = "A palavra *"+ girias[j][0] +"* pode ser uma gíria! \nSeu significado é: \n*"+ (girias[j][1]) + "*\n\n"
                            tempo = tempo + fraseTemp
                        else:
                           messageTroc = message.replace(girias[j][0], girias[j][2])

    return messageTroc



message = "cria subcria tá doido top"

string = tokenFrase(message)

print(string)