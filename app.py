import pygal
from flask import Flask, render_template
from threading import Thread
from modules.Graphs import Graphs
from modules.API import API

app = Flask(__name__)

# Global
graph = Graphs()
api = API(runtime=300)


@app.route('/')
def index():
    x, y = graph.get_graph_values()

    bar_chat = pygal.Bar()
    bar_chat.title = "Bitcoin Chart"
    bar_chat.x_labels = map(str, x)
    bar_chat.add(title="BitCoin", values=y)

    bar_chat_data = bar_chat.render_data_uri()

    return render_template('index.html', barchat_data=bar_chat_data)


def run_api():
    api.run()


def run_server():
    app.run()


if __name__ == '__main__':
    t1 = Thread(target=run_api())
    t2 = Thread(target=run_server())

    t1.daemon = True

    t1.start()
    t2.start()
