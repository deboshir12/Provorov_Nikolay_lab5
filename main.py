import requests
import json
import tkinter


while True:
    iss = input('ISS information - 1,Request website = 2,Weather in SPB - 3,dayly foto - 4, exit = 0 \n')
    match iss:
        case '2':
            website = input('Enter url: \n')
            r = requests.get(website)
            print(r.text)
        case '0':break
        case '1':
            iss_s = input('ISS location - 1, Count people in space - 2, exit - 0\n')
            if iss_s == '1':
                r = requests.get('http://api.open-notify.org/iss-now.json') 
                s = r.json()
                print('Timestamp : %s'%s['timestamp'])
                print('Longitude : %s' % s['iss_position']['longitude'])
                print('Latitude : %s' % s['iss_position']['latitude'])
            elif iss_s == '2':
                r = requests.get('http://api.open-notify.org/astros.json') 
                s = r.json()
                print('Numbers astronaut : %s' % s['number'])
            elif iss_s == '0':break
            else:print('Wrong value')
        case '3':
            url = 'https://api.openweathermap.org/data/2.5/weather?'

            payload = {
                'id' :'536203',
                'appid' : '52a97dd42a46e316ec5c9013d8da4bc0'
            }
            req = requests.get(url,params = payload)
            data = req.json()

            print('Pressure: %s'%data['main']['pressure'])
            print('Humidity: %s'%data['main']['humidity'])
            print('Weather: %s' % data['weather'][0]['description'])
            #print('Temperature in SPB %s' % round(float(data['main']['temp'])-273.15,1))
        
        case '4':
            url_t = 'https://api.nasa.gov/planetary/apod?api_key=LGY02XeuPZhn4mrvM0fnK1jAAubvmKCODBeGpg8e'

            r = requests.get(url_t)
            data = r.json()
            img_url = data['hdurl']
            reques_img = requests.get(img_url)
            with open('req_img.png', 'wb') as file:
                file.write(reques_img.content)
            print(img_url)
            window = tkinter.Tk()

            window.title('FoTo')

            canvas = tkinter.Canvas(window, width=1000,height=800)
            canvas.pack()
            test = tkinter.PhotoImage(file='req_img.png')
            testImg = canvas.create_image(100,190, image = test)
            window.mainloop()

            
        case _:
            print('Wrong values')
            