from fractions import gcd

def value(N1, D1, N2, D2: int, operation: chr) -> int:
    if operation == "+":
        first_term = N1 * D2 + N2 * D1
        second_term = D1 * D2

    elif operation == "-":
        first_term = N1 * D2 - N2 * D1
        second_term = D1 * D2

    elif operation == "*":
        first_term = N1 * N2
        second_term = D1 * D2

    else:
        first_term = N1 * D2
        second_term = N2 * D1

    return first_term, second_term


def main():
    while True:
        try:
            cases = int(input())

            for i in range(cases):
                elements = [element for element in input().split()]
                N1, D1, N2, D2 = (
                    int(elements[0]),
                    int(elements[2]),
                    int(elements[4]),
                    int(elements[6]),
                )
                operation = elements[3]

                numbers = value(N1, D1, N2, D2, operation)

                common_divisor = gcd(numbers[0], numbers[1])

                if common_divisor != 1:
                    simplified_1 = int(numbers[0] / common_divisor)
                    simplified_2 = int(numbers[1] / common_divisor)

                    print(
                        str(numbers[0])
                        + "/"
                        + str(numbers[1])
                        + " = "
                        + str(simplified_1)
                        + "/"
                        + str(simplified_2)
                    )

                else:
                    print(
                        str(numbers[0])
                        + "/"
                        + str(numbers[1])
                        + " = "
                        + str(numbers[0])
                        + "/"
                        + str(numbers[1])
                    )

        except EOFError:
            break

main()
