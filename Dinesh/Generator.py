#for input tensor
import tensorflow
normal = tensorflow.random.normal
from tensorflow.keras.models import load_model
#to plot image
import matplotlib.pyplot as plt
from PIL import Image

#load model from the h5 filepath
#h5path = '/content/drive/My Drive/ProjectData/zigzaglinev1.h5' # for colab use by me
h5path = './final32v3.h5' # for github

#noise dimension of the input. DONOT change under any circumstances. value is 150 100+50 200-50
noise_dim =150

#compile and load the model from the path
generator = load_model(h5path,compile=True)

print("Loading model Complete")

#defining the endpoint
def generate_image(fName="savefig.jpg"):
  # 16 inputs to generate 16 images.
  # inside the for loop to generate new images each time
  test_input = normal([16, noise_dim])
  
  #get the tensor returned after calculation from the model
  predictions = generator(test_input, training=False)
  
  #define figure to plot and plot the images
  fig = plt.figure(figsize=(4,4))

  for i in range(predictions.shape[0]):
      plt.subplot(4, 4, i+1)
      #not changing this because i am lazy. change and see if it works if you want
      plt.imshow(predictions[i, :, :, 0] * 127.5 + 127.5, cmap='gray')
      #cancel axis from image
      plt.axis('off')
      
  # this is the saving point. savefig.png is to be streamed to the frontend.
  # save as jpg to solve transparency issue
  plt.savefig(fName)
  
  design = Image.open(fName)
  #design_copy = design.copy()
  #img = Image.new('RGB', design.size, (255, 255, 255))
  #design_copy.paste(img)
  #design.save(fName, "PNG")
  
  return
  #unnecessary maybe but i am too lazy to change
  #plt.show()
  


if __name__ == "__main__":
  # the endpoint to call  
  generate_image()
