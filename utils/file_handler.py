import pandas as pd
from tkinter import filedialog,messagebox
def load_file():
    file_path=filedialog.askopenfilename(
        title="Select a csv or excel file",
        filetypes=[("CSV files", "*.csv"), ("Excel Files", "*.xlsx")]
)
    if not file_path:
        return None,None
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        else:
            df=pd.read_excel(file_path)
        return df,file_path
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None,None
def save_file(df):
    file_path=filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV  files","*.csv")]





    )
    if not file_path:
        return
    try:
        df.to_csv(file_path,index=False)
        messagebox.showinfo("Success", "File saved")
    except Exception as e :
        messagebox.showerror("Error", str(e))










