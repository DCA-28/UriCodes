def deal(a,b): #a and b are sets

    changes = []
    changes.append(len(a.difference(b))) #the cards that 'a' can change
    changes.append(len(b.difference(a))) #the cards that 'b' can change

    return min(changes)

n = input().split()        
results = []

while(n[0] + n[1] != '00'):

    a = input().split()
    b = input().split()
    #setting the sets
    
    a = set(a)
    b = set(b)

    results.append(deal(a,b))
    n = input().split()

for element in results:
    print(element)

