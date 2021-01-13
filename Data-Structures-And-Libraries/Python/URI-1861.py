def set_order(murderers_dict, murdered_set) -> None:
    murderers_set = set(murderers_dict.keys())
    unredeble_data = (murderers_set).intersection(murdered_set)
    remaning_kilers = sorted(list(murderers_dict.items()))

    print("HALL OF MURDERERS")

    for element in remaning_kilers:
        if element[0] in unredeble_data:
            continue
        else:
            print("{} {}".format(element[0], element[1]))


def main():
    murderers_dict = {}
    murdered_set = set([])
    while True:
        try:
            names = input().split()
            if len(names) == 0:
                raise EOFError
            murdered_set.add(names[1])
            murderers_dict[names[0]] += 1
        except KeyError:
            murderers_dict[names[0]] = 1
        except EOFError:
            set_order(murderers_dict, murdered_set)
            break


main()
