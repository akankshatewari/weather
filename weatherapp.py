from tkinter import *
import tkinter as tk
import requests
import pint


def test_function(entry):
	print("This is the entry:", entry)

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		if Fahreneit_button:
			final = 'Place: %s \nWeather: %s \nTemperature: %s' % (name, desc, temp)

		if Celcius_button:
			final = 'Place: %s \nWeather: %s \nTemperature: %s' % (name, desc, temp)


	except:
		final = 'Problem in extracting information'

	return final

def weather_info(city):
	weather = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'Imperial'}
	response = requests.get(url, params=params)
	weather1 = response.json()

	label['text'] = format_response(weather1)

def weather_info1(city):
	weather = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather, 'q': city, 'units': 'Metric'}
	response = requests.get(url, params=params)
	weather1 = response.json()

	label['text'] = format_response(weather1)

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=500,bg='light green')
canvas.pack()

frame = tk.Frame(root, bg='Blue', bd=25)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.15, anchor='n',)

entry = tk.Entry(frame, font=30)
entry.place(relwidth=0.5, relheight=1)

Fahreneit_button = tk.Button(frame, text="Fahrenheit", font='Cartes', command=lambda: weather_info(entry.get()))
Fahreneit_button.place(relx=0.53,rely=0,relheight=1, relwidth=0.25)

Celcius_button = tk.Button(frame, text="Celsius", font='Cartes', command=lambda: weather_info1(entry.get()))
Celcius_button.place(relx=0.8,rely=0,relheight=1, relwidth=0.25)

frame_1 = tk.Frame(root, bg='Blue', bd=10)
frame_1.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(frame_1)
label.place(relwidth=1, relheight=1)

root.mainloop()
