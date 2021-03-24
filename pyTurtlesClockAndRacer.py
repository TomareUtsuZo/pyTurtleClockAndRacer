# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020C
# Assignment: Assignment 1.2 - Turtle graphics, loops, and function
# Author: Carl Eranio (s3608100)
# Created date: 13/11/2020
# Last modified date: 10/12/2020
# This program is a demonstration of Carl Eranio's budding code skills. The task is to
# create a clock using the Turtles. This was very similar to my first practice coding.
# So, I updated some of the functions to use new methods and tools. draw_a_line() benefited
# greatly, as did the main loop, which was simplified to one turtle handling the hands of the
# clock.

from time import localtime, strftime
import datetime
from random import randint
import turtle
import math

# Parameters                This is an important section of the coding process, as it allows the
#                           coder to change important parameters of the program in one place,
#                           without having to hunt for the various locations.

clock_radius = 280          # This sets the radius of the clock face
hour_forward = 100          # these codes are parameters for how long the hands will be
minutes_forward = 170
seconds_forward = 170
home = [0, 70]
curr_date = datetime.date.today()
min_sec_count_down = 60
hour_count_down = 24
mon_count_down = 12

# Functions                 This is an important section of the coding process where the coder
#                           creates the repeatable logics and functions of his program, simplifying
#                           the main and saving coding space for repeatable tasks


def make_window(color, title):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    # based on code by Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers
    # Source repository is at https://code.launchpad.net/~thinkcspy-rle-team/thinkcspy/thinkcspy3-rle

    w = turtle.Screen()
    w.setup(width=.95, height=.95)
    w.bgcolor(color)
    w.title(title)
    return w


