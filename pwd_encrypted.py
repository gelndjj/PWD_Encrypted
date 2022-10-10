
##############################################################################
##############################################################################
##  ______        ______     _____                             _           _##
##|  _ \ \      / /  _ \   | ____|_ __   ___ _ __ _   _ _ __ | |_ ___  __| |##
##| |_) \ \ /\ / /| | | |  |  _| | '_ \ / __| '__| | | | '_ \| __/ _ \/ _` |##
##|  __/ \ V  V / | |_| |  | |___| | | | (__| |  | |_| | |_) | ||  __/ (_| |##
##|_|     \_/\_/  |____/___|_____|_| |_|\___|_|   \__, | .__/ \__\___|\__,_|##
##                    |_____|                     |___/|_|                  ##
##############################################################################
##############################################################################

#from cgitb import text
#from curses.textpad import Textbox
from itertools import tee
from tkinter import ttk, filedialog, messagebox
from tkinter import *
from cryptography.fernet import Fernet

import random as r
import string as s
import os
import os.path 
import shutil

#CREATE A WINDOW
root = Tk()
root.geometry('600x400')
root.title('Password Generator')

#CREATE TABS
tabControl = ttk.Notebook(root)
tabControl.pack()

#FIRST TAB
tab0 = Frame(tabControl)
tab0.pack(fill='both')
tabControl.add(tab0,text='PWD Gen.')

#SECOND TAB
tab1 = Frame(tabControl)
tab1.pack(fill='both')
tabControl.add(tab1,text='Decode')
tabControl.pack(fill='both', expand=True)

#CREATE ALL THE LABELS PRESENT IN BOTH TAB
lbl_decoded_in = Entry(tab1,width=25,borderwidth=3, fg='green')
lbl_decoded_in.place(x=160,y=130)
lbl_decoded_in.insert(0,'')

lbl_decoded_out = Entry(tab1,width=25,borderwidth=3, fg='green')
lbl_decoded_out.place(x=160,y=170)
lbl_decoded_out.insert(0,'')

lbl_tab1 = Label(tab1,text='Paste your key in :').place(x=20,y=130)
lbl2_tab1 = Label(tab1,text='Password decoded :').place(x=20,y=170)

lbl_field_pass2 = Entry(tab0,width=15,borderwidth=3, bg='black', fg='yellow')
lbl_field_pass2.insert(0,'')
lbl_field_pass2.place(x=300, y=50)

lbl_pwd = Label(tab0,text='Your password :')
lbl_pwd.place(x=180,y=50)

lbl_field_pass = Label(tab0, text='Length :').place(x=40,y=50)

lbl_encoded = Entry(tab0,width=15, borderwidth=3, fg='grey')
lbl_encoded.place(x=380,y=130)
lbl_encoded.insert(0,'')

lbl_pwd_encoded = Label(tab0,text='Password encoded :')
lbl_pwd_encoded.place(x=240, y=130)

#CREATE A COMBOBOX (PASSWORD LENGTH)
combo_list = [
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '17',
            '18',
            '19',
            '20']

btn_combo_choice = ttk.Combobox(tab0, values=combo_list, width=3)
btn_combo_choice.set('0')
btn_combo_choice.place(x=110,y=50)

#CREATE THE CHECK BUTTONS FOR THE LETTERS, DIGITS AND SPECIAL CHARACTERS
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()

btn_digits = Checkbutton(tab0,text='Digits',width=15,variable=v1, onvalue=1, offvalue=0)
btn_digits.place(x=40, y=132)

btn_specials = Checkbutton(tab0,text='Specials',width=15,variable=v2, onvalue=1, offvalue=0)
btn_specials.place(x=40,y=172)

btn_letters = Checkbutton(tab0, text='Letters min/MAJ', width=15,variable=v3, state='disabled')
btn_letters.place(x=40, y=92)
btn_letters.select()

btn_count_digits = ttk.Combobox(tab0, values=combo_list, width=3)
btn_count_digits.set('0')
btn_count_digits.place(x=180, y=132)

btn_count_specials = ttk.Combobox(tab0, values=combo_list, width=3)
btn_count_specials.set('0')
btn_count_specials.place(x=180, y=172)

