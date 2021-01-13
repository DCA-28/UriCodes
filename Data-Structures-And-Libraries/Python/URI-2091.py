def main():
    while True:
        numbers = int(input())
        if numbers == 0:
            break
        values = input().split()

        values_dict = {}

        for value in values:
            try:
                values_dict[value] += 1

            except KeyError:
                values_dict[value] = 1

        for element in values_dict:
            if values_dict[element] % 2 != 0:
                print(element)
                break


main()
