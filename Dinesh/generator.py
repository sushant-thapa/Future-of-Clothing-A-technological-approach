# -*- coding: utf-8 -*-
import os
#for input tensor
import tensorflow
import numpy as np
from random import randint
normal = tensorflow.random.normal
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import plot_model
#to plot image
import matplotlib.pyplot as plt
from PIL import Image
import pydot
import tensorflow.keras
import pydotplus
from tensorflow.keras.utils import model_to_dot
tensorflow.keras.utils.pydot = pydot

# save_image(generator_output,fName)


def generator(model, test_input):
    prediction = model(test_input, training = False)
    return prediction

def return_image(name, random_Color):
    design_to_save = Image.open(name)
    design_to_save = np.array(design_to_save)
    for i in range(len(design_to_save)):
      for j in range(len(design_to_save[0])):
        if sum(design_to_save[i][j][:2])/3 > 100:
          design_to_save[i][j]= (random_Color[0], random_Color[1], random_Color[2],255)
    design_to_save = Image.fromarray(design_to_save)
    return design_to_save

def save_image(predictions, fName='savefig.png'):
    fig = plt.figure(figsize=(4,4))
        
    for i in range(predictions.shape[0]):
       plt.subplot(4, 4, i+1)
       #not changing this because i am lazy. change and see if it works if you want
       plt.imshow(predictions[i, :, :, 0] * 127.5 + 127.5, cmap='gray')
       #cancel axis from image
       plt.axis('off')
    plt.savefig('small' + fName)
    plt.clf()
    plt.imshow(predictions[randint(1,len(predictions)) -1 , :, :, 0] * 127.5 + 127.5, cmap='gray')
    plt.axis('off')
    # this is the saving point. savefig.png is to be streamed to the frontend.
    plt.savefig(fname+ ' sample1.png')
    plt.clf()
    plt.imshow(predictions[randint(1,len(predictions))-1, :, :, 0] * 127.5 + 127.5, cmap='gray')
    plt.axis('off')
    # this is the saving point. savefig.png is to be streamed to the frontend.
    plt.savefig(fname+ ' sample2.png')
    plt.clf()
    plt.imshow(predictions[randint(1,len(predictions))-1, :, :, 0] * 127.5 + 127.5, cmap='gray')
    plt.axis('off')
    # this is the saving point. savefig.png is to be streamed to the frontend.
    plt.savefig(fname+ ' sample3.png')
    
  
    #copy and paste designs
    #design_copy = design.copy()
    #img = Image.new('RGB', design.size, (255, 255, 255))
    random_Color = (randint(100,255), randint(100,255), randint(1,255))
    # random_Color = (255,255,255)
    img = Image.new('RGB', (3048, 3048), random_Color)
    designs = []
    designs.append(return_image('hello.png', random_Color))
    designs.append(return_image('hello2.png', random_Color))
    designs.append(return_image('hello3.png', random_Color))
    for i in range(20):
      x = 500* ((i//5)+1)+ randint(1, 150)
      y= 400* ((i%5)+1) + randint(1, 150)
      random_place = (x,y)
      img.paste(designs[randint(0,3)-1], random_place)
    plt.imshow(img)
    img.save(fName, "PNG")
    #design_copy.paste(img)
    #design.save(fName, "PNG")
    
    return

def generate_image(fName="savefig.png"):
    #load model from the h5 filepath
    h5path32 = './final32v3.h5' # for github
    h5path128 = './final128v12.h5'

    # h5path32 = '/content/drive/My Drive/Dinesh/final32v3.h5' # for Colab
    # h5path128 = '/content/drive/My Drive/Dinesh/final128v5u.h5'
    # h5path128 = '/content/drive/My Drive/ProjectData/final128v12n150.h5'


    #compile and load the model from the path
    try:
        generator32 = load_model(h5path32, compile=True)
        generator128 = load_model(h5path128, compile=True)
    except:
        print("something wrong with path or the generator save file. Please check")

    #noise dimension of the input. DONOT change under any circumstances. value is 150 100+50 200-
    noise_dim32 =150
    noise_dim128=150

    #create noise inputs for the system

    noise32 = normal([16, noise_dim32])
    noise128 = normal([16, noise_dim128])

    #input for larger generator from smaller generator
    generator_input = generator(generator32, noise32)
    #output from larger generator
    generator_output = generator(generator128, [generator_input, noise128])
    #save the 16 images obtained as savefig.png
    save_image(generator_input,'input.png')
    save_image(generator_output,fName)

if __name__=='__main__':
    generate_image('savefig.png')