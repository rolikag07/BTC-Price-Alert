import requests
import json


# Class Telegram
class Telegram:
    def __init__(self):
        self.API = "https://api.telegram.org/bot" + "5089058278:AAEBvK84SjcR47CDl763tkYes1DNi3ccvSo" + "/sendMessage"

    def send_telegram_message(self, message):
        data = {
            "chat_id": "-1001761530166",
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
