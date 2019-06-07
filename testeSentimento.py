import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import nltk
from nltk.metrics import ConfusionMatrix 


basetreinamento = [
('este trabalho e agradável', 'positivo'),
('gosto de ficar no seu aconchego','positivo'),
('fiz a adesão ao curso hoje porque eu gostei','positivo'),
('eu sou admirada por muitos','positivo'),
('eu gosto disso', 'positivo'), 
('este trabalho e agradável','positivo'), 
('este trabalho e agradável','positivo'),
('gosto de ficar no seu aconchego','positivo'),
('cara você é muito top','positivo'),
('isso aqui tá mec','positivo'),
('ela tá na minha, tá ligado','positivo'),
('fiz adesão ao curso hoje porque gostei','positivo'),
('eu sou admirada por muitos','positivo'),
('quero agradar meus filhos','positivo'),
('sinto muito afeição por ele','positivo'),
('somos tãp amáveis um com o outro','positivo'),
('adoro a cor dos seus olhos','positivo'),
('adoro como você é','positivo'),
('eu sou muito linda','positivo'),
('sou muito afortunado','positivo'), 
('e benefico para todos esta nova medida','positivo'), 
('ficou lindo','positivo'), 
('achei esse sapato muito simpático','positivo'), 
('estou ansiosa pela sua chegada','positivo'), 
('congratulações pelo seu aniversário','positivo'), 
('delicadamente ele a colocou para dormir','positivo'), 
('a musica e linda','positivo'), 
('sem musica eu não vivo','positivo'), 
('conclui uma tarefa muito difícil','positivo'),
('isso tudo e um erro','negativo'), 
('não gosto da maneira que você fala', 'negativo'),
('eu sou errada eu sou errante','negativo'), 
('olha que feia esta roupa','negativo'),
('da próxima vez, vou inventar tudo sozinho','negativo'),
('estar depressivo e muito ruim','negativo'),
('este lugar continua assustador','negativo'),
('se sair tão tarde, poderei ser assaltada','negativo'),
('perdi todo meu dinheiro','negativo'),
('odioso e deseumano','negativo'),
('estou muito bolado com você','negativo'),
('ele só pode estar de caô','negativo'),
('que ranço de certas pessoas','negativo'),
('estou com o diabo no corpo','negativo'),
('esse trouxa me deixou esperando','negativo'),
('eu não posso perder ela, eu amo demais para ficar sozinho','negativo'),
('que incomodo essa dor','negativo'),
('queria que fosse o ultimo dia da minha vida','negativo'),
('tenho muito dó do cachorro','negativo'), 
('e dolorida a perda de um filho','negativo'), 
('essa tragedia vai nos abalar para sempre','negativo'), 
('perdi meus filhos','negativo'), 
('isso vai me aborrecer','negativo'), 
('estou com muita aflição','negativo'), 
('me aflige o modo como fala','negativo'), 
('estou em agonia com meu intimo','negativo'),
('hoje eu bati de carro, estou pistola','negativo'),
('nao acredito que eu fiz isso estou muito brabo','negativo')
]

baseteste = [
('gosto de ficar no seu aconchego','positivo'), 
('fiz a adesão ao curso hoje','positivo'), 
('eu sou admirada por muitos','positivo'), 
('adoro como você e','positivo'), 
('adoro seu cabelo macio','positivo'), 
('adoro a cor dos seus olhos','positivo'), 
('somo tão amáveis um com o outro','positivo'), 
('sinto uma grande afeição por ele','positivo'), 
('quero agradar meus filhos','positivo'), 
('me sinto completamente amado','positivo'), 
('eu amo você','positivo'),
('não precisei pagar o ingresso','positivo'), 
('se eu ajeitar tudo fica bem','positivo'), 
('minha fortuna ultrapassa a sua','positivo'), 
('perdi meu curso','negativo'), 
('sou só uma chorona','negativo'), 
('você e um chorão','negativo'), 
('se arrependimento matasse','negativo'), 
('caraca ela ficou muito pistola hoje','negativo'),
('me sinto deslocado em sala de aula','negativo'), 
('foi uma passagem fúnebre','negativo'), 
('aquilo é muito desnecessário','negativo'),
('eu nao acredito que ele amarelou','negativo'),
('perdi tod mue dinheiro hoje estou pistola','negativo'),
('estava tudo bem ate voce chegar ranço','negativo'),
('eu odeio essa matéria','negativo'),
('hoje o transito estava o diabo','negativo'),
('que tragedia o que aconteceu hoje','negativo')
]
stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
frasescomstemmingtreinamento = ''
frasescomstemmingteste = ''
palavrastreinamento = ''
palavrasteste = ''
frequenciatreinamento = ''
frequenciateste = ''
caracteristicasfrase = ''
basecompletatreinamento = ''
basecompletateste = ''
classificador = ''

def aplicastemmer(texto): 
    stemmer = nltk.stem.RSLPStemmer() 
    frasessstemming = [] 
    for (palavras, emocao) in texto: 
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk] 
        frasessstemming.append((comstemming, emocao)) 

    return frasessstemming

def buscapalavras(frases): 
    todaspalavras = [] 
    for (palavras, emocao) in frases: 
        todaspalavras.extend(palavras) 
    return todaspalavras

def buscafrequencia(palavras): 
    palavras = nltk.FreqDist(palavras) 
    return palavras

def extratorpalavras(documento): 
    doc = set(documento) 
    caracteristicas = {} 
    for palavras in palavrastreinamento: 
        caracteristicas['%s' % palavras] = (palavras in doc) 
    return caracteristicas

def analiseSentimento(messageSenti):

    frasescomstemmingtreinamento = aplicastemmer(basetreinamento) 
    frasescomstemmingteste = aplicastemmer(baseteste)

    palavrastreinamento = buscapalavras(frasescomstemmingtreinamento)
    palavrasteste = buscapalavras(frasescomstemmingteste)

    frequenciatreinamento = buscafrequencia(palavrastreinamento) 
    frequenciateste = buscafrequencia(palavrasteste)
    print(frequenciatreinamento)
    print(frequenciateste)

    #caracteristicasfrase = extratorpalavras(['am', 'nov', 'dia'])

    basecompletatreinamento = nltk.classify.apply_features(extratorpalavras, frasescomstemmingtreinamento) 
    basecompletateste = nltk.classify.apply_features(extratorpalavras, frasescomstemmingteste)

    classificador = nltk.NaiveBayesClassifier.train(basecompletatreinamento) 
    print(classificador.labels())
    print(nltk.classify.accuracy(classificador, basecompletateste))

    erros = [] 
    for (frase, classe) in basecompletateste: 
        resultado = classificador.classify(frase) 
        if resultado != classe: 
            erros.append((classe, resultado, frase))

    
    esperado = [] 
    previsto = [] 
    for (frase, classe) in basecompletateste: 
        resultado = classificador.classify(frase) 
        previsto.append(resultado) 
        esperado.append(classe)

    matriz = ConfusionMatrix(esperado, previsto) 
    print(matriz)


    testestemming = [] 
    stemmer = nltk.stem.RSLPStemmer() 
    for (palavrastreinamento) in messageSenti.split(): 
        comstem = [p for p in palavrastreinamento.split()] 
        testestemming.append(str(stemmer.stem(comstem[0])))

    novo = extratorpalavras(testestemming) 
    distribuicao = classificador.prob_classify(novo)
    resultado = classificador.classify(novo)
    return resultado

teste = 'você é muito chato ruim não perdi chorona fala' 
resul = analiseSentimento(teste)
print('RESULTADO:') 
print(resul)