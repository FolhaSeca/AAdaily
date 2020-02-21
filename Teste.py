from tkinter import *

class Myapp:
    def __init__(self, AAdaily):
        AAdaily.title('ArcheAge Daily')
        AAdaily.geometry('1280x720')

        self.label_abyssal = Label(AAdaily,
                                   text='Abyssal',
                                   font='Arial 16')

        self.label_aegis = Label(AAdaily,
                                 text='Aegis',
                                 font='Arial 16')

        self.label_whalesong = Label(AAdaily,
                                     text='Whalesong',
                                     font='Arial 16')

        self.label_hiramdaily = Label(AAdaily,
                                      text='Hiram Daily',
                                      font='Arial 16')

        self.label_cr = Label(AAdaily,
                              text='CR',
                              font='Arial 16')

        self.label_gr = Label(AAdaily,
                              text='GR',
                              font='Arial 16')

        self.label_halcyona = Label(AAdaily,
                                    text='Halcyona',
                                    font='Arial 16')

        self.label_dgsolo = Label(AAdaily,
                                  text='Dg solo',
                                  font='Arial 16')

        self.label_noryeti = Label(AAdaily,
                                   text='Noryeti',
                                   font='Arial 16')

        self.button_abyssal = Button(AAdaily,
                                     text='X',
                                     font='Arial 20',
                                     bg='red')
        self.button_abyssal.bind('<Button-1>', self.muda_cor_abyssal)

        self.button_aegis = Button(AAdaily,
                                   text='X',
                                   font='Arial 20',
                                   bg='red')
        self.button_aegis.bind('<Button-1>', self.muda_cor_aegis)

        self.button_whalesong = Button(AAdaily,
                                       text='X',
                                       font='Arial 20',
                                       bg='red')
        self.button_whalesong.bind('<Button-1>', self.muda_cor_whalesong)

        self.button_hiramdaily = Button(AAdaily,
                                        text='X',
                                        font='Arial 20',
                                        bg='red')
        self.button_hiramdaily.bind('<Button-1>', self.muda_cor_hiramdaily)

        self.button_cr = Button(AAdaily,
                                text='X',
                                font='Arial 20',
                                bg='red')
        self.button_cr.bind('<Button-1>', self.muda_cor_cr)

        self.button_gr = Button(AAdaily,
                                text='X',
                                font='Arial 20',
                                bg='red')
        self.button_gr.bind('<Button-1>', self.muda_cor_gr)

        self.button_halcyona = Button(AAdaily,
                                      text='X',
                                      font='Arial 20',
                                      bg='red')
        self.button_halcyona.bind('<Button-1>', self.muda_cor_halcyona)

        self.button_dgsolo = Button(AAdaily,
                                      text='X',
                                      font='Arial 20',
                                      bg='red')
        self.button_dgsolo.bind('<Button-1>', self.muda_cor_dgsolo)

        self.button_noryeti = Button(AAdaily,
                                      text='X',
                                      font='Arial 20',
                                      bg='red')
        self.button_noryeti.bind('<Button-1>', self.muda_cor_noryeti)

        self.button_abyssal.grid(row=1, column=0,)
        self.button_aegis.grid(row=1, column=1)
        self.button_whalesong.grid(row=1, column=2)
        self.button_hiramdaily.grid(row=1, column=3)
        self.button_cr.grid(row=1, column=4,)
        self.button_gr.grid(row=1, column=5,)
        self.button_halcyona.grid(row=1, column=6)
        self.button_dgsolo.grid(row=1, column=7)
        self.button_noryeti.grid(row=1, column=8)

        self.label_abyssal.grid(row=0, column=0, ipadx=20)
        self.label_aegis.grid(row=0, column=1, ipadx=20)
        self.label_whalesong.grid(row=0, column=2, ipadx=20)
        self.label_hiramdaily.grid(row=0, column=3, ipadx=20)
        self.label_cr.grid(row=0, column=4, ipadx=20)
        self.label_gr.grid(row=0, column=5, ipadx=20)
        self.label_halcyona.grid(row=0, column=6, ipadx=20)
        self.label_dgsolo.grid(row=0, column=7, ipadx=20)
        self.label_noryeti.grid(row=0, column=8, ipadx=20)

    def muda_cor_abyssal(self, event):
        if self.button_abyssal['bg'] == 'red':
            self.button_abyssal['bg'] = 'green'
        if self.button_abyssal['text'] == 'X':
            self.button_abyssal['text'] = 'C'
        else:
            self.button_abyssal['bg'] = 'red'
            self.button_abyssal['text'] = 'X'

    def muda_cor_aegis(self, event):
        if self.button_aegis['bg'] == 'red':
            self.button_aegis['bg'] = 'green'
        if self.button_aegis['text'] == 'X':
            self.button_aegis['text'] = 'C'
        else:
            self.button_aegis['bg'] = 'red'
            self.button_aegis['text'] = 'X'

    def muda_cor_whalesong(self, event):
        if self.button_whalesong['bg'] == 'red':
            self.button_whalesong['bg'] = 'green'
        if self.button_whalesong['text'] == 'X':
            self.button_whalesong['text'] = 'C'
        else:
            self.button_whalesong['bg'] = 'red'
            self.button_whalesong['text'] = 'X'

    def muda_cor_hiramdaily(self, event):
        if self.button_hiramdaily['bg'] == 'red':
            self.button_hiramdaily['bg'] = 'green'
        if self.button_hiramdaily['text'] == 'X':
            self.button_hiramdaily['text'] = 'C'
        else:
            self.button_hiramdaily['bg'] = 'red'
            self.button_hiramdaily['text'] = 'X'

    def muda_cor_cr(self, event):
        if self.button_cr['bg'] =='red':
            self.button_cr['bg'] = 'green'
        if self.button_cr['text'] == 'X':
            self.button_cr['text'] = 'C'
        else:
            self.button_cr['bg'] = 'red'
            self.button_cr['text'] = 'X'

    def muda_cor_gr(self, event):
        if self.button_gr['bg'] == 'red':
            self.button_gr['bg'] = 'green'
        if self.button_gr['text'] == 'X':
            self.button_gr['text'] = 'C'
        else:
            self.button_gr['bg'] = 'red'
            self.button_gr['text'] = 'X'

    def muda_cor_halcyona(self, event):
        if self.button_halcyona['bg'] == 'red':
            self.button_halcyona['bg'] = 'green'
        if self.button_halcyona['text'] == 'X':
            self.button_halcyona['text'] = 'C'
        else:
            self.button_halcyona['bg'] = 'red'
            self.button_halcyona['text'] = 'X'

    def muda_cor_dgsolo(self, event):
        if self.button_dgsolo['bg'] == 'red':
            self.button_dgsolo['bg'] = 'green'
        if self.button_dgsolo['text'] == 'X':
            self.button_dgsolo['text'] = 'C'
        else:
            self.button_dgsolo['bg'] = 'red'
            self.button_dgsolo['text'] = 'X'

    def muda_cor_noryeti(self, event):
        if self.button_noryeti['bg'] == 'red':
            self.button_noryeti['bg'] = 'green'
        if self.button_noryeti['text'] == 'X':
            self.button_noryeti['text'] = 'C'
        else:
            self.button_noryeti['bg'] = 'red'
            self.button_noryeti['text'] = 'X'



app = Tk()
Myapp(app)
app.mainloop()
