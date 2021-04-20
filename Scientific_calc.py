from tkinter import *
import unicodedata
import time as t


class ScientificCalculator:
    def __init__(self, root, width, height):

        self.GUI_width = width
        self.GUI_height = height
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        x = (self.screen_width / 2) - (self.GUI_width / 2)
        y = (self.screen_height / 2) - (self.GUI_width / 2)
        root.title("Made with " + u"\u2764\ufe0f")
        root.geometry(f"{self.GUI_width}x{self.GUI_height}+{int(x)}+{int(y)}")

    def Structure(self, root):
        self.tf = StringVar()
        self.tf.set("")
        self.button = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.output = Entry(root, textvariable=self.tf, bg="white", fg="black", font="Times 42 bold")
        self.output.pack(fill=X, pady=10, padx=10, ipadx=15)

        # Frames
        frame0 = Frame(root, bg="white", relief=RIDGE, borderwidth=5)
        frame0.pack(padx=20, pady=10, side=TOP, anchor=W)
        frame0A = Frame(root, bg="white", relief=RIDGE, borderwidth=5)
        frame0A.pack(padx=20, pady=5, side=TOP, anchor=W)
        frame0B = Frame(root, bg="white", relief=RIDGE, borderwidth=5)
        frame0B.pack(padx=20, pady=5, side=TOP, anchor=W)

        frame1 = Frame(root, bg="white", relief=RIDGE, borderwidth=5)
        frame1.pack(padx=20, pady=10, side=TOP, anchor=W)
        frame2 = Frame(root, bg="white", relief=RIDGE, borderwidth=5)
        frame2.pack(padx=20, pady=5, side=TOP, anchor=W)
        frame3 = Frame(root, bg="white", relief=RIDGE, borderwidth=5)
        frame3.pack(padx=20, pady=5, side=TOP, anchor=W)
        frame4 = Frame(root, bg="white", relief=RIDGE, borderwidth=5)
        frame4.pack(padx=20, pady=5, side=TOP, anchor=W)
        frameOperator = Frame(root, bg="grey", relief=RIDGE, borderwidth=5)
        frameOperator.pack(padx=20, pady=10, side=TOP, anchor=W)

        self.PIbutton = Button(frame0, text=unicodedata.lookup('GREEK SMALL LETTER PI'), relief=RIDGE, bg="black",
                               fg='white', width=4, height=1,
                               font="times 14 bold")
        self.PIbutton.pack(side=LEFT, padx=5)
        self.PIbutton.bind("<Button-1>", self.click)

        self.Expbutton = Button(frame0, text='e', relief=RIDGE, bg="black", fg='white', width=4, height=1,
                                font="times 14 bold")
        self.Expbutton.pack(side=LEFT, padx=5)
        self.Expbutton.bind("<Button-1>", self.click)

        butsqrt = Button(frame0, text="sqrt", relief=RIDGE, bg="black", fg="white", width=4, height=1,
                         font="Times 14 italic bold")
        butsqrt.pack(side=LEFT, padx=5)
        butsqrt.bind("<Button-1>", self.click)

        butclear = Button(frame0, text="C", relief=RIDGE, bg="black", fg="white", width=4, height=1,
                          font="times 14 italic bold")
        butclear.pack(side=LEFT, padx=5)
        butclear.bind("<Button-1>", self.click)

        Backbutton = Button(frame0, text="<<", relief=RIDGE, bg="black", fg="white", width=4, height=1,
                          font="times 14 bold italic")
        Backbutton.pack(side=LEFT, padx=5)
        Backbutton.bind("<Button-1>", self.click)

        butXpowY = Button(frame0A, text=u'x^y', relief=RIDGE, bg="black", fg="white", width=4, height=1,
                         font="times 14 bold")
        butXpowY.pack(side=LEFT, padx=5)
        butXpowY.bind("<Button-1>", self.click)

        butModX = Button(frame0A, text=u'|x|', relief=RIDGE, bg="black", fg="white", width=4, height=1,
                         font="times 14 italic bold")
        butModX.pack(side=LEFT, padx=5)
        butModX.bind("<Button-1>", self.click)

        butexp = Button(frame0A, text=u'exp', relief=RIDGE, bg="black", fg="white", width=4, height=1,
                          font="times 14 bold")
        butexp.pack(side=LEFT, padx=5)
        butexp.bind("<Button-1>", self.click)

        butfactorial = Button(frame0A, text=u'n!', relief=RIDGE, bg="black", fg="white", width=4, height=1,
                          font="times 14 bold")
        butfactorial.pack(side=LEFT, padx=5)
        butfactorial.bind("<Button-1>", self.click)

        butleftbracket = Button(frame0A, text=u'(', relief=RIDGE, bg="black", fg="white", width=4, height=1,
                          font="times 14 bold")
        butleftbracket.pack(side=LEFT, padx=5)
        butleftbracket.bind("<Button-1>", self.click)


        self.TenPowxbutton = Button(frame0B, text=u'10^x', relief=RIDGE, bg="black", fg='white', width=4, height=1,
                                 font="times 14 italic bold")
        self.TenPowxbutton.pack(side=LEFT, padx=5)
        self.TenPowxbutton.bind("<Button-1>", self.click)

        self.SinXbutton = Button(frame0B, text=u'sin', relief=RIDGE, bg="black", fg='white', width=4, height=1,
                                 font="times 14 italic bold")
        self.SinXbutton.pack(side=LEFT, padx=5)
        self.SinXbutton.bind("<Button-1>", self.click)

        self.CosXbutton = Button(frame0B, text=u'cos', relief=RIDGE, bg="black", fg='white', width=4, height=1,
                                 font="times 14 italic bold")
        self.CosXbutton.pack(side=LEFT, padx=5)
        self.CosXbutton.bind("<Button-1>", self.click)

        self.TanXbutton = Button(frame0B, text=u'tan', relief=RIDGE, bg="black", fg='white', width=4, height=1,
                                 font="times 14 italic bold")
        self.TanXbutton.pack(side=LEFT, padx=5)
        self.TanXbutton.bind("<Button-1>", self.click)

        butrightbracket = Button(frame0B, text=u')', relief=RIDGE, bg="black", fg="white", width=4, height=1,
                          font="times 14 bold")
        butrightbracket.pack(side=LEFT, padx=5)
        butrightbracket.bind("<Button-1>", self.click)

        self.Cubebutton = Button(frame2, text=u'x\u00b3', relief=RIDGE, bg="black", fg='white', width=4, height=1,
                                 font="times 14 italic")
        self.Cubebutton.pack(side=LEFT, padx=5)
        self.Cubebutton.bind("<Button-1>", self.click)

        self.reciprocalButton = Button(frame3, text=u'1/x', relief=RIDGE, bg="black", fg='white', width=4, height=1,
                                       font="times 14 italic")
        self.reciprocalButton.pack(side=LEFT, padx=5)
        self.reciprocalButton.bind("<Button-1>", self.click)

        self.logButton = Button(frame4, text=u'log', relief=RIDGE, bg="black", fg='white', width=4, height=1,
                                font="times 14 italic")
        self.logButton.pack(side=LEFT, padx=5)
        self.logButton.bind("<Button-1>", self.click)

        self.lnButton = Button(frameOperator, text=u'ln', relief=RIDGE, bg="black", fg='white', width=4, height=1,
                               font="times 14 italic")
        self.lnButton.pack(side=LEFT, padx=5)
        self.lnButton.bind("<Button-1>", self.click)

        # Number Buttons

        for i in range(0, 10):
            if 0 < i < 4:
                self.button[i] = Button(frame2, text=f"{i}", relief=RIDGE, bg="white", width=4, height=1,
                                        font="times 14 bold")
                self.button[i].pack(side=LEFT, padx=5)
                self.button[i].bind("<Button-1>", self.click)
            elif 4 <= i < 7:
                self.button[i] = Button(frame3, text=f"{i}", relief=RIDGE, bg="white", width=4, height=1,
                                        font="times 14 bold")
                self.button[i].pack(side=LEFT, padx=5)
                self.button[i].bind("<Button-1>", self.click)
            elif 7 <= i < 10:
                self.button[i] = Button(frame4, text=f"{i}", relief=RIDGE, bg="white", width=4, height=1,
                                        font="times 14 bold")
                self.button[i].pack(side=LEFT, padx=5)
                self.button[i].bind("<Button-1>", self.click)
            else:

                self.button[i] = Button(frameOperator, text=f"{i}", relief=RIDGE, bg="white", width=9, height=1,
                                        font="times 14 bold")
                self.button[i].pack(side=LEFT, padx=8)
                self.button[i].bind("<Button-1>", self.click)

        # Other Buttons



        butsub = Button(frame2, text="-", relief=RIDGE, bg="orange", fg="white", width=4, height=1,
                        font="times 14 bold")
        butsub.pack(side=RIGHT, padx=5)
        butsub.bind("<Button-1>", self.click)

        butmult = Button(frame3, text="X", relief=RIDGE, bg="orange", fg="white", width=4, height=1,
                         font="times 14 bold")
        butmult.pack(side=TOP, padx=5)
        butmult.bind("<Button-1>", self.click)

        butdivide = Button(frame4, text="/", relief=RIDGE, bg="orange", fg="white", width=4, height=1,
                           font="times 14 bold")
        butdivide.pack(side=TOP, padx=5)
        butdivide.bind("<Button-1>", self.click)

        butdecimle = Button(frameOperator, text=".", relief=RIDGE, bg="cyan", width=4, height=1, font="times 14 bold")
        butdecimle.pack(side=LEFT, padx=5)
        butdecimle.bind("<Button-1>", self.click)

        butequals = Button(frameOperator, text="=", relief=RIDGE, bg="orange", fg="white", width=4, height=1,
                           font="times 14 bold")
        butequals.pack(side=TOP, padx=5)
        butequals.bind("<Button-1>", self.click)

        butsquare = Button(frame1, text=u'x\u00b2', relief=RIDGE, bg="black", fg="white", width=4, height=1,
                           font="times 14 italic")
        butsquare.pack(side=LEFT, padx=5)
        butsquare.bind("<Button-1>", self.click)

        butclear = Button(frame1, text="C", relief=RIDGE, bg="orange", fg="white", width=4, height=1,
                          font="times 14 bold")
        butclear.pack(side=LEFT, padx=5)
        butclear.bind("<Button-1>", self.click)

        butremainder = Button(frame1, text="%", relief=RIDGE, bg="orange", fg="white", width=4, height=1,
                              font="times 14 bold")
        butremainder.pack(side=LEFT, padx=5)
        butremainder.bind("<Button-1>", self.click)

        self.butpower = Button(frame1, text="OFF", relief=RIDGE, bg="red", fg="white", width=4, height=1,
                               font="times 14 bold")
        self.butpower.pack(side=LEFT, padx=5)
        self.butpower.bind("<Button-1>", self.click)

        butAdd = Button(frame1, text="+", relief=RIDGE, bg="orange", fg="white", width=4, height=1,
                        font="times 14 bold")
        butAdd.pack(side=LEFT, padx=5)
        butAdd.bind("<Button-1>", self.click)

    def welcome(self):
        import time as t
        self.tf.set("W")
        self.output.update()
        self.button[1]['bg'] = 'cyan'
        self.button[1].update()
        t.sleep(0.2)
        self.tf.set("We")
        self.button[1]['bg'] = 'white'
        self.button[1].update()
        self.button[2]['bg'] = 'cyan'
        self.button[2].update()
        self.output.update()
        t.sleep(0.2)
        self.tf.set("Wel")
        self.output.update()
        self.button[2]['bg'] = 'white'
        self.button[2].update()
        self.button[3]['bg'] = 'cyan'
        self.button[3].update()
        t.sleep(0.2)
        self.tf.set("Welc")
        self.output.update()
        self.button[3]['bg'] = 'white'
        self.button[3].update()
        self.button[4]['bg'] = 'cyan'
        self.button[4].update()
        t.sleep(0.2)
        self.tf.set("Welco")
        self.output.update()
        self.button[4]['bg'] = 'white'
        self.button[4].update()
        self.button[5]['bg'] = 'cyan'
        self.button[5].update()
        t.sleep(0.2)
        self.tf.set("Welcom")
        self.output.update()
        self.button[5]['bg'] = 'white'
        self.button[5].update()
        self.button[6]['bg'] = 'cyan'
        self.button[6].update()
        t.sleep(0.2)
        self.tf.set("Welcome")
        self.output.update()
        self.button[6]['bg'] = 'white'
        self.button[6].update()
        self.button[7]['bg'] = 'cyan'
        self.button[7].update()
        t.sleep(0.2)
        self.tf.set("Welcome.")
        self.output.update()
        self.button[7]['bg'] = 'white'
        self.button[7].update()
        self.button[8]['bg'] = 'cyan'
        self.button[8].update()
        t.sleep(0.2)
        self.tf.set("Welcome..")
        self.output.update()
        self.button[8]['bg'] = 'white'
        self.button[8].update()
        self.button[9]['bg'] = 'cyan'
        self.button[9].update()
        t.sleep(0.2)
        self.tf.set("Welcome...")
        self.output.update()
        self.button[9]['bg'] = 'white'
        self.button[9].update()
        t.sleep(0.2)
        self.tf.set("Welcome...")
        self.output.update()
        t.sleep(0.2)

        self.tf.set("")
        self.output.update()

    def click(self, event):
        text = event.widget.cget("text")
        if text == "X":
            text = "*"
        if text == "=":
            if self.tf.get().isdigit():
                result = int(self.tf.get())
            else:
                try:
                    result = eval(self.output.get())
                except Exception as e:
                    print(e)
                    result = "Error"
                    self.output.update()

            self.tf.set(result)
            self.output.update()

        elif text == "C":
            self.tf.set("")
            self.output.update()

        elif text == "OFF":
            self.butpower['text'] = "ON"
            self.button[0]['bg'] = 'white'
            self.tf.set("")
            self.output.config(state='disabled')
        elif text == "ON":
            self.output.config(state='normal')
            self.butpower['text'] = "OFF"
            # welcome()

        elif self.butpower['text'] != 'ON':
            self.tf.set(self.tf.get() + text)
            self.output.update()

        else:
            self.tf.set("")


root = Tk()

SC = ScientificCalculator(root, 380, 600)
SC.Structure(root)
root.mainloop()
