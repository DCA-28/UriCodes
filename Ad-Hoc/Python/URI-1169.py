def main():
    cases = int(input())
    for i in range(cases):
        houses = int(input())
        wheat = 0
        for j in range(houses):
            wheat += 2**j
        print("{} kg".format(int(wheat/12000)))

main()
