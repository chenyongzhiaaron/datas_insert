import re

import requests
import urllib3


class DoHttp(object):
    @staticmethod
    def do_http(r_host, r_method, r_url, r_params=None, r_header=None):
        """

        Args:
            r_host: 请求域名
            r_method: 请求方法 get post
            r_url: 请求地址
            r_params: 请求参数
            r_header: 请求头部信息

        Returns: 请求结果对象

        """
        # 关闭 https 警告信息
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        if re.search("(https://.*?)", r_url) or re.search("(http://.*?)", r_url):
            do_url = r_url
        else:
            do_url = r_host + r_url

        if "post" == r_method.lower():
            print(do_url)
            res = requests.post(url=do_url, json=r_params, headers=r_header, verify=False)
        elif "get" == r_method.lower():
            res = requests.get(url=do_url, params=r_params, headers=r_header, verify=False)
        else:
            res = None
        return res


if __name__ == '__main__':
    # host = "https://restapi.amap.com"
    # url = "/v3/geocode/geo?parameters"
    # method = "get"
    # parameters = {"key": "4390d4ccaa8df203783e767136960921", "address": "河源市紫金县丽景嘉园"}
    host = "https://mdxz.kt1.pagoda.com.cn"
    url = "/api/token?phone=13162583810&source=pm"
    method = "post"
    header = {"Content-Type": "application/json"}
    test = DoHttp().do_http(host, method, url, r_header=header)
    print(test.json())
