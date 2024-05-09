import random

naipes = ['ouro' , 'copas', 'espadas', 'paus'] 
numeros = ['Ás', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q','k']

cartas = []

#for para naipes
for i in range(4):
  #for para numeros 
  for u in range(13):
    cartas.append(str(numeros[u])+" de "+naipes[i])

quantidade = int(input("Digite a quantidade da cartas"))

random.shuffle(cartas)
for i in range(quantidade):
  print(cartas[i] )
    