
import matplotlib
matplotlib.use("TkAgg")  # For embedding in Tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_line(df, x_col, y_col, parent_frame):
    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col])
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    _embed_plot(fig, parent_frame)

def plot_bar(df, x_col, y_col, parent_frame):
    fig, ax = plt.subplots()
    ax.bar(df[x_col], df[y_col])
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    _embed_plot(fig, parent_frame)

def plot_hist(df, column, parent_frame):
    fig, ax = plt.subplots()
    ax.hist(df[column], bins=20)
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    _embed_plot(fig, parent_frame)

def plot_scatter(df, x_col, y_col, parent_frame):
    fig, ax = plt.subplots()
    ax.scatter(df[x_col], df[y_col])
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    _embed_plot(fig, parent_frame)

def _embed_plot(fig, parent_frame):
    """Internal function to embed Matplotlib figure in Tkinter."""
    for widget in parent_frame.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)