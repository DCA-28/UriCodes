def plus(a,b):
    if ((a + b) >= 24):
        return (a + b) - 24

    else:
        return a + b

def intTransform(values):
    for i in range(len(values)):
        values[i] = int(values[i])

def hoursCount(vectorValues):
    values = vectorValues
    totalMinutes = 0

    #começar analisando a exceção

    if(values[0] == values[2] and values[1] > values[3]):
        totalMinutes = 1440 - (values[1] - values[3])

    while(values[0] != values[2]): #enquanto as horas não forem iguas
        if(values[1] != 0):
            minutesRemain = 60 - values[1]
            totalMinutes = totalMinutes + minutesRemain
            values[0] = plus(values[0], 1)
            values[1] = 0

        if(values[1] == 0 and values[0] != values[2]):
            totalMinutes = totalMinutes + 60            
            values[0] = plus(values[0], 1) #até aqui esta certa a hora, falta o minuto

    #somar os minutos restantes, até aqui está correto

    if(values[1] != values[3] and (values[1] < values[3])):
        totalMinutes = totalMinutes + (values[3] - values[1])

    print(totalMinutes)

#main program

vector = []
values = input().split()
intTransform(values)

while(sum(values) != 0):
    vector.append(values)
    values = input().split()
    intTransform(values)

for i in range(len(vector)):
    hoursCount(vector[i])
