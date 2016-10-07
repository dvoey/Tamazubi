from Tkinter import *
from math import *

class Animationsdaten(object):
    def __init__(self):
        self.s_p_x = 500
        self.s_p_y = 500
        self.s_m = 3000
        self.s_v_x = 0
        self.s_v_y = 0

        self.e_p_x = 800
        self.e_p_y = 500
        self.e_m = 10
        self.e_v_x = 0
        self.e_v_y = -10


root = Tk()

w = Canvas(root, width=1000, height=1000)
w.pack()




def animate():
    w.delete(ALL)

    # neue Geschwindigkeit berechnen
    G = 7
    r = sqrt((ad.s_p_x - ad.e_p_x)*(ad.s_p_x - ad.e_p_x)+(ad.s_p_y - ad.e_p_y)*(ad.s_p_y - ad.e_p_y))
    r3 = pow(r,3)

    # Sonne
    ad.s_v_x = ad.s_v_x + G * ad.e_m * (ad.e_p_x - ad.s_p_x) / r3
    ad.s_v_y = ad.s_v_y + G * ad.e_m * (ad.e_p_y - ad.s_p_y) / r3
    # Erde
    ad.e_v_x = ad.e_v_x + G * ad.s_m * (ad.s_p_x - ad.e_p_x) / r3
    ad.e_v_y = ad.e_v_y + G * ad.s_m * (ad.s_p_y - ad.e_p_y) / r3

    # neue Position berechnen
    ad.s_p_x = ad.s_p_x + ad.s_v_x
    ad.s_p_y = ad.s_p_y + ad.s_v_y
    ad.e_p_x = ad.e_p_x + ad.e_v_x
    ad.e_p_y = ad.e_p_y + ad.e_v_y


    # Objekte zeichnen
    w.create_oval(ad.s_p_x-10, ad.s_p_y-10, ad.s_p_x+10, ad.s_p_y + 10, fill="#D0D050")
    w.create_oval(ad.e_p_x-3, ad.e_p_y-3, ad.e_p_x+3, ad.e_p_y + 3, fill="#50D0FF")

    root.after(20, animate)


ad = Animationsdaten()

animate()
root.mainloop()