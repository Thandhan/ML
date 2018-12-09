import pandas as pd
hypo = ['%','%','%','%','%','%']
dataset = pd.read_csv('p1.csv')
X = dataset.iloc[:, :].values
data = []
for row in X:
    if row[len(row)-1].upper() == "YES":
        data.append(row)
print('The Training Examples are : ')
for x in data:
    print(x)
print('\nSteps of Find-s Algorithm :\n') 
hypo = data[0]
hypo = hypo[0:-1]
for i in range(len(data)):
    for k in range(d):
        if hypo[k] != data[i][k]:
            hypo[k] = '?'
    print(hypo)
print('\n\nMax Specific Find-S hypothesis for given csv are :')
print(hypo)