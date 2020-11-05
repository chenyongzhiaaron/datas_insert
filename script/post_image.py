'''
Author: kira
Date: 2020-10-12 12:30:48
LastEditTime: 2020-10-12 23:15:41
LastEditors: kira
Description:
FilePath: \datas_project\script\post_image.py
神马都是浮云，没 BUG 才是王道
'''
import json

from qiniu import put_file

token = "KvTee7Itlh16MzvMxP5ETVA_7QTpRZSMd5E55lwU:CdSgRDjMHjH0GlBU1r58DSarFbU" \
        "=:eyJzY29wZSI6InNtYXJ0LWxvY2F0aW9uIiwiZGVhZGxpbmUiOjE2MDI1NjU0OTJ9 "
with open("../东莞百果园成熟商圈明细表(（2020.7） -.docx.filecontent/word/imageMap.json", 'r', encoding='utf-8') as json_file:
    image_path = json.load(json_file)
    print(image_path)
    print(type(image_path))

key = '河源市紫金县丽景嘉园-商圈外景图'
localfile = '..\image\图片1.png'
ret, info = put_file(token, key, localfile)
print(info, "--------", ret)
remote_url = "https://cdn2.mdxz.pagoda.com.cn/" + ret["key"]
print(remote_url)