def pwd_gen():

    global lbl_pwd
    global btn_gen
    global lbl_field_pass2

    sample_1= s.ascii_letters 
    sample_2 = s.ascii_letters + s.digits
    sample_3 = s.ascii_letters + s.digits + s.punctuation
    sample_4 = s.ascii_letters + s.punctuation
    sample_01 = s.digits
    sample_02 = s.punctuation

    #MAKE A FANCY PASSWORD
    sample_digits = r.choices(sample_01,k=int(btn_count_digits.get()))
    sample_specials = r.choices(sample_02, k=int(btn_count_specials.get()))
    sample_letters = r.choices(sample_1,k=int(btn_combo_choice.get()) - int(btn_count_digits.get()) - int(btn_count_specials.get()))

    if v1.get() == 1 and v2.get() == 0:

        pwd_temp = r.choices(sample_1, k = int(btn_combo_choice.get()) - int(btn_count_digits.get()))
        pwd = ''.join(r.sample(pwd_temp + sample_digits, k=int(btn_combo_choice.get())))
        lbl_field_pass2 = Entry(tab0,width=15,borderwidth=3, bg='black', fg='yellow')
        lbl_field_pass2.insert(0,pwd)
        lbl_field_pass2.place(x=300, y=50)

    elif v1.get() == 1 and v2.get() == 1:

        pwd_temp = r.choices(sample_1, k = int(btn_combo_choice.get()) - int(btn_count_digits.get()) - int(btn_count_specials.get()))
        pwd = ''.join(r.sample(pwd_temp + sample_digits + sample_specials, k=int(btn_combo_choice.get())))
        lbl_field_pass2 = Entry(tab0,width=15,borderwidth=3, bg='black', fg='yellow')
        lbl_field_pass2.insert(0,pwd)
        lbl_field_pass2.place(x=300, y=50)

    elif v1.get() == 0 and v2.get() == 0:

        pwd_temp = r.choices(sample_1, k = int(btn_combo_choice.get()))
        pwd = ''.join(pwd_temp)
        lbl_field_pass2 = Entry(tab0,width=15,borderwidth=3, bg='black', fg='yellow')
        lbl_field_pass2.insert(0,pwd)
        lbl_field_pass2.place(x=300, y=50)

    else:

        pwd_temp = r.choices(sample_1, k = int(btn_combo_choice.get()) - int(btn_count_specials.get()))
        pwd = ''.join(r.sample(pwd_temp + sample_specials, k=int(btn_combo_choice.get())))
        lbl_field_pass2 = Entry(tab0,width=15,borderwidth=3, bg='black', fg='yellow')
        lbl_field_pass2.insert(0,pwd)
        lbl_field_pass2.place(x=270, y=20)

def gen_key_file():

    global btn_key
    global key_file

    file_located = os.path.expanduser('~/pass.key')
    file_exists = os.path.isfile(file_located)

    if file_exists == True:

        question = messagebox.askyesno(title='Already Present', message='A token is already present.\n\nDo you want to remove it ? ')

        if question == True:

            os.remove(file_located)
            msg00= messagebox.showinfo(title='File removed',message=file_located + '\nremoved')

    else:

        key = Fernet.generate_key()
        with open(os.path.expanduser('~/pass.key'),'wb') as key_file:
            key_file.write(key)
        btn_key['state'] = DISABLED
        msg = Label(tab0,text='TOKEN\'s path : ' + key_file.name)
        msg.configure(font=('Courier',12, 'italic'))
        msg.place(x=40, y=310)

    
def call_key():

    return open(os.path.expanduser('~/pass.key'),'rb').read()

def encode():

    global encoded
    global lbl_encoded

    try:

        lbl_encoded.delete(0,END)
        key = call_key()
        msg_to_encode = lbl_field_pass2.get().encode()
        a = Fernet(key)
        encoded = a.encrypt(msg_to_encode)
        lbl_encoded.insert(0,encoded)

    except:

        messagebox.showwarning(title=None, message='You must have a token to be able to encode/decode !!')

