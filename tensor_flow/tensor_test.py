# -*- coding: utf-8 -*-

#tensorflow测试
import tensorflow as tf
import os

# 忽略对cpu扩展指令的警告
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

w = tf.Variable(tf.constant(5,dtype=tf.float32))
lr = 0.1
epoch = 40
print("初始的w为:",w.numpy()) # 转为numpy数

for epoch in range(epoch): # 顶层循环，表示对数据集循环epoch次，次例的数据集
    with tf.GradientTape() as tape: # with结构到grads框架起了梯度的计算过程
        loss = tf.square(w + 1)
    grads = tape.gradient(loss,w) # gradient函数告知谁对谁求导

    w.assign_sub(lr * grads) # assign_sub 对变量做自减，即w-=lr*grads
    print("after %s epoch,w is %f,loss is %f" % (epoch,w.numpy(),loss))

# lr初始值：0.2，请自改学习率 0.001 0.999 看收敛过程
# 最终目的：找到loss最小，即w = -1 的最优参数w


# # 第二个测试 -- 这是使用gpu的
# a = tf.constant(0.1,dtype=tf.float32)
# with tf.compat.v1.Session() as sess: # with  as 处理文件读写，可以自动关闭流和处理异常
#      sess.run(a)