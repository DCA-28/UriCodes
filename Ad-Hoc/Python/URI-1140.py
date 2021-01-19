def findTautogram(mySentence):
    myInput = mySentence
    firstLetter = []
    tautogram = 'Y'
    firstLetter.append(myInput[0])

    for i in range(1, len(myInput)):  #saving the first letter in an array
        if(myInput[i-1] == ' '):
            firstLetter.append(myInput[i])

    for i in range(1, len(firstLetter)):
        if( (abs(ord(firstLetter[0]) - ord(firstLetter[i]))) == 0 or (abs(ord(firstLetter[0]) - ord(firstLetter[i]))) == 32):
            continue                   #checking if it is a tautogram

        else:
            tautogram = 'N'
            
    print(tautogram)

#main program

vector = []
mySentence = input()
while(mySentence != '*'):
    vector.append(mySentence)    
    mySentence = input()

for i in range(len(vector)):
    findTautogram(vector[i])
