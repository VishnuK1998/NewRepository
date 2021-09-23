# Gacha modeling program
# Assumes a simple model without any form of pity where pulls can be 5*, 4* or 3*
# Probability of pulling a 5* = 1.0%
# Probability of pulling a 4* = 20.0%

from random import random

# Function to simulate gacha pull
def gachapull (P):
    x = random()
    if (x<=P[0]): J = 0
    elif (x<=P[1]): J = 1
    else: J = 2
    return J


N = int(input("Enter the number of pulls: "))

#No. of characters pulled
L = [0,0,0]

#Base cumulative probabilities
P = [0,0,0]
P[0] = 0.01
P[1] = 0.20 + P[0]
P[2] = 1

#Counting the results
for i in range(0,N):
    y = gachapull(P)
    L[y] += 1
    
print("Pull results: {}".format(L))    
