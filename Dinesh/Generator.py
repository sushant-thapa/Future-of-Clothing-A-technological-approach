#for input tensor
import tensorflow
normal = tensorflow.random.normal
from tensorflow.keras.models import load_model
#to plot image
import matplotlib.pyplot as plt

#defining the endpoint
def generate_image(fName="savefig.png"):
    
    #load model from the h5 filepath
    #h5path = '/content/drive/My Drive/ProjectData/zigzaglinev1.h5' # for colab use by me
    h5path32 = './final32v3.h5' # for github
    h5path128 = './final128v5u.h5'
    
    
    #compile and load the model from the path
    try:
        generator32 = load_model(h5path32, compile=True)
        generator128 = load_model(h5path128, compile=True)
    except:
        print("something wrong with path or the generator save file. Please check")
        
    
    #noise dimension of the input. DONOT change under any circumstances. value is 150 100+50 200-50
    noise_dim32 =150
    noise_dim128=20
    
    #create noise inputs for the system
    noise32 = normal([16, noise_dim32])
    noise128 = normal([16, noise_dim32])
    
    #input for larger generator from smaller generator
    generator_input = generator(generator32, noise32)
    #output from larger generator
    generator_output = generator(generator128, [noise128, generator_input])
    
    #save the 16 images obtained as savefig.png
    save_image(generator_output)



def generator(model, test_input):
    prediction = generator(test_input, training = False)
    return prediction

def save_image(predictions, fName='savefig.png'):
    fig = plt.figure(figsize=(4,4))
        
    for i in range(predictions.shape[0]):
        plt.subplot(4, 4, i+1)
        #not changing this because i am lazy. change and see if it works if you want
        plt.imshow(predictions[i, :, :, 0] * 127.5 + 127.5, cmap='gray')
        #cancel axis from image
        plt.axis('off')
        
    # this is the saving point. savefig.png is to be streamed to the frontend.
    plt.savefig(fName)
  
    #copy and paste designs
    #design_copy = design.copy()
    #img = Image.new('RGB', design.size, (255, 255, 255))
    #design_copy.paste(img)
    #design.save(fName, "PNG")
    
    return

if __name__ == "__main__":
  # the endpoint to call  
  generate_image()






#old function

#def generate_image(fName="savefig.png"):
    
  #16 inputs to generate 16 images.
  #inside the for loop to generate new images each time
  #test_input = normal([16, noise_dim])
  
  #get the tensor returned after calculation from the model
  #predictions = generator(test_input, training=False)
  
  #define figure to plot and plot the images
  #fig = plt.figure(figsize=(4,4))

  #for i in range(predictions.shape[0]):
      #plt.subplot(4, 4, i+1)
      #not changing this because i am lazy. change and see if it works if you want
      #plt.imshow(predictions[i, :, :, 0] * 127.5 + 127.5, cmap='gray')
      #cancel axis from image
      #plt.axis('off')
      
  #this is the saving point. savefig.png is to be streamed to the frontend.
  #plt.savefig(fName)
  
  #copy and paste designs
  #design_copy = design.copy()
  #img = Image.new('RGB', design.size, (255, 255, 255))
  #design_copy.paste(img)
  #design.save(fName, "PNG")
  
  #return
  #unnecessary maybe but i am too lazy to change
  #plt.show()
