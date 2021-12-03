# Imports

import matplotlib.pyplot as plt
import csv


# Graph Class
class Graphs:
    def __init__(self):
        self.data_file = "./files/data.csv"

    def get_graph_values(self):
        x = []
        y = []

        with open(self.data_file, 'r') as data:
            plots = csv.reader(data, delimiter=',')

            for row in plots:
                if "Price" in row:
                    continue
                x.append(row[1])
                y.append(float(row[2]))

        return x, y
