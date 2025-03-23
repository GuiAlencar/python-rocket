# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10 # Atributo de classe

    def __init__(self, nome) -> None:
        self.nome = nome # Atributo de instância

    # requer uma instância para ser chamado
    def metodo_instancia(self):
        print(f'Método de instância chamado para: {self.nome}')
    
    @classmethod
    def metodo_classe(cls):
        return f"Método de classe chamado para valor : {cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return 'Método estático chamado'

obj = MinhaClasse('Guilherme')
obj.metodo_instancia()
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

print("#" * 10)

class Carro():
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))
    
configuracao1 = "Ford,Fiesta,2008"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

class Matematica:
    @staticmethod
    def soma(x, y):
        return x + y

print(Matematica.soma(2, 3))
