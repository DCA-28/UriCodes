def intTransform(values):
    for i in range(len(values)):
        values[i] = int(values[i])

def scanning(paper): #paper == array[i]
    black = 0
    white = 0
    alternative = ''

    for i in range(len(paper)):
        if(paper[i] <= 127):
            black = black + 1
            alternative = i

        else:
            white = white + 1

    if(black > 1 or white == 5):
        return '*'

    else:
        if(alternative == 0):
            alternative = 'A'
        elif(alternative == 1):
            alternative = 'B'
        elif(alternative == 2):
            alternative = 'C'
        elif(alternative == 3):
            alternative = 'D'
        else:
            alternative = 'E'

        return alternative
        
n = int(input()) #number of tests
answers = []

while(n != 0):
    array = [] #tests enter here
    for i in range(n):
        vector = [0,0,0,0,0] #represents a test
        array.append(vector)

    for i in range(len(array)):
        values = input().split()
        intTransform(values)
        array[i] = values
        answers.append(scanning(array[i]))

    n = int(input())

for i in range(len(answers)):    
    print(answers[i])
