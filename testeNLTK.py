import nltk
import csv
from nltk.corpus import stopwords
#import pandas as pd
#precisa baixar os pacotes antes de rodar
#nltk.download()



frase = "Fala ai cria, tudo na tranquilidade? O menor da rua de baixo tá chamando a gente pro role, pega logo a peita que tá aqui em casa!!!"

def pegaGirias():
    with open('arquivos/girias.csv', 'r', encoding="utf-8") as csvGirias:
        csv_lendo = list(csv.reader(csvGirias))
    csvGirias.close()
    return csv_lendo

def tokenFrase(frase):
    #Gera os tokens da frase
    token_frase = nltk.word_tokenize(frase)
    #coloca tudo em minusculo
    palavras = [token_frase.lower() for token_frase in token_frase]
    #print(frase_low)
    
    #table = str.maketrans('', '', string.punctuation)
    #stripped = [w.translate(table) for w in palavras]
    words = [word for word in palavras if word.isalpha()]
    stop_words = set(stopwords.words('portuguese'))
    words = [w for w in words if not w in stop_words]
    return words


"precisa retirar a pontuação para diminuir as interações"


#for i in range(array_length):
#    print (token_frase[i])
    
#outra forma de separarar   
#for index, word in enumerate(nltk.word_tokenize(texto)):
#print(index,word)
    
#abre o arquivo csv e coleta as girias 

fraseRecebida = tokenFrase(frase)
fraseTamanho = len(fraseRecebida)

csvGirias = pegaGirias()
csv_length = len(csvGirias)

for a in range(csv_length):
    print(csvGirias[a][0])
print("------")         
print(frase)
for i in range(fraseTamanho):
    for j in range(csv_length):
        if(csvGirias[j][0] in fraseRecebida[i]):
            print("------")   
            print("Nesta frase é possível que a palavra "+ csvGirias[j][0] + " seja uma gíria!")
            print("Seu significado é: ")
            print(csvGirias[j][1])