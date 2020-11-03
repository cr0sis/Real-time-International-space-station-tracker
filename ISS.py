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

iss.penup()   ### Avoid a line being drawn from initiliation to first coord
iss.pen(pencolor="red", pensize=1) 

def wipe():
    iss.clear()

screen.onkey(wipe, "space")### Allow us to clear history with spacebar 
screen.listen()            ### if screen gets too busy over time

while True:       
    location = ISS_Info.iss_current_loc()
    lat = location['iss_position']['latitude']
    lon = location['iss_position']['longitude']
    print("Position: \n latitude: {}, longitude: {}".format(lat,lon))
    pos = iss.pos() 
    posx = iss.xcor()
    if iss.xcor() >= (179.1):           ### Stop drawing at the right edge of  
        iss.penup()                     ### the screen to avoid a 
        iss.goto(float(lon),float(lat)) ### horizontal wrap round line
        time.sleep(5)
    else:
      iss.goto(float(lon),float(lat))
      iss.pendown()
      time.sleep(5)
