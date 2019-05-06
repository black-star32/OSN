import tensorflow as tf

class TextCNN(object):
    """
    embedding层，卷积层，池化层，softmax层
    """
    def __init__(self, sequence_length, num_classes,
                 embedding_size, filter_sizes, num_filters, l2_reg_lambda=0.0):  #定义各种输入参数

        # Placeholders for input, output and dropout
        #（样本数*句子长度*128）的tensor, None表示样本数不定
        self.input_x = tf.placeholder(tf.float32, [None, sequence_length, embedding_size], name="input_x")
        #（样本数*类别）的tensor
        self.input_y = tf.placeholder(tf.float32, [None, num_classes], name="input_y")
        # dropout概率，防止过度拟合
        self.dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob")

        # Keeping track of l2 regularization loss (optional) l2正则的初始化，有点像sum=0
        l2_loss = tf.constant(0.0)

        # # Embedding layer
        # input_x的tensor维度为[none，seq_len], 那么这个操作的输出为none * seq_len * em_size
        self.embedded_chars = self.input_x
        # 增加一个维度，变成，batch_size*seq_len*em_size*channel(=1)的4维tensor，符合图像的习惯
        self.embedded_chars_expanded = tf.expand_dims(self.embedded_chars, -1)

        # # Create a convolution + maxpool layer for each filter size
        pooled_outputs = []
        for index, filter_size in enumerate(filter_sizes):
            with tf.name_scope("conv-maxpool-{}".format(filter_size)):  # 循环第一次，建立一个名称为如”conv-ma-3“的模块
                # Convolution Layer
                # operation1，没名称，卷积核参数，高*宽*通道*卷积个数
                filter_shape = [filter_size, embedding_size, 1, num_filters]
                # operation2，名称”W“，变量维度filter_shape的tensor
                W = tf.Variable(tf.truncated_normal(filter_shape, stddev=0.1), name="W")
                # operation3，名称"b",变量维度卷积核个数的tensor
                b = tf.Variable(tf.constant(0.1, shape=[num_filters]), name="b")
                # operation4，卷积操作，名称”conv“，与w系数相乘得到一个矩阵
                conv = tf.nn.conv2d(
                    self.embedded_chars_expanded,
                    W,
                    strides=[1, 1, 1, 1],  # 样本，height，width，channel移动距离
                    padding="VALID",
                    name="conv")
                # Apply nonlinearity
                # operation5，加上偏置，进行relu，名称"relu"
                h = tf.nn.relu(tf.nn.bias_add(conv, b), name="relu")
                # Max pooling over the outputs
                # 每个卷积核和pool处理一个样本后得到一个值，这里维度如batchsize*1*1*卷积核个数
                # 三种卷积核，append3次
                pooled = tf.nn.max_pool(
                    h,
                    ksize=[1, sequence_length - filter_size + 1, 1, 1],
                    strides=[1, 1, 1, 1],
                    padding='VALID',
                    name="pool")
                pooled_outputs.append(pooled)

       # Combine all the pooled features
        # operation，每种卷积核个数与卷积核种类的积
        num_filters_total = num_filters * len(filter_sizes)
        # operation，将outputs在第4个维度上拼接，如本来是128*1*1*64的结果3个，拼接后为128*1*1*192的tensor
        self.h_pool = tf.concat(pooled_outputs, 3)
        # operation，结果reshape为128*192的tensor
        self.h_pool_flat = tf.reshape(self.h_pool, [-1, num_filters_total])

        # Add dropout
        # 添加一个"dropout"的模块，里面一个操作，输出为dropout过后的128*192的tensor
        with tf.name_scope("dropout"):
            self.h_drop = tf.nn.dropout(self.h_pool_flat, self.dropout_keep_prob)

        # Final (unnormalized) scores and predictions
        with tf.name_scope("output"):#添加一个”output“的模块，多个operation
            # operation1，系数tensor，如192*2，192个features分2类，名称为"W"，注意这里用的是get_variables
            W = tf.get_variable(
                "W",
                shape = [num_filters_total, num_classes],
                initializer=tf.contrib.layers.xavier_initializer())

            # operation2,偏置tensor，如2，名称"b"
            b = tf.Variable(tf.constant(0.1, shape=[num_classes]), name="b")
            # operation3，loss上加入w的l2正则
            l2_loss += tf.nn.l2_loss(W)
            # operation4，loss上加入b的l2正则
            l2_loss += tf.nn.l2_loss(b)
            # operation5，scores计算全连接后的输出，如[0.2,0.7]名称”scores“
            self.scores = tf.nn.xw_plus_b(self.h_drop, W, b, name="scores")
            # operations，计算预测值，输出最大值的索引，0或者1，名称”predictions“
            self.predictions = tf.argmax(self.scores, 1, name="predictions")

        # CalculateMean cross-entropy loss
        with tf.name_scope("loss"):#定义一个”loss“的模块
            losses = tf.nn.softmax_cross_entropy_with_logits(logits=self.scores, labels=self.input_y)
            #operation1，定义losses，交叉熵，如果是一个batch，那么是一个长度为batchsize1的tensor？
            self.loss = tf.reduce_mean(losses) + l2_reg_lambda * l2_loss
            #operation2，计算一个batch的平均交叉熵，加上全连接层参数的正则

        # Accuracy
        with tf.name_scope("accuracy"):#定义一个名称”accuracy“的模块
            correct_predictions = tf.equal(self.predictions, tf.argmax(self.input_y, 1))
            #operation1，根据input_y和predictions是否相同，得到一个矩阵batchsize大小的tensor
            self.accuracy = tf.reduce_mean(tf.cast(correct_predictions, "float"), name="accuracy")
            #operation2，计算均值即为准确率，名称”accuracy“















