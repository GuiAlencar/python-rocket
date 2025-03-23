# lista = [1, 2, 3, 4, 5]
# print("For usando lista")
# for elemento in lista:
#   print(elemento)

# print("For usando tupla")
# tupla = (6, 7, 8, 9, 10)
# for i in tupla:
#   print(i)


# pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# print("For utilizando dicionário - chaves")
# for chave in pessoa.keys():
#   print(chave)

# print()

# print("For utilizando dicionário - valor")
# for valor in pessoa.values():
#   print(valor)

# print()

# print("For utilizando dicionário - itens")
# for chave, valor in pessoa.items():
#   print(f"{chave}:{valor}")

# # range(): intervalo numérico
# print("Utilizando a função range()")
# for i in range(5):
#   print("Número: ", i)

# print("utilizando a função range() com len()")
# lista = [1, 2, 3, 4, 5]
# for indice in range(0, len(lista)):
#   print(f"indice {indice} , elemento {lista[indice]}")
#   if indice == 3:
#     lista[indice] = 'guilherme'
#   else:
#     lista[indice] = 0

# print(lista)

# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
  print(f"{indice}:{valor}")
  if indice == 1:
    lista_enumerate[indice] = "teste"
  elif valor == "c":
    lista_enumerate[indice] = "guilherme"
  elif valor == "a":
    lista_enumerate[indice] = "alencar"
  print(lista_enumerate)
    
    

