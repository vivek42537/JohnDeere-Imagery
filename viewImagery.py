from PIL import Image

"""
Lauren Trinks, ltrinks@purdue.edu | DMJohnDeere
"""

fromURL = True
fromDrive = False

filePathToImages = 'Imagery/URLImagery/AckermanNAIP2020-09-28 02_57_24.582799/AckermanNAIP2020-09-28 ' \
                       '02:57:24.582799.'
fileEndR = 'R.tif'
fileEndG = 'G.tif'
fileEndB = 'B.tif'

##########################################################################################################

if fromURL:

    workingImageB = Image.open(filePathToImages + fileEndB).convert('L')
    workingImageG = Image.open(filePathToImages + fileEndG).convert('L')
    workingImageR = Image.open(filePathToImages + fileEndR).convert('L')

    combinedImage = Image.merge("RGB", (workingImageB, workingImageG, workingImageR))
    combinedImage.show()

if fromDrive:

    # decide to get from drive or to use drive folder on local machine
    # code below not for anything, prevents unexpected EOF
    fromDrive = False
