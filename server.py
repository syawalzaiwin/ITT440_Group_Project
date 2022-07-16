import socket
import sys
from _thread import *

host = '192.168.56.104'
port = 8989
ThreadCount = 0
money = 0

def client_handler(connection):
    connection.send(str.encode('You are now connected to the replay server... Type BYE to stop'))
    while True:
        currency = connection.recv(2048)
        mescur = currency.decode('utf-8')
        
        data = connection.recv(2048).decode()
        ammount = int(data)
        
        if mescur == 'dollar':
            money = ammount * 4.41
            rmoney = round(money, 2)
            reply = f'{rmoney} Dollar US'
            
        if mescur == 'pound':
            money = ammount * 5.34
            rmoney = round(money, 2)
            reply = f'{rmoney} Pound UK'
            
        if mescur == 'euro':
            money = ammount * 4.60
            rmoney = round(money, 2)
            reply = f'{rmoney} Euro'
        
        if mescur == 'riyal':
            money = ammount * 1.18
            rmoney = round(money, 2)
            reply = f'{rmoney} Riyal Saudi'
        
        if mescur == 'australian dollar':
            money = ammount * 3.02
            rmoney = round(money, 2)
            reply = f'{rmoney] AUD'
        
        if mescur == 'none':
            break
         
        connection.send(str.encode(reply))
        connection.close()

def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(client_handler, (Client, ))

def start_server(host, port):
    ServerSocket = socket.socket()
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(f'Server is listing on the port {port}...')
    ServerSocket.listen()

    while True:
        accept_connections(ServerSocket)
start_server(host, port)
