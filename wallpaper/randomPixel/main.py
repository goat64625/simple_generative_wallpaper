from PIL import Image, ImageDraw
import random
#creats background
canvas = Image.new('RGB', (1600, 900), 'pink')
img_draw = ImageDraw.Draw(canvas)
canvas.save('wallpaper.png')

#opens background
bg = Image.open("wallpaper.png")

#loop for adding the random pixals
x = 1
while x < 10000:
	area = random.randint(0, 1600),random.randint(0, 900)
	small = Image.open("fg.png")#.rotate(random.randint(0,360), expand=True)
	bg.paste(small, (area), small.convert('RGBA'))
	
	area = random.randint(0, 1600),random.randint(0, 900)
	fg1 = Image.open("fg1.png")
	bg.paste(fg1, (area), fg1.convert('RGBA'))
	
	area = random.randint(0, 1600),random.randint(0, 900)
	fg1 = Image.open("fg2.png")
	bg.paste(fg1, (area), fg1.convert('RGBA'))
	
	area = random.randint(0, 1600),random.randint(0, 900)
	fg1 = Image.open("fg3.png")
	bg.paste(fg1, (area), fg1.convert('RGBA'))
	
	area = random.randint(0, 1600),random.randint(0, 900)
	fg1 = Image.open("fg4.png")
	bg.paste(fg1, (area), fg1.convert('RGBA'))
	
	x = x+1
#end of loop
#saveing the result
bg.save("wallpaper.png")
#bg.show()
