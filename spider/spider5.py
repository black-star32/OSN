# 爬取语料库
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
        time.sleep(0.1)
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
                if item['card_type'] == 9 :
                    str_temp = item['mblog']['text']
                    # print(str_temp)
                    if str_temp == None:
                        continue
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
    _path = "/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/weibo_fenlei1/{user_id}.txt".format(user_id=str(user_id))
    # if not os.path.exists(_path):
    #     os.makedirs(_path)
    with open(_path, 'w') as file:
        for ele in _list:
            file.write(ele.encode('GBK','ignore').decode('GBk') + "\n")


if __name__ == '__main__':
    with open("fenlei.txt", "r") as file1:
        lines1 = file1.readlines()
        for line1 in lines1:
            if os.path.exists("D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/weibo_fenlei1/" + line1[:-1] + '.txt'):
                print("D:/pycharm/PyCharm 2017.2.3/Project/APT&OSN/data/weibo_fenlei1/" + line1[:-1] + '.txt')
                continue
            else:
                sinaname(10000, line1[:-1])