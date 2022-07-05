import socket

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
    currency = input('Convert To Currency (dollar,pound,euro,riyal): ')
    ClientSocket.send(str.encode(currency))
    
    ammount = input('Enter Ammount: RM')
    ClientSocket.send(str.encode(ammount))
    
    if currency == 'none':
            break
    
    Response = ClientSocket.recv(2048)
    print(Response.decode('utf-8'))
ClientSocket.close()