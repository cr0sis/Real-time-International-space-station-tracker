import ISS_Info
import turtle
import time
import json
import urllib.request

screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic("world.png")
screen.register_shape("iss.gif")
screen.title("Real time ISS tracker")

iss = turtle.Turtle()
iss.shape("iss.gif")

# Home
hlat = -2.8650
hlon = 54.07036

prediction = turtle.Turtle()
prediction.penup()
prediction.color('yellow')
prediction.goto(hlat,hlon)
prediction.dot(5)
prediction.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' +str(hlat) + '&lon=' + str(hlon) ### Grab UTC time of next pass over at coords above
response = urllib.request.urlopen(url)
result = json.loads(response.read())

over = result ['response'][1]['risetime']   ### Convert UTC to human readable time and date format
prediction.write(time.ctime(over))    ### Print result to screen at coords


iss.penup()   ### Avoid a line being drawn from initialisation to first coord
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




    
