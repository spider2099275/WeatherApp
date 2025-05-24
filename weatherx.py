from tkinter import *
from tkinter import ttk
import requests
from PIL import ImageTk, Image

def data_get():
    state = state_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+state+"&appid=b0eb38b9685dd277b8910725edf0dec6&units=metric").json()
    w1_label.config(text=data["weather"][0]["description"])
    ct1_label.config(text=data["main"]["temp"])
    ctfl1_label.config(text=data["main"]["feels_like"])
    h1_label.config(text=data["main"]["humidity"])

win = Tk()
win.title("Weather App")
win.config(bg = "light blue")
win.geometry("500x600")
image = Image.open(r"C:\\Users\\Spyder\\Downloads\\pngtree-white-cloud-on-blue-sky-weather-background-image_410050.jpg")
resized_image = image.resize((500, 600), Image.LANCZOS)
photo_image = ImageTk.PhotoImage(resized_image)

bg_label = Label(win, image=photo_image)
bg_label.image = photo_image  
bg_label.pack(fill="both", expand=True) 

name_label= Label(win,text="Weather X",
                  font=("Time New Roman",50,"bold"))
name_label.place(x=25,y=50,height=60,width=450) 

state_name= StringVar()

list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com= ttk.Combobox(win,text="Weather X",values=list_name,
                  font=("Time New Roman",20,"bold"),textvariable=state_name) 
com.place(x=25,y=120,height=60,width=450)  

w_label= Label(win,text="Weather Climate",
                  font=("Time New Roman",17))
w_label.place(x=25,y=260,height=60,width=210)

w1_label= Label(win,text="",
                  font=("Time New Roman",17))
w1_label.place(x=250,y=260,height=60,width=210)

ct_label= Label(win,text="Climate temperature",
                  font=("Time New Roman",17))
ct_label.place(x=25,y=330,height=60,width=210)

ct1_label= Label(win,text="",
                  font=("Time New Roman",17))
ct1_label.place(x=250,y=330,height=60,width=210)

ctfl_label= Label(win,text="Climate feels like",
                  font=("Time New Roman",17))
ctfl_label.place(x=25,y=400,height=60,width=210)

ctfl1_label= Label(win,text="",
                  font=("Time New Roman",17))
ctfl1_label.place(x=250,y=400,height=60,width=210)

h_label= Label(win,text="Humidity",
                  font=("Time New Roman",17))
h_label.place(x=25,y=470,height=60,width=210)

h1_label= Label(win,text="",
                  font=("Time New Roman",17))
h1_label.place(x=250,y=470,height=60,width=210)

done_buttton=Button(win,text="Done",
                  font=("Time New Roman",20,"bold"),command=data_get)

done_buttton.place(x=200,y=190,height=60,width=100)

win.mainloop()