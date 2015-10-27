from graphics import *

window = GraphWin("Visualisation", 750, 750)

#setBackground(color_rgb(255, 255, 255))
line = line(point(200, 200), point(200,550))
line.setfill(color_rgb(255, 0, 0))
line.draw(window)
xspeed = 2

while True:
    currentPos = line.getP2()
    if(currentPos.getX() >= 700):
        yspeed = -yspeed
    if(currentPos.getP1() >= 0):
        xspeed = -xspeed
        
window.getMouse()