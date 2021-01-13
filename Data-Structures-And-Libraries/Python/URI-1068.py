def analysis(equation: "as string") -> str:
    state = 0
    values = [41, 40]

    for digit in equation:
        if ord(digit) not in values:
            continue
        else:
            if digit == ")" and state == 0:
                return "incorrect"
            elif digit == ")" and state > 0:
                state -= 1
            elif digit == "(":
                state += 1

    if state != 0:  # neutral state
        return "incorrect"
    else:
        return "correct"


def main():
    while True:
        try:
            equation = input()
            if equation == '':
                print('correct')
                continue

            # Starting the analysis

            if equation.count("(") != equation.count(")"):
                print("incorrect")
            else:
                result = analysis(equation)
                print(result)
        except EOFError:
            break


main()