def decode():

    try:

        key = call_key()
        b = Fernet(key)
        decrypt = bytes(lbl_decoded_in.get(),'utf-8')
        decoded1 = b.decrypt(decrypt)
        decoded11 = decoded1.decode()
        lbl_decoded_out = Entry(tab1,width=25,borderwidth=3, fg='green')
        lbl_decoded_out.insert(0,decoded11)
        lbl_decoded_out.place(x=160,y=170)

    except:

        messagebox.showwarning(title=None, message='Bad token used or not found  !!')

def reset0():

    btn_count_digits.set('0')
    btn_count_specials.set('0')
    btn_combo_choice.set('0')

def showerror():

    messagebox.showerror(title='Error', message='Please, check off at least one option')

def erase_lbl():

    lbl_field_pass2.delete(0,END)

    try:

        lbl_encoded.delete(0,END)

    except:

        pass

def copy_txt():

    tab0.clipboard_clear()

    try:

        root.clipboard_append(lbl_encoded.get())
        btn_paste['state'] = NORMAL

    except:

        pass

def C():

    tab0.clipboard_clear()

    try:

        root.clipboard_append(lbl_field_pass2.get())

    except:

        pass

def paste_txt():

    lbl_decoded_in.delete(0,END)

    try:

        lbl_decoded_in.insert(0,tab0.clipboard_get())

    except:

        pass

def load():

    try:

        file_located = os.path.expanduser('~/pass.key')
        file_exists = os.path.isfile(file_located)

        if file_exists == True:

            question = messagebox.askyesnocancel(title='Already Present', message='A token is already present.\n\nDo you want to remove it ? ')
            
            if question == True:
                
                os.remove(file_located)
                msg01 = messagebox.showinfo(title='File removed', message=file_located + '\n has been removed')

        else:

            openup = filedialog.askopenfilename()
            file_x = open(openup,'rb')
            src_file_x = file_x.name
            dest_file_x = os.path.expanduser('~')
            shutil.copy2(src_file_x, dest_file_x)
            messagebox.showinfo(title='Succes', message='File loaded !!')
            message = Label(tab1, text=openup)
            message.place(x=170,y=17)

    except :

        pass

def load2():

        openup2 =  filedialog.askopenfile()
        lbl_decoded_in.insert(0,openup2.read())
        message = Label(tab1, text=openup2.name)
        message.place(x=215,y=57)

def saveas():

    nfile = filedialog.asksaveasfilename(filetypes=[('txt file','.txt')], defaultextension='.txt')
    file = open(nfile,'w')
    file.write(lbl_encoded.get())
    file.close()

def exit_soft():

    root.destroy()

#CREATE BUTTONS
btn_gen = Button(tab0,text='Generate', command=pwd_gen)
btn_gen.place(x=40,y=230)
btn_erase_lbl = Button(tab0, text='Clear',command=erase_lbl)
btn_erase_lbl.place(x=140,y=230)
btn_exit = Button(tab0,text='Exit',command=exit_soft)
btn_exit.place(x=40,y=270)
btn_reset0 = Button(tab0,text='Reset', command=reset0)
btn_reset0.place(x=220,y=230)
btn_encode = Button(tab0,text='Encode',fg='red', command=encode)
btn_encode.place(x=370,y=90)
btn_key = Button(tab0, text='Create a TOKEN',fg='black', command=gen_key_file)
btn_key.place(x=230,y=90)
btn_decode = Button(tab1,text='Decode',fg='green', command=decode)
btn_decode.place(x=240, y=210)
btn_exit2 = Button(tab1,text='Exit',command=exit_soft)
btn_exit2.place(x=255, y=240)
btn_C = Button(tab0,text='Copy', command=C)
btn_C.place(x=455,y=50)
btn_copy = Button(tab0, text='Copy', command=copy_txt, padx=5)
btn_copy.place(x=450, y=160)
btn_paste = Button(tab1, text='Paste', command=paste_txt)
btn_paste.place(x=410,y=130)
btn_load = Button(tab1,text='Load the TOKEN', command=load)
btn_load.place(x=20,y=15)
btn_load2 = Button(tab1,text='Load the ENCODED FILE', command=load2)
btn_load2.place(x=20,y=55)
btn_saveas = Button(tab0, text='Save the encoded pwd', command=saveas)
btn_saveas.place(x=350,y=190)

root.mainloop()

