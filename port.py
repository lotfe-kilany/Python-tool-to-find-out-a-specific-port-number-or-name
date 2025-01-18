import socket

port = input("Enter Name Or Number The Port:")

if port.isdigit():
    port = int(port)
    service = socket.getservbyport(port)
    print(service)
elif isinstance(port, str):
    service = socket.getservbyname(port)
    print(service)
else:
    print("ERROR")