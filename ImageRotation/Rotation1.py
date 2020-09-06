from PIL import Image
import glob
img.show()
s = Image.open('rotate.png')
a=int(input("Enter the angle by which image has to be rotated"))
r = s.rotate(a)
r.show()
