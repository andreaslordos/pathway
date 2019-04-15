import requests
import json
import time
def getTrafficRisk(source,destination):

    def getTraffic(source,destination):
        url = "https://maps.googleapis.com/maps/api/distancematrix/json"
        querystring = {"units":"metric","departure_time":str(int(time.time())),"traffic_model":"pessimistic","origins":source,"destinations":destination,"key":"AIzaSyB1adu0mLQ3pUg1jtI-eeyzcLaO65LFeqQ"}
        headers = {
            'cache-control': "no-cache",
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        d = json.loads(response.text)
        return d['rows'][0]['elements'][0]['duration_in_traffic']['value'],d['rows'][0]['elements'][0]['duration']['value']

    def calculateRisk(traffic_time,total_time):
        relative_traffic = abs((total_time-traffic_time))/total_time
        if relative_traffic>1:
            return 1
        return relative_traffic

    traffic_time,total_time = getTraffic(source,destination)
    print(traffic_time,total_time)
    return calculateRisk(traffic_time,total_time)
