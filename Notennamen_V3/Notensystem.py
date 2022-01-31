def NotenSystem(width, height):
    for i in range(3,8):
        line(0+(width/10),height/10*i,width-(width/10),height/10*i)
        #Das Fenster wird horizontal in zehn Stuecke geteilt und Linien gezeichnet. Damit in der Mitte fuenf Linien angezeigt werden, werden nur die Linien in range 3 bis 8 angezeigt.
        
def Note(pointerVal):
    YNote = [height/10*7.5,height/10*7,height/10*6.5,height/10*6,height/10*5.5,height/10*5,height/10*4.5,height/10*4,height/10*3.5, height/10*3, height/10*2.5]
     #Fuer die Note gibt es verschiedene moegliche Werte. Die halben Schritte sind fuer die Noten auf den Linien. Die YPosition ist abhaengig von der Fensterhoehe.
    ellipse(width/2,YNote[pointerVal],width/12,height/10)
   
