#Tuition Management App
#Author:-Amit Verma
#Email:- root.avanti@gmail.com
#Date=23-11-2020

try:
    import tkinter as tk
    from tkinter import ttk
    from PIL import ImageTk,Image
    import mysql.connector as mysql
    from tkinter import messagebox
    from Std_Info import Student_Info
    import datetime
    import time
    import threading
    import os
    import sys
    from fpdf import FPDF
 

except ImportError as r:
    tk.messagebox.showerror("Error!",r)
    print('Module not found!',r)



class Teacher_Register(tk.Frame):
    """Teacher Registration frame for registering the teachers"""
    
    def __init__(self, parent, *args, **kwargs):        
        super().__init__(parent, *args, **kwargs)
        font_size=14
        
        saveimg=Image.open('images/floppy-disk.png')
        save_img=ImageTk.PhotoImage(saveimg)
     
        load1 = Image.open("images/man-icon.png")
        render_load1 = ImageTk.PhotoImage(load1)

        load2 = Image.open("images/App-password-icon (1).png")
        render_load2 = ImageTk.PhotoImage(load2)

        load3 = Image.open("images/42496-school-icon (1).png")
        render_load3 = ImageTk.PhotoImage(load3)

        regisimg=Image.open('images/register.jpg')
        regisimg = regisimg.resize((400, 180), Image.ANTIALIAS)
        regis_img=ImageTk.PhotoImage(regisimg)
        

        regis = ttk.Label(self,image=regis_img)
        regis.render=regis_img 
        
        

        inst_l = ttk.Label(self, text="Institute Name",image=render_load3,compound=tk.LEFT,font=("TkDefaultFont", font_size))
        inst_l.image=render_load3 
        username_l = ttk.Label(self, text="Username",image=render_load1,compound=tk.LEFT,font=("TkDefaultFont", font_size))
        username_l.image =render_load1
        password_l = ttk.Label(self, text="Password",image=render_load2,compound=tk.LEFT,font=("TkDefaultFont", font_size))
        password_l.image=render_load2 
       

        self.inst = ttk.Entry(self,width=20)
        self.username = ttk.Entry(self)
        self.password = ttk.Entry(self,show="*")

        self.save_button = ttk.Button(self, text="Save",image=save_img,compound=tk.LEFT,command=self.save_teacher)
        self.save_button.render=save_img
      
        
        regis.grid(row=0, column=0,columnspan=2,pady=20) 
        inst_l.grid(row=1, column=0,sticky=tk.W)       
        username_l.grid(row=2, column=0,sticky=tk.W)               
        password_l.grid(row=3, column=0,sticky=tk.W)

        self.inst.grid(row=1, column=1,ipadx=20,padx=10)       
        self.username.grid(row=2, column=1,ipadx=20,padx=10)               
        self.password.grid(row=3, column=1,ipadx=20,padx=10)

        self.save_button.grid(row=4, column=0)

        

  
      
       
        

    def save_teacher(self):
        """Function to save teacher details"""
        conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
        c=conn.cursor()
    
        if self.username.get() == "" or self.password.get()=="":
            tk.messagebox.showerror("Error!","Fill username and password!")
        else:
      
            try:
                c.execute("""
                CREATE TABLE IF NOT EXISTS teacher
                ( institute VARCHAR(40) NOT NULL , 
                username VARCHAR(20) NOT NULL , 
                password VARCHAR(20) NOT NULL , 
                PRIMARY KEY (username)) ENGINE = InnoDB;""")

                c.execute("INSERT INTO teacher VALUES(%s,%s,%s)",(self.inst.get(),self.username.get(),self.password.get()))
                tk.messagebox.showinfo("Success!","Record Successfully inserted!")
                conn.commit()
                c.close()
                conn.close()
            except:
                tk.messagebox.showwarning("Warning!","Username already taken!")
                c.close()
                conn.close()



        

    
        

class Teacher_login(tk.Frame):

    """Frame for teacher login window"""
    def __init__(self, parent, *args, **kwargs):        
        super().__init__(parent, *args, **kwargs)
        usr_img=Image.open('images/user (2).png')
        pass_img=Image.open('images/key (1).png')
        banner_img=Image.open('images/login.png')
        banner_img=banner_img.resize((300, 120), Image.ANTIALIAS)
        usr_img_ren=ImageTk.PhotoImage(usr_img)
        pas_img_ren=ImageTk.PhotoImage(pass_img)
        banner_img_ren=ImageTk.PhotoImage(banner_img)

        banner=ttk.Label(self,image=banner_img_ren)
        banner.grid(row=0,column=0,columnspan=2)
        banner.render=banner_img_ren

        
        usrlt=ttk.Label(self,text="Username",image=usr_img_ren,compound=tk.LEFT,font=("TkDefaultFont", 14))
        usrlt.grid(row=1,column=0)   
        usrlt.render=usr_img_ren
        passlt=ttk.Label(self,text="Password",image=pas_img_ren,compound=tk.LEFT,font=("TkDefaultFont",14))
        passlt.grid(row=2,column=0)
        passlt.render=pas_img_ren
        

        self.usrl=ttk.Entry(self)
        self.passl=ttk.Entry(self,show="*")
      
        self.usrl.grid(row=1,column=1)
        self.passl.grid(row=2,column=1)

      

        

    

            

class Student_Edit_Ask(tk.Frame):

    """Frame to ask for roll no to edit student details and fees"""
    def __init__(self, parent, *args, **kwargs):        
        super().__init__(parent, *args, **kwargs)
        bannerimg=Image.open('images/undraw_Checklist__re_2w7v.png')
        bannerimg = bannerimg.resize((360, 300), Image.ANTIALIAS)
        bannerimgr=ImageTk.PhotoImage(bannerimg)
        bannerl=ttk.Label(self,image=bannerimgr)
        bannerl.grid(row=0,column=0,columnspan=2)
        bannerl.render=bannerimgr
        rolledit=ttk.Label(self,text="Enter Roll No. for Editing",font=("TkDefaultFont", 18))
        rolledit.grid(row=1,column=0,columnspan=2)

        roll=ttk.Label(self,text="Roll No",font=("TkDefaultFont", 14))
        self.rolle=ttk.Entry(self)

        roll.grid(row=2,column=0,pady=20)
        self.rolle.grid(row=2,column=1,ipadx=40,pady=20)

    
class Student_Registeration_Image(tk.Frame):
    """ Frame that contains Bokks Image In student registration window """ 
    def __init__(self, parent, *args, **kwargs):        
        super().__init__(parent, *args, **kwargs)
        
            
class Student_Registeration_Image_Main(tk.Frame):
    """ Main Frame that contains Student Registration Frame and Student Registration Main Frame """
    def __init__(self, parent, *args, **kwargs):        
        super().__init__(parent, *args, **kwargs)            

            

        


