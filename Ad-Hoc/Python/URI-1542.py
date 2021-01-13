import math

def main():
    while True:
        try:
            q, d, p = [int(number) for number in input().split()]
            pags_difference = p - q
            days_difference = p * d

            days = float(days_difference / pags_difference)
            total_pages = math.floor(days * q)

            if abs(total_pages) > 1:
                print("{} paginas".format(total_pages))

            else:
                print("{} pagina".format(total_pages))

        except ValueError:
            break

main()
