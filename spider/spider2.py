# 爬取用户关注列表

import requests
import os
# import Queue
import time
import json


def sinaname(pages, user_id):
    i = 0
    n = 0
    flag = True
    _list = []
    print("当前用户：" + user_id)
    while i < pages and flag == True:
        i += 1
        # url_next = "https://m.weibo.cn/api/container/getSecond?containerid=100505" + str(user_id) + "_-_FOLLOWERS&page=" + str(i)
        url_next = "https://m.weibo.cn/api/container/getSecond?containerid=100505{user_id}_-_FOLLOWERS" \
                   "&page={page}".format(user_id=str(user_id), page=str(i))
        html = requests.get(url_next)
        json_response = html.content.decode()
        try:
            dict_json = json.loads(json_response)
        except Exception as json_decode_error:
            print(json_decode_error)
            continue
        if dict_json['ok'] == 0:
            print("当前页为空")
            break
        try:
            for item in dict_json['data']['cards']:
                if item['user']['follow_count'] >= 10000:
                    return
                else:
                    # print(item['user']['id'])
                    _list.append(str(item['user']['id']))
        except Exception as key_error:
            print(key_error)
            continue
        # time.sleep(1)
    print("write..." + str(user_id))
    write_to_file(user_id, _list)
    # if Return == 1:
    #     return q
    # else:
    #     q.queue_clear()


def write_to_file(user_id, _list):
    _path = "D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/follows/{user_id}.txt".format(user_id=str(user_id))
    # if not os.path.exists(_path):
    #     os.makedirs(_path)
    # file = open(_path + str(user_id) + ".txt", 'w')
    # for ele in _queue.queue:
    #     file.write(ele+"\n")
    # file.close()
    with open(_path, 'w') as file:
        for ele in _list:
            file.write(ele + "\n")


if __name__ == '__main__':
    file = open("2271848313.txt")
    lines = file.readlines()
    count = 1
    for line in lines:
        if os.path.exists("D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/follows/" + line[:-1] + ".txt"):
            print(str(count) + "D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/follows/" + line[:-1] + ".txt")
            count += 1
            continue
        sinaname(10000, line[:-1])
