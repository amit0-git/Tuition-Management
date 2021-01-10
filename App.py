#Tuition Management App
#Author:-Amit Verma
#Teacher:-Ramesh Bhatt
#Date=23-11-2020

try:
    import tkinter as tk
    from tkinter import ttk
    from PIL import ImageTk, Image
    import threading

except ImportError as r:
    tk.messagebox.showerror("Error!",r)
    print('Module not found!',r)


start1=tk.Tk()
start1.resizable(False,False)

start1.geometry("+350+100")
start1.overrideredirect(1) #remove the window border

start1.lift()


start1.title("Tuition Management")
class First(tk.Frame):
    """Frame for first Page"""
    def __init__(self, parent, *args, **kwargs):        
        super().__init__(parent, *args, **kwargs)

class About(tk.Frame):
    """Frame for About developer"""
    def __init__(self, parent, *args, **kwargs):        
        super().__init__(parent, *args, **kwargs)

class Text_Intro:
    """Text Animation Class"""
    def __init__(self):
        self.y_cord=135
        self.x_cord=350
        self.change_time=3000

        self.q1="It enables a private tutor or any coaching class to maintain a list of students enrolled, track their fees payment."
        self.q2="It helps keep track students that have due fees records."
        self.q3="Add or remove fees in very simple steps."

    def chnge(self):
        canvas.delete('abcd')
        canvas.create_text(self.x_cord,self.y_cord,text=self.q1,justify=tk.CENTER,font=('Arial',15),width=470,tags="abcd",fill="#ff1744")
        a.after(self.change_time,self.chnge1)

    def chnge1(self):
        canvas.delete('abcd')
        canvas.create_text(self.x_cord,self.y_cord,text=self.q2,justify=tk.CENTER,font=('Arial',15),width=470,tags="abcd",fill="#ff1744")
        a.after(self.change_time,self.chnge2)

    def chnge2(self):
        canvas.delete('abcd')
        canvas.create_text(self.x_cord,self.y_cord,text=self.q3,justify=tk.CENTER,font=('Arial',15),width=470,tags="abcd",fill="#ff1744")
        a.after(self.change_time,self.chnge)

frim=Image.open('images/fogg-welcome-2.png')
frim=frim.resize((730, 490), Image.ANTIALIAS)
frimg=ImageTk.PhotoImage(frim)

stim=Image.open('images/power.png')
stim=stim.resize((40, 20), Image.ANTIALIAS)
stimg=ImageTk.PhotoImage(stim)
def main():
    global a
    a=First(start1)
    a.pack()
    global canvas
    canvas=tk.Canvas(a,height=490,width=730)
    canvas.pack()
    canvas.create_image(365,245,image=frimg)
    canvas.create_rectangle(0, 0, 800, 90, fill="#00b0ff",width=0)
    canvas.create_text(370,45,text="TUITION-MANAGEMENT",font=('Arial',30),anchor=tk.CENTER,justify=tk.CENTER,fill="white")
    dd=Text_Intro()
    txxt="Tuition Management made easy."
    canvas.create_text(350,120,text=txxt,font=('Arial',15),anchor=tk.CENTER,justify=tk.LEFT,width=470,tags="abcd",fill="#ff1744")
    a.after(3000,dd.chnge)
    def open_Tuition():
        
        start1.destroy()
        import Tuition
    but=ttk.Button(canvas,image=stimg,command=open_Tuition)
    but.place(x=340,y=248)
    time=300
    x=430
    y=470
    font_size=15
    w=200
    def h1():
        canvas.delete("avc")
        canvas.create_text(x,y,text='Am|',tags="avc",font=('Arial',font_size),width=w,fill="red")
        a.after(time,h2)

    def h2():
        canvas.delete("avc")
        canvas.create_text(x,y,text='Ami|',tags="avc",font=('Arial',font_size),width=w,fill="red")
        a.after(time,h3)
    def h3():
        canvas.delete("avc")
        canvas.create_text(x,y,text='Amit|',tags="avc",font=('Arial',font_size),width=w,fill="red")
        a.after(time,h4)
    def h4():
        canvas.delete("avc")
        canvas.create_text(x,y,text='Amit |',tags="avc",font=('Arial',font_size),width=w,fill="red")
        a.after(time,h5)
    def h5():
        canvas.delete("avc")
        canvas.create_text(x,y,text='Amit V|',tags="avc",font=('Arial',font_size),width=w,fill="red")
        a.after(time,h6)
    def h6():
        canvas.delete("avc")
        canvas.create_text(x,y,text='Amit Ve|',tags="avc",font=('Arial',font_size),width=w,fill="red")
        a.after(time,h7)
    def h7():
        canvas.delete("avc")
        canvas.create_text(x,y,text='Amit Ver|',tags="avc",font=('Arial',font_size),width=w,fill="red")
        a.after(time,h8)
    def h8():
        canvas.delete("avc")
        canvas.create_text(x,y,text='Amit Verm|',tags="avc",font=('Arial',font_size),width=w,fill="red")
        a.after(time,h9)
    def h9():
        canvas.delete("avc")
        canvas.create_text(x,y,text='Amit Verma|',tags="avc",font=('Arial',font_size),width=w,fill="red")
        a.after(time,start2)


    canvas.create_text(280,470,text="Developed By:-",font=('Arial',15),anchor=tk.CENTER,justify=tk.LEFT,width=470,tags="avcd",fill="#1a237e")
    def close_win():
        start1.destroy()

    cl_but=ttk.Button(canvas,text="Exit",command=close_win)
    cl_but.place(x=560,y=460)
    
    def start2():
        a.after(300,h1)
    t1=threading.Thread(target=start2)
    t1.start()
    ab_but=ttk.Button(canvas,text="Me",command=about_win)
    ab_but.place(x=640,y=460)

abim=Image.open('images/About Me.png')

abimg=ImageTk.PhotoImage(abim)
def about_win():
    a.destroy()
    canvas.destroy()
    b=About(start1)#frame for about developer
    canvas1=tk.Canvas(b,width=730,height=490)#canvas for about developer
    b.pack()
    canvas1.pack()
    canvas1.create_image(365,245,image=abimg)
    canvas1.render=abimg
    def cl():
        """Function to destroy the about developer frame"""
        b.destroy()
        main()#open main function
    cl1_but=ttk.Button(canvas1,text="Exit",command=cl)
    cl1_but.place(x=630,y=460)

if __name__=="__main__":
    main()
    start1.mainloop()
