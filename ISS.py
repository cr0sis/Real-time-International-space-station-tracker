import ISS_Info
import turtle
import time
import json
import urllib.request
import urllib.error  # <-- for catching URL-related errors

# Set up the screen
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("map.png")
screen.bgcolor("black")
screen.title("Real time ISS tracker")

# Try registering the shape
try:
    screen.register_shape("isss.gif")
except turtle.TurtleGraphicsError as e:
    print("Error registering shape: ", e)

# Set up ISS turtle
iss = turtle.Turtle()
try:
    iss.shape("isss.gif")
except turtle.TurtleGraphicsError:
    iss.shape("circle")  # Fallback shape
    print("Using default shape instead of 'isss.gif'")
iss.penup()
iss.pen(pencolor="red", pensize=1)
style = ('Arial', 8, 'bold')

# Set up astronauts info turtle
astronauts = turtle.Turtle()
astronauts.penup()
astronauts.color('orange')
astronauts.goto(-178, 0)
astronauts.hideturtle()

# Fetch astronaut data
url = "http://api.open-notify.org/astros.json"
try:
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    print("There are currently " + str(result["number"]) + " astronauts in space:\n")
    astronauts.write("People in space: " + str(result["number"]), font=style)
    astronauts.sety(astronauts.ycor() - 5)

    for p in result.get("people", []):
        print(p["name"] + " on: " + p["craft"])
        astronauts.write(p["name"] + " on: " + p["craft"], font=style)
        astronauts.sety(astronauts.ycor() - 5)
except urllib.error.URLError as e:
    print("Failed to fetch astronaut data:", e)
    astronauts.write("Error fetching astronaut data", font=style)
except json.JSONDecodeError as e:
    print("Failed to decode astronaut JSON:", e)

# Clear ISS path with spacebar
def wipe():
    iss.clear()

screen.onkey(wipe, "space")
screen.listen()

# Main loop
while True:
    try:
        location = ISS_Info.iss_current_loc()
        lat = float(location['iss_position']['latitude'])
        lon = float(location['iss_position']['longitude'])

        print("Position: \n latitude: {}, longitude: {}".format(lat, lon))

        if iss.xcor() >= 178:
            iss.penup()
            iss.goto(lon, lat)
        else:
            iss.goto(lon, lat)
            iss.pendown()
    except (KeyError, TypeError, ValueError) as e:
        print("Error in ISS location data:", e)
    except Exception as e:
        print("Unexpected error:", e)

    time.sleep(30)
