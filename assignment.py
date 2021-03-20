import sqlite3
from sqlite3 import Error
import pygame
from pygame_functions import *

screenSize(1280,960)

b = makeSprite("btn.png")

drawRect(0,0,1280/2, 960,(68, 189, 219))
drawRect(1280/2,0,1280/2, 960,(242, 182, 29))

moveSprite(b,1280/2,0)
showSprite(b)
endWait()
