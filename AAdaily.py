from tkinter import *
from datetime import datetime
from time import strftime


class Myapp:
    def __init__(self, AAdaily):
        AAdaily.title('ArcheAge Daily')
        AAdaily.geometry('1280x300')



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
                              text='Crimson Rift',
                              font='Arial 16')

        self.label_gr = Label(AAdaily,
                              text='Grimghast Rift',
                              font='Arial 16')

        self.label_halcyona = Label(AAdaily,
                                    text='\n\nHalcyona',
                                    font='Arial 16')

        self.label_dgsolo = Label(AAdaily,
                                  text='\n\nHowling Abyss',
                                  font='Arial 16')

        self.label_noryette = Label(AAdaily,
                                    text='\n\nNoryette',
                                    font='Arial 16')

        self.label_reddragon = Label(AAdaily,
                                     text='\n\nRed Dragon',
                                     font='Arial 16')

        self.label_castle = Label(AAdaily,
                                  text='\n\nCastle',
                                  font='Arial 16')

        self.label_bluesalt = Label(AAdaily,
                                    text='\n\nBlue Salt',
                                    font='Arial 16')


        self.label_time = Label(AAdaily,
                                text='',
                                font='Arial 30',
                                bg='#DCDCDC')

        def tic():
            rel['text'] = strftime('   Hora   \n   %H:%M:%S   ',)

        def tac():
            tic()
            rel.after(1000, tac)

        rel = self.label_time
        rel.grid(row=1, column=6)
        tac()

        self.button_abyssal = Button(AAdaily,
                                     text='X',
                                     font='Arial 20')
        abyssal = open('doc.txt/abyssal.txt', 'r')
        x = abyssal.read()
        if x == 'red' or x == '':
            self.button_abyssal = Button(AAdaily,
                                         bg='red',
                                         text='X',
                                         font='Arial 20')

        if x == 'green':
            self.button_abyssal = Button(AAdaily,
                                         bg='green',
                                         text='✓',
                                         font='Arial 20')
        self.button_abyssal.bind('<Button-1>', self.muda_cor_abyssal)

        aegis = open('doc.txt/aegis.txt', 'r')
        x = aegis.read()
        if x == 'red' or x == '':
            self.button_aegis = Button(AAdaily,
                                       bg='red',
                                       text='X',
                                       font='Arial 20')
        if x == 'green':
            self.button_aegis = Button(AAdaily,
                                       bg='green',
                                       text='✓',
                                       font='Arial 20')
        self.button_aegis.bind('<Button-1>', self.muda_cor_aegis)

        whalesong = open('doc.txt/whalesong.txt', 'r')
        x = whalesong.read()
        if x == 'red' or x == '':
            self.button_whalesong = Button(AAdaily,
                                           bg='red',
                                           text='X',
                                           font='Arial 20')
        if x == 'green':
            self.button_whalesong = Button(AAdaily,
                                           bg='green',
                                           text='✓',
                                           font='Arial 20')
        self.button_whalesong.bind('<Button-1>', self.muda_cor_whalesong)

        hiram = open('doc.txt/hiramdaily.txt', 'r')
        x = hiram.read()
        if x == 'red' or x == '':
            self.button_hiramdaily = Button(AAdaily,
                                            bg='red',
                                            text='X',
                                            font='Arial 20')
        if x == 'green':
            self.button_hiramdaily = Button(AAdaily,
                                            bg='green',
                                            text='✓',
                                            font='Arial 20')
        self.button_hiramdaily.bind('<Button-1>', self.muda_cor_hiramdaily)

        cr = open('doc.txt/cr.txt', 'r')
        x = cr.read()
        if x == 'red' or x == '':
            self.button_cr = Button(AAdaily,
                                    bg='red',
                                    text='X',
                                    font='Arial 20')
        if x == 'green':
            self.button_cr = Button(AAdaily,
                                    bg='green',
                                    text='✓',
                                    font='Arial 20')
        self.button_cr.bind('<Button-1>', self.muda_cor_cr)

        gr = open('doc.txt/gr.txt', 'r')
        x = gr.read()
        if x == 'red' or x == '':
            self.button_gr = Button(AAdaily,
                                    bg='red',
                                    text='X',
                                    font='Arial 20')
        if x == 'green':
            self.button_gr = Button(AAdaily,
                                    bg='green',
                                    text='✓',
                                    font='Arial 20')
        self.button_gr.bind('<Button-1>', self.muda_cor_gr)

        halcyona = open('doc.txt/halcyona.txt', 'r')
        x = halcyona.read()
        if x == 'red' or x == '':
            self.button_halcyona = Button(AAdaily,
                                          bg='red',
                                          text='X',
                                          font='Arial 20')
        if x == 'green':
            self.button_halcyona = Button(AAdaily,
                                          bg='green',
                                          text='✓',
                                          font='Arial 20')
        self.button_halcyona.bind('<Button-1>', self.muda_cor_halcyona)

        dgsolo = open('doc.txt/dgsolo.txt', 'r')
        x = dgsolo.read()
        if x == 'red' or x == '':
            self.button_dgsolo = Button(AAdaily,
                                        bg='red',
                                        text='X',
                                        font='Arial 20')
        if x == 'green':
            self.button_dgsolo = Button(AAdaily,
                                        bg='green',
                                        text='✓',
                                        font='Arial 20')
        self.button_dgsolo.bind('<Button-1>', self.muda_cor_dgsolo)

        noryette = open('doc.txt/noryette.txt', 'r')
        x = noryette.read()
        if x == 'red' or x == '':
            self.button_noryette = Button(AAdaily,
                                          bg='red',
                                          text='X',
                                          font='Arial 20')
        if x == 'green':
            self.button_noryette = Button(AAdaily,
                                          bg='green',
                                          text='✓',
                                          font='Arial 20')
        self.button_noryette.bind('<Button-1>', self.muda_cor_noryette)

        reddragon = open('doc.txt/reddragon.txt', 'r')
        x = reddragon.read()
        if x == 'red' or x == '':
            self.button_reddragon = Button(AAdaily,
                                           bg='red',
                                           text='X',
                                           font='Arial 20')
        if x == 'green':
            self.button_reddragon = Button(AAdaily,
                                           bg='green',
                                           text='✓',
                                           font='Arial 20')
        self.button_reddragon.bind('<Button-1>', self.muda_cor_reddragon)

        castle = open('doc.txt/castle.txt', 'r')
        x = castle.read()
        if x == 'red' or x == '':
            self.button_castle = Button(AAdaily,
                                        bg='red',
                                        text='X',
                                        font='Arial 20')
        if x == 'green':
            self.button_castle = Button(AAdaily,
                                        bg='green',
                                        text='✓',
                                        font='Arial 20')
        self.button_castle.bind('<Button-1>', self.muda_cor_castle)

        bluesalt = open('doc.txt/bluesalt.txt', 'r')
        x = bluesalt.read()
        if x == 'red' or x == '':
            self.button_bluesalt = Button(AAdaily,
                                          bg='red',
                                          text='X',
                                          font='Arial 20')
        if x == 'green':
            self.button_bluesalt = Button(AAdaily,
                                          bg='green',
                                          text='✓',
                                          font='Arial 20',)
        self.button_bluesalt.bind('<Button-1>', self.muda_cor_bluesalt)

        self.button_reset = Button(AAdaily,
                                   bg='red',
                                   text='Reset',
                                   font='Arial 20',
                                   fg='black')
        self.button_reset.bind('<Button-1>', self.click_reset)

        self.button_abyssal.grid(row=1, column=0,)
        self.button_aegis.grid(row=1, column=1)
        self.button_whalesong.grid(row=1, column=2)
        self.button_hiramdaily.grid(row=1, column=3)
        self.button_cr.grid(row=1, column=4,)
        self.button_gr.grid(row=1, column=5,)
        self.button_halcyona.grid(row=3, column=0)
        self.button_dgsolo.grid(row=3, column=1)
        self.button_noryette.grid(row=3, column=2)
        self.button_reddragon.grid(row=3, column=3)
        self.button_castle.grid(row=3, column=4)
        self.button_bluesalt.grid(row=3, column=5)
        self.button_reset.grid(row=3, column=6)

        self.label_abyssal.grid(row=0, column=0, ipadx=20)
        self.label_aegis.grid(row=0, column=1, ipadx=20)
        self.label_whalesong.grid(row=0, column=2, ipadx=20)
        self.label_hiramdaily.grid(row=0, column=3, ipadx=20)
        self.label_cr.grid(row=0, column=4, ipadx=20)
        self.label_gr.grid(row=0, column=5, ipadx=20)
        self.label_halcyona.grid(row=2, column=0, ipadx=20)
        self.label_dgsolo.grid(row=2, column=1, ipadx=20)
        self.label_noryette.grid(row=2, column=2, ipadx=20)
        self.label_reddragon.grid(row=2, column=3, ipadx=20)
        self.label_castle.grid(row=2, column=4, ipadx=20)
        self.label_bluesalt.grid(row=2, column=5, ipadx=20)


    def muda_cor_abyssal(self, event):
        abyssal = open('doc.txt/abyssal.txt', 'r+')
        x = abyssal.read()

        if x == 'red' or x == '':
            self.button_abyssal['bg'] = 'green'
            self.button_abyssal['text'] = '✓'
            abyssal = open('doc.txt/abyssal.txt', 'w+')
            abyssal.write('green')
            abyssal.close()

        elif x == 'green':
            self.button_abyssal['bg'] = 'red'
            self.button_abyssal['text'] = 'X'
            abyssal = open('doc.txt/abyssal.txt', 'w+')
            abyssal.write('red')
            abyssal.close()

    def muda_cor_aegis(self, event):
        aegis = open('doc.txt/aegis.txt', 'r+')
        x = aegis.read()

        if x == 'red' or x == '':
            self.button_aegis['bg'] = 'green'
            self.button_aegis['text'] = '✓'
            aegis = open('doc.txt/aegis.txt', 'w')
            aegis.write('green')
            aegis.close()
        elif x == 'green':
            self.button_aegis['bg'] = 'red'
            self.button_aegis['text'] = 'X'
            aegis = open('doc.txt/aegis.txt', 'w')
            aegis.write('red')
            aegis.close()

    def muda_cor_whalesong(self, event):
        whalesong = open('doc.txt/whalesong.txt', 'r+')
        x = whalesong.read()

        if x == 'red' or x == '':
            self.button_whalesong['bg'] = 'green'
            self.button_whalesong['text'] = '✓'
            whalesong = open('doc.txt/whalesong.txt', 'w')
            whalesong.write('green')
            whalesong.close()
        elif x == 'green' or x == '':
            self.button_whalesong['bg'] = 'red'
            self.button_whalesong['text'] = 'X'
            whalesong = open('doc.txt/whalesong.txt', 'w')
            whalesong.write('red')
            whalesong.close()

    def muda_cor_hiramdaily(self, event):
        hiram = open('doc.txt/hiramdaily.txt', 'r+')
        x = hiram.read()
        if x == 'red' or x == '':
            self.button_hiramdaily['bg'] = 'green'
            self.button_hiramdaily['text'] = '✓'
            hiram = open('doc.txt/hiramdaily.txt', 'w')
            hiram.write('green')
            hiram.close()
        elif x == 'green':
            self.button_hiramdaily['bg'] = 'red'
            self.button_hiramdaily['text'] = 'X'
            hiram = open('doc.txt/hiramdaily.txt', 'w')
            hiram.write('red')
            hiram.close()

    def muda_cor_cr(self, event):
        cr = open('doc.txt/cr.txt', 'r+')
        x = cr.read()
        if x == 'red' or x == '':
            self.button_cr['bg'] = 'green'
            self.button_cr['text'] = '✓'
            cr = open('doc.txt/cr.txt', 'w')
            cr.write('green')
            cr.close()
        elif x == 'green':
            self.button_cr['bg'] = 'red'
            self.button_cr['text'] = 'X'
            cr = open('doc.txt/cr.txt', 'w')
            cr.write('red')
            cr.close()

    def muda_cor_gr(self, event):
        gr = open('doc.txt/gr.txt', 'r+')
        x = gr.read()
        if x == 'red' or x == '':
            self.button_gr['bg'] = 'green'
            self.button_gr['text'] = '✓'
            gr = open('doc.txt/gr.txt', 'w')
            gr.write('green')
            gr.close()
        elif x == 'green':
            self.button_gr['bg'] = 'red'
            self.button_gr['text'] = 'X'
            gr = open('doc.txt/gr.txt', 'w')
            gr.write('red')
            gr.close()

    def muda_cor_halcyona(self, event):
        halcyona = open('doc.txt/halcyona.txt', 'r+')
        x = halcyona.read()
        if x == 'red' or x == '':
            self.button_halcyona['bg'] = 'green'
            self.button_halcyona['text'] = '✓'
            halcyona = open('doc.txt/halcyona.txt', 'w')
            halcyona.write('green')
            halcyona.close()
        elif x == 'green':
            self.button_halcyona['bg'] = 'red'
            self.button_halcyona['text'] = 'X'
            halcyona = open('doc.txt/halcyona.txt', 'w')
            halcyona.write('red')
            halcyona.close()

    def muda_cor_dgsolo(self, event):
        dgsolo = open('doc.txt/dgsolo.txt', 'r+')
        x = dgsolo.read()
        if x == 'red' or x == '':
            self.button_dgsolo['bg'] = 'green'
            self.button_dgsolo['text'] = '✓'
            dgsolo = open('doc.txt/dgsolo.txt', 'w')
            dgsolo.write('green')
            dgsolo.close()
        elif x == 'green':
            self.button_dgsolo['bg'] = 'red'
            self.button_dgsolo['text'] = 'X'
            dgsolo = open('doc.txt/dgsolo.txt', 'w')
            dgsolo.write('red')
            dgsolo.close()

    def muda_cor_noryette(self, event):
        noryette = open('doc.txt/noryette.txt', 'r+')
        x = noryette.read()
        if x == 'red' or x == '':
            self.button_noryette['bg'] = 'green'
            self.button_noryette['text'] = '✓'
            noryette = open('doc.txt/noryette.txt', 'w')
            noryette.write('green')
            noryette.close()
        elif x == 'green':
            self.button_noryette['bg'] = 'red'
            self.button_noryette['text'] = 'X'
            noryette = open('doc.txt/noryette.txt', 'w')
            noryette.write('red')
            noryette.close()

    def muda_cor_reddragon(self, event):
        reddragon = open('doc.txt/reddragon.txt', 'r+')
        x = reddragon.read()
        if x == 'red' or x == '':
            self.button_reddragon['bg'] = 'green'
            self.button_reddragon['text'] = '✓'
            reddragon = open('doc.txt/reddragon.txt', 'w')
            reddragon.write('green')
            reddragon.close()
        elif x == 'green':
            self.button_reddragon['bg'] = 'red'
            self.button_reddragon['text'] = 'X'
            reddragon = open('doc.txt/reddragon.txt', 'w')
            reddragon.write('red')
            reddragon.close()

    def muda_cor_castle(self, event):
        castle = open('doc.txt/castle.txt', 'r+')
        x = castle.read()
        if x == 'red' or x == '':
            self.button_castle['bg'] = 'green'
            self.button_castle['text'] = '✓'
            castle = open('doc.txt/castle.txt', 'w')
            castle.write('green')
            castle.close()
        elif x == 'green':
            self.button_castle['bg'] = 'red'
            self.button_castle['text'] = 'X'
            castle = open('doc.txt/castle.txt', 'w')
            castle.write('red')
            castle.close()

    def muda_cor_bluesalt(self, event):
        bluesalt = open('doc.txt/bluesalt.txt', 'r+')
        x = bluesalt.read()
        if x == 'red' or x == '':
            self.button_bluesalt['bg'] = 'green'
            self.button_bluesalt['text'] = '✓'
            castle = open('doc.txt/bluesalt.txt', 'w')
            castle.write('green')
            castle.close()
        elif x == 'green':
            self.button_bluesalt['bg'] = 'red'
            self.button_bluesalt['text'] = 'X'
            castle = open('doc.txt/bluesalt.txt', 'w')
            castle.write('red')
            castle.close()

    def click_reset(self, event):
        if self.button_reset:
            abyssal = open('doc.txt/abyssal.txt', 'w')
            aegis = open('doc.txt/aegis.txt', 'w')
            bluesalt = open('doc.txt/bluesalt.txt', 'w')
            castle = open('doc.txt/castle.txt', 'w')
            cr = open('doc.txt/cr.txt', 'w')
            dgsolo = open('doc.txt/dgsolo.txt', 'w')
            gr = open('doc.txt/gr.txt', 'w')
            halcyona = open('doc.txt/halcyona.txt', 'w')
            hiramdaily = open('doc.txt/hiramdaily.txt', 'w')
            noryette = open('doc.txt/noryette.txt', 'w')
            reddragon = open('doc.txt/reddragon.txt', 'w')
            whalesong = open('doc.txt/whalesong.txt', 'w')
            abyssal.write('red')
            abyssal.close()
            self.button_abyssal['bg'] = 'red'
            self.button_abyssal['text'] = 'X'
            aegis.write('red')
            aegis.close()
            self.button_aegis['bg'] = 'red'
            self.button_aegis['text'] = 'X'
            bluesalt.write('red')
            bluesalt.close()
            self.button_bluesalt['bg'] = 'red'
            self.button_bluesalt['text'] = 'X'
            castle.write('red')
            castle.close()
            self.button_castle['bg'] = 'red'
            self.button_castle['text'] = 'X'
            cr.write('red')
            cr.close()
            self.button_cr['bg'] = 'red'
            self.button_cr['text'] = 'X'
            dgsolo.write('red')
            dgsolo.close()
            self.button_dgsolo['bg'] = 'red'
            self.button_dgsolo['text'] = 'X'
            gr.write('red')
            gr.close()
            self.button_gr['bg'] = 'red'
            self.button_gr['text'] = 'X'
            halcyona.write('red')
            halcyona.close()
            self.button_halcyona['bg'] = 'red'
            self.button_halcyona['text'] = 'X'
            hiramdaily.write('red')
            hiramdaily.close()
            self.button_hiramdaily['bg'] = 'red'
            self.button_hiramdaily['text'] = 'X'
            noryette.write('red')
            noryette.close()
            self.button_noryette['bg'] = 'red'
            self.button_noryette['text'] = 'X'
            reddragon.write('red')
            reddragon.close()
            self.button_reddragon['bg'] = 'red'
            self.button_reddragon['text'] = 'X'
            whalesong.write('red')
            whalesong.close()
            self.button_whalesong['bg'] = 'red'
            self.button_whalesong['text'] = 'X'


app = Tk()
Myapp(app)
app.mainloop()
