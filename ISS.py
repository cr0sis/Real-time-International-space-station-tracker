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
    pos = iss.pos() 
    posx = iss.xcor()
    print(posx)
    if iss.xcor() >= (179):                 ### Lift up at the right edge of  
        iss.penup()                         ### the screen to avoid drawing a 
        iss.goto(float(lon),float(lat))     ### horizontal wrap round line
        time.sleep(5)
    else:
      iss.goto(float(lon),float(lat))
      iss.pendown()
      time.sleep(5)
