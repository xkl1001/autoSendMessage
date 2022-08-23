import requests


class OneSpeak(object):

    def main(self) -> str:
        wea_url = 'https://apis.juhe.cn/fapig/soup/query'
        param_dict = {"key": "14b2cfa8340a62efabd15554f40e6992"}

        re = requests.get(wea_url, param_dict)
        re.encoding = 'utf-8'
        res = re.json()
        oneSpeak = res["result"]["text"]

        return oneSpeak
