import weather
from send_message import SendMessage
import oneSpeak


class Main(object):

    def __init__(self) -> None:
        """
        构造函数
        """
        pass

    def main(self) -> None:

        weath = weather.Weather.main(self)
        onespeaks = oneSpeak.OneSpeak.main(self)



        with open("currtime.txt", 'r', encoding='utf8') as fr:
            currtimes = fr.read()

        with open("currtime.txt", 'w') as fw:
            currtime = int(currtimes) + 1
            fw.write(str(currtime))

        city = weath["city"]
        info = weath["info"]
        temperature = weath["temperature"]

        if int(temperature) < 25:
            attention = "请注意多穿衣服哦！"
        else:
            attention = "请注意防晒哦！！"

        # 实例SendMessage
        sm = SendMessage()
        # 获取接口返回数据
        json_data = {"name": "小何", "front": "早上好！(ฅ∀<`๑)♡ 请查收今天天气，注意穿衣哦！(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ", "city": city, "info": info, "temperature": temperature, "attention": attention, "currtime": currtimes, "onespeak": onespeaks}
        # 发送消息
        sm.send_message(json_data=json_data)


if __name__ == '__main__':
    main = Main()
    main.main()
