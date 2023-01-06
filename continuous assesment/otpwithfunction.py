import random #random module to get random integers to create OTP
import input #email and password of sender from another file
import smtplib #simple message transfer protocol#library to send email to users email address

n=6
OTP=""
for i in range(n):
    OTP+=str(random.randint(0,9))

server =smtplib.SMTP('smtp.gmail.com',587)
Senders_email = "aneraoganesh79@gmail.com"
Senders_password= "xxxx xxxx xxxx xxxx"

server.starttls()
server.login(Senders_email, password=Senders_password) 

receivers_name=input("Enter receivers name ")
receivers_email=input("Enter receivers email ")

msg=("Hi "+ receivers_name +"\n"+ str(OTP)+" is your OTP ")
print (msg)
server.sendmail (Senders_email, receivers_email,msg)
server.quit() 
print("email has been sent!")