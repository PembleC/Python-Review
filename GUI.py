"""
Carson Pemble
8/26/2020
Python GUI
"""

from tkinter import *

root = Tk()     # start the window

# Labels
theLabel = Label(root, text="This is Carson's First Python GUI", bg="white", fg="black")
theLabel.pack()

labelTwo = Label(root, text="This is an X filled label", bg="green", fg="black")
labelTwo.pack(fill=X)
labelThree = Label(root, text="This is a Y filled label", bg="blue", fg="white")
labelThree.pack(side=TOP, fill=Y)


# Frames
topFrame = Frame(root)      # Top invisible section
topFrame.pack()

bottomFrame = Frame(root)   # Bottom invisible section
bottomFrame.pack(side=BOTTOM)

# Widget
button1 = Button(bottomFrame, text="Button 1", fg="red")        # Params = Where, Text, Forground
button2 = Button(bottomFrame, text="Button 2", fg="blue")
button3 = Button(bottomFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="black")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop() # Display the scren
