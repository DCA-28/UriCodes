def toInteger(array):

    for i in range(len(array)):

        array[i] = int(array[i])

def getValues(array, processingPoints, tests, minimumStick):

    stickCounter = 0

    elementSum = 0

    for i in range(processingPoints):

        for j in range(tests):
            
            elementSum += array[j][i]

            if array[j][i] == 0:

                if elementSum >= minimumStick:

                    stickCounter += 1

                elementSum = 0
            
        if(elementSum >= minimumStick):
            
            stickCounter += 1

        elementSum = 0

    return stickCounter

while(True):

    values = input().split()

    toInteger(values)

    if(sum(values)) == 0:

        break
            
    vector = [None] * values[1]

    for i in range(values[1]):

        raw = input().split()

        toInteger(raw)

        vector[i] = raw

    sticks = getValues(vector, values[0], values[1], values[2])

    print(sticks)
