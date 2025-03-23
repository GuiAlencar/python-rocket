def adicionar_tarefa(tarefas, nome_tarefa): 
  tarefa = {"tarefa": nome_tarefa, "completada": False}
  tarefas.append(tarefa)
  print(f"\033[1;32mTarefa {nome_tarefa} foi adicionada com sucesso!\033[m")
  return

def ver_tarefas(tarefas):
  print("\nLista de tarefas:")
  for indice, tarefa in enumerate(tarefas, start=1):
    #status = "✓" if tarefa["completada"] else " "
    if tarefa["completada"]:
      status = "✓"
    else:
      status = " "

    nome_tarefa = tarefa["tarefa"]
    print(f"\033[1;34m{indice}->[{status}] {nome_tarefa}\033[m")
  return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
  indice_tarefa_ajustado = indice_tarefa - 1
  if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
    tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
    print(f"\033[1;32mTarefa {indice_tarefa} atualizada para {novo_nome_tarefa}\033[m")
  else:
    print("\033[1;31m Indice de tarefa inválido! \033[m")
  return

def completar_tarefa(tarefas, indice_tarefa):
  indice_tarefa_ajustado = indice_tarefa - 1
  if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
    if tarefas[indice_tarefa_ajustado]["completada"]:
      print(f"\033[1;31mTarefa do índice {indice_tarefa_ajustado + 1} já foi completada!\033[m")
    else:
      tarefas[indice_tarefa_ajustado]["completada"] = True
      print(f"\033[1;32mTarefa {indice_tarefa} marcada como completada!\033[m")
  else:
    print("\033[1;31mIndice de tarefa inválido!\033[m")
  return

def deletar_todas_tarefas_completadas(tarefas):
  for tarefa in tarefas:
    if tarefa["completada"] == True:
      tarefas.remove(tarefa)   
      print("\033[1;32mTarefas completadas foram deletadas com sucesso!\033[m")            
  return

def deletar_tarefa_completada(tarefas, indice_tarefa):   
  indice_tarefa_ajustado = indice_tarefa - 1 
  if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
      if tarefas[indice_tarefa_ajustado]["completada"] == True:
        tarefas.pop(indice_tarefa_ajustado)
        print("\033[1;32mTarefa completada deletada com sucesso!\033[m")
      else:
        print("\033[1;31mTarefa não pode ser removida, pois não foi completada!\033[m")
  else:
    print("\033[1;31mIndice de tarefa inválido!\033[m")
  return     

tarefas = []
while True:
  print("\nMenu do gerenciador de lista de tarefas: ")
  print("1. Adicionar tarefa")
  print("2. ver tarefas")
  print("3. atualizar tarefa")
  print("4. completar tarefa")
  print("5. deletar todas as tarefas completadas")
  print("6. deletar tarefa completada por indice")
  print("7. Sair")
  
  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_tarefa = input("Informe o nome da tarefa que deseja adicionar: \n")
    adicionar_tarefa(tarefas, nome_tarefa)

  elif escolha == "2":
    ver_tarefas(tarefas)

  elif escolha == "3":
    ver_tarefas(tarefas)
    indice_tarefa = int(input("Informe o número da tarefa que deseja atualizar: "))
    novo_nome = input("Informe o novo nome da tarefa: ")
    print()
    atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)

  elif escolha == "4":
    ver_tarefas(tarefas)
    indice_tarefa = int(input("Informe o número da tarefa que deseja completar: "))
    completar_tarefa(tarefas, indice_tarefa)
  
  elif escolha == "5":
    deletar_todas_tarefas_completadas(tarefas)
    ver_tarefas(tarefas)
  
  elif escolha == "6":
    ver_tarefas(tarefas)
    indice_tarefa = int(input("Informe o número da tarefa completada que deseja deletar: "))
    deletar_tarefa_completada(tarefas, indice_tarefa)
    ver_tarefas(tarefas)

  elif escolha == "7":
    break

print("Programa finalizado")