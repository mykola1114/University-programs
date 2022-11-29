import turtle

class L_System:
    def __init__(self, t, axiom, angle, width, length):
        self.axiom = axiom
        self.state = axiom
        self.width = width
        self.length = length
        self.angle = angle
        self.t = t
        self.rules = {}
        self.t.pensize(self.width)

    def add_rules(self, *rules):
        for key, value in rules:
            self.rules[key] = value

    def generate_path(self, n_iter):
        for n in range(n_iter):
            for key, value in self.rules.items():
                self.state = self.state.replace(key, value.lower())

            self.state = self.state.upper()

    def draw_turtle(self, start_pos, start_angle):
        self.t.up()
        self.t.setpos(start_pos)
        self.t.seth(start_angle)
        self.t.down()

        for move in self.state:
            if move == 'F':
                self.t.forward(self.length)
            elif move == 'S':
                self.t.up()
                self.t.forward(self.length)
                self.t.down()
            elif move == '+':
                self.t.left(self.angle)
            elif move == '-':
                self.t.right(self.angle)

        turtle.done()



if __name__ == '__main__':
    width = 1200
    height = 600
    screen = turtle.Screen()
    screen.setup(width, height, 0, 0)

    t = turtle.Turtle()
    t.speed(0)

    # Реактивна швидкість черепахи
    turtle.tracer(1, 0)

    dragon_settings = {'angle': 90,
                       'axiom': "FX",
                       'rules': (("FX", "FX+FY+"), ("FY", "-FX-FY")),
                       'pen_width': 2,
                       'f_len': 5}

    sierpinski_settings = {'angle': 60,
                           'axiom': "FXF--FF--FF",
                           'rules': (("F", "FF"), ("X", "--FXF++FXF++FXF--")),
                           'pen_width': 2,
                           'f_len': 5}

    # Змінювати налаштування тут
    current_settings = sierpinski_settings # dragon_settings

    l_sys = L_System(t, current_settings['axiom'], current_settings['angle'], current_settings['pen_width'], current_settings['f_len'])
    l_sys.add_rules(current_settings['rules'][0], current_settings['rules'][1])
    l_sys.generate_path(5) # 11
    l_sys.draw_turtle((0, 0), 0)
