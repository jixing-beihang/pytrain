from tkinter import *
from tkinter import messagebox

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLable = Label(self, text='Hello Wolrd')
#         self.helloLable.pack()
#         self.quitButton = Button(self, text='quit', command=self.quit())
#         self.quitButton.pack()
#
#
# app = Application()
# app.master.title('Hello World')
# app.mainloop()


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'World'
        messagebox.showinfo('Message', 'Hello %s' % name)


app = Application()
app.master.title('Hello World')
app.mainloop()
