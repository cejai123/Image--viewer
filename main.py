import tkinter 
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
root = Tk()
root.title("Image checker")
root.geometry("400x500")
root.resizable(False, False)
def getpicture():
    filename = filedialog.askopenfilename(title="Select file ")
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    f.configure(image=img)
    f.image = img
f = Label(root)
f.pack()
frame1 = Frame()
frame1.pack()
button1 = Button(text="Select File", command=getpicture, width=20)
button1.pack(side=BOTTOM)

root.mainloop()