from PIL import Image, ImageDraw
import random
#creats background
canvas = Image.new('RGB', (1600, 900), 'red')
img_draw = ImageDraw.Draw(canvas)
canvas.save('wallpaper.png')

#opens background
bg = Image.open("wallpaper.png")

#loop for adding the random pixals art
x = 1
while x < 1600:
	area = random.randint(0, 1600),random.randint(0, 900)
	small = Image.open("peni.png").rotate(random.randint(0,360), expand=True)
	bg.paste(small, (area), small.convert('RGBA'))
	x = x+1
#end of loop
#saveing the result
bg.save("wallpaper.png")
#bg.show()
