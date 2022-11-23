# 1º DSM 2/2022
# JEAN LUCAS DE FARIA SILVA
# GABRIELA DA SILVA BARBOSA

# IMPORTANDO AS BIBLIOTECAS PYTHON
import random
import requests

# DEFINIR VARIAVEIS
letrasCertas = letrasErradas = ""

# DEFINIR A LISTA DE PALAVRAS QUE O SITE POSSUI
listaPalavras = requests.get('https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt').text.lower().split()

def escolhe():
    palavraEscolhida = random.choice(listaPalavras)
    return palavraEscolhida

palavraEscolhida = escolhe()

def chute(x):
    #DEFINIÇÕES NA VARIÁVEL CHUTE
    global letrasCertas
    global letrasErradas
    alfabeto = list(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    x = x
    Valido = False

    #UM LAÇO DE REPETIÇÃO PARA VERIFICAR SE A LETRA É VÁLIDA
    while Valido = False:
        while (x not in alfabeto):
            x = input('Você não digitou uma letra, ou já digitou esta letra antes, tente novamente!')
        while (x in letrasCertas) or (x in letrasErradas):
            x = input('Você já digitou essa letra antes.')
        Valido = True:

    #SE FOR VÁLIDA, IRÁ IDENTIFICAR SE É UMA LETRA QUE ESTÁ NA PALAVRA ESCOLHIDA OU NÃO
    if x in palavraEscolhida:
        letrasCertas += x
    else:
        letrasErradas += x

    #DEFINE VALIDO COMO FALSO PARA QUE A PRÓXIMA VEZ QUE A VARIÁVEL FOR CHAMADA REALIZAR A VERIFICAÇÃO NOVAMENTE
    Valido = False

    return 'Letra escolhida com sucesso!'

def desenha():
    desenho = ["""
       +-------+
       |       |
       |       |
       ~       |
       O       |
      /|\      |
      / \      |
               |
================
"""]
