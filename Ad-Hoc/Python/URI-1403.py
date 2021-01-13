n, m = input().split()
n, m = int(n), int(m)

while True:

    if n + m == 0:
        break

    numbers = {}

    for i in range(int(n)):
        values = input().split()

        for element in values:
            try:
                numbers[element] += 1

            except Exception:
                numbers[element] = 1

    most_recurrence = [None] * len(numbers)

    count = 0

    for element, occurrence in numbers.items():
        most_recurrence[count] = (occurrence, element)

        count += 1

    most_recurrence.sort()
    most_recurrence = list(reversed((most_recurrence)))

    second_bigger = most_recurrence[1][0]
    final_result = []

    for i in range(1, len(most_recurrence)):
        if most_recurrence[i][0] < second_bigger:
            break

        else:
            final_result.append(int(most_recurrence[i][1]))

    final_result.sort()

    for element in final_result:
        print(str(element), end=" ")

    print()

    n, m = input().split()
    n, m = int(n), int(m)
