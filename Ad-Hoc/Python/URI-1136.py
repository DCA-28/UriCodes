def main():
    while True:
        entry = [int(i) for i in input().split()]
        if sum(entry) == 0:
            break
        remaining_numbers = set([int(i) for i in input().split()])

        # Starting the analyses

        if entry[1] > entry[0]:
            print("Y")
            continue
        elif (entry[0] not in remaining_numbers) or (0 not in remaining_numbers):
            print("N")
            continue
        else:
            numbers_sequence = set([int(i) for i in range(0, entry[0] + 1)])
            calculated = set([0])
            used = set([])

            for number in remaining_numbers:
                used.add(number)
                subtract = remaining_numbers.difference(used)
                for element in subtract:
                    calculated.add(abs(number - element))

            if calculated == numbers_sequence:
                print("Y")
                continue

            else:
                print("N")


main()
