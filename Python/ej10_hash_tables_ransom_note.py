"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.  
"""

"""
Harold es un secuestrador que escribió una nota de rescate, pero ahora le preocupa que se pueda rastrear hasta él a través de su letra. Encontró una revista y quiere saber si puede recortar palabras completas y usarlas para crear una réplica imposible de rastrear de su nota de rescate. Las palabras en su nota distinguen entre mayúsculas y minúsculas y debe usar solo palabras completas disponibles en la revista. No puede usar subcadenas o concatenaciones para crear las palabras que necesita.

Dadas las palabras en la revista y las palabras en la nota de rescate, escriba Sí si puede replicar su nota de rescate exactamente usando palabras completas de la revista; de lo contrario, imprima No.
"""

def ransom_note(magazine, ransom):
    #Solution here
    magazine_dict = {}
    ransom_dict = {}
    for word in magazine:
        if word not in magazine_dict:
            magazine_dict[word] = 1
        else:
            magazine_dict[word] += 1
    for word in ransom:
        if word not in ransom_dict:
            ransom_dict[word] = 1
        else:
            ransom_dict[word] += 1
    for word in ransom_dict:
        if word not in magazine_dict or ransom_dict[word] > magazine_dict[word]:
            return False
    return True


