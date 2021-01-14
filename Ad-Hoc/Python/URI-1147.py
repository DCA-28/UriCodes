def pawnPositions(initialPosition):

    finalPosition = set([])

    for i in range(len(initialPosition)):

        p = ord(initialPosition[i][0]) - 1
        l = ord(initialPosition[i][1])

        if p == 48:
            continue  # pawn in raw 1

        if l == 97:  # pawn in column a

            finalPosition.add(chr(p) + chr(l + 1))

        elif l == 104:  # pawn in column h

            finalPosition.add(chr(p) + chr(l - 1))

        else:

            finalPosition.add(chr(p) + chr(l + 1))
            finalPosition.add(chr(p) + chr(l - 1))

    return finalPosition


def horsePositions(initialPosition):

    finalPositions = set([])

    operands = [
        [1, -2],
        [1, 2],
        [2, -1],
        [2, 1],
        [-1, -2],
        [-1, 2],
        [-2, -1],
        [-2, 1],
    ]  # possible horse moves

    p = ord(initialPosition[0])
    l = ord(initialPosition[1])

    for i in range(8):

        possiblePosition = chr(p + operands[i][0]) + chr(l + operands[i][1])

        if ord(possiblePosition[0]) > 56 or ord(possiblePosition[0]) < 49:

            continue

        if ord(possiblePosition[1]) > 104 or ord(possiblePosition[1]) < 97:

            continue

        finalPositions.add(possiblePosition)

    return finalPositions


def main():

    horseHouse = input()

    number = 0

    while horseHouse != "0":

        number += 1

        h = horsePositions(horseHouse)

        pawnHouse = [None] * 8

        for i in range(8):

            pawnHouse[i] = input()

        p = pawnPositions(pawnHouse)

        moviments = len(h.difference(p))

        print("Caso de Teste #{}: {} movimento(s).".format(number, moviments))

        horseHouse = input()

if __name__ == "__main__":

    main()
