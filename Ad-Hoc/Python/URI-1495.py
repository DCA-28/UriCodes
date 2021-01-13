def main():
    while True:
        try:
            total_points = 0
            to_draw = 0
            defeats = []
            balance = True  # Incating some goal in goals_balance

            matches, goals_balance = [int(i) for i in input().split()]

            for i in range(matches):

                goals_scored, goals_conceded = [
                    int(i) for i in input().split()
                ]

                if goals_scored > goals_conceded:
                    total_points += 3

                elif goals_scored == goals_conceded:
                    if goals_balance > 0:
                        total_points += 3
                        goals_balance -= 1
                    else:
                        total_points += 1
                        balance = False

                elif goals_conceded - goals_scored == 1:
                    to_draw += 1

                else:
                    defeats.append(
                        goals_conceded - goals_scored
                    )  # Difference to draw

            defeats.sort()

            if balance:  # More rentable trade
                for i in range(to_draw):
                    if goals_balance >= 2:  # Possible turn over
                        total_points += 3
                        goals_balance -= 2

                    elif goals_balance == 1:
                        total_points += 1
                        goals_balance -= 1
                        balance = False
                        break

                    else:
                        balance = False
                        break

            if balance:  # Secod most rentable trade
                for difference in defeats:
                    if goals_balance >= difference + 1:  # Possible turn over
                        total_points += 3
                        goals_balance = goals_balance - (difference + 1)

                    elif goals_balance == difference:
                        total_points += 1
                        goals_balance = goals_balance - difference
                        balance = False
                        break

                    else:  # No more moves
                        balance = False
                        break

            print(total_points)
            # print(to_draw)
            # print(defeats)

        except EOFError:
            break


main()
