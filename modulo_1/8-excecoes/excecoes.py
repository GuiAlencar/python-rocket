print("Exemplo de captura de exceções")
try:
    numero = input("Digite um número: ")
    resultado = 10 / int(numero)
except ValueError as e:
    print(f"Erro de value error: {e}")
    raise ValueError("Tipo de variáveis incompaveis")
except Exception as e:
    print(f"Erro: {e}")
else:
    print("O resultado é", resultado)
finally:
    print("Operação finalizada")