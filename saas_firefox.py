#!/usr/bin/python36

print("content-type: text/html")
print("")

import subprocess
import crypt
import getpass
import cgi


form = cgi.FieldStorage()
usr = form.getvalue('usr')
port = form.getvalue('port')

#usr = input("enter new user you want to add : ")
#port = input("enter a number (1024 - 65000) : ")

passw = "iuc"
passw = crypt.crypt(passw)
a=subprocess.getstatusoutput("sudo useradd -p '"+passw+"' "+usr)

if a[0] == 0:
	b = subprocess.getstatusoutput("docker run -dit -p {1}:22 --name {0} firefox_test:v1".format(usr , port))

#	b = subprocess.getstatusoutput("docker run -dit --ipc=host --net=host --env=DISPLAY --volume=$HOME/.Xauthority:/root/.Xauthority --name={0} centos_net:v1  firefox".format(usr))

	if b[0] == 0:
		print("Firefox is ready, run this script in your terminal !!!!!!!!  \n\n\n")

		#print("docker run -dit --ipc=host --net=host --env=DISPLAY --volume=$HOME/.Xauthority:/root/.Xauthority --name={0} centos_net:v1 firefox".format(usr))
		#print("\n\nssh {0}@192.168.43.7 -t -X 'docker start {0};sleep 5000' ".format(usr))

		print("\n \n ssh 192.168.43.7 -p {} -X firefox".format(port))
		print("\n \n YOUR DEFAULT PASSWORD IS 'iuc'")
	else:
		print("user name or number already exits, try again!!!")    

else:
       input("user name already exits, TRY AGAIN") 
       


print("for windows")

print ("user name for login: {0}".format(usr))
print("\n \n YOUR DEFAULT PASSWORD IS 'iuc'")



print("\n \n DOWNLOAD MOBAEXTREAM FROM HERE!!!!! ")

print("\n \n Click on start local terminal and wait for terminal to arrive")

print("\n \n copy the following command")

print(("\n \n ssh {0}@192.168.43.7 -X firefox".format(usr))

print("\n \n enter your password")












	

