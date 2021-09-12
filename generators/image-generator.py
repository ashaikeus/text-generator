import os
import random
from PIL import Image, ImageFont, ImageDraw
from text_generator import generate, initialize
import textwrap

path = random.choice(os.listdir("{}".format(
    r"D:\Text Generator\Text Generator\task\text_generator\images")))
img = Image.open("..\images\\" + path)
img.filename = img.filename.split("\\")[2]

if img.filename.startswith("girl"):  # good
    coords = (47, 50)
    size = 50
    width = 70
elif img.filename.startswith("group"):
    coords = (1205, 240)
    size = 125
    width = 35
elif img.filename.startswith("man"):  # good
    coords = (410, 40)
    size = 35
    width = 25
elif img.filename.startswith("stock"):
    coords = (45, 90)
    size = 50
    width = 25
elif img.filename.startswith("woman"):  #
    coords = (620, 60)
    size = 40
    width = 18

initialize("..\бк.txt")
text = generate()
try:
    text = "\n".join(textwrap.wrap(text, width=width))
except IndexError:
    pass
font = ImageFont.truetype("..\Lobster.ttf", size=size)
ImageDraw.Draw(img).text(coords, text, (0, 0, 0), font=font)
img.save("output" + str(random.randint(1, 999)) + ".jpg")
img.show()
