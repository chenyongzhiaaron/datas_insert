# coding:utf-8

import jsonpath
import pymongo

from common.my_log import MyLog


class DoMongo(object):
    def do_mongo(self, sql, method=None):
        client = pymongo.MongoClient(host='193.112.176.56', port=9008)  # 获取链接实例
        db = client["smart_location"]
        if "select" == method:
            res = db["users"].find_one(sql)
        else:
            # 执行插入数据操作
            res = db["intentionshops"].insert_one(sql)
        return res


if __name__ == '__main__':
    sql_dates = {
        "_id": "5f8850f9cfb8751205580101",
        "name": "北京市丰台区泥洼地铁站",
        "realEstatePrice": 60000,
        "businessDistrictResidenceNumber": 2690,
        "rent": "450-550",
        "transferFee": "10-15",
        "corrivals": "果唯伊",
        "preelectionBusinessDistrict": "我爱我家，中国联通，链家",
        "assignorContactInformation": "链家任13240018281",
        "businissStatus": "丰台第一小学，西国贸大厦，十二中",
        "openPlanTime": 2020,
        "remark": "商圈好，店铺极少，租金高",
        "region": "北京",
        "extraPois": [{
            "latitude": "",
            "longitude": "",
            "location": {
                "longitude": "",
                "latitude": "",
                "formattedAddress": "",
                "addressComponent": {
                    "city": "",
                    "province": "",
                    "adcode": "",
                    "district": "",
                    "towncode": "",
                    "country": "",
                    "township": "",
                    "citycode": ""
                },
                "customAddress": ""
            },
            "scale": "1072",
            "name": "泥洼小区",
            "typeName": "小区",
            "typeUnit": "户"
        }, {
            "latitude": "39.858844",
            "longitude": "116.303218",
            "location": {
                "longitude": "116.303218",
                "latitude": "39.858844",
                "formattedAddress": "北京市丰台区盛鑫嘉园",
                "addressComponent": {
                    "city": "北京市",
                    "province": "北京市",
                    "adcode": "110106",
                    "district": "",
                    "towncode": "",
                    "country": "中国",
                    "township": "",
                    "citycode": "010"
                },
                "customAddress": "北京市丰台区盛鑫嘉园"
            },
            "scale": "902",
            "name": "盛鑫嘉园",
            "typeName": "小区",
            "typeUnit": "户"
        }, {
            "latitude": "39.858392",
            "longitude": "116.301075",
            "location": {
                "longitude": "116.301075",
                "latitude": "39.858392",
                "formattedAddress": "北京市丰台区东瑞丽景",
                "addressComponent": {
                    "city": "北京市",
                    "province": "北京市",
                    "adcode": "110106",
                    "district": "",
                    "towncode": "",
                    "country": "中国",
                    "township": "",
                    "citycode": "010"
                },
                "customAddress": "北京市丰台区东瑞丽景"
            },
            "scale": "276",
            "name": "丰管路甲25号院440.东瑞丽景",
            "typeName": "小区",
            "typeUnit": "户"
        }],
        "businessDistrictPlanImage": {},
        "streetscapeImage": {},
        "address": {
            "longitude": "116.304173",
            "latitude": "39.858609",
            "formattedAddress": "北京市丰台区泥洼地铁站",
            "addressComponent": {
                "city": "北京市",
                "province": "北京市",
                "adcode": "110106",
                "district": "丰台区",
                "towncode": "",
                "streetNumber": {},
                "country": "中国",
                "businessAreas": [],
                "building": {},
                "neighborhood": {},
                "citycode": "010"
            },
            "customAddress": "北京市丰台区泥洼地铁站"
        },
        "city": "北京市",
        "userId": "5de78dbbe50acb18b812754c"
    }
    res = jsonpath.jsonpath(sql_dates, "$..latitude")
    print(res)
    print(len(res))
    result = []
    for i in res:
        if i == "":
            result.append("False")
        else:
            result.append("True")
    if "False" in result:
        MyLog().my_log("序号 = {0} 的数据需要重新确认地理位置，名称：{1}".format(sql_dates["name"], sql_dates["_id"]), "ERROR",
                       "error")
        print(result)
    else:
        print("OK")
