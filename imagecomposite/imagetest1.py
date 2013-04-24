from PIL import Image, ImageDraw
import random

def selectImage(image1, image2):
  if (random.random() <.5):
    return image1
  else:
    return image2
  
# size of the composite box
boxSize = 200

im1 = Image.open("e:\\tmp\\image-1.jpg")
im2 = Image.open("e:\\tmp\\image-2.jpg")

# image1 and image2 must be the same size
assert(im1.size[0] == im2.size[0])
assert(im1.size[1] == im2.size[1])

imSize = im1.size

output = Image.new("RGB", imSize)

for y in range(0, imSize[1], boxSize):
  for x in range (0, imSize[0], boxSize):
    imCurrent = selectImage(im1, im2)
    
    imcrop = imCurrent.crop((x, y, x+boxSize, y+boxSize))

    output.paste(imcrop, (x,y))

output.show()

# inputImage.save("e:\\tmp\\imageout.jpg")