class Student_Registeration(tk.Frame):
    """Frame for student registeration window"""
    def __init__(self, parent, *args, **kwargs):        
        super().__init__(parent, *args, **kwargs)
        
        
        font_size=13
        

        #image for labels start
        roll_img=Image.open('images/ID-2-icon.png')
        render_roll_img=ImageTk.PhotoImage(roll_img)

        name_img=Image.open('images/man-icon.png')
        render_name=ImageTk.PhotoImage(name_img)

        class_img=Image.open('images/Science-Class-icon.png')
        render_class=ImageTk.PhotoImage(class_img)

        section_img=Image.open('images/Science-Classroom-icon.png')
        render_section=ImageTk.PhotoImage(section_img)

        school_img=Image.open('images/school-bus-icon.png')
        render_school=ImageTk.PhotoImage(school_img)

        address_img=Image.open('images/42496-school-icon (1).png')
        render_address=ImageTk.PhotoImage(address_img)

        father_img=Image.open('images/Office-Customer.png')
        render_father=ImageTk.PhotoImage(father_img)

        father_no_img=Image.open('images/phone-icon.png')
        render_father_no=ImageTk.PhotoImage(father_no_img)

        mobile_img=Image.open('images/WhatsApp-icon.png')
        render_mobile=ImageTk.PhotoImage(mobile_img)

        doj_img=Image.open('images/Calendar-icon.png')
        render_doj=ImageTk.PhotoImage(doj_img)

        reg_img=Image.open('images/regis1.png')
        reg_img = reg_img.resize((340, 140), Image.ANTIALIAS)
        render_reg=ImageTk.PhotoImage(reg_img)

        button_img=Image.open('images/save_i.jpg')
        button_img = button_img.resize((45, 25), Image.ANTIALIAS)
        render_button=ImageTk.PhotoImage(button_img)

        #image for labels end

        #registration image
        reg_l= ttk.Label(self,image=render_reg)
        reg_l.image=render_reg
        reg_l.grid(row=0,column=0,columnspan=2)

        # student registration labels
        roll_l= ttk.Label(self,text="Roll No",image=render_roll_img,compound=tk.LEFT,font=("TkDefaultFont", font_size))
        roll_l.image=render_roll_img
        name_l= ttk.Label(self,text="Name *",image=render_name,compound=tk.LEFT,font=("TkDefaultFont", font_size))
        name_l.image=render_name
        class_l= ttk.Label(self,text="Class *",image=render_class,compound=tk.LEFT,font=("TkDefaultFont", font_size))
        class_l.image=render_class
        section_l= ttk.Label(self,text="Section",image=render_section,compound=tk.LEFT,font=("TkDefaultFont", font_size))
        section_l.image=render_section
        school_l= ttk.Label(self,text="School *",image=render_school,compound=tk.LEFT,font=("TkDefaultFont", font_size))
        school_l.image=render_school
        address_l= ttk.Label(self,text="Address *",image=render_address,compound=tk.LEFT,font=("TkDefaultFont", font_size))
        address_l.image=render_address
        father_l= ttk.Label(self,text="Father",image=render_father,compound=tk.LEFT,font=("TkDefaultFont", font_size))
        father_l.image=render_father
        father_no_l= ttk.Label(self,text="Father's No. *",image=render_father_no,compound=tk.LEFT,font=("TkDefaultFont", font_size))
        father_no_l.image=render_father_no
        mobile_l= ttk.Label(self,text="Mobile *",image=render_mobile,compound=tk.LEFT,font=("TkDefaultFont", font_size))
        mobile_l.image=render_mobile
        doj_l= ttk.Label(self,text="DOJ *",image=render_doj,compound=tk.LEFT,font=("TkDefaultFont", font_size))
        doj_l.image=render_doj

        
        roll_l.grid(row=1,column=0,padx=10)
       
        name_l.grid(row=2,column=0,padx=10)
        class_l.grid(row=3,column=0,padx=10)
        section_l.grid(row=4,column=0,padx=10)
        school_l.grid(row=5,column=0,padx=10)
        address_l.grid(row=6,column=0,padx=10)
        father_l.grid(row=7,column=0,padx=10)
        father_no_l.grid(row=8,column=0,padx=10)
        mobile_l.grid(row=9,column=0,padx=10)
        doj_l.grid(row=10,column=0,padx=10)

        #student registration entry widgets
        self.roll_e=  ttk.Label(self,text="Auto Assigned",font=("TkDefaultFont", font_size))
        self.name_e= ttk.Entry(self)
        self.class_e= ttk.Entry(self)
        self.section_e= ttk.Entry(self)
        self.school_e= ttk.Entry(self)
        self.address_e= ttk.Entry(self)
        self.father_e= ttk.Entry(self)
        self.father_no_e= ttk.Entry(self)
        self.mobile_e= ttk.Entry(self)
    
        self.doj_e= ttk.Entry(self)
      


        self.roll_e.grid(row=1,column=1,ipadx=30,padx=10)
        self.name_e.grid(row=2,column=1,ipadx=30,padx=10)
        self.class_e.grid(row=3,column=1,ipadx=30,padx=10)
        self.section_e.grid(row=4,column=1,ipadx=30,padx=10)
        self.school_e.grid(row=5,column=1,ipadx=30,padx=10)
        self.address_e.grid(row=6,column=1,ipadx=30,padx=10)
        self.father_e.grid(row=7,column=1,ipadx=30,padx=10)
        self.father_no_e.grid(row=8,column=1,ipadx=30,padx=10)
        self.mobile_e.grid(row=9,column=1,ipadx=30,padx=10)
        self.doj_e.grid(row=10,column=1,ipadx=30,padx=10)

        # button to register the students
        self.save=ttk.Button(self,text="Save",image=render_button,compound=tk.LEFT,command=self.save_student)
        self.save.image=render_button
        self.save.grid(row=11,column=0,columnspan=2)

       
    def clear_student_fields(self):
        self.name_e.delete(0,tk.END)
        self.class_e.delete(0,tk.END)
        self.section_e.delete(0,tk.END)
        self.school_e.delete(0,tk.END)
        self.address_e.delete(0,tk.END)
        self.father_e.delete(0,tk.END)
        self.father_no_e.delete(0,tk.END)
        self.mobile_e.delete(0,tk.END)
        self.doj_e.delete(0,tk.END)

   

 
    def save_student(self):
        """Function to save student"""

        datever=Date_Verify()
        if self.name_e.get()=="" or self.class_e.get()=="" or self.school_e.get()=="" or self.address_e.get()=="" or self.father_no_e.get()=="" or self.mobile_e.get()=="" or self.doj_e.get()=="":
            tk.messagebox.showerror("Error!","It is compulsory to fill mandatory details!")
        
        elif self.mobile_e.get().isalpha() and self.father_no_e.get().isalpha():
            tk.messagebox.showerror("Error!","Check Phone Number fields!")
        
        elif not datever.isValid(self.doj_e.get()):
            tk.messagebox.showerror("Error!","Date format(yyyy-mm-dd)")

        
        else:

            try:
                conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
                c=conn.cursor()
                c.execute("INSERT INTO student(name,class,section,school,address,father,father_no,mobile,doj) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.name_e.get(),self.class_e.get(),self.section_e.get(),self.school_e.get(),self.address_e.get(),self.father_e.get(),self.father_no_e.get(),self.mobile_e.get(),self.doj_e.get()))
                tk.messagebox.showinfo("Success!","Record Successfully inserted!")
                conn.commit()
                c.close()
                conn.close()
                self.clear_student_fields()

            except Exception as e:
                tk.messagebox.showerror("Error!",e)

        
        
class Student_Edit(Student_Registeration):
    """Frame to open student edit window inherited from student registeration"""
    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)
        

        conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
        c=conn.cursor()
        
        #c.execute("INSERT INTO teacher VALUES('"+self.inst.get()+"','"+self.username.get()+"','"+self.password.get()+"')")
        c.execute("SELECT * FROM student WHERE rollno={}".format(asas.rolle.get()))
        rec=c.fetchall()
        
        rollu=rec[0][0]
        nameu=rec[0][1]
        classu=rec[0][2]
        sectionu=rec[0][3]
        schoolu=rec[0][4]
        addressu=rec[0][5]
        fatheru=rec[0][6]
        fathernou=rec[0][7]
        mobileu=rec[0][8]
        doju=rec[0][9]

        self.roll_e.configure(text=rollu)
        self.name_e.insert(0,nameu)
        self.class_e.insert(0,classu)
        self.section_e.insert(0,sectionu)
        self.school_e.insert(0,schoolu)
        self.address_e.insert(0,addressu)
        self.father_e.insert(0,fatheru)
        self.father_no_e.insert(0,fathernou)
        self.mobile_e.insert(0,mobileu)
        self.doj_e.insert(0,doju)

        c.close()
        conn.close()
        

       

    def save_student(self):
        """Overide save_student method to update student details""" 
        if self.name_e.get()=="" or self.class_e.get()=="" or self.school_e.get()=="" or self.address_e.get()=="" or self.father_no_e.get()=="" or self.mobile_e.get()=="" or self.doj_e.get()=="":
            tk.messagebox.showerror("Error!","It is compulsory to fill mandatory details!")
        
        elif self.mobile_e.get().isalpha() and self.father_no_e.get().isalpha():
            tk.messagebox.showerror("Error!","Check Phone Number fields!")

        else:
            try:

                conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
                c=conn.cursor()
                c.execute("UPDATE student SET name=%s,class=%s,section=%s,school=%s,address=%s,father=%s,father_no=%s,mobile=%s,doj=%s WHERE rollno=%s",(self.name_e.get(),self.class_e.get(),self.section_e.get(),self.school_e.get(),self.address_e.get(),self.father_e.get(),self.father_no_e.get(),self.mobile_e.get(),self.doj_e.get(),asas.rolle.get()))
                #c.execute("UPDATE {} SET name=self.name_e.get() class=self.class_e.get() ,section=self.section_e.get(),school=self.school_e.get(), address=self.address_e.get(), father=self.father_e.get(),father_no=self.father_no_e.get(),mobile=self.mobile_e.get(),doj=self.doj_e.get() WHERE rollno='"+asas.rolle.get()+"' ")
                tk.messagebox.showinfo("Success!","Record Successfully Updated!")
                conn.commit()
                c.close()
                conn.close()

            except Exception as e:
                tk.messagebox.showerror("Error!",e)


