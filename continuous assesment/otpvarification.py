import random 
import smtplib # send mail from sender to user
server = smtplib.SMTP('smtp.gmail.com',587)
server .starttls() #security
server.login('aneraoganesh79@gmail.com',password='gvkd ydvy xofo huxva')
otp = ''.join ([str(random.randint(0,9))for i in range(4)])
msg = 'hello,your otp is '+str(otp)
vr = msg
rc = str(input("Enter receiver's mail: "))
server.sendmail('aneraoganesh79@gmail.com',str(rc),msg)
server.quit()
print(otp)
temp = str(input("Enter received OTP: "))
if(otp==temp):
    print("Verified..!!")
else:
    print(" not verified")