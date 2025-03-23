def saudacao(nome):
    print(f"olá {nome}")

saudacao("Guilherme")

# função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

resultado_quadrado = quadrado(5)
print(resultado_quadrado)

# função com multiplos parametros

def soma(num1, num2):
    resultado = num1 + num2
    return resultado


num1 = 2
num2 = 2
resultado_soma = soma(num1, num2)
print("A soma do número %s e o número %s é %s " % (num1, num2, resultado_soma))