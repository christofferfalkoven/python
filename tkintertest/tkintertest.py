# from Tkinter import *
# import ScrolledText
#
# root = Tk()
#
# # theLable = Label(root, text="hello this is shit")
# # theLable.pack()
# # topFrame = Frame(root)
# # topFrame.pack()
# # bottomFrame = Frame(root)
# # bottomFrame.pack(side=BOTTOM)
#
# # button1 = Button(topFrame, text="Button one", fg="red")
# # button2 = Button(topFrame, text="Button two", fg="blue")
# # button3 = Button(topFrame, text="Button three", fg="green")
# # button4 = Button(bottomFrame, text="Button four", fg="purple")
# # button1.pack(side=LEFT)
# # button2.pack(side=LEFT)
# # button3.pack(side=LEFT)
# # button4.pack(side=BOTTOM)
# # fg= foreground, aka label color
# # bg = background, aka background.
#
# # one = Label(root, text="ONE", bg="black", fg="white")
# # one.pack()
# # two = Label(root, text="TWO", bg="white", fg="black")
# # two.pack(fill=X)
# # three = Label(root, text="THREE", bg="blue", fg="white")
# # three.pack(side=LEFT, fill=Y)
# # four = Label(root, text="FOUR", bg="yellow", fg="black")
# # four.pack(fill=BOTH, expand=True)
#
# # label_1 = Label(root, text="Name")
# # label_2 = Label(root, text="Password")
# # entry_1 = Entry(root)
# # entry_2 = Entry(root)
# # # N, E, S, W = north east, south, west
# # label_1.grid(row=0, sticky=E)
# # label_2.grid(row=1, sticky=E)
# # entry_1.grid(row=0, column=1)
# # entry_2.grid(row=1, column=1)
# #
# # c = Checkbutton(root, text="Keep me logged in")
# # c.grid(columnspan=2)
#
# # def printName(event):
# #     print("hello there mydude")
# #
# #
# # button_1 = Button(root, text="Print name")
# # # button_1 = Button(root, text="Print name", command=printName)
# # button_1.bind("<Button-1>", printName)
# # button_1.pack()
#
# # scrollBar
# class Gibberish():
#    def __init__:

from Tkinter import *
import ScrolledText
from random import randint

root = Tk()
root.title("Gibberish")

displayWindow = ScrolledText.ScrolledText(root)
chatSend = Button(root, text="Send")

nick_button = Button(root, text="Confirm")
nick_label = Label(root, text="Chose a nickname: ")
nickEntry = Entry(root)
nick_label.grid(row=0,column=1, sticky=E)
nickEntry.grid(row=0, column=2)
nick_button.grid(row=0, column=2, sticky=E)
currentIP = "123.123.000.000"
ip_label = Label(root, text="your IP: ")
ip_label.grid(row=0, column=0, sticky=W)
ip_text = Label(root, text=currentIP)

ip_text.grid(row=0, column=0, sticky=E)
chatSend.grid(row=0, column=0, sticky=W)
chatEntry = Text(root, height=2, width=70)

displayWindow.grid(row=1, columnspan=3, sticky=E)
chatSend.grid(row=2, column=2, sticky=E)
chatEntry.grid(row=2, columnspan=3, sticky=W)
chatSend.config(height=2, width=10)
messages_frame = Frame(root)

user = "guest" + str(randint(0, 9999))


def retrieve_nick(event):
    global user
    print user
    user = str(nickEntry.get())
    nickEntry.delete(0, 'end')


nick_button.bind("<Button-1>", retrieve_nick)


def retrieve_input(event):
    input = chatEntry.get("1.0", "end-1c")
    print input
    chatEntry.delete('1.0', END)
    displayWindow.insert(INSERT, user + ": " + '%s\n' % input)


chatSend.bind("<Button-1>", retrieve_input)

root.mainloop()
