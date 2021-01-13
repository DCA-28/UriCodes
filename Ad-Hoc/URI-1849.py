def main():
    sizes = [int(number) for number in input().split()]
    final_square = 0
    if sizes[0] > sizes[1]:
        h1 = sizes[0]
        b1 = sizes[1]
    else:
        h1 = sizes[1]
        b1 = sizes[0]
    if sizes[2] > sizes[3]:
        h2 = sizes[2]
        b2 = sizes[3]
    else:
        h2 = sizes[3]
        b2 = sizes[2]

    limiting_height = min(h1,h2)
    bases_sum = sum([b1,b2])
    biggest_common = min(limiting_height, bases_sum)

    final_square = biggest_common**2

    #Check if one of the rectangles didn't cause a smaller result
    #Wich happens when h1 * b1 fits h2 * b2 or vice-versa

    if(h2 > h1 and b2 > b1):
        possible_square = min(h2,b2)**2
        final_square = max(possible_square, final_square)
    elif(h1 > h2 and b1 > b2):
        possible_square = min(h1,b1)**2
        final_square = max(possible_square, final_square)

    print(final_square)
    
main()
