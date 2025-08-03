from tkinter import filedialog, messagebox

def export_to_csv(df):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv")])
    if file_path:
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Export Complete", f"File saved at {file_path}")

def export_to_excel(df):
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                             filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        df.to_excel(file_path, index=False)
        messagebox.showinfo("Export Complete", f"File saved at {file_path}")

def export_to_json(df):
    file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                             filetypes=[("JSON files", "*.json")])
    if file_path:
        df.to_json(file_path, orient="records")
        messagebox.showinfo("Export Complete", f"File saved at {file_path}")