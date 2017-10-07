from PIL import Image, ImageDraw, ImageFont
from random import choice, randint
import os
import random

def getSize(txt, font):
    testImg = Image.new('RGB', (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textsize(txt, font)

def getFont():
    return choice( os.listdir("fonts") )

def getColor():
    r = 255
    g = 255
    b = 255
    while r+g+b > 640:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
    return (r,g,b)

def imageFromText(text, fileName):
    fontname = "fonts/"+getFont()
    fontsize = 40
    padding = 30

    (r, g, b) = getColor()
    colorBackground = "white"

    font = ImageFont.truetype(fontname, fontsize)
    width, height = getSize(text, font)
    img = Image.new('RGB', (width+padding*2, height+padding*2), colorBackground)
    d = ImageDraw.Draw(img)
    d.text((padding, padding), text, (r,g,b), font=font)

    img.save(fileName)
