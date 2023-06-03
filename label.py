import pandas as pd

df = pd.read_table('coco-labels-paper.txt',index_col=False)
col = str(df.columns[0])

result = df.to_numpy().reshape(-1,).tolist()
result.insert(0,col)
