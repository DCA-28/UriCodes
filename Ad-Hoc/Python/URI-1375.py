def setPosition(carNumber, initialPosition, positions):

    if(initialPosition >= 1 and initialPosition <= n):

        if(positions[initialPosition] == 'E'):

            positions[initialPosition] = carNumber

        else:

            return -1

    else:

        return - 1

n = int(input())

while(n != 0):

    positions = {position : 'E' for position in range(1,n+1)}
    buildableGrid = True

    for i in range(1,n+1):

        carDate = input().split()

        if(buildableGrid):
            
            carNumber = int(carDate[0])
            carMoves = int(carDate[1])
            initialPosition = i + carMoves

            finalPosition = setPosition(carNumber, initialPosition, positions)

            if(finalPosition == -1):
                print(finalPosition)
                buildableGrid = False

        else:
            continue

    if(finalPosition != -1):

        for key in range(1,len(positions)):

            print(positions[key],end = ' ')

        print(positions[n])

    n = int(input())
