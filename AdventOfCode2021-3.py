

file = open("txt-3.txt", 'r')
gammaRate = ""
one = 0
zero = 0
counter = 0
i = 0
epsilonRate = ""
e = 0
g = 0





list = []

for line in file:
    list.append(line.strip())


while(counter < len(list[0])):
    for j in range(len(list)):
        if list[j][i] == "1":
             one += 1
        else:
             zero += 1
    if(one > zero):
        gammaRate += "1"
        epsilonRate += "0"
    else:
        gammaRate += "0"
        epsilonRate += "1"
    i += 1
    counter += 1
    one = 0
    zero = 0
    
for i in range(len(gammaRate)):
    if(gammaRate[i] == "1"):
        g +=  2**(len(gammaRate) - i - 1)

    
print(epsilonRate)
        
for i in range(len(epsilonRate)):
    print(i)
    if(epsilonRate[i] == "1"):
        e +=  2**(len(epsilonRate) - i - 1)
print(e*g)

    
    

