from tkinter import *
import os
import bcrypt
from database import *

createTable()

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()
        
def delete5():
    screen10.destroy()
    
def delete6():
    screen14.destroy()

def delete7():
    screen12.destroy()

def delete8():
    screen6.destroy()
    
def delete9():
    screen7.destroy()

def save():
    screen9.destroy()
    filename=raw_filename.get()
    notes=raw_notes.get()
    
    data=open("Notes/"+filename,"w")
    data.write(notes)
    data.close()
    
    global screen10
    screen10=Toplevel(screen)
    screen10.title("Save Note")
    screen10.geometry("150x100")
    screen10['bg']='orange' 
    Label(screen10,text="",bg='orange').pack()
    Label(screen10,text="Saved",bg='white',fg='green',font=("Calibri",12)).pack()
    Label(screen10,text="",bg='orange').pack()
    Button(screen10,text='Ok',command=delete5).pack()

def create_notes():
    global screen9
    screen9=Toplevel(screen)
    screen9.title("Notes")
    screen9.geometry("300x300")
    screen9['bg']='orange'
    Label(screen9,text="New Note",bg="green",fg='white',width="300",height="2", font=("Calibri",13)).pack()
    Label(screen9,text="",bg='orange').pack()
    
    global raw_filename
    raw_filename=StringVar()
    global raw_notes
    raw_notes=StringVar()
    
    Label(screen9,text="Name of the note:",bg='orange').pack()
    Entry(screen9,textvariable=raw_filename).pack()
    Label(screen9,text="",bg='orange').pack()
    Label(screen9,text="Write Note:",bg='orange').pack()
    Entry(screen9,textvariable=raw_notes).pack()
    Label(screen9,text="",bg='orange').pack()
    Button(screen9,text="Save",command=save).pack()

def open_notes():
    screen11.destroy()
    filename1=raw_filename1.get()
    data=open("Notes/"+filename1,"r")
    data1=data.read()
    
    global screen12
    screen12=Toplevel(screen)
    screen12.title(filename1)
    screen12.geometry("400x400")
    screen12['bg']='orange'
    Label(screen12,text="Notes",bg="green",fg='white',width="400",height="2", font=("Calibri",13)).pack()
    Label(screen12,text="",bg='orange').pack()
    
    '''l1=Label(screen12,text=data1,bg='orange',anchor=W)
    l1.pack(fill=X)'''
    T=Text(screen12,height=15,wrap=WORD)
    T.pack()
    T.insert(END,data1)
    Label(screen12,text="",bg="orange").pack()
    Button(screen12,text="Close",command=delete7).pack()
    
def sel(event):
    x=lbox.curselection()[0]
    f=lbox.get(x)
    raw_filename1.set(f)
    
def view_notes():
    global screen11
    screen11=Toplevel(screen)
    screen11.title("Notes")
    screen11.geometry("300x400")
    screen11['bg']='orange'
    Label(screen11,text="Notes List",bg="green",fg='white',width="300",height="2", font=("Calibri",13)).pack()
    Label(screen11,text="",bg='orange').pack()
    
    all_files=os.listdir("Notes/")
    #all_files=[f for f in os.listdir("Notes/") if f.endswith('.txt')]
    
    Label(screen11,text="Use one of the filenames below",bg='orange').pack()
    #Label(screen11,text=all_files).pack()
    global lbox
    global text
    lbox=Listbox(screen11)
    lbox.pack()
    for items in all_files:
        lbox.insert(END,items)
    Label(screen11,text="",bg='orange').pack()
    lbox.bind("<<ListboxSelect>>",sel)
    
    global raw_filename1
    raw_filename1= StringVar()
    
    Label(screen11,text="Enter/Select file name",bg='orange').pack()
    Entry(screen11,textvariable=raw_filename1).pack()
    Label(screen11,text="",bg='orange').pack()
    Button(screen11,text="Open",command=open_notes).pack()

def delete_selected():
    screen13.destroy()
    filename3=raw_filename2.get()
    os.remove("Notes/"+filename3)
    
    global screen14
    screen14=Toplevel(screen)
    screen14.title("Notes")
    screen14.geometry("200x100")
    screen14['bg']='orange'
    Label(screen14,text="",bg='orange').pack()
    Label(screen14,text=filename3+" Deleted",bg='white',fg='red',font=("Calibri",12)).pack()
    Label(screen14,text="",bg='orange').pack()
    Button(screen14,text='Ok',command=delete6).pack()

def sel2(event):
    x=lbox.curselection()[0]
    f=lbox.get(x)
    raw_filename2.set(f)

