import random
import os

# change path to where images are stored
# change pathSeparator to / if on Linux

path ='C://Users//User//Pictures'
pathSeparator = '//'


print("This will sort your images which begin with IMG with tags alphabetically.\n")

for x in os.listdir(path):
    if x.endswith(('.jpg', '.png')) and x.startswith("IMG"):
        imageDir = path + pathSeparator + x
        imageExtension = x[-4:]
        print(imageDir)
        userInput = input("Input some tags for this image: ")
        userInputSplit = userInput.split(" ")
        userInputSplitSorted = sorted(userInputSplit)
        newName = '_'.join(userInputSplitSorted)
        newFileName = newName + "_" + str(random.randint(1, 100))
        newImageDir = path + pathSeparator + newFileName + imageExtension
        os.rename(imageDir, newImageDir)
        print('\n')