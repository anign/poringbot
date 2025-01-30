import pandas as pd
import sqlite3

db = sqlite3.connect(':memory:')
dfs = pd.read_excel('somefile.xlsx', sheet_name=None)
for table, df in dfs.items():
    df.to_sql(table, db)