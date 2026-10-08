import heapq
import pygame

from utils import getNodeNames, getConnections, getConnectionMap
from graphics import drawNode, drawBoard, show, drawConnection, drawNodes

node_names = getNodeNames()
connections = getConnections()

color = 0x66BBFF
line_color = 0x0066FF
path_color = 0xFFFFFF

starting_node = node_names["Flensburg"]
target_node = node_names["Garmisch-Partenkirchen"]

drawBoard()
drawNode(starting_node, color, 25)
drawNode(target_node, color, 25)
show()

distances = {starting_node: 0}
parent = {}
queue = [(0, 0, starting_node)]
visited = set()
counter = 0

while queue:
    distance, _, current = heapq.heappop(queue)

    if current in visited:
        continue

    visited.add(current)

    if current == target_node:
        break

    for connection in connections:
        if connection.getNode1() == current:
            neighbor = connection.getNode2()
        elif connection.getNode2() == current:
            neighbor = connection.getNode1()
        else:
            continue

        new_distance = distance + connection.getWeight()

        if new_distance < distances.get(neighbor, float("inf")):
            distances[neighbor] = new_distance
            parent[neighbor] = current

            counter += 1
            heapq.heappush(queue, (new_distance, counter, neighbor))

            drawConnection(connection, line_color)
            drawNodes()
            drawNode(starting_node, color, 25)
            drawNode(target_node, color, 25)
            show()
            pygame.time.wait(20)

path = []
current = target_node

while current != starting_node:
    path.append(current)
    current = parent[current]

path.append(starting_node)
path.reverse()

for a, b in zip(path, path[1:]):
    drawConnection(getConnectionMap()[frozenset((a, b))], path_color)
    show()
    pygame.time.wait(100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    show()
    pygame.time.Clock().tick(60)