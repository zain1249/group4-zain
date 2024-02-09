"""
    Group4_activity1
    Group Members: 1) Hafs Hyderali Shaikh -->> Did the functions setPos(turta, x, y), hexagon(turta, hexa_color, border_color),
                      square(turta, square_color, border_color), circle(turta, circle_color, border_color)
                   2) Monsef -->> Did the function pattern(turta, hexa_color, circle_color, square_color, border_color)
                   3) Zain -->> Did main()
    This Python script uses the Turtle graphics library to draw a pattern of hexagons, circles, and squares in three lines.
    
    """

import turtle
def setPos(turta, x, y):
    """
    Set the turtle's position without drawing.

    Parameters:
    - turta (turtle.Turtle): The Turtle object.
    - x (int): The x-coordinate to set the turtle's position.
    - y (int): The y-coordinate to set the turtle's position.

    """
    turta.penup()
    turta.goto(x, y)
    turta.pendown()

def hexagon(turta, hexa_color, border_color):
    """
    Draw a filled hexagon with specified colors.

    Parameters:
    - turta (turtle.Turtle): The Turtle object.
    - hexa_color (str): The fill color of the hexagon.
    - border_color (str): The border color of the hexagon.
    
    """
    turta.color(border_color, hexa_color)
    turta.begin_fill()
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.end_fill()

def square(turta, square_color, border_color):
    """
    Draw a filled square with specified colors.

    Parameters:
    - turta (turtle.Turtle): The Turtle object.
    - square_color (str): The fill color of the square.
    - border_color (str): The border color of the square.
    
    """
    turta.color(border_color, square_color)
    turta.begin_fill()
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.end_fill()

def circle(turta, circle_color, border_color):
    """
    Draw a filled circle with specified colors.

    Parameters:
    - turta (turtle.Turtle): The Turtle object.
    - circle_color (str): The fill color of the circle.
    - border_color (str): The border color of the circle.
    
    """
    turta.color(border_color, circle_color)
    turta.begin_fill()
    turta.circle(45)
    turta.end_fill()
    
def pattern(turta, hexa_color, circle_color, square_color, border_color):
    """
    Draw a pattern of hexagons, circles, and squares in three lines.

    Parameters:
    - turta (turtle.Turtle): The Turtle object.
    - hexa_color (str): The fill color of the hexagons.
    - circle_color (str): The fill color of the circles.
    - square_color (str): The fill color of the squares.
    - border_color (str): The border color of the shapes.
    
    """
    #1st line
    setPos(turta, -250, 100)
    hexagon(turta, hexa_color, border_color)
    setPos(turta, -110, 100)
    circle(turta, circle_color, border_color)
    setPos(turta, -40, 100)
    square(turta, square_color, border_color)
    #2nd line
    setPos(turta, -150, 0)
    hexagon(turta, hexa_color, border_color)
    setPos(turta, -10, 0)
    circle(turta, circle_color, border_color)
    setPos(turta, 60, 0)
    square(turta, square_color, border_color)
    #3rd line
    setPos(turta, -50, -100)
    hexagon(turta, hexa_color, border_color)
    setPos(turta, 90, -100)
    circle(turta, circle_color, border_color)
    setPos(turta, 160, -100)
    square(turta, square_color, border_color)
    
    
def main():
    """
    Main function to initialize Turtle graphics and draw the pattern.

    The user is prompted to enter colors for hexagons, circles, squares,
    and shape borders. The resulting pattern is drawn on the Turtle graphics
    window, and the program exits on click.Draw a pattern of hexagons, circles, and squares using Turtle graphics.

    This function initializes a Turtle object and draws a pattern consisting of
    hexagons, circles, and squares in three lines. The colors of the hexagons,
    circles, squares, and their borders are provided by the user as input.
    
    """
    turta = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("light blue")
    turta.speed(2)
    hexa_color= input("Enter the color of hexagon = ")
    circle_color= input("Enter the color of circle = ")
    square_color= input("Enter the color of square = ")
    border_color= input("Enter the color of shape borders = ")
    pattern(turta, hexa_color, circle_color, square_color, border_color)
    screen.exitonclick()


main()