from tkinter import *
win=Tk()
win.title("Current Bill")
win.geometry("600x320")
win.resizable(0,0)
photo = PhotoImage(file = "logo.png")
win.iconphoto(False, photo)

fr=Frame(win,bg="white")
fr.place(x=0,y=0,width=299,height=400)
img=PhotoImage(file="win2.png")
label=Label(fr,image=img).place(x=000,y=000)

def billam():
    x=int(p.get())
    y=int(a.get())
    t=x-y;
    if(t<=50):
        uc=1;
        bill=t*1;
    elif(t<=100):
        uc=2;
        bill=50+((t-50)*2);
    elif(t<=150):
        uc=3;
        bill=50+100+((t-100)*3);
    elif(t<=200):
        uc=4;
        bill=50+100+150+((t-150)*4);
    else:
        uc=5;
        bill=500+((t-200)*5);
    print(bill,"rs")  
    tot.set(bill)            

frame=Frame(win,bg="#003b4f")
frame.place(x=300,y=00,width=300,height=400)
# img2=PhotoImage(file="APDCL.png")
label3=Label(frame,text="CURRENT BILL AMOUNT",font=("times roman",15),fg="white",bg="#003b4f").place(x=30,y=30)
l2=Label(frame,text="PRESENT UNITS   : ",font=("arial",10,"bold"),fg="white",bg="#003b4f").place(x=10,y=90)
l1=Label(frame,text="PREVIOUS UNITS    : ",font=("arial",10,"bold"),fg="white",bg="#003b4f").place(x=10,y=140)
p=StringVar()
e1=Entry(frame,width=23,relief="solid",textvariable=p).place(x=140,y=90)
a=StringVar()
e1=Entry(frame,width=23,relief="solid",textvariable=a).place(x=140,y=140)
l3=Label(frame,text="-------------------------------------------------------------",font=("arial",18,"bold"),fg="white",bg="#003b4f").place(x=0,y=210)
l3=Label(frame,text="Total Amount : ",font=("arial",18,"bold"),fg="white",bg="#003b4f").place(x=0,y=250)
tot=StringVar()
e2=Entry(frame,textvariable=tot,font=("arial",20,"bold"),relief="solid",fg="red",bg="#003b4f").place(height=30,x=180,width=100,y=250)

b1=Button(frame,text="BILL AMOUNT",command=billam).place(x=170,y=180)



win.mainloop()
