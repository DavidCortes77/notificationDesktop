# import required libraries 
import requests 
from bs4 import BeautifulSoup 
from win10toast import ToastNotifier 

# create an object to ToastNotifier class 
n = ToastNotifier() 

# define a function 
def getdata(url): 
	r = requests.get(url) 
	return r.text 
	
htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/") 

soup = BeautifulSoup(htmldata, 'html.parser') 

current_temp = soup.find_all("span", class_= "CurrentConditions--tempValue--MHmYY") 

chances_rain = soup.find_all("div", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf") 

temp = (str(current_temp))

temp_rain = str(chances_rain)
print(temp_rain) 

result = "Temperatura actual " + temp[82:84] + " En Medellin" + "\n" + temp_rain[131:-14] 
n.show_toast("Actualizacion del clima", 
			result, duration = 10) 
