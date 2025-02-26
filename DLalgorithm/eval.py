#! /usr/bin/env python

import tensorflow as tf
import numpy as np
import os
import time
import datetime
import data_process
import word2vec_helpers
from text_cnn import TextCNN
import csv

# Parameters
# ==================================================

# Data Parameters
tf.flags.DEFINE_string("input_text_file", "D:/data/weibo_dataset/cleaned_data/weibo1/", "Test text data source to evaluate.")
tf.flags.DEFINE_string("input_label_file", "", "Label file for test text data source.")

# Eval Parameters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: 64)")
tf.flags.DEFINE_string("checkpoint_dir", "D:/pycharm/PyCharm 2018.3.2/projects/OSN/DLalgorithm/run/1557995852.5313356/checkpoints/", "Checkpoint directory from training run")
tf.flags.DEFINE_boolean("eval_train", True, "Evaluate on all training data")

# Misc Parameters
tf.flags.DEFINE_boolean("allow_soft_placement", True, "Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement", False, "Log placement of ops on devices")

# Parse parameters from commands
FLAGS = tf.flags.FLAGS

print("Parameters:")
for attr, value in sorted(FLAGS.flag_values_dict().items()):
    print("{}={}".format(attr.upper(), value))
print("")

# validate
# ==================================================

# validate checkout point file
checkpoint_file = tf.train.latest_checkpoint(FLAGS.checkpoint_dir)
if checkpoint_file is None:
    print("Cannot find a valid checkpoint file!")
    exit(0)
print("Using checkpoint file : {}".format(checkpoint_file))

# validate word2vec model file
trained_word2vec_model_file = os.path.join(FLAGS.checkpoint_dir, "..", "trained_word2vec.model")
if not os.path.exists(trained_word2vec_model_file):
    print("Word2vec model file \'{}\' doesn't exist!".format(trained_word2vec_model_file))
print("Using word2vec model file : {}".format(trained_word2vec_model_file))

# validate training params file
training_params_file = os.path.join(FLAGS.checkpoint_dir, "..", "training_params.pickle")
if not os.path.exists(training_params_file):
    print("Training params file \'{}\' is missing!".format(training_params_file))
print("Using training params file : {}".format(training_params_file))

# Load params
params = data_process.load_dict(training_params_file)
num_labels = int(params['num_labels'])
max_document_length = int(params['max_document_length'])


def predict(filename, input_file, max_document_length):
    # Load data
    if FLAGS.eval_train:
        x_raw, y_test = data_process.load_data_and_labels(input_file, FLAGS.input_label_file, num_labels)
    else:
        x_raw = ["a masterpiece four years in the making", "everything is off."]
        y_test = [1, 0]

    # Get Embedding vector x_test
    if len(x_raw) == 0:
        return
    sentences, max_document_length = data_process.padding_sentences(x_raw, '补', padding_sentence_length = max_document_length)
    #此处有问题，data_process.padding_sentences返回后一些句子长度会增加1，这些句子都是过长进行裁剪的，原因不清楚，暂时通过二次裁剪修正
    sentences = [sentence[:max_document_length] for sentence in sentences]
    x_test = np.array(word2vec_helpers.embedding_sentences(sentences, file_to_load = trained_word2vec_model_file))
    print(len(x_test))

    print("x_test.shape = {}".format(x_test.shape))



    # Evaluation
    # ==================================================
    print("\nEvaluating...\n")
    checkpoint_file = tf.train.latest_checkpoint(FLAGS.checkpoint_dir)
    graph = tf.Graph()
    with graph.as_default():
        session_conf = tf.ConfigProto(
          allow_soft_placement=FLAGS.allow_soft_placement,
          log_device_placement=FLAGS.log_device_placement)
        sess = tf.Session(config=session_conf)
        with sess.as_default():
            # Load the saved meta graph and restore variables
            saver = tf.train.import_meta_graph("{}.meta".format(checkpoint_file))
            saver.restore(sess, checkpoint_file)

            # Get the placeholders from the graph by name
            input_x = graph.get_operation_by_name("input_x").outputs[0]
            # input_y = graph.get_operation_by_name("input_y").outputs[0]
            dropout_keep_prob = graph.get_operation_by_name("dropout_keep_prob").outputs[0]

            # Tensors we want to evaluate
            predictions = graph.get_operation_by_name("output/predictions").outputs[0]

            # Generate batches for one epoch
            batches = data_process.batch_iter(list(x_test), FLAGS.batch_size, 1, shuffle=False)

            # Collect the predictions here
            all_predictions = []

            for x_test_batch in batches:
                batch_predictions = sess.run(predictions, {input_x: x_test_batch, dropout_keep_prob: 1.0})
                all_predictions = np.concatenate([all_predictions, batch_predictions])

    # Print accuracy if y_test is defined
    if y_test is not None:
        correct_predictions = float(sum(all_predictions == y_test))
        print("Total number of test examples: {}".format(len(y_test)))
        print("Accuracy: {:g}".format(correct_predictions/float(len(y_test))))

    # Save the evaluation to a csv
    # predictions_human_readable = np.column_stack((np.array([text.encode('utf-8') for text in x_raw]), all_predictions))
    predictions_human_readable = np.column_stack((np.array(x_raw), all_predictions))
    out_path = os.path.join(FLAGS.checkpoint_dir, "..", filename)
    print("Saving evaluation to {0}".format(out_path))
    with open(out_path, 'w') as f:
        csv.writer(f).writerows(predictions_human_readable)


for root,dirs,files in os.walk(FLAGS.input_text_file):
    for filename in files:
        input_file = os.path.join(FLAGS.input_text_file, filename)
        # print(filename, input_file, max_document_length)
        predict(filename, input_file, max_document_length)
