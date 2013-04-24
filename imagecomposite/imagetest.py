from PIL import Image, ImageDraw
import random

# User prefs
# size of the composite box
boxSize = 150

# FUNCTIONS =========================
def selectImage(images, index):
  return images[index % len(images)]

# MAIN ==============================
images = []
i = 0
while True:
  i += 1
  try:
    print i
    im = Image.open("e:\\tmp\\image-%i.jpg" % i)
    images.append(im)
    # images must be the same size
    assert(images[0].size[0] == im.size[0])
    assert(images[0].size[1] == im.size[1])
  except Exception as detail:
    print detail
    break

# there must be at least 2 images
assert(len(images)>1)

imSize = images[0].size

output = Image.new("RGB", imSize)
imageIndexStart = 0
for y in range(0, imSize[1], boxSize):
  imageIndex = imageIndexStart
  imageIndexStart += 1
  for x in range (0, imSize[0], boxSize):
    imCurrent = selectImage(images, imageIndex)
    imageIndex += 1
    
    imcrop = imCurrent.crop((x, y, x+boxSize, y+boxSize))

    output.paste(imcrop, (x,y))

output.show()

# inputImage.save("e:\\tmp\\imageout.jpg")

