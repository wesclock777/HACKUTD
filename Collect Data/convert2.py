import pandas as pd

df = pd.read_json('apple.json', orient='records', lines=True)

print(df.head())

df.to_csv('applerealtime.csv')
