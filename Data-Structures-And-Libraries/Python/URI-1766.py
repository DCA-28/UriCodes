from operator import attrgetter

class Reindeer:
    def __init__(self, name, weight, age, height):
        self.name = name
        self.weight = weight
        self.age = age
        self.height = height

    def __repr__(self):
        return repr((self.name))


def main():
    cases = int(input())
    total_case = 1

    for i in range(cases):
        reindeer, work_reindeer = [int(number) for number in input().split()]
        reindeers = []

        for r in range(reindeer):
            reindeerAttributes = input().split()

            reindeers.append(
                Reindeer(
                    reindeerAttributes[0],
                    int(reindeerAttributes[1]),
                    int(reindeerAttributes[2]),
                    float(reindeerAttributes[3]),
                )
            )

        reindeers.sort(key=attrgetter("name"))
        reindeers.sort(key=attrgetter("height"))
        reindeers.sort(key=attrgetter("age"))
        reindeers.sort(key=attrgetter("weight"), reverse=True)

        count = 1

        print("CENARIO {%d}" % total_case)

        for reindeer in reindeers:
            if count > work_reindeer:
                break
            print("{} - {}".format(count, reindeer.name))
            count += 1

        total_case += 1


main()
