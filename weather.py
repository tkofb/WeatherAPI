import requests
from time import sleep

def celsiusToFahrenheit(num):
    convertedNum = (num*1.8) + 32
    return convertedNum

# Used sleep function to override personal issue
sleep(1)


params = { 
    'zip': '21801',
    'appid': '68454091de219371a75b27123462f4d0',
    'units': 'imperial'
}

try:
    request = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params = params)
except:
     print("",end="")

try: 
    if request.status_code == 200:
        currentTemp = int(request.json()['main']["feels_like"])
        returnString = f"{currentTemp}°F"
        print(returnString)
except:
    print("",end="")
    


