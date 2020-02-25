'''
Created on Jan 6, 2020

@author: nicomp
'''
# This one is in Main.py only
from image_functions import *


# open an image file. The default path is where this python module is
im = Image.open("SiriusAndViolet.jpg")
print(im.width, im.height, im.mode, im.format)  # Display some info about the image

"""
    Load an image file from disk
    :param filename: The file to load
    :return the image object
"""
'''

my_image = load_image("SiriusAndViolet.jpg")
my_image.show(my_image)
'''
im = Image.open("SiriusAndViolet.jpg")  
im_c = im.crop((200,300,400,500)) # (left, top, right, bottom) it's a tuple!
im_c.show()
