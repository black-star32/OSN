import re
import os
import pickle
# str = "hello,world!!%[545]你好234世界。。。"
# # str = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", str)
# # print(str)
# # # str = re.sub(r"[^\u4e00-\u9fff]", " ", str)
# str = re.sub("[^\u4e00-\u9fff]", " ", str)
# print(str)
# str = re.sub("\s{2,}", " ", str)
# print(str)
import numpy


def mkdir_if_not_exist(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

def seperate_line(line):
    return ''.join([word + ' ' for word in line])

def clean_str(str):
    #替换非中文字符
    str = re.sub(r"[^\u4e00-\u9fff]", "", str)
    # #移除html标签
    # str = (re.compile(r'<[^>]+>', re.S)).sub('', str)
    #替换空白符
    str = re.sub(r"\s{2,}", "", str)
    #移除开头空格
    return str.strip()

def read_and_clean_weibo_file(input_file, output_cleaned_file = None):
    file1 = open(input_file, "r")
    file2 = open(output_cleaned_file, 'wb')
    lines = file1.readlines()
    # lines = clean_str(seperate_line(line.decode('utf-8')) for line in lines)
    # print(clean_str(seperate_line(lines[0])))
    # print((re.compile(r'<[^>]+>',re.S)).sub('',lines[0]))
    for line in lines:
        line = clean_str(line)
        if line == "" or line == "转发微博":
            continue
        line = seperate_line(line)
        file2.write((line + '\n').encode('utf-8'))
    file2.close()
    file1.close()
    return lines


def read_cleaned_file(input_file):
    with open(input_file, "rb") as file:
        lines = file.readlines()
        lines = [seperate_line(line.decode('utf-8')) for line in lines[:20000]]
        return lines

def load_cleaned_data_files(dir_cleaned_path):
    #从文件中读取数据
    category_1 = []
    category_2 = []
    category_3 = []
    category_4 = []
    category_5 = []
    category_6 = []
    category_7 = []
    category_8 = []
    category_9 = []
    category_10 = []
    category_11 = []
    category_12 = []
    category_13 = []
    category_14 = []
    category_15 = []
    category_16 = []
    category_17 = []
    category_18 = []
    category_19 = []
    category_20 = []
    category_21 = []
    category_22 = []
    category_23 = []
    for root,dirs,files in os.walk(dir_cleaned_path):
        for filename in files:
            input_file = os.path.join(dir_cleaned_path, filename)
            # print(filename)
            if filename == "1644114654.txt" or filename == "2286908003.txt" \
                    or filename == "1643971635.txt" or filename == "1654134123.txt":
                category_1 = read_cleaned_file(input_file)
                print(len(category_1))
            elif filename == "1715118170.txt" or filename == "1402400261.txt" \
                or filename == "2206258462" or filename == "2827386331":
                category_2 = read_cleaned_file(input_file)
                print(len(category_2))
            elif filename == "1649159940.txt" or filename == "1974561081.txt" \
                or filename == "1725765581.txt" or filename == "1825396097.txt":
                category_3 = read_cleaned_file(input_file)
                print(len(category_3))
            elif filename == "73730626.txt" or filename == "5612278337.txt" \
                or filename == "5103645868.txt" or filename == "6221623314.txt":
                category_4 = read_cleaned_file(input_file)
                print(len(category_4))
            elif filename == "3986147355.txt" or filename == "2054853403.txt" \
                or filename == "1820114225.txt" or filename == "1803310643.txt":
                category_5 = read_cleaned_file(input_file)
                print(len(category_5))
            elif filename == "1266269835.txt" or filename == "1721030997.txt" \
                or filename == "1665103091.txt":
                category_6 = read_cleaned_file(input_file)
                print(len(category_6))
            elif filename == "1638781994.txt":
                category_7 = read_cleaned_file(input_file)
                print(len(category_7))
            elif filename == "2142168143.txt" or filename == "5078700027.txt" \
                    or filename == "1796790562.txt":
                category_8 = read_cleaned_file(input_file)
                print(len(category_8))
            elif filename == "1499104401.txt":
                category_9 = read_cleaned_file(input_file)
                print(len(category_9))
            elif filename == "2307318984.txt":
                category_10 = read_cleaned_file(input_file)
                print(len(category_10))
            elif filename == "2056382103.txt" or filename == "1765148101.txt" \
                    or filename == "1796790562.txt":
                category_11 = read_cleaned_file(input_file)
                print(len(category_11))
            elif filename == "1749975705.txt" or filename == "3007406932.txt" \
                    or filename == "1796790562.txt":
                category_12 = read_cleaned_file(input_file)
                print(len(category_12))
            elif filename == "2396658275.txt":
                category_13 = read_cleaned_file(input_file)
                print(len(category_13))
            elif filename == "1920773361.txt":
                category_14 = read_cleaned_file(input_file)
                print(len(category_14))
            elif filename == "1502844527.txt":
                category_15 = read_cleaned_file(input_file)
                print(len(category_15))
            elif filename == "2306405891.txt":
                category_16 = read_cleaned_file(input_file)
                print(len(category_16))
            elif filename == "2040909313.txt":
                category_17 = read_cleaned_file(input_file)
                print(len(category_17))
            elif filename == "3306279953.txt":
                category_18 = read_cleaned_file(input_file)
                print(len(category_18))
            elif filename == "1735618041.txt":
                category_19 = read_cleaned_file(input_file)
                print(len(category_19))
            elif filename == "2035809322.txt":
                category_20 = read_cleaned_file(input_file)
                print(len(category_20))
            elif filename == "2477971432.txt":
                category_21 = read_cleaned_file(input_file)
                print(len(category_21))
            elif filename == "5888489073.txt" or filename == "2855071827.txt":
                category_22 = read_cleaned_file(input_file)
                print(len(category_22))
            elif filename == "3912522941.txt":
                category_23 = read_cleaned_file(input_file)
                print(len(category_23))
            else:
                continue
    #合并数据
    data = category_1 + category_2 + category_3 + category_4 + category_5 + category_6 + category_7 + \
           category_8 + category_9 + category_10 + category_11 + category_12 + category_13 + category_14 + \
           category_15 + category_16 + category_17 + category_18 + category_19 + category_20 + category_21 + \
           category_22 + category_23
    #生成标签
    category_1_labels = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_1]
    category_2_labels = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_2]
    category_3_labels = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_3]
    category_4_labels = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_4]
    category_5_labels = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_5]
    category_6_labels = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_6]
    category_7_labels = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_7]
    category_8_labels = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_8]
    category_9_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_9]
    category_10_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_10]
    category_11_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_11]
    category_12_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_12]
    category_13_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_13]
    category_14_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_14]
    category_15_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] for _ in category_15]
    category_16_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] for _ in category_16]
    category_17_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] for _ in category_17]
    category_18_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0] for _ in category_18]
    category_19_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] for _ in category_19]
    category_20_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] for _ in category_20]
    category_21_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] for _ in category_21]
    category_22_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] for _ in category_22]
    category_23_labels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] for _ in category_23]
    label = category_1_labels + category_2_labels + category_3_labels + category_4_labels + \
            category_5_labels + category_6_labels + category_7_labels + category_8_labels + \
            category_9_labels + category_10_labels + category_11_labels + category_12_labels + \
            category_13_labels + category_14_labels + category_15_labels + category_16_labels + \
            category_17_labels + category_18_labels + category_19_labels + category_20_labels + \
            category_21_labels + category_22_labels + category_23_labels
    return [data, label]

