def Knopf(ButtX,ButtY,Butta,Buttb):

    if mouseX >= ButtX and mouseX <= ButtX + Butta and mouseY >= ButtY and mouseY <= ButtY + Buttb:
        fill(150, 150, 150)
    else:
        fill (60, 60, 60)
    rect(ButtX, ButtY, Butta, Buttb)
   # Die Farbe des Buttons werden definiert. Wenn die Maus darueber schwebt, soll sich die Farbe von dunkel- auf hellgrau auendern.
   
