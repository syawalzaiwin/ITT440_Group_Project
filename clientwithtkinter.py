import socket
from tkinter import *

root = Tk()
root.title("Client")
root.geometry('350x200')

host = '192.168.56.104'
port = 8989

ClientSocket = socket.socket()
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
Response = ClientSocket.recv(2048)

while True:

    lbl1 = Label(root, text = "Convert To Currency (dollar,pound,euro,riyal): ")
    lbl1.grid()

    txt1 = Entry(root, width=10)
    txt1.grid(column =1, row =0)


    lbl2 = Label(root, text = "Enter Ammount: RM ")
    lbl2.grid(column =0, row =1)

    txt2 = Entry (root, width=10)
    txt2.grid(column =1, row =1)

    def clicked():

        ClientSocket.send(str.encode(txt1.get()))

        ClientSocket.send(str.encode(txt2.get()))

        Response = ClientSocket.recv(2048)
        reply = Response.decode('utf-8')
        lbl3 = Label(root, text = reply )
        lbl3.grid(column =0,row =3)
        
    btn = Button(root, text = "CLICK", fg = "red", command=clicked)

    btn.grid(column =1, row =2)


    
    root.mainloop()

ClientSocket.close()
