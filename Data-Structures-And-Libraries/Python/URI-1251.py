def organize(chars_array: "list of chars", last_frequency: int) -> None:

    chars_array = list(reversed(chars_array))

    for i in range(len(chars_array)):
        chars_array[i] = ord(chars_array[i])

    for element in chars_array:
        print("{} {}".format(element, last_frequency))


def set_order(recurrence: "list of tuples") -> None:

    last_frequency = recurrence[0][0]
    last_iteration = [recurrence[0][1]]

    for i in range(1, len(recurrence)):

        if recurrence[i][0] == last_frequency:
            last_iteration.append(recurrence[i][1])

        else:

            if len(last_iteration) > 1:
                organize(last_iteration, last_frequency)
                last_iteration.clear()
                last_iteration.append(recurrence[i][1])
                last_frequency = recurrence[i][0]

            # when the len is equal to 1

            else:

                print("{} {}".format(ord(last_iteration[0]), last_frequency))
                last_iteration.clear()
                last_iteration.append(recurrence[i][1])
                last_frequency = recurrence[i][0]

    # making the final call for the last_iteration

    organize(last_iteration, last_frequency)


def main():

    next_input = input()

    while True:

        try:

            chars_dict = {}

            char_values = next_input

            if char_values == "":
                raise EOFError

            for char in char_values:
                try:
                    if char == "\n":
                        continue

                    chars_dict[char] += 1

                except KeyError:
                    chars_dict[char] = 1

            recurrence = [None] * len(chars_dict)

            count = 0

            for element, ocorrunce in chars_dict.items():

                recurrence[count] = (ocorrunce, element)

                count += 1

            recurrence.sort()

            set_order(recurrence)  # toDo

            next_input = input()

            if next_input != "":

                print()

        except EOFError:
            break


main()
