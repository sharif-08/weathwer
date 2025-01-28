from tkinter import *
from tkinter import ttk
import requests
def get_data():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=94d443f9a130a9ba102376cc2c46ef7d").json()

    w_lable1.config(text=data['weather'][0]["main"])
    wd_lable1.config(text=data["weather"][0]["description"])
    temp_lable1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_lable1.config(text=data["main"]["pressure"])
    wind_lable1.config(text=data["wind"]["speed"])

win = Tk()
win.geometry("500x500")
win.config(bg="light blue",)
win.title("weather")

name_lable = Label(win,text= "weather",font=('Times New Roman',40,"bold"))
name_lable.place(x=25,y=30,height=50,width=450)

list_name =["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

city_name = StringVar()
com =ttk.Combobox(win,text="weather", values= list_name,font=("Times Nem Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=95,height=40,width=400)

w_lable = Label(win,text= "weather",font=('Times New Roman',25))
w_lable.place(x=25,y=185,height=30,width=210)
w_lable1 = Label(win,text= "",font=('Times New Roman',25))
w_lable1.place(x=250,y=185,height=30,width=210)

wd_lable = Label(win,text= "Description",font=('Times New Roman',25,))
wd_lable.place(x=25,y=225,height=30,width=210)
wd_lable1= Label(win,text= "",font=('Times New Roman',25,"bold"))
wd_lable1.place(x=250,y=225,height=30,width=210)



temp_lable = Label(win,text= "temperature",font=('Times New Roman',25))
temp_lable.place(x=25,y=265,height=30,width=210)
temp_lable1 = Label(win,text= "",font=('Times New Roman',25))
temp_lable1.place(x=250,y=265,height=30,width=210)

per_lable = Label(win,text= "pressure",font=('Times New Roman',25))
per_lable.place(x=25,y=305,height=30,width=210)
per_lable1 = Label(win,text= "",font=('Times New Roman',25))
per_lable1.place(x=250,y=305,height=30,width=210)

wind_lable = Label(win,text= "wind",font=("Times New Roman",25))
wind_lable.place(x=25,y=345,height=30,width=210)
wind_lable1 = Label(win,text="",font=("Times New Roman",25))
wind_lable1.place(x=250,y=345,height=30,width=210)


done_button= Button(win,text="Done",font=("Time New Roman",20,"bold"),command=get_data)
done_button.place(y=145,height=30,width=100,x=200)

win.mainloop()