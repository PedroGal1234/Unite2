#Pedro Gallino
#9/18/17
#coloredSquare.py - makes a random number

from ggame import *
from random import randint

num = randint(1,6)

if num == 1:
    red = Color(0xff0000,1)
    line = LineStyle(3,red)
    rectangle = RectangleAsset(100,100,line,red)
elif num == 2:
    blue = Color(0x000ff,1)
    line = LineStyle(3,blue)
    rectangle = RectangleAsset(100,100,line,blue)
elif num == 3:
    yellow = Color(0xffff00,1)
    line = LineStyle(3,yellow)
    rectangle = RectangleAsset(100,100,line,yellow)
elif num == 4:
    purpel = Color(0xff33ff,1)
    line = LineStyle(3,purpel)
    rectangle = RectangleAsset(100,100,line,purpel)
elif num == 5:
    green = Color(0x66cc00,1)
    line = LineStyle(3,green)
    rectangle = RectangleAsset(100,100,line,green)
elif num == 6:
    orange = Color(0xff8000,1)
    line = LineStyle(3,orange)
    rectangle = RectangleAsset(100,100,line,orange)

Sprite(rectangle)
myApp = App()
myApp.run()
