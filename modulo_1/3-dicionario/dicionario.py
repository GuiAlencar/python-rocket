pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

print("Nome: ", pessoa["nome"])
print("Idade: ", pessoa["idade"])
print("Cidade: ", pessoa["cidade"])
pessoa["sobrenome"] = "Alencar"

print("sobrenome: ", pessoa["sobrenome"])

pessoa["idade"] = 31
print("Idade atualizada: ", pessoa["idade"])

# removendo um par de chave e valor 
del pessoa["sobrenome"]

print(pessoa)

# métodos: keys(), values(), items()

chaves = list(pessoa.keys())
print("Chaves do dicionários", chaves)
print("Primeira chave: ", chaves[0])

# método values
valores = list(pessoa.values())
print("Valores do dicionarios: ", valores)
print("Primeiro valor: ", valores[0])

# método items
itens = list(pessoa.items())
print("Pares chave-valor do dicionario: ", itens)
print("Primeiro item do dicionario: %s = %s " % (itens[0][0], itens[0][1]))


