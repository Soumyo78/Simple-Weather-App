from tkinter import *
from PIL import ImageTk, Image
import requests
import json
import reverse_geocoder as rg
from io import BytesIO
from geopy.geocoders import Nominatim


root = Tk()
root.title("Simple Weather")
root.geometry("450x280")
root.resizable(width=False, height=False)
root.iconphoto(True, PhotoImage(file="/home/soumyo/PycharmProjects/Simple Weather Application/icon"))

def gridForget():
    search_btn.config(state=NORMAL)
    root.config(bg="white")
    entry_box.delete(0, "end")
    my_label2.grid_forget()
    my_label1.grid_forget()
    my_label3.grid_forget()
    my_label4.grid_forget()
    clear_btn.config(state=DISABLED)


def search():
    clear_btn.config(state=NORMAL)
    search_btn.config(state=DISABLED)
    global AQI
    global status
    global temp
    global lat
    global lon
    global color
    global source
    global pure_link
    global pure_description
    global my_label1
    global my_label2
    global my_label3
    global my_label4
    city_name = entry_box.get()
    geolocator = Nominatim(user_agent='myapplication')
    location = geolocator.geocode(city_name)
    la = location.raw["lat"]
    lo = location.raw["lon"]
    api_add = "http://api.airpollutionapi.com/1.0/aqi?lat="+str(la)+"&lon="+str(lo)+"&APPID=sfe5amidb4dsuq5uvmgf4ob4r9"

    # Using Try or Except
    try:
        api_request = requests.get(api_add)
        api = json.loads(api_request.content)

        AQI = api["data"]["value"]
        status = api["data"]["text"]
        temp = api["data"]["temp"]
        lat = api["data"]["coordinates"]["latitude"]
        lon = api["data"]["coordinates"]["longitude"]
        source = api["data"]["source"]["name"]
        color = api["data"]["color"]
        color = color[:-1]
        clouds = api["data"]["clouds"]
        descripsion, link_text = clouds.split(",")
        pure_link = link_text.split("=")
        pure_description = descripsion.split("=")

    except Exception as e:
        api = "Error ..."

    root.config(bg=color)  # Changing root window background color

    url = pure_link[1]

    # Creating image for weather
    # img_url = url
    # response = requests.get(img_url)
    # img_data = response.content
    # img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    # img_label = Label(root, image=img, bg=color, anchor="w")
    # img_label.grid(row=2, column=1, sticky=W)

    def reverseGeocode(coordinates):
        global city
        result = rg.search(coordinates)
        city = result[0]["name"]

    # Driver function
    if __name__ == "__main__":
        # Coorinates tuple.Can contain more than one pair.
        coordinates = (lat, lon)

        reverseGeocode(coordinates)

    # Creating Labels
    my_label1 = Label(root, text="Location : " + city + "\nAQI : " + str(AQI) + " | Status : " + status, font=("Arial", 20), bg=color, fg="white")
    my_label1.grid(row=1, column=0, columnspan=2)

    my_label2 = Label(root, text="Temperature : " + temp + " °C", font=("Arial", 20), bg=color, fg="white")
    my_label2.grid(row=3, column=0, padx=5, columnspan=2)

    my_label3 = Label(root, text="Weather :" + pure_description[1], font=("Arial", 20), bg=color, fg="white")
    my_label3.grid(row=2, column=0, padx=5, columnspan=2)

    my_label4 = Label(root, text="Source : " + source, bg=color, fg="white")
    my_label4.grid(row=4, column=0, sticky=W, pady=20, padx=5, columnspan=2)


# Creating EntryBox
entry_box = Entry(root, font=("Arial", 15), width=25, bg="yellow", fg="black", justify=CENTER)
entry_box.grid(row=0, column=0, pady=30, padx=8, sticky=W+E+N+S)

# Creating Search Button
search_btn = Button(root, text="Search", bg="cyan", fg="black", font=("Arial"), command=search)
search_btn.grid(row=0, column=1, pady=30, sticky=W+E+N+S)

# Creating Search Button
clear_btn = Button(root, text="Clear", bg="red", fg="white", font=("Arial"), state=DISABLED, command=gridForget)
clear_btn.grid(row=0, column=2, pady=30, sticky=W+E+N+S)





root.mainloop()