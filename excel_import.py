#This python script is a substite for Power Query in regards to importing a source of data into an excel file.
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('Primary Table for Import')

root.filename = filedialog.askopenfilename(initialdir= "/Macintosh HD/Users/matthewventura/Documents", title="Select an Excel File", filetypes=(("xls files", "*.xls"),("xlsx files", "*.xlsx")))
'''
ent1 = tk.Entry(root,font=40)
ent1.grid(row=2,col=2)
'''
# install GUI to navigate to excel files: first the origin, then the destination
'''folder = r'/Macintosh HD/Users/matthewventura/Documents/Cousera/Google_Data_Analyst/ExcelFiles' #not in use, just a temporary variable declaration
df_total  = pd.DataFrame()
files = os.listdir(folder)
'''
'''for file in files: #loop through all files in folder
    if file.endswith('.xlsx'):
        excel_file = pd.ExcelFile(f'{folder}/{file}')
        sheets = excel_file.sheet_names
        for sheet in sheets:
            df = excel_file.parse(sheet_name = sheet)
            df_total = df_total.append(df)

df_total.to_excel(f'{folder}/combined_file.xlsx')
'''
