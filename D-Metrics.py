import random

import pygame as pg


class Point:
    def __init__(self, pos):
        self.x_ = pos[0]
        self.y_ = pos[1]
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def get_pos(self):
        return (self.x_, self.y_)

class Plot:
    #settings
    colorList4 = [(0,0,0),(255,0,0),(0,255,0),(0,0,255)]
    def __init__(self, scr_size):
        pg.init()
        self.is_run = False
        self.w_ = scr_size[0]
        self.h_ = scr_size[1]
        self.screen = pg.display.set_mode(list(scr_size))
        self.center = Point((scr_size[0]/2, scr_size[1]/2))
        self.onceFlag = False

    def compute(self, comm, p1, p2, color=(0,0,0)):
        if comm == 'D_1':
            self.makeD_1(p1, p2, color)
        elif comm == 'D_2':
            self.makeD_2(p1, p2, color)
            self.countD_2(p1, p2)
        elif comm == 'D_PIE':
            self.countD_PIE(p1, p2)
            self.makeD_PIE(p1, p2, color)
        else:
            raise Exception('Incorrect metric')

    def countD_2(self, p1, p2, text='D_2 metrics'):
        if not self.onceFlag:
            b = pow(p1.x_-p2.x_, 2) + pow(p1.y_-p2.y_, 2)
            d2 = pow(b, 0.5)
            print(f'{text}: {d2}')

    def countD_PIE(self, p1, p2, text='D_PIE metrics'):
        if not self.onceFlag:
            if p1.x_ == p2.x_:
                dpie = abs(p1.y_-p2.y_)
            else:
                dpie = abs(p1.x_ - p2.x_) + abs(p2.x_) + abs(p2.y_)
            print(f'{text}: {dpie}')

    def makeAxes(self):
        if not self.is_run:
            raise Exception('Plot is not active')

        pg.draw.line(self.screen, (0, 0, 0), (self.w_/2, 0), (self.w_/2, self.h_), 1)
        pg.draw.line(self.screen, (0, 0, 0), (0, self.h_/2), (self.w_, self.h_/2), 1)

    def show(self, metric='D_2'):
        self.is_run = True
        while self.is_run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_run = False
            # Your code here
            pg.display.set_caption(f'{metric} metric')
            self.screen.fill((255, 255, 255))

            self.makeAxes()
            self.makeAllP()

            for i in range(len(self.points)-1):
                for j in range(i+1, len(self.points)):
                    if type(metric) == str:
                        self.compute(metric, self.points[i], self.points[j])
                    elif type(metric) == list:
                        for k, x in enumerate(metric):
                            self.compute(x, self.points[i], self.points[j], Plot.colorList4[k])

            self.onceFlag = True
            pg.display.flip()
            # End here
        pg.quit()

    def setP(self, n):
        self.points = []
        for i in range(n):
            pos = (random.randint(0,500), random.randint(0,500))
            self.points.append(Point(pos))

    def makeAllP(self):
        for p in self.points:
            pg.draw.circle(self.screen, p.color, (p.x_, p.y_), 5)

    def makeD_2(self, p1, p2, color):
        if not self.is_run:
            raise Exception('Plot is not active')

        pg.draw.line(self.screen, color, (p1.x_, p1.y_), (p2.x_, p2.y_), 3)

    def makeD_1(self, p1, p2, color):
        if not self.is_run:
            raise Exception('Plot is not active')

        pg.draw.line(self.screen, color, (p1.x_, p1.y_), (p1.x_, p2.y_), 3)
        pg.draw.line(self.screen, color, (p1.x_, p2.y_), (p2.x_, p2.y_), 3)

    def makeD_PIE(self, p1, p2, color):
        if not self.is_run:
            raise Exception('Plot is not active')

        if p1.x_ == p2.x_:
            pg.draw.line(self.screen, color, (p1.x_, p1.y_), (p2.x_, p2.y_), 3)
        else:
            pg.draw.line(self.screen, color, (p1.x_, p1.y_), (p1.x_, self.center.y_), 3)
            pg.draw.line(self.screen, color, (p1.x_, self.center.y_), (p2.x_, self.center.y_), 3)
            pg.draw.line(self.screen, color, (p2.x_, self.center.y_), (p2.x_, p2.y_), 3)


if __name__ == '__main__':
    map1 = Plot((500, 500))
    map1.setP(3)
    map1.show('D_PIE')
    #map1.show(['D_2', 'D_PIE', 'D_1'])
    # D_1 D_2 D_PIE

