def custom_sort(string) -> "Sorted by length":

    return len(string)


def main():

    cases = int(input())

    for i in range(cases):
        strings = input().split()

        strings = sorted(strings, key=custom_sort, reverse=True)

        space_control = len(strings)

        for i in range(len(strings)):
            if i != space_control - 1:
                print(strings[i], end=" ")
            else:
                print(strings[i])


main()
