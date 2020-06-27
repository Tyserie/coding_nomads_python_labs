'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
#This program prints hostname, private and public IP of windows server.

# Importing libraries
import socket
import urllib.request

def get_Host_name():
    def get_the_values():
        try:
            host_name = socket.gethostname()
            return host_name
        except:
            return "Unable to get Hostname"
    x = get_the_values()
    return x

def get_IP():
    def get_the_values():
        try:
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            return host_ip
        except:
            return "Unable to get IP"
    x = get_the_values()
    return x

def get_Public_IP():
    def get_the_values():
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        return external_ip
    x = get_the_values()
    return x

print(f"Hostname of this server is: {get_Host_name()}")
print(f"Private IP of this server is: {get_IP()}")
print(f"Public IP of this server is: {get_Public_IP()}")
