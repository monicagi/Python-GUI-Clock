"""
    Name: Monica Guevara
    Class: CSC 4800
    Assignment: HW #8
    Date: 3/15/17
"""

from tkinter import *
from math import sin, cos, radians
from datetime import datetime


class point():
    """ A  point class that stores xy pairs"""
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return point(x, y)

    def __str__(self):
        return '[x:{0}, y:{1}]'.format(self.x, self.y)

    def offsetByVector(self, angle, length):
        """Creates a point from the origin and a vector. The vector consists of a length and an angle in radians"""
        x = int(cos(angle) * length) + self.x
        y = int(sin(angle) * length) + self.y
        return point(x, y)


class clockHands():
    """ This class manages the clock's hands which need to be placed in a circle"""
    root = Tk()

    # The clock's hand are initialized
    longHand = ""
    shortHand = ""
    secondHand = ""

    # The top and bottom corners of the rectangle or circle
    topCorner = point(45, 45)
    bottomCorner = point(470, 470)

    # Creates a Tk window
    def centerPoint(self):
        """The centerPoint function uses the midpoint formula to find th center"""
        x = (self.topCorner.x + self.bottomCorner.x) / 2
        y = (self.topCorner.y + self.bottomCorner.y) / 2
        return point(x, y)

    def updateClock(self, canvas):
        """The updateClock function initializes a clock"""

        def initHand(hand, color, width):
            """The initHand function creates the clock's hands """
            if hand == "":
                hand = canvas.create_line(0, 0, 0, 0, fill=color, width=width, capstyle="round")
                canvas.pack()
            return hand

        # Updates the clock's hour, minute, and second hands
        shortHand = self.shortHand = initHand(self.shortHand, "grey", 7)
        longHand = self.longHand = initHand(self.longHand, "black", 4)
        secHand = self.secondHand = initHand(self.secondHand, "red", 1)

        time = datetime.now()

        #This checks for any changes that a clock may have over a rotation
        hourAngle = ((time.hour * 30.0) + (30.0 * (time.minute / 60.0)))
        minuteAngle = ((time.minute * 6.0) + (6.0 * (time.second / 60.0)))
        secondAngle = (time.second * 6)

        def drawHand(Hand, angle, length):
            """The drawHand function draws the clock's hour, minute, and second hands"""

            #Sets the top of the clock to 0
            angle -= 90.0

            rads = radians(angle)
            center = self.centerPoint()
            endPoint = center.offsetByVector(rads, length)
            canvas.coords(Hand, center.x, center.y, endPoint.x, endPoint.y)

        drawHand(longHand, hourAngle, 150)
        drawHand(shortHand, minuteAngle, 190)
        drawHand(secHand, secondAngle, 200)

        # Calls the updateClock function after 500 ms
        rotate = lambda: self.updateClock(canvas)
        canvas.after(500, rotate)

    def run(self):
        self.root.mainloop()

    def __init__(self):
        #Adds the hour markers to the clock
        canvas = Canvas(self.root, width=500, height=550)
        canvas.create_text(262,27, font = "Times 20", text = "12")
        canvas.create_text(379, 55, font="Times 20", text="1")
        canvas.create_text(465, 145, font="Times 20", text="2")
        canvas.create_text(487, 260, font="Times 20", text="3")
        canvas.create_text(460, 377, font="Times 20", text="4")
        canvas.create_text(370, 465, font="Times 20", text="5")
        canvas.create_text(262, 489, font="Times 20", text="6")
        canvas.create_text(140, 465, font="Times 20", text="7")
        canvas.create_text(59, 385, font="Times 20", text="8")
        canvas.create_text(25, 260, font="Times 20", text="9")
        canvas.create_text(55, 145, font="Times 20", text="10")
        canvas.create_text(145, 55, font="Times 20", text="11")
        canvas.create_text(250, 530, font="Times 20", text="Monica Guevara")

        #Gets the corners of the rectangle or circle
        topCorner = self.topCorner
        bottomCorner = self.bottomCorner

        canvas.create_oval(topCorner.x, topCorner.y, bottomCorner.x, bottomCorner.y, width=3, fill= 'powderblue')
        center = self.centerPoint()

        def createTickMark(angle, dFromCenter, length, mark):
            """The createTickMark function creates the clock's minute tick marks"""
            angle -= 90.0
            rads = radians(angle)
            p1 = center.offsetByVector(rads, dFromCenter)
            p2 = center.offsetByVector(rads, dFromCenter + length)
            mark(p1, p2)

        sm_Tick = lambda p1, p2: canvas.create_line(p1.x, p1.y, p2.x, p2.y)

        # This creates the minute tick marks
        for angle in range(0, 360, 6):
            if(not angle %10 == 0):
                createTickMark(angle, 200, 15, sm_Tick)

        # Adds the second markers
        for angle in range(0, 360, 30):
            canvas.create_text(262, 60, font="Times 10", text="0")
            canvas.create_text(362, 85, font="Times 10", text="5")
            canvas.create_text(434, 160, font="Times 10", text="10")
            canvas.create_text(457, 260, font="Times 10", text="15")
            canvas.create_text(430, 357, font="Times 10", text="20")
            canvas.create_text(360, 430, font="Times 10", text="25")
            canvas.create_text(262, 460, font="Times 10", text="30")
            canvas.create_text(160, 433, font="Times 10", text="35")
            canvas.create_text(85, 360, font="Times 10", text="40")
            canvas.create_text(62, 260, font="Times 10", text="45")
            canvas.create_text(90, 159, font="Times 10", text="50")
            canvas.create_text(159, 89, font="Times 10", text="55")


        canvas.pack()
        #Adds a title to the frame or canvas
        self.root.wm_title("Clock")
        self.updateClock(canvas)


def main():
    Hand = clockHands()
    Hand.run()

if __name__ == '__main__':
    main()