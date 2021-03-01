from PIL import Image, ImageDraw
import random

width = 1600
height = 900
back_ground = 'yellow'
color_of_pixel = "fg1.png"

#creats background
canvas = Image.new('RGB', (width, height), back_ground)
img_draw = ImageDraw.Draw(canvas)
canvas.save('wallpaper.png')

#opens background
bg = Image.open("wallpaper.png")

#loop for adding the random pixals
y = 0
z = 0
def pixel():
	fg = Image.open(color_of_pixel)
	bg.paste(fg, (y, z), fg.convert('RGBA'))

b = 0
while True:
	pixel()
	y = y +2
	if y > width:
		y = 1
		b = b + 1
		if b == 2:
			y = 0
			b = 0
		z = z + 1
	if z > height:
	 	break
#720000
#end of loop
#saveing the result
bg.save("wallpaper.png")
#bg.show()
