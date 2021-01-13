def main():
    while True:
        try:
            entry = input().split()
            owner = entry[0].rstrip()
            gifts = int(entry[1])

            gifts_list = []

            for i in range(gifts):

                name = input().rstrip()
                price, priority = [float(number) for number in input().split()]

                gifts_list.append((name, price, priority))

            gifts_list.sort(key=lambda element: element[0])
            gifts_list.sort(key=lambda element: element[1])
            gifts_list.sort(key=lambda element: element[2], reverse=True)

            print("Lista de {}".format(owner))

            for gift in gifts_list:
                print("{} - R${:.2f}".format(gift[0], gift[1]))

            print()

        except EOFError:  
            break



main()
