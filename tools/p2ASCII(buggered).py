'''
David Staffen 
464166
'''
#Pixel 2 ASCII
#Code from user Alderven on stackoverflow @ https://stackoverflow.com/questions/76950470/trasforming-pixel-art-into-ascii-art
#I just tweeked it ever so slightly this is all him baby. but I need this.
#This is gonna need some work... dear lord

#inport the Pillow commands PIL is short for Pillow. don't ask me why IDK
from PIL import Image
#defining each color's symbol
ITEMS = {(255, 255, 255, 255): '░',
         (180, 180, 180, 255): '▒',
         (70, 70, 70, 255): '▓',
         (111, 49, 152, 255): '@',
         (34, 177, 76, 255): '¥',
         (153, 0, 48, 255): 'E',
         (153, 217, 234, 255): 'w',
         (0, 183, 239, 255): 's',
         (77, 109, 243, 255): 'z'}
#image name being defined
image_input = "Maptemp.png"
#Opening the image in python
image = Image.open(image_input)
#defining how tall and wide the image is
width, height = image.size
#no idea what is going on here
pix = image.load()
print(pix[1,6])
#for each pixel along the y acsess from 0 in the image to the height with a step of 1
for y in range(0, height, 1):
    #defining line. its like a temporary var
    line = ''
    #for each pixel in the x axis in a range from 0 to width with a step of 1 run a command
    for x in range(0, width, 1):
        print(ITEMS[pix[x, y]])
        input("this goes up to 11")
        #the variable line will equil what ever it's value was last execution + the value of ITEMS in the imaged loaded to the variable pix at the location of x,y adding a | symbol for effect 
        line += ITEMS[pix[x, y]] + '|'
    print(line[:-1])
input('Dont leave yet.')
exit()
