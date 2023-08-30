'''
David Staffen 
464166
'''

#(#1).(#2).(#3) #1: release canidate;  #2 Major Version Change; #3 Minor version.
game_version ='0.1.0'
'''
making this on arch linux rn.... like a weirdo.
this website is a good source for text writing in pythion https://stackoverflow.com/questions/18256363/how-do-i-print-the-content-of-a-txt-file-in-python
Using this for art https://manytools.org/hacker-tools/convert-images-to-ascii-art/
time.sleep(seconds) remeber this it forces the progeme to wait is float compatyable. fhdjsfgyhdsjafhdsjklfhdsklj its 10pm I tired.
random.randrange(2,8,4) generates a random value from 2 to 8 with a step of 4
'''
'''
#saving this for later 
# Including end=' ' keeps output on same line
print('Hello there.', end=' ')
print('My name is...', end=' ')
print('Carl?')
output would be (Hello there. My name is... Carl) a neet trick for later. may save some time.

don't forget += in variables'
'''


import os
import random
import time
import save

os_type = save.os_type
player_name = save.player_name
os_clear = save.os_clear

   
#litteraly here just to make the end when I want it to die
def end():
    dummy = input("The Game has Ended. Press ENTER to end program:")
    exit()

#this function will  open a file and return the contents of the file. text files that is.
def file_contents(file):
    #file you want "unpacked"
    with open(file,'r') as f:
        dialog = f.read()
    return(dialog)

#used to write to things like a save file. I'm sure thius will totaly get used other places.
def file_write(file,content):
    #file you want wrten to
    #content is the content you want writen to it
    with open(file,'w+') as f:
       i = 0
       while i < len(content):
        f.write(content[i])
        f.write('\n')
        i = i + 1

#Plan on using this function to clear the screen and print graphics. might work.
def print_screen(print_file, mode):
    #print_file is the file you want to print out
    #mode, d - dialog, s - sprite (ASCII) 
    os.system(os_clear)
    if mode == "d":
        print(file_contents('dialog/'+print_file))
    elif mode == "s":
        print(file_contents('sprites/'+print_file))
    elif mode == "t":
        print(file_contents("dialog/title"))
    else:
        print('You have cuased a critial Error lol')
        end()

#this is here for when I flesh out how player action logic works
def player_input():
    print("fuck off errors")
    end()

def your_name():
    print('[What is your name?]')
    player_name = input('>_')
    print('Your name is "'+player_name+'"?')
    print('[yes],[no]')
    temp_confirm = input('>_')
    if temp_confirm == "Yes" or temp_confirm == "yes"or temp_confirm == "y"or temp_confirm == "Y":
        return(player_name)
    elif temp_confirm == "No" or temp_confirm == "no"or temp_confirm == "n"or temp_confirm == "N":
        return your_name()
    else:
        print('You said '+temp_confirm+". that don't make sense. Try Again.")
        return your_name()




#Functions from this point on are there to do actual game stuff. ^^^^ is the stuff for the gmae to function.

#the into if no save is detected to load
def intro():
    #each os.system(os_clear) represents a new screen or section really.
    os.system(os_clear)

    #intoduction that the playfile_write('testsave', os_type)er actualy sees
    print_screen("dummy","t")
    dummy = input("         Press Enter to Continue")
    print_screen("intro","d")

    save_file_temp = []
    save_file_temp.append('os_type = "'+ os_type +'"')
    save_file_temp.append('os_clear = "'+os_clear+'"')
    save_file_temp.append('player_name = "'+your_name()+'"')
    file_write('save.py',save_file_temp)

    os.system(os_clear)
    print("for now that is all. Reload this program with the game now being saved and see what happens")
    end()
    #each os.system(os_clear) represents a new screen or section really.
    os.system(os_clear)

#somethiong to show a new load.
def  loaded_save():
    os.system(os_clear)
    print("Save loaded: " + player_name+"\nRemeber to play this on "+os_type+" or the program will break. \nKnowing me it will break anyway.")
    print()
    end()
if os_type == '':
    #OS test and set up
    os_type = input("What is your OS? Use one of the following exsaclty. [windows, linux]") #temp disabed for testing other things. I will have to make a debug set of tools here soon or risk shooting myself in the foot.

    #logic for the OS setting
    if os_type == "linux":
        print("OS is set to linux")
        os_clear = 'clear'
        os.system('title LOVE ' + game_version)
    elif os_type == "windows":
        print("OS is set to windows")
        os_clear = 'cls'
        os.system('title LOVE ' + game_version)
    elif os_type == "andoird":
        print('andoird bitch')
        end()
    else:
        print("Don't try this. It will break")
        end()
    intro()
elif os_type == "windows" or os_type == "linux":
    loaded_save()
    end()
else:
    end()
