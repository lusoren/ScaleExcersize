import random

for x in range(1 , 60):
    
    start  = str(400 + (25*x))
    end    = str(((x-1)* 25) + 400)
    r      = random.randint(0,255)
    g      = random.randint(0,255)
    b      = random.randint(0,255)
    
    r = str(r)
    g = str(g)
    b = str(b)
    
    print ""
    print "@media (max-width: " + start + "px) and (min-width: " + end + "px){"
    print "     body {"
    print "         background-color: rgb(" + r + "," + g + "," + b + ");"
    print "     }"
    print "}"
    