sumOfDistances = []
name = input()

while(name != ''):

    try:

        distance = float(input())
        sumOfDistances.append(distance)
        name = input()

    except EOFError:
        break

size = float(len(sumOfDistances))
result = sum(sumOfDistances)/size
print('%.1f' % result)        
