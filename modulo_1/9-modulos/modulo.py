print("Exemplo de importação de um módulo padrão: ")
# importa todo o módulo de  math
import math

# importa apenas a função sqrt do módulo math
from math import sqrt

raiz_quadrada = math.sqrt(25)
print(raiz_quadrada)

print("\nExemplo de criação e utilização de um módulo personalizado: ")

# import meu_modulo
from meu_modulo import saudacao, dobro

mensagem = saudacao("Guilherme")
resultado_dobro = dobro(5)

print(mensagem)
print(resultado_dobro)