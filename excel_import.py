#This python script is a substite for Power Query in regards to importing a source of data into an excel file.
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

class Window(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Import/Merge Excel Files")
        self.pack(fill = 'both', expand = 1)
        self.filepath = tk.StringVar()

        quitBtn = tk.Button(self, text = 'Quit', command = self.close_window)
        quitBtn.place(x = 0, y = 0)

        browseBtn1 = tk.Button(self, text = 'Browse Root', command = self.first_browser)
        browseBtn1.place(x = 880, y = 0)
        #browseBtn1.pack(side= tk.Right, x = 0, y = 30)

        filepathText = tk.Entry(self, textvariable= self.filepath, width= 80)
        filepathText.pack()

    def close_window(self):
        root.destroy()

    def show_file_browser(self):
        self.filename = filedialog.askopenfilename()
        return self.filename

    def first_browser(self):
        file = self.show_file_browser()
        self.filepath.set(file)


root = tk.Tk()
root.title('Primary Table for Import')
root.geometry('1000x400')

app = Window(root)

root.mainloop()

'''def select_file():
    filetypes_lst = (("Excel Files", "*.xls*"), ("xls files","*.xls"), ("all files", "*.*"))
    title_str = "Select File"
    dir_str = "/Macintosh HD/Users/matthewventura/Documents"
    root.filename = filedialog.askopenfilename(parent = root, initialdir=dir_str, title= title_str, filetypes= filetypes_lst)
    select_label = tk.Label(root, text=root.filename).pack()
    

tk.Button(root, test = "Select File", command=select_file).pack
'''


'''root.filename = filedialog.askopenfilename(initialdir= "/Macintosh HD/Users/matthewventura/Documents", title="Select an Excel File", filetypes=(("Excel Files", "*.xls*"), ("xls files","*.xls"), ("all files", "*.*")))


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
