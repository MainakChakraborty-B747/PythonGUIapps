from tkinter import *

w=Tk()
w.config(background='orange')
w.title('BMI Calculator')

def submit():
    h=float(entry.get())
    we=float(entry2.get())
    bmi=(we)/((h/100)**2)
    bmi=round(bmi,1)
    l1=Label(w,text=f"Your BMI is {bmi}",font=('Arial',25,'bold'),fg='#4287f5',bg='#ccf069')
    l1.place(x=500,y=290)
    if bmi<(18.5):
        l2=Label(w,text="Status: UNDERWEIGHT",font=('Arial',25,'bold'),fg='#4287f5',bg='#ccf069')
        l2.place(x=500,y=390)
    elif (bmi>=18.5) and (bmi<=24.9):
        l2=Label(w,text="Status: NORMAL WEIGHT",font=('Arial',25,'bold'),fg='#4287f5',bg='#ccf069')
        l2.place(x=500,y=390)
    elif (bmi>=25.0) and (bmi<=29.9):
        l2=Label(w,text="Status: OVERWEIGHT",font=('Arial',25,'bold'),fg='#4287f5',bg='#ccf069')
        l2.place(x=500,y=390)
    elif (bmi>=30.0) and (bmi<=34.9):
        l2=Label(w,text="Status: OBESE CLASS I",font=('Arial',25,'bold'),fg='#4287f5',bg='#ccf069')
        l2.place(x=500,y=390)
    elif (bmi>=35.0) and (bmi<=39.9):
        l2=Label(w,text="Status: OBESE CLASS II",font=('Arial',25,'bold'),fg='#4287f5',bg='#ccf069')
        l2.place(x=500,y=390)
    elif bmi>=40.0:
        l2=Label(w,text="Status: OBESE CLASS III",font=('Arial',25,'bold'),fg='#4287f5',bg='#ccf069')
        l2.place(x=500,y=390)
    
label1=Label(w,text="height(in cms): ",font=('Arial',25,'bold'),fg='#4287f5',bg='#ccf069')
label1.place(x=0,y=0)
entry=Entry(w,font=('Arial',25,'bold'),fg='blue',bg='yellow')
entry.place(x=250,y=0)

label2=Label(w,text="weight(in kg):",font=('Arial',25,'bold'),fg='#4287f5',bg='#ccf069')
label2.place(x=0,y=80)
entry2=Entry(w,font=('Arial',25,'bold'),fg='blue',bg='yellow')
entry2.place(x=250,y=80)
b2=Button(w,text="Submit",command=submit,font=('Arial',15))
b2.place(x=800,y=80)

w.mainloop()
