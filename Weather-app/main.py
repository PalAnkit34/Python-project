from tkinter import *
from tkinter import  ttk
import  requests

def data_get():
    city = city_name.get()
    data =requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=cd7fe7307274d5a1c0d05c499870341e").json()
    W_lab1.config(text=data["weather"][0]["main"])
    Wb_lab1.config(text=data["weather"][0]["description"])
    temp_lab1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_lab1.config(text=data["main"]["pressure"])

win  = Tk()
win.title("Weather App ☁☁☁🌡🌡")
win.iconbitmap('icon.ico')
win.config(bg="#101250")
win.geometry("700x700")

name_lab = Label(win,text="Weather App",font=("Time New Roman",40,"bold"))
name_lab.place(x=105,y=50,height=50,width=450)

city_name = StringVar()
list_name = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai",
    "Kolkata", "Surat", "Pune", "Jaipur", "Lucknow", "Kanpur",
    "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Pimpri-Chinchwad",
    "Patna", "Vadodara", "Ghaziabad", "Ludhiana", "Agra", "Nashik",
    "Faridabad", "Meerut", "Rajkot", "Kalyan-Dombivli", "Vasai-Virar",
    "Varanasi", "Srinagar", "Aurangabad", "Dhanbad", "Amritsar",
    "Navi Mumbai", "Allahabad", "Ranchi", "Howrah", "Coimbatore",
    "Jabalpur", "Gwalior", "Vijayawada", "Jodhpur", "Madurai",
    "Raipur", "Kota", "Guwahati", "Chandigarh", "Solapur",
    "Hubli-Dharwad", "Tiruchirappalli", "Bareilly", "Mysore",
    "Tiruppur", "Gurgaon", "Aligarh", "Jalandhar", "Bhubaneswar",
    "Salem", "Mira-Bhayandar", "Warangal", "Thiruvananthapuram",
    "Guntur", "Bhiwandi", "Saharanpur", "Gorakhpur", "Bikaner",
    "Amravati", "Noida", "Jamshedpur", "Bhilai", "Cuttack",
    "Firozabad", "Kochi", "Bhavnagar", "Dehradun", "Durgapur",
    "Asansol", "Nanded", "Kolhapur", "Ajmer", "Gulbarga",
    "Jamnagar", "Ujjain", "Loni", "Siliguri", "Jhansi",
    "Ulhasnagar", "Nellore", "Jammu", "Sangli-Miraj & Kupwad",
    "Belgaum", "Mangalore", "Ambattur", "Tirunelveli", "Malegaon",
    "Gaya", "Udaipur", "Maheshtala", "Davanagere", "Kozhikode"
]
com = ttk.Combobox(win, values=list_name, font=("Time New Roman", 30, "bold"),textvariable=city_name)
com.place(x=105,y=120,height=50,width=450)


#Weather Climate

W_lab = Label(win,text="Weather Climate",font=("Time New Roman",20,"bold"))
W_lab.place(x=30,y=270,height=50,width=250)

W_lab1 = Label(win,text="",font=("Time New Roman",20,"bold"))
W_lab1.place(x=320,y=270,height=50,width=200)
#Weather Description

Wb_lab = Label(win,text="Weather Description",font=("Time New Roman",18,"bold"))
Wb_lab.place(x=30,y=330,height=50,width=250)

Wb_lab1 = Label(win,text="",font=("Time New Roman",18,"bold"))
Wb_lab1.place(x=320,y=330,height=50,width=200)

#Temperature

temp_lab = Label(win,text="Temperature",font=("Time New Roman",20,"bold"))
temp_lab.place(x=30,y=390,height=50,width=250)

temp_lab1 = Label(win,text="",font=("Time New Roman",20,"bold"))
temp_lab1.place(x=320,y=390,height=50,width=200)

#Pressure

per_lab = Label(win,text="Pressure",font=("Time New Roman",20,'bold'))
per_lab.place(x=30,y=450,height=50,width=250)

per_lab1 = Label(win,text="",font=("Time New Roman",20,'bold'))
per_lab1.place(x=320,y=450,height=50,width=200)

# done button

Done_button = Button(win,text="Done",font=("Time New Roman", 30, "bold"),command=data_get)
Done_button.place(y=190,height=50,width=100,x=270)

win.mainloop()


