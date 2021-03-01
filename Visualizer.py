import random

import matplotlib.pyplot as plt
import networkx as nx


class Visualizer:

    def draw(self, input):
        g = nx.DiGraph()

        for car in random.sample(input.cars, 2): # pick a random sample of edges to limit the number displayed
            lastNode = car.route[0]
            color = random.choice("rgb")
            for node in car.route[1:]:
                g.add_edge(lastNode, node, color=color)
                lastNode = node

        # for name, street in random.sample(input.streets.items(), 100): # pick a random sample of edges to limit the number displayed
        #     g.add_edge(street.startNode, street.endNode, name=street.name)

        # plt.figure(1, figsize=(200, 200))
        colors = [g[u][v]['color'] for u,v in g.edges]
        pos = nx.spring_layout(g, k=0.75, iterations=200)
        nx.draw_networkx(g, pos, edge_color=colors, node_size=10, width=0.2, with_labels=False)
        plt.show()
