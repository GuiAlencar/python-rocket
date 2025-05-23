class Animal:
  def __init__(self, nome):
    self.nome = nome

  def emitir_som(self):
    pass

class Mamifero(Animal):
  def amamentar(self):
    return f"{self.nome} está mamando"
  
class Ave(Animal):
  def voar(self):
    return f"{self.nome} está voando"
    
class Morcego(Mamifero, Ave):
  def emitir_som(self):
    return "Morcego está emitindo som"

morcego = Morcego(nome="Batman")

# Acessando métodos da clesse base 'Animal'
print(f"Nome do morcego: {morcego.nome}")
print(f"Som do morcego: {morcego.emitir_som()}")

# Acessando métodos da classe base 'Mamifero' e 'Ave'
print(f"Morcego amamentando: {morcego.amamentar()}")
print(f"Morcego voando: {morcego.voar()}")

