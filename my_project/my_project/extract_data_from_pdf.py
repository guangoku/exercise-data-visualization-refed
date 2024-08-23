file = "/Users/mingyunguan/exercise-data-visualization-refed/exercise-data-visualization-refed/my_project/data/ResourcesandGuidesReFED.pdf"

import csv
import pdfplumber

import pdfplumber
import pandas as pd



    

_table2 = []


# Open the PDF file
def df_extraction (file, page_range_start, page_range_end):
    _table = []
    with pdfplumber.open(file) as pdf:
    # Loop through each page
        for page in pdf.pages[page_range_start:page_range_end]:
            # Extract the tables from the current page
            tables = page.extract_tables()
            # Add the tables to the all_tables list
            for table in tables:
                _table.append(table)

    # Convert _table1 and _table2 to pandas DataFrames
    df = pd.concat([pd.DataFrame(table) for table in _table], ignore_index=True)

    df.columns = df.iloc[0]
    df = df.drop(df.index[0])     
    df = df[(df['#'] != '#' )].reset_index(drop=True)
    return df
df1 = df_extraction(file, 0,12)
df2 = df_extraction(file, 12,16)

# df = pd.concat([df1, df2], axis=1)
df = pd.merge(df1, df2, on='#', how='inner')
df = df.drop('Description', axis=1)
df = df[df['Grant Name'].notnull()].reset_index(drop=True)

# Write DataFrame to CSV
df.to_csv('output.csv', index=False)
