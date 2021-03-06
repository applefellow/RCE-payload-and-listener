#server
#first of all import the socket library 
import socket  
import progressbar
import random
import os  
import time 
from tqdm import tqdm
import pyglet
from playsound import playsound  
import sys
import hashlib      
from pyfiglet import Figlet
os.system('clear')
full=[]
count=0
server_loading=0
a="program loading..."
for i in range(len(a)):
    os.system("clear")
    print(a[:i])
    time.sleep(0.1)
for i in tqdm(range(100)):
    time.sleep(0.01)
for word1 in range(130000):
    count+=1
    word1 =str(word1*2)
    word2 =str(word1*3)
    word3 =str(word1*4)
    word4 =str(word1*5)
    result1 = hashlib.md5(word1.encode())
    result2 = hashlib.md5(word2.encode())
    result3 = hashlib.md5(word3.encode())
    result4 = hashlib.md5(word4.encode())
    final1 = result1.hexdigest() 
    final2= result2.hexdigest()
    final3 = result3.hexdigest()
    final4 = result4.hexdigest()
    full.append(final1)
    full.append(final2)
    full.append(final3)
    full.append(final4)
    if count <= 12500:
        print ("      ",final1[0:16],final1[17:32],final2[0:16],final2[17:32],final3[0:16],final3[17:32],final4[0:16],final4[17:32],"  ")
    elif count <= 25000:
        print ("      ",final1[0:14],' ',final1[17:30],' ',final2[0:14],' ',final2[17:30],' ',final3[0:14],' ',final3[17:30],' ',final4[0:14],' ',final4[17:30],"  ")
    elif count <= 40000:
        print ("      ",final1[0:12],'   ',final1[17:29],'   ',final2[0:12],'   ',final2[17:29],'   ',final3[0:12],'   ',final3[17:29],'   ',final4[0:12],'   ',final4[17:29],"  ")
    elif count <= 55000:
        print ("      ",final1[0:10],'     ',final1[17:27],'     ',final2[0:10],'     ',final2[17:27],'     ',final3[0:10],'     ',final3[17:27],'     ',final4[0:10],'     ',final4[17:27],"  " )
    elif count <= 70000:
        print ("      ",final1[0:8],'       ',final1[17:25],'       ',final2[0:8],'       ',final2[17:25],'       ',final3[0:8],'       ',final3[17:25],'       ',final4[0:8],'       ',final4[17:25],"  ")
    elif count <= 85000:
        print ("      ",final1[0:6],'         ',final1[17:23],'         ',final2[0:6],'         ',final2[17:23],'         ',final3[0:6],'         ',final3[17:23],'         ',final4[0:6],'         ',final4[17:23],"  ")
    elif count <= 100000:
        print ("      ",final1[0:4],'           ',final1[17:21],'           ',final2[0:4],'           ',final2[17:21],'           ',final3[0:4],'           ',final3[17:21],'           ',final4[0:4],'           ',final4[17:21],"  ")
    elif count <= 112500:
        print ("      ",final1[0:2],'             ',final1[17:19],'             ',final2[0:2],'             ',final2[17:19],'             ',final3[0:2],'             ',final3[17:19],'             ',final4[0:2],'             ',final4[17:19],"  ")
    elif count <=125000:
        print ("      ",final1[0:1],'               ',final1[17:18],'               ',final2[0:1],'               ',final2[17:18],'               ',final3[0:1],'               ',final3[17:18],'               ',final4[0:1],'               ',final4[17:18],"  ")
    elif count == 130000:
        os.system('clear')
time.sleep(1)
filename='server'
file=open(filename,"r")
for line in file:
    a=line.strip('\n')
    print(a)
    time.sleep(0.1)
print("\n")
s = socket.socket()        
print("Socket successfully created")
port = random.randint(1,65535)
s.bind(('', port))         
print("socket binded to %s" %(port)) 
s.listen(5)    
print("socket is listening...")            
while True: 
  c, addr = s.accept()     
  print('Got connection from', addr)  
c.send('Thank you for connecting') 
c.close() 
                  
