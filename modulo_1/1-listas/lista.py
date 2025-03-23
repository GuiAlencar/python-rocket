# declaração

minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

print("Minha lista de exemplo ", minha_lista)

minha_lista[0] = "python"
print("Minha_lista[0] = ", minha_lista[0])
print(minha_lista[1:7])
print(minha_lista[:6])
print(minha_lista[2:])

# métodos de lista

# método append(): adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após append", minha_lista)

# método index
indice = minha_lista.index(6)
print(indice)

# método insert: insere um elemento num indice específico
minha_lista.insert(2, 10)
print(minha_lista)

# método pop
elemento_removido = minha_lista.pop(3)
print(minha_lista)

# método remove
minha_lista.remove(True)
print(minha_lista)

# método sort

minha_lista.sort()
print(minha_lista)