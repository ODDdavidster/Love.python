'''
David Staffen 
464166
'''
#Pixel 2 ASCII
#Code from user Alderven on stackoverflow @ https://stackoverflow.com/questions/76950470/trasforming-pixel-art-into-ascii-art
#I just tweeked it ever so slightly this is all him baby. but I need this.
from PIL import Image

ITEMS = {(255, 255, 255, 255): '░',
         (180, 180, 180, 255): '▒',
         (70, 70, 70, 255): '▓',
         (111, 49, 152, 255): '@',
         (34, 177, 76, 255): '¥',
         (153, 0, 48, 255): 'E',
         (153, 217, 234, 255): 'w',
         (0, 183, 239, 255): 's',
         (77, 109, 243, 255): 'z'}
image_input = input("put the file name here nerd>_") + '.png'
image = Image.open(image_input) 
print(image)
width, height = image.size
pix = image.load()
for y in range(0, height, 1):
    line = ''
    for x in range(0, width, 1):
        line += ITEMS[pix[x, y]] + '|'
    print(line[:-1])
input('Dont leave yet.')
exit()