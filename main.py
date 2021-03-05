import numpy as np
import math
import time
import pygame

radius = 1000
smallRadius = 300

pygame.init()
screen = pygame.display.set_mode([800, 800])

while True:
    for rot in range(0, 360, 1):
        screen.fill((0, 0, 0))

        angle = math.radians(rot)
        rotateX = np.array([[1, 0, 0], [0, math.cos(angle), -1 * math.sin(angle)], [0, math.sin(angle), math.cos(angle)]])
        rotateY = np.array([[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-1 * math.sin(angle), 0, math.cos(angle)]])
        rotateZ = np.array([[math.cos(angle), -1 * math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]])



        for alpha in range(0, 360, 5):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)

            radians = math.radians(alpha)
            x = round(radius * math.cos(radians))
            y = round(radius * math.sin(radians))
            z = 0

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

                position = rotateY.dot(position)
                position = rotateX.dot(position)
                x1 = position[0]
                y1 = position[1]
                z1 = position[2] + 500

                xx = 0.3 * z1 * x1/z1 + 400
                yy = 0.3 * z1 * y1/z1 + 400

                cc = 150 + z1/2 - 250
                print(cc)
                if cc > 255:
                    cc = 255
                if cc < 30:
                    cc = 30

                color = (cc, cc, cc)
                pygame.draw.circle(screen, color, (xx, yy), 2)


        pygame.display.flip()
        # time.sleep(0.01)

pygame.quit()


