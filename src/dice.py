#Python file to roll dice

from random import randint
n = int(input("Enter the number of rolls: "))

for i in range(0,n):
    print(randint(1,6))

