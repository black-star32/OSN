# 爬取用户的关注列表

import requests
import os
import time
import json


def sinaname(pages, user_id):
    i = 0
    n = 0
    flag = True
    _list = []
    print("当前用户："+user_id)
    while i < pages and flag == True:
        i += 1
        # url_next = "https://m.weibo.cn/api/container/getSecond?containerid=100505" + str(user_id) + "_-_FOLLOWERS&page=" + str(i)
        url_next = "https://m.weibo.cn/api/container/getSecond?containerid=100505{user_id}_-_FOLLOWERS" \
                   "&page={page}".format(user_id=str(user_id),page=str(i))
        # cookies = {"Cookie": "_T_WM=7d5879d8fd056520abbc051a69acdcdb; "
        #             "SCF=Aqgi2hOh0oD5JFM0xCyI5S_LEeg3WLs-fF8uGYhtt1F5BHpf9lBVQVGj_GCWxmAuNn90uqpTeat-i-lSKRTRZZc.; "
        #             "WEIBOCN_FROM=1110006030; "
        #             "M_WEIBOCN_PARAMS=luicode%3D20000173%26fid%3D102803_ctg1_8999_-_ctg1_8999_home%26uicode%3D10000011; "
        #             "SUB=_2A253xeK1DeRhGeVM7lYX8ybNzD-IHXVVSY79rDV6PUJbkdAKLXHdkW1NTGxXSUMp7ZePpDYugaLwF1GieESeFktF; "
        #             "SUHB=0U15w-7GQDkBk7; "
        #             "SSOLoginState=1522635493"}
        # html = requests.get(url_next, headers=cookies)
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
        if dict_json['data']['count']>400:
            print(dict_json['data']['count'])
            return
        try:
            for item in dict_json['data']['cards']:
                _list.append(str(item['user']['id']))
        except Exception as key_error:
            print(key_error)
            continue
        time.sleep(0.1)
        # time.sleep(1)
    if len(_list) == 0:
        return
    print("write..." + str(user_id))
    write_to_file(user_id, _list)
    return
    # if Return == 1:
    #     return q
    # else:
    #     q.queue_clear()


def write_to_file(user_id, _list):
    _path = "D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/follows" \
            "/follows/{user_id}.txt".format(user_id=str(user_id))
    print(_path)
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
    with open("2271848313.txt") as file1:
        lines1 = file1.readlines()
        for line1 in lines1:
            print("***************************************************"+str(line1))
            if os.path.exists("D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN"
                              "/data/follows/{}.txt".format(line1[:-1])):
                print("D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/"
                      "follows/{}.txt".format(line1[:-1]))
                with open("D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN"
                              "/data/follows/{}.txt".format(line1[:-1]), 'r') as file2:
                    lines2 = file2.readlines()
                    if len(lines2) > 400:
                        continue
                    for line2 in lines2:
                        if os.path.exists("D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN"
                                          "/data/follows/follows/{}.txt".format(line2[:-1])):
                            print("pass")
                            continue
                        else:
                            sinaname(10000, line2[:-1])
            else:
                continue
