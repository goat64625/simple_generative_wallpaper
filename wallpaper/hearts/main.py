from PIL import Image, ImageDraw
import random
#creats background
#add a png image called fg.png
width = 900
height = 1600

canvas = Image.new('RGB', (height, width), 'pink')

img_draw = ImageDraw.Draw(canvas)

canvas.save('wallpaper.png')


#opens background
bg = Image.open("wallpaper.png")
small = Image.open("fg.png")


#loop for adding the random pixals
small = small.rotate(random.randint(0,360), expand=True)
x = 1
area = random.randint(0, height),random.randint(0, width)
sm = small.rotate(random.randrange(360), expand=True)
while x < 4000:
	
	bg.paste(sm, (random.randint(0, height),random.randint(0, width)), sm.convert('RGBA'))
	sm = small.rotate(random.randrange(360), expand=True)
	
	x = x+1
#end of loop
#saveing the result
#bg.show()
bg.save("wallpaper.png")

