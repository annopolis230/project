
file = open("C:/test.txt","r")
data = str(file.read())
dataList = []
readList = []

num = 0

for i in data:
    dataList.append(i)

x = True

for i in dataList:
    if i != ' ' and i != ',' and i != '\n':
        num = num+1
        if i.isdigit() == False:
            print("Input must be a number")
            x = False
            break
        else:
            print('Input Data', num,':', i)
            readList.append(int(i))
            

if x == True:
    deltaQ = readList[0] - readList [1]
    deltaP = readList[2] - readList [3]
    avgQ = (readList[0] + readList[1])/2
    avgP = (readList[2] + readList [3]) / 2
    elasticity = (deltaQ/avgQ)/(deltaP/avgP)
    elastype = ""

    if (elasticity == 1):
        elastype = "Unitary"
    elif (elasticity > 1) and (elasticity < 5):
        elastype = "Relatively Elastic"
    elif (elasticity > 5):
        elastype = "Highly Elastic"
    elif (elasticity <1) and (elasticity > 0.5):
        elastype = "Relatively Inelastic"
    elif (elasticity < 0.5):
        elastype = "Highly Inelastic"

    print("Elasticity Type: ", elastype)
    print("Elasticity Coefficient: ", elasticity)

else:
    print("Calculation aborted")



