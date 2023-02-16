import badger2040w
import badger_os
import urequests
from time import sleep


# ------------------------------
#        Program setup
# ------------------------------

# Create a new Badger and set it to update NORMAL
display = badger2040w.Badger2040W()
display.led(128)
display.set_update_speed(badger2040w.UPDATE_NORMAL)
display.connect()
#check for connection
if not(display.isconnected()):  
    display.text("Hello...sorry...No connection", 10, 10, scale=2)

# Global Constants
WIDTH = badger2040w.WIDTH
HEIGHT = badger2040w.HEIGHT
TEXT_WIDTH = WIDTH - 1
#--------------------------------
# Some helper functions
#--------------------------------

def clearscreen():
    display.set_pen(15)
    display.clear()
    display.set_pen(0)

def truncatestring(text, text_size, width):
    while True:
        length = display.measure_text(text, text_size)
        if length > 0 and length > width:
            text = text[:-1]
        else:
            text += ""
            return text

#Clear the connnection string 
clearscreen()
#Set Font
display.set_font("bitmap8")

#Draw first screens. 
clearscreen()
display.text("Rockets", 0, 10, scale=2)
display.line(0,26,WIDTH,26)

display.text("Acquiring data",0,30,scale=1)
sleep(1)
display.update()

#Carry out data request and get the JSON.
#Current requests are aimed at the dev stream - Unlimited requests but data is not updated
request = urequests.get("https://lldev.thespacedevs.com/2.2.0/launch/upcoming/")
data = request.json()

#Extract data and build strings
mission = "Mission Name: " +str(data['results'][0]['mission']['name'])
description = "Mission Description: "+truncatestring(str(data['results'][0]['mission']['description']),1,TEXT_WIDTH)

#Rebuild top of screen to remove acquiring data
clearscreen()
display.text("Rockets", 0, 10, scale=2)
display.line(0,26,WIDTH,26)

#Build mission data and and display
display.text("First Mission:",0,40,scale=1)
display.text(mission,0,50,scale=1)
display.text(description,0,60,scale=1)
display.update()
display.halt()
