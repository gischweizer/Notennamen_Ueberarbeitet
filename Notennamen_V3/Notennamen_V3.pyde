from Notensystem import NotenSystem, Note
from KnopfWechsel import Knopf
from Modi import Violin, Bass
#Importiert den Code aus den anderen Tabs.

Modus = 1
Bimg = 0
Vimg = 0
movingMode = False
pointerPos = 0
pointerVal = 1.0
windowswidth = 800
windowsheight = 500

#globale Variabeln

def setup():
    global Vimg, Bimg
    size(windowswidth, windowsheight)
    #Grösse des Fensters
    background(255,255,255)
    #Hintergrundfarbe(weiss)
    Vimg = loadImage("violin.png")
    Bimg = loadImage("bass.png")
    # Die Notenschluessel werden geladen und der bestimmten Variabel zugeteilt. 
    
def draw(): #wird einmal pro Frame ausgeführt
    background(255,255,255)
    global Modus
    global pointerVal
    NotenSystem(width, height) # Dynamische Positionierung des Notensystems
    draw_ruler(width/10, height/8*7, width/10*8) # Dynamische Positionierung des Schiebereglers
    Note(pointerVal) 
    
    
    # Position und Groesse des Buttons
    ButtX = width/13*11
    ButtY = height/8
    Butta = width/20
    Buttb = height/20
    Knopf(ButtX,ButtY,Butta,Buttb)
    if mouseX >= ButtX and mouseX <= ButtX + Butta and mouseY >= ButtY and mouseY <= ButtY + Buttb and mousePressed == True:
        if Modus == 1:
            Modus = 0
            delay(500)
        elif Modus == 0:
            Modus = 1
            delay(500)
# Wenn der Mauszeiger auf dem Button ist und die Maustaste gedrueckt wird, wird der Modus gewechselt (entweder vom Violin- zum Bassschluessel oder umgekehrt) 
# Es wird ein Delay hinzugefuegt, damit der Modus nicht ununterbrochen gewechselt wird, wenn man die Maustaste zu lange drueckt.
    if Modus == 1:
        Violin(pointerVal, Vimg)
    else:
        Bass(pointerVal,Bimg)


'''
' Schieberegler
' Simon Hefti, Okt. 2020
'''

# Funktion: Schieberegler generieren
# objX:      X-Position des Reglers
# objY:      Y-Position des Reglers
# objLength: Länge des Reglers
def draw_ruler(objX, objY, objLength):
    global movingMode
    global pointerPos
    global pointerVal
    
    # Schieber einstellen
    pointerRadius = 24
    if pointerPos == 0:
        pointerPos = objX
    
    # Linie zeichnen
    fill(85)
    strokeWeight(6)
    line(objX, objY, objX + objLength, objY)
    fill(185)
    strokeWeight(2)
    
    # Überprüfen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseX > pointerPos - pointerRadius and mouseX < pointerPos + pointerRadius and mouseY > objY - pointerRadius and mouseY < objY + pointerRadius and mousePressed == True:
        movingMode = True
    
    # Wenn keine Maustaste gedrückt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseX > objX and mouseX < objX + objLength:
            pointerPos = mouseX
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseX < objX:
                pointerPos = objX
            if mouseX > objX:
                pointerPos = objX + objLength

    # Schieber zeichnen            
    circle(pointerPos, objY, pointerRadius)
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal = int(10 / float(objLength) * (pointerPos - objX))
    # Die Variable pointerVal wird unter anderem auch für die Tonhoehe verwendet
            
