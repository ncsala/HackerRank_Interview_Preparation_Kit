"""
Given the sequence of up and down steps during a hike, .
find and print the number of valleys walked through.
"""

#
# countingValleys has the following parameter(s):
# int steps: the number of steps on the hike
# string path: a string describing the path
#

def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    previousLevel = 0
    currentLevel = 0
    
    for r in range(steps):
        #actualizar nivel previo y nivel actual
        previousLevel = currentLevel
        if path[r] == 'U':
            currentLevel += 1
        else:
            currentLevel -= 1
        #Determinar si un nuevo valle es completado
        if currentLevel == 0 and previousLevel == -1:
            valleys += 1
    
    return (valleys)
    

