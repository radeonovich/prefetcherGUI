import configparser
from pathlib import Path
from tkinter import *
from tkinter import filedialog
import os
config = configparser.ConfigParser()
if Path("./prefetch.ini").is_file():
    config.read("./prefetch.ini")
    print('kek')
else:
    print("No prefetch.ini found!")
section = 'PrefetchFolder'
name = ''


def addPath():
    global name
    directory = inputDirectory.get()
    directory = directory.replace('/', '\\\\')
    name = directory.split('\\\\')[-1]

    if name == '':
        return
    config.set(section, name, directory)
    writeToFile()
    os.startfile('prefetch.exe')

def writeToFile():
    with open('./prefetch.ini', 'w') as configfile:
        config.write(configfile, space_around_delimiters=False)

root = Tk()
root.title('Prefetcher (selector)')
root.geometry('400x70')
root.resizable(width=False, height = False)

def select():
    dir = filedialog.askdirectory()
    inputDirectory.insert(0, dir)


buttonSelect = Button(root, text='Папка...', command=select)
buttonSelect.place(x=340, y=10)

buttonApply = Button(root, text='Применить', command=addPath)
buttonApply.place(x=305, y=40, width=90)

inputDirectory = Entry(root)
inputDirectory.place(x=10, y=15, width=320)
root.mainloop()
