def loop(samples, values):
    n = samples
    vector = values
    peaks = 0
    countedPeaks = []
    magnitude = []

    #creating my magnitude sequence to find peaks
    magnitude.append(vector[n-1])

    for i in range(0, n):
        magnitude.append(vector[i])

    magnitude.append(vector[0])

    #vector to find peaks is made

    for i in range(1, n+1):
        #think i could be smarter here without that 'or'
        
        if(((magnitude[i] < magnitude[i-1]) and (magnitude[i] < magnitude[i+1])) or ((magnitude[i] > magnitude[i-1]) and (magnitude[i] > magnitude[i+1]))): 
            peaks = peaks + 1
            countedPeaks.append(magnitude[i])

    print(peaks) #number of peaks

#main program

vectorOfSamples = []
vectorOfValues = []

while(True):    
    samples = int(input())

    if(samples == 0):
        break

    else:
        vectorOfSamples.append(samples)        
        values = input().split()
        for i in range(0, len(values)):
                values[i] = int(values[i])

        vectorOfValues.append(values)
        
#calling the function as long as exist inputs

for i in range(0, len(vectorOfSamples)):
    samples = vectorOfSamples[i]
    values = vectorOfValues[i]
    loop(samples, values)
