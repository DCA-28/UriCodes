def main():
    while True:
        try:
            size, operations = [int(number) for number in input().split()]

            parking = "-" * size
            parking_dict = {}
            balance = 0

            for i in range(operations):
                entry = input().split()

                if len(entry) == 3:
                    status, car_palate, car_size = entry[0], entry[1], entry[2]

                elif len(entry) == 2:
                    status, car_palate = entry[0], entry[1]

                if status == "C":  # Verify possible space to park
                    handle = parking.find("-" * int(car_size))

                    if handle != -1:
                        parking = parking.replace(
                            "-" * int(car_size), "*" * int(car_size), 1
                        )

                        parking_dict[car_palate] = (
                            handle,
                            handle + int(car_size) - 1,
                        )

                        balance += 10

                else:
                    initial = parking_dict[car_palate][0]
                    final = parking_dict[car_palate][1]

                    if final + 1 == len(parking):  # Adjusting the right limit
                        final = len(parking) - 1

                    parking = ("-" * (final - initial + 1)).join(
                        [parking[0:initial], parking[final + 1 : len(parking)]]
                    )

                    parking_dict.pop(car_palate)

            print(balance)

        except EOFError:  # Change for EOFError when running in Ideone
            break



main()
