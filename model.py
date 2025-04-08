import time, os, glob

from PIL import Image, ImageDraw, ImageFont
from matplotlib.pyplot import imshow
i=0
image_list = []
for filename in glob.glob(r'C:\Users\chadi\Desktop\Kagglehub\train-scene classification\train\*.jpg'):
    im = Image.open(filename)

    i+=1

print(i)