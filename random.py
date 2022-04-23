# Randomizando-alunos.py
sorteio em random e sorteio em sequência.

import random
n1=str(input('primeiro nome:'))
n2=str(input('segundo nome:'))
n3=str(input('terceiro nome:'))
n4=str(input('quarto nome:'))
lista=[n1, n2, n3, n4]
escolhido=random.choice(lista)
print('o aluno escolhido foi {}!'.format(escolhido))

import random
n1=(input('primeiro nome:'))
n2=(input('segundo nome:'))
n3=(input('terceiro nome:'))
n4=(input('quarto nome:'))
lista=[n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
