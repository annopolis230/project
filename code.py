import math

#import data
file = open("C:\pythontest.txt", "r")
data = file.readlines()

#write input data
num = -1
for i in range(4):
    num = num+1
    print("Input Data: ", data[num])

#elasticity calculations
deltaQ = int(data[0]) - int(data[1])
deltaP = int(data[2]) - int(data[3])
avgQ = (int(data[0]) + int(data[1]))/2
avgP = (int(data[2]) + int(data[3]))/2
elasticity = (deltaQ/avgQ)/(deltaP/avgP)
elastype = ""

#ranges
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

#print elasticity
print("Elasticity Type: ", elastype)
print("Elasticity Coefficient: ", elasticity)


file.close()