import nltk
import csv
#import pandas as pd
#precisa baixar os pacotes antes de rodar
#nltk.download()


frase = "Fala ai cria, tudo na tranquilidade? O menor da rua de baixo tá chamando a gente pro role, pega logo a peita que tá aqui em casa!!!"

#Gera os tokens da frase
token_frase = nltk.word_tokenize(frase)

#coloca tudo em minusculo
frase_low = [token_frase.lower() for token_frase in token_frase]
#print(frase_low)
array_length = len(frase_low)

"precisa retirar a pontuação para diminuir as interações"
    
#for i in range(array_length):
#    print (token_frase[i])
    
#outra forma de separarar   
#for index, word in enumerate(nltk.word_tokenize(texto)):
#print(index,word)
    
#abre o arquivo csv e coleta as girias 
with open('arquivos/girias.csv', 'r', encoding="utf-8") as csvGirias:
    csv_lendo = list(csv.reader(csvGirias))
csvGirias.close()


csv_length = len(csv_lendo)

for a in range(csv_length):
    print(csv_lendo[a][0])
print("------")         
print(frase)
for i in range(array_length):
    for j in range(csv_length):
        if(csv_lendo[j][0] in frase_low[i]):
            print("------")   
            print("Nesta frase é possível que a palavra "+ csv_lendo[j][0] + " seja uma gíria!")
            print("Seu significado é: ")
            print(csv_lendo[j][1])


    


