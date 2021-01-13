def find(dictionary: "dict of stones", value: "stone to find") -> "identifier":
    if value in dictionary.keys():
        return "{} found at {}".format(value, dictionary[value])

    else:
        return "{} not found".format(value)


def main():

    global_case = 1

    while True:
        entry = input().split()
        q, n = int(entry[0]), int(entry[1])
        if q + n == 0:
            break
        stones = [None] * q
        for i in range(len(stones)):
            stones[i] = int(input())
        stones.sort()

        stones_dict = {}
        counter = 1
        for stone in stones:
            if stone not in stones_dict.keys():
                stones_dict[stone] = counter
            counter += 1

        print("CASE# {}:".format(global_case))
        for i in range(n):
            value = int(input())
            ans = find(stones_dict, value)
            print(ans)

        global_case += 1


main()
