tarefas = []

def adicionar_atendimento(tarefas, contador_id, descricao, nome_cliente, nome_barbeiro, horario_atendimento, urgencia):
    """
    Adiciona um atendimento à lista de tarefas.

    Parâmetros:
        tarefas (list): lista que armazena todos os atendimentos.
        contador_id (int): identificador único da tarefa.
        descricao (str): descrição do atendimento.
        nome_cliente (str): nome do cliente.
        nome_barbeiro (str): nome do barbeiro responsável.
        horario_atendimento (str): horário marcado para o atendimento.
        urgencia (str): nível de urgência (Alta, Normal ou Baixa).

    Retorno:
        tuple: lista de atendimentos atualizada e o próximo contador_id.
    """
    tarefa = {
        "id": contador_id,
        "descricao": descricao,
        "status": "Pendente",
        "nome_cliente": nome_cliente,
        "nome_barbeiro": nome_barbeiro,
        "horario_atendimento": horario_atendimento,
        "urgencia": urgencia
    }

    tarefas.append(tarefa)
    contador_id += 1
    return tarefas, contador_id

def listar_atendimentos(tarefas):
    """
    Lista todas os atendimentos cadastrados.

    Parâmetros:
        tarefas (list): lista de atendimentos.
    """
    if not tarefas:
        print("\nNão existe nenhum atendimento aqui... 😴\n")
        return

    print("\n---- LISTA DE TAREFAS ----\n")
    
    for tarefa in tarefas:
        print("ID:", tarefa["id"])
        print("| Descrição:", tarefa["descricao"]) 
        print("| Status:", tarefa["status"])
        print("| Nome do Cliente:", tarefa["nome_cliente"])
        print("| Nome do Barbeiro:", tarefa["nome_barbeiro"])
        print("| Horário de atendimento:", tarefa["horario_atendimento"])
        print("| Urgência:", tarefa["urgencia"])

    print("\n---------------------------\n")

def concluir_atendimento(tarefas, id_tarefa):
    """
    Marca um atendimento como concluído.

    Parâmetros:
        tarefas (list): lista de tarefas.
        id_tarefa (int): identificador da tarefa.
    """
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["status"] = "concluída"
            print("Atendimento concluído! 🎉\n")
            return
        
    print("Atendimento não encontrado. ❌\n")
    
def remover_atendimento(tarefas, id_tarefa):
    """
    Remove um atendimento da lista.

    Parâmetros:
        tarefas (list): lista de tarefas.
        id_tarefa (int): identificador da tarefa.
    """
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefas.remove(tarefa)
            print("Atendimento removido! 💥\n")
            return
        
    print("Atendimento não encontrado. ❌\n")
    
def menu():
    """
    Exibe o menu principal e controla a execução do sistema.
    """
    tarefas = []
    contador_id = 1
    
    while True:
        print("=== Sistema de Gestão de Tarefas da Barbearia ===")
        print("1 - Adicionar atendimento 📍")
        print("2 - Listar atendimentos 📃")
        print("3 - Concluir atendimento 🎯")
        print("4 - Remover atendimento 🧨")
        print("5 - Sair 👋")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            descricao = input("Digite a descrição do atendimento: ")
            nome_cliente = input("Digite o nome do Cliente: ")
            nome_barbeiro = input("Digite o nome do Barbeiro: ")
            horario_atendimento = input("Digite o horário de atendimento: ")
            urgencia = input("Digite a urgência (Alta/Normal/Baixa): ")
            if urgencia == "":
                urgencia = "Normal"
                
            tarefas, contador_id = adicionar_atendimento(
                tarefas, contador_id, descricao, nome_cliente, nome_barbeiro, horario_atendimento, urgencia
            )
            print("Atendimento adicionado! 💡\n")
            
        elif opcao == "2":
            listar_atendimentos(tarefas)
            
        elif opcao == "3":
            try:
                id_tarefa = int(input("Digite o ID do atendimento que será concluído: "))
                concluir_atendimento(tarefas, id_tarefa)
            except ValueError:
                print("ID inválido. ❌\n")
                
        elif opcao == "4":
            try:
                id_tarefa = int(input("Digite o ID do atendimento a remover: "))
                remover_atendimento(tarefas, id_tarefa)
            except ValueError:
                print("ID inválido. ❌\n")
                
        elif opcao == "5":
            print("Saindo... 🏃")
            break
        
        else:
            print("Opção inválida. ❌\n")
            
menu()