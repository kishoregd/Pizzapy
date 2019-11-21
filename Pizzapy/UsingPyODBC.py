import pyodbc           # python odbc
import pandas as pd     # for dataframe

conn_str = ('server=WIN-EEL3AK31AJF;database=PizzapyDB;TRUSTED_CONNECTION=yes')

conn = pyodbc.connect(r'DRIVER={ODBC Driver 13 for SQL Server};' + conn_str)

sql = "SELECT TOP 10 * FROM [PizzapyDB].[dbo].[Order]"

df = pd.read_sql(sql,conn)

print(df)