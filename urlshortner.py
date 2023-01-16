import pyshorteners
import tkinter as tk

root = tk.Tk()
root.title('Email shortner')
root.geometry("600x400")
originalURL = tk.StringVar()


def emailShortner():
    longURL = originalURL.get()

    typebitly = pyshorteners.Shortener(api_key='907d50194fef619716d31f1b482917559b12953a')
    shortURL = typebitly.bitly.short(longURL)

    print("The Shortened URL is: " + shortURL)


url_label = tk.Label(root, text='Enter the URL', font=('calibre', 10, 'bold'))
url_entry = tk.Entry(root, textvariable=originalURL,width=40, font=('calibre', 10, 'normal'))
shorten_btn = tk.Button(root, text='Shorten', command=emailShortner)

url_label.grid(row=0, column=0)
url_entry.grid(row=0, column=1)
shorten_btn.grid(row=2, column=1)

root.mainloop()