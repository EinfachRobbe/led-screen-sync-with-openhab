import time
import getpixelcolor
from openhab import OpenHAB

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

base_url = 'http://yourip:8080/rest' #for example 'http://localhost:8080/rest'
openhab = OpenHAB(base_url)

print("CONNECTED TO REST API(" + base_url + ")")

# fetch all items
items = openhab.fetch_all_items()

lsCol = items.get('yourItemName') #for example 'KITCHEN_RGB_STRIP_COLOR'

x = 1

while(x == 1):

    rgb = getpixelcolor.average(0,0, 1920, 1080)
    rgbl = list(rgb)


    hsvt = rgb_to_hsv(rgbl[0], rgbl[1], rgbl[2])
    hsvl = list(hsvt)


    hsv = str(hsvl[0]) + "," + str(hsvl[1]) + "," + str(hsvl[2])

    lsCol.command(hsv)

    time.sleep(your delay) #for example 0.3








