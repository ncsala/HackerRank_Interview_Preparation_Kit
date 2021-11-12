
"""
 The player can jump on any cumulus cloud having a number that is equal to the number of the current 
 cloud plus  1 or 2 . The player must avoid the thunderheads. Determine the minimum number of jumps it 
 will take to jump from the starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided."""

#
# 'jumpingOnClouds'#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code
    contadorJumps = 0
    index = 0
    
    #Ejecutar una estrategia de salto
    while index < len(c) - 2:
        contadorJumps += 1
        if c[index + 2] == 0:
            index += 2
        else:
            index += 1
    
    # salta uno mas si no has llegado
    if index == len(c) - 2:
        contadorJumps += 1
    
    return (contadorJumps)
