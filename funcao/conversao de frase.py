def codificar_frase(frase):
    """
    Codifica uma frase substituindo cada letra por outra do alfabeto.
    
    Args:
        frase (str): A frase a ser codificada.
        
    Returns:
        str: A frase codificada.
    """
    # Define um dicionário de substituição
    substituicao = {
        'a': 'z',
        'b': 'y',
        'c': 'x',
        'd': 'w',
        'e': 'v',
        'f': 'u',
        'g': 't',
        'h': 's',
        'i': 'r',
        'j': 'q',
        'k': 'p',
        'l': 'o',
        'm': 'n',
        'n': 'm',
        'o': 'l',
        'p': 'k',
        'q': 'j',
        'r': 'i',
        's': 'h',
        't': 'g',
        'u': 'f',
        'v': 'e',
        'w': 'd',
        'x': 'c',
        'y': 'b',
        'z': 'a'
    }
    
    # Converte a frase para minúsculas
    frase = frase.lower()
    
    # Inicializa uma lista para armazenar os caracteres codificados
    codificado = []
    
    # Substitui cada letra na frase
    for letra in frase:
        if letra in substituicao:
            codificado.append(substituicao[letra])
        else:
            codificado.append(letra)
    
    # Retorna a frase codificada
    return ''.join(codificado)



frase = "Olá, isso é muito interessante!"
frase_codificada = codificar_frase(frase)
print(frase_codificada)

