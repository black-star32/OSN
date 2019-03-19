import os
import tensorflow as tf
import time
import numpy

# Define hyperparameters

# Data loading parameters
from DLalgorithm import data_process
from DLalgorithm import word2vec_helpers

tf.flags.DEFINE_float("dev_sample_percentage", .1, "Percentage of the training data to use for validation")
tf.flags.DEFINE_string("dir_cleaned_path", "D:\pycharm\PyCharm 2017.2.3\Project\APT&OSN\data\cleaned_data\weibo_fenlei\\",
                    "Data source for the load_cleaned_data")
tf.flags.DEFINE_integer("num_labels", 23, "Number of labels for data.")
# Model hyperparameters
tf.flags.DEFINE_integer("embedding_dim", 128, "Dimensionality of character embedding")

# Training paramters

# Parse parameters from commands
FLAGS = tf.flags.FLAGS

FLAGS._parse_flags()
print("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
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
del x_text
# 将句子转化为向量
# x = numpy.array(word2vec_helpers.embedding_sentences(sentences, embedding_size=FLAGS.embedding_dim,
#                                                      file_to_load = 'trained_word2vec.model',
#                                                      file_to_save=os.path.join(output_dir,'trained_word2vec.model')))
x = numpy.array(word2vec_helpers.embedding_sentences(sentences, embedding_size=FLAGS.embedding_dim,
                                                     file_to_save=os.path.join(output_dir,'trained_word2vec.model')))
y = numpy.array(y)
print("x.shape = {}".format(x.shape))
print("y.shape = {}".format(y.shape))
