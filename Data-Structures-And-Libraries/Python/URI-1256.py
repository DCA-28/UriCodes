def initialize_map(dictionary, adresses) -> None:
    args = [0, adresses]
    for i in range(*args):
        dictionary[i] = []


def get_values(dictionary) -> None:

    for element in dictionary.keys():
        if dictionary[element] == []:
            print("{} -> \\".format(element))
        else:
            print("{} -> ".format(element), end="")
            for number in dictionary[element]:
                print("{} -> ".format(number), end="")
            print("\\")


def main():

    cases = int(input())
    for i in range(cases):
        adresses, keys = [int(element) for element in input().split()]
        values = input().split()

        hash_map = {}
        initialize_map(hash_map, adresses)

        for number in values:
            hash_map[int(number) % adresses].append(number)

        get_values(hash_map)

        if not (i == cases - 1):
            print()


main()
