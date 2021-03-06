import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

data = [1, 3, 2, 4]

root = tkinter.Tk()

# create plot(s)
fig = plt.Figure()
sub = fig.add_subplot('111') # add plot as first plot (third "1") to figure (with one row (first "1") and one column (second "1")
sub.plot(data)

# create canvas with plot and add (pack) to tkinter's window
canvas = FigureCanvasTkAgg(fig, master=root) # fig = figure with plot, master = window, frame or widget which has to display it
canvas.draw()
canvas.get_tk_widget().pack(side='top', fill='both', expand=1) # `side='top', fill='both', expand=1` will resize plot when you resize window

tkinter.mainloop()

