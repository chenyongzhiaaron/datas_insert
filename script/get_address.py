
import sys
import json
sys.path.append("./")
sys.path.append("./common")
from jsonpath import jsonpath
from common.do_http import DoHttp

host = "https://restapi.amap.com"
url = "/v3/geocode/geo?parameters"
method = "get"
parameters = {"key":"4390d4ccaa8df203783e767136960921","address":"绿地中心玉玺","city":"成都市"}

res = DoHttp().do_http(host,method, url, parameters).json()
print(json.dumps(res,ensure_ascii=False))
geocodes = jsonpath(res,"$..geocodes")
# if len(geocodes):
#     print(len(geocodes))
# location = jsonpath(res, "$..location")[0].split(",")[0]
# print(location)