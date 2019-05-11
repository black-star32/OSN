import requests
import json

# example_url = "https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_3261134763&type=all&since_id="
example_url = "https://m.weibo.cn/api/container/getSecond?containerid=1005052271848313_-_FOLLOWERS&page=1"
html = requests.get(example_url)
json_response = html.content.decode()
dict_json = json.loads(json_response)
print(dict_json)
print(json.dumps(dict_json, sort_keys=True, indent=2))

# if __name__ == '__main__':
#     example_url = "https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_3261134763&type=all&since_id="
#     html = requests.get(example_url)
#     json_response = html.content.decode()
#     # print(type(json_response))
#     print(json_response)
#     # print(type(json_response))
#     dict_json = json.loads(json_response)
#     print(type(dict_json))
#     print(json.dump(dict_json, sort_keys=True,))
#     # for key in dict_json:
#     #     print(key,dict_json[key])
#     # if dict_json['ok'] == 0:
#     #     print("当前页为空")


