#create in crescent order 1# -> make that a set
#sort the returned divers 2# -> make a that a set
#del the 2# from the 1# -> print the result with " "

def intTransform(values):

    vector = values

    for i in range(len(vector)):

        vector[i] = int(vector[i])

numbers = input()

while(numbers != ''):

    try:

        numbers = numbers.split(' ')
        divers = []

        for i in range(int(numbers[0])):

            divers.append(i+1)

        a = set(divers)
        survivors = input().split(' ')
        intTransform(survivors)
        survivors.sort()
        b = set(survivors)

        if(len(a) == len(b)):

            print('*')

        else:

            c = a.difference(b)
            c = list(c)
            c.sort()

            for element in c:
                print(element, end = ' ')

            print()

        numbers = input()

    except EOFError:

        break
