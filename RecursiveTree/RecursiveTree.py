from tkinter import *
import math

rotate = 20
scale  = 0.8
rootLength = 150
gens = 13

def getEndPoint(startPoint, angle, length):
    return (startPoint[0] + math.cos(math.pi*(angle/180))*length,
            startPoint[1] - math.sin(math.pi*(angle/180))*length) 

class Node:
    def __init__(self, startPoint, angle, length):
        self.angle      = angle
        self.starPoint  = startPoint
        self.length     = length
    
    def Grow(self,canvas):
        endPoint = getEndPoint(self.starPoint, self.angle, self.length)
        canvas.create_line(self.starPoint[0],self.starPoint[1],endPoint[0],endPoint[1])

        node1 = Node(endPoint,
                     self.angle - rotate,
                     self.length * scale)
        node2 = Node(endPoint,
                     self.angle + rotate,
                     self.length * scale)
        return [node1,node2]    

win = Tk()
win.attributes("-fullscreen", True)
win.title("Recursive Tree")

canvas = Canvas(win)
# canvas.config(background='black')
canvas.pack(fill=BOTH, expand=1)

root = Node((500,700),90,rootLength)
nodes = root.Grow(canvas)
def Plant(nodes,i):
    child = []
    i += 1
    for node in nodes:
        child += node.Grow(canvas)
    if i < gens:
        Plant(child, i)
    return i
Plant(nodes,1)

    
win.mainloop()




