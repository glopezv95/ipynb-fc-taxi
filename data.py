import os
from pathlib import Path
import pandas as pd

df = pd.DataFrame()
PROJECT_PATH = Path().parent.resolve()
TAXI_DATA_PATH = Path(PROJECT_PATH, 'data')

for entry in os.scandir(TAXI_DATA_PATH):
    if '.parquet' in entry.path:
        
        parquet = pd.read_parquet(entry.path)
        df = pd.concat([df, parquet], ignore_index = True)

df.drop(df.columns[df.columns.str.lower().str.contains('id')], axis = 1, inplace = True)
df.drop(['tpep_dropoff_datetime', 'payment_type', 'store_and_fwd_flag'], axis = 1, inplace = True)

df['tpep_pickup_datetime'] = df['tpep_pickup_datetime'].dt.date
df = df.groupby('tpep_pickup_datetime').agg('sum')

start_2023 = pd.Timestamp('2023-01-01').date()
end_2024 = pd.Timestamp('2023-12-31').date()

df = df.loc[
    (df.index >= start_2023) &
    (df.index < end_2024), :]

df.index = pd.to_datetime(df.index)
df = df.asfreq(freq = 'D')