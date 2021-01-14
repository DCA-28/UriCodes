def grid(a,b): # a and b are lists
    l = a
    c = b
    qtd = 0

    for i in range(len(c)):
        if(c[i] != l[i]):
            for j in range(i,len(l)):
                if(l[j] == c[i]):                
                    while(j!=i):
                        l[j-1],l[j] = l[j],l[j-1]
                        qtd += 1
                        j -= 1

                    break

    return qtd

#main program

final_result = []
number = input()

while(number != ''):
    initial_grid = input().split()
    final_grid = input().split()
    final_result.append(grid(initial_grid,final_grid))

    try:
        number = input()

    except EOFError:
        break

    except RuntimeError:
        break

for element in final_result:
    print(element)
