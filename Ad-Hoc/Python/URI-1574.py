t = int(input())

n = input()

while(n != ''):

    n = int(n)

    moves = [0] * n #this may require to much memory

    position = 0

    for i in range(n):

        goTo = input()

        if (goTo == 'LEFT'):
            position -= 1
            moves[i] = -1

        elif (goTo == 'RIGHT'):
            position += 1
            moves[i] = 1

        else:
            elements = goTo.split(" ")
            index = int(elements[2])
            position = position + moves[index - 1]

            moves[i] = moves[index - 1]

    print(position)

    try:

        n = (input())

    except(EOFError):

        break
