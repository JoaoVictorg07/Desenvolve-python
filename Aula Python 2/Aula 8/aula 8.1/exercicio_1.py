def caracteres_unicos(s):
    # Usa um set para armazenar caracteres únicos, ignorando maiúsculas e minúsculas
    caracteres = set(s.lower())
    
    # Remove espaços e caracteres não alfabéticos
    caracteres = {c for c in caracteres if c.isalpha()}

    # Ordena os caracteres
    caracteres_ordenados = sorted(caracteres)

    return caracteres_ordenados

# Exemplo de uso
string = "Exemplo de String com Duplicatas!"
resultado = caracteres_unicos(string)
print(resultado)
