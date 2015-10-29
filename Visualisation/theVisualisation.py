from graphics import *

window = GraphWin("Visualisation", 750, 750)

file = open("C:\Users\George\Documents\GitHub\DAT505-Assignment-2\Visualisation\data.txt")
scores = file.readline().strip().split('.')

#setBackground(color_rgb(255, 255, 255))
ball = circle(point(200, 200), point(200,550))
ball.setfill(color_rgb(255, 0, 0))
ball.draw(window)
xspeed = 2

while True:
    currentPos = line.getcenter()
    if(currentPos.getX() >= 700):
        xspeed = -xspeed
    if(currentPos.getX() >= 0):
        xspeed = -xspeed
    if(currentPos.getY() >= 700):
        Yspeed = -Yspeed
    if(currentPos.getY() >= 0):
        Yspeed = -Yspeed
        
window.getMouse()