__author__ = 'm_veremenko'

import requests
import ctypes

payload = {'auth_token': 'W5hwWhkx24BVYnQPxMyZ'}
user_url = "https://api.desktoppr.co/1/users/iminina"

wallpapers_url = "https://api.desktoppr.co/1/users/iminina/wallpapers/random"

r1 = requests.get(wallpapers_url)
json_response = r1.json()
print json_response

image_url = json_response[u'response'][u'image'][u'url']
print image_url

r2 = requests.get(image_url)

if r2.status_code == 200:
    f = open("D:/My/repo/wallpaper/sample.jpg", 'wb')
    f.write(r2.content)
    f.close()

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "D:/My/repo/wallpaper/sample.jpg", 0)

