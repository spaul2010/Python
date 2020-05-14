# ------------------------------------------------------------------------------
#    Python GUI Programming - Usage of Grid
# ------------------------------------------------------------------------------
import tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry('640x500')


# ------------------------------------------------------------------------------
#    Creating Label & Canvas
# ------------------------------------------------------------------------------
label = tkinter.Label(mainWindow, text="Hello World!")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')


# ------------------------------------------------------------------------------
#    Adding Button
# ------------------------------------------------------------------------------
button1 = tkinter.Button(mainWindow, text='button1')
button2 = tkinter.Button(mainWindow, text='button2')
button3 = tkinter.Button(mainWindow, text='button3')

button1.grid(row=0, column=3)
button2.grid(row=1, column=3)
button3.grid(row=2, column=3)


# ------------------------------------------------------------------------------
#    Configure the Columns
# ------------------------------------------------------------------------------
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)


mainWindow.mainloop()


