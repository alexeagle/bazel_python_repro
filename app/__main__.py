import cowsay
import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

cowsay.cow(x.text)
