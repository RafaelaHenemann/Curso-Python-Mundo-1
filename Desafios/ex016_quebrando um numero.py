# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira.

# Uma das formas de resolver:
'''from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))'''

# Outra opção de resolver:
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))