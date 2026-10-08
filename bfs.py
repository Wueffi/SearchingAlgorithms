from collections import deque
import pygame

from utils import getNodeNames, getConnections, getConnectionMap
from graphics import drawNode, drawBoard, show, drawConnection, drawNodes

node_names = getNodeNames()
connections = getConnections()

color = 0x66BBFF
line_color = 0x0066FF
path_color = 0xFFFFFF

starting_node = node_names["Sassnitz"]
target_node = node_names["Loerrach"]

drawBoard()
drawNode(starting_node, color, 25)
drawNode(target_node, color, 25)
show()

queue = deque([starting_node])
visited = {starting_node}
parent = {}

while queue:
    current = queue.popleft()

    if current == target_node:
        break

    for connection in connections:
        if connection.getNode1() == current:
            neighbor = connection.getNode2()
        elif connection.getNode2() == current:
            neighbor = connection.getNode1()
        else:
            continue

        if neighbor not in visited:
            visited.add(neighbor)
            parent[neighbor] = current
            queue.append(neighbor)

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