def intTransform(values):
    vector = values
    for i in range(len(vector)):
        vector[i] = int(vector[i])

def localization(dp1, dp2, c1, c2):
    dp1 = dp1
    dp2 = dp2
    c1 = c1
    c2 = c2

    needLocate = True
    i = 0 #index of the region

    while(needLocate):
        if(dp1 == c1 or dp2 == c2):
            i = 4 #to return divisa
            needLocate = False

        elif( c1 < dp1 ): #going left
            if(c2 > dp2):
                i = 0 #going left and up
                needLocate = False
                
            else: #going left and down
                i = 3
                needLocate = False

        elif(c1 > dp1): #going right
            if(c2 > dp2):
                i = 1 #going right and up
                needLocate = False

            else:
                i = 2 #going right and down
                needLocate = False

    return i           

def region(i):
    region = ''
    if (i == 0):
        region = 'NO'

    elif (i == 1):
        region = 'NE'

    elif (i == 2):
        region = 'SE'

    elif (i == 3):
        region = 'SO'

    else:
        region = 'divisa'

    return region

#main program

searchs = int(input())
finalRegions = []
while(searchs != 0):
    qtd = 0 #quantity of cordenates
    divisionPoint = input().split()        
    intTransform(divisionPoint)
    while(qtd != searchs):
        cordinates = input().split()
        intTransform(cordinates)
        l = localization(divisionPoint[0],divisionPoint[1],cordinates[0],cordinates[1])
        finalRegions.append(region(l))
        qtd = qtd + 1

    searchs = int(input())

for region in finalRegions:
    print(region)
