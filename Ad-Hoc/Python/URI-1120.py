def zero_sequence(number: "as string") -> str:
    final_position = 0

    for i in range(len(number)):
        if number[i] != "0":
            final_position = i  # position when the zero sequence is over
            break

    if final_position == 0:  # After iterating all number, no one were different of zero
        return 0

    else:
        number = number[final_position : len(number)]
        return number


def main():

    while True:
        broken_key, original = [number for number in input().split()]
        if int(broken_key) + int(original) == 0:
            break
            # Starting the analysis

        if original.find(broken_key) == -1:  # No broken key used in number
            print(original)

        else:
            new_number = original.replace(broken_key, "")

            try:
                if (
                    new_number[0] == "0"
                ):  # find leading zeros but some valid digitis exists
                    result = zero_sequence(new_number)
                    print(result)

                else:
                    print(
                        new_number
                    )  # Broken key used but no leading zero had appear

            except IndexError:
                print(0)  # All digits were leading zeros


main()
