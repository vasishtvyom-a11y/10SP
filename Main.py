from tkinter import*
root=Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top=Toplevel()
    top.geometry("180x100")
    root.title("999999999")
    l2=Label(top,text="this is top level")
    l2.pack()
    top.mainloop()
l1=Label(root,text="This is root window")
btn=Button(root,text="click here to open top window",command=topwin)
l1.pack()
btn.pack()
root.mainloop()