#####################################################################################################
##                                      Fees Window Frames                                         ##
feesin=None
class Fees_Main_Frame(tk.Frame):
    """Main Fees Frame to hold Fees frame,Fees Info Frame, Del_Fees Frame """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Date_Verify:
    """Common class to verify date"""

    def isValid(self,date1):
        """Funtion to return True if date1 is valid"""
        try:
            if datetime.datetime.strptime(date1,'%Y-%m-%d'):
                return True
            else:
                return False
        except ValueError:
            return False
       

class Fees(tk.Frame):
    """Frame to show basic details of student for submitting fees"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        dateimg=Image.open('images/Calendar-icon.png')
        rollimg=Image.open('images/ID-2-icon.png')
        feesimg=Image.open('images/money-bag.png')
        nameim=Image.open('images/id-card.png')
        classim=Image.open('images/online-class.png')
        secim=Image.open('images/videoconference.png')
    

        addimg=Image.open('images/add.png')
        addimgr=ImageTk.PhotoImage(addimg)
        
       
        
        feesimgr=ImageTk.PhotoImage(feesimg)
        dateimgr=ImageTk.PhotoImage(dateimg)
        rollimgr=ImageTk.PhotoImage(rollimg)
        nameimg=ImageTk.PhotoImage(nameim)
        classimg=ImageTk.PhotoImage(classim)
        secimg=ImageTk.PhotoImage(secim)
     
        main_label=tk.Label(self,text="Add Fees",font=("TkDefaultFont", 20))
        main_label.grid(row=0,column=0,columnspan=2)
        rollno=ttk.Label(self,text="Roll No",image=rollimgr,compound=tk.LEFT,font=("TkDefaultFont", 12))
        rollno.render=rollimgr

        conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
        c=conn.cursor()
        c.execute("SELECT name,class,section FROM student  WHERE rollno={}".format(asas.rolle.get()))
        details=c.fetchall()
        c.close()
        conn.close()

        name_fees=ttk.Label(self,text="Name",font=("TkDefaultFont",12),image=nameimg,compound=tk.LEFT)
        name_fees.render=nameimg
        name_fees.grid(row=2,column=0)
        name_fees1=ttk.Label(self,text=details[0][0],font=("TkDefaultFont",12))
        name_fees1.grid(row=2,column=1)

        class_fees=ttk.Label(self,text="Class",font=("TkDefaultFont",12),image=classimg,compound=tk.LEFT)
        class_fees.render=classimg
        class_fees.grid(row=3,column=0)
        class_fees1=ttk.Label(self,text=details[0][1],font=("TkDefaultFont",12))
        class_fees1.grid(row=3,column=1)

        section_fees=ttk.Label(self,text="Section",font=("TkDefaultFont",12),image=secimg,compound=tk.LEFT)
        section_fees.render=secimg
        section_fees.grid(row=4,column=0)
        section_fees1=ttk.Label(self,text=details[0][2],font=("TkDefaultFont",12))
        section_fees1.grid(row=4,column=1)
    
        rollnol=ttk.Label(self,text=asas.rolle.get(),font=("TkDefaultFont", 12))
        amt=ttk.Label(self,text="Amount",image=feesimgr,compound=tk.LEFT,font=("TkDefaultFont",12))
        amt.render=feesimgr
        dos=ttk.Label(self,text="Date",image=dateimgr,compound=tk.LEFT,font=("TkDefaultFont", 12))
        dos.render=dateimgr

        fsave=ttk.Button(self,text="Add",image=addimgr,compound=tk.LEFT,command=self.save_fees)
        fsave.render=addimgr
        fsave.grid(row=7,column=0,columnspan=2)
        

        self.amt_e=ttk.Entry(self)

        self.dos_e=ttk.Entry(self)

        curdate=datetime.datetime.now()
        curdate1=curdate.date()
        self.dos_e.insert(0,curdate1)
        
        rollno.grid(row=1,column=0)
        rollnol.grid(row=1,column=1)

        amt.grid(row=5,column=0)
        self.amt_e.grid(row=5,column=1,padx=10)

        dos.grid(row=6,column=0,ipadx=10)
        self.dos_e.grid(row=6,column=1,padx=10)

    



    def save_fees(self):
        """Function to save fees"""
        date_ver=Date_Verify()
       

    
        
        
        if self.amt_e.get() =="" or self.dos_e.get() == "":
            tk.messagebox.showerror("Error!","Fill Amount and Date!")

        

        
        elif self.amt_e.get().isalpha():
            tk.messagebox.showerror("Error!","Fill Correct Amount!")

        elif not date_ver.isValid(self.dos_e.get()):
            tk.messagebox.showerror("Error!","Correct Date Format(YYYY-MM-DD)")

            
            


        elif self.amt_e.get().isdigit() and date_ver.isValid(self.dos_e.get()):
            try:

                conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
                c=conn.cursor()
                c.execute("INSERT INTO fees(rollno,amount,date) VALUES(%s,%s,%s)",(asas.rolle.get(),self.amt_e.get(),self.dos_e.get()))
                feesin.append() #temporarily update fees slips
                
                tk.messagebox.showinfo("Success!","Fees Successfully inserted!")
                conn.commit()
                c.close()
                self.amt_e.delete(0,tk.END)

            except Exception as e:
                tk.messagebox.showerro("Error!",e)


        else:
             tk.messagebox.showerror("Error!","Check Amount!")

            
            
          


      
 
class Del_Fees(tk.Frame):
    """Frame to show Del Fees widgets"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        idimg=Image.open('images/driver-license.png')
        idimgr=ImageTk.PhotoImage(idimg)
        delimg=Image.open('images/delete.png')
        delimgr=ImageTk.PhotoImage(delimg)
        
       


        dell=ttk.Label(self,text="Delete Fees Slip",font=("TkDefaultFont", 20))
        dell.grid(row=1,column=0,columnspan=3)

        feeid=ttk.Label(self,text="Fees Id",image=idimgr,compound=tk.LEFT)
        feeid.render=idimgr

        feeid.grid(row=2,column=0)
        self.feeid_e=ttk.Entry(self)
        self.feeid_e.grid(row=2,column=1)

        del_but=ttk.Button(self,text="Delete",image=delimgr,compound=tk.LEFT,command=self.del_fee)
        del_but.render=delimgr
        del_but.grid(row=3,column=0,columnspan=2)

    def getDelfee(self):
        """Function to get fees related to fees id"""
        conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
        c=conn.cursor()
        c.execute("SELECT amount FROM fees WHERE fees_id={}".format(self.feeid_e.get()))
        f=c.fetchone()
        c.close()
        conn.close()
        return f[0]
    
  
    def getdeldata(self):
        """Function to get total fees submitted by student"""
        try:
            conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
            c=conn.cursor()
            c.execute("SELECT CAST(SUM(amount) AS SIGNED) FROM fees WHERE rollno={}".format(asas.rolle.get()))
            
            rec=c.fetchone()
            total=rec[0]
            return total
            c.close()
            conn.close()
        except Exception as e:
            tk.messagebox.showerro("Error!",e)



    def del_fee(self):

        """Function to delete fees by using its fees id"""
        conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
        c=conn.cursor()
        c.execute("SELECT rollno FROM fees WHERE fees_id={}".format(self.feeid_e.get()))
        check_feeid=c.fetchall()
        if check_feeid:
            del_amt=self.getDelfee()
            prev_data=self.getdeldata()
            try:

                c.execute("DELETE FROM fees WHERE fees_id={}".format(self.feeid_e.get()))
                conn.commit()
        
                total_amt.configure(text=prev_data-int(del_amt))

                tk.messagebox.showinfo("Success!","Fees Successfully deleted!")
        
                self.feeid_e.delete(0,tk.END)
                c.close()
                conn.close()
            except Exception as e:
                tk.messagebox.showerro("Error!",e)


        else:
            tk.messagebox.showerror("Error!","Invalid Id!")
        
        

