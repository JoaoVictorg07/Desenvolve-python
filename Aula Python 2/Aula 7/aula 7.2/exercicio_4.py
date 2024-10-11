import re

def validador_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    
    # Verifica se a senha contém pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        return False
    
    # Verifica se a senha contém pelo menos uma letra minúscula
    if not re.search(r'[a-z]', senha):
        return False
    
    # Verifica se a senha contém pelo menos um número
    if not re.search(r'[0-9]', senha):
        return False
    
    # Verifica se a senha contém pelo menos um caractere especial
    if not re.search(r'[@#$%^&+=!]', senha):
        return False

    # Se todos os critérios forem atendidos, a senha é válida
    return True
