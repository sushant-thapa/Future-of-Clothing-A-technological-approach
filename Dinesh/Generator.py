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

def return_image(tensor, random_Color):
    design_to_save = tensor.array()* 127.5 + 127.5

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
    plt.savefig(fName)
    plt.clf()

    # plt.imshow(predictions[randint(1,len(predictions)) -1 , :, :, 0] * 127.5 + 127.5, cmap='gray')
    # plt.axis('off')
    # plt.savefig('sample1.png')
    # plt.clf()
    # plt.imshow(predictions[randint(1,len(predictions))-1, :, :, 0] * 127.5 + 127.5, cmap='gray')
    # plt.axis('off')
    # plt.savefig('sample2.png')
    # plt.clf()
    # plt.imshow(predictions[randint(1,len(predictions))-1, :, :, 0] * 127.5 + 127.5, cmap='gray')
    # plt.axis('off')
    # plt.savefig('sample3.png')
    
    random_Color = (randint(100,255), randint(100,255), randint(1,255))
    for i in range(randint(1,3)):
        designs.append(return_image( predictions[randint(1,len(predictions)) -1 , :, :, 0] , random_Color)
    # random_Color = (255,255,255)
    img = Image.new('RGB', (3048, 3048), random_Color)
    # designs = []
    # designs.append(return_image('sample1.png', random_Color))
    # designs.append(return_image('sample2.png', random_Color))
    # designs.append(return_image('sample3.png', random_Color))

    for i in range(60 if 'input' in fname else 20):
        if 'input' in fname:
            dim = 32
            fac = 8
        else:
            dim = 128
            fac = 5
        x = 500 * ((i//5)+1)+ randint(1, 1.25*dim)
        y = 400 * ((i%5)+1) + randint(1, 1.25*dim)
        random_place = (x,y)
        img.paste(designs[randint(0,3)-1], random_place)
    plt.imshow(img)

    img.save(fName, "PNG")
    return

def generate_imageold(fName="savefig.png"):
    #load model from the h5 filepath
    h5path32 = './final32v3.h5' # for github
    h5path128 = './final128v12.h5'

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
    save_image(generator_input,'designs/input.png')
    save_image(generator_output,fName)


def generate_image(fName="savefig.png"):
    #load model from the h5 filepath
    h5path32 = './final32v3.h5' # for github
    h5path128 = './final128v12.h5'

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

    noise32 = normal([1, noise_dim32])
    noise128 = normal([1, noise_dim128])

    #input for larger generator from smaller generator
    generator_input = generator(generator32, noise32)
    #output from larger generator
    generator_output = generator(generator128, [generator_input, noise128])
    # input_image = return_image(generator_input)
    output_image = return_image(generator_output)
    output_image.save(fName,'PNG')

if __name__=='__main__':
    generate_image('savefig.png')