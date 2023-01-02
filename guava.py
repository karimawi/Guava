import ctypes
import os
import threading
import time
import webbrowser
import easygui
import shutil
from tkinter import *
import pyperclip as ppc
from ahk import AHK
from AppOpener import give_appnames, run
from tinydb import Query, TinyDB
from tkextrafont import Font

configdb = TinyDB(r'data\settings.json', sort_keys=True, indent=4, separators=(',', ': '))
db = TinyDB(r'data\accounts.json', sort_keys=True, indent=4, separators=(',', ': '))
applist = list(give_appnames())

accounts = Query()


def centerwind(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def findapp(appname:str):
    appname = appname.replace(' ','')
    applist = list(give_appnames())
    strippedlist = str(applist).replace('[','').replace(']','').replace("'",'').replace(',','\n').replace(' ','')

    try:
        os.remove(r'data\apps.txt')
    except:
        pass

    with open(r'data\apps.txt','w') as apps:
        apps.write(strippedlist)
        apps.close()

    with open(r'data\apps.txt','r') as apps:
        finalapplist = apps.readlines()
        apps.close()

    ppc.copy(finalapplist[86])
    for i in range(len(finalapplist)):
        if finalapplist[i].replace('\n','') == appname:
            os.remove(r'data\apps.txt')
            return True

    os.remove(r'data\apps.txt')
    return False

root = Tk()
ahk = AHK()
root.geometry("401x501")
guavaicon = PhotoImage(file=r'assests\root\guavaicon18.png')
root.configure(bg='#2C2C2C')
root.title("Guava")
root.resizable(0,0)
root.iconphoto(True, guavaicon)
myappid = 'karimawi.guava.version.1.0' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
centerwind(root)

sidebar = Frame(root, width=73,height=501,bg="#1E1E1E")

#fonts

cwd = os.path.dirname(os.path.realpath(__file__))

font1 = Font(file=cwd+r'\assests\fonts\Nexa Bold.ttf', family="Nexa")
font2 = Font(file=cwd+r'\assests\fonts\Nexa Light.ttf', family="Nexa")
font3 = Font(file=cwd+r'\assests\fonts\Quicksand-Medium.ttf', family="Quicksand")
font4 = Font(file=cwd+r'\assests\fonts\Quicksand-SemiBold.ttf', family="Quicksand")

#fonts

#root assets
accountsicon = PhotoImage(file=r'assests\root\AccountsIcon.png')
addbtnicon = PhotoImage(file=r'assests\root\addbtn.png')
addbtniconactive = PhotoImage(file=r'assests\root\addactive.png')
removebtnicon = PhotoImage(file=r'assests\root\removebtn.png')
removebtniconactive = PhotoImage(file=r'assests\root\removeactive.png')
removebtndisabled = PhotoImage(file=r'assests\root\removedisabled.png')
editbtnicon = PhotoImage(file=r'assests\root\editbtn.png')
editbtniconactive = PhotoImage(file=r'assests\root\editactive.png')
editbtndisabled = PhotoImage(file=r'assests\root\editdisabled.png')
copybtnicon = PhotoImage(file=r'assests\root\copybtn.png')
copybtniconactive = PhotoImage(file=r'assests\root\copybtnhover.png')
copybtndisabled = PhotoImage(file=r'assests\root\copydisabled.png')
copybtnsuccess = PhotoImage(file=r'assests\root\copybtnsuccess.png')
infobtnicon = PhotoImage(file=r'assests\root\infobtn.png')
infobtniconactive = PhotoImage(file=r'assests\root\infoactive.png')
settingsbtnicon = PhotoImage(file=r'assests\root\settingsbtn.png')
settingsbtniconactive = PhotoImage(file=r'assests\root\settingsactive.png')
accountslabelbg = PhotoImage(file=r'assests\root\AccountsLabelBg.png')
lstbximg = PhotoImage(file=r'assests\root\lstboxbg.png')
lstbximgshort = PhotoImage(file=r'assests\root\lstboxbgshort.png')
mainwindnote = PhotoImage(file=r'assests\root\note.png')
mainwindnoteclose = PhotoImage(file=r'assests\root\closenote.png')
rednoteclose = PhotoImage(file=r'assests/root/redclosenote.png')
rednote = PhotoImage(file=r'assests/root/rednote.png')
counterbg10to99 = PhotoImage(file=r'assests/root/counter10to99+.png')
counterbg1to9 = PhotoImage(file=r'assests/root/counter1to9.png')
copyhoverlbl = PhotoImage(file=r'assests/root/copyhoverlbl.png')
edithoverlbl = PhotoImage(file=r'assests/root/edithoverlbl.png')
removehoverlbl = PhotoImage(file=r'assests/root/removehoverlbl.png')
addhoverlbl = PhotoImage(file=r'assests/root/addhoverlbl.png')
infohoverlbl = PhotoImage(file=r'assests/root/infohoverlbl.png')
settingshoverlbl = PhotoImage(file=r'assests/root/settingshoverlbl.png')
accountsiconbg = PhotoImage(file=r'assests\root\AccountsIconbg.png')
mp3path = r'assests/root/success.mp3'
errormp3path = r'assests\root\error.mp3'
notifmp3path = r'assests\root\notif.mp3'

#toplevel assets
cancelbtnicon = PhotoImage(file=r'assests\addwind\cancelbtn.png')
cancelbtnactive = PhotoImage(file=r'assests\addwind\cancelbtnactive.png')
submitbtnicon = PhotoImage(file=r'assests\addwind\submitbtn.png')
submitbtnactive = PhotoImage(file=r'assests\addwind\submitbtnactive.png')
eyeicon = PhotoImage(file=r'assests\addwind\hidepass.png')
crosseyeicon = PhotoImage(file=r'assests\addwind\showpass.png')
entrybgimg = PhotoImage(file=r'assests\addwind\entrybg.png')
entrylabelbgimg = PhotoImage(file=r'assests\addwind\entrylabelbg.png')
aboutbgimg = PhotoImage(file=r'assests\infowind\aboutbg.png')
scrolltrough = PhotoImage(file=r'assests\infowind\scrolltrough.png')
logosimg = PhotoImage(file=r'assests\infowind\logos.png')
flag = PhotoImage(file=r'assests\infowind\flag_EG.png')
socialsnversionbg = PhotoImage(file=r'assests/infowind/socialsnversionbg.png')
github = PhotoImage(file=r'assests/infowind/github.png')
githubhoverlabel = PhotoImage(file=r'assests/infowind/githubhoverlabel.png')
discord = PhotoImage(file=r'assests/infowind/discord.png')
discordhoverlabel = PhotoImage(file=r'assests/infowind/discordhoverlabel.png')
paypal = PhotoImage(file=r'assests/infowind/paypal.png')
paypalhoverlabel = PhotoImage(file=r'assests/infowind/paypalhoverlabel.png')

#settings assets
toggleon = PhotoImage(file=r'assests\settingswind\toggleon.png')
toggleoff = PhotoImage(file=r'assests\settingswind\toggleoff.png')
tabsgeneral = PhotoImage(file=r'assests\settingswind\tabsgeneral.png')
tabsdata = PhotoImage(file=r'assests\settingswind\tabsdata.png')
tabscopy = PhotoImage(file=r'assests\settingswind\tabscopy.png')
importlistboxbg = PhotoImage(file=r'assests\settingswind\importlistboxbg.png')
importhoverlbl = PhotoImage(file=r'assests\settingswind\importhoverlbl.png')
importhover = PhotoImage(file=r'assests\settingswind\importhover.png')
importbtn = PhotoImage(file=r'assests\settingswind\importbtn.png')
formattabplain = PhotoImage(file=r'assests\settingswind\formattabplain.png')
formattabdiscord = PhotoImage(file=r'assests\settingswind\formattabdiscord.png')
formattabcustom = PhotoImage(file=r'assests\settingswind\formattabcustom.png')
exporthoverlbl = PhotoImage(file=r'assests\settingswind\exporthoverlbl.png')
exporthover = PhotoImage(file=r'assests\settingswind\exporthover.png')
exportbtn = PhotoImage(file=r'assests\settingswind\exportbtn.png')
copyformatentrybg = PhotoImage(file=r'assests\settingswind\copyformatentrybg.png')
copybtnhoverlbl = PhotoImage(file=r'assests\settingswind\copybtnhoverlbl.png')
    #reused
# cancelbtnicon = PhotoImage(file=r'assests\addwind\cancelbtn.png')
# cancelbtnactive = PhotoImage(file=r'assests\addwind\cancelbtnactive.png')
# submitbtnicon = PhotoImage(file=r'assests\addwind\submitbtn.png')
# submitbtnactive = PhotoImage(file=r'assests\addwind\submitbtnactive.png')
# copybtnicon = PhotoImage(file=r'assests\root\copybtn.png')
# copybtniconactive = PhotoImage(file=r'assests\root\copybtnhover.png')
# copybtndisabled = PhotoImage(file=r'assests\root\copydisabled.png')
# copybtnsuccess = PhotoImage(file=r'assests\root\copybtnsuccess.png')

#msgb assets
errormsgb = PhotoImage(file=r'assests\msgb\errormsgb.png')
infomsgb = PhotoImage(file=r'assests\msgb\infomsgb.png')
msgbbtn = PhotoImage(file=r'assests\msgb\msgbbtn.png')

###commands

def msgb(title:str,type:str,msg:str,optionright:str,optionleft:str = None):

    msgbwind = Toplevel()
    msgbwind.grab_set()
    msgbwind.geometry("450x175")
    msgbwind.configure(bg='#2C2C2C')
    msgbwind.title(title)
    msgbwind.resizable(0,0)
    centerwind(msgbwind)

    msgbimg = Label(msgbwind,bg="#2C2C2C",borderwidth=0)

    if type == 'error':
        msgbimg.config(image=errormsgb)
        msgbimg.place(x=0,y=0)
        msgberrording = threading.Thread(target=ahk.sound_play, args=(errormp3path,))
        msgberrording.start()
    elif type == 'info':
        msgbimg.config(image=infomsgb)
        msgbimg.place(x=0,y=0)
        msgbding = threading.Thread(target=ahk.sound_play, args=(notifmp3path,))
        msgbding.start()
    
    def btn1click():
        msgbwind.destroy()
        return optionleft
    
    def btn2click():
        msgbwind.destroy()
        return optionright

    if optionleft == None:
        pass
    else:
        btn1 = Button(msgbwind,bg='#1E1E1E',fg='#C2C2C2'
        ,image=msgbbtn,borderwidth=0,activebackground='#1E1E1E'
        ,text=optionleft,font=('Nexa Bold',12),justify=CENTER
        ,activeforeground='#C2C2C2',command=btn1click,compound=CENTER).place(x=175,y=115)

    btn2 = Button(msgbwind,bg='#1E1E1E',fg='#C2C2C2',image=msgbbtn,borderwidth=0,activebackground='#1E1E1E'
    ,text=optionright,font=('Nexa Bold',12),justify=CENTER
    ,activeforeground='#C2C2C2',command=btn2click,compound=CENTER).place(x=310,y=115)

    msglbl = Label(msgbwind,bg="#2C2C2C",font=('Nexa Light', 10)
    ,text=msg,fg="#C2C2C2",wraplength=320,justify=LEFT).place(x=80,y=33)



def note(msg:str,color:str = 'yellow',timer:int = 5000):
    try:
        root.nametowidget('note1').destroy()
        root.nametowidget('noteclosebtn').destroy()
    except:
        pass
    
    if color == 'red':
        ncolor = rednote
        ncloseclr = rednoteclose
        bgcolor = '#C53131'
        fgcolor = '#C2C2C2'
        errording = threading.Thread(target=ahk.sound_play, args=(errormp3path,))
        errording.start()
    else:
        ncolor = mainwindnote
        ncloseclr = mainwindnoteclose
        bgcolor = '#B5C531'
        fgcolor = '#000000'
        notifding = threading.Thread(target=ahk.sound_play, args=(notifmp3path,))
        notifding.start()

    def endnote():
        note1.destroy()
        noteclosebtn.destroy()

        def destroy_note():
            lstbximglabel.config(image=lstbximg)
            lstbx.config(height= 14)

        root.after(500,destroy_note)
    

    lstbx.config(height= 12)

    lstbximglabel.config(image=lstbximgshort)
    note1 = Label(root,name='note1',bg="#2C2C2C",font=('Quicksand SemiBold', 9)
    ,justify=LEFT,image=ncolor,text=msg,fg=fgcolor,compound=CENTER)
    root.nametowidget('note1').place(x=105,y=422)
    noteclosebtn = Button(root,name='noteclosebtn',bg=bgcolor,image=ncloseclr
    ,borderwidth=0,activebackground=bgcolor,command=endnote)
    noteclosebtn.place(x=325,y=437)
 
    root.after(timer,endnote)

def addwind():
    addwindow = Toplevel()
    addwindow.grab_set()
    addwindow.geometry("394x290")
    addwindow.configure(bg='#2C2C2C')
    addwindow.title("Guava - Add an account")
    addwindow.resizable(0,0)
    centerwind(addwindow)

    #render entry boxes

        #name
    namelblbg = Label(addwindow,image=entrylabelbgimg,bg="#2C2C2C").place(x=28.5-7,y=20)
    nameentrybg = Label(addwindow,image=entrybgimg,bg="#1E1E1E").place(x=168.5-7,y=28.5)
    namelbl = Label(addwindow,bg="#1E1E1E",font=('Nexa Light', 11)
    ,text='Name',fg="#C2C2C2").place(x=43-7,y=36)

    name_var = StringVar()
    name_entry = Entry(addwindow,textvariable = name_var,show=None,font = ('Nexa Light',11)
    ,width=17,relief=FLAT,bg='#535353',fg='#C2C2C2',insertbackground='#C2C2C2')
    name_entry.place(x=175,y=37)
    name_entry.focus_set()

        #username
    usrnamelblbg = Label(addwindow,image=entrylabelbgimg,bg="#2C2C2C").place(x=28.5-7,y=20+65)
    usrnameentrybg = Label(addwindow,image=entrybgimg,bg="#1E1E1E").place(x=168.5-7,y=28.5+65)
    usrnamelbl = Label(addwindow,bg="#1E1E1E",font=('Nexa Light', 11)
    ,text='Username',fg="#C2C2C2").place(x=43-7,y=36+65)

    usrname_var = StringVar()
    usrname_entry = Entry(addwindow,textvariable = usrname_var,show=None,font = ('Nexa Light',11)
    ,width=17,relief=FLAT,bg='#535353',fg='#C2C2C2',insertbackground='#C2C2C2')
    usrname_entry.place(x=175,y=102)

        #password
    passwlblbg = Label(addwindow,image=entrylabelbgimg,bg="#2C2C2C").place(x=28.5-7,y=20+130)
    passwentrybg = Label(addwindow,image=entrybgimg,bg="#1E1E1E").place(x=168.5-7,y=28.5+130)
    passwlbl = Label(addwindow,bg="#1E1E1E",font=('Nexa Light', 11)
    ,text='Password',fg="#C2C2C2").place(x=43-7,y=36+130)

    passw_var = StringVar()
    passw_entry = Entry(addwindow,textvariable = passw_var,font = ('Nexa Light',11)
    ,width=15,relief=FLAT,bg='#535353',fg='#C2C2C2',insertbackground='#C2C2C2')
    passw_entry.place(x=175,y=167)

    def pass_setting():
        
        def showpass():
            configdb.upsert({'always_showpass':'true'}, Query().always_showpass.exists())
            eyebtn.config(image=eyeicon,command=hidepass)
            passw_entry.config(show='')
            addwindow.update()
        
        def hidepass():
            configdb.upsert({'always_showpass':'false'}, Query().always_showpass.exists())
            eyebtn.config(image=crosseyeicon,command=showpass)
            passw_entry.config(show='•')
            addwindow.update()

        if configdb.contains(Query().always_showpass == 'true') == True:
            passw_entry.config(show='')
            eyebtn = Button(addwindow,image=eyeicon,bg="#535353",borderwidth=0
            ,activebackground="#535353",command=hidepass,relief=FLAT)
            addwindow.update()
        else:
            passw_entry.config(show='•')
            eyebtn = Button(addwindow,image=crosseyeicon,bg="#535353",borderwidth=0
            ,activebackground="#535353",command=showpass,relief=FLAT)
            addwindow.update()
        
        eyebtn.place(x=334,y=168)

    pass_setting()

    def submit():
        name = name_var.get()
        username = usrname_var.get()
        password = passw_var.get()

        def empty():

            if name == '' and username == '' and password == '':
                return '"Name", "Username" and "Password"'
            elif name == '' and username == '':
                return '"Name" & "Username"'
            elif name == '' and password == '':
                return '"Name" & "Password"'
            elif username == '' and password == '':
                return '"Username" & "Password"'
            elif name == '':
                return '"Name"'
            elif username == '':
                return '"Username"'
            elif password == '':
                return '"Password"'

        
        if name == '' or username == '' or password == '':
            msg1 = "{} Can't be empty".format(empty())
            msgb(title="Guava - Invalid Credentials",type='error',msg=msg1,optionright='Ok')
        else:
            for item in db:
                if item['name'] == name:
                    msg2 = 'There\'s already an account with the name "{}", please choose another name or delete the existing one.'.format(name)
                    msgb(title="Guava - Invalid Name",msg=msg2,type='error',optionright='Ok')
                    break
                elif item['username'] == username:
                    msg3 = 'There\'s already an account with the username "{}" added as "{}", please use that to login, or use the edit function if you want to change the stored password.'.format(username,item['name'])
                    msgb(title="Guava - Account already added",msg=msg3,type='error',optionright='Ok')
                    addwindow.destroy()
                    notemsg = 'Operation Canceled!'
                    note(notemsg)
                    break
            else:
                db.insert({'name':name,'username':username,'password':password})
                addwindow.destroy()
                notemsg = 'Account added successfully!'
                note(notemsg)
        fetch()

        return
        
    def enterkey(event):
    
        if addwindow.focus_get() == name_entry:
            usrname_entry.focus_set()
        elif addwindow.focus_get() == usrname_entry:
            passw_entry.focus_set()
        elif addwindow.focus_get() == passw_entry:
            submit()
    
    addwindow.bind('<Return>', enterkey)

    submit_btn = Button(addwindow,image=submitbtnicon,bg="#2C2C2C",borderwidth=0
            ,activebackground="#2C2C2C",command=submit,relief=FLAT)

    def submit_btn_hover(event):
        submit_btn.config(image=submitbtnactive)
    
    def submit_btn_unhover(event):
        submit_btn.config(image=submitbtnicon)
    
    submit_btn.bind('<Enter>',submit_btn_hover)
    submit_btn.bind('<Leave>',submit_btn_unhover)

    submit_btn.place(x=334,y=220)

    def cancel():
        addwindow.destroy()
        notemsg = 'Operation Canceled!'
        note(notemsg)
    
    cancel_btn = Button(addwindow,image=cancelbtnicon,bg="#2C2C2C",borderwidth=0
        ,activebackground="#2C2C2C",command=cancel,relief=FLAT)

    def cancel_btn_hover(event):
        cancel_btn.config(image=cancelbtnactive)
    
    def cancel_btn_unhover(event):
        cancel_btn.config(image=cancelbtnicon)
    
    cancel_btn.bind('<Enter>',cancel_btn_hover)
    cancel_btn.bind('<Leave>',cancel_btn_unhover)

    cancel_btn.place(x=300,y=230)

def editwind():
    if lstbx.size() == 0:
        return
    else:
        if lstbx.curselection() == ():
            note('Select an account first!','red')
            return
        else:
            selectindex = lstbx.curselection()[0]
            editname = lstbx.get(selectindex,last=None)
            account = db.get(accounts.name == editname)
            if account['name'] == editname:
                oldname = account['name']
                oldusername = account['username']
                oldpassw = account['password']
                acc_doc_id = account.doc_id
            else:
                print('Account not found in db')
                return

    editwindow = Toplevel()
    editwindow.grab_set()
    editwindow.geometry("394x290")
    editwindow.configure(bg='#2C2C2C')
    editwindow.title('Guava - Editing "{}"'.format(oldname))
    editwindow.resizable(0,0)
    centerwind(editwindow)

    #render entry boxes

        #name
    namelblbg = Label(editwindow,image=entrylabelbgimg,bg="#2C2C2C").place(x=28.5-7,y=20)
    nameentrybg = Label(editwindow,image=entrybgimg,bg="#1E1E1E").place(x=168.5-7,y=28.5)
    namelbl = Label(editwindow,bg="#1E1E1E",font=('Nexa Light', 11)
    ,text='Name',fg="#C2C2C2").place(x=43-7,y=36)

    name_var = StringVar()
    name_entry = Entry(editwindow,textvariable = name_var,show=None,font = ('Nexa Light',11)
    ,width=17,relief=FLAT,bg='#535353',fg='#C2C2C2',insertbackground='#C2C2C2')
    name_entry.insert(0,oldname)
    name_entry.place(x=175,y=37)
    name_entry.focus_set()

        #username
    usrnamelblbg = Label(editwindow,image=entrylabelbgimg,bg="#2C2C2C").place(x=28.5-7,y=20+65)
    usrnameentrybg = Label(editwindow,image=entrybgimg,bg="#1E1E1E").place(x=168.5-7,y=28.5+65)
    usrnamelbl = Label(editwindow,bg="#1E1E1E",font=('Nexa Light', 11)
    ,text='Username',fg="#C2C2C2").place(x=43-7,y=36+65)

    usrname_var = StringVar()
    usrname_entry = Entry(editwindow,textvariable = usrname_var,show=None,font = ('Nexa Light',11)
    ,width=17,relief=FLAT,bg='#535353',fg='#C2C2C2',insertbackground='#C2C2C2')
    usrname_entry.insert(0,oldusername)
    usrname_entry.place(x=175,y=102)

        #password
    passwlblbg = Label(editwindow,image=entrylabelbgimg,bg="#2C2C2C").place(x=28.5-7,y=20+130)
    passwentrybg = Label(editwindow,image=entrybgimg,bg="#1E1E1E").place(x=168.5-7,y=28.5+130)
    passwlbl = Label(editwindow,bg="#1E1E1E",font=('Nexa Light', 11)
    ,text='Password',fg="#C2C2C2").place(x=43-7,y=36+130)

    passw_var = StringVar()
    passw_entry = Entry(editwindow,textvariable = passw_var,font = ('Nexa Light',11)
    ,width=15,relief=FLAT,bg='#535353',fg='#C2C2C2',insertbackground='#C2C2C2')
    passw_entry.insert(0,oldpassw)
    passw_entry.place(x=175,y=167)

    def pass_setting():
        
        def showpass():
            configdb.upsert({'always_showpass':'true'}, Query().always_showpass.exists())
            eyebtn.config(image=eyeicon,command=hidepass)
            passw_entry.config(show='')
            editwindow.update()
        
        def hidepass():
            configdb.upsert({'always_showpass':'false'}, Query().always_showpass.exists())
            eyebtn.config(image=crosseyeicon,command=showpass)
            passw_entry.config(show='•')
            editwindow.update()

        if configdb.contains(Query().always_showpass == 'true') == True:
            passw_entry.config(show='')
            eyebtn = Button(editwindow,image=eyeicon,bg="#535353",borderwidth=0
            ,activebackground="#535353",command=hidepass,relief=FLAT)
            editwindow.update()
        else:
            passw_entry.config(show='•')
            eyebtn = Button(editwindow,image=crosseyeicon,bg="#535353",borderwidth=0
            ,activebackground="#535353",command=showpass,relief=FLAT)
            editwindow.update()
        
        eyebtn.place(x=334,y=168)

    pass_setting()

    def submit():
        name = name_var.get()
        username = usrname_var.get()
        password = passw_var.get()

        def empty():

            if name == '' and username == '' and password == '':
                return '"Name", "Username" and "Password"'
            elif name == '' and username == '':
                return '"Name" & "Username"'
            elif name == '' and password == '':
                return '"Name" & "Password"'
            elif username == '' and password == '':
                return '"Username" & "Password"'
            elif name == '':
                return '"Name"'
            elif username == '':
                return '"Username"'
            elif password == '':
                return '"Password"'

        
        if name == '' or username == '' or password == '':
            msg1 = "{} Can't be empty".format(empty())
            msgb(title="Guava - Invalid Credentials",msg=msg1,type='error',optionright='Ok')
        elif name == oldname and username == oldusername and password == oldpassw:
            editwindow.destroy()
            notemsg = 'Operation Canceled!'
            note(notemsg)
        else:
            db.update({'name':name,'username':username,'password':password},doc_ids = [acc_doc_id])
            editwindow.destroy()
            notemsg = 'Account edited successfully!'
            note(notemsg)
        fetch()

        return
        
    def enterkey(event):

        if editwindow.focus_get() == name_entry:
            usrname_entry.focus_set()
        elif editwindow.focus_get() == usrname_entry:
            passw_entry.focus_set()
        elif editwindow.focus_get() == passw_entry:
            submit()

    editwindow.bind('<Return>', enterkey)

    submit_btn = Button(editwindow,image=submitbtnicon,bg="#2C2C2C",borderwidth=0
            ,activebackground="#2C2C2C",command=submit,relief=FLAT)

    def submit_btn_hover(event):
        submit_btn.config(image=submitbtnactive)

    def submit_btn_unhover(event):
        submit_btn.config(image=submitbtnicon)

    submit_btn.bind('<Enter>',submit_btn_hover)
    submit_btn.bind('<Leave>',submit_btn_unhover)

    submit_btn.place(x=334,y=220)

    def cancel():
        editwindow.destroy()
        notemsg = 'Operation Canceled!'
        note(notemsg)

    cancel_btn = Button(editwindow,image=cancelbtnicon,bg="#2C2C2C",borderwidth=0
        ,activebackground="#2C2C2C",command=cancel,relief=FLAT)

    def cancel_btn_hover(event):
        cancel_btn.config(image=cancelbtnactive)

    def cancel_btn_unhover(event):
        cancel_btn.config(image=cancelbtnicon)

    cancel_btn.bind('<Enter>',cancel_btn_hover)
    cancel_btn.bind('<Leave>',cancel_btn_unhover)

    cancel_btn.place(x=300,y=230)
    return

def remove():
    if lstbx.size() == 0:
        return
    else:
        if lstbx.curselection() == ():
            note('Select an account first!','red')
            return
        else:
            selectindex = lstbx.curselection()[0]
            delname = lstbx.get(selectindex,last=None)
            for item in db:
                if item['name'] == delname:
                    msg4 = 'Are you sure you want to delete "{}", this action cannot be reverted.'.format(delname)
                    
                    msgbwind = Toplevel()
                    msgbwind.grab_set()
                    msgbwind.geometry("450x175")
                    msgbwind.configure(bg='#2C2C2C')
                    msgbwind.title('Guava - Delete Confirmation')
                    msgbwind.resizable(0,0)
                    centerwind(msgbwind)

                    msgbimg = Label(msgbwind,bg="#2C2C2C",borderwidth=0)
                    msgbimg.config(image=infomsgb)
                    msgbimg.place(x=0,y=0)
                    msgbding = threading.Thread(target=ahk.sound_play, args=(notifmp3path,))
                    msgbding.start()
                    
                    def btn1click():
                        db.remove(accounts.name == delname)
                        fetch()
                        notemsg = 'Account removed successfully!'
                        note(notemsg)
                        msgbwind.destroy()
                    
                    def btn2click():
                        notemsg = 'Operation Canceled!'
                        note(notemsg)

                    btn1 = Button(msgbwind,bg='#1E1E1E',fg='#C2C2C2'
                    ,image=msgbbtn,borderwidth=0,activebackground='#1E1E1E'
                    ,text='Yes',font=('Nexa Bold',12),justify=CENTER
                    ,activeforeground='#C2C2C2',command=btn1click,compound=CENTER).place(x=175,y=115)

                    btn2 = Button(msgbwind,bg='#1E1E1E',fg='#C2C2C2',image=msgbbtn,borderwidth=0,activebackground='#1E1E1E'
                    ,text='No',font=('Nexa Bold',12),justify=CENTER
                    ,activeforeground='#C2C2C2',command=btn2click,compound=CENTER).place(x=310,y=115)

                    msglbl = Label(msgbwind,bg="#2C2C2C",font=('Nexa Light', 10)
                    ,text=msg4,fg="#C2C2C2",wraplength=320,justify=LEFT).place(x=80,y=33)

def openurl(site:str):
    if site == 'github':
        webbrowser.open('https://github.com/karimawii/Guava', new=0, autoraise=True)
    elif site == 'paypal':
        webbrowser.open('https://paypal.me/karimawi', new=0, autoraise=True)
    elif site == 'discord':
        if findapp('discord') == True:
            disurl = 'discord://'
        else:
            disurl = ''
        webbrowser.open(disurl+'https://discord.com/users/609230785769111554', new=0, autoraise=True)
    return

def info():

    infowindow = Toplevel()
    infowindow.grab_set()
    infowindow.geometry("394x411")
    infowindow.configure(bg='#2C2C2C')
    infowindow.title("Guava - Info")
    infowindow.resizable(0,0)
    centerwind(infowindow)

    #socials
    socialsbglbl = Label(infowindow,image=socialsnversionbg,bg='#2C2C2C',borderwidth=0).place(x=31,y=345)

        #github
    def github_hover(event):
        githublbl.place(x=27,y=322)
    
    def github_unhover(event):
        githublbl.place_forget()

    githubbtn = Button(infowindow,image=github,bg='#1E1E1E',borderwidth=0,activebackground='#1E1E1E'
    ,command=lambda: openurl('github'))
    githublbl = Label(infowindow,image=githubhoverlabel,bg='#2C2C2C',borderwidth=0)
    githubbtn.bind('<Enter>',github_hover)
    githubbtn.bind('<Leave>',github_unhover)
    githubbtn.place(x=51-7,y=351)
        #github
    
        #paypal
    def paypal_hover(event):
        paypallbl.place(x=67,y=322)
    
    def paypal_unhover(event):
        paypallbl.place_forget()

    paypalbtn = Button(infowindow,image=paypal,bg='#1E1E1E',borderwidth=0,activebackground='#1E1E1E'
    ,command=lambda: openurl('paypal'))
    paypallbl = Label(infowindow,image=paypalhoverlabel,bg='#2C2C2C',borderwidth=0)
    paypalbtn.bind('<Enter>',paypal_hover)
    paypalbtn.bind('<Leave>',paypal_unhover)
    paypalbtn.place(x=91-7,y=351)
        #paypal

        #discord
    def discord_hover(event):
        discordlbl.place(x=107,y=322)
    
    def discord_unhover(event):
        discordlbl.place_forget()

    discordbtn = Button(infowindow,image=discord,bg='#1E1E1E',borderwidth=0,activebackground='#1E1E1E'
    ,command=lambda: openurl('discord'))
    discordlbl = Label(infowindow,image=discordhoverlabel,bg='#2C2C2C',borderwidth=0)
    discordbtn.bind('<Enter>',discord_hover)
    discordbtn.bind('<Leave>',discord_unhover)
    discordbtn.place(x=131-7,y=353)
        #discord

        #version
    versionlbl = Label(infowindow,bg="#1E1E1E",font=('Nexa Light',11),text='v1.0.0 - Beta',justify=CENTER,fg="#C2C2C2")
    versionlbl.place(x=240,y=351.5)
    #socials

    #flag
    flaglbl = Label(infowindow,image=flag,bg='#2C2C2C',borderwidth=0).place(x=167,y=311)

    y_offset = 40
    aboutframe = Frame(infowindow,width=307,height=205,bg='#1E1E1E',relief=SUNKEN,borderwidth=0)
    aboutbg = Label(infowindow,image=aboutbgimg,bg='#2C2C2C',borderwidth=0).place(x=31,y=40+y_offset)
    aboutframe.place(x=45,y=55+y_offset)
    aboutframe.lift()

    logosframe = Frame(infowindow,width=327,height=57,bg='#1E1E1E',relief=SUNKEN,borderwidth=0)
    logosframe.place(x=32,y=15)
    logos = Label(logosframe,image=logosimg,bg='#2C2C2C',width=327,height=57).place(x=0,y=0)

    def trough_link(event):
        # print(v.get()[0])
        y_add = v.get()[0]*275.5555555555555
        trough.place_configure(x=349,y=50+y_offset+y_add)
        return
    
    v=Scrollbar(aboutframe, orient='vertical',activebackground='#1E1E1E',bg='#1E1E1E',bd=0
    ,highlightbackground='#1E1E1E',highlightcolor='#1E1E1E'
    ,troughcolor='#1E1E1E',width=0,relief=FLAT,
    highlightthickness=0,elementborderwidth=0,command=trough_link)
    v.place(x=1000,y=0)
    v.lower()

    trough = Label(infowindow,image=scrolltrough,bg='#1E1E1E',name='trough')
    trough.place(x=349,y=50+y_offset)

    
    about=Text(aboutframe, font=("Nexa Light",10), yscrollcommand=v.set
    ,width=37,height=13,selectbackground='#1E1E1E',selectforeground='#C2C2C2'
    ,bg='#1E1E1E',fg='#C2C2C2',wrap=WORD,borderwidth=0,relief=FLAT)

    about.tag_configure("about_tag", justify='center')

    
    mytext = "Hey, my name is Karim, the developer of Guava and I'm from Egypt.\n\nI created this project because.. well I play League of Legends but also, I wanted to git gud in coding as well, I may be good at creating modern UI designs and styling stuff, but when it comes to coding my code used to come out not so pretty.\n\nSo I started looking for projects I can do that can heavily challenge my abilities and at the same time be something that I’m passionate about so I don’t quit (lmao).\n\nThat’s why I started developing guava, we were learning Tkinter in the Python course in college, so I wondered what else can I do with it, turns out, not much in today’s standards, since this library is so old, it looks kinda crap, but it has so much funcion in it and I could very well feel the potential, I wanted to push it to the limits, and design a GUI that looks modern and functions well, that’s where Guava came to my mind.\n\nBtw don’t ask me why I named it Guava, idk, I just like the fruit, maybe cause it has a lot of seeds in it just like the switcher can contain a lot of accounts (wow so dumb), I really have no idea, I also love yellow so why not.\n"
    about.insert(END, mytext)
    about.config(state='disabled',cursor='')

    
    v.config(command=about.yview)
    about.tag_add("about_tag", "1.0", "end")
    about.place(x=0,y=0)
    about.lift()
    about.bind('<MouseWheel>',trough_link)


    return

def copy():
    if lstbx.size() == 0:
        return
    else:
        if lstbx.curselection() == ():
            note('Select an account first!','red')
            return
        else:
            selectindex = lstbx.curselection()[0]
            copyname = lstbx.get(selectindex,last=None)
            copyaccount = db.get(accounts.name == copyname)
            copyname = copyaccount['name']
            copyusrname = copyaccount['username']
            copypassw = copyaccount['password']
            
            discordform = '```\nUsername: {}\nPassword: {}\n```'.format(copyusrname,copypassw)
            ppc.copy(discordform)

            copybtn.unbind('<Enter>')
            copybtn.unbind('<Leave>')
            copybtn.config(image=copybtnsuccess)

            ding = threading.Thread(target=ahk.sound_play, args=(mp3path,))
            ding.start()
            copylbl.place_forget()

            def returncopy():
                copybtn.config(image=copybtnicon)
                copybtn.bind('<Enter>',copybtn_onEnter)
                copybtn.bind('<Leave>',copybtn_onLeave)
                return

            root.after(2500,returncopy)
            

    return

def settings():

    settwindow = Toplevel()
    settwindow.grab_set()
    settwindow.geometry("360x336")
    settwindow.configure(bg='#2C2C2C')
    settwindow.title("Guava - Settings")
    settwindow.resizable(0,0)
    centerwind(settwindow)

    
    #GENERAL
    def generaltab():
        for i in range(1,15):
            try:
                settwindow.nametowidget('datatab'+str(i)).destroy()
                settwindow.nametowidget('datatab'+str(i)).destroy()
            except:
                pass

        for i in range(1,15):
            try:
                settwindow.nametowidget('copytab'+str(i)).destroy()
                settwindow.nametowidget('copytab'+str(i)).destroy()
            except:
                pass

        SettTabs.config(image=tabsgeneral)
        Gtab_btn.config(bg='#1E1E1E',activebackground='#1E1E1E')
        Dtab_btn.config(bg='#535353',activebackground='#535353')
        Ctab_btn.config(bg='#535353',activebackground='#535353')

        #name widgets

        def toggle_check():
            if configdb.contains(Query().disable_startup_msg == 'true') == True:
                DSMtog.config(image=toggleon)
            else:
                DSMtog.config(image=toggleoff)
            
            if configdb.contains(Query().always_showpass == 'true') == True:
                ALStog.config(image=toggleon)
            else:
                ALStog.config(image=toggleoff)
            
            if configdb.contains(Query().exit_after_login == 'true') == True:
                EALtog.config(image=toggleon)
            else:
                EALtog.config(image=toggleoff)
        
        def toggle_tog(togname:str):

            if togname == 'DSM':
                if configdb.contains(Query().disable_startup_msg == 'true') == True:
                    configdb.upsert({'disable_startup_msg':'false'}, Query().disable_startup_msg.exists())
                else:
                    configdb.upsert({'disable_startup_msg':'true'}, Query().disable_startup_msg.exists())

            elif togname == 'ALS':
                if configdb.contains(Query().always_showpass == 'true') == True:
                    configdb.upsert({'always_showpass':'false'}, Query().always_showpass.exists())
                else:
                    configdb.upsert({'always_showpass':'true'}, Query().always_showpass.exists())
            
            elif togname == 'EAL':
                if configdb.contains(Query().exit_after_login == 'true') == True:
                    configdb.upsert({'exit_after_login':'false'}, Query().exit_after_login.exists())
                else:
                    configdb.upsert({'exit_after_login':'true'}, Query().exit_after_login.exists())
            
            toggle_check()


        DSMtog = Button(settwindow,name='generaltab1',bg='#1E1E1E',borderwidth=0,activebackground='#1E1E1E'
        ,activeforeground='#1E1E1E',command=lambda: toggle_tog('DSM'))
        DSMlbl = Label(settwindow,name='generaltab2',text='Disable Startup Message'
        ,font=('Nexa Light',11),justify=LEFT,bg='#1E1E1E',fg='#C2C2C2').place(x=30,y=63)
        DSMdesclbl = Label(settwindow,name='generaltab3',text='disables the “Double click to login” message\nthat appears when Guava starts'
        ,font=('Nexa Bold',7),justify=LEFT,bg='#1E1E1E',fg='#535353').place(x=30,y=85)

        ALStog = Button(settwindow,name='generaltab4',bg='#1E1E1E',borderwidth=0,activebackground='#1E1E1E'
        ,activeforeground='#1E1E1E',command=lambda: toggle_tog('ALS'))
        ALSlbl = Label(settwindow,name='generaltab5',text='Always Show Passwords'
        ,font=('Nexa Light',11),justify=LEFT,bg='#1E1E1E',fg='#C2C2C2').place(x=30,y=63+90)
        ALSdesclbl = Label(settwindow,name='generaltab6',text='will always show passwords when editing or\nadding accounts, this is also linked to the “eye”\nicon on both pop-ups'
        ,font=('Nexa Bold',7),justify=LEFT,bg='#1E1E1E',fg='#535353').place(x=30,y=85+90)

        EALtog = Button(settwindow,name='generaltab7',bg='#1E1E1E',borderwidth=0,activebackground='#1E1E1E'
        ,activeforeground='#1E1E1E',command=lambda: toggle_tog('EAL'))
        EALlbl = Label(settwindow,name='generaltab8',text='Close After Login'
        ,font=('Nexa Light',11),justify=LEFT,bg='#1E1E1E',fg='#C2C2C2').place(x=30,y=63+90+95)
        EALdesclbl = Label(settwindow,name='generaltab9',text='will close Guava after the login is successful'
        ,font=('Nexa Bold',7),justify=LEFT,bg='#1E1E1E',fg='#535353').place(x=30,y=85+90+95)

        toggle_check()

        DSMtog.place(x=280,y=0+30+30+20)
        ALStog.place(x=280,y=20+130+20)
        EALtog.place(x=280,y=40+230-30+20)
        

    #DATA
    def datatab():
        for i in range(1,15):
            try:
                settwindow.nametowidget('generaltab'+str(i)).destroy()
                settwindow.nametowidget('generaltab'+str(i)).destroy()
            except:
                pass

        for i in range(1,15):
            try:
                settwindow.nametowidget('copytab'+str(i)).destroy()
                settwindow.nametowidget('copytab'+str(i)).destroy()
            except:
                pass

        SettTabs.config(image=tabsdata)
        Dtab_btn.config(bg='#1E1E1E',activebackground='#1E1E1E')
        Gtab_btn.config(bg='#535353',activebackground='#535353')
        Ctab_btn.config(bg='#535353',activebackground='#535353')

        #name widgets
        
        def importfunc():
            settwindow.withdraw()
            root.withdraw()
            restorefilepath = easygui.fileopenbox(title='Guava - Choose Restore File',default='C:\\*.json',filetypes='*.json')
            root.deiconify()
            root.lift()
            settwindow.deiconify()
            settwindow.lift()
            
            if restorefilepath == None:
                return
            else:
                importdb = TinyDB(restorefilepath, sort_keys=True, indent=4, separators=(',', ': '))

                importlstbx = Listbox(settwindow,name='datatab10',bg = "#535353", font =('Nexa Light',9),justify=CENTER
                ,fg="black",highlightthickness=0,selectmode=SINGLE,width = 35
                ,height= 10,activestyle=NONE,borderwidth=0,border=0,relief=FLAT
                ,selectborderwidth=0,disabledforeground='#C2C2C2')

                importlstbx.delete(0,END)
                impcurrentsize = 0

                for item in importdb:
                    impcurrentsize += 1
                    importlstbx.insert(0,item['name'])        
                
                if impcurrentsize == 0:
                    settwindow.destroy()
                    note('Invalid JSON Format')
                    return

                else:
                    def finalimport():
                        msg4 = 'PLEASE EXPORT YOU CURRENT LIST FIRST!\nDo you want to add {} accounts to your existing list, or do you want to completely replace your list with this list'.format(impcurrentsize)
                        
                        msgbwind = Toplevel()
                        msgbwind.grab_set()
                        msgbwind.geometry("450x175")
                        msgbwind.configure(bg='#2C2C2C')
                        msgbwind.title('Guava - Import Confirmation')
                        msgbwind.resizable(0,0)
                        centerwind(msgbwind)

                        msgbimg = Label(msgbwind,bg="#2C2C2C",borderwidth=0)
                        msgbimg.config(image=infomsgb)
                        msgbimg.place(x=0,y=0)
                        msgbding = threading.Thread(target=ahk.sound_play, args=(notifmp3path,))
                        msgbding.start()
                        
                        def btn1click():
                            failedaccs = 0
                            for item in importdb:
                                try:
                                    dupname = db.get(accounts.name == item['name'])
                                except:
                                    dupname = None
                                    pass

                                try:
                                    dupusrname = db.get(accounts.username == item['username'])
                                    if dupusrname['username'] == item['username']:
                                        failedaccs += 1
                                except:
                                    dupusrname = None
                                    pass

                                if dupname != None and dupusrname == None:
                                    importname = item['name']+'(1)'
                                    importusrname = item['username']
                                    importpassw = item['password']

                                    db.insert({'name':importname,'username':importusrname,'password':importpassw})

                                elif dupname == None and dupusrname == None:
                                    importname = item['name']
                                    importusrname = item['username']
                                    importpassw = item['password']

                                    db.insert({'name':importname,'username':importusrname,'password':importpassw})

                            if failedaccs == 0:
                                notemsg = '{} accounts added successfully!'.format(impcurrentsize)
                                note(notemsg)
                                msgbwind.destroy()
                                settwindow.destroy()
                            elif failedaccs > 0:
                                msgbmsg = '{} accounts were imported, {} failed to import due to them having the same username as ones from the existing list'.format(impcurrentsize-failedaccs,failedaccs)
                                msgb(type='info',msg=msgbmsg,title='Guava - Import Completed!',optionright='Ok')
                                msgbwind.destroy()
                                settwindow.destroy()
                            msgbwind.destroy()

                            fetch()
                        
                        def btn2click():
                            shutil.copyfile(restorefilepath,r'data\accounts.json')
                            notemsg = 'Accounts replaced successfully!'
                            note(notemsg)
                            msgbwind.destroy()
                            settwindow.destroy()
                            fetch()

                        btn1 = Button(msgbwind,bg='#1E1E1E',fg='#C2C2C2'
                        ,image=msgbbtn,borderwidth=0,activebackground='#1E1E1E'
                        ,text='Add',font=('Nexa Bold',12),justify=CENTER
                        ,activeforeground='#C2C2C2',command=btn1click,compound=CENTER).place(x=175,y=115)

                        btn2 = Button(msgbwind,bg='#1E1E1E',fg='#C2C2C2',image=msgbbtn,borderwidth=0,activebackground='#1E1E1E'
                        ,text='Replace',font=('Nexa Bold',12),justify=CENTER
                        ,activeforeground='#C2C2C2',command=btn2click,compound=CENTER).place(x=310,y=115)

                        msglbl = Label(msgbwind,bg="#2C2C2C",font=('Nexa Light', 10)
                        ,text=msg4,fg="#C2C2C2",wraplength=320,justify=LEFT).place(x=80,y=30)
                    
                    def cancel():
                        settwindow.destroy()
                        notemsg = 'Operation Canceled!'
                        note(notemsg)
                
                    cancel_btn = Button(settwindow,name='datatab9',image=cancelbtnicon,bg="#1E1E1E",borderwidth=0
                        ,activebackground="#1E1E1E",command=cancel,relief=FLAT)

                    def cancel_btn_hover(event):
                        cancel_btn.config(image=cancelbtnactive)
                    
                    def cancel_btn_unhover(event):
                        cancel_btn.config(image=cancelbtnicon)
                    
                    cancel_btn.bind('<Enter>',cancel_btn_hover)
                    cancel_btn.bind('<Leave>',cancel_btn_unhover)

                    cancel_btn.place(x=140+100,y=261)

                    submimport_btn = Button(settwindow,name='datatab8',image=submitbtnicon,bg="#1E1E1E",borderwidth=0
                    ,activebackground="#1E1E1E",command=finalimport,relief=FLAT)

                    def submimport_btn_hover(event):
                        submimport_btn.config(image=submitbtnactive)
                    
                    def submimport_btn_unhover(event):
                        submimport_btn.config(image=submitbtnicon)
                    
                    submimport_btn.bind('<Enter>',submimport_btn_hover)
                    submimport_btn.bind('<Leave>',submimport_btn_unhover)

                    submimport_btn.place(x=170+100,y=250.5)

                
                importlstbx.config(state=DISABLED)
                importlstbx.place(x=40,y=65)

        def exportfunc():
            settwindow.withdraw()
            root.withdraw()
            backupdirpath = easygui.diropenbox(title='Guava - Choose Backup Destination',default=r'C://')
            root.deiconify()
            root.lift()
            settwindow.deiconify()
            settwindow.lift()
            copies = 0

            for i in range(1,101):
                if os.path.isfile(backupdirpath+r'\backup ({}).json'.format(str(i))) == True:
                    copies += i+1
                else:
                    break
            
            if os.path.isfile(backupdirpath+r'\backup.json') == True and os.path.isfile(backupdirpath+r'\backup (1).json') == False:
                bkpname = r'\backup (1).json'
            elif copies != 0:
                bkpname = r'\backup ({}).json'.format(copies)
            elif copies == 0:
                bkpname = r'\backup.json'

            shutil.copyfile(r'data\accounts.json',backupdirpath+bkpname)
            notemsg = 'Accounts backuped successfully!'
            note(notemsg)
            return

        importlstbxbglbl = Label(settwindow,name='datatab7',bg="#1E1E1E",image=importlistboxbg).place(x=35,y=52)
        importlstbxlbl = Label(settwindow,name='datatab6',bg="#535353"
        ,fg='#767373',text="Imports List",font=('Nexa Bold', 12)).place(x=135,y=110+10)
        importlstbxlbl2 = Label(settwindow,name='datatab5',bg="#535353"
        ,fg='#767373',text="(There's nothing imported yet!)",font=('Nexa Bold', 8)).place(x=100,y=133+10)

        importtkbtn = Button(settwindow,name='datatab3',image=importbtn,bg="#1E1E1E",borderwidth=0
        ,activebackground="#1E1E1E",command=importfunc)
        importtklbl = Label(settwindow,name='datatab4',image=importhoverlbl,bg="#1E1E1E")

        def importtkbtn_onEnter(event):
            importtkbtn.config(image=importhover)
            importtklbl.place(x=140,y=261)
            importtklbl.lift()

        def importtkbtn_onLeave(event):
            importtkbtn.config(image=importbtn)
            importtklbl.place_forget()

        importtkbtn.bind('<Enter>',importtkbtn_onEnter)
        importtkbtn.bind('<Leave>',importtkbtn_onLeave)

        importtkbtn.place(x=35,y=255)


        exporttkbtn = Button(settwindow,name='datatab1',image=exportbtn,bg="#1E1E1E",borderwidth=0
        ,activebackground="#1E1E1E",command=exportfunc)
        exporttklbl = Label(settwindow,name='datatab2',image=exporthoverlbl,bg="#1E1E1E")

        def exporttkbtn_onEnter(event):
            exporttkbtn.config(image=exporthover)
            exporttklbl.place(x=140,y=261)
            exporttklbl.lift()

        def exporttkbtn_onLeave(event):
            exporttkbtn.config(image=exportbtn)
            exporttklbl.place_forget()

        exporttkbtn.bind('<Enter>',exporttkbtn_onEnter)
        exporttkbtn.bind('<Leave>',exporttkbtn_onLeave)

        exporttkbtn.place(x=35+50,y=255)
    
    #COPY
    def copytab():
        for i in range(1,15):
            try:
                settwindow.nametowidget('generaltab'+str(i)).destroy()
                settwindow.nametowidget('generaltab'+str(i)).destroy()
            except:
                pass
        
        for i in range(1,15):
            try:
                settwindow.nametowidget('datatab'+str(i)).destroy()
                settwindow.nametowidget('datatab'+str(i)).destroy()
            except:
                pass

        SettTabs.config(image=tabscopy)
        Ctab_btn.config(bg='#1E1E1E',activebackground='#1E1E1E')
        Dtab_btn.config(bg='#535353',activebackground='#535353')
        Gtab_btn.config(bg='#535353',activebackground='#535353')

        #name widgets
        

    #Tab Buttons
    SettTabs = Label(settwindow,bg="#2C2C2C",borderwidth=0)
    Gtab_btn = Button(settwindow,bg='#535353',fg='#767373',borderwidth=0,activebackground='#535353'
    ,text='General',font=('Nexa Bold',9),justify=CENTER,activeforeground='#767373',command=generaltab)
    Dtab_btn = Button(settwindow,bg='#535353',fg='#767373',borderwidth=0,activebackground='#535353'
    ,text='Data',font=('Nexa Bold',9),justify=CENTER,activeforeground='#767373',command=datatab)
    Ctab_btn = Button(settwindow,bg='#535353',fg='#767373',borderwidth=0,activebackground='#535353'
    ,text='Copy',font=('Nexa Bold',9),justify=CENTER,activeforeground='#767373',command=copytab)

    datatab()
    Gtab_btn.place(x=35,y=16)
    Dtab_btn.place(x=128,y=16)
    Ctab_btn.place(x=128+83,y=16)
    SettTabs.pack(anchor=CENTER,pady=16)
    


def login(event):

    if lstbx.curselection() == ():
        return
    if lstbx.curselection() != ():

        riotindex = lstbx.curselection()[0]
        riotname = lstbx.get(riotindex,last=None)
        account = db.get(accounts.name == riotname)

        if account['name'] == riotname:
            loginname = account['name']
            loginusername = account['username']
            print(loginusername)
            loginpassw = account['password']
        else:
            print('Account not found in db')
            return

        lstbx.config(state=DISABLED,cursor='no')
        note('Logging in...!')

        os.system("taskkill /f /im  RiotClientCrashHandler.exe")
        os.system("taskkill /f /im  RiotClientCrashHandler.exe")
        os.system("taskkill /f /im  RiotClientServices.exe")
        os.system("taskkill /f /im  RiotClientServices.exe")
        os.system("taskkill /f /im  RiotClientUx.exe")
        os.system("taskkill /f /im  RiotClientUx.exe")
        os.system("taskkill /f /im  RiotClientUxRender.exe")
        os.system("taskkill /f /im  RiotClientUxRender.exe")
        os.system("taskkill /f /im  LeagueClient.exe")
        os.system("taskkill /f /im  LeagueClient.exe")
        os.system("taskkill /f /im  LeagueClientUx.exe")
        os.system("taskkill /f /im  LeagueClientUx.exe")

        if findapp('league of legends') == True:
            run('league of legends')

            found = 0

            for i in range(60):
                root.update()
                riotwin = ahk.win_get(title = "Riot Client")
                time.sleep(0.5)
                try:
                    if riotwin.exist:
                        riotwin.activate()
                        riotwinLoc = riotwin.rect
                        riotwinX = riotwinLoc[0]
                        riotwinY = riotwinLoc[1]
                        riotwinX2 = riotwinX + (riotwinLoc[2] // 2)
                        riotwinY2 = riotwinY + riotwinLoc[3]
                        found = 1
                        break
                except:
                    try:
                        leaguewin = ahk.win_get(title = "League of Legends")
                        if leaguewin.exist:
                            note('Please log out first!','red')
                            break
                    except:
                        pass
                    pass

            for i in range(60):
                if found == 1:
                    root.update()
                    time.sleep(0.5)
                    riotlogo = ahk.image_search(image_path=r'assests\image_recog\riotlogo.png',
                    color_variation=70,upper_bound= [riotwinX,riotwinY],lower_bound = [riotwinX2,riotwinY2])
                    if riotlogo != None:
                        #username
                        ahk.mouse_move(riotlogo[0]+55,riotlogo[1]+175,speed=0)
                        ahk.click()
                        ahk.type(loginusername)
                        #password
                        ahk.mouse_move(riotlogo[0]+55,riotlogo[1]+220,speed=0)
                        ahk.click()
                        ahk.type(loginpassw)
                        #loginbtn
                        ahk.mouse_move(riotlogo[0]+65,riotlogo[1]+530,speed=0)
                        ahk.click()
                        logged_in = 1
                        break
                else:
                    logged_in = 0
                    note('Riot Client window not found','red')
                    break

            for i in range(60):
                if logged_in == 1:
                    root.update()
                    time.sleep(0.5)

                    playbtn = ahk.image_search(image_path=r'assests\image_recog\playbtn.png',
                    color_variation=70,upper_bound= [riotwinX,riotwinY],lower_bound = [riotwinX2,riotwinY2])

                    if playbtn != None:
                        ahk.mouse_move(playbtn[0]+120,playbtn[1]+23,speed=0)
                        ahk.click()

                    try:
                        leaguewin = ahk.win_get(title = "League of Legends")
                        if leaguewin.exist:
                            note('Logged in successfully!')
                            if configdb.contains(Query().exit_after_login == 'true') == True:
                                exit()
                            else:
                                configdb.upsert({'exit_after_login':'false'}, Query().exit_after_login.exists())
                                pass
                            break
                        else:
                            break
                    except:
                        pass
                    
                else:
                    break
        else:
            note('Game Not Found!','red')

        lstbx.config(state=NORMAL,cursor='')
    return

###commands


#accicon
def count(no:int,x_offset:int = 0):
    try:
        root.nametowidget('counter').destroy()
    except:
        pass

    if no == 100:
        finalcount = '99+'

    else:
        finalcount = str(no)
    
    invisforcount = Label(name='counter',text=finalcount,font=('Quicksand SemiBold',8),bg='#C53131'
    ,fg='#C2C2C2',borderwidth=0,justify=CENTER,anchor=CENTER)
    # default = 0
    # dbl digit = -2
    # 99+ = -4
    invisforcount.place(x=31+x_offset,y=43)

accountsbglbl = Label(image=accountsiconbg,bg="#1E1E1E",borderwidth=0).place(x=0,y=0)
accountsiconlbl = Label(image=accountsicon,bg="#282828",width=69,height=73)
accountsiconlbl.place(x=0,y=0)


#accicon

######addbtn

addbtn = Button(image=addbtnicon,bg="#1E1E1E",width=69,height=43,borderwidth=0,activebackground="#1E1E1E",command=addwind)
addlbl = Label(image=addhoverlbl,bg="#1E1E1E")

def addbtn_onEnter(event):
    addbtn.config(image=addbtniconactive)
    addlbl.place(x=6,y=310)
    addlbl.lift()

def addbtn_onLeave(event):
    addbtn.config(image=addbtnicon)
    addlbl.place_forget()

addbtn.bind('<Enter>',addbtn_onEnter)
addbtn.bind('<Leave>',addbtn_onLeave)
addbtn.place(x=0,y=83+5)

#####addbtn

#####rmvbtn

removebtn = Button(image=removebtnicon,bg="#1E1E1E",width=69,height=43,borderwidth=0,activebackground="#1E1E1E",command=remove)
rmvlbl = Label(image=removehoverlbl,bg="#1E1E1E")
def removebtn_onEnter(event):
    removebtn.config(image=removebtniconactive)
    rmvlbl.place(x=6,y=310)
    rmvlbl.lift()

def removebtn_onLeave(event):
    removebtn.config(image=removebtnicon)
    rmvlbl.place_forget()


removebtn.place(x=0,y=136+5)

#####rmvbtn

#####edtbtn

editbtn = Button(image=editbtnicon,bg="#1E1E1E",width=69,height=43,borderwidth=0,activebackground="#1E1E1E",command=editwind)
editlbl = Label(image=edithoverlbl,bg="#1E1E1E")
def editbtn_onEnter(event):
    editbtn.config(image=editbtniconactive)
    editlbl.place(x=6,y=310)
    editlbl.lift()

def editbtn_onLeave(event):
    editbtn.config(image=editbtnicon)
    editlbl.place_forget()

editbtn.place(x=0,y=190+5)

#####edtbtn

#####copybtn

copybtn = Button(image=copybtnicon,bg="#1E1E1E",width=69,height=43,borderwidth=0
,activebackground="#1E1E1E",command=copy)
copylbl = Label(image=copyhoverlbl,bg="#1E1E1E")

def copybtn_onEnter(event):
    copybtn.config(image=copybtniconactive)
    copylbl.place(x=6,y=310)
    copylbl.lift()

def copybtn_onLeave(event):
    copybtn.config(image=copybtnicon)
    copylbl.place_forget()

copybtn.place(x=0,y=195+43+11)

#####copybtn

####infbtn

infobtn = Button(image=infobtnicon,bg="#1E1E1E",width=69,height=43,borderwidth=0,activebackground="#1E1E1E",command=info)
infolbl = Label(image=infohoverlbl,bg="#1E1E1E")

def infobtn_onEnter(event):
    infobtn.config(image=infobtniconactive)
    infolbl.place(x=6,y=310)
    infolbl.lift()


def infobtn_onLeave(event):
    infobtn.config(image=infobtnicon)
    infolbl.place_forget()

infobtn.bind('<Enter>',infobtn_onEnter)
infobtn.bind('<Leave>',infobtn_onLeave)

infobtn.place(x=0,y=380+5)

####infbtn

####setbtn

settingsbtn = Button(image=settingsbtnicon,bg="#1E1E1E",width=69,height=43,borderwidth=0,activebackground="#1E1E1E",command=settings)
settingslbl = Label(image=settingshoverlbl,bg="#1E1E1E")

def settingsbtn_onEnter(event):
    settingsbtn.config(image=settingsbtniconactive)
    settingslbl.place(x=6,y=310)
    settingslbl.lift()

def settingsbtn_onLeave(event):
    settingsbtn.config(image=settingsbtnicon)
    settingslbl.place_forget()

settingsbtn.bind('<Enter>',settingsbtn_onEnter)
settingsbtn.bind('<Leave>',settingsbtn_onLeave)

settingsbtn.place(x=0,y=440)

####setbtn

sidebar.pack(side=LEFT)

accountslbl = Label(root,bg="#2C2C2C",font=('Nexa Bold',20),image=accountslabelbg,text='Accounts',fg="#C2C2C2",compound=CENTER)
accountslbl.pack(anchor=N,pady=25)

lstbximglabel = Label(root,bg="#2C2C2C",image=lstbximg)
lstbximglabel.place(x=108,y=96-11)

lstbx = Listbox(root,bg = "#535353", font =('Nexa Light',14),justify=CENTER,fg="#C2C2C2",highlightthickness=0,selectmode=SINGLE,
 width = 21,height= 12,selectbackground="#B5C531"
 ,activestyle=NONE,borderwidth=0,highlightcolor="black"
 ,selectforeground="black",border=0
 ,relief=FLAT,selectborderwidth=0,exportselection=False)
lstbx.bind('<Double-Button-1>',login)
lstbx.pack(anchor=CENTER)

def fetch():

    lstbx.delete(0,END)
    currentsize = 0

    for item in db:
        currentsize += 1
        try:
            lstbx.insert(0,item['name'])
        except:
            pass

    if lstbx.size() == 0:
        removebtn.config(image=removebtndisabled,cursor='no',command=None,relief=SUNKEN)
        removebtn.unbind('<Enter>')
        removebtn.unbind('<Leave>')

        editbtn.config(image=editbtndisabled,cursor='no',command=None,relief=SUNKEN)
        editbtn.unbind('<Enter>')
        editbtn.unbind('<Leave>')

        copybtn.config(image=copybtndisabled,cursor='no',command=None,relief=SUNKEN)
        copybtn.unbind('<Enter>')
        copybtn.unbind('<Leave>')
    else:
        
        editbtn.config(cursor='')
        editbtn.bind('<Enter>',editbtn_onEnter)
        editbtn.bind('<Leave>',editbtn_onLeave)

        removebtn.config(cursor='')
        removebtn.bind('<Enter>',removebtn_onEnter)
        removebtn.bind('<Leave>',removebtn_onLeave)

        copybtn.config(cursor='')
        copybtn.bind('<Enter>',copybtn_onEnter)
        copybtn.bind('<Leave>',copybtn_onLeave)
    

    if currentsize == 0:
        accountsiconlbl.config(image=accountsicon)
        try:
            root.nametowidget('counter').destroy()
        except:
            pass
        pass
    elif currentsize >= 1 and currentsize <= 9:
        accountsiconlbl.config(image=counterbg1to9)
        count(currentsize)
    elif currentsize >= 10 and currentsize <= 99:
        accountsiconlbl.config(image=counterbg10to99)
        count(currentsize,-2)
    elif currentsize >= 100:
        accountsiconlbl.config(image=counterbg10to99)
        count(100,-4)
    

fetch()

if lstbx.size() != 0:
    def notelmao():
        note('Double Click To Login!')

    if configdb.contains(Query().disable_startup_msg == 'true') == True or configdb.contains(Query().disable_startup_msg == 'false') == True:
        if configdb.contains(Query().disable_startup_msg == 'true') == True:
            pass
        else:
            root.after(1000,notelmao)
    else:
        configdb.insert({'disable_startup_msg':'false'})
else:
    pass

root.mainloop()