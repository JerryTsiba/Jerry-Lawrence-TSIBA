import tkinter as tk
from datetime import date


root=tk.Tk()
root.title('Freedom Dynamics Investment Calculator 1.0')
root.geometry("550x500")
#root.configure(bg="orange red")

#Blank Lines
blanklineLabel=tk.Label(root,text="").grid(row=0,column=0)

tk.Label(root,text="Welcome to Freedom Dynamics Investment Calculator !",bg='green',fg='white',font='bold',justify='center').grid(row=1,column=0,columnspan=30)

#Blank Lines
blanklineLabel=tk.Label(root,text="").grid(row=2,column=0)
blanklineLabel=tk.Label(root,text="").grid(row=3,column=0)

#Gather user contacts
nameLabel=tk.Label(root,text="Name:").grid(row=5,column=0,padx=2,pady=2,sticky='we',columnspan=3)
nameEntry=tk.Entry(root).grid(row=5,column=1, padx=2,pady=2,sticky='we',columnspan=10)

surnameLabel=tk.Label(root,text="Surname:").grid(row=6,column=0,sticky='e')
surnameEntry=tk.Entry(root).grid(row=6,column=1, padx=2,pady=2,sticky='we',columnspan=10)

phoneLabel=tk.Label(root,text="Phone:").grid(row=7,column=0,sticky='e')
phoneEntry=tk.Entry(root).grid(row=7,column=1, padx=2,pady=2,sticky='we',columnspan=10)

emailLabel=tk.Label(root,text="Email:").grid(row=8,column=0,sticky='e')
emailEntry=tk.Entry(root).grid(row=8,column=1, padx=2,pady=2,sticky='we',columnspan=10)

addressLabel=tk.Label(root,text="Address:").grid(row=9,column=0,sticky='e')
addressEntry=tk.Entry(root).grid(row=9,column=1, padx=2,pady=2,sticky='we',columnspan=10)

#Placement of current date
today=date.today()
dt=today.strftime("%d/%m/%y")
dateLabel=tk.Label(root,text=dt,width=20, borderwidth=3, justify='center').grid(row=9,column=21,columnspan=3)

#Money entry
#Inscription fee [fee]
feeLabel=tk.Label(root,text="Inscription fee:").grid(row=5,column=20,padx=2,pady=2,sticky='e')
fee=tk.DoubleVar()
feeEntry=tk.Entry(root,textvariable=fee).grid(row=5,column=21,columnspan=3)
unit1Label=tk.Label(root,text="[$]").grid(row=5,column=25, padx=2,pady=2,sticky='we',columnspan=3)

#Capital to invest [capital]
capitalLabel=tk.Label(root,text="Capital to invest:").grid(row=6,column=20,padx=2,pady=2,sticky='e')
capital=tk.DoubleVar()
capitalEntry=tk.Entry(root,textvariable=capital).grid(row=6,column=21,columnspan=3)
unit2Label=tk.Label(root,text="[$]").grid(row=6,column=25,padx=2,pady=2,sticky='we',columnspan=3)

#Daily rate percentage [drp]
drpLabel=tk.Label(root,text="Daily rate percentage:").grid(row=7,column=20, padx=2,pady=2,sticky='e')
drp=tk.DoubleVar()
drpEntry=tk.Entry(root,textvariable=drp).grid(row=7,column=21,columnspan=3)
unit2Label=tk.Label(root,text="[%]").grid(row=7,column=25,padx=2,pady=2,sticky='we',columnspan=3)

#Retrieval percentage [rtp]
retpercLabel=tk.Label(root,text="Retrieval percentage:").grid(row=8,column=20, padx=2,pady=2,sticky='e')
rtp=tk.DoubleVar()
rtpEntry=tk.Entry(root,textvariable=rtp).grid(row=8,column=21,columnspan=3)
unit3Label=tk.Label(root,text="[%]").grid(row=8,column=25,padx=2,pady=2,sticky='we',columnspan=3)

