def reset_state(dicitonary) -> None:
    for element in dicitonary.keys():
        dicitonary[element] = []


def sort_dict(dictionary) -> None:
    for index in dictionary.keys():
        dictionary[index] = sorted(dictionary[index])


def main():

    """ dictionaries for solving the problem """

    color_size_dict = {
        "brancoP": 1,
        "brancoM": 2,
        "brancoG": 3,
        "vermelhoP": 4,
        "vermelhoM": 5,
        "vermelhoG": 6,
    }

    owners_dict = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
    }

    relate_dict = {
        1: "branco P",
        2: "branco M",
        3: "branco G",
        4: "vermelho P",
        5: "vermelho M",
        6: "vermelho G",
    }

    to_jump = 0

    while True:

        cases = int(input())
        if cases == 0:
            break
        if to_jump != 0:
            print()
        for i in range(cases):
            name = input()
            attributes = input().split()

            case_number = color_size_dict[attributes[0] + attributes[1]]
            owners_dict[case_number].append(name)

        sort_dict(owners_dict)

        for number, lst in owners_dict.items():
            if len(lst) == 0:
                continue
            for owner in lst:
                print(relate_dict[number], owner)

        reset_state(owners_dict)
        to_jump += 1

main()
