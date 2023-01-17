import tkinter as tk
import time
from time import gmtime, strftime

root = tk.Tk()
root.title('Notes App')
root.geometry("600x400")
message = tk.StringVar()


def readFromFile():
    print("Your notes are: \n")
    textFile = open('file.txt', 'r')
    listOfLines = textFile.readlines()

    for line in listOfLines:
        print(line)

    textFile.close()


def writeToFile():
    textFile = open('file.txt', 'a')
    listOfWords = []

    line = message.get()
    listOfWords.append(line)
    listOfWords.append(',')

    currentTime = time.time()
    finalTime = strftime("%a, %d %b %Y %H:%M", gmtime(currentTime))
    listOfWords.append("This note was added on: ")
    listOfWords.append(finalTime)
    listOfWords.append("\n")

    textFile.writelines(listOfWords)
    textFile.close()

    message.set("")
    print("Note successfully added")


name_label = tk.Label(root, text='Enter your note: ',font=('calibre', 10, 'bold'))
name_entry = tk.Entry(root, textvariable=message,width=40, font=('calibre', 10, 'normal'))
add_btn = tk.Button(root, text='Add note', command=writeToFile)
show_btn = tk.Button(root, text='Show all notes', command=readFromFile)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
add_btn.grid(row=1, column=0)
show_btn.grid(row=1, column=1)

root.mainloop()