feesw=None
class Fees_Info(tk.Frame):

    """Frame to show fees Slips in fees window"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        


    
    def show_fees(self):
        """function to show fees slips"""
        

        conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
        c=conn.cursor()
        c.execute("SELECT * FROM fees WHERE rollno={}".format(asas.rolle.get()))
        rec=c.fetchall()
        self.r=3
        for a in rec:
            self.c=0
            
            feesidi=ttk.Label(self,text=a[0],font=("TkDefaultFont",11))
            feesidi.grid(row=self.r,column=self.c,padx=10)
            self.c+=1
            amti=ttk.Label(self,text=a[2],font=("TkDefaultFont", 11))
            amti.grid(row=self.r,column=self.c,padx=55)
            self.c+=1
            dateii=ttk.Label(self,text=a[3],font=("TkDefaultFont",11))
            dateii.grid(row=self.r,column=self.c)
            self.r+=1

    def append(self):
        """Function to temporarily add fees slips"""

        if (feesw.amt_e.get() and feesw.dos_e.get()) !="":
            def fees_up():
                conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
                c=conn.cursor()
                c.execute("SELECT CAST(SUM(amount) AS SIGNED) FROM fees WHERE rollno={}".format(asas.rolle.get()))
                   
                rec=c.fetchone()
                total=rec[0]
               

                    
                return total
                c.close()
                conn.close()

            self.c=0
            feesidi=ttk.Label(self,text='AA',font=("TkDefaultFont",11))
            feesidi.grid(row=self.r,column=self.c,padx=10)
            self.c+=1
            amti=ttk.Label(self,text=feesw.amt_e.get(),font=("TkDefaultFont", 11))
            amti.grid(row=self.r,column=self.c,padx=45)
            self.c+=1
            dateii=ttk.Label(self,text=feesw.dos_e.get(),font=("TkDefaultFont",11))
            dateii.grid(row=self.r,column=self.c)
            self.r+=1

            #update total fees paid amount temporarily
            data11=fees_up()
            if data11==None:
                data11=0
            total_amt.configure(text=(data11+int(feesw.amt_e.get())))
            
          
            
        


#####################################################################################################
##                                      Fees Window Frames                                         ##

month = 0
days = 0

class Due_Fees(tk.Frame):
    """fRame to show window with students that have pending fees"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def info(self):
        """Function to display students with pending fees"""

        conn = mysql.connect(
            host='localhost', database='tuition', user='app_admin', password='app_admin@12345')
        c = conn.cursor()

        c.execute("SELECT rollno,name,doj,class,section FROM student")

        rec1 = c.fetchall()
        r = 2
        roll2 = ttk.Label(self,text="Roll No", font=("TkDefaultFont",12,"bold"))
        roll2.grid(row=1, column=0)

        name3 = ttk.Label(self,text="Name", font=("TkDefaultFont",12,"bold"))
        name3.grid(row=1, column=1)

        class2 = ttk.Label(self,text="Class", font=("TkDefaultFont", 12,"bold"))
        class2.grid(row=1, column=2)

        section2= ttk.Label(self,text="Section", font=("TkDefaultFont",12,"bold"))
        section2.grid(row=1, column=3)

        doj2= ttk.Label(self,text="DOJ", font=("TkDefaultFont",12,"bold"))
        doj2.grid(row=1, column=4)

        for a in rec1:
            c = 0
            if a[2] is not None:
                y, m, d = str(a[2]).split('-')

                if self.isdue(y, m, d, a[0]):
                  
                    due_date = month, "month", days, "days"

                    roll1 = ttk.Label(
                        self, text=a[0], font=("TkDefaultFont", 11))
                    roll1.grid(row=r, column=c,padx=10)
                    c += 1

                    name1 = ttk.Label(
                        self, text=a[1], font=("TkDefaultFont", 11))
                    name1.grid(row=r, column=c,padx=30)
                    c += 1

                    class11 = ttk.Label(
                        self, text=a[3], font=("TkDefaultFont", 11))
                    class11.grid(row=r, column=c,padx=15)
                    c += 1

                    section1 = ttk.Label(
                        self, text=a[4], font=("TkDefaultFont", 11))
                    section1.grid(row=r, column=c,padx=15)
                    c += 1

                    month1 = ttk.Label(self, text=due_date,
                                       font=("TkDefaultFont", 11))
                    month1.grid(row=r, column=c,padx=22)
                    r += 1

    def isdue(self, y, m, d, roll):

        self.y = int(y)
        self.m = int(m)
        self.d = int(d)
        self.roll = roll
        import datetime
        conn = mysql.connect(
            host='localhost', database='tuition', user='app_admin', password='app_admin@12345')
        d = conn.cursor()

        d.execute("SELECT rollno,date FROM fees WHERE rollno={}".format(self.roll))

        rec2 = d.fetchall()
        
        date1 = datetime.datetime.now()
        curdate = date1 #current date
        jdate = datetime.datetime(self.y, self.m, self.d) #date of joining of student
        difference = (curdate-jdate) #difference between their dates 

        data = difference.days #total number of days
        data1=difference.days

        global month,days
        month = 0
        days = 0
        
        datedif = ((difference.days//30)-len(rec2))
        data1=(data1-(30*len(rec2)))
        while data1 > 0:
            if data1 >= 30:
                data1 -= 30
                month += 1
            else:
                days = data1
                break
           
        

        
        if datedif >= 0:
            
           
            return True
        else:
            return False


class Student_Edit_Main(tk.Frame):
    """Empty Frame to Hold Student Edit frame and Student Edit Image Frame"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
class Student_Edit_Image(tk.Frame):
    """Frame for placing banner in Student Edit Main Frame"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

sri_canvas=None
sri=None
class Quotes_Animation:
    """Class for animation of quotes"""
    def __init__(self):
        self.y_cord=180
        self.x_cord=250
        self.change_time=3000

        self.q1='Change is the end result of all true learning. – Leo Buscaglia'
        self.q2='An investment in knowledge pays the best interest. –  Benjamin Franklin'
        self.q3='Live as if you were to die tomorrow. Learn as if you were to live forever. ― Mahatma Gandhi'
        self.q4='The learning process continues until the day you die. – Kirk Douglas'
        self.q5='Education is not preparation for life; education is life itself. – John Dewey'
        self.q6='They know enough who know how to learn. – Henry Adams'
        self.q7='All power is within you; You can do anything and everything. - Swami Vivekananda'
        self.q8='Books are the means by which we build bridges between cultures. - Sarvepalli Radhakrishnan'

    def chnge(self):
        sri_canvas.delete('abc')
        sri_canvas.create_text(self.x_cord,self.y_cord,text=self.q2,justify=tk.CENTER,font=('Purisa',20),width=400,tags="abc",fill="red")
        sri.after(self.change_time,self.chnge1)

    def chnge1(self):
        sri_canvas.delete('abc')
        sri_canvas.create_text(self.x_cord,self.y_cord,text=self.q3,justify=tk.CENTER,font=('Arial',20),width=400,tags="abc",fill="red")
        sri.after(self.change_time,self.chnge2)

    def chnge2(self):
        sri_canvas.delete('abc')
        sri_canvas.create_text(self.x_cord,self.y_cord,text=self.q4,justify=tk.CENTER,font=('Arial',20),width=400,tags="abc",fill="red")
        sri.after(self.change_time,self.chnge3)

    def chnge3(self):
        sri_canvas.delete('abc')
        sri_canvas.create_text(self.x_cord,self.y_cord,text=self.q5,justify=tk.CENTER,font=('Arial',20),width=400,tags="abc",fill="red")
        sri.after(self.change_time,self.chnge4)

    def chnge4(self):
        sri_canvas.delete('abc')
        sri_canvas.create_text(self.x_cord,self.y_cord,text=self.q6,justify=tk.CENTER,font=('Arial',20),width=400,tags="abc",fill="red")
        sri.after(self.change_time,self.chnge5)

    def chnge5(self):
        sri_canvas.delete('abc')
        sri_canvas.create_text(self.x_cord,self.y_cord,text=self.q7,justify=tk.CENTER,font=('Arial',20),width=400,tags="abc",fill="red")
        sri.after(self.change_time,self.chnge6)

    def chnge6(self):
        sri_canvas.delete('abc')
        sri_canvas.create_text(self.x_cord,self.y_cord,text=self.q8,justify=tk.CENTER,font=('Arial',20),width=400,tags="abc",fill="red")
        sri.after(self.change_time,self.chnge)


class PDF_gen:

    """Class to create pdf for individual students with their details and fees details"""
    def __init(self):
        pass

    def get_total_amt(self,r):
        
        conn = mysql.connect(host='localhost', database='tuition',user='app_admin', password='app_admin@12345')
        c = conn.cursor()
        c.execute('SELECT CAST(SUM(amount) AS SIGNED) FROM fees WHERE rollno={}'.format(r))
        rec = c.fetchall()
        return rec[0][0]

    def generate_pdf(self,r,ins):
        conn = mysql.connect(host='localhost', database='tuition',user='app_admin', password='app_admin@12345')
        c = conn.cursor()
        c.execute('SELECT * FROM student WHERE rollno={}'.format(r))
        rec1 = c.fetchall()
        pdf = FPDF(orientation='P')
        pdf.add_page()
        pdf.set_font('Arial', "B", 30)
        pdf.set_text_color(156,33,33)  
        pdf.cell(180, 10,ins, align="C")
        pdf.ln(30)
        pdf.line(10, 30, 200,30)
        pdf.set_font('Arial', "B", 15)

        line_space=14
        x1=30
        x2=10
        pdf.set_text_color(0,0,0)  
        pdf.cell(x1, 10,"Roll No", align="L")
        pdf.cell(x2+60, 10,str(rec1[0][0]), align="L")
        pdf.cell(x1, 10,"Address", align="L")
        pdf.cell(x2, 10,str(rec1[0][5]), align="L")
        pdf.ln(line_space)

        pdf.cell(x1, 10,"Name", align="L")
        pdf.cell(x2+60, 10,str(rec1[0][1]), align="L")
        pdf.cell(x1, 10,"Father", align="L")
        pdf.cell(x2, 10,str(rec1[0][6]), align="L")
        pdf.ln(line_space)

        pdf.cell(x1, 10,"Class", align="L")
        pdf.cell(x2+60, 10,str(rec1[0][2]), align="L")
        pdf.cell(x1, 10,"Phone", align="L")
        pdf.cell(x2, 10,str(rec1[0][7]), align="L")
        pdf.ln(line_space)

        pdf.cell(x1, 10,"Section", align="L")
        pdf.cell(x2+60, 10,str(rec1[0][3]), align="L")
        pdf.cell(x1, 10,"DOJ", align="L")
        pdf.cell(x2, 10,str(rec1[0][9]), align="L")
        pdf.ln(line_space)

        pdf.cell(x1, 10,"School", align="L")
        pdf.cell(x2, 10,str(rec1[0][4]), align="L")
        pdf.line(10, 110, 200, 110)
        c.close()
        conn.close()
        pdf.ln(line_space)
        pdf.set_font('Arial', "B", 20)
        pdf.set_text_color(3,115,252)  
        pdf.cell(180, 40,"Fees Details", align="C")
        pdf.ln(30)

        pdf.set_font('Arial', "B", 15)
        pdf.set_text_color(0,0,0)
        conn1 = mysql.connect(host='localhost', database='tuition',user='app_admin', password='app_admin@12345')
        c = conn1.cursor()
        c.execute('SELECT * FROM fees WHERE rollno={}'.format(r))
        rec = c.fetchall()
        pdf.cell(20, 10,"Fees Id", align="C")
        pdf.cell(40, 10,"Amount", align="C")
        pdf.cell(20, 10,"Date", align="C")
        pdf.ln(15)
        for i in rec:
            pdf.cell(20, 10,str(i[0]), align="C")
            pdf.cell(40, 10,str(i[2]), align="C")
            pdf.cell(20, 10,str(i[3]), align="C")
            pdf.ln(14)

        c.close()
        conn1.close()
        pdf.ln(30)
        pdf.set_font('Arial', "B",20)
        pdf.set_text_color(3,115,252)
        pdf.cell(180, 10,"Fees Status", align="C")
        pdf.ln(15)
        pdf.set_font('Arial', "B",15)
        pdf.set_text_color(0,0,0)
        pdf.cell(40, 10,"Total Amount", align="L")
        pdf.cell(20, 10,str(self.get_total_amt(r)), align="L")
        save_name=str(rec1[0][1])+".pdf"
        if sys.platform=="win32":
    

            path=os.path.join(os.environ["USERPROFILE"],"Desktop")
          
            filepath=os.path.join(path,"Tuition Fees Slips")
            if not os.path.exists(filepath):
                os.mkdir(filepath)

            else:
                print("Folder Exists")
        try:

            save_name=os.path.join(filepath,str(rec1[0][1])+".pdf")
            pdf.output(save_name, 'F')

        except:
            pdf.output(save_name,'F')


####################################################################################

notebook1=None
asas=None

class MyApplication(tk.Tk): 
    """Main Application class"""
    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)        
        self.title("Tuition Management")
        self.resizable(False,False)
        self.a=Teacher_Register(self)
        self.a.grid(row=0,column=0,sticky=(tk.N+tk.W))
        loginimg=Image.open('images/login (1).png')
        login_img=ImageTk.PhotoImage(loginimg)

        self.login1=ttk.Button(self.a,text="Login",image=login_img,compound=tk.LEFT,command=self.open_login)
        self.login1.render=login_img
        self.login1.grid(row=4,column=1,pady=10)  

     

    def open_login(self):
        """Function to open login window"""
        self.a.destroy() #destroys teacher registeration frame
        self.p=Teacher_login(self) #opens teacher login ui
        self.p.grid()
        logim=Image.open('images/login (3).png')
        logimg=ImageTk.PhotoImage(logim)

       

        log= ttk.Button(self.p,text="Login",command=self.login,image=logimg,compound=tk.LEFT)   
        log.render=logimg  
        log.grid(columnspan=2,pady=10) 
        self.login1.destroy()#open login window destroying the current window

    def login(self):
        """Function to execute if login creds are True"""
        try:

            conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
            c=conn.cursor()
            c.execute("SELECT * FROM teacher WHERE username=%s AND password=%s",(self.p.usrl.get(),self.p.passl.get()))
            rec=c.fetchall()
        except Exception as e:
            tk.messagebox.showerror("Error!",e)
            app.destroy()
        
        else:
            
            if rec:
                #to be used when creating separate table for each user
                #global stu_table
                #global stu_fees
                #stu_table=self.p.usrl.get()+"_student"
                #stu_fees=self.p.usrl.get()+"_fees"

                c.execute("""CREATE TABLE IF NOT EXISTS student (
                                rollno int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                name varchar(25) NOT NULL,
                                class int(2) NOT NULL,
                                section varchar(10) DEFAULT NULL,
                                school varchar(30) NOT NULL,
                                address varchar(30) DEFAULT NULL,
                                father varchar(30) DEFAULT NULL,
                                father_no varchar(10) DEFAULT NULL,
                                mobile varchar(10) NOT NULL,
                                doj date NOT NULL,
                                FULLTEXT KEY name (name,father))
                                ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; """)

                c.execute("""CREATE TABLE IF NOT EXISTS fees (
                            fees_id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            rollno int(10) NOT NULL,
                            amount int(10) NOT NULL,
                            date date NOT NULL,
                            CONSTRAINT foreignkey FOREIGN KEY (rollno) REFERENCES student (rollno) ON DELETE CASCADE
                            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;""")
                
                self.p.destroy()
                global notebook1
                notebook1=ttk.Notebook(self)
                notebook1.grid(row=0,column=0)

                sregmain=Student_Registeration_Image_Main(notebook1) #main frame to hold two frames (Student Registeration and Student Registration Image)
                sregmain.grid(row=0,column=0)
                sreg=Student_Registeration(sregmain) #opens student registeration frame in notebook
                clim=Image.open('images/digital-clock.png')
                clim=clim.resize((200, 100), Image.ANTIALIAS)
                cloc_img=ImageTk.PhotoImage(clim)
                banner=Image.open('images/books.jpg')
                banner=banner.resize((730, 490), Image.ANTIALIAS)
                banner_r=ImageTk.PhotoImage(banner)

                global sri
                sri=Student_Registeration_Image(sregmain)# frame in Student Registration Main for image
                sri.grid(row=0,column=1)

                global sri_canvas
                sri_canvas=tk.Canvas(sri,height=520,width=730)
                sri_canvas.grid(row=0,column=0,sticky=tk.NSEW)
            
                
                sri_canvas.create_image(370,270,image=banner_r)
                sri_canvas.render=banner_r
                global institute_lbl
                institute_lbl=rec[0][0] #name of institute
                
                sri_canvas.create_text(360,60,text=institute_lbl,font=('Arial',30),anchor=tk.CENTER,justify=tk.CENTER,width=700,fill="#7200ca")
                sri_canvas.create_line(80,90,700,90)

                qts=Quotes_Animation() #initialising quotes_animation class
                def quotesThred():
                    global sri_canvas

                    sri_canvas.create_text(qts.x_cord,qts.y_cord,text="Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world. - Albert Einstein",font=('Purisa',20),anchor=tk.CENTER,tags="abc",width=400,justify=tk.CENTER,fill="red")
                    sri.after(3000,qts.chnge)
                t1=threading.Thread(target=quotesThred)
                t1.start()

                def tick():
                    time_string=time.strftime("%H:%M:%S")
                    clock.config(text=time_string)
                    clock.after(200,tick)
            
                
                cl_lbl=ttk.Label(sri_canvas,image=cloc_img)
                cl_lbl.render=cloc_img
                cl_lbl.place(x=70,y=300)
                clock=ttk.Label(sri_canvas,font=("arial",20,"bold"),anchor=tk.CENTER,justify=tk.CENTER,background="#c50e29",foreground="white")
                clock.place(x=90,y=318,height=70,width=168)

                t2=threading.Thread(target=tick) #separate thread for clock
                t2.start()

                sreg.grid(row=0,column=0)

                
                stuedit=Student_Edit_Main(notebook1) #Frame to hold student_edt_img frame 
                stuedit.grid(row=0,column=0)

                student_edt_img=Student_Edit_Image(stuedit) #frame for image in student edit window
                student_edt_img.grid(row=0,column=1)

                edit_banner=Image.open('images/gwhqps.jpg') #banner image in edit student window

                edit_banner=edit_banner.resize((770, 495), Image.ANTIALIAS)
                edit_banner_img=ImageTk.PhotoImage(edit_banner)

                student_edt_img_lbl=ttk.Label(student_edt_img,image=edit_banner_img)
                student_edt_img_lbl.render=edit_banner_img
                student_edt_img_lbl.grid(row=0,column=0,sticky=tk.EW)




                global asas
                asas=Student_Edit_Ask(stuedit) #frame to ask roll no to open edit or fees window
                
                asas.grid(row=0,column=0)


            
                std_info=Student_Info(notebook1)# initialising student info window
                std_info.student_Count()
                std_info.grid(row=0,column=0)
                ##############################################
                
        

                img_canvas=tk.Canvas(notebook1,width=900,height=500)
                img_canvas.grid(row=0,column=1)
                global bc_img
                global bc_imgr

                bc_img=Image.open('images/PWS-BlogTopic-Aug20-Resized-copy.jpg') #backgrund image for due fees window
                bc_img=bc_img.resize((1200, 500), Image.ANTIALIAS)
                bc_imgr=ImageTk.PhotoImage(bc_img)

                img_canvas.create_image(600,250,image=bc_imgr)
                label=img_canvas.create_text(330,110,text="Due Fees",font=("TkDefaultFont",30),fill="red")
                container = tk.Frame(img_canvas)
                



                canvas = tk.Canvas(container, width=520, height=265)
                scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        
                due = Due_Fees(canvas) #Due fees frame
                due.info()

                def refresh1():
                    """Function to refresh due fees window"""
                    nonlocal due
                    due.destroy()
                    due = Due_Fees(canvas)
                    due.info()
                    canvas.create_window((0, 0), window=due, anchor="nw")
                

                refresh_due=ttk.Button(img_canvas,text="Refresh",command=refresh1)
                refresh_due.place(x=100,y=460)
            

                due.bind(
                    "<Configure>",
                    lambda e: canvas.configure(
                        scrollregion=canvas.bbox("all")
                    )
                )


                canvas.create_window((0, 0), window=due, anchor="nw")
                canvas.configure(yscrollcommand=scrollbar.set)

                #container.grid(row=1, column=1)
                canvas.grid(row=2, column=0)
                scrollbar.grid(row=2, column=1, sticky=tk.NS)

                img_canvas.create_window(300,280,window=container)


                img1=Image.open('images/internet.png')
                img11=ImageTk.PhotoImage(img1)

                notebook1.add(sregmain,text="Add",image=img11,compound=tk.LEFT) #add Add tab in notebook
                notebook1.render=img11

                notebook1.add(std_info,text="Info") #add Info tab in notebook
                notebook1.add(img_canvas,text="Due Fees")

                notebook1.add(stuedit,text="Edit")
                editim=Image.open('images/pencil.png')
                feesim=Image.open('images/money-bag.png')
                deli=Image.open('images/delete.png')
                pdi=Image.open('images/pdf.png')

                editimg=ImageTk.PhotoImage(editim)
                feesimg=ImageTk.PhotoImage(feesim)
                delimg1=ImageTk.PhotoImage(deli)
                pdf_img=ImageTk.PhotoImage(pdi)

                editbut=ttk.Button(asas,text="Edit",command=self.open_editable_win,image=editimg,compound=tk.LEFT)
                editbut.render=editimg
                editbut.grid(row=3,column=0)

                feesbut=ttk.Button(asas,text="Fees",command=self.open_fees_window,image=feesimg,compound=tk.LEFT)
                feesbut.render=feesimg
                feesbut.grid(row=3,column=1)

                delstu=ttk.Button(asas,text="Delete",image=delimg1,compound=tk.LEFT,command=self.delete_student_record)
                delstu.render=delimg1
                delstu.grid(row=4,column=0,pady=10)

                pdfbut=ttk.Button(asas,text="Gen. PDF",image=pdf_img,compound=tk.LEFT,command=self.create_pdf)
                pdfbut.render=pdf_img
             
                pdfbut.grid(row=4,column=1,pady=10)

            else:
                c.close()
                conn.close()
                tk.messagebox.showerror("Error!","Incorrect Username or Password!")

    def create_pdf(self):
      
        if asas.rolle.get()!="":
            try:
                pdf_cl=PDF_gen()
                pdf_cl.generate_pdf(asas.rolle.get(),institute_lbl)
                tk.messagebox.showinfo("Success!","PDF report for student successfully created!")

            except Exception as e:
                tk.messagebox.showerror("Error!",e)

        else:
            tk.messagebox.showerror("Error!","Provide Valid Roll No!")  
    def delete_student_record(self):
        if asas.rolle.get()!="":
            response=tk.messagebox.askquestion('Delete Roll No!','The data of Roll No will be deleted!') 
            if response=="yes":
                try:

                    conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
                    c=conn.cursor()
                    c.execute("DELETE FROM student WHERE rollno={}".format(asas.rolle.get()))
                    conn.commit()
                    tk.messagebox.showinfo("Success!","Record Successfully Deleted!")
                    c.close()
                    conn.close()

                except Exception as e:
                    tk.messagebox.showerror("Error!",e)
        else:
            tk.messagebox.showerror("Error!","Provide Valid Roll No!")


    def open_editable_win(self):
        if asas.rolle.get()!="":
            ste_edit_ban=Image.open('images/books1.jpg')
            ste_edit_ban=ste_edit_ban.resize((730, 490), Image.ANTIALIAS)
            ste_banner=ImageTk.PhotoImage(ste_edit_ban)

            
            close_bt=Image.open('images/cancel.png')
            close_btn_img=ImageTk.PhotoImage(close_bt)

            def close_tab_fees():
                """Function to close Student Edit window tabs """
                student_edit_main_frame.destroy()
            
            conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
            c=conn.cursor()
            c.execute("SELECT * FROM student WHERE rollno={}".format(asas.rolle.get())) 
            rec=c.fetchall()
            if rec:
                
                
                student_edit_main_frame=Student_Edit_Main(notebook1)#main frame in student edit window
                student_edit_main_frame.grid()

                student_edit_canvas=tk.Canvas(student_edit_main_frame,height=530,width=730)#canvas for creating image in student edit window
                student_edit_canvas.grid(row=0,column=1)
                student_edit_canvas.create_image(370,280,image=ste_banner)# image in student edit window in canvas
                student_edit_canvas.render=ste_banner

                

                ste=Student_Edit(student_edit_main_frame)
                ste.grid(row=0,column=0)
                txt=f"Update {asas.rolle.get()}"
                notebook1.add(student_edit_main_frame,text=txt)
                remove_edit_tab=ttk.Button(ste,text="Close Window",command=close_tab_fees,image=close_btn_img,compound=tk.LEFT)
                remove_edit_tab.render=close_btn_img
                remove_edit_tab.grid(row=12,column=0,columnspan=2,pady=10)
                
            else:
                tk.messagebox.showerror("Error!","Provide correct Roll No.")
        else:

            tk.messagebox.showerror("Error!","Roll No can't be empty!")

        
        


    def open_fees_window(self):
        if asas.rolle.get() !="":

            conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
            c=conn.cursor()
            c.execute("SELECT * FROM student WHERE rollno={}".format(asas.rolle.get()))  
            rec=c.fetchall()

            if rec:
            
                
                fs=Fees_Main_Frame(notebook1) #frame to show fees frames
            
                fs.grid(row=0,column=0)

            
                bannerimg=Image.open('images/fee-banner.jpg')
                bannerimg=bannerimg.resize((980, 200), Image.ANTIALIAS)
                banner_img=ImageTk.PhotoImage(bannerimg)

                main_banner=tk.Label(fs,image=banner_img)
                main_banner.render=banner_img
                main_banner.grid(row=0,column=0,columnspan=3)

                #feesw.grid(row=0,column=0)

                fees_canvas=tk.Canvas(fs,width=400)#fees window
                global feesw
                feesw=Fees(fees_canvas) #Fees Frame

                fees_canvas.grid(row=1,column=0) 
                fees_canvas.create_window((150,130),window=feesw)

                container = tk.Frame(fs)
                fees_slip=ttk.Label(container,text="Fees Slips",font=("TkDefaultFont", 20))
                fees_slip.grid(row=0,column=0,columnspan=3)

                
                canvas = tk.Canvas(container,width=350)

                feesid=ttk.Label(container,text="F_Id        Amount          Date",font=("TkDefaultFont", 14))

                
    
                feesid.grid(row=1,column=0,sticky=tk.W)
            

                scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)

                global feesin
                feesin = Fees_Info(canvas) #frame to show fees slips
                feesin.show_fees()
                
            

                feesin.bind(
                    "<Configure>",
                    lambda e: canvas.configure(
                        scrollregion=canvas.bbox("all")
                    )
                )


                canvas.create_window((0, 0), window=feesin, anchor="nw")

                canvas.configure(yscrollcommand=scrollbar.set)

                container.grid(row=1,column=1,padx=10)


                canvas.grid(row=2,column=0)
                
                scrollbar.grid(row=2,column=1,sticky=tk.NS)



            
                del_canvas=tk.Canvas(fs,width=290)
                del_canvas.grid(row=1,column=2)

                df=Del_Fees(del_canvas)# fess delete window in main fees frame
                
                close_bt=Image.open('images/cancel.png')
                close_btn_img=ImageTk.PhotoImage(close_bt)

                def close_tabs():
                    
                    fs.destroy()# destroys a fees window opened as Fees tab
                    
                def total_paid():
                    """Function to get total fees submitted of a roll no"""
                    conn=mysql.connect(host='localhost',database='tuition',user='app_admin',password='app_admin@12345')
                    c=conn.cursor()
                    c.execute("SELECT CAST(SUM(amount) AS SIGNED) FROM fees WHERE rollno={}".format(asas.rolle.get()))
                    #c.execute("SELECT SUM(amount) FROM fees WHERE rollno='"+asas.rolle.get()+"'")    
                    rec=c.fetchone()
                    total=rec[0]
               

                    
                    return total
                    c.close()
                    conn.close()


                
                
                global total_fees_paid
                total_fees_paid=total_paid()
                

               
                
                
                
                
                total=ttk.Label(df,text="Total Paid",font=("TkDefaultFont", 14))
                total.grid(row=5,column=0)

                global total_amt
                total_amt=ttk.Label(df,text=total_fees_paid,font=("TkDefaultFont", 14)) #label to display total fees paid
                total_amt.grid(row=5,column=1)

                close_window=ttk.Button(df,text="Close Window",command=close_tabs,image=close_btn_img,compound=tk.LEFT) #button to close the current window
                close_window.render=close_btn_img
                close_window.grid(row=4,column=0,columnspan=2,padx=10)

                del_canvas.create_window((130,100),window=df)
                txt1=f"Fees {asas.rolle.get()}"

                notebook1.add(fs,text=txt1)
            
            else:
                tk.messagebox.showerror("Error!","Provide correct Roll No.")

        else:
            tk.messagebox.showerror("Error!","Roll No can't be empty!")

            
            

    
           

#if __name__ == '__main__':    
app = MyApplication()
    
app.mainloop()
    





