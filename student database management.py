from tkinter import *
from tkinter import ttk #this  module provide combo box. See gender label.
import pymysql
root=Tk()
class Student:
    def add_students(self):
        conn=pymysql.connect(host="localhost",user="root",passwd="",database="Mystudent")
        cur=conn.cursor()
        cur.execute("insert into data1 values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),self.address_var.get()))
        conn.commit()
        self.fetch_data1()
        self.clear()
        conn.close()

    def fetch_data1(self):
        conn=pymysql.connect(host="localhost",user="root",passwd="",database="Mystudent")
        cur=conn.cursor()
        cur.execute("select * from data1")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
        conn.commit()
        conn.close()


    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.address_var.set("")


    def get_cursor(self,ev):
        curosor_row=self.Student_table.focus()
        contents=self.Student_table.item(curosor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.address_var.set(row[6])

    def update_data1(self):
        conn=pymysql.connect(host="localhost",user="root",passwd="",database="Mystudent")
        cur=conn.cursor()
        cur.execute("update  data1 set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roo_no=%s",(
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.address_var.get(),
                                                                         self.Roll_No_var.get()))
        conn.commit()
        self.fetch_data1()
        self.clear()
        conn.close()


    def delete_data1(self):
        conn=pymysql.connect(host="localhost",user="root",passwd="",database="Mystudent")
        cur=conn.cursor()
        #sql=
        cur.execute('delete from data1 where roo_no=%s',self.Roll_No_var.get())
        conn.commit()
        conn.close()
        self.fetch_data1()
        self.clear()


    def search_data1(self):
        conn=pymysql.connect(host="localhost",user="root",passwd="",database="Mystudent")
        cur=conn.cursor()
        cur.execute("select * from data1 where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
        conn.commit()
        conn.close()
        

    def __init__(self,root):
        ########### Header #############
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="Grey",fg="blue")
        title.pack(side=TOP,fill=X)

        ################Variables###############
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.address_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        ############ Manage Frame #############
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=580)
        m_title=Label(Manage_Frame,text="Manage Students",font=("times new roman",20,"bold"),fg="Green",bg="yellow")
        m_title.grid(row=0,columnspan=2,pady=20,padx=100)

        lbl_roll=Label(Manage_Frame,text="Roll Number",font=("times new roman",15,"bold"),fg="white",bg="crimson")
        lbl_roll.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        txt_roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,padx=10,pady=10,sticky="W")


        lbl_name=Label(Manage_Frame,text="Name",font=("times new roman",15,"bold"),fg="white",bg="crimson")
        lbl_name.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,padx=10,pady=10,sticky="W")

        lbl_email=Label(Manage_Frame,text="Email ID",font=("times new roman",15,"bold"),fg="white",bg="crimson")
        lbl_email.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,padx=10,pady=10,sticky="W")

        lbl_Gender=Label(Manage_Frame,text="Gender",font=("times new roman",15,"bold"),fg="white",bg="crimson")
        lbl_Gender.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        combo_Gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state="readonly")
        combo_Gender['values']=("Male","Female","Other")
        combo_Gender.grid(row=4,column=1,padx=10,pady=10)

        lbl_Contact=Label(Manage_Frame,text="Contact",font=("times new roman",15,"bold"),fg="white",bg="crimson")
        lbl_Contact.grid(row=5,column=0,padx=10,pady=10,sticky="w")
        txt_Contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,padx=10,pady=10,sticky="W")

        lbl_DOB=Label(Manage_Frame,text="DOB",font=("times new roman",15,"bold"),fg="white",bg="crimson")
        lbl_DOB.grid(row=6,column=0,padx=10,pady=10,sticky="w")
        txt_DOB=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,padx=10,pady=10,sticky="W")

        lbl_Address=Label(Manage_Frame,text="Address",font=("times new roman",15,"bold"),fg="white",bg="crimson")
        lbl_Address.grid(row=7,column=0,padx=10,pady=10,sticky="w")
        txt_Address=Entry(Manage_Frame,textvariable=self.address_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Address.grid(row=7,column=1,padx=10,pady=10,sticky="W")

        ############Manage Button###########
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="blue")
        btn_Frame.place(x=10,y=500,width=430)
        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data1).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data1).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)



        ############ Detail Frame #############
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=820,height=580)

        lbl_search=Label(Detail_Frame,text="Search_By",font=("times new roman",15,"bold"),fg="white",bg="crimson")
        lbl_search.grid(row=0,column=0,padx=10,pady=10,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=15,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("roo_no","name")
        combo_search.grid(row=0,column=1,padx=10,pady=10)

        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10,command=self.search_data1).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show all",width=10,command=self.fetch_data1).grid(row=0,column=4,padx=10,pady=10)


        ########### Table Frame. #################
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=20,y=70,width=760,height=500)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll Number")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email ID")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("DOB",text="DOB")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column('roll',width=100)
        self.Student_table.column('name',width=100)
        self.Student_table.column('email',width=100)
        self.Student_table.column('Gender',width=100)
        self.Student_table.column('Contact',width=100)
        self.Student_table.column('DOB',width=100)
        self.Student_table.column('Address',width=150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data1()
oj=Student(root)
root.mainloop()
