from PIL import *
from scipy import ndimage
import numpy as np
from skimage import io

im = Image.open("exp.jpg")
width,height=im.size
def create_image(i,j):
    image=Image.new("RGB",(i,j),"White")
    return image
def get_pixel(image,i,j):
    width,height=image.size
    if i>width or j>height:
        return none
    pixel=image.getpixel((i,j))
    return pixel
def black_white():  
    new=create_image(width,height)
    pixels=new.load()
    for i in range(width):
        for j in range(height):
            pixel=get_pixel(im,i,j)
            red=pixel[0]
            green=pixel[1]
            blue=pixel[2]
            gray=(red*0.299)+(green*0.587)+(blue*0.114)
            pixels[i,j]=(int(gray),int(gray),int(gray))
    new.save("output.jpg",'png')
def red_extract():
    new=create_image(width,height)
    pixels=new.load()
    for i in range(width):
        for j in range(height):
            pixel=get_pixel(im,i,j)
            red=pixel[0]
            green=pixel[1]
            blue=pixel[2]
            gray=(red*0.299)+(green*0.587)+(blue*0.114)
            pixels[i,j]=(red,int(gray),int(gray))
    new.save("output.jpg",'png')
def blue_extract():
    new=create_image(width,height)
    pixels=new.load()
    for i in range(width):
        for j in range(height):
            pixel=get_pixel(im,i,j)
            red=pixel[0]
            green=pixel[1]
            blue=pixel[2]
            gray=(red*0.299)+(green*0.587)+(blue*0.114)
            pixels[i,j]=(int(gray),int(gray),blue)
    new.save("output.jpg",'png')
def green_extract():
    new=create_image(width,height)
    pixels=new.load()
    for i in range(width):
        for j in range(height):
            pixel=get_pixel(im,i,j)
            red=pixel[0]
            green=pixel[1]
            blue=pixel[2]
            gray=(red*0.299)+(green*0.587)+(blue*0.114)
            pixels[i,j]=(int(gray),green,int(gray))
    new.save("output.jpg",'png')
def redfilter():
    new=create_image(width,height)
    pixels=new.load()
    for i in range(width):
        for j in range(height):
            pixel=get_pixel(im,i,j)
            red=pixel[0]
            pixels[i,j]=(red,0,0)
    new.save("output.jpg",'png')
def greenfilter():
    new=create_image(width,height)
    pixels=new.load()
    for i in range(width):
        for j in range(height):
            pixel=get_pixel(im,i,j)
            green=pixel[1]
            pixels[i,j]=(0,green,0)
    new.save("output.jpg",'png')
def bluefilter():
    new=create_image(width,height)
    pixels=new.load()
    for i in range(width):
        for j in range(height):
            pixel=get_pixel(im,i,j)
            blue=pixel[2]
            pixels[i,j]=(0,0,blue)
    new.save("output.jpg",'png')
def brightness(value):
    new=create_image(width,height)
    pixels=new.load()
    for i in range(width):
        for j in range(height):
            pixel=get_pixel(im,i,j)
            red=pixel[0]
            green=pixel[1]
            blue=pixel[2]
            pixels[i,j]=(int(red*value),int(green*value),int(blue*value))
    new.save("output.jpg",'png')
