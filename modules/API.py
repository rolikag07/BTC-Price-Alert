# Imports
import json
from datetime import datetime, date
from time import time, sleep
import requests
import csv
from threading import Thread
from modules.Telegram import Telegram


class API:
    def __init__(self, runtime):
        self.runtime = runtime
        self.data = None
        self.time = None
        self.date = None
        self.bot = Telegram()
        self.init_csv()
        print("Object Initialized")

    def fetch_data(self):
        url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,INR"
        response = requests.request("GET", url)
        response = json.loads(response.text)
        current_price = response["INR"]
        # Step 1
        if current_price <= 200000:
            message = " The BitCoin rate has fallen to " + str(
                current_price) + ". Kindly invest accordingly."
            telegram_status = self.bot.send_telegram_message(message)
            print("This is the Telegram status:", telegram_status)

        # Step 2
        if current_price >= 450000:
            print("Alert! BitCoin rate is rising")
            message = "The BitCoin rate has risen to" + str(current_price) + " Kindly invest accordingly. "
            telegram_status = self.bot.send_telegram_message(message)
            print("This is the Telegram status:", telegram_status)

        self.data = current_price
        self.date = date.today()
        self.time = datetime.now().strftime("%H:%M:%S")
        self.save_data()

    # Init  CSV
    def init_csv(self):
        with open(".\\files\\data.csv", mode='a+', newline='') as _csv_file:
            if not self.check_csv_header():
                headers = ["Date", "Time", "Price"]
                writer = csv.writer(_csv_file)
                writer.writerow(headers)

    # Check CSV Headers
    def check_csv_header(self):
        with open(".\\files\\data.csv", mode='r') as _csv_file:
            csv_reader = csv.reader(_csv_file, delimiter=',')
            headers = next(csv_reader, None)

            if headers is None:
                return False
            elif headers[0] == "Date" and headers[1] == "Time" and headers[2] == "Price":
                return True

    # Save Data to CSV
    def save_data(self):
        with open(".\\files\\data.csv", mode='a+', newline='') as _csv_file:
            writer = csv.writer(_csv_file)
            print("Saving Data at time:", self.time)
            writer.writerow([self.date, self.time, self.data])

    def run(self):
        print("Process Started")
        start_time = time()
        while time() - start_time <= self.runtime:
            self.fetch_data()
            sleep(60)


# # Main
# if __name__ == "__main__":
#     runtime = 300  # Runtime in 300 seconds = 5 minutes
#     api = API(runtime=runtime)
#
#     t = Thread(target=api.run())
#
#     t.daemon = True
#
#     t.start()
#
#     print("Process Completed.")
