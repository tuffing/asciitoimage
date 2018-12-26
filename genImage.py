#!/usr/bin/python3

import sys
import PIL
from PIL import Image


class GenImage(object):
    
    def __init__(self):
        pass    

    
    def convert(self, asciiArray, charMap, newImagePath):
        tileSize = 5
        charToImage = dict()
        for k,v in charMap.items():
            charToImage[k] = Image.open(v, 'r')
        
        background = Image.new('RGBA', (len(asciiArray[0])*tileSize, len(asciiArray)*tileSize), (0, 0, 0, 255))

        for y,row in enumerate(asciiArray):
            for x, cell in enumerate(row):
                background.paste(charToImage[cell], (x*tileSize,y*tileSize))
            print('Row %s of %s' % (y + 1, len(asciiArray)))
        background.save(newImagePath)        


if __name__ == '__main__':
    mapping = {'.': 'images/sand.png', '#': 'images/clay.png', '~': 'images/still.png', '|': 'images/moving.png'}
    
    inputFile = open('visualisation.txt', 'r')
    text = inputFile.read().strip().split('\n')
    inputFile.close()
    
    GenImage().convert(text, mapping, 'target.png')