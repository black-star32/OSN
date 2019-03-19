# 爬取用户的粉丝列表

import requests
import os
import Queue    # 编辑器误报
import time
import json


def sinaname(pages, user_id, Return):
    i = 0
    n = 1
    flag = True
    q = Queue.Queue(size=100000)

    while i < pages and flag == True:
        i += 1
        # print("正在提取第{}页".format(i+1))
        # url_next = "https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_3261134763&type=all&since_id=" + str(i)
        url_next = "https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_" + str(user_id) + "&type=all&since_id=" + str(i)
        html = requests.get(url_next)
        json_response = html.content.decode()
        # print(type(json_response))
        dict_json = json.loads(json_response)
        # print(type(dict_json))
        if dict_json['ok'] == 0:
            # print("当前页为空")
            break
        # print(dict_json.keys())
        # print(dict_json['data'].keys())
        # print(type(dict_json['data']['cards']))
        for item in dict_json['data']['cards']:
            # print(item)
            # print(type(item))
            # print(item.keys())
            # print(item['card_group'])
            try:
                for item1 in item['card_group']:
                    # print(type(item1))
                    # print(item1.keys())
                    # print(item1['user'])
                    # print(str(n) + " ", end = "")
                    # print(str(user_id) + " " + str(item1['user']['id']))
                    # n += 1
                    if item1['user']['followers_count'] >= 100000:
                        continue
                    else:
                        print(item1['user']['id'])
                        q.enqueue(str(item1['user']['id']))
            except Exception as key_err:
                print(key_err)
                continue
                # sinaname(1000, item1['user']['id'])
            # print(type(item['card_type']))
        # time.sleep(1)
    print("当前用户" + str(user_id))
    # q.show_queue()
    print("...")
    write_to_file(user_id, q)
    if Return == 1:
        return q
    else:
        q.queue_clear()


def write_to_file(user_id, _queue):
    _path = "D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/fans/"
    if not os.path.exists(_path):
        os.makedirs(_path)
    file = open(_path + str(user_id) + ".txt", 'a')
    for ele in _queue.queue:
        file.write(ele+"\n")
    file.close()


if __name__ == '__main__':
    # sinaname(1000, 1790528423, 0)
    Q = Queue.Queue(100000)
    Q = sinaname(100000, 2271848313, 1)
    print("assafasdfasdf")
    # Q = sinaname(100000, 6524941020, 1)
    while Q.is_empty() == False:
        Q.show_queue()
        temp_ele = Q.dequeue()
        # print(temp_ele)
        sinaname(100000, temp_ele, -1)
