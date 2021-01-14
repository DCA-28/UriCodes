from sys import stdin
 
def intTransform(values):
    vector = values
    for i in range(len(vector)):
      vector[i] = int(vector[i])
 
 
results = []
 
while True:
  try:
 
    n = input()
    notes = input().split()
 
    intTransform(notes)
 
    n = int(n)
    compass = 0
 
    if(sum(notes) % n != 0): #checking if its possible to build a perfect coral
      results.append(-1)
 
    #if it's buildble
 
    else:
 
      if(notes.count(notes[-1]) == n): #the coral is already harmonical
        results.append(1)
 
      else:
        compass += 1 #the first compass wasn't harmonical
        control = sum(notes) / n
 
        for i in range(-n, -1): #the last note gets the correct value naturally
          if(control - notes[i]) > 0:
            compass += (control - notes[i])
 
    if(compass > 0):
      results.append(int(compass))    
 
  except EOFError:
    for element in results:
      print(element)
 
    break
