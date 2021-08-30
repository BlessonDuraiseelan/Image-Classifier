import os
#os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
#os.environ["CUDA_VISIBLE_DEVICES"]="-1"  # or even "-1"

from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
from glob import glob

model = load_model('model.h5')



labels = {0:'airplane',1:'car', 2:'cat',3:'dog',4:'flower',5:'fruit',6:'motorbike',7:'person'}


def pipeline_model(path):
    img = image.load_img(path,target_size=(64,64))
    img = image.img_to_array(img)
    img = img/255.0
    img = np.expand_dims(img,axis=0)

    pred = model.predict(img)
    max_preds = []
    pred = pred[0]
    for i in range(5):
        name = labels[pred.argmax()]
        per = round(np.amax(pred)*100,2)
        max_preds.append([name,per])
        ele = pred.argmax()
        pred = np.delete(pred,ele)

    paths = glob('static/uploads/*')
    if len(paths)>5:
        for path in paths[:4]:
            os.remove(path)
    return max_preds