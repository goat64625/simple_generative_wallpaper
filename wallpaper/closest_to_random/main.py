from PIL import Image, ImageDraw
import random
#creats background
#add a png image called fg.png
width = 900
height = 1600

canvas = Image.new('RGB', (height, width),)

img_draw = ImageDraw.Draw(canvas)

#canvas.save('wallpaper.png')


x = 0
y = 0
img = canvas #Image.open('wallpaper.png')
pix = img.load()
#print(pix[100,200])
for i in range (0,1440000):
	pix[x,y] = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
	y = y + 1
	if y == width:
		y = 0
		x = x + 1
		
img.save("wallpaper.png")

