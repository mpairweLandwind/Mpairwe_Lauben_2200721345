# Libraries for web scraping
# Request,BeautifulSoup,lxml, scrapy, seleinium
# API keys
# Exercises, openweathermap.org UGX5000000,

# step1: import Libraries
import requests
from bs4 import BeautifulSoup
import csv
import json

# step2:  Fetch the web pages
# url = 'https://www.worldometers.info/coronavirus/'
# response = requests.get(url)

url = 'http://ryeko.org'
response = requests.get(url)
html_content = response.text
api_key = 'User API Key'

# step3: Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')


# step4: Extract the specific data
data = []
for item in soup.find_all('a'):
    title = item.text.strip()
    link = item.get('href')
    data.append({'title': title, 'link': link})
      


# step5 : save the data to a csv file
csv_file = 'scraped_data.csv'
with open('csv_file.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'link'])
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print('data printed successfully')

# step6 save the data to json 
json_file = 'scraped_data.json'
with open('json_file.json', mode = 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
  
# step 7: save successfully to csv file and json file
print("Data saved successfully to {csv_file} and {json_file}")

# Exercise: scrape data from the http://openweathermap.org
# current weatherdata
api_key = '5b50df8f16618f048565ce6c6669ae1d'
city = 'ibanda'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    main = data['main']
    weather = data['weather'][0]
    wind = data['wind']
    
    print(f"City: {data['name']}")
    print(f"Temperature: {main['temp']}°K")
    print(f"Pressure: {main['pressure']} hPa")
    print(f"Humidity: {main['humidity']}%")
    print(f"Weather: {weather['description']}")
    print(f"Wind Speed: {wind['speed']} m/s")
else:
    print(f"Failed to get weather data for {city}. Error code: {response.status_code}")



    
    