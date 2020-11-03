import ISS_Info
import turtle
import time

screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic("world.png")
screen.register_shape("iss.gif")
screen.title("Real time ISS tracker")

iss = turtle.Turtle()
iss.shape("iss.gif")
iss.penup()
iss.pen(pencolor="red", outline=2)

while True:    
    location = ISS_Info.iss_current_loc()
    lat = location['iss_position']['latitude']
    lon = location['iss_position']['longitude']
    print("Position: \n latitude: {}, longitude: {}".format(lat,lon))
    iss.goto(float(lon),float(lat))
    iss.pendown()
    time.sleep(5)
