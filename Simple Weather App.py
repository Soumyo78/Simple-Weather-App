from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Simple Weather")
root.geometry("400x200")
root.config(bg="green")
root.iconphoto(True, PhotoImage(file="/home/soumyo/PycharmProjects/Simple Weather Application/icon"))

try:
    api_request = requests.get("https://api.openaq.org/v1/measurements?country=IN&city=Kolkata&location=Bidhannagar%2C+Kolkata+-+WBPCB&limit=1&date_to=2020-05-14")
    api = json.loads(api_request.content)

    city = api["results"][0]["location"]
    parameter = api["results"][0]["parameter"]
    value = api["results"][0]["value"]
    unit = api["results"][0]["unit"]


except Exception as e:
    api = "Error ..."

status = StringVar()

if (value >= 0) and (value < 51):
    status.set("Good")
elif (value >= 51) and (value < 101):
    status.set("Satisfactory")
elif (value >= 101) and (value < 169):
    status.set("Moderately polluted")
elif (value >= 169) and (value < 209):
    status.set("Poor")
elif (value >= 209) and (value < 749):
    status.set("Very Poor")
elif value >= 749:
    status.set("Severe")

my_label = Label(root, text=city+"\nOzon Index is "+"("+parameter+")"+": "+str(value)+" "+unit+"\nStatus : "+status.get(), font=("Arial", 20), bg="green", fg="white")
my_label.pack(pady=30)


root.mainloop()