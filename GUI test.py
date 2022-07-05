from tkinter import *
from tkinter import ttk

converter = Tk()
converter.title("Unit Converter")
converter.geometry("500x400")

OPTIONS = {
    "Australian Dollar": 3.04,
    "British Pound": 5.35,
    "Chinese Yuan": 0.66,
    "Euro":4.61,
    "Indonesian Rupiah":0.0029,
    "Japanese Yen":0.032,
    "Pakistani Rupee":0.02,
    "Swiss Franc":4.60,
    "US Dollar":4.42
        }

def ok():
    price = ringgit.get()
    answer = variable1.get()
    DICT = OPTIONS.get(answer,None)
    converted = float(DICT)*float(price)
    result.delete(1.0,END)
    result.insert(INSERT,"Price in ",INSERT,answer,INSERT," = ",INSERT,converted)
appName = Label(converter,text="Currency Converter",font=("arial",25,"bold","underline"),fg="dark red")
appName.place(x=150, y=10)

result = Text(converter,height=5,width=50,font=("arial",10,"bold"),bd=5)
result.place(x=125, y=60)

india = Label(converter,text="Value in indian Rupees:",font=("arial",10,"bold"),fg="red")
india.place(x=30, y=165)

rupees = Entry(converter,font=("arial",20))
rupees.place(x=200, y=160)

choice = Label(converter,text="Choice:",font=("arial",10,"bold"),fg="red")
choice.place(x=30, y=220)

variable1 = StringVar(converter)
variable1.set(None)
option = OptionMenu(converter,variable1,*OPTIONS)
option.place(x=100 , y=210,width=100, height=40)

button = Button(converter,text="Convert",fg="green",font=("arial",20),bg="powder blue",command=ok)
button.place(x=200, y=210,height=40,width=150)








converter.mainloop()
