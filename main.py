__author__ = 'm_veremenko'

import requests
import ctypes
import threading
import time

# payload = {'auth_token': 'W5hwWhkx24BVYnQPxMyZ'}
# user_url = "https://api.desktoppr.co/1/users/iminina"

SPI_SETDESKWALLPAPER = 20
wallpapers_url = "https://api.desktoppr.co/1/wallpapers/random"

def set_wallpaper():
    r1 = requests.get(wallpapers_url)
    json_response = r1.json()
    print json_response

    image_url = json_response[u'response'][u'image'][u'url']
    print image_url

    r2 = requests.get(image_url)

    if r2.status_code == 200:
        f = open("sample.jpg", 'wb')
        f.write(r2.content)
        f.close()
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "sample.jpg", 0)
    return

def run():
  threading.Timer(10800.0, run).start()
  set_wallpaper()
  print time.strftime('%X %x %Z')

run()
