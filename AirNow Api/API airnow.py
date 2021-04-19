from tkinter import *
from PIL import Image, ImageTk
import requests
import json

root = Tk()
root.iconbitmap('images/batman.ico')
root.title('Batman')


def zipcheck():
    try:
        query_url = 'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zip.get() + '&distance=25&API_KEY=2AB23C26-BE81-4702-AD0B-2C65D65B3665'
        api_request = requests.get(query_url)
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        if category == 'Good':
            weather_color = '#0C0'  # Green
        elif category == 'Moderate':
            weather_color = '#FFFF00'  # Yellow
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = '#ff9900'  # Orange
        elif category == 'Unhealty':
            weather_color = '#FF0000'  # Red
        elif category == 'Very Unhealthy':
            weather_color = '#990066'  # Purple
        elif category == 'Hezardous':
            weather_color = '#660000'  # Hard Red

        root.configure(background=weather_color)
        myLabel = Label(text=city + ' - Air Quality: ' + str(quality) + ' ' + str(category), font=("Helvetica", 20),
                        background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        print(e)


zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)
zip_button = Button(root, text='Zipcode Check', command=zipcheck)
zip_button.grid(row=0, column=1, stick=W+E+N+S)

root.mainloop()
