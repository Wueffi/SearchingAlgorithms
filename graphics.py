import pygame
from utils import getNodes, getConnections

pygame.init()

scale = 4

screen = pygame.display.set_mode((600, 800))

big = pygame.Surface((2400, 3200))
big.fill(0x111111)

connections = getConnections()
nodes = getNodes()

def drawNode(node, color, radius):
    x = round(node.getX())
    y = round(node.getY())
    pygame.draw.circle(big, 0xFFFFFF, (x, y), radius)
    pygame.draw.circle(big, color, (x, y), radius - 5)

def drawConnection(connection, color):
    p1 = (round(connection.node1.getX()), round(connection.node1.getY()))
    p2 = (round(connection.node2.getX()), round(connection.node2.getY()))
    pygame.draw.line(big, color, p1, p2, 8)

def drawBoard():
    for connection in connections:
        drawConnection(connection, 0x676767)
    drawNodes()
    drawGermany()

def drawNodes():
    for node in nodes:
        drawNode(node, 0x676767, 15)

def drawGermany():
    pass

def show():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    frame = pygame.transform.smoothscale(big, (600, 800))
    screen.blit(frame, (0, 0))
    pygame.display.flip()