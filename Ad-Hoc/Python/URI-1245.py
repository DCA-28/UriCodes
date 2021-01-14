def numberOfPairs(value):
    pairs = 0
    qtD = 0
    qtE = 0

    for i in range(len(value)):
        if(value[i] == 'D'):
            qtD += 1

        else:
            qtE += 1

    while(qtD != 0 and qtE != 0):
        qtD -= 1
        qtE -= 1
        pairs += 1

    return pairs

n = (input())
finalResults = []

while(n != ''):
    n = int(n)
    totalBoots = {}
    results = []

    foot = [''] * 31 #could i decrease this list size? Think i can change n for 31
                      #once 31 is the max number of indexes (foot sizes)
    index = 0
    
    for i in range(n):
        boots = input().split()

        if(boots[0] not in totalBoots):
            totalBoots[boots[0]] = index #creatinga a new key with its value
            foot[totalBoots[boots[0]]] += boots[1] #had born with the correct index
            index += 1
        
        else: #the key already exists           
            foot[totalBoots[boots[0]]] += boots[1]

    #computing the number of pairs

    for element in totalBoots.keys():
        value = (foot[int(totalBoots[element])])
        results.append(numberOfPairs(value))

    finalResults.append(sum(results))

    try:
        n = input()

    except EOFError:
        break

    except RuntimeError:
        break

for element in finalResults:
    print(element)
