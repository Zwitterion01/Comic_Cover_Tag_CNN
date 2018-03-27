import random
import os
from PIL import Image
#Generate the test dataset.
list_name=[]
filedir='D:\\project\\data\\theme_train\\sports'
for file in os.listdir(filedir):
              file_path = os.path.join(filedir, file)
              list_name.append(file_path)
#for x in list_name:
slice = random.sample(list_name,15)
for x in slice:
    '''
    f1 = open(x, 'r')
    lena = Image.open(x)
    f=x.replace('.jpg','co.jpg')
    lena.save(f)
    f1.close()'''
    os.remove(x)
    print(x+' done')