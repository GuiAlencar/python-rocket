# if, elif e else

# exemplo de if
idade = int(input("Informe sua idade ? \n"))

if idade >= 18:
  print("você é maior de idade")
elif idade == 15:
  print("Você é jovem")
else:
  print("Você é menor de idade")

mensagem = "Pode tirar a carteira de motorista" if idade >= 18 else "você não pode tirar carteira de motorista"
print(mensagem)
# if idade == 19:
#   print("Você tem 19 anos")

# if idade < 18:
#   print("Você é menor de idade")

# if idade != 10:
#   print("Você não tem 10 anos")
