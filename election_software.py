from tkinter import *
from tkinter.ttk import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from captcha.image import ImageCaptcha
from PIL import ImageTk,Image
from tkinter import messagebox
import random
import smtplib
import mysql.connector as sqltor

class Election(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("800x600")
        self.title("Election Software")
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(expand=True)
         
class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Student Council Elections 2019-20", font=('Times New Roman', 18, "bold")).grid()
        Button(self, text="Vote",command=lambda: master.switch_frame(Instructions)).grid()
        Button(self, text="Result",command=lambda: master.switch_frame(Result)).grid()
        Button(self, text="Analysis",command=lambda:master.switch_frame(Analysis)).grid()
        
class Instructions(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Student Council Elections 2019-20", font=('Times New Roman', 18, "bold")).grid(row=0)
        inst=open("Instructions.txt","r")
        l=1
        for I in inst.readlines():
            Label(self, text=I).grid(row=l,column=0,sticky=W)
            l=l+1
        Button(self, text="Next",command=lambda: master.switch_frame(VoteLogin)).grid()
l=[]
for x in range(1,1001):
    l.append(x)
for y in range(0,len(l)):
    l[y]=str(l[y])
class VoteLogin(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)
        Label(self,text="Login",font=("Times New Roman",18,"bold")).grid(row=0,sticky=N)
        lname=Label(self, text="Name").grid(row=1,column=0)
        self.ename=Entry(self)
        self.ename.grid(row=1,column=1)
        lrollno=Label(self,text="Admission No.").grid(row=2,column=0)
        self.erollno=Entry(self)
        self.erollno.grid(row=2,column=1)
        grade=StringVar()
        grade.set("Class")
        hr=OptionMenu(self,grade,"","6","7","8","9","10","11","12")
        hr.grid(row=3,column=0)
        section=StringVar()
        section.set("Section")
        hb=OptionMenu(self,section,"","Corbett","Sariska","Gir","Kanha","Ranthambore")
        hb.grid(row=3,column=1)
        house=StringVar()
        house.set("House")
        self.wc=OptionMenu(self,house,"","Tigers","Lions","Panthers","Leopards")
        self.wc.grid(row=3,column=2)
        def detail():
            Mycon=sqltor.connect(host="localhost",user="root",password="kq@sql",database="Student_Council")
            c="Insert into Voter values("+self.erollno.get()+",'"+self.ename.get()+"',"+grade.get()+",'"+section.get()+"','"+house.get()+"')"
            Cursor=Mycon.cursor()
            Cursor.execute(c)
            Mycon.commit()
            Mycon.close()
        def func():
            if self.erollno.get() in l:
                l.remove(self.erollno.get())
                master.switch_frame(Head_boy)
            else:
                messagebox.showerror("Error", "You have already voted")
        def submit():
            detail()
            func()
        Button(self, text="Submit",command=submit).grid()
        
cand=sqltor.connect(host="localhost",user="root",password="kq@sql",database="Student_Council")
post=cand.cursor()
post.execute("SELECT Head_Boy FROM Candidates")
hb=[]
shb=post.fetchall()
for x in shb:
    hb.append(x[0])
rhb=[]
class Head_boy(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)
        L=[]
        Label(self,text="Vote For Head Boy",font=('Times New Roman', 15, "bold")).grid(row=0)
        for i in range(0,len(hb)):
            L.append(Button(self, text=hb[i], command=lambda i=i:[rhb.append(hb[i]),master.switch_frame(Head_girl)]))
            L[i].grid(row=i+1)

post.execute("SELECT Head_Girl FROM Candidates")
hg=[]
shg=post.fetchall()
for x in shg:
    hg.append(x[0])
rhg=[]
class Head_girl(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)
        L=[]
        Label(self,text="Vote For Head Girl",font=('Times New Roman', 15, "bold")).grid(row=0)
        for i in range(0,len(hg)):
            L.append(Button(self, text=hg[i], command=lambda i=i:[rhg.append(hg[i]),master.switch_frame(Vice_Head_boy)]))
            L[i].grid(row=i+1)

post.execute("SELECT VHead_Boy FROM Candidates")
vhb=[]
svhb=post.fetchall()
for x in svhb:
    vhb.append(x[0])
rvhb=[]
class Vice_Head_boy(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)
        L=[]
        Label(self,text="Vote For Vice Head Boy",font=('Times New Roman', 15, "bold")).grid(row=0)
        for i in range(0,len(vhb)):
            L.append(Button(self, text=vhb[i], command=lambda i=i:[rvhb.append(vhb[i]),master.switch_frame(Vice_Head_girl)]))
            L[i].grid(row=i+1)

post.execute("SELECT VHead_Girl FROM Candidates")
vhg=[]
svhg=post.fetchall()
for x in svhg:
    vhg.append(x[0])
rvhg=[]
class Vice_Head_girl(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)
        L=[]
        Label(self,text="Vote For Vice Head Girl",font=('Times New Roman', 15, "bold")).grid(row=0)
        for i in range(0,len(vhg)):
            L.append(Button(self, text=vhg[i], command=lambda i=i:[rvhg.append(vhg[i]),master.switch_frame(SportsC)]))#
            L[i].grid(row=i+1)

post.execute("SELECT Sports_C FROM Candidates")
sc=[]
ssc=post.fetchall()
for x in ssc:
    sc.append(x[0])
rsc=[]
class SportsC(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)
        L=[]
        Label(self,text="Vote For Sports Captain",font=('Times New Roman', 15, "bold")).grid(row=0)
        for i in range(0,len(sc)):
            L.append(Button(self, text=sc[i], command=lambda i=i:[rsc.append(sc[i]),master.switch_frame(ArtsC)]))
            L[i].grid(row=i+1)

post.execute("SELECT Arts_C FROM Candidates")
ac=[]
sac=post.fetchall()
for x in sac:
    ac.append(x[0])
rac=[]
class ArtsC(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)
        L=[]
        Label(self,text="Vote For Arts Captain",font=('Times New Roman', 15, "bold")).grid(row=0)
        for i in range(0,len(ac)):
            L.append(Button(self, text=ac[i], command=lambda i=i:[rac.append(ac[i]),master.switch_frame(HouseC)]))#
            L[i].grid(row=i+1)

post.execute("SELECT Tiger_HCapt FROM Candidates")
thc=[]
sthc=post.fetchall()
for x in sthc:
    thc.append(x[0])
rthc=[]
post.execute("SELECT Lion_HCapt FROM Candidates")
lhc=[]
slhc=post.fetchall()
for x in slhc:
    lhc.append(x[0])
rlhc=[]
post.execute("SELECT Panther_HCapt FROM Candidates")
phc=[]
sphc=post.fetchall()
for x in sphc:
    phc.append(x[0])
rphc=[]
post.execute("SELECT Leopard_HCapt FROM Candidates")
ldhc=[]
sldhc=post.fetchall()
for x in sldhc:
    ldhc.append(x[0])
rldhc=[]
class HouseC(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)
        Mycon=sqltor.connect(host="localhost",user="root",password="kq@sql",database="student_council")
        Cursor=Mycon.cursor()
        Cursor.execute("SELECT*FROM Voter;")
        a=Cursor.fetchall()
        b=a[-1][-1]
        if b=="Tigers":
            L=[]
            Label(self,text="Vote For Tiger House Captain",font=('Times New Roman', 15, "bold")).grid(row=0)
            for i in range(0,len(thc)):
                L.append(Button(self, text=thc[i], command=lambda i=i:[rthc.append(thc[i]),master.switch_frame(ViceHouseC)]))
                L[i].grid(row=i+1)
        elif b=="Lions":
            L=[]
            Label(self,text="Vote For Lion House Captain",font=('Times New Roman', 15, "bold")).grid(row=0)
            for i in range(0,len(lhc)):
                L.append(Button(self, text=lhc[i], command=lambda i=i:[rlhc.append(lhc[i]),master.switch_frame(ViceHouseC)]))
                L[i].grid(row=i+1)
        elif b=="Panthers":
            L=[]
            Label(self,text="Vote For Panther House Captain",font=('Times New Roman', 15, "bold")).grid(row=0)
            for i in range(0,len(phc)):
                L.append(Button(self, text=phc[i], command=lambda i=i:[rphc.append(phc[i]),master.switch_frame(ViceHouseC)]))
                L[i].grid(row=i+1)
        elif b=="Leopards":
            L=[]
            Label(self,text="Vote For Leopard House Captain",font=('Times New Roman', 15, "bold")).grid(row=0)
            for i in range(0,len(ldhc)):
                L.append(Button(self, text=ldhc[i], command=lambda i=i:[rldhc.append(ldhc[i]),master.switch_frame(ViceHouseC)]))
                L[i].grid(row=i+1)
        Mycon.close()
        
post.execute("SELECT Tiger_HVCapt FROM Candidates")
tvhc=[]
stvhc=post.fetchall()
for x in stvhc:
    tvhc.append(x[0])
rtvhc=[]
post.execute("SELECT Lion_HVCapt FROM Candidates")
lvhc=[]
slvhc=post.fetchall()
for x in slvhc:
    lvhc.append(x[0])
rlvhc=[]
post.execute("SELECT Panther_HVCapt FROM Candidates")
pvhc=[]
spvhc=post.fetchall()
for x in spvhc:
    pvhc.append(x[0])
rpvhc=[]
post.execute("SELECT Leopard_HVCapt FROM Candidates")
ldvhc=[]
sldvhc=post.fetchall()
for x in sldvhc:
    ldvhc.append(x[0])
rldvhc=[]

class ViceHouseC(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)
        Mycon=sqltor.connect(host="localhost",user="root",password="kq@sql",database="student_council")
        Cursor=Mycon.cursor()
        Cursor.execute("SELECT*FROM Voter;")
        a=Cursor.fetchall()
        b=a[-1][-1]
        if b=="Tigers":
            L=[]
            Label(self,text="Vote For Tiger House Vice Captain",font=('Times New Roman', 15, "bold")).grid(row=0)
            for i in range(0,len(tvhc)):
                L.append(Button(self, text=tvhc[i], command=lambda i=i:[rtvhc.append(tvhc[i]),master.switch_frame(StartPage)]))
                L[i].grid(row=i+1)
        elif b=="Lions":
            L=[]
            Label(self,text="Vote For Lion House Vice Captain",font=('Times New Roman', 15, "bold")).grid(row=0)
            for i in range(0,len(lvhc)):
                L.append(Button(self, text=lvhc[i], command=lambda i=i:[rlvhc.append(lvhc[i]),master.switch_frame(StartPage)]))
                L[i].grid(row=i+1)
        elif b=="Panthers":
            L=[]
            Label(self,text="Vote For Panther House Vice Captain",font=('Times New Roman', 15, "bold")).grid(row=0)
            for i in range(0,len(pvhc)):
                L.append(Button(self, text=pvhc[i], command=lambda i=i:[rpvhc.append(pvhc[i]),master.switch_frame(StartPage)]))
                L[i].grid(row=i+1)
        elif b=="Leopards":
            L=[]
            Label(self,text="Vote For Leopard House Vice Captain",font=('Times New Roman', 15, "bold")).grid(row=0)
            for i in range(0,len(ldvhc)):
                L.append(Button(self, text=ldvhc[i], command=lambda i=i:[rldvhc.append(ldvhc[i]),master.switch_frame(StartPage)]))
                L[i].grid(row=i+1)
        Mycon.close()

class Result(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)
        tabControl=Notebook(self,width=1920,height=1080)  
        b=Frame(tabControl)
        tabControl.add(b, text='Head Boy')
        g=Frame(tabControl)
        tabControl.add(g, text='Head Girl')
        vb=Frame(tabControl)
        tabControl.add(vb, text='Vice Head Boy')
        vg=Frame(tabControl)
        tabControl.add(vg, text='Vice Head Girl')
        sb=Frame(tabControl)
        tabControl.add(sb, text='Sports Captain')
        ab=Frame(tabControl)
        tabControl.add(ab, text='Arts Captain')
        th=Frame(tabControl)
        tabControl.add(th, text='Tiger House')
        lh=Frame(tabControl)
        tabControl.add(lh, text='Lion House')
        ph=Frame(tabControl)
        tabControl.add(ph, text='Panther House')
        ldh=Frame(tabControl)
        tabControl.add(ldh, text='Leopard House')
        tabControl.pack()
        Label(b, text="Results for the post of Head Boy", font=('Helvetica', 18, "bold")).grid()
        eb=open("Head Boy.txt","w+")
        for y in range(0,len(hb)):
            t=hb[y]
            eb.write(t)
            eb.write(" : ")
            eb.write(str(rhb.count(t)))
            eb.write("\n")
        eb.close()
        ebr=open("Head Boy.txt","r")
        q=ebr.readlines()
        for z in q:
            Label(b,text=z,font=('Times New Roman', 14, "bold")).grid(sticky=N+W+S+E)
            
        Label(g, text="Results for the post of Head Girl", font=('Helvetica', 18, "bold")).grid()
        eg=open("Head Girl.txt","w+")
        for y in range(0,len(hg)):
            t=hg[y]
            eg.write(t)
            eg.write(" : ")
            eg.write(str(rhg.count(t)))
            eg.write("\n")
        eg.close()
        egr=open("Head Girl.txt","r")
        q=egr.readlines()
        for z in q:
            Label(g,text=z,font=('Times New Roman', 14, "bold")).grid(sticky=W)

        Label(vb, text="Results for the post of Vice Head Boy", font=('Times New Roman', 18, "bold")).grid()
        evb=open("Vice Head Boy.txt","w+")
        for y in range(0,len(vhb)):
            t=vhb[y]
            evb.write(t)
            evb.write(" : ")
            evb.write(str(rvhb.count(t)))
            evb.write("\n")
        evb.close()
        evbr=open("Vice Head Boy.txt","r")
        q=evbr.readlines()
        for z in q:
            Label(vb,text=z,font=('Times New Roman', 14, "bold")).grid(sticky=W)
        
        Label(vg, text="Results for the post of Vice Head Girl", font=('Helvetica', 18, "bold")).grid()
        evg=open("Vice Head Girl.txt","w+")
        for y in range(0,len(vhg)):
            t=vhg[y]
            evg.write(t)
            evg.write(" : ")
            evg.write(str(rvhg.count(t)))
            evg.write("\n")
        evg.close()
        evgr=open("Vice Head Girl.txt","r")
        q=evgr.readlines()
        for z in q:
            Label(vg,text=z,font=('Times New Roman', 14, "bold")).grid(sticky=W)

        Label(sb, text="Results for the post of Sports Captain", font=('Helvetica', 18, "bold")).grid()
        esb=open("Sports Captain.txt","w+")
        for y in range(0,len(sc)):
            t=sc[y]
            esb.write(t)
            esb.write(" : ")
            esb.write(str(rsc.count(t)))
            esb.write("\n")
        esb.close()
        esbr=open("Sports Captain.txt","r")
        q=esbr.readlines()
        for z in q:
            Label(sb,text=z,font=('Times New Roman', 14, "bold")).grid(sticky=W)

        Label(ab, text="Results for the post of Arts Captain", font=('Helvetica', 18, "bold")).grid()
        eab=open("Arts Captain.txt","w+")
        for y in range(0,len(ac)):
            t=ac[y]
            eab.write(t)
            eab.write(" : ")
            eab.write(str(rac.count(t)))
            eab.write("\n")
        eab.close()
        eabr=open("Arts Captain.txt","r")
        q=eabr.readlines()
        for z in q:
            Label(ab,text=z,font=('Times New Roman', 14, "bold")).grid(sticky=W)

        Label(th, text="Results for Tiger House", font=('Helvetica', 18, "bold")).grid(row=0)
        Label(th, text="Tiger House Captain",font=('Times New Roman', 15, "bold")).grid(row=1,column=0)
        ethc=open("Tiger House Captain.txt","w+")
        for y in range(0,len(thc)):
            t=thc[y]
            ethc.write(t)
            ethc.write(" : ")
            ethc.write(str(rthc.count(t)))
            ethc.write("\n")
        ethc.close()
        erthc=open("Tiger House Captain.txt","r")
        q=erthc.readlines()
        r=2
        for z in q:
            Label(th,text=z,font=('Times New Roman', 14, "bold")).grid(row=r,column=0)
            r=r+1
        Label(th, text="Tiger House Vice Captain",font=('Times New Roman', 15, "bold")).grid(row=1,column=1,sticky=NSEW)
        etvhc=open("Tiger House Vice Captain.txt","w+")
        for y in range(0,len(tvhc)):
            t=tvhc[y]
            etvhc.write(t)
            etvhc.write(" : ")
            etvhc.write(str(rtvhc.count(t)))
            etvhc.write("\n")
        etvhc.close()
        ertvhc=open("Tiger House Vice Captain.txt","r")
        q=ertvhc.readlines()
        r=2
        for z in q:
            Label(th,text=z,font=('Times New Roman', 14, "bold")).grid( row=r,column=1)
            r=r+1

        Label(lh, text="Results for Lion House", font=('Helvetica', 18, "bold")).grid(row=0)
        Label(lh, text="Lion House Captain",font=('Times New Roman', 15, "bold")).grid(row=1,column=0)
        elhc=open("Lion House Captain.txt","w+")
        for y in range(0,len(lhc)):
            t=lhc[y]
            elhc.write(t)
            elhc.write(" : ")
            elhc.write(str(rlhc.count(t)))
            elhc.write("\n")
        elhc.close()
        erlhc=open("Lion House Captain.txt","r")
        q=erlhc.readlines()
        r=2
        for z in q:
            Label(lh,text=z,font=('Times New Roman', 14, "bold")).grid(row=r,column=0)
            r=r+1
        Label(lh, text="Lion House Vice Captain",font=('Times New Roman', 15, "bold")).grid(row=1,column=1)
        elvhc=open("Lion House Vice Captain.txt","w+")
        for y in range(0,len(lvhc)):
            t=lvhc[y]
            elvhc.write(t)
            elvhc.write(" : ")
            elvhc.write(str(rlvhc.count(t)))
            elvhc.write("\n")
        elvhc.close()
        erlvhc=open("Lion House Vice Captain.txt","r")
        q=erlvhc.readlines()
        r=2
        for z in q:
            Label(lh,text=z,font=('Times New Roman', 14, "bold")).grid(row=r,column=1)
            r=r+1

        Label(ph, text="Results for Panther House", font=('Helvetica', 18, "bold")).grid(row=0)
        Label(ph, text="Panther House Captain",font=('Times New Roman', 15, "bold")).grid(row=1,column=0)
        ephc=open("Panther House Captain.txt","w+")
        for y in range(0,len(phc)):
            t=phc[y]
            ephc.write(t)
            ephc.write(" : ")
            ephc.write(str(rphc.count(t)))
            ephc.write("\n")
        ephc.close()
        erphc=open("Panther House Captain.txt","r")
        q=erphc.readlines()
        r=2
        for z in q:
            Label(ph,text=z,font=('Times New Roman', 14, "bold")).grid(row=r,column=0)
            r=r+1
        Label(ph, text="Panther House Vice Captain",font=('Times New Roman', 15, "bold")).grid(row=1,column=1)
        epvhc=open("Panther House Vice Captain.txt","w+")
        for y in range(0,len(pvhc)):
            t=pvhc[y]
            epvhc.write(t)
            epvhc.write(" : ")
            epvhc.write(str(rpvhc.count(t)))
            epvhc.write("\n")
        epvhc.close()
        erpvhc=open("Panther House Vice Captain.txt","r")
        q=erpvhc.readlines()
        r=2
        for z in q:
            Label(ph,text=z,font=('Times New Roman', 14, "bold")).grid(row=r,column=1)
            r=r+1

        Label(ldh, text="Results for Leopard House", font=('Helvetica', 18, "bold")).grid(row=0)
        Label(ldh, text="Leopard House Captain",font=('Times New Roman', 15, "bold")).grid(row=1,column=0)
        eldhc=open("Leopard House Captain.txt","w+")
        for y in range(0,len(ldhc)):
            t=ldhc[y]
            eldhc.write(t)
            eldhc.write(" : ")
            eldhc.write(str(rldhc.count(t)))
            eldhc.write("\n")
        eldhc.close()
        erldhc=open("Leopard House Captain.txt","r")
        q=erldhc.readlines()
        r=2
        for z in q:
            Label(ldh,text=z,font=('Times New Roman', 14, "bold")).grid(row=r,column=0)
            r=r+1
        Label(ldh, text="Leopard House Vice Captain",font=('Times New Roman', 15, "bold")).grid(row=1,column=1)
        eldvhc=open("Leopard House Vice Captain.txt","w+")
        for y in range(0,len(lvhc)):
            t=ldvhc[y]
            eldvhc.write(t)
            eldvhc.write(" : ")
            eldvhc.write(str(rldvhc.count(t)))
            eldvhc.write("\n")
        eldvhc.close()
        erldvhc=open("Leopard House Vice Captain.txt","r")
        q=erldvhc.readlines()
        r=2
        for z in q:
            Label(ldh,text=z,font=('Times New Roman', 14, "bold")).grid(row=r,column=1)
            r=r+1
        Button(b, text="Home", command=lambda:[master.switch_frame(StartPage),Notebook.destroy(self)]).grid()
        
class Analysis(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        tabControl=Notebook(self,width=1920,height=1080)  
        b=Frame(tabControl)
        tabControl.add(b, text='Head Boy')
        g=Frame(tabControl)
        tabControl.add(g, text='Head Girl')
        vb=Frame(tabControl)
        tabControl.add(vb, text='Vice Head Boy')
        vg=Frame(tabControl)
        tabControl.add(vg, text='Vice Head Girl')
        sb=Frame(tabControl)
        tabControl.add(sb, text='Sports Captain')
        ab=Frame(tabControl)
        tabControl.add(ab, text='Arts Captain')
        th=Frame(tabControl)
        tabControl.add(th, text='Tiger House')
        lh=Frame(tabControl)
        tabControl.add(lh, text='Lion House')
        ph=Frame(tabControl)
        tabControl.add(ph, text='Panther House')
        ldh=Frame(tabControl)
        tabControl.add(ldh, text='Leopard House')
        tabControl.pack()
        Label(b, text="Analysis for Head Boy", font=('Times New Roman', 15, "bold")).grid()
        Label(g, text="Analysis for Head Girl", font=('Times New Roman', 15, "bold")).grid()
        Label(vb, text="Analysis for Vice Head Boy", font=('Times New Roman', 15, "bold")).grid()
        Label(vg, text="Analysis for Vice Head Girl", font=('Times New Roman', 15, "bold")).grid()
        Label(sb, text="Analysis for Sports Captain", font=('Times New Roman', 15, "bold")).grid()
        Label(ab, text="Analysis for Arts Captain", font=('Times New Roman', 15, "bold")).grid()
        Label(th, text="Analysis for Tiger House", font=('Times New Roman', 15, "bold")).grid(row=0)
        Label(lh, text="Analysis for Lion House", font=('Times New Roman', 15, "bold")).grid(row=0)
        Label(ph, text="Analysis for Panther House", font=('Times New Roman', 15, "bold")).grid(row=0)
        Label(ldh, text="Analysis for Leopard House", font=('Times New Roman', 15, "bold")).grid(row=0)
        figure = Figure(figsize=(5, 4), dpi=100)
        k1=[]
        for u in hb:
            k1.append(rhb.count(u))
        figure.add_subplot(111).plot(hb,k1)
        canvas= FigureCanvasTkAgg(figure,b)
        canvas.get_tk_widget().grid()
        
        figure = Figure(figsize=(5, 4), dpi=100)
        k2=[]
        print(hg)
        for u in hg:
            k2.append(rhg.count(u))
        figure.add_subplot(111).plot(hg,k2)
        canvas2= FigureCanvasTkAgg(figure,g)
        canvas2.get_tk_widget().grid()
        
        figure = Figure(figsize=(5, 4), dpi=100)
        k3=[]
        for u in vhb:
            k3.append(rvhb.count(u))
        figure.add_subplot(111).plot(vhb,k3)
        canvas3= FigureCanvasTkAgg(figure,vb)
        canvas3.get_tk_widget().grid()
        
        figure = Figure(figsize=(5, 4), dpi=100)
        k4=[]
        for u in vhg:
            k4.append(rvhg.count(u))
        figure.add_subplot(111).plot(vhg,k4)
        canvas4= FigureCanvasTkAgg(figure,vg)
        canvas4.get_tk_widget().grid()
        
        figure= Figure(figsize=(5, 4), dpi=100)
        k5=[]
        for u in sc:
            k5.append(rsc.count(u))
        figure.add_subplot(111).plot(sc,k5)
        canvas5= FigureCanvasTkAgg(figure,sb)
        canvas5.get_tk_widget().grid()
        
        figure = Figure(figsize=(5, 4), dpi=100)
        k6=[]
        for u in ac:
            k6.append(rac.count(u))
        figure.add_subplot(111).plot(ac,k6)
        canvas6= FigureCanvasTkAgg(figure,ab)
        canvas6.get_tk_widget().grid()

        Label(th, text="Tiger House Captain",font=('Times New Roman', 14, "bold")).grid(row=1,column=0)
        figure = Figure(figsize=(5, 4), dpi=100)
        k7=[]
        for u in thc:
            k7.append(rthc.count(u))
        figure.add_subplot(111).plot(thc,k7)
        canvas7= FigureCanvasTkAgg(figure,th)
        canvas7.get_tk_widget().grid(row=2,column=0)

        Label(th, text="Tiger House Vice Captain",font=('Times New Roman', 14, "bold")).grid(row=1,column=1)
        figure = Figure(figsize=(5, 4), dpi=100)
        k8=[]
        for u in tvhc:
            k8.append(rtvhc.count(u))
        figure.add_subplot(111).plot(tvhc,k8)
        canvas8= FigureCanvasTkAgg(figure,th)
        canvas8.get_tk_widget().grid(row=2,column=1)

        Label(lh, text="Lion House Captain",font=('Times New Roman', 14, "bold")).grid(row=1,column=0)
        figure = Figure(figsize=(5, 4), dpi=100)
        k9=[]
        for u in lhc:
            k9.append(rlhc.count(u))
        figure.add_subplot(111).plot(thc,k9)
        canvas9= FigureCanvasTkAgg(figure,lh)
        canvas9.get_tk_widget().grid(row=2,column=0)

        Label(lh, text="Lion House Vice Captain",font=('Times New Roman', 14, "bold")).grid(row=1,column=1)
        figure = Figure(figsize=(5, 4), dpi=100)
        k10=[]
        for u in lvhc:
            k10.append(rlvhc.count(u))
        figure.add_subplot(111).plot(lvhc,k10)
        canvas10= FigureCanvasTkAgg(figure,lh)
        canvas10.get_tk_widget().grid(row=2,column=1)
                
        Label(ph, text="Panther House Captain",font=('Times New Roman', 14, "bold")).grid(row=1,column=0)
        figure = Figure(figsize=(5, 4), dpi=100)
        k11=[]
        for u in phc:
            k11.append(rphc.count(u))
        figure.add_subplot(111).plot(phc,k11)
        canvas11= FigureCanvasTkAgg(figure,ph)
        canvas11.get_tk_widget().grid(row=2,column=0)

        Label(ph, text="Panther House Vice Captain",font=('Times New Roman', 14, "bold")).grid(row=1,column=1)
        figure = Figure(figsize=(5, 4), dpi=100)
        k12=[]
        for u in vhg:
            k12.append(rpvhc.count(u))
        figure.add_subplot(111).plot(pvhc,k12)
        canvas12= FigureCanvasTkAgg(figure,ph)
        canvas12.get_tk_widget().grid(row=2,column=1)

        Label(ldh, text="Leopard House Captain",font=('Times New Roman', 14, "bold")).grid(row=1,column=0)
        figure = Figure(figsize=(5, 4), dpi=100)
        k13=[]
        for u in ldhc:
            k13.append(rldhc.count(u))
        figure.add_subplot(111).plot(ldhc,k13)
        canvas13= FigureCanvasTkAgg(figure,ldh)
        canvas13.get_tk_widget().grid(row=2,column=0)

        Label(ldh, text="Leopard House Vice Captain",font=('Times New Roman', 14, "bold")).grid(row=1,column=1)
        figure = Figure(figsize=(5, 4), dpi=100)
        k14=[]
        for u in ldvhc:
            k14.append(rldvhc.count(u))
        figure.add_subplot(111).plot(ldvhc,k14)
        canvas14= FigureCanvasTkAgg(figure,ldh)
        canvas14.get_tk_widget().grid(row=2,column=1)
        
class Login(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.Label=Label(self, text="Login", font=('Times New Roman', 15, "bold")).grid()
        self.Label=Label(self, text="Username:").grid(row=0,column=0,sticky=W+S+N+E)
        self.Label=Label(self, text="Password:").grid(row=1,column=0,sticky=W+S+N+E)
        self.entry=Entry(self)
        self.entry.grid(row=0,column=1)
        self.entry2=Entry(self, show="*")
        self.entry2.grid(row=1,column=1)
        an=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','9','8','7','6','5','4','3','2','1']
        cp=[]
        for n in range(0,6):
            c=random.choice(an)
            cp.append(c)
            random.shuffle(an)
        image_captcha=ImageCaptcha()
        image1=image_captcha.generate_image(''.join(cp))
        image_captcha.write(''.join(cp),''.join(cp)+".png")
        self.canvas=Canvas(self, width = 250, height = 100)
        self.canvas.grid(row=2) 
        self.img = ImageTk.PhotoImage(Image.open(''.join(cp)+".png"))      
        self.canvas.create_image(100,50, image=self.img)
        self.canvas.image=self.img
        self.entry3=Entry(self, show="*")
        self.entry3.grid(row=2,column=1)
        self.Label=Label(self, text="Verification:").grid(row=3,column=0,sticky=W+S+N+E)
        self.Label=Label(self, text="Please enter the security message given above").grid(row=3,column=1,sticky=W+S+N+E)
        def data():
            u=self.entry.get()
            v=self.entry2.get()
            w=self.entry3.get()
            if u=="snsresult" and v=="result@201920" and w==''.join(cp):
                master.switch_frame(Result)
            elif u=="snsanalysis" and v=="analysis@201920" and w==''.join(cp):
                master.switch_frame(Analysis)
            else:
                messagebox.showerror("Error", "Invalid Username or Password")
        Button(self, text="Submit", command=data).grid()

if __name__ == "__main__":
    app = Election()
    app.mainloop()