def padding_sentences(input_sentences, padding_token, padding_sentence_length = None):
    sentences = [sentence.split('   ') for sentence in input_sentences]
    if padding_sentence_length is not None:
        max_sentence_length = padding_sentence_length
    else:
        max_sentence_length = max([len(sentence) for sentence in sentences])
    for sentence in sentences:
        if len(sentence) > max_sentence_length:
            sentence = sentence[:max_sentence_length]
            # print("1"+ str(len(sentence)))
        else:
            #长度不足的句子用padding_token进行补充
            sentence.extend([padding_token]*(max_sentence_length - len(sentence)))
            # print("2" + str(len(sentence)))
    return (sentences, max_sentence_length)

def save_dict(input_dict, output_file):
    with open(output_file, 'wb') as file:
        pickle.dump(input_dict, file)
    return

def load_dict(dict_file):
    output_dict = None
    with open(dict_file, 'rb') as file:
        output_dict = pickle.load(file)
    return output_dict

def load_data_and_labels(input_text_file, input_label_file, num_labels):
    x_text = read_cleaned_file(input_text_file)
    y = None if not os.path.exists(input_label_file) else map(int, list(open(input_label_file, "r").readlines()))
    return (x_text, y)

def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.批量数据batchsize生成器
    定义一个函数，输出batch样本，参数为data（包括feature和label），batchsize，epoch
    """
    data = numpy.array(data)#全部数据转化为array
    data_size = len(data)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1#每个epoch有多少个batch，个数
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = numpy.random.permutation(numpy.arange(data_size))
            shuffled_data = data[shuffle_indices]# shuffled_data按照上述乱序得到新的样本
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):#开始生成batch
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)#这里主要是最后一个batch可能不足batchsize的处理
            yield shuffled_data[start_index:end_index]
            #yield，在for循环执行时，每次返回一个batch的data，占用的内存为常数

#if __name__ == '__main__':
    # str = '''<span class="url-icon"><img src="//h5.sinaimg.cn/m/emoticon/icon/default/d_taikaixin-2ea4a8779a.png" style="width:1em;height:1em;" alt="[太开心]"></span>家长说了，这沉甸甸的酷狗直播年度荣誉，得多拿点这样的奖～<span class="url-icon"><img src="//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png" style="width:1em;height:1em;" alt="[心]"></span>wuli毛毛<a href='https://m.weibo.cn/n/毛不易'>@毛不易</a> 呀，胖汪看好你呦(  )'''
    # print(clean_str(str))if __name__ == '__main__':

    # dir_original_path = "D:\data\weibo_dataset\original_data\weibo1"
    # dir_cleaned_path = "D:\data\weibo_dataset\cleaned_data\weibo1\\"
    #dir_original_path = "D:\data\weibo_dataset\original_data\weibo_fenlei"
    #dir_cleaned_path = "D:\data\weibo_dataset\cleaned_data\weibo_fenlei\\"

    # cleaned data
    #mkdir_if_not_exist(dir_cleaned_path)
    #for root,dirs,files in os.walk(dir_original_path):
       # for filename in files:
       #     input_file = os.path.join(root,filename)
       #     output_cleaned_file = os.path.join(dir_cleaned_path,filename)
       #     if os.path.exists(output_cleaned_file):
       #         continue
            # print(input_file)
            # print(output_cleaned_file)
       #    read_and_clean_weibo_file(input_file,output_cleaned_file)

    #load cleaned data
    # load_cleaned_data_files(dir_cleaned_path)
