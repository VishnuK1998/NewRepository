# Gacha modeling program
# Assumes a simple model without any form of pity where pulls can be 5*, 4* or 3*
# Probability of pulling a 5* = 1.0%
# Probability of pulling a 4* = 20.0%

from random import random, choice
import numpy as np
import pandas as pd

class Gacha:

    def __init__(self):
        pity = 0
        P = []
        CL = []
        

    def pull(self):
        x = random()
        if (x<=self.P[0]): y = 0
        elif (x<=self.P[1]): y = 1
        else: y = 2
        N = choice(self.CL[y])
        self.pity = 0 if y==0 else self.pity + 1
        if self.pity>50: 
            self.P[0] += 0.02
            self.P[1] += 0.02
        return y, N

def fetchlist():
    df = pd.read_csv('charlist.csv')
    split = list(df.groupby("Rarity"))
    CL = []
    for x in split[::-1]:
        CL.append(list((x[1])["CHName"]))
    return(CL)


StdG = Gacha()
StdG.P = [0.01, 0.21, 1]
StdG.CL = fetchlist()
StdG.pity = 0

count = np.zeros(3)

N = int(input("Enter the number of pulls: "))
for i in range(0,N):
    y,name = StdG.pull()
    print(5-y,'\t',name)
      
