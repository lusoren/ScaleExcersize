import random

for x in range(1 , 60):
    
    start  = str(400 + (25*x))
    end    = str(((x-1)* 25) + 400)
    r      = (255/20)*x
    g      = (255/40)*x
    b      = (255/60)*x
    
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b >255:
        b = 255

    r = str(r)
    g = str(g)
    b = str(b)
    
    print ""
    print "@media (max-width: " + start + "px) and (min-width: " + end + "px){"
    print "     body {"
    print "         background-color: rgb(" + r + "," + g + "," + b + ");"
    print "     }"
    print "}"
    