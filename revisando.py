from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('CALCULADORA')
# row 1 : PRIMER NUMERO
numero1_label = Label(root,text="INGRESE SU PRIMER NUMERO:")
numero1_label.grid(row=1,column=1)
numero1_str = StringVar()
numero1_entry = Entry(root,textvariable=numero1_str)
numero1_entry.grid(row=1,column=2)
#row 2 : the last name
numero2_label= Label(root,text="INGRESE SU SEGUNDO NUMERO : ")
numero2_label.grid(row=2,column=1)
numero2_str = StringVar()
numero2_entry = Entry(root,textvariable=numero2_str)
numero2_entry.grid(row=2,column=2)

#FUNCION SUMA Y RESTA 
def Suma():
   n1=float(numero1_entry.get())
   n2=float(numero2_entry.get())
   suma=n1+n2
   messagebox.showinfo("test","LA SUMA ES IGUAL A: %.2f"%suma)
   numero1_entry.delete(0,20)
   numero2_entry.delete(0,20)

def Resta():
   n1=float(numero1_entry.get())
   n2=float(numero2_entry.get())
   resta=n1-n2
   messagebox.showinfo("test","LA RESTA ES IGUAL A: %.2f"%resta)
   numero1_entry.delete(0,20)
   numero2_entry.delete(0,20)

#row 3 : the email
#mail_label = Label(root,text="RESULTADO : ")
#mail_label.grid(row=3,column=1)
#mail_str = StringVar()
#mail_entry = Entry(root,textvariable=mail_str)
#mail_entry.grid(row=3,column=2)
#row 4 : end
suma = Button(root, text = "SUMA", command = Suma, width=15)
suma.grid(row=4,column=2)
resta = Button(root, text = "RESTA", command = Resta, width=15)
resta.grid(row=6, column=2)
root.mainloop()
