"""
Carson Pemble
8/26/2020
Python GUI
"""
from tkinter import *





### Functions ###
def printName():
    print("Carson Pemble")

def printNameEvent(event):
    print("Carson Pemble from Event")

def leftClick(event):
    print("Left Clicked")

def midClick(event):
    print("Middle Clicked")

def rightClick(event):
    print("Right Clicked")

def close_window():
    root.destroy()


### tkinter Start ###
root = Tk()     # start the window


### Frames ###
topFrame = Frame(root, width=600, height=500)      # Top invisible section
topFrame.pack(side=TOP)

bottomFrame = Frame(root, width=600, height=500)   # Bottom invisible section
bottomFrame.pack(side=BOTTOM)


### Labels ###
theLabel = Label(topFrame, text="This is Carson's First Python GUI", bg="white", fg="black")
#theLabel.pack()
theLabel.grid(row=0, column=0, columnspan=2)      # more accurate placement

# labelTwo = Label(root, text="This is an X filled label", bg="green", fg="black")
# labelTwo.pack(fill=X)
#
# labelThree = Label(root, text="This is a Y filled label", bg="blue", fg="white")
# labelThree.pack(side=TOP, fill=Y)

labelName = Label(topFrame, text="Name")
labelPassword = Label(topFrame, text="Password")

labelName.grid(row=1, sticky=E)
labelPassword.grid(row=2, sticky=E)     # sticky=E is Right aligned




### Widget ###
button1 = Button(bottomFrame, text="Button 1", fg="red", command=printName)        # Params = Where, Text, Forground, function
button2 = Button(bottomFrame, text="Button 2", fg="blue")
button2.bind("<Button-1>", printNameEvent)                      # Another option for button clicks

button3 = Button(bottomFrame, text="Button 3", fg="green")
button3.bind("<Button-1>", leftClick)
button3.bind("<Button-2>", midClick)
button3.bind("<Button-3>", rightClick)

button4 = Button(bottomFrame, text="Button 4", fg="black", command=close_window)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)


entryName = Entry(topFrame)
entryPassword = Entry(topFrame)

check = Checkbutton(topFrame, text="Keep me logged in")
check.grid(columnspan=2)




entryName.grid(row=1, column=1)
entryPassword.grid(row=2, column=1)

root.mainloop() # Display the scren
