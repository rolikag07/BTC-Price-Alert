# Imports


# API Class
class API:
    def __init__(self):
        self.data = None

    def fetch_data(self):
        pass

    def share_data(self):
        print(self.data)


# Main
if __name__ == "__main__":
    api = API()
    api.fetch_data()
    api.share_data()
