import tkinter as tk
import smtplib
# import ssl

root = tk.Tk()
root.title('Sending email')
root.geometry("600x400")
receiver_email = tk.StringVar()
message = tk.StringVar()


def sendEmail():

    email = receiver_email.get()
    msg = message.get()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("ashutoshusingpython@gmail.com", 'qqwueudhurjnurtr')
        print("Login successfull")

        server.sendmail("ashutoshusingpython@gmail.com", email, msg)
        print("Email sent successfully")

    except Exception as e:
        print(e)
    finally:
        server.quit()


name_label = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))
name_entry = tk.Entry(root, textvariable=receiver_email, width=40, font=('calibre', 10, 'normal'))
mwssage_label = tk.Label(root, text='Message', font=('calibre', 10, 'bold'))
message_entry = tk.Entry(root, textvariable=message, width=40, font=('calibre', 10, 'normal'))
sub_btn = tk.Button(root, text='Send', command=sendEmail)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
mwssage_label.grid(row=1, column=0)
message_entry.grid(row=1, column=1)
sub_btn.grid(row=3, column=1)

root.mainloop()