

from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image


model = load_model("shape.h5") # loading our model

def predict(InputImg):
    
    img=image.load_img(InputImg,target_size=(64,64)) #load and reshaping the image
    x=image.img_to_array(img)#converting image to array
    x=np.expand_dims(x,axis=0)
    pred=model.predict_classes(x)
    #pred=np.argmax(model.predict(x), axis=-1)
    print(pred)
    index=['circle', 'square', 'triangle']
    result=str(index[pred[0]])


    return result