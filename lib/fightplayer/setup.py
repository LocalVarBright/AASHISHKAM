import __matrix as m
import __display as d

#width = 2
#height = 2

from keyboard import is_pressed
import time

framerate = 15

d.add_layer('base')

def input():
    width, height = d.width, d.height
    if is_pressed("up"):
        if height > 48: height -= 1
    if is_pressed("down"):
        height += 1
    if is_pressed("left"):
        if width > 64: width -= 1
    if is_pressed("right"):
        width += 1
    d.set_size(width, height)

def update():
    width, height = d.width, d.height
    sizeLayer = [1]* width + ([1]+[-1]*(width-2)+[1])*(height-2) + [1]*width
    d.set_size(width, height)

    d.update_layer('base', sizeLayer)


def frameLoop():
    t1 = time.time()
    
    input()
    #print(width, height, sep=', ')
    update()
    d.push_frame()
    
    t2 = time.time()

    if t2 - t1 < 1/framerate:
        time.sleep(1/framerate - (t2 - t1))


print("EXECUTION TEST")
while True:
    frameLoop()

    if is_pressed("enter"):
        #d.toggle_layer('base')
        f = open('display.txt', 'w')
        width, height = d.width, d.height
        f.write(str(width) + '\n' + str(height))
        f.close()

        break
    
d.reset()