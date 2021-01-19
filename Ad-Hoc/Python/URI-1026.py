#main program

finalResult = []
numbers = input()

while (numbers != ''):
    n1, n2 = numbers.split(" ")        
    finalResult.append((int(n1)^int(n2))) #exclusive or bit-bit

    try:        
        numbers = input()
        
    except (EOFError):        
        break

    except (RuntimeError):
        break

for i in range(len(finalResult)):
    print(finalResult[i])
