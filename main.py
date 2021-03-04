#Bibliotheken
from tkinter import *
import datetime
import random
from tkinter import messagebox
import turtle as t
import time as ti

                        ###### Memory Spiel für Kinder######

#zwei Fenster mit "Toplevel()" funktion machen, eines für die Regel und eines für das Spiel


#->erstes Fenster

window = Tk()
#Titel für das erste Fenster
window.title('Memory Spiel')

#Anzeige des aktuellen Datums und der Uhrzeit rechts oben im Fenster
now = datetime.datetime.now()
clock = now.strftime("%Y-%m-%d %H:%M:%S")

#Größe des Fensters mit Hintergrundfarbe
canvas = Canvas(window, width = 800, height = 400, background = 'deep sky blue')
#Himmel mit Regeln
canvas.create_text(450,150,text="\t\tSPIELREGEL\n\n\n\n1. Drehen Sie zwei beliebige Karten um.\n\n"
                       "2. Wenn die beiden Karten übereinstimmen, bleiben sie offen liegen.\n\n"
                       "3. Wenn nicht, werden sie mit der Vorderseite nach unten gedreht.\n\n"
                       "4. Das Spiel ist beendet, wenn alle Karten übereinstimmen.\n\n"
                       "5. Drücken Sie die Taste PLAY zum Abspielen.\n\n"        
                       "6. Drücken Sie ESC, um zu beenden")
#aktuellem Datum und Uhrzeit
canvas.create_text(790,10,anchor='ne' , font=('Helvetica',11,'bold'),fill='dark blue',text ="Aktuelles Datum und Uhrzeit :\n " + clock)
#Boden
canvas.create_rectangle(-5, 300, 805, 405, fill='sea green', width=0)
#Sonne
canvas.create_oval(-80,-80,120,120,fill='orange' , width=0)
canvas.pack()
#Beenden des Spiels mit der Esc-Taste
window.bind("<Escape>", lambda event: exit())



#->zweites Fenster

