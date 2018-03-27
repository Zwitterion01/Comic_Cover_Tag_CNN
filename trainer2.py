import model_2XCNN
import model_3XCNN
import tensorflow as tf
import numpy as np
#Training machine for the model and generate the model.
img, label = model_3XCNN.read_and_decode("D:\\project\\data\\people_rgb_train.tfrecords")
img_batch, label_batch = tf.train.shuffle_batch([img, label],
                                            batch_size=50, capacity=50000, min_after_dequeue=26000)
p = model_2XCNN.mmodel(img_batch, 50)
cost = model_2XCNN.loss(p, label_batch)
train_op = model_2XCNN.training(cost, 0.0001)
acc = model_2XCNN.get_accuracy(p, label_batch)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
saver = tf.train.Saver()
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

try:
        for step in np.arange(800):
            print(step)
            if coord.should_stop():
                break
            _, train_acc, train_loss = sess.run([train_op, acc, cost])
            print("loss:{} accuracy:{}".format(train_loss, train_acc))
except tf.errors.OutOfRangeError:
     print("Done!!!")
finally:

    coord.request_stop()
coord.join(threads)
saver.save(sess, 'D:\\project\\data\\people_rgb_model\\people_rgb_model.ckpt')
sess.close()