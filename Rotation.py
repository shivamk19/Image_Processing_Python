from PIL import Image
import glob

img = Image.new('RGB', (60, 30), color = (10,255,10))
img.save('r.png')
#img.show()
#s = Image.open('download.jpg')
#a=int(input("Enter the angle by which image has to be rotated"))
#r = s.rotate(a)
#r.show()
