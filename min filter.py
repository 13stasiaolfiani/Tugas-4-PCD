# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter

# creating a image object
im1 = Image.open(r"image1.jpeg")

# applying the min filter
im2 = im1.filter(ImageFilter.MinFilter(size = 3))

im2.show()
