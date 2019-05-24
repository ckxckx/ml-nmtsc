import pandas as pd
myset = pd.read_csv("train_set_O2.csv")

cout = 0
for idx,row in myset.iterrows():
    cout +=1
    print "\n---------"
    print row
    if cout >10:
        break