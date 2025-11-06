import requests

# ----------- Input -----------
city= input("Enter city name :  ")
api_key = "b95a8322266cff6f78334ffc4ae0f5eb"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# ----------- API Call -----------

response = requests.get(url)
data = response.json()
w=((data["weather"][0]["main"]))
wd=(data["weather"][0]["description"])
tem=(data["main"]["temp"])
min=(data["main"]["temp_min"])
max=(data["main"]["temp_max"])
pre=(data["main"]["pressure"]) 
ws=(data["wind"]["speed"])    

print(f"weather-{w}")
print(f"weathe description-{wd}")
print(f"tempreture-{tem}")
print(f"temp_mini-{min}")
print(f"temp_max-{max}")
print(f"pressure-{pre}")
print(f"wint-speed-{ws}")

    
