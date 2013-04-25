from PIL import Image, ImageDraw
from Tkinter import Tk
from tkFileDialog import askopenfilenames

import random

# User prefs
# size of the composite box
boxSize = 150

# to allow repeatability. Comment out to create random image each run
randomSeed = 0

# FUNCTIONS =========================
def selectImage(images):
  return images[random.randrange(0, len(images))]

def getImages():
  images = []
  
  # only allow jpgs
  #options = {}
  #options['filetypes'] = [('JPG files', '*.jpg')]
  
  # ask the user to select the images to process
  Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
  # files = askopenfiles(mode="r", **options) # show an "Open" dialog box and return a list of files
  filenames = askopenfilenames() # show an "Open" dialog box and return a list of files
  filenames = filenames.split() # work around for windows python bug: http://bugs.python.org/issue5712
  
  for filename in filenames:
    print filename
    try:
      im = Image.open(filename)
      images.append(im)
      # images must be the same size
      assert(images[0].size[0] == im.size[0])
      assert(images[0].size[1] == im.size[1])
    except:
      break

  # the user must have select 2 or more images
  assert(len(images) > 1)

  return images

# MAIN ==============================
if not (randomSeed is None):
  random.seed(randomSeed)
  
images = getImages()

imSize = images[0].size

output = Image.new("RGB", imSize)

for y in range(0, imSize[1], boxSize):
  for x in range (0, imSize[0], boxSize):
    imCurrent = selectImage(images)
    
    imcrop = imCurrent.crop((x, y, x+boxSize, y+boxSize))

    output.paste(imcrop, (x,y))

output.show()

# inputImage.save("e:\\tmp\\imageout.jpg")

