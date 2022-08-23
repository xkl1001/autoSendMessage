

import json
import requests
from access_token import AccessToken


class SendMessage(object):
    # 消息接收者
    TOUSER = 'o65BI6-J04_Ntu6DFbS4PgwSv9GU'
    # 消息模板id
    TEMPLATE_ID = 'bHmyv-ulY9rHYQ_qVCiXUNkvrYPaylm9ga4HerG78bA'
    # 点击跳转链接（可无）
    CLICK_URL = 'https://www.tinydinostudy.com'

    def __init__(self, touser=TOUSER, template_id=TEMPLATE_ID, click_url=CLICK_URL) -> None:
        """
        构造函数
        :param touser: 消息接收者
        :param template_id: 消息模板id
        :param click_url: 点击跳转链接（可无）
        """
        self.access_token = AccessToken().get_access_token()
        self.touser = touser
        self.template_id = template_id
        self.click_url = click_url

    def get_send_data(self, json_data) -> object:
        """
        获取发送消息data
        :param json_data: json数据对应模板
        :return: 发送的消息体
        """
        return {
            "touser": self.touser,
            "template_id": self.template_id,
            "url": self.click_url,
            "topcolor": "#FF0000",
            # json数据对应模板
            "data": {
                "name": {
                    "value": json_data["name"],
                    # 字体颜色
                    "color": "#FF0066"
                },
                "front": {
                    "value": json_data["front"],
                    # 字体颜色
                    "color": "#ff6699"
                },
                "city": {
                    "value": json_data["city"],
                    "color": "#33CCCC"
                },
                "info": {
                    "value": json_data["info"],
                    "color": "#F70909"
                },
                "temperature": {
                    "value": json_data["temperature"],
                    "color": "#33FF00"
                },
                "attention": {
                    "value": json_data["attention"],
                    "color": "#E61A42"
                },
                "currtime": {
                    "value": json_data["currtime"],
                    "color": "#E61A42"
                },
                "onespeak": {
                    "value": json_data["onespeak"],
                    "color": "#ff99cc"
                },
            }
        }

    def send_message(self, json_data) -> None:
        """
        发送消息
        :param json_data: json数据
        :return:
        """
        # 模板消息请求地址
        url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={self.access_token}"
        data = json.dumps(self.get_send_data(json_data))
        resp = requests.post(url, data=data)
        result = resp.json()
        if result["errcode"] == 0:
            print("消息发送成功")
        else:
            print(result)
