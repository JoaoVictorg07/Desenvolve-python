import csv

# Função para carregar usuários de um arquivo CSV
def carregar_usuarios(arquivo):
    usuarios = []
    with open(arquivo, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuarios.append(row)
    return usuarios

# Função para salvar usuários em um arquivo CSV
def salvar_usuarios(usuarios, arquivo):
    with open(arquivo, mode='w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['nome', 'senha', 'tipo'])
        writer.writeheader()
        for usuario in usuarios:
            writer.writerow(usuario)

# Função para criar um novo usuário
def criar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
    tipo = input("Digite o tipo (admin, funcionario, cliente): ")
    usuarios.append({'nome': nome, 'senha': senha, 'tipo': tipo})
    print("Usuário criado com sucesso!")

# Função para ler e listar usuários
def ler_usuarios(usuarios):
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Tipo: {usuario['tipo']}")

# Função para atualizar um usuário
def atualizar_usuario(usuarios):
    nome = input("Digite o nome do usuário que deseja atualizar: ")
    for usuario in usuarios:
        if usuario['nome'] == nome:
            usuario['senha'] = input("Digite a nova senha: ")
            usuario['tipo'] = input("Digite o novo tipo: ")
            print("Usuário atualizado com sucesso!")
            return
    print("Usuário não encontrado.")

# Função para excluir um usuário
def excluir_usuario(usuarios):
    nome = input("Digite o nome do usuário que deseja excluir: ")
    for usuario in usuarios:
        if usuario['nome'] == nome:
            usuarios.remove(usuario)
            print("Usuário excluído com sucesso!")
            return
    print("Usuário não encontrado.")

# Função principal
def main():
    arquivo_usuarios = 'usuarios.csv'
    usuarios = carregar_usuarios(arquivo_usuarios)
    
    while True:
        print("\nMenu de Usuários:")
        print("1. Criar usuário")
        print("2. Ler usuários")
        print("3. Atualizar usuário")
        print("4. Excluir usuário")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            criar_usuario(usuarios)
            salvar_usuarios(usuarios, arquivo_usuarios)
        elif opcao == '2':
            ler_usuarios(usuarios)
        elif opcao == '3':
            atualizar_usuario(usuarios)
            salvar_usuarios(usuarios, arquivo_usuarios)
        elif opcao == '4':
            excluir_usuario(usuarios)
            salvar_usuarios(usuarios, arquivo_usuarios)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execute o programa
if __name__ == "__main__":
    main()
