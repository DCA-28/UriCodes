#implementation of the matches logic

numbers = input().split()

countries = int(numbers[0])

matches = int(numbers[1])

while(countries != 0):

    totalPoints = 0
    numberWins = 0
    numberDraws = 0

    for i in range(countries):

        matchDate = input().split()
        totalPoints += int(matchDate[1])

    #Calculating the draws. With this logic, my initial number of draws is 0,
    #and if 'equation' transpass the totalPoints, the algorithm resignifies the
    #tuple witch represents the diofantin solution

    numberWins = matches

    equation = numberDraws*2 + numberWins*3

    if(equation == totalPoints):
        pass

    elif(equation > totalPoints):

        excedent = equation - totalPoints

        numberWins = matches - excedent

        numberDraws += excedent

    print(numberDraws)

    numbers = input().split()

    countries = int(numbers[0])

    matches = int(numbers[1])
