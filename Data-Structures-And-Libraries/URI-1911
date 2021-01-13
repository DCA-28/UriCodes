def main():
    while True:
        names = int(input())
        if names == 0:
            break
        original_signatures = {}
        fakes = 0

        for i in range(names):
            name, signature = [element.rstrip() for element in input().split()]
            original_signatures[name] = signature

        checks = int(input())

        for i in range(checks):
            key, value = [element.rstrip() for element in input().split()]
            compare_value = original_signatures[key]
            count = 0
            for j in range(len(compare_value)):
                if ord(value[j]) != ord(compare_value[j]):
                    count += 1
                if count > 1:
                    fakes += 1
                    break

        print(fakes)

main()
