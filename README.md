# RGB-LED screen sync with openHAB REST API
A python script which gets the average color on your screen, converts it to hsv and sends it to openHAB api.

## Libraries

 - python-openhab ([https://pypi.org/project/python-openhab](https://pypi.org/project/python-openhab))
 - getpixelcolor ([https://pypi.org/project/GetPixelColor](https://pypi.org/project/GetPixelColor))

## Instruction

**1.** Get your openHAB REST API link and paste into base_url
**2.** Open the API link in your browser and go to "items"
**3.** Search for your LED and copy the name-field (type must be Color)
**4.** Paste it into the lsCol-variable
**5.** Set your update-delay at the bottom (the less delay, the more network load)
**6.** Here you are!

## Contact
**Discord:** *"einfachrobbe"*