def make_turtle(t_color, size):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
     """
    # Based on code by Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers
    # Source repository is at https://code.launchpad.net/~thinkcspy-rle-team/thinkcspy/thinkcspy3-rle

    t = turtle.Turtle()
    t.color(t_color)
    t.pensize(size)
    t.speed(0)
    return t


def make_clock_face(clock_it, face_size):
    """
        This builds a clock face. It calls for an input to determine how big the face should be, relative
        to the clock size
    """
    # Created by Carl Eranio 2020-11-12
    face_size = face_size - 30        # face_size should be relative to the radius of the clock
    face_style = ('Courier', 15, 'bold')
    clock_it.shape("circle")
    clock_it.penup()
    clock_it.pensize(1)
    num_it = int(face_size * .70)            # these calculate the parameters of the clock face
    dash_len = int(face_size * .10)          # drawing
    space_it = int(face_size * .20)
    clock_it.setheading(90)                 # set first 12
    clock_it.hideturtle()                   # Moves faster when not seen, like ninja
    clock_it.setpos(home)

    for i in range(60):                     # this loop makes the 12 positions of the clock face
        clock_it.penup()
        clock_it.forward(num_it)        # it moves the turtle forward to where the dash line
        if i % 5 == 0:
            if i != 0:
                clock_it.write(i//5, font=face_style, align='center')
            else:
                clock_it.setx(clock_it.xcor() - 5)
                clock_it.write('12', font=face_style, align='center')
        clock_it.forward(space_it)          # moves forward to stamp itself into the clock face.
        if i % 5 == 0:      # if one of the 12 hour demarcations on the clock
            clock_it.forward(dash_len)
            clock_it.stamp()
        else:
            clock_it.pendown()
            clock_it.forward(dash_len)
        clock_it.penup()
        clock_it.goto(home)
        clock_it.right(6)


def draw_a_line(t, what_direction, length, t_color, t_size, start):
    """
    This will draw a line. I created it for the clock hands to be drawn, repeatedly. There is a gotcha
    here. The length of the the line is also a function of where the line starts, so one one needs to
    tell the x/y components where the line starts from, to get true length.
    :param t: turtle name
    :param what_direction: what heading wil the turtle move
    :param length: how long the hand will be
    :param t_color: what color will the line be
    :param t_size: how long the line will be
    :param start: [x, y] coordinate where line will start
    """
    # Improved by code in class
    t.penup()
    t.color(t_color)
    t.pensize(t_size)
    t.goto(start)
    t.pendown()
    x = int(length * math.cos(math.radians(what_direction)) + start[0])
    y = int(length * math.sin(math.radians(what_direction)) + start[1])
    line.goto(x, y)


def create_the_clock():   # this will do all the drawing that needs doing before telling time
    """
        this logic will create the clock face This is just to keep the main clean
    """
    # created Carl Eranio 2020-11-13

    draw_circle = make_turtle("black", 12)
    draw_circle.speed(0)        # this block of code will preposition the turtle
    draw_circle.hideturtle()
    draw_circle.penup()
    draw_circle.setpos(home[0], (home[1] - clock_radius))
    draw_circle.pendown()
    draw_circle.circle(clock_radius)
    make_clock_face(draw_circle, clock_radius)                   # this will make the pretty face of the clock


def racer(t, is_inside_y):
    """
    This will do the racer actions. calculates the racer's track position, gens a randint to move
    forward.
    :param t: turtle name
    :param is_inside_y: 1 is yes
    :return:
    """
    # created by Carl Eranio 2020-11-15
    turtle_close = 20
    turtle_far = 40
    if is_inside_y == 'inside':
        edge_case = turtle_close
        in_case = turtle_far
    else:
        edge_case = turtle_far
        in_case = turtle_close
    what_forward = randint(1, 10)            # create a rand into to see how well the turtle does this turn
    if t.heading() == 90:                    # make sure the turtle hasn't met the edge of the track while
        if t.ycor() + what_forward <= clock_radius + edge_case + home[1]:        # heading up. if it hasn't move the
            t.forward(what_forward)                             # rand distance
        else:                               # If it has hit limit of the track then turn
            t.sety(clock_radius + edge_case + home[1])
            t.left(90)
    elif t.heading() == 180:                # make sure the turtle hasn't met the edge of
        if t.xcor() - what_forward >= -clock_radius - in_case + home[0]:   # make sure the turtle hasn't met the edge of
            t.forward(what_forward)         # the track while heading left. if it hasn't move the rand distance
        else:                               # If it has hit limit of the track then turn
            t.setx(-clock_radius - in_case + home[0])
            t.left(90)
    elif t.heading() == 270:                # make sure the turtle hasn't met the edge of
        if t.ycor() - what_forward >= -clock_radius - in_case + home[1]:   # make sure the turtle hasn't met the edge of
            t.forward(what_forward)         # the track while heading down. if it hasn't move the rand distance
        else:                               # If it has hit limit of the track then turn
            t.sety(-clock_radius - in_case + home[1])
            t.left(90)
    elif t.heading() == 0:                  # make sure the turtle hasn't met the edge of
        if t.xcor() + what_forward <= clock_radius + edge_case + home[0]:    # make sure the turtle hasn't met the edge of
            t.forward(what_forward)          # the track while heading right. if it hasn't move the rand distance
        else:                                # If it has hit limit of the track then turn
            t.setx(clock_radius + edge_case + home[0])
            t.left(90)


def racers_get_ready(t, inside_y):
    """
    This is created to ready the racers, w repeatable logic
    :param t: turtle name
    :param inside_y: will this be inside, 1 = yes
    """
    # Created by Carl Eranio 2020-11-15
    if inside_y == 1:
        track = clock_radius + 40
    else:
        track = clock_radius + 70

    t.shape("turtle")
    t.speed(0)
    t.penup()
    t.forward(track)
    t.left(90)


def leap_is_one(year):
    """
    taking a year, tells caller if this is a leap year
    """
    # TomareUtsuZo
    return (year % 400 == 0) or ((year % 100 != 0) and year % 4 == 0)


def days_in_mon(month, year):
    """
    This will return how many days in am month.
    :param month:
    :param year:
    :return: int: days in a called month
    """
    thirty_days = [4, 6, 9, 11]

    if month == 2:
        if leap_is_one(year):
            how_many = 29
        else:
            how_many = 28
    elif month in thirty_days:
        how_many = 30
    else:
        how_many = 31

    return how_many


make_window("white", "this is a clock")

create_the_clock()                          # creates clock face

inside_track = make_turtle("red", 20)       # these will preposition the racers
outside_track = make_turtle("blue", 20)
racers_get_ready(inside_track, 1)
racers_get_ready(outside_track, 0)

line = make_turtle("black", 10)             # these (draw) turtles are for the hands
line.hideturtle()
digi_write = make_turtle('hotpink', 1)      # This turtle is for writing the text
digi_write.hideturtle()
digi_write.penup()
style = ('Courier', 15, 'normal')
seconds_was = 0                             # these force the clock to draw it's first time
day_count_down = days_in_mon(curr_date.month, curr_date.year)

while 1:
    curr_date = datetime.date.today()
    hour_now = int(strftime("%H", localtime()))     # Get the current time variables
    minute_now = int(strftime("%M", localtime()))
    seconds_now = int(strftime("%S", localtime()))

    if seconds_now != seconds_was:              # if the second has changed
        line.clear()                            # clear the hands, the draw
        draw_a_line(line, -((seconds_now % 60) * 6) + 90, seconds_forward, 'red',  1, home)  # second
        draw_a_line(line, -((minute_now % 60) * 6) + 90, minutes_forward, 'black', 1, home)  # minute
        draw_a_line(line, -((hour_now % 12) * 30) + 90, hour_forward, 'black', 5, home)  # hour
        digi_write.clear()  # clear the text below then write
        digi_write.setpos(home[0], home[1] - clock_radius - 100)
        digi_write.write("Current time is {} {},".format(curr_date, (strftime("%H:%M:%S"))),
                         font=style, align='center')
        digi_write.sety(home[1] - clock_radius - 130)
        digi_write.write("There are {} months, {} days, {} hours, {} minutes, and {} seconds left "
                         "till the New Year!!"
                         .format((mon_count_down - curr_date.month), (day_count_down - curr_date.day),
                                 (hour_count_down - hour_now), (min_sec_count_down - minute_now),
                                 (min_sec_count_down - seconds_now)), font=style, align='center')
        seconds_was = seconds_now               # acknowledge doing as much
    else:                                       # if there is no need to update the clock, do the great race
        racer(inside_track, 'inside')
        racer(outside_track, 'outside')
