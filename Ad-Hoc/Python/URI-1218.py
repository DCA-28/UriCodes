def main():
    global_cases = 1
    while True:
        try:
            to_find = input()

            if global_cases > 1:
                print()

            shoes = input().split()

            flag = False
            total_ocurrences = 0
            male_pair = 0
            female_pair = 0

            for information in shoes:
                if information == to_find:
                    total_ocurrences += 1
                    flag = True

                else:
                    if flag:
                        if information == "M":
                            male_pair += 1
                        elif information == "F":
                            female_pair += 1
                        flag = False

            print("Caso {}:".format(global_cases))
            print("Pares Iguais: {}".format(total_ocurrences))
            print("F: {}".format(female_pair))
            print("M: {}".format(male_pair))

            global_cases += 1

        except Exception:
            break


main()
