from ipaddress import ip_address
import socket

host = input("Masukkan nama domain : ")
ip_address = socket.gethostbyname(host)

print(f"nama domain : {host}")
print(f"IP Address : {ip_address}")