def delete_note():
    global screen13
    screen13=Toplevel(screen)
    screen13.title("Notes")
    screen13.geometry("300x400")
    screen13['bg']='orange'
    Label(screen13,text="Notes List",bg="green",fg='white',width="300",height="2", font=("Calibri",13)).pack()
    Label(screen13,text="",bg='orange').pack()
    
    all_files=os.listdir("Notes/")
    Label(screen13,text="Use one of the filenames below",bg='orange').pack()
    #Label(screen11,text=all_files).pack()
    
    global lbox
    lbox=Listbox(screen13)
    lbox.pack()
    for items in all_files:
        lbox.insert(END,items)
    Label(screen13,text="",bg='orange').pack()
    lbox.bind("<<ListboxSelect>>",sel2)
    
    global raw_filename2
    raw_filename2= StringVar()
    Label(screen13,text="Enter/Select file name",bg='orange').pack()
    Entry(screen13,textvariable=raw_filename2).pack()
    Label(screen13,text="",bg='orange').pack()
    Button(screen13,text="Delete",fg="red",command=delete_selected).pack()

def session():
    screen8=Toplevel(screen)
    screen8.title("Dashboard")
    screen8.geometry("300x250")
    screen8['bg']='orange'
    Label(screen8,text="Welcome to the dashboard",bg="green",fg="white",width="300",height="2", font=("Calibri",13)).pack()
    Label(screen8,text="",bg='orange').pack()
    Button(screen8,text="Create Notes",command=create_notes).pack()
    Label(screen8,text="",bg='orange').pack()
    Button(screen8,text="View Notes",command=view_notes).pack()
    Label(screen8,text="",bg='orange').pack()
    Button(screen8,text="Delete Notes",command=delete_note).pack()
    
def login_success():
    screen2.destroy()
    session()

def login_failure():
    global screen4
    screen4=Toplevel(screen)
    screen4.title("Failure")
    screen4.geometry("150x100")
    screen4['bg']='orange'
    Label(screen4,text="",bg='orange').pack()
    Label(screen4,text="Wrong credentials",bg='white',fg='red',font=("Calibri",12)).pack()
    Label(screen4,text="",bg='orange').pack()
    Button(screen4,text="Ok",command=delete3).pack()
    

def error():
    global screen7
    screen7=Toplevel(screen)
    screen7.title("Register")
    screen7.geometry("200x100")
    screen7['bg']='orange'
    Label(screen7,text="",bg="orange").pack()
    Label(screen7,text="All fields required",bg='white',fg='red',font=("Calibri",12)).pack()
    Label(screen7,text="",bg="orange").pack()
    Button(screen7,text="Ok",command=delete9).pack()    

def success():
    screen1.destroy()
    global screen6
    screen6=Toplevel(screen)
    screen6.title("Register")
    screen6.geometry("200x100")
    screen6['bg']='orange'
    Label(screen6,text="",bg='orange').pack()
    Label(screen6,text="Registration Successful",bg='white',fg="green",font=("Calibri",12)).pack()
    Label(screen6,text="",bg="orange").pack()
    Button(screen6,text="Ok",command=delete8).pack()
    
def register_user():
    username_info=username.get()
    password_info=password.get()
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    if username_info=="":
        error()
    elif password_info=="":
        error()
    else:
        salt=bcrypt.gensalt()
        hashed=bcrypt.hashpw(password_info.encode(),salt)
        d=(username_info,)
        result=searchData(d)
        #print(result)
        if result!=0:
            d=(username_info,hashed)
            insertData(d)
            success()
        else:
            error()


def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    screen1['bg']='orange'
    
    global username
    global password
    global username_entry
    global password_entry
    username=StringVar()
    password=StringVar()
    Label(screen1,text="Please enter details",bg="white",fg='black',width="300",height="2", font=("Calibri",13)).pack()
    Label(screen1,text="",bg="orange").pack()
    Label(screen1,text="Username *",bg="orange").pack()
    username_entry=Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text="",bg="orange").pack()
    Label(screen1,text="Password *",bg="orange").pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text="",bg="orange").pack()
    Button(screen1,text="Register",width="10",height="1",command=register_user).pack()


def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)
    
    d=(username1,)
    inputData=(username1,password1)
    try:
        if (validateData(d,inputData)):
            login_success()
        else:
            login_failure()
    except IndexError:
        login_failure()
    

def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    screen2['bg']='orange'
    Label(screen2,text="Please enter details to login",bg="white",fg='black',width="300",height="2", font=("Calibri",13)).pack()
    Label(screen2,text="",bg='orange').pack()
    
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify=StringVar()
    password_verify=StringVar()
    
    Label(screen2,text="Username *",bg='orange').pack()
    username_entry1=Entry(screen2,textvariable=username_verify)
    username_entry1.pack()
    Label(screen2,text="",bg='orange').pack()
    Label(screen2,text="Password *",bg='orange').pack()
    password_entry1=Entry(screen2,textvariable=password_verify)
    password_entry1.pack()
    Label(screen2,text="",bg='orange').pack()
    Button(screen2,text="Login",width="10",height="1",command=login_verify).pack()

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Notes 2.0")
    screen['bg']='orange'
    Label(text="Notes 2.0",bg="white",fg='black',width="300",height="2", font=("Calibri",13)).pack()
    Label(text="",bg='orange').pack()
    Button(text="Login",width="30",height="2",command=login).pack()
    Label(text="",bg='orange').pack()
    Button(text="Register",width="30",height="2",command=register).pack()

    screen.mainloop()
	
main_screen()
