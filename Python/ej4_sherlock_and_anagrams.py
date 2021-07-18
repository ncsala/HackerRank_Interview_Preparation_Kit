
""" Two strings are anagrams of each other if the letters of one string can be rearranged to form the 
other string. Given a string, find the number of pairs of substrings of the string that are 
anagrams of each other."""

import os

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code
    # contar las ocurrencias de cada unica substring conectada
    diccionario = {}
    for r in range(len(s)):
        for j in range(r, len(s)):
            substr = ''.join(sorted(s[r:j+1]))
            diccionario.setdefault(substr, 0)
            diccionario[substr] += 1
            
    # usar el diccionario para contar las diferentes ocurrencias de los anagramas
    contador = 0
    for string in diccionario:
        # esta es una forma: con formula de numeros triangulares 
        # count += int((diccionario[string] - 1) * diccionario[string] / 2))
        # la segunda opcion es esta
        contador += sum( [r for r in range(diccionario[string])] )
        
    return (contador)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
                    
