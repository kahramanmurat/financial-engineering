import pandas as pd
from glob import glob

files = glob('data/*.csv')
full_df = []

for f in files:
    print(f)
    df = pd.read_csv(f)

    symbol = f.split('/')[1].split('.')[0]
    df['Name'] = symbol

    full_df.append(df)

full_df = pd.concat(full_df, ignore_index=True)
full_df.to_csv('sp500full.csv', index=False)
