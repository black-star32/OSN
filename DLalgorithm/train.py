import os
import tensorflow as tf
import time
import numpy
from text_cnn import TextCNN
import datetime

# Define hyperparameters

# Data loading parameters
import data_process
import word2vec_helpers

tf.flags.DEFINE_float("dev_sample_percentage", .1, "Percentage of the training data to use for validation")
tf.flags.DEFINE_string("dir_cleaned_path", "D:/data/weibo_dataset/cleaned_data/weibo_fenlei",
                    "Data source for the load_cleaned_data")
tf.flags.DEFINE_integer("num_labels", 23, "Number of labels for data.")
# Model hyperparameters
# tf.flags.DEFINE_integer("embedding_dim", 128, "Dimensionality of character embedding")
tf.flags.DEFINE_integer("embedding_dim", 16, "Dimensionality of character embedding")
tf.flags.DEFINE_string("filter_sizes", "3,4,5", "Comma-spearated filter sizes (default: '3,4,5')")
tf.flags.DEFINE_integer("num_filters", 16, "Number of filters per filter size (default: 128)")
tf.flags.DEFINE_float("dropout_keep_prob", 0.5, "Dropout keep probability (default: 0.5)")
tf.flags.DEFINE_float("l2_reg_lambda", 0.0, "L2 regularization lambda (default: 0.0)")

# Training paramters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
tf.flags.DEFINE_integer("num_epochs", 10, "Number of training epochs (default: 200)")
tf.flags.DEFINE_integer("evaluate_every", 100, "Evalue model on dev set after this many steps (default: 100)")
tf.flags.DEFINE_integer("checkpoint_every", 100, "Save model after this many steps (defult: 100)")
tf.flags.DEFINE_integer("num_checkpoints", 5, "Number of checkpoints to store (default: 5)")

