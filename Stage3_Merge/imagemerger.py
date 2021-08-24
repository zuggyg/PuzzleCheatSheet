# Zuggyg 24/06/21
#the goal of this script is to overlap image B onto image A based on given dimension %

import sys
from PIL import Image

#set inputs then acquire sizes of images
zoomA = 1.00
HshiftA = 0
VshiftA = 0
fileA = Image.open('imageA.jpg')
fileB = Image.open('imageB.png')

widthA, heightA = fileA.size
widthB, heightB = fileB.size

#zoomsA
fileA = fileA.resize((int(widthA*zoomA),int(heightA*zoomA)))
left = widthA*((zoomA - 1)/2)
right = left + widthA
top = heightA*((zoomA - 1)/2)
bottom = top + heightA
fileAcropped = fileA.crop((left,top,right,bottom))

#resize A to B dimensions
fileAtoB = fileAcropped.resize((widthB, heightB))

#shift the image in two steps, first creating a bigger canvas and then cropping
HshiftResult = widthB + abs(HshiftA)
VshiftResult = heightB + abs(VshiftA)
shiftingA = Image.new('RGBA',(HshiftResult,VshiftResult))

shiftX = 0
shiftY = 0
if HshiftA > 0:
	shiftX = HshiftA
if VshiftA > 0:
	shiftY = VshiftA

shiftingA.paste(fileAtoB,(shiftX,shiftY))

cropX = HshiftA
cropY = VshiftA
if HshiftA > 0:
	cropX = 0
if VshiftA > 0:
	cropY = 0

shiftedA = shiftingA.crop((cropX,cropY,cropX+widthB,cropY+widthB))


#creates a canvas based on imageB and then pastes A and B
canvas = Image.new('RGBA',(widthB, heightB))
canvas.paste(shiftedA, (0,0))
canvas.paste(fileB, (0,0), fileB)

#save the canvas
canvas.save('combineAB.png')
