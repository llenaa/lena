#exercise day 2
import numpy as np
import pandas as pd


dat = open("data.pgxseg", 'r')     #open data frame
d = dat.readlines()
print(d)

col= ['sample', 'ref', 'start', 'end', 'log2', 'var.type', 'ref.base', 'alt.base']  #create column names
df= pd.DataFrame( columns= col)
print(df)       # i was not able to finish the exercise
