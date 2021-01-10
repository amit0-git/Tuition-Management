try:

    import tkinter as tk
    from tkinter import ttk
    from PIL import ImageTk,Image
    import mysql.connector as mysql

except ImportError as r:
    tk.messagebox.showerror("Error!",r)
    print('Module not found!',r)


tree=None
data=None
class Student_Info(tk.Frame):
    """Class to show details of student in treeview widget"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        serim=Image.open('images/seo.png')
        serimg=ImageTk.PhotoImage(serim)

        

       
        self.syms=['quoteleft','Tab','Caps_Lock','Shift_L','Shift_R','Control_L','Control_R','Alt_L','Alt_R','Return','Escape','Delete','Left','Right']
        self.data=''

        name=ttk.Label(self,text="Search Records By Name",font=("TkDefaultFont", 14),image=serimg,compound=tk.LEFT)
        name.render=serimg
        name.grid(row=0,column=0,ipady=10)
        self.namee=ttk.Entry(self)
        self.namee.grid(row=0,column=1,sticky=tk.W,ipadx=20)
  

      

        container = tk.Frame(self,height=600)
        container.grid(row=1,column=0,columnspan=2)


        scrollbar=ttk.Scrollbar(container)
        scrollbar.grid(row=2,column=1,sticky=tk.NS,columnspan=2)
        global tree
        tree=ttk.Treeview(container,columns=(1,2,3,4,5,6,7,8),show="headings",yscrollcommand=scrollbar.set)
        scrollbar.config(command=tree.yview)

        tree.column(1,anchor=tk.CENTER,width=50)
        tree.column(2,anchor=tk.CENTER,width=120)
        tree.column(3,anchor=tk.CENTER,width=50)
        tree.column(4,anchor=tk.CENTER,width=80)
        tree.column(5,anchor=tk.CENTER,width=200)
        tree.column(6,anchor=tk.CENTER,width=170)
        tree.column(7,anchor=tk.CENTER,width=200)
        tree.column(8,anchor=tk.CENTER,width=200)

        tree.heading(1,text="Roll No")
        
        tree.heading(2,text="Name",)
       
        tree.heading(3,text="Class")
        
        tree.heading(4,text="Section")
        
        tree.heading(5,text="School")
        
        tree.heading(6,text="Address")
        
        tree.heading(7,text="Father")
    
        tree.heading(8,text="Father No")
      
        tree.grid(row=2,column=0,pady=10,padx=10)
        self.insert_all()

        self.namee.bind("<KeyPress>",self.search)

    def insert_all(self):
        conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
        c=conn.cursor()
        c.execute("SELECT rollno,name,class,section,school,address,father,father_no FROM student")
        rec1=c.fetchall()
        if rec1:
            for a in rec1:
                tree.insert(parent='',index='end',values=(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]))

        c.close()
        conn.close()


    def student_Count(self):

        def class11_count():
            conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
            c=conn.cursor()
            c.execute('SELECT COUNT(*) FROM student WHERE class=11')
            cl11rec=c.fetchone()
            c.close()
            conn.close()
            if cl11rec:
                return cl11rec[0]
            else:
                return 0

        def class12_count():
            conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
            c=conn.cursor()
            c.execute('SELECT COUNT(*) FROM student WHERE class=12')
            cl12rec=c.fetchone()
            c.close()
            conn.close()
            if cl12rec:
                return cl12rec[0]
            else:
                return 0

        def class9_count():
            conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
            c=conn.cursor()
            c.execute('SELECT COUNT(*) FROM student WHERE class=9')
            cl9rec=c.fetchone()
            c.close()
            conn.close()
            if cl9rec:
                return cl9rec[0]
            else:
                return 0

        def class10_count():
            conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
            c=conn.cursor()
            c.execute('SELECT COUNT(*) FROM student WHERE class=10')
            cl10rec=c.fetchone()
            c.close()
            conn.close()
            if cl10rec:
                return cl10rec[0]
            else:
                return 0

        stc=tk.Canvas(self,width=800)
        stc.grid(row=3,column=0)

        stc.create_rectangle(20, 0, 800, 90, fill="blue",width=0)



        stc.create_text(400,40,text="Total Students",font=('Arial',25),anchor=tk.CENTER,justify=tk.CENTER,fill="white")

        stc.create_rectangle(20, 120, 200, 210, fill="#00b0ff",width=0)
        stc.create_text(100,140,text="Class 9",font=('Arial',20),anchor=tk.CENTER,justify=tk.CENTER,fill="white")
        stc.create_text(100,180,text=class9_count(),font=('Arial',20),anchor=tk.CENTER,justify=tk.CENTER,fill="white")

        stc.create_rectangle(220, 120, 400, 210, fill="red",width=0)
        stc.create_text(300,140,text="Class 10",font=('Arial',20),anchor=tk.CENTER,justify=tk.CENTER,fill="white")
        stc.create_text(300,180,text=class10_count(),font=('Arial',20),anchor=tk.CENTER,justify=tk.CENTER,fill="white")

        stc.create_rectangle(420, 120, 600, 210, fill="#00b0ff",width=0)
        stc.create_text(500,140,text="Class 11",font=('Arial',20),anchor=tk.CENTER,justify=tk.CENTER,fill="white")
        stc.create_text(500,180,text=class11_count(),font=('Arial',20),anchor=tk.CENTER,justify=tk.CENTER,fill="white")

        stc.create_rectangle(620, 120, 800, 210, fill="red",width=0)
        stc.create_text(700,140,text="Class 12",font=('Arial',20),anchor=tk.CENTER,justify=tk.CENTER,fill="white")
        stc.create_text(700,180,text=class12_count(),font=('Arial',20),anchor=tk.CENTER,justify=tk.CENTER,fill="white")



        




    
    def search(self,inp):
        """Function to automatically search when any key pressed"""
        global data
        tree.delete(*tree.get_children())
        #if entry box is already empty and pressed  backspace then the functionality will not work check this
    
        if inp.keysym=="space":
            self.data=self.data+" "
        elif inp.keysym=="BackSpace":
            self.data=self.data[:-1]
        elif inp.keysym not in self.syms:
            
            self.data=self.data+str(inp.keysym)
       
            

        else:
            pass

        if self.data=="all":
            self.insert_all()
        conn = mysql.connect(host='localhost', database='tuition', user='app_admin', password='app_admin@12345')
        c = conn.cursor()
        data1=self.data+"*"
        try:
            c.execute("SELECT rollno,name,class,section,school,address,father,father_no FROM student WHERE MATCH(name,father) AGAINST('"+data1+"' IN BOOLEAN MODE)")
            rec=c.fetchall()
            
            if rec:
                tree.delete(*tree.get_children())
             
                
        
                for a in rec:
                    tree.insert(parent='',index='end',values=(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]))
                
        except Exception as e:
            print("Error!",e)



