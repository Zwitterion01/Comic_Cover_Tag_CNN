import os
import tensorflow as tf
from PIL import Image  # 注意Image,后面会用到
#import matplotlib.pyplot as plt
import numpy as np
#Generate the tfrecord file.
cwd = 'D:\\project\\data\\theme_train\\'
classes = ( 'hotblood', 'magic','schoollove','scifi','sports')  # 人为 设定 3 类
writer = tf.python_io.TFRecordWriter("D:\\project\\data\\theme_rgb_train.tfrecords")  # 要生成的文件

for index, name in enumerate(classes):
    print(index, name)
    class_path = cwd + name + '\\'
    for img_name in os.listdir(class_path):
        img_path = class_path + img_name  # 每一个图片的地址
        img = Image.open(img_path)
        img = img.resize((32, 32))
        img_raw = img.tobytes()  # 将图片转化为二进制格式
        example = tf.train.Example(features=tf.train.Features(feature={
            "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[index])),
            'img_raw': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw]))
        }))  # example对象对label和image数据进行封装
        writer.write(example.SerializeToString())  # 序列化为字符串
        print(img_path+' done')

writer.close()