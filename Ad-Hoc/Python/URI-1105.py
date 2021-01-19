#hereafter implement OOP

def balance(a,b,c):
        reserves[a-1] -= c #debtor reserve
        reserves[b-1] += c #credor reserve

banks, debentures = input().split()

banks = int(banks)
debentures = int(debentures)

results = []

while(banks + debentures != 0):

    reserves = []
    need_loan = False
    monetary_reserve = input().split()

    for i in range(len(monetary_reserve)):
        reserves.append(int(monetary_reserve[i]))

    for i in range(debentures):

        D,C,V = input().split()
        
        D = int(D)
        C = int(C)
        V = int(V)

        balance(D,C,V)

    for reserve in reserves:
        if(reserve < 0):
            need_loan = True

    if(need_loan):
        results.append('N')

    else:
        results.append('S')

    banks, debentures = input().split()

    banks = int(banks)
    debentures = int(debentures)

for result in results:
    print(result)
