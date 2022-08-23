
import requests


class AccessToken(object):

    APPID = "wxb152514b1d92675e"

    APPSECRET = "da8aaf5b5721cd05a5b762b1d6a6a6d1"

    def __init__(self, app_id=APPID, app_secret=APPSECRET) -> None:
        self.app_id = app_id
        self.app_secret = app_secret

    def get_access_token(self) -> str:
        """
        获取access_token凭证
        :return: access_token
        """
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}"
        resp = requests.get(url)
        result = resp.json()
        if 'access_token' in result:
            return result["access_token"]
        else:
            print(result)
