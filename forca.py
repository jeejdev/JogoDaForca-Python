# 1º DSM 2/2022
# JEAN LUCAS DE FARIA SILVA
# GABRIELA DA SILVA BARBOSA

import random
import requests

letrasCertas = letrasErradas = ""

listaPalavras = requests.get('https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt').text.lower().split()
palavraEscolhida = random.choice(listaPalavras)

def chute(a):
    alfabeto = list(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    a = input('Insira uma letra!')
    while a not in alfabeto:
        a = input('Você não digitou uma letra, tente novamente!')

print(palavraEscolhida)