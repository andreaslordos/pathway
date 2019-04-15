import requests
def getWeatherRisk(lat,long):

	def get_weather(lat,long):
		apikey="c38a7168acf848dde7ada7bef2e531ce"
		data = requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(long)+"&appid="+apikey)
		data = data.content
		#print(data)
		weather=eval(str(data)[2:-1])
		return weather

	def calculateRisk(weather_dict):
		'''
		IDs:
		2xx -> Thunderstorm
		3xx -> Drizzle
		5xx -> Rain
		6xx -> Snow
		7xx -> Atmosphere
			701 -> Mist
			741 -> Fog
			762 -> Volcanic Ash
			781 -> Tornado
		'''
		if weather_dict['visibility']<1000:
			risk = 1-((weather_dict['visibility']/1000))
		else:
			risk=0

		wid = int(str(weather_dict['weather'][0]['id'])[0])
		print("wid",wid)
		if wid=xxx=2 or wid==6 or wid==7:
			risk += 0.6
		elif wid==5:
			risk += 0.4
		elif wid==3:
			risk += 0.2
		if risk>1:
			return 1
		return risk

	weather=get_weather(lat,long)
	return calculateRisk(weather)
