from tkinter import *

root = Tk()
root.geometry('300x200')

# Define the scale widgets
scale_min = Scale(root, from_=0, to=1000, orient=HORIZONTAL, length=400, label='Min value')
scale_max = Scale(root, from_=0, to=100, orient=HORIZONTAL, length=200, label='Max value')

# Set initial values for the scales
scale_min.set(20)
scale_max.set(80)

# Position the scales on the root window
scale_min.pack(pady=20)
scale_max.pack()

root.mainloop()
