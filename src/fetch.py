
import pandas as pd

cl = pd.read_csv('charlist.csv')

cl.sort_values(by=[' Rarity'], ascending = False)

print(cl)