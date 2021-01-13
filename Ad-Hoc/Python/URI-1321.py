def toInt(values):

    for i in range(len(values)):

        values[i] = int(values[i])


def verifyNumber(number, usedCards):

    while number in usedCards:

        number += 1

    if number > 52:

        number = -1

    return number


def calculateWin(sisterCards, kingCards, usedCards):

    if (
        sisterCards[2] > kingCards[0] and sisterCards[1] > kingCards[1]
    ):  # sister can win at least in one case

        return -1

    elif (kingCards[0] > sisterCards[2] and kingCards[0] > sisterCards[1]) and (
        kingCards[1] > sisterCards[2] and kingCards[1] > sisterCards[1]
    ):  # all kings cards are bigger than sister cards, king always win

        value = verifyNumber(1, usedCards)

        return value

    elif kingCards[1] < sisterCards[2] and kingCards[1] < sisterCards[1]:

        value = verifyNumber(sisterCards[2], usedCards)  # safe value needed

        return value

    else:  # toDo

        value = verifyNumber(sisterCards[1] + 1, usedCards)

        return value


def main():

    numbers = input().split()
    toInt(numbers)

    while sum(numbers) != 0:

        sisterCards = numbers[0:3]
        kingCards = numbers[3:5]

        value1 = sorted(sisterCards)
        value2 = list(reversed(sorted(kingCards)))

        r = calculateWin(value1, value2, numbers)

        print(r)

        numbers = input().split()
        toInt(numbers)


if __name__ == "__main__":

    main()
