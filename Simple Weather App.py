from tkinter import *
from PIL import ImageTk, Image
import requests
import json
import reverse_geocoder as rg
import pprint


root = Tk()
root.title("Simple Weather")
root.geometry("400x200")
root.iconphoto(True, PhotoImage(file="/home/soumyo/PycharmProjects/Simple Weather Application/icon"))

try:
    api_request = requests.get("http://api.airpollutionapi.com/1.0/aqi?lat=23.40576&lon=88.49073&APPID=sfe5amidb4dsuq5uvmgf4ob4r9")
    #api_request = requests.get("http://api.airpollutionapi.com/1.0/aqi?lat=28.7041&lon=77.1025&APPID=sfe5amidb4dsuq5uvmgf4ob4r9")
    api = json.loads(api_request.content)

    AQI = api["data"]["value"]
    status = api["data"]["text"]
    temp = api["data"]["temp"]
    lat = api["data"]["coordinates"]["latitude"]
    lon = api["data"]["coordinates"]["longitude"]
    source = api["data"]["source"]["name"]
    color = api["data"]["color"]
    color = color[:-1]
except Exception as e:
    api = "Error ..."

root.config(bg=color)


def reverseGeocode(coordinates):
    global city
    result = rg.search(coordinates)
    city = result[0]["name"]


# Driver function
if __name__ == "__main__":
    # Coorinates tuple.Can contain more than one pair.
    coordinates = (lat, lon)

    reverseGeocode(coordinates)

my_label1 = Label(root, text="Location : "+city+"\nAQI : "+str(AQI)+"\t| Status : "+status+"\nTemperature : "+temp+" °C", font=("Arial", 20), bg=color, fg="white")
my_label1.pack(pady=30)

my_label2 = Label(root, text="Source : "+source, bg=color, fg="white")
my_label2.pack()



root.mainloop()