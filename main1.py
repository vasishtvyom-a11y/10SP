from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Denomination")
root.geometry("650x450")
root.configure(bg="lightblue")

label1=Label(root,text="Welcome to denomination calculator",bg="lightblue")
label1.place(relx=0.5,rely=340,anchor=CENTER)

def msg():
    Msgbox=messagebox.showinfo("Alert","Do you want to calculate denomination?")
    if Msgbox=="ok":
        topwin()
button1=Button(root,text="Start",command=msg,bg="brown",fg="white")
button1.place(x=260,y=360)

def topwin():
    top=Toplevel()
    top.title("Denomination cal")
    top.configure(bg="lightgrey")
    top.geometry("600x350+50+50")
    label2=Label(top,text="Enter amount:",bg="lightgrey")
    entry=Entry(top)
    label3=Label(top,text="Notes in denomination are:",bg="lightgrey")
    l1=Label(top,text="2000",bg="light grey")
    l2=Label(top,text="500",bg="light grey")
    l3=Label(top,text="100",bg="light grey")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    def cal():
        try:
            amount=int(entry.get())
            note2000=amount//2000
            amount%=2000
            note500=amount//500
            amount%=500
            note100=amount//100
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))
        except ValueError:
            messagebox.showinfo("Error","Please Enter a valid number")
    btn=Button(top,text="Calculate",command=cal,bg="brown",fg="white")
    label2.place(x=230,y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    label3.place(x=140,y=170)
    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)
    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)
    top.mainloop()
root.mainloop()