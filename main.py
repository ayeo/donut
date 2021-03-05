import numpy as np
import math
import time
import pygame

radius = 1000
smallRadius = 300

pygame.init()
screen = pygame.display.set_mode([800, 800])

# structure = np.empty((0,3))


large_circles = np.empty((0,18,3))
for alpha in range(0, 360, 10):
    radians = math.radians(alpha)
    x = round(radius * math.cos(radians))
    y = round(radius * math.sin(radians))
    z = 0

    small_circles = np.empty((0,3))
    for psi in range(0, 360, 20):

        radians = math.radians(psi)
        xs = round(smallRadius * math.sin(radians))
        ys = 0
        zs = round(smallRadius * math.cos(radians))

        angle = math.radians(alpha)
        rotateZZ = np.array([[math.cos(angle), -1 * math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]])
        position = [xs, ys, zs]
        position = rotateZZ.dot(position)
        position = position + np.array([x, y, z])
        small_circles = np.vstack((small_circles, position))

    large_circles = np.vstack((large_circles, [small_circles]))

o = 0
panes = np.empty((36*18,3,3))
for i in range(0, 36, 1):
    for j in range(0, 18, 1):
        p1 = large_circles[i][j]
        p2 = large_circles[i][j-1]
        p3 = large_circles[i-1][j]
        panes[o] = [p1, p2, p3]
        o += 1

while True:
    for rot in range(0, 360, 1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)

        screen.fill((0, 0, 0))

        angle = math.radians(rot)
        rotateX = np.array([[1, 0, 0], [0, math.cos(angle), -1 * math.sin(angle)], [0, math.sin(angle), math.cos(angle)]])
        rotateY = np.array([[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-1 * math.sin(angle), 0, math.cos(angle)]])
        rotateZ = np.array([[math.cos(angle), -1 * math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]])

        xxx = panes

        for structure in xxx:
            position = structure[0]
            position = rotateY.dot(position)
            position = rotateX.dot(position)
            x1 = position[0]
            y1 = position[1]
            z1 = position[2] + 500

            xx = 0.3 * z1 * x1/z1 + 400
            yy = 0.3 * z1 * y1/z1 + 400

            cc = 150 + z1/2 - 250
            # print(cc)
            if cc > 255:
                cc = 255
            if cc < 30:
                cc = 30

            color = (cc, cc, cc)
            pygame.draw.circle(screen, color, (xx, yy), 2)

        time.sleep(0.01)
        pygame.display.flip()

pygame.quit()


