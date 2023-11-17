import turtle
from tkinter import messagebox

from config_a import *
##from config_b import *
##from config_c import *
##from config_d import *
##from config_e import *
##from config_f import *
##from config_algae import *
##from config_bush import *
##from config_bush_2 import *
##from config_weed import *


# F = move forward
# + = clockwise
# - = counterclockwise


class LSystemGenerator:
    def __init__(self, iterations):
        self.axiom_generator = self.generate_rules(axiom)
        self.angle = angle
        self.distance = distance
        self.leaf = 1
        self.branch = 1
        self.iterations = iterations

    def generate_rules(self, current_val):
        for _ in range(self.iterations):
            next_val = ""
            for char in current_val:
                if char in rules:
                    # index into rule
                    next_val += rules[char]
                else:
                    # carry over into next gen without change
                    next_val += char
            current_val = next_val
            yield current_val

    def draw_result(self, next_val):
        # makes turtle not visible while drawing
        turtle.hideturtle()
        stack = []
        saved_state = (turtle.position(), turtle.heading())
        turtle.width(self.branch)
        for char in next_val:
            if char == 'F':
                turtle.forward(self.distance)
            elif char == '+':
                turtle.left(self.angle)
            elif char == '-':
                turtle.right(self.angle)
            elif char == "[":
                stack.append((turtle.position(), turtle.heading()))
            elif char == "]":
                # draw leaf
                turtle.width(1)
                turtle.color("green")
                turtle.begin_fill()
                turtle.fillcolor("green")
                turtle.circle(self.leaf, 70)
                turtle.left(110)
                turtle.circle(self.leaf, 70)
                turtle.end_fill()
                turtle.penup()
                # reset for branch
                turtle.pencolor('brown')
                turtle.width(self.branch)
                position_select, heading_select = stack.pop()
                turtle.goto(position_select)
                turtle.setheading(heading_select)
                turtle.pendown()
        turtle.penup()
        turtle.goto(saved_state[0])
        turtle.setheading(saved_state[1])
        turtle.pendown()

    def on_click(self, x, y):
        # binds result with click
        try:
            axiom = next(self.axiom_generator) # get next iteration
            turtle.clear()
            self.draw_result(axiom)
            print(axiom)
        except StopIteration:
            print("Done")


    def increase_angle(self):
        self.angle += 10
        print(f"The angle is increased by 10 and is now: {self.angle}")

    def decrease_angle(self):
        self.angle -= 10
        print(f"The angle is decreased by 0.5 and is now: {self.angle}")

    def increase_distance(self):
        self.distance += 0.5
        print(f"The distance is increased by 0.5 and is now: {self.distance}")

    def decrease_distance(self):
        self.distance -= 0.5
        print(f"The distance is decreased by 10 and is now: {self.distance}")

    def resize_canvas(self):
        try:
            width = turtle.numinput("Resize Canvas", "Enter Width: ", default=800)
            height = turtle.numinput("Resize Canvas", "Enter Height: ", default=600)
            turtle.setup(width=width, height=height)
            turtle.listen() 
        except:
            print("Operation cancelled or invalid")

    def clear_reset(self):
        turtle.clear()
        self.axiom_generator = self.generate_rules(axiom)
        print("reset")

    def increase_leaf(self):
        self.leaf += 1
        print(f"The leaf size increased by 1 and is now: {self.leaf}")

    def decrease_leaf(self):
        if self.leaf > 1:
            self.leaf -= 1
            print(f"The leaf size decreased by 1 and is now: {self.leaf}")

    def increase_branch(self):
        self.branch += 1
        print(f"The branch size increased by 1 and is now: {self.branch}")

    def decrease_branch(self):
        if self.branch > 1:
            self.branch -= 1
            print(f"The branch size decreased by 1 and is now: {self.branch}")

    def how_to_use(self):
        instructions = """
        Instructions:
        - Click to generate the next iteration.
          > Once it has reached iteration count it will stop.
        - Press Right arrow to increase angle by 10.
        - Press Left arrow to decrease angle by 10.
        - Press Up to increase distance by 0.5.
        - Press Down to decrease distance by 0.5.
        - Press r key to resize the canvas.
        - Press c key to clear and reset generation.
        - Press i key to change iteration count.
        - Press w key to increase leaf size.
        - Press s key to decrease leaf size.
        - Press a key to increase branch size.
        - Press d key to decrease branch size.
    
        Click OK to close.
        """
        messagebox.showinfo("Instructions", instructions)

    def iteration_count(self):
        try:
            new_iterations = turtle.numinput("Iteration Count", "Enter number of iterations (this will reset the drawing): ", default=self.iterations)
            self.iterations = int(new_iterations)
            print(f"New Iteration count: {self.iterations}")
            turtle.listen() 
            self.clear_reset()
        except:
            print("Operation cancelled or invalid")

    def main(self):
        turtle.setup(width=800, height=600)
        turtle.title("L System Generator")
        turtle.tracer(False)
        print("Press h for help")
        turtle.penup()
        turtle.pencolor('brown')
        turtle.goto(0, -250)
        turtle.setheading(90)
        turtle.pendown()
        turtle.onscreenclick(self.on_click)
        turtle.listen()
        turtle.onkey(lambda: self.increase_angle(), 'Right')
        turtle.onkey(lambda: self.decrease_angle(), 'Left')
        turtle.onkey(lambda: self.increase_distance(), 'Up')
        turtle.onkey(lambda: self.decrease_distance(), 'Down')
        turtle.onkey(lambda: self.resize_canvas(), 'r')
        turtle.onkey(lambda: self.clear_reset(), 'c')
        turtle.onkey(lambda: self.iteration_count(), 'i')
        turtle.onkey(lambda: self.how_to_use(), 'h')
        turtle.onkey(lambda: self.increase_leaf(), 'w')
        turtle.onkey(lambda: self.decrease_leaf(), 's')
        turtle.onkey(lambda: self.increase_branch(), 'd')
        turtle.onkey(lambda: self.decrease_branch(), 'a')
        turtle.mainloop()

if __name__ == "__main__":
    l_system_generator = LSystemGenerator(iterations)
    l_system_generator.main()

