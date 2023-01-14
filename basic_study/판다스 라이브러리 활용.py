import pandas as pd 
names = ['bob', 'jessica', 'mary', 'john', 'mel']
births = [ 968, 155, 77, 578, 973]
custom = [1, 5, 25, 13, 23232]

babydataset = list(zip(names,births))
df = pd.DataFrame(data = babydataset, columns=['names', 'birth'])

df.head()