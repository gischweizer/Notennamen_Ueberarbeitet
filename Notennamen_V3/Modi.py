def Violin(pointerVal,Vimg):
    imageMode(CENTER)
    #Das Bild wird psitioniert und das Seitenverhaeltnis dynamisch angepassst.
    image(Vimg,width/8,height/2,height*7*422/7200,height/10*7)
    #Dir moeglichen Toene werden aufgelistet. Je nach dem, welcher Wert pointerVal ist, wird ein anderer Notennamen angezeigt.
    tonv = ["d1","e1","f1","g1","a1","h1","c2","d2","e2","f2","g2"]
    textSize(82)
    #Schriftgrsse
    fill(236,64,122)
    #Schriftfarbe
    text(tonv[pointerVal],20,64)
    #Textgroesse und -position wird definiert. Der text ist abhaengig von der Position des Reglers, bzw. von der Variable pointerVal.
    textSize(height/25);
    text("Press button to change\nto bass clef.", width/11*7, height/10); # Text weist darauf hin, dass der Button gedrueckt werden kann.
    
    #Gleiches Verfahren beim Modus Bassschluessel
def Bass(pointerVal,Bimg):
    imageMode(CENTER)
    image(Bimg,width/8,height/2-height/30,height/10*3.5,height/10*3.5*(1280/1097))
    tonb = ["F","G","A","H","c","d","e","f","g","a","h"]
    textSize(82)
    fill(236,64,122)
    text(tonb[pointerVal],20,64)
    textSize(height/25);
    text("Press button to change\nto violin clef.", width/11*7, height/10);
