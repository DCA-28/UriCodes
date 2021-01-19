def findSuspect(values): #values is a vector of integer numbers
    vectorOriginal = values
    vectorDictionary = []

    for i in range(len(vectorOriginal)):
        element = [ vectorOriginal[i],i ]        
        vectorDictionary.append(element)

    vectorDictionary = dict(vectorDictionary) #to find the index in O(1)
    vectorOriginal.sort()
    suspect = vectorOriginal[-2]
    return (vectorDictionary[suspect] + 1)

#main program

finalResult = []
numberOfSuspects = int(input())

while(numberOfSuspects != 0):
    values = []
    crimeScale = input().split()

    for i in range(len(crimeScale)):
        values.append(int(crimeScale[i]))

    finalResult.append(findSuspect(values))
    numberOfSuspects = int(input())

for suspect in finalResult:
    print(suspect)
