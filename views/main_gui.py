
# File: views/main_gui.py
import tkinter as tk
from tkinter import ttk, messagebox

from utils.file_handler import load_file, save_file
from utils.theme_manager import apply_theme
from utils.language_manager import get_text

from controllers.data_processor import (
    calculate_mean, calculate_median, calculate_std, calculate_correlation,
    drop_missing, fill_missing_with_mean, fill_missing_with_median,
    filter_rows, sort_data, group_data
)
from controllers.data_stats import get_summary_statistics
from controllers.data_exporter import export_to_csv, export_to_excel, export_to_json
from controllers.plot_generator import plot_line, plot_bar, plot_hist, plot_scatter
from controllers.real_time_plot import start_real_time_plot
from controllers.thread_manager import run_in_thread

current_df = None
current_lang = "English"
dark_mode = False

def start_gui():
    global current_df, current_lang, dark_mode

    root = tk.Tk()
    root.title("Smart Data Analyzer & Visualizer")
    root.geometry("1000x600")

    # --- Top Menu ---
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label=get_text(current_lang, "load_file"), command=lambda: load_data(preview_area))
    file_menu.add_command(label=get_text(current_lang, "save_file"), command=lambda: save_data())
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)

    lang_menu = tk.Menu(menubar, tearoff=0)
    lang_menu.add_command(label="English", command=lambda: change_language("English"))
    lang_menu.add_command(label="Bangla", command=lambda: change_language("Bangla"))
    menubar.add_cascade(label="Language", menu=lang_menu)

    theme_menu = tk.Menu(menubar, tearoff=0)
    theme_menu.add_command(label="Dark Mode", command=lambda: toggle_theme(True))
    theme_menu.add_command(label="Light Mode", command=lambda: toggle_theme(False))
    menubar.add_cascade(label="Theme", menu=theme_menu)

    # --- Frame Layout ---
    frame_left = tk.Frame(root, width=300)
    frame_left.pack(side="left", fill="y")

    frame_right = tk.Frame(root)
    frame_right.pack(side="right", fill="both", expand=True)

    # --- Data Preview ---
    preview_area = tk.Text(frame_left, height=20, width=40)
    preview_area.pack(pady=5)

    # --- Buttons for Processing ---
    btn_frame = tk.Frame(frame_left)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text=get_text(current_lang, "mean"), command=lambda: calc_stat("mean")).grid(row=0, column=0, pady=2)
    tk.Button(btn_frame, text=get_text(current_lang, "median"), command=lambda: calc_stat("median")).grid(row=1, column=0, pady=2)
    tk.Button(btn_frame, text=get_text(current_lang, "std_dev"), command=lambda: calc_stat("std")).grid(row=2, column=0, pady=2)
    tk.Button(btn_frame, text=get_text(current_lang, "correlation"), command=lambda: calc_stat("correlation")).grid(row=3, column=0, pady=2)

    tk.Button(btn_frame, text=get_text(current_lang, "drop_na"), command=lambda: process_data("drop_na")).grid(row=4, column=0, pady=2)
    tk.Button(btn_frame, text=get_text(current_lang, "fill_mean"), command=lambda: process_data("fill_mean")).grid(row=5, column=0, pady=2)
    tk.Button(btn_frame, text=get_text(current_lang, "fill_median"), command=lambda: process_data("fill_median")).grid(row=6, column=0, pady=2)

    tk.Button(btn_frame, text="Real-Time Plot", command=lambda: start_real_time_plot(frame_right)).grid(row=7, column=0, pady=2)

    tk.Button(btn_frame, text="Export CSV", command=lambda: export_to_csv(current_df)).grid(row=8, column=0, pady=2)
    tk.Button(btn_frame, text="Export Excel", command=lambda: export_to_excel(current_df)).grid(row=9, column=0, pady=2)
    tk.Button(btn_frame, text="Export JSON", command=lambda: export_to_json(current_df)).grid(row=10, column=0, pady=2)

    # --- Plot Buttons ---
    plot_frame = tk.Frame(frame_left)
    plot_frame.pack(pady=5)

    tk.Button(plot_frame, text="Line Plot", command=lambda: choose_plot("line", frame_right)).grid(row=0, column=0)
    tk.Button(plot_frame, text="Bar Plot", command=lambda: choose_plot("bar", frame_right)).grid(row=1, column=0)
    tk.Button(plot_frame, text="Histogram", command=lambda: choose_plot("hist", frame_right)).grid(row=2, column=0)
    tk.Button(plot_frame, text="Scatter Plot", command=lambda: choose_plot("scatter", frame_right)).grid(row=3, column=0)

    root.mainloop()

def load_data(preview_area):
    global current_df
    df, path = load_file()
    if df is not None:
        current_df = df
        preview_area.delete("1.0", tk.END)
        preview_area.insert(tk.END, str(df.head()))

def save_data():
    global current_df
    if current_df is not None:
        save_file(current_df)

def calc_stat(stat_type):
    global current_df
    if current_df is None:
        messagebox.showerror("Error", "No file loaded")
        return

    col = ask_column_name()
    if col not in current_df.columns:
        messagebox.showerror("Error", "Invalid column name")
        return

    if stat_type == "mean":
        result = calculate_mean(current_df, col)
    elif stat_type == "median":
        result = calculate_median(current_df, col)
    elif stat_type == "std":
        result = calculate_std(current_df, col)
    elif stat_type == "correlation":
        col2 = ask_column_name(prompt="Enter second column for correlation:")
        result = calculate_correlation(current_df, col, col2)
    else:
        result = None

    messagebox.showinfo("Result", f"{stat_type} = {result}")

def process_data(action):
    global current_df
    if current_df is None:
        return

    if action == "drop_na":
        current_df = drop_missing(current_df)
    elif action == "fill_mean":
        current_df = fill_missing_with_mean(current_df)
    elif action == "fill_median":
        current_df = fill_missing_with_median(current_df)

    messagebox.showinfo("Info", "Processing complete!")

def choose_plot(plot_type, frame_right):
    global current_df
    if current_df is None:
        return

    if plot_type == "hist":
        col = ask_column_name()
        plot_hist(current_df, col, frame_right)
    else:
        col_x = ask_column_name(prompt="Enter X column:")
        col_y = ask_column_name(prompt="Enter Y column:")
        if plot_type == "line":
            plot_line(current_df, col_x, col_y, frame_right)
        elif plot_type == "bar":
            plot_bar(current_df, col_x, col_y, frame_right)
        elif plot_type == "scatter":
            plot_scatter(current_df, col_x, col_y, frame_right)

def ask_column_name(prompt="Enter column name:"):
    return tk.simpledialog.askstring("Column", prompt)

def change_language(lang):
    global current_lang
    current_lang = lang
    messagebox.showinfo("Info", f"Language changed to {lang}")

def toggle_theme(dark):
    global dark_mode
    dark_mode = dark
    apply_theme(tk._default_root, dark_mode)