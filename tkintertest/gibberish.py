from Tkinter import *
import ScrolledText
from random import randint
import tkMessageBox
import socket

class Gibberish:
    def __init__(self, root, ip):
        root.title("Gibberish")
        root.geometry("665x460")
        self.user = "guest" + str(randint(0, 9999))

        displayWindow = ScrolledText.ScrolledText(root)
        chatSend = Button(root, text="Send")

        nick_button = Button(root, text="Confirm")
        nick_label = Label(root, text="Chose a nickname: ")
        nickEntry = Entry(root)
        nick_label.grid(row=0, column=1, sticky=E)
        nickEntry.grid(row=0, column=2)
        nick_button.grid(row=0, column=2, sticky=E)
        currentIP = ip
        ip_label = Label(root, text="your IP: ")
        ip_label.grid(row=0, column=0, sticky=W)
        ip_text = Label(root, text=currentIP)

        ip_text.grid(row=0, column=0, sticky=E)
        chatSend.grid(row=0, column=0, sticky=W)
        chatEntry = Text(root, height=2, width=70, relief="groove")

        displayWindow.grid(row=1, columnspan=3, sticky=E)
        chatSend.grid(row=2, column=2, sticky=E)
        chatEntry.grid(row=2, columnspan=3, sticky=W)
        chatSend.config(height=2, width=10)
        messages_frame = Frame(root)

        def retrieve_nick(event):
            self.user = str(nickEntry.get())
            nickEntry.delete(0, 'end')

        nick_button.bind("<Button-1>", retrieve_nick)

        def retrieve_input(event):
            input = chatEntry.get("1.0", "end-1c")
            print input
            chatEntry.delete('1.0', END)

            displayWindow.insert(INSERT, self.user + ": " + '%s\n' % input)

        chatSend.bind("<Button-1>", retrieve_input)
        root.bind('<Return>', retrieve_input)

        def on_closing():
            if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)


root = Tk()
ip = str(socket.gethostbyname(socket.gethostname()))

Gibberish(root, ip)
root.resizable(False, False)




root.mainloop()
