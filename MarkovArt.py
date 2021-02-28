"""
Name: Markov Visual Arts
Author: Jiankun Wu
Date: 2021.02.28
Intro: Draw a symbolic painting with turtle module using Markov Chain. 
"""

import turtle as t 
import numpy as np
import random

class MarkovArt:
    def __init__(self, transition_matrix):
        """Simulates a visual art that relies on a simple Markov chain.
           Args:
                transition_matrix (dict): transition probabilities
        """
        self.transition_matrix = transition_matrix
        self.symbols = list(transition_matrix.keys())


    def get_next_symbol(self, current_symbol):
        """Decides which symbol to generate next based on the current symbol.
           Args:
               current_symbol (str): the current symbol being generated.
        """
        return np.random.choice(
            self.symbols,
            p=[self.transition_matrix[current_symbol][next_symbol] \
            for next_symbol in self.symbols]
        )

    def compose_sequence(self, current_symbol="A", length=6):
        """Generates a sequence of symbols.
           Args:
                current_symbol (str): the symbol we are currently drawing

                length (int): how many symbols we should generate for the image.
        """
        symbols = []

        while len(symbols) < length:
            next_symbol = self.get_next_symbol(current_symbol)
            symbols.append(next_symbol)
            current_symbol = next_symbol
        
        print(symbols)
        return symbols
  

    def get_image(self, symbols):
        """Generates different figures using turtle module.
           Args:
                current_symbol (str): the symbol we are currently drawing

                length (int): how many symbols we should generate for the image.
        """

        def draw_diamond(turt):
            # To draw a diamond
            turt.pendown()
            turt.pencolor("grey")
            turt.begin_fill()
            turt.fillcolor("green")

            for i in range(1,3):
                turt.forward(200) 
                turt.right(45) 
                turt.forward(200) 
                turt.right(135) 
            turt.end_fill()
            turt.penup()

        def draw_square(turt):
            # To draw a square
            turt.pendown()
            turt.pencolor("green")
            turt.begin_fill()
            turt.fillcolor("green")
            for i in range(1,3):
                turt.forward(120) 
                turt.right(90) 
                turt.forward(120) 
                turt.right(90)
                turt.forward(120) 
            turt.end_fill()
            turt.penup()
            
        def draw_triangle(turt):
            # To draw a triangle
            turt.pendown()
            turt.pencolor("yellow")
            turt.begin_fill()
            turt.fillcolor("yellow")
            for i in range(1,3):
                turt.forward(120) 
                turt.right(120) 
                turt.forward(120) 
                turt.right(120)
            turt.end_fill()
            turt.penup()

        def draw_heart(turt):
            # To draw a heart
            turt.pendown()
            turt.pencolor("pink")
            turt.begin_fill()
            turt.fillcolor("pink")
            turt.left(45)
            turt.fd(200)
            turt.circle(100, 180)
            turt.right(90)
            turt.circle(100, 180)
            turt.fd(200)
            turt.end_fill()
            turt.penup() 

        def draw_star(turt):
            # To draw a star
            turt.pendown()
            turt.pencolor("red")
            turt.begin_fill()
            turt.fillcolor("red")
            for i in range(5):
                turt.forward(200)
                turt.right(144)
            turt.end_fill()
            turt.penup()


        window = t.Screen()
        window.screensize(4000, 4000)
        window.bgcolor("mint cream") 
        brad = t.Turtle() 
        brad.shape('turtle') 
        brad.color("green") 
        brad.speed('fast') 
       
        x = 0
        for current_note in symbols:
            if current_note == "A":
                draw_diamond(brad)
                brad.goto(-100 + x, -50)
            if current_note == "B":
                draw_triangle(brad)
                brad.goto(-150 + x, -20)
            if current_note == "C":
                draw_square(brad)
                brad.goto(200 + x, 50)
            if current_note == "D":
                draw_heart(brad)
                brad.goto(0 + x, 100)
            if current_note == "E":
                draw_star(brad)
                brad.goto(-200 + x, 150)
            x += 30
        brad.hideturtle()
        window.exitonclick() 
        return 

def main():
    art_maker = MarkovArt({
        "A": {"A": 0.3, "B": 0.2, "C": 0.2, "D": 0.2, "E": 0.1},
        "B": {"A": 0.1, "B": 0.2, "C": 0.3, "D": 0.1, "E": 0.3},
        "C": {"A": 0.2, "B": 0.2, "C": 0.2, "D": 0.2, "E": 0.2},
        "D": {"A": 0.4, "B": 0.2, "C": 0.1, "D": 0.2, "E": 0.1},
        "E": {"A": 0.9, "B": 0.05, "C": 0.01, "D": 0.02, "E": 0.02},
    })

    new_art = art_maker.compose_sequence(current_symbol="C", length=10)
    art_maker.get_image(new_art)


if __name__ == "__main__":
    main()
