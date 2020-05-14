from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Simple Weather")
root.geometry("600x600")
root.iconphoto(True, PhotoImage(file="/home/soumyo/PycharmProjects/Simple Weather Application/icon"))

try:
    api_request = requests.get("https://api.openaq.org/v1/measurements?country=IN&city=Kolkata&location=Bidhannagar%2C+Kolkata+-+WBPCB")
    api = json.loads(api_request.content)
except Exception as e:
    api = "Error ..."

my_label = Label(root, text=api["results"][0])
my_label.pack()

root.mainloop()