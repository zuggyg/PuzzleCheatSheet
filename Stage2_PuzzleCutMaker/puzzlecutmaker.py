# This is stage 2 of 3 in the Puzzle Cheat Sheet Project
# 22/06/2021 Zuggyg

import sys
from PIL import Image

# open file to know size of puzzle
file1 = open(r"cutdna.txt","r")
dna = file1.read().splitlines()

puzzlecolumns = len(dna[0])
puzzlelines = len(dna)

print("puzzlecolumns =",puzzlecolumns)
print("puzzlelines =",puzzlelines)

# open standard piece to know dimensions
pstandard = Image.open('pstandard.png')
pwidth, pheight = pstandard.size

# create canvas using size of puzzle and dimensions of piece
cwidth = pwidth*(puzzlecolumns+1)
cheight = pheight*(((puzzlelines-1)/2)+1)
canvas = Image.new('RGBA',(int(cwidth),int(cheight)))


# open all edge types
pN = Image.open('N.png')
pW = Image.open('W.png')
pL = Image.open('L.png')
pR = Image.open('R.png')
pU = Image.open('U.png')
pD = Image.open('D.png')


# add edges to canvas. for even lines add tops, for odd lines add sides
linecount = 0
for line in dna:
	if linecount%2 == 0:
		x_offset = pwidth/2
		y_offset = (linecount/2)*pheight
		for piece in dna[linecount]:
			abort = False
			if piece == "N":
				pdecoded = pN
			elif piece == "d":
				pdecoded = pD
			elif piece == "u":
				pdecoded = pU
			else:
				print("unexpected atom")
				abort = True
			if abort == True:
				print("abort")
			else:
				canvas.paste(pdecoded,(int(x_offset),int(y_offset)),pdecoded)
			x_offset += pwidth

	else:
		x_offset = 0
		y_offset = pheight/2 + ((linecount-1)/2)*pheight
		for piece in dna[linecount]:
			abort = False
			if piece == "W":
				pdecoded = pW
			elif piece == "l":
				pdecoded = pL
			elif piece == "r":
				pdecoded = pR
			else:
				print("unexpected atom")
				abort = True
			if abort == True:
				print("abort")
			else:
				canvas.paste(pdecoded,(int(x_offset),int(y_offset)),pdecoded)
			x_offset += pwidth

	linecount += 1


# save the canvas
canvas.save('puzzlecut.png',"PNG")
print("it worked")
