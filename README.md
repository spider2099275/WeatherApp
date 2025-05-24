# WeatherApp
A simple and user-friendly Weather App built with Python that fetches real-time weather data using the OpenWeatherMap API. This project demonstrates how to integrate external APIs, parse JSON responses, and build a functional GUI using tkinter.

from tkinter import *: Imports all classes and functions from the Tkinter GUI library.
from tkinter import ttk: Imports themed widgets like Combobox, Treeview, etc.
import requests: Allows sending HTTP requests (used to fetch weather data from API).
from PIL import ImageTk, Image: Used to open and display images in Tkinter.

def data_get(): Defines a function triggered when the button is clicked.
state = state_name.get(): Retrieves the selected state name from the dropdown.
requests.get(...): Sends a GET request to OpenWeatherMap API using the selected state as city name. The URL includes:
appid: Your API key.
units=metric: Returns temperatures in Celsius.
.json(): Converts the response to a dictionary.
w1_label.config(...): Updates the corresponding label widgets with:
weather description (e.g., "clear sky")
main["temp"]: Current temperature
main["feels_like"]: What it feels like
main["humidity"]: Current humidity %

win = Tk(): Creates the main Tkinter window.
win.title(...): Sets the title of the window.
win.config(...): Sets the background color of the window.
win.geometry(...): Sets the size (width x height) of the window.

Image.open(...): Opens the image from a local path.
.resize(...): Resizes the image to fit the window.
Image.LANCZOS: A high-quality resampling filter for resizing.
ImageTk.PhotoImage(...): Converts PIL image to Tkinter-compatible image.

Label(...): Creates a label widget to hold the background image.
.image = photo_image: Prevents image from being garbage collected.
.pack(...): Places the label in the window and expands it to fill.

Creates a text label with title "Weather X".
Sets font and size.
.place(...): Manually positions the widget.

ttk.Combobox: A dropdown menu to select state.
textvariable=state_name: Binds selection to state_name.
