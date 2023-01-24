import random
import smtplib

n = random.randint(1000, 9999)
print(n)

email = input("Enter your email: ")
message = str(n)


def sendEmail():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("ashutoshusingpython@gmail.com", 'qqwueudhurjnurtr')
        print("Login successfull")

        server.sendmail("ashutoshusingpython@gmail.com", email, message)
        print("Email sent successfully")

    except Exception as e:
        print(e)
    finally:
        server.quit()


sendEmail()

otp = input("Enter the OTP: ")
if (str(otp) == message):
    print("Verification successfull")
else:
    print("Verification unsuccessfull")
