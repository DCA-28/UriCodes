def get_species(dictionary: "dict of species", flag: "indicate calling scope") -> float:
    trees = [specie for specie in dictionary.keys()]
    trees.sort()
    total = sum(list(dictionary.values()))
    for tree in trees:
        print("%s %.4f" % (tree, (dictionary[tree] / total) * 100))
    dictionary.clear()
    if flag is "loop":
        print()


def main():
    cases = int(input())
    line_feed = input()
    total_feed = 1
    trees_dict = {}
    while True:
        try:
            specie = input()
            if len(specie) == 0:
                total_feed += 1
                get_species(trees_dict, "loop")
            else:
                try:
                    trees_dict[specie] += 1
                except KeyError:
                    trees_dict[specie] = 1
        except EOFError:
            get_species(trees_dict, "end")
            break


main()
