import os
import socket

userlogin = os.getlogin()
username = ""
operatingSystem = socket.gethostname()
homedirectory = os.environ['HOME']

print(userlogin)
print(username)
print(operatingSystem)
print(homedirectory)

def stringIsAdmin(sentence):
    '''String -> Booléen'''
    return "admin" in sentence.lower() 
        