#Misc parameters
tf.flags.DEFINE_boolean("log_device_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("allow_soft_placement", False, "Log placement of ops on devices")

# Parse parameters from commands
FLAGS = tf.flags.FLAGS

print("Parameters:")
for attr, value in sorted(FLAGS.flag_values_dict().items()):
    print("{}={}".format(attr.upper(), value))
print("")

# Prepare output directory for models and summaries
#output directory
timestamp = str(time.time())
output_dir = os.path.abspath(os.path.join(os.path.curdir, "run", timestamp))
print("Writing to {}\n".format(output_dir))
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Data preprocess
print("Loading data...")
x_text, y = data_process.load_cleaned_data_files(FLAGS.dir_cleaned_path)
# print(data)
# Get embedding vector
# 填充句子
sentences, max_document_lenth = data_process.padding_sentences(x_text, '补')
# del x_text
# 将句子转化为向量
# x = numpy.array(word2vec_helpers.embedding_sentences(sentences, embedding_size=FLAGS.embedding_dim,
#                                                      file_to_load = 'trained_word2vec.model',
#                                                      ))
x = numpy.array(word2vec_helpers.embedding_sentences(sentences, embedding_size=FLAGS.embedding_dim,
                                                     file_to_save=os.path.join(output_dir,'trained_word2vec.model')))
y = numpy.array(y)
print("x.shape = {}".format(x.shape))
print("y.shape = {}".format(y.shape))

# Save params
training_params_file = os.path.join(output_dir,'training_params.pickle')
params = {'num_labels': FLAGS.num_labels, 'max_document_length': max_document_lenth}
data_process.save_dict(params, training_params_file)

#Shuffle data randomly
numpy.random.seed(10)
# 打乱指数
shuffle_indices = numpy.random.permutation(numpy.arange(len(y)))
x_shuffled = x[shuffle_indices]
y_shuffled = y[shuffle_indices]

# split train/test set
dev_sample_index = -1 * int(FLAGS.dev_sample_percentage * float(len(y)))
x_train, x_dev = x_shuffled[:dev_sample_index], x_shuffled[dev_sample_index:]
y_train, y_dev = y_shuffled[:dev_sample_index], y_shuffled[dev_sample_index:]
print("Train/Dev split: {:d}/{:d}".format(len(y_train),len(y_dev)))

#Training
with tf.Graph().as_default():
    session_config = tf.ConfigProto(
        log_device_placement = FLAGS.log_device_placement,  # 是否打印设备分配日志
        allow_soft_placement = FLAGS.allow_soft_placement   # 如果你指定的设备不存在，允许TF自动分配设备
    )
    sess = tf.Session(config=session_config)
    with sess.as_default():
        cnn = TextCNN(
            sequence_length=x_train.shape[1],
            num_classes=y_train.shape[1],
            embedding_size=FLAGS.embedding_dim,
            filter_sizes=list(map(int, FLAGS.filter_sizes.split(","))),
            num_filters=FLAGS.num_filters,
            l2_reg_lambda=FLAGS.l2_reg_lambda)

        # Define Training procedure
        global_step = tf.Variable(0, name="global_step", trainable=False)
        # 对于在变量列表中的变量计算对于损失函数的梯度，这个函数返回一个（梯度，变量）对的列表，其中梯度就是相对应变量的梯度
        optimizer = tf.train.AdamOptimizer(1e-3)
        grads_and_vars = optimizer.compute_gradients(cnn.loss)
        train_op = optimizer.apply_gradients(grads_and_vars, global_step=global_step)

        # Keep track of gradient values and sparsity (optional)
        grad_summaries = []
        for g, v in grads_and_vars:
            if g is not None:
                grad_hist_summary = tf.summary.histogram("{}/grad/hist".format(v.name), g)
                sparsity_summary = tf.summary.scalar("{}/grad/sparsity".format(v.name), tf.nn.zero_fraction(g))
                grad_summaries.append(grad_hist_summary)
                grad_summaries.append(sparsity_summary)
        grad_summaries_merged = tf.summary.merge(grad_summaries)

        # Output directory for models and summaries
        print("Writing to {}\n".format(output_dir))

        # Summaries for loss and accuracy
        loss_summary = tf.summary.scalar("loss", cnn.loss)
        acc_summary = tf.summary.scalar("accuracy", cnn.accuracy)

        # Train Summaries
        train_summary_op = tf.summary.merge([loss_summary, acc_summary, grad_summaries_merged])
        train_summary_dir = os.path.join(output_dir, "summaries", "train")
        train_summary_writer = tf.summary.FileWriter(train_summary_dir, sess.graph)

        # Dev summaries
        dev_summary_op = tf.summary.merge([loss_summary, acc_summary])
        dev_summary_dir = os.path.join(output_dir, "summaries", "dev")
        dev_summary_writer = tf.summary.FileWriter(dev_summary_dir, sess.graph)

        # Checkpoint directory. Tensorflow assumes this directory already exists so we need to create it
        checkpoint_dir = os.path.abspath(os.path.join(output_dir, "checkpoints"))
        checkpoint_prefix = os.path.join(checkpoint_dir, "model")
        if not os.path.exists(checkpoint_dir):
            os.makedirs(checkpoint_dir)
        saver = tf.train.Saver(tf.global_variables(), max_to_keep=FLAGS.num_checkpoints)

        # # Initialize all variables
        # sess.run(tf.global_variables_initializer())
        #
        #
        # def train_step(x_batch, y_batch):
        #     """
        #     A single training step
        #     """
        #     feed_dict = {
        #         cnn.input_x: x_batch,
        #         cnn.input_y: y_batch,
        #         cnn.dropout_keep_prob: FLAGS.dropout_keep_prob
        #     }
        #     _, step, summaries, loss, accuracy = sess.run(
        #         [train_op, global_step, train_summary_op, cnn.loss, cnn.accuracy],
        #         feed_dict)
        #     time_str = datetime.datetime.now().isoformat()
        #     print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
        #     train_summary_writer.add_summary(summaries, step)
        #
        #
        # def dev_step(x_batch, y_batch, writer=None):
        #     """
        #     Evaluates model on a dev set
        #     """
        #     feed_dict = {
        #         cnn.input_x: x_batch,
        #         cnn.input_y: y_batch,
        #         cnn.dropout_keep_prob: 1.0
        #     }
        #     step, summaries, loss, accuracy = sess.run(
        #         [global_step, dev_summary_op, cnn.loss, cnn.accuracy],
        #         feed_dict)
        #     time_str = datetime.datetime.now().isoformat()
        #     print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
        #     # fe.write("{}: step {}, loss {:g}, acc {:g}\n".format(time_str, step, loss, accuracy))
        #     if writer:
        #         writer.add_summary(summaries, step)
        #
        #
        # # Generate batches
        # batches = data_process.batch_iter(
        #     list(zip(x_train, y_train)), FLAGS.batch_size, FLAGS.num_epochs)
        #
        # # Training loop. For each batch...
        # for batch in batches:
        #     x_batch, y_batch = zip(*batch)
        #     train_step(x_batch, y_batch)
        #     current_step = tf.train.global_step(sess, global_step)
        #     if current_step % FLAGS.evaluate_every == 0:
        #         print("\nEvaluation:")
        #         dev_step(x_dev, y_dev, writer=dev_summary_writer)
        #         print("")
        #     if current_step % FLAGS.checkpoint_every == 0:
        #         path = saver.save(sess, checkpoint_prefix, global_step=current_step)
        #         print("Saved model checkpoint to {}\n".format(path))

        # Initialize all variables
        sess.run(tf.global_variables_initializer())  # 初始化所有变量


        # 定义了一个函数，输入为1个batch
        def train_step(x_batch, y_batch):
            """
            A single training step
            """
            feed_dict = {
                cnn.input_x: x_batch,
                cnn.input_y: y_batch,
                cnn.dropout_keep_prob: FLAGS.dropout_keep_prob
            }
            _, step, summaries, loss, accuracy = sess.run(
                [train_op, global_step, train_summary_op, cnn.loss, cnn.accuracy],
                feed_dict)
            # 梯度更新（更新模型），步骤加一，存储数据，计算一个batch的损失，计算一个batch的准确率
            time_str = datetime.datetime.now().isoformat()  # 当时时间
            print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
            train_summary_writer.add_summary(summaries, step)


        # 定义了一个函数，用于验证集，输入为一个batch
        def dev_step(x_batch, y_batch, writer=None):
            """
            Evaluates model on a dev set
            """
            # 验证集太大，会爆内存，采用batch的思想进行计算，下面生成多个子验证集
            num = 20
            x_batch = x_batch.tolist()
            y_batch = y_batch.tolist()
            l = len(y_batch)
            l_20 = int(l / num)
            x_set = []
            y_set = []
            for i in range(num - 1):
                x_temp = x_batch[i * l_20:(i + 1) * l_20]
                x_set.append(x_temp)
                y_temp = y_batch[i * l_20:(i + 1) * l_20]
                y_set.append(y_temp)
            x_temp = x_batch[(num - 1) * l_20:]
            x_set.append(x_temp)
            y_temp = y_batch[(num - 1) * l_20:]
            y_set.append(y_temp)

            # 每个batch验证集计算一下准确率，num个batch再平均
            lis_loss = []
            lis_accu = []
            for i in range(num):
                feed_dict = {
                    cnn.input_x: numpy.array(x_set[i]),
                    cnn.input_y: numpy.array(y_set[i]),
                    cnn.dropout_keep_prob: 1.0
                }
                step, summaries, loss, accuracy = sess.run(
                    [global_step, dev_summary_op, cnn.loss, cnn.accuracy],
                    feed_dict)
                lis_loss.append(loss)
                lis_accu.append(accuracy)
                time_str = datetime.datetime.now().isoformat()
                print("{}: step {}, loss {:g}, acc {:g}".format(time_str, step, loss, accuracy))
            print("test_loss and test_acc" + "\t\t" + str(sum(lis_loss) / num) + "\t\t" + str(sum(lis_accu) / num))
            if writer:
                writer.add_summary(summaries, step)


        # Generate batches（生成器），得到一个generator，每一次返回一个batch，没有构成list[batch1,batch2,batch3,...]
        batches = data_process.batch_iter(
            list(zip(x_train, y_train)), FLAGS.batch_size, FLAGS.num_epochs)
        # zip将样本与label配对，
        # Training loop. For each batch...
        for batch in batches:
            x_batch, y_batch = zip(*batch)  # unzip，将配对的样本，分离出来data和label
            train_step(x_batch, y_batch)  # 训练，输入batch样本，更新模型
            current_step = tf.train.global_step(sess, global_step)
            if current_step % FLAGS.evaluate_every == 0:  # 每多少步，算一下验证集效果
                print("\nEvaluation:")
                dev_step(x_dev, y_dev, writer=dev_summary_writer)  # 喂的数据为验证集，此时大小不止一个batchsize1的大小
                print("")
            if current_step % FLAGS.checkpoint_every == 0:  # 每多少步，保存模型
                path = saver.save(sess, checkpoint_prefix, global_step=current_step)
                print("Saved model checkpoint to {}\n".format(path))
