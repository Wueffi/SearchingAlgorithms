import json


class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def getName(self):
        return self.name

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Connection:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.weight = pow(pow(abs(node1.getX() - node2.getX()), 2) + pow(abs(node1.getY() - node2.getY()), 2), 0.5)

    def getNode1(self):
        return self.node1

    def getNode2(self):
        return self.node2

    def getWeight(self):
        return self.weight


with open("nodes.json", "r") as file:
    node_data = json.load(file)

nodes = [Node(obj["name"], obj["x"], obj["y"]) for obj in node_data]
node_names = {node.getName(): node for node in nodes}

with open("connections.json", "r") as file:
    connection_data = json.load(file)

connections = [Connection(node_names[a], node_names[b]) for obj in connection_data for a, b in obj.items()]

connection_map = {}

for connection in connections:
    a = connection.getNode1()
    b = connection.getNode2()
    connection_map[frozenset((a, b))] = connection

def getNodes():
    return nodes

def getNodeNames():
    return node_names

def getConnections():
    return connections

def getConnectionMap():
    return connection_map