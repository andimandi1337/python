import socket
input_menu = input("Enter DNS or IP depending which you want to enter. \n")

if input_menu == "DNS":
    input_dns = input("Enter the DNS you would like to lookup: \n" )
    ip = socket.gethostbyname(input_dns)
    print(ip)
elif input_menu == "IP":
    input_ip = input("Enter the IP you would like to lookup: \n")
    address = socket.getfqdn(input_ip)
    print(address)
else: print("Invalid Input :(")