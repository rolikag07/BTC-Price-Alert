import requests
import json


# Class Telegram
class Telegram:
    def __init__(self):
        self.API = "https://api.telegram.org/bot" + "XXXXXxxxxxxxxxxx" + "/sendMessage"

    def send_telegram_message(self, message):
        data = {
            "chat_id": "-10017xxxx45",
            "text": message
        }
        try:
            response = requests.request(
                "POST",
                self.API,
                params=data
            )

            print(response.text)
            telegram_data = json.loads(response.text)
            return telegram_data["OK"]
        except Exception as e:
            print("An error occurred in sending the alert message via Telegram")
            print(e)
            return False
