from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from math import floor,log10
from random import randint
import logging
import os
import http.client

def openJson(file_dir):
    json_data = open(file_dir).read()
    data = json.loads(json_data)
    return data

def getCurrentPoints(user):
    data=openJson("..\\points.json")
    if user in data:
        return data[user]
    else:
        return 0

def writeJson(user,points):
    data=openJson("..\\points.json")
    data[user]=points
    with open("..\\points.json", "w") as jsonFile:
        json.dump(data, jsonFile)
        jsonFile.close()

logging.basicConfig(level=logging.INFO) #sets up logging module
logger = logging.getLogger(__name__)


file_directory="..\\points.json"

@csrf_exempt
def index(request):
    logging.info("Got a new request")
    messages={'messages':[]}
    event=request.POST.get('event')
    user = str(request.POST.get('username'))
    if event == "'updatePoints'":
        pointsToAdd = int(request.POST.get('points'))
        current = getCurrentPoints(user)
        new = current + pointsToAdd
        writeJson(user,new)
    elif event == "'initPoints'":
        writeJson(user,0)
    elif event == "'fetchDiscounts'":
        #Return discounts available
        #STATIC FEATURE! TO BE IMPLEMENTED AFTER COMPETITION. DEPENDS ON INSURANCE COMPANY
        raise NotImplementedError
    elif event == "'purchaseDiscount'":
        #process payment
        raise NotImplementedError
    elif event == "'fetchLeaderboard'":
        jsonF = openJson(file_directory)
        points = []
        pointsToUser={}
        for user in jsonF:
            points.append(jsonF[user])
            pointsToUser[points]=user
        points = sorted(points)
        totalStr=""
        for thing in points:
            totalStr=totalStr+pointsToUser[thing]+" "+thing+" "
        totalStr = totalStr[:-1]
        messages['messages'].append(totalStr)
    elif event == "'fetchPoints'":
        getCurrentPoints(user)
        messages['messages'].append("OK")
    else:
        messages['messages'].append("Invalid stuff")

    return HttpResponse(json.dumps({ #send message back
        'messages':
            messages['messages']

    }), 'application/json')
