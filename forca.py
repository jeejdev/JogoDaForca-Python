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
    Valido = False

    #UM LAÇO DE REPETIÇÃO PARA VERIFICAR SE A LETRA É VÁLIDA
    while Valido == False:
        while (x not in alfabeto):
            x = input('Você não digitou uma letra, tente novamente: ')
        while (x in letrasCertas) or (x in letrasErradas):
            x = input('Você já digitou essa letra antes, tente novamente: ')
        Valido = True

    #SE FOR VÁLIDA, IRÁ IDENTIFICAR SE É UMA LETRA QUE ESTÁ NA PALAVRA ESCOLHIDA OU NÃO
    if x in palavraEscolhida:
        letrasCertas += x
        print(f'Parabéns, você acertou a letra {x} :)')
    else:
        letrasErradas += x
        print(f'Nessa palavra não havia a letra {x} :(')

    #DEFINE VALIDO COMO FALSO PARA QUE A PRÓXIMA VEZ QUE A VARIÁVEL FOR CHAMADA REALIZAR A VERIFICAÇÃO NOVAMENTE
    Valido = False

    return

#7 TENTATIVAS 

def desenha():
    desenho = ["""
       +-------+
       |       |
       |       |
               |
               |
               |
               |
               |
================ ""","""
       +-------+
       |       |
       |       |
       ~       |
               |
               |
               |
               |
================ ""","""
       +-------+
       |       |
       |       |
       ~       |
       O       |
               |
               |
               |
================ ""","""
       +-------+
       |       |
       |       |
       ~       |
       O       |
       |       |
               |
               |
================ ""","""
       +-------+
       |       |
       |       |
       ~       |
       O       |
      /|       |
               |
               |
================ ""","""
       +-------+
       |       |
       |       |
       ~       |
       O       |
      /|\      |
               |
               |
================ ""","""
       +-------+
       |       |
       |       |
       ~       |
       O       |
      /|\      |
      /        |
               |
================ ""","""
       +-------+
       |       |
       |       |
       ~       |
       O       |
      /|\      |
      / \      |
               |
================ """
]

    #PRINTA DEPENDENDO DO NÚMERO DE ERROS
    print(desenho[len(letrasErradas)])

    #SE A LETRA ESTIVER PRESENTE NA STRING LETRASCERTAS IRÁ APARECER, CASO CONTRÁRIO SERÁ SUBSTITUIDA POR _ 
    for x in palavraEscolhida:
        if x in letrasCertas:
            print(f'{(x)}', end = ' ')
        else:
            print('_', end = ' ')

    #PULA LINHA
    print('\n')
    return

#FUNÇÃO PARA JOGAR NOVAMENTE
def jogarNovamente():
    global palavraEscolhida
    global letrasCertas
    global letrasErradas

    y = ''
    while y != 's' or y != 'n':
        y = input('Você quer jogar novamente? (S/N):').lower()
        if y == 's':
            palavraEscolhida = escolhe()
            letrasErradas = letrasCertas = ''
            return
        else:
            exit()

def ganhou():
    if set(letrasCertas) == set(palavraEscolhida):
        print('=*=*') * 10
        print('Parabéns, você acertou todas as letras!')
        print('=*=*') * 10
        jogarNovamente()

def perdeu():
    if len(letrasErradas) >= 7:
        print('Ei, você perdeu! :(')
        jogarNovamente()

while True:
    #ESQUEMA PARA CHUTAR UMA LETRA
    x = input('Insira uma letra: ').lower()
    chute(x)

    #FORCA E RESULTADO DESENHADO APÓS O CHUTE DA LETRA
    desenha()
    
    #VERIFICA SE JOGADOR JÁ GANHOU OU PERDEU (CASO NENHUM DOS DOIS OCORRA, ESSAS DUAS LINHAS SÃO PULADAS)
    ganhou()
    perdeu()

        
    