#die Abspielfunktion zur Ausführung des zweiten Fensters
def play():
    top = Toplevel()
    #Titel für das zweite Fenster
    top.title("Memory Spiel")
    #Zuweisung von false an Breite und Höhe, um die Größe des Fensters zu fixieren
    top.resizable(width=False, height=False)
    # Beenden des Spiels mit der Esc-Taste
    top.bind("<Escape>", lambda event: exit())
    #global variablen
    global first, previousx, previousy, match
    #Variable first als erste Karte deklarieren und als True initialisieren
    first = True
    #zwei Variablen,auf Null initialisiert, die sich die Koordinaten der ersten Karte merken werden
    previousx = 0
    previousy = 0
    #counter, um zu prüfen, ob keine Karten mehr verfügbar sind
    match = 0
    # leeres Dictionary das speichert die Buttons mit ihre Werte
    buttons = {}
    # leeres Dictionary das speichert die images für die Buttons
    button_images = {}


    #Funktion, die prüft, wenn die Karten übereinstimmen
    def show_images(button_x, button_y):
        global first
        global previousx, previousy
        global match
        #Images einfügen für jede button
        buttons[button_x, button_y]['text'] = button_images[button_x, button_y]
        # Funktion, die für die Aktualisierung der buttons verantwortlich ist.
        buttons[button_x, button_y].update_idletasks()
        #Anklicken der ersten Karte
        if first:
            previousx = button_x
            previousy = button_y
            first = False
        #Anklicken der zweiten Karte
        elif previousx != button_x or previousy != button_y:
            #wenn die Karten nicht identisch sind, werden wieder umgedreht
            if buttons[previousx, previousy]['text'] != buttons[button_x, button_y]['text']:
                top.after(1000)#Karte wird für 1sec angezeigt
                buttons[previousx, previousy]['text'] = u'\u2B1B'
                buttons[button_x, button_y]['text'] = u'\u2B1B'
            else:
                #wenn sie identisch, Karten bleiben umgedreht
                buttons[previousx, previousy]['command'] = DISABLED
                buttons[button_x, button_y]['command'] = DISABLED
                #auf eins erhöhen, wenn die Karten gleich sind
                match = match + 1
                #bestimmt, ob alle Karten umgedreht sind
                if match == 12:
                    #es wird eine Meldung angezeigt, wenn das Spiel beendet ist
                    messagebox.showinfo("Geschafft!", "Geschafft!\n\n Öffne dein Überraschung?")


                    #Herstellung eines Roboters als Überraschung am Ende des Spiels

                    #Rechteckfunktion zur Herstellung des Roboters
                    def rectangle(hor, ver, col):
                        t.pendown() #anzufangen zu schreiben
                        t.pensize(1)#Größe des Stifts
                        t.color(col)
                        t.begin_fill()

                        #zwei Schritte machen
                        for counter in range(1, 3):
                            t.forward(hor)
                            t.right(90)
                            t.forward(ver)
                            t.right(90)
                        t.end_fill()
                        t.penup()

                    t.penup()
                    #Geschwindigkeit des Stifts
                    t.speed('slow')
                    #Hintergrundfarbe
                    t.bgcolor('Dodger blue')


                    #Füße
                    t.goto(-100, -150)
                    rectangle(50, 20, 'blue')
                    t.goto(-30, -150)
                    rectangle(50, 20, 'blue')

                    #Beine
                    t.goto(-25, -50)
                    rectangle(15, 100, 'grey')
                    t.goto(-55, -50)
                    rectangle(-15, 100, 'grey')

                    #Körper
                    t.goto(-90, 100)
                    rectangle(100, 150, 'red')

                    #Arme
                    t.goto(-150, 70)
                    rectangle(60, 15, 'grey')
                    t.goto(-150, 110)
                    rectangle(15, 40, 'grey')
                    t.goto(10, 70)
                    rectangle(60, 15, 'grey')
                    t.goto(55, 110)
                    rectangle(15, 40, 'grey')

                    #Hals
                    t.goto(-50, 120)
                    rectangle(15, 20, 'grey')

                    #Kopf
                    t.goto(-85, 170)
                    rectangle(80, 50, 'red')

                    #Augen
                    t.goto(-60, 160)
                    rectangle(30, 10, 'white')
                    t.goto(-55, 155)
                    rectangle(5, 5, 'black')
                    t.goto(-40, 155)
                    rectangle(5, 5, 'black')

                    #Mund
                    t.goto(-65, 138)
                    rectangle(40, 5, 'black')

                    #Hände
                    t.goto(-155, 130)
                    rectangle(25, 25, 'green')
                    t.goto(-147, 130)
                    rectangle(10, 15, t.bgcolor())
                    t.goto(50, 130)
                    rectangle(25, 25, 'green')
                    t.goto(58, 130)
                    rectangle(10, 15, t.bgcolor())

                    #Hurra!
                    # H
                    t.goto(-250, 290)
                    rectangle(15, 100, 'white')
                    t.goto(-200, 290)
                    rectangle(-15, 100, 'white')
                    t.goto(-240, 250)
                    rectangle(40, 20, 'white')

                    # u
                    t.goto(-170, 230)
                    rectangle(40, 40, 'white')
                    t.goto(-158, 230)
                    rectangle(18, 25, t.bgcolor())

                    #r
                    t.goto(-110, 235)
                    rectangle(15, 50, 'white')
                    t.goto(-110, 235)
                    rectangle(40, 20, 'white')

                    #r
                    t.goto(-40, 235)
                    rectangle(15, 50, 'white')
                    t.goto(-40, 235)
                    rectangle(40, 20, 'white')

                    #a
                    t.goto(30, 230)
                    rectangle(40, 40, 'white')
                    t.goto(45, 220)
                    rectangle(15, 20, t.bgcolor())
                    t.goto(65, 235)
                    rectangle(10, 50, 'white')

                    #!
                    t.goto(100, 290)
                    rectangle(15, 80, 'white')
                    t.goto(100, 200)
                    rectangle(15, 15, 'white')
                    t.hideturtle()
                    ti.sleep(10)
                    t.hideturtle()

            #die erste Karte wieder auf True setzen
            first = True


    #Eigene images list erstellen
    images = ['Was sagt ein\n Informatiker\nwenn er auf die Welt\nkommt?\n\nHallo Welt!',
              ' | | | | |\n ( O  O )\n--oOO- U -OOo-\n Ich Grüsse Dich',
              './\…/\ \n(.‘•..•’.) \n..=*=.. \n    (.\.||./.)~~**\n\n SCHÖNES WOCHENENDE!',
              '()_()    ()_()   ()_()\n(-.-)    (o.O)  (^.^)\n(")(")   (")(")  (")(")\n   Hi!   Hallo! Tschüss!',
              '$$$$$$$        $$$$$$$\n$$$$$$$$$    $$$$$$$$$\n$$$$$$$$$$ $$$$$$$$$$\n$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$\n'
              '$$$$$$$$$\n$$$$$\n$$\n$',
              '$$$$$$$$$$$$$$\n    $$$$$$    \n    $$$$$$    \n    $$$$$$    \n    $$$$$$    \n    $$$$$$    \n    $$$$$$'
              '    \n    $$$$$$    \n$$$$$$$$$$$$$$',
              '$$$$$$$$$    $$$$$$$$$\n $$$$$            $$$$$\n $$$$$            $$$$$\n $$$$$            $$$$$\n $$$$$$ '
              '        $$$$$$ \n $$$$$$     $$$$$$\n   $$$$$$$$$$$$$\n  $$$$$$$$$',
              u'\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\n\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\n'
              u'\u2708\n GUTE REISE!!!\n\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\n\u2728\u2728\u2728\u2728\u2728\u2728'
              u'\u2728\u2728\u2728',
              u'\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\n\u2717\u2717\u2717'
              u'\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\n\n\u274C\nFALSCH!\n\n\u2717\u2717\u2717'
              u'\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\n\u2717\u2717\u2717\u2717\u2717\u2717\u2717'
              u'\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717',
              u'\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\n\u2714\u2714\u2714'
              u'\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\n\n\u2705\nRICHTIG!\n\n\u2714\u2714\u2714'
              u'\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\n\u2714\u2714\u2714\u2714\u2714\u2714\u2714'
              u'\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714',
              'Esel essen\n Nesseln nicht.\nNesseln essen\n Esel nicht.',
              'Sieben Schneeschipper\nschippen sieben\nSchippen Schnee.',

              'Was sagt ein\n Informatiker\nwenn er auf die Welt\nkommt?\n\nHallo Welt!',
              ' | | | | |\n ( O  O )\n--oOO- U -OOo-\n Ich Grüsse Dich',
              './\…/\ \n(.‘•..•’.) \n..=*=.. \n    (.\.||./.)~~**\n\n SCHÖNES WOCHENENDE!',
              '()_()    ()_()   ()_()\n(-.-)    (o.O)  (^.^)\n(")(")   (")(")  (")(")\n   Hi!   Hallo! Tschüss!',
              '$$$$$$$        $$$$$$$\n$$$$$$$$$    $$$$$$$$$\n$$$$$$$$$$ $$$$$$$$$$\n$$$$$$$$$$$$$$$$$\n$$$$$$$$$$$$$\n$$$$$$$$$\n$$$$$\n$$\n$',
              '$$$$$$$$$$$$$$\n    $$$$$$    \n    $$$$$$    \n    $$$$$$    \n    $$$$$$    \n    $$$$$$    \n    $$$$$$    '
              '\n    $$$$$$    \n$$$$$$$$$$$$$$',
              '$$$$$$$$$    $$$$$$$$$\n $$$$$            $$$$$\n $$$$$            $$$$$\n $$$$$            $$$$$\n $$$$$$         '
              '$$$$$$ \n $$$$$$     $$$$$$\n   $$$$$$$$$$$$$\n  $$$$$$$$$',
              u'\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\n\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\n'
              u'\u2708\n GUTE REISE!!!\n\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\n\u2728\u2728\u2728\u2728\u2728'
              u'\u2728\u2728\u2728\u2728',
              u'\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\n\u2717\u2717\u2717'
              u'\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\n\n\u274C\nFALSCH!\n\n\u2717\u2717\u2717'
              u'\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\n\u2717\u2717\u2717\u2717\u2717\u2717\u2717'
              u'\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717\u2717',
              u'\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\n\u2714'
              u'\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\n\n\u2705\nRICHTIG!\n\n'
              u'\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\n\u2714\u2714\u2714'
              u'\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714\u2714',
              'Esel essen\n Nesseln nicht.\nNesseln essen\n Esel nicht.',
              'Sieben Schneeschipper\nschippen sieben\nSchippen Schnee.']

    #random funktion um die Symbole zu mischen(images)
    random.shuffle(images)

    #buttons ertellen mit for loops
    for button_x in range(6):
        for button_y in range(4):
            #buttons mit Größe und Eigenschaften
            #Lambda-Funktion, um command in jede button zu speichern
            button = Button(top, command=lambda button_x=button_x, button_y=button_y: show_images(button_x, button_y),
                            text=u'\u2B1B', highlightbackground='brown', fg='black', width=21, height=9,
                            highlightthickness=24)
            button.grid(column=button_x, row=button_y)
            #Speicherung aller button im variable buttons
            buttons[button_x, button_y] = button
            #Verwendung der pop methode, um die images zu erhalten
            button_images[button_x, button_y] = images.pop()

#Erstellen einer Funktion für die Play-Taste zum Starten des Hauptspiels
button_start = Button(window, text="PLAY", highlightbackground='red',fg='black', highlightthickness=5, width=87, height=2, command=play)
button_start.pack()

#Ende des Fensters
window.mainloop()