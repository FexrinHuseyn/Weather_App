import requests
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup

#Screen
screen=tk.Tk()
screen.title("Weather App")
screen.config(width=500,height=800,bg="#d49ef3")

#image
search_icon = PhotoImage(file="search.png")
temp_icon = PhotoImage(file="temp.png")
sky_icon = PhotoImage(file="skyicon.png")
time_icon = PhotoImage(file="timeicon.png")
img = PhotoImage(file="file.png")
img_label = Label(image=img, bg="#d49ef3")
img_label.place(x=-30, y=400)


#Font& Color
Font=("Comic Sans",15,"bold")
Color="#d49ef3"


#Label
text_label=Label(text="Weather App",font=("Comic Sans MS",50,'bold'),bg=Color,fg="#3c025c")
text_label.place(x=40,y=100)


question_label = Label(text="Please enter City:", fg="white", font=('Arial', 15, 'bold'), bg=Color)
question_label.place(x=180, y=200)


temp_icon_label = Label(image=temp_icon, bg=Color)
temp_icon_label.place(x=11, y=200)


time_icon_label = Label(image=time_icon, bg=Color)
time_icon_label.place(x=27, y=300)


sky_icon_label = Label(image=sky_icon, bg=Color)
sky_icon_label.place(x=22, y=360)

#entry
question_entry = Entry(width=30, font=('Helvetica', 10, 'bold'),fg="#610297")
question_entry.focus()
question_entry.place(x=155, y=240)

#Func
def fetch_weather():
    city = question_entry.get()
    url = f"https://www.google.com/search?q=weather{city}"

    if question_entry.get() == "":
        messagebox.showerror(title="Error", message="Please enter a city name !")
    else:
        try:
            html = requests.get(url).content
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
            std = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
            data = std.split('\n')
            time = data[0]
            sky = data[1]

            temp_output_label = Label(text=f"Temperature: {temp}", font=Font, bg=Color)
            temp_output_label.place(x=160, y=420)

            time_output_label = Label(text=f"Time: {time}", font=Font, bg=Color)
            time_output_label.place(x=160, y=470)

            sky_output_label = Label(text=f"Sky: {sky}", font=Font, bg=Color)
            sky_output_label.place(x=160, y=520)



        except Exception as e:
            messagebox.showerror("Error", "Unable to fetch weather data !")


#Button
info_button = Button(image=search_icon, width=207, command=fetch_weather,bg="#ebc6ff")
info_button.place(x=155, y=270)
exit_button = Button(text="Exit", width=20, command=lambda: screen.destroy(), font=('Helvetica', 13, 'bold'),bg="#ebc6ff")
exit_button.place(x=155, y=330)













screen.mainloop()