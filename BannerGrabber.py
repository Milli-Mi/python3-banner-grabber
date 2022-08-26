

import socket

def banner(ip, port):
   s = socket.socket()
   s.connect((ip, int(port)))
   s.settimeout(5)
   print(s.recv(1024).decode("utf-8").rstrip())

def main():
    ip = input("Please enter the IP: ")
    port = str(input("Please enter the port: "))
    banner(ip, port)

main()
