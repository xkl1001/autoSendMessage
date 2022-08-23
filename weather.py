import requests


class Weather(object):

    def __init__(self) -> None:
        """
        构造函数
        """
        pass

    def main(self) -> dict:
        wea_url = 'http://apis.juhe.cn/simpleWeather/query'
        param_dict = {"city": "新田", "key": "9a51e00811f97ed22e1672cd4d286cf1"}

        re = requests.get(wea_url, param_dict)
        re.encoding = 'utf-8'
        print(re.json())
        res = re.json()
        city = res["result"]["city"]
        info = res["result"]["realtime"]["info"]
        temperature = res["result"]["realtime"]["temperature"]

        weather = {"city": city, "info": info, "temperature": temperature}

        return weather
