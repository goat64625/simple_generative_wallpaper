import random
from PIL import Image , ImageDraw
height = 1600
width = 900
totalNumberOfColor = 3


color = []

for i in range(totalNumberOfColor):
	color.append((random.randrange(256),random.randrange(256),random.randrange(256)))



x = 0
y = 0
canvas = Image.new('RGB', (height, width), 'pink')

img_draw = ImageDraw.Draw(canvas)

pix = canvas.load()
for i in range (0,1440000):
	pix[x,y] = color[random.randrange(totalNumberOfColor)]
	y = y + 1
	if y == width:
		y = 0
		x = x + 1


canvas.save('wallpaper.png')
