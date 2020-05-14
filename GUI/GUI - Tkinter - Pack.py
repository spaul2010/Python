# ------------------------------------------------------------------------------
#    Python GUI Programming - Usage of Pack
# ------------------------------------------------------------------------------
import tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Hello World")

# ------------------------------------------------------------------------------
#    Creating Label & Canvas
# ------------------------------------------------------------------------------
label = tkinter.Label(mainWindow, text="Hello World!")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')


# ------------------------------------------------------------------------------
#    Adding Button
# ------------------------------------------------------------------------------
button1 = tkinter.Button(mainWindow, text='button1')
button2 = tkinter.Button(mainWindow, text='button2')
button3 = tkinter.Button(mainWindow, text='button3')

button1.pack(side='top', anchor='n')
button2.pack(side='top', anchor='s')
button3.pack(side='top', anchor='e')

mainWindow.mainloop()
