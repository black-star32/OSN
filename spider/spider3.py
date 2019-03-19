# 爬取用户2018-01-01到2018-05-14时间段内的所有微博

import os
import requests
import time
import json


def sinaname(pages, user_id):
    i = 0
    flag = True
    _list = []
    print("当前用户："+user_id)
    while i < pages and flag == True:
        i += 1
        print("正在提取第{}页".format(i+1))
        url_next = "https://m.weibo.cn/api/container/getIndex?type=uid&value=" \
                   "{user_id_1}&containerid=107603{user_id_2}&page={_page}".format(
            user_id_1=str(user_id),
            user_id_2=str(user_id),
            _page=str(i)
        )
        html = requests.get(url_next)
        json_response = html.content.decode()
        # print(type(json_response))
        try:
            dict_json = json.loads(json_response)
        except Exception as json_decode_error:
            print(json_decode_error)
            continue
        if dict_json['ok'] == 0:
            print("当前页为空")
            break
        #
        # print(dict_json.keys())
        # print(dict_json['data'].keys())
        # print(dict_json['data']['cards'])
        try:
            for item in dict_json['data']['cards']:
                # print(item)
                # print(type(item))
                # print(item.keys())
                # print(item['card_type'])
                # print(type(item['card_type']))

                # 微博正文页"scheme"
                # if item['card_type'] == 9:
                #     print(item['scheme'])
                if item['card_type'] == 9 and item['mblog']['created_at'] > '01-01' \
                        and item['mblog']['created_at'] < '05-14':
                    # # print(item['mblog'])
                    # #微博对应的某个唯一值，每条不同，用来爬取评论
                    # print(item['itemid'][-16:] + "  ", end="")
                    # #发送微博时间
                    # print(item['mblog']['created_at'] + "  ", end="")
                    # #微博内容
                    # print(item['mblog']['text']+ "  ", end="")
                    # #微博正文页链接
                    # print(item['scheme'])
                    str_temp = "{itemid} {mblog_created_at} {mblog_text} {scheme}".format(
                        itemid=item['itemid'][-16:],
                        mblog_created_at=item['mblog']['created_at'],
                        mblog_text=item['mblog']['text'],
                        scheme=item['scheme'])
                    _list.append(str_temp)
                elif item['card_type'] == 11:
                    continue
                else:
                    flag = False
                    break
        except Exception as key_error:
            print(key_error)
            continue
        # time.sleep(1)
    if len(_list) == 0:
        return
    # print(_list)
    write_to_file(user_id, _list)


def write_to_file(user_id, _list):
    _path = "D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/weibo1/{user_id}.txt".format(user_id=str(user_id))
    # if not os.path.exists(_path):
    #     os.makedirs(_path)
    with open(_path, 'w') as file:
        for ele in _list:
            file.write(ele.encode('GBK','ignore').decode('GBk') + "\n")


if __name__ == '__main__':
    _path = "D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/weibo1/"
    if not os.path.exists(_path):
        os.makedirs(_path)
    with open("2271848313.txt", "r") as file:
        lines = file.readlines()
        count = 1
        for line in lines:
            if os.path.exists("D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/weibo1/" + line[:-1] + '.txt'):
                print(str(count) + "D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/weibo1/" + line[:-1] + '.txt')
                count += 1
                continue
            sinaname(10000, line[:-1])