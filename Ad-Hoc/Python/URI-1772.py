def main():
    while True:
        number, swaps = [int(element) for element in input().split()]
        if number + swaps == 0:
            break
        bin_number = bin(number)
        bits_dict = {key: 0 for key in range(32)}
        index = len(bin_number) - 3  # -3 -> The 0, b and starting at 0
        values = []

        values.append(number)

        for bit in range(2, len(bin_number)):
            bits_dict[index] = int(bin_number[bit])
            index -= 1

        # print(bits_dict)
        # print(ones_indexes)

        for i in range(swaps):
            swap = [int(number) for number in input().split()]

            if bits_dict[swap[0]] == bits_dict[swap[1]]:
                continue
            else:
                if bits_dict[swap[1]] == 1:  # 0 1 -> 1 0
                    number += 2 ** swap[0]
                    number -= 2 ** swap[1]
                else:  # 1 0 -> 0 1
                    number -= 2 ** swap[0]
                    number += 2 ** swap[1]

                bits_dict[swap[0]], bits_dict[swap[1]] = (
                    bits_dict[swap[1]],
                    bits_dict[swap[0]],
                )

                values.append(number)

        # print(bits_dict)
        print(values[-1], end=" ")
        print(max(values), end=" ")
        print(min(values))

main()
