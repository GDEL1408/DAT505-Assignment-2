from graphics import *
import random, time

file = open("data.txt",'r')
size = file.read().splitlines()
n = len(size)
i = 0
#print(n)

window = GraphWin("Visualisation", 700, 700)


for i in range(0, n):
    #print(i)
    r = float(size[i])
    colormark = None
    
    X = random.randrange(200, 500)
    Y = random.randrange(200, 500)
    
    #print("50",size[i])
    
    if r < 40:
        colormark = color_rgb(255,0,0)
        #print('low')
    
    elif r > 40 and r < 70:
        colormark = color_rgb(255,255,0)
        #print('mid')
    
    else: 
        colormark = color_rgb(0,255,0)
        #print('high')
    
    ball = Circle(Point(X, Y), r)
    ball.setFill(colormark)
    ball.draw(window)
        
    X = None
    Y = None
        
    i = i + 1
    
    time.sleep(0.5)
    
    ball.undraw()

#window.getMouse()
window.close()