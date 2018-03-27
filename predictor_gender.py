import tensorflow as tf
import model_2XCNN
import model_3XCNN
from PIL import Image
import numpy as np
import os
#Test procedure/ Predictor.
def getpro(filename,type):
  log_dir = 'D:\\project\\data\\people_rgb_model'
  #image_arr = get_one_image(test_file)
  image = Image.open(filename)
  image = image.resize([32, 32])
  image_arr = np.array(image)
  with tf.Graph().as_default():
      image = tf.cast(image_arr, tf.float32)* (1. / 255) - 0.5
      #image = tf.image.per_image_standardization(image)
      image = tf.reshape(image, [1,32, 32, 3])
      p = model_2XCNN.mmodel(image, 1)
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
        max_index = np.argmax(prediction)
        #if 0.2>=abs(prediction[0][1]-prediction[0][0]):
        if type==1:
            if 0.2 >= prediction[0][0] - prediction[0][1] and 0<prediction[0][0] - prediction[0][1]:
               max_index=3
            print(filename + ' ' + str(max_index))
            if (max_index == 1 or max_index == 3):
                return 1
            else:
                return 0
        if type==0:
            if 0.2 >= prediction[0][1] - prediction[0][0] and 0<prediction[0][1] - prediction[0][0]:
               max_index=3
            print(filename + ' ' + str(max_index))
            if (max_index == 0 or max_index == 3):
                return 1
            else:
                return 0




filedir='D:\\project\\data\\people_test\\female'
list_name=[]
f_total=0;
f_rtotal=0;
m_total=0;
m_rtotal=0;
total=0;
r_total=0;
for file in os.listdir(filedir):
              file_path = os.path.join(filedir, file)
              list_name.append(file_path)
for x in list_name:
    result=getpro(x,1)
    r_total=r_total+result
    f_rtotal=f_rtotal+result
    total=total+1
    f_total = f_total+1
    pre=float(r_total)/float(total)
    f_pre=float(f_rtotal)/float(f_total)
    print(pre)
print('The accuracy for the test female is：'+str(f_pre))
filedir1='D:\\project\\data\\people_test\\male'
list_name1=[]
for file in os.listdir(filedir1):
              file_path = os.path.join(filedir1, file)
              list_name1.append(file_path)
for x in list_name1:
    result2 = getpro(x, 0)
    r_total=r_total+result2
    total=total+1
    pre=float(r_total)/float(total)
    m_rtotal = m_rtotal + result2
    m_total = m_total + 1
    m_pre = float(m_rtotal) / float(m_total)
    print(m_pre)
print('The accuracy for the test male is：'+str(m_pre))
print('The accuracy for the total is：'+str(pre))