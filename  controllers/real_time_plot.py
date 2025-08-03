import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

def start_real_time_plot(parent_frame, interval=1000):
    """Simulates live data updates in a plot every `interval` ms."""
    fig, ax = plt.subplots()
    x_data, y_data = [], []

    def update(frame):
        x_data.append(len(x_data) + 1)
        y_data.append(random.randint(0, 100))
        ax.clear()
        ax.plot(x_data, y_data)
        ax.set_title("Real-Time Data Plot")
        ax.set_xlabel("Time")
        ax.set_ylabel("Value")

    ani = FuncAnimation(fig, update, interval=interval)
    _embed_plot(fig, parent_frame)

def _embed_plot(fig, parent_frame):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
