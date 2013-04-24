from PIL import Image, ImageDraw
import random

# User prefs
# size of the composite box
boxSize = 150

# to allow repeatability. Comment out to create random image each run
randomSeed = 0

# FUNCTIONS =========================
def selectImage(images):
  return images[random.randrange(0, len(images))]

# MAIN ==============================
if not (randomSeed is None):
  random.seed(randomSeed)
  
images = []
i = 0
while True:
  i += 1
  try:
    im = Image.open("e:\\tmp\\image-%i.jpg" % i)
    images.append(im)
    # images must be the same size
    assert(images[0].size[0] == im.size[0])
    assert(images[0].size[1] == im.size[1])
  except:
    break

# there must be at least 2 images
assert(len(images)>1)

imSize = images[0].size

output = Image.new("RGB", imSize)

for y in range(0, imSize[1], boxSize):
  for x in range (0, imSize[0], boxSize):
    imCurrent = selectImage(images)
    
    imcrop = imCurrent.crop((x, y, x+boxSize, y+boxSize))

    output.paste(imcrop, (x,y))

output.show()

# inputImage.save("e:\\tmp\\imageout.jpg")

