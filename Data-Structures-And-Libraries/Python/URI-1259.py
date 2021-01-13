def main():
    cases = int(input())
    odd = []
    even = []

    for i in range(cases):
        entry = int(input())
        if entry % 2 == 0:
            even.append(entry)
        else:
            odd.append(entry)

    even.sort()
    odd.sort(reverse=True)

    for element in even:
        print(element)
    for element in odd:
        print(element)


main()
