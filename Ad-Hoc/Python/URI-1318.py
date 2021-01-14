n = input().split()

results = []

while(n[0] + n[1] != '00'):

    students = {}
    falseTickets = 0
    tickets = input().split()

    for i in range(len(tickets)):

        if (tickets[i] not in students):
            students[tickets[i]] = 1

        else:

            students[tickets[i]] += 1

    for key in students.keys():

        if(students[key] != 1):
            falseTickets += 1

    results.append(falseTickets)
    n = input().split()

for element in results:
    print(element)
        