#Blank Lines
blanklineLabel=tk.Label(root,text="").grid(row=10,column=0)
blanklineLabel=tk.Label(root,text="").grid(row=11,column=0)

#DISPLAY SCREEN 
#Daily amount [da]
daLabel=tk.Label(root,text="Daily amount:").grid(row=15,column=20, padx=2,pady=2,sticky='e')
da=tk.DoubleVar()
daLabel=tk.Label(root,textvariable=da,bg="black",fg="green",font="bold").grid(row=15,column=21,padx=2,pady=2,sticky='we',columnspan=3)
unit4Label=tk.Label(root,text="[$]").grid(row=15,column=25,padx=2,pady=2,sticky='we',columnspan=3)

#Retrieval fee [rf]
rfLabel=tk.Label(root,text="Retrieval fee:").grid(row=16,column=20, padx=2,pady=2,sticky='e')
rf=tk.DoubleVar()
rfLabel=tk.Label(root,textvariable=rf,bg="black",fg="green",font="bold").grid(row=16,column=21,padx=2,pady=2,sticky='we',columnspan=3)
unit5Label=tk.Label(root,text="[$]").grid(row=16,column=25,padx=2,pady=2,sticky='we',columnspan=3)

#Total amount at deadline [tad]
tadLabel=tk.Label(root,text="Total amount at deadline:").grid(row=17,column=20, padx=2,pady=2,sticky='e')
tad=tk.DoubleVar()
tadLabel=tk.Label(root,textvariable=tad,bg="black",fg="green",font="bold").grid(row=17,column=21,padx=2,pady=2,sticky='we',columnspan=3)
unit6Label=tk.Label(root,text="[$]").grid(row=17,column=25,padx=2,pady=2,sticky='we',columnspan=3)

# Profit [pf]
pfLabel=tk.Label(root,text="Total profit:").grid(row=18,column=20,padx=2,pady=2,sticky='e')
pf=tk.DoubleVar()
pfLabel=tk.Label(root,textvariable=pf,bg="black",fg="green",font="bold").grid(row=18,column=21,padx=2,pady=2,sticky='we',columnspan=3)
unit7Label=tk.Label(root,text="[$]").grid(row=18,column=25,padx=2,pady=2,sticky='we',columnspan=3)

# Profit [pf]
pfLabel=tk.Label(root,text="Total profit:").grid(row=18,column=20,padx=2,pady=2,sticky='e')
pf=tk.DoubleVar()
pfLabel=tk.Label(root,textvariable=pf,bg="black",fg="green",font="bold").grid(row=18,column=21,padx=2,pady=2,sticky='we',columnspan=3)
unit7Label=tk.Label(root,text="[$]").grid(row=18,column=25,padx=2,pady=2,sticky='we',columnspan=3)


#calculations
def cal():
    #Formulats
    c=float(capital.get())
    p=float(drp.get())
    d=float((c*p)/100)
    e=float(rtp.get())
    
    da.set(d)
    tad.set(d*30)
    rf.set(d*30*(e/100))
    pf.set((d*30-(d*30*(e/100)))-c)

#Calculation Button
BtnCal=tk.Button(root,text="Calculate", width=10,command=cal).grid(row=17,column=0,columnspan=10)


#Blank Lines
blanklineLabel=tk.Label(root,text="").grid(row=20,column=0)
blanklineLabel=tk.Label(root,text="").grid(row=21,column=0)
blanklineLabel=tk.Label(root,text="").grid(row=22,column=0)

tk.Label(root,text="Release date: 05 Dec 2020",font=('bold',8),justify='center').grid(row=24,column=0,columnspan=30)
tk.Label(root,text="For any feedback,contact Jerry TSIBA at JerryTsiba@gmail.com  !",font=('bold',8),justify='center').grid(row=25,column=0,columnspan=30)


root.mainloop()