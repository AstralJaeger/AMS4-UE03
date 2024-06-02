import os

import networkx as nx
from IPython.core.display import Image
from networkx.drawing.nx_agraph import to_agraph

basepath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'images'))
if not os.path.exists(basepath):
    os.makedirs(basepath)


def plot_and_save(graph: nx.Graph, filename):
    a = to_agraph(graph)
    image_path = os.path.join(basepath, filename)
    a.draw(image_path, prog='dot', format='png')
    display(Image(os.path.join(basepath, 'images', filename)))


def prim():
    pass


def kruskal():
    pass