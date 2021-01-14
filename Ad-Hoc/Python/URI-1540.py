import decimal
 
decimal.getcontext().rounding = decimal.ROUND_DOWN
 
def toInteger(array):
 
    for i in range(len(array)):
 
        array[i] = int(array[i])
 
while (True):
 
    try:
 
        n = input()
 
        if n == '':
 
            raise EOFError
 
        n = int(n)
 
        data = [None] * 4
 
        for i in range(n):
 
            data = input().split()
 
            toInteger(data)
 
            average = decimal.Decimal(data[3] - data[1])/(data[2] - data[0])
 
            average = (float(round(average,2)))
 
            average = ("%.2f") % average
 
            print(str(average).replace('.',',')) #this print rounds? yes, by the default settings
 
    except EOFError:
 
        break
