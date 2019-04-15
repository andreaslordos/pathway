import requests
from random import randint
import urllib
import time
import random
def req(lat, long):
        r = requests.get('https://nominatim.openstreetmap.org/reverse?lat=' + str(lat) + '&zoom=16&lon=' + str(long) + '&format=json').json()
#        print(r)
        latmin = float(r['boundingbox'][0])
        latmax = float(r['boundingbox'][1])
        longmin = float(r['boundingbox'][2])
        longmax = float(r['boundingbox'][3])

        path = random.random()

        print(latmin + (latmax-latmin)*path, longmin + (longmax-longmin)*path)
#        print(name);
'''        name = urllib.parse.quote_plus(name)
        time.sleep(1)
        r = requests.get('https://nominatim.openstreetmap.org/search?q=' + name + '&format=json').json()
#        print(r)
        if r==[]:
                return;
        try:
                latit = r[0]['lat']
                longit = r[0]['lon']
        except Exception as e:
                print(r)
                print(e)
#        print(name);
        name = urllib.parse.quote_plus(name)
        print(latit+randint(, ', ', longit)

        time.sleep(1)'''
        
for i in range(100):  
        req(35.1856 + randint(-100,100)/10000, 33.3823 + randint(-100,100)/10000);
for i in range(50):
        req(35.181679 + randint(-100,100)/100000, 33.385824 + randint(-100,100)/100000);
while True:
        req(35.1856 + randint(-1000,1000)/10000, 33.3823 + randint(-1000,1000)/10000);

#req(35.1856, 33.3823)
#for i in range(10):
#        print(35.1832 + randint(-100,100)/100000);
#//r = requests.get('https://github.com/timeline.json')
#r.json()
