n = input().split()

n[0] = int(n[0]) #number of students
n[1] = int(n[1]) #number of dinners

results = []

while(sum(n)!= 0):

    students = {}
    allPresences = False

    for i in range(n[0]):
        students[i] = 0 #initializing the dictionary

    for j in range(n[1]): #analyzing the dinners
        dinner = input().split()

        for k in range(len(dinner)): #len(dinner) == n[0]
            students[k] += int(dinner[k])

    for element in students.keys():
        if(students[element] == n[1]):

            allPresences = True

            break

    if(allPresences == True):
        results.append('yes')

    else:
        results.append('no')   

    n = input().split()
    
    n[0] = int(n[0])
    n[1] = int(n[1])

for result in results:
    print(result)
