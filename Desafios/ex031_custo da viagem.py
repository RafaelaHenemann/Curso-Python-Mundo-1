# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas.

distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
