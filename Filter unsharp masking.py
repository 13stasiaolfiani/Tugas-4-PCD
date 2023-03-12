# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter

# creating a image object
im1 = Image.open(r"image4.jpg")

# applying the unsharpmask method
im2 = im1.filter(ImageFilter.UnsharpMask(radius=3, percent=200, threshold=5))

im2.show()
