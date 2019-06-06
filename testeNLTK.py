import nltk
import csv
from nltk.corpus import stopwords
import re
from shlex import split
from testeSentimento import analiseSentimento



# Pega gírias do arquivo .csv
####### Ainda falta opção para inserir novas gírias #######
def pegaGirias():
    with open('arquivos/girias.csv', 'r', encoding="utf-8") as csvGirias:
        csv_lendo = list(csv.reader(csvGirias))
    csvGirias.close()
    return csv_lendo

def pegaDic():
    with open('arquivos/dicionario.csv', 'r', encoding="utf-8", errors="ignore") as csvDic:
        csv_lendo_dic = list(csv.reader(csvDic))
    csvDic.close()
    return csv_lendo_dic


def checandoNoDicio(tempoWord):
    dicio = pegaDic()
    dicioTamanho = len(dicio)
    tanodicio = 0
    for a in range(dicioTamanho):
        if tempoWord in dicio[a]:            
            tanodicio = 1
    return tanodicio

# Parte principal
def tokenFrase(message):
    # Analise de sentimento
    messageSenti = message
    sentimento = analiseSentimento(messageSenti)
    # Gera os tokens da frase enviada
    message = message.lower()
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
    girias = pegaGirias()
    giriasTamanho = len(girias)

    dicio = pegaDic()
    dicioTamanho = len(dicio)

    tempo = ""
    fraseTemp = ""
    existeGirias = 0
    giriaRepetida = 0
    for i in range(fraseTamanho):
        print(existeGirias)
        print(words[i])
        for j in range(giriasTamanho):
            if(words[i] in girias[j][0]):
                #print("0000000000000000000000")
                #print("giria -------------- " + girias[j][0])                     
                if(girias[j][0] == words[i]):
                 #   print(words[i] in girias[j][0])
                    existeGirias = 1
                    tempoWord = words[i]
                    variavel = checandoNoDicio(tempoWord)
                    if (variavel == 1):
                        fraseTemp = "\n\nA palavra *"+ words[i] +"* pode ser uma gíria! \nSeu significado é: \n*"+ (girias[j][1]) + "*\n"
                        tempo = tempo + fraseTemp
                    elif (variavel == 0):
                        giriaRepetida = 1
                        message = (message.replace(girias[j][0], girias[j][2]))

    if(existeGirias == 1):
        if(giriaRepetida == 0):
            messageRetorno = message + tempo
        elif(giriaRepetida == 1):
            messageRetorno = "\nA frase contém girias e elas foram trocadas:\n" + message + tempo
    elif(existeGirias == 0):
        messageRetorno = message

    messageRetorno = messageRetorno + "\n Esta frase tem um sentimento " + sentimento
    return messageRetorno, existeGirias


message = "menor"

#string = tokenFrase(message)

#print(string)