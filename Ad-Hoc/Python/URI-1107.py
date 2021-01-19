# simplified laser
def intTransform(values):
    vector = values

    for i in range(len(vector)):
        vector[i] = int(vector[i])

def totalLaser(a,b,values):
    heigh = a
    lengh = b
    vector = values   
    laser = heigh - vector[0] #getting the first values to make the comparation

    for i in range(1, len(vector)):
        if (vector[i] < vector[i-1]):
            laser = laser + (vector[i-1] - vector[i]) #computing the difference

        else:
            continue

    return laser

#main program
finalLasers = []
heighLengh = input().split()
intTransform(heighLengh)

while(sum(heighLengh) != 0):
    values = input().split()
    intTransform(values)
    finalLasers.append(totalLaser(heighLengh[0],heighLengh[1],values))
    heighLengh = input().split()
    intTransform(heighLengh)

for laser in finalLasers:
    print(laser)
