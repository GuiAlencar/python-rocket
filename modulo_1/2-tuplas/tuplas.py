# tuplas são imutáveis

minha_tupla = (1, 2, 2, 3, 5)

print(minha_tupla)
print("Minha tupla: ", minha_tupla[0])
print("Minha tupla: ", minha_tupla[2])
print("Minha tupla: ", minha_tupla[-1])

# método count

contagem = minha_tupla.count(2)
print("quantidade de vezes que o elemento 2 aparece", contagem)

indice = minha_tupla.index(5)

print("A posição do elemento 5 é: ", indice)