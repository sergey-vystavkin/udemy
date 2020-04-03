import pandas as pd
import lxml
import html5lib
from sqlalchemy import create_engine


# CSV
csv_df = pd.read_csv('example.csv')
csv_df.to_csv('example.csv', index=False)   # If index True it add new unnamed column with index to file

# Excel
# Pandas import only data it can't import formats, image, macros

# excel_df = pd.read_excel('example.xlsx', sheet_name='Sheet1')
# excel_df.to_excel('example.xlsx', sheet_name='New_sheet')

# HTML
html_data = pd.read_html('https://en.wikipedia.org/wiki/Table_(information)') # It find all tables in HTML and return list of DataFrames of each table

# SQL
engine = create_engine('sqlite:///:memory:')
csv_df.to_sql('my_table', engine)

sql_df = pd.read_sql('my_table', con=engine)

print(sql_df)
