import tensorflow as tf
import model_2XCNN
import model_3XCNN
from PIL import Image
import numpy as np
import os
#Test procedure/ Predictor.
def getpro(filename,type):
  log_dir = 'D:\\project\\data\\3XCNN_theme_model'
  #image_arr = get_one_image(test_file)
  image = Image.open(filename)
  image = image.resize([32, 32])
  image_arr = np.array(image)
  with tf.Graph().as_default():
      image = tf.cast(image_arr, tf.float32)* (1. / 255) - 0.5
      #image = tf.image.per_image_standardization(image)
      image = tf.reshape(image, [1,32, 32, 3])
      p = model_3XCNN.mmodel(image, 1)
      logits = tf.nn.softmax(p)
      x = tf.placeholder(tf.float32, shape=[32, 32, 3])
      saver = tf.train.Saver()
      with tf.Session() as sess:
        ckpt = tf.train.get_checkpoint_state(log_dir)
        if ckpt and ckpt.model_checkpoint_path:
            global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
            saver.restore(sess, ckpt.model_checkpoint_path)
            #print('Loading success')
        else:
            print('No checkpoint')
        prediction = sess.run(logits, feed_dict={x: image_arr})
        print(prediction)
        max_index1 = np.argmax(prediction)
        prediction[0][max_index1]=0
        max_index2 = np.argmax(prediction)
        print(filename + ' ' + str(max_index1)+ ' ' + str(max_index2))
        if type==0:
         if(max_index1==0 or max_index2==0):
             return 1
         else:
             return 0
        if type == 1:
            if (max_index1 == 1 or max_index2 == 1):
                return 1
            else:
                return 0
        if type == 2:
            if (max_index1 == 2 or max_index2 == 2):
                return 1
            else:
                return 0
        if type == 3:
            if (max_index1 == 3 or max_index2 == 3):
                return 1
            else:
                return 0
        if type == 4:
            if (max_index1 == 4 or max_index2 == 4):
                return 1
            else:
                return 0
total=0;
r_total=0;


filedir1='D:\\project\\data\\theme_test\\hotblood'
list_name1=[]
r_total0=0;
total0=0;
for file in os.listdir(filedir1):
              file_path = os.path.join(filedir1, file)
              list_name1.append(file_path)
for x in list_name1:
    result=getpro(x,0)
    r_total = r_total + result
    total = total + 1
    r_total0 = r_total0 + result
    total0 = total0 + 1
    pre = float(r_total) / float(total)
    pre0 = float(r_total0) / float(total0)
    print(pre)

print('HotBlood Over')
filedir2='D:\\project\\data\\theme_test\\magic'
list_name2=[]
r_total1=0;
total1=0;
for file in os.listdir(filedir2):
              file_path = os.path.join(filedir2, file)
              list_name2.append(file_path)
for x in list_name2:
    result=getpro(x,1)
    r_total = r_total + result
    total = total + 1
    r_total1 = r_total1 + result
    total1 = total1 + 1
    pre = float(r_total) / float(total)
    pre1 = float(r_total1) / float(total1)
    print(pre)

print('Magic Over')
filedir3='D:\\project\\data\\theme_test\\schoollove'
list_name3=[]
r_total2=0;
total2=0;
for file in os.listdir(filedir3):
              file_path = os.path.join(filedir3, file)
              list_name3.append(file_path)
for x in list_name3:
    result=getpro(x,2)
    r_total = r_total + result
    total = total + 1
    r_total2 = r_total2 + result
    total2 = total2 + 1
    pre = float(r_total) / float(total)
    pre2 = float(r_total2) / float(total2)
    print(pre)

print('Schoollove Over')
filedir4='D:\\project\\data\\theme_test\\scifi'
list_name4=[]
r_total3=0;
total3=0;
for file in os.listdir(filedir4):
              file_path = os.path.join(filedir4, file)
              list_name4.append(file_path)
for x in list_name4:
    result=getpro(x,3)
    r_total = r_total + result
    total = total + 1
    r_total3 = r_total3 + result
    total3 = total3 + 1
    pre = float(r_total) / float(total)
    pre3 = float(r_total3) / float(total3)
    print(pre)

print('Scifi Over')
filedir5='D:\\project\\data\\theme_test\\sports'
list_name5=[]
r_total4=0;
total4=0;
for file in os.listdir(filedir5):
              file_path = os.path.join(filedir5, file)
              list_name5.append(file_path)
for x in list_name5:
    result=getpro(x,4)
    r_total = r_total + result
    total = total + 1
    r_total4 = r_total4 + result
    total4 = total4 + 1
    pre = float(r_total) / float(total)
    pre4 = float(r_total4) / float(total4)
    print(pre)
print('Sports Over All Over')
print('The accuracy of HotBlood is:'+str(pre0))
print('The accuracy of Magic is:'+str(pre1))
print('The accuracy of Schoollove is:'+str(pre2))
print('The accuracy of Scifi is:'+str(pre3))
print('The accuracy of Sports is:'+str(pre4))
print('Total accuracy is:'+str(pre))