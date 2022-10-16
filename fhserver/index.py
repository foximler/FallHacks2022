from datetime import datetime, timedelta
import time
from tracemalloc import start
import requests
import json
import eventlet
import socketio
sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
  '/': {'content_type': 'text/html', 'filename': 'index.html'}
})
@sio.event
def connect(sid, environ):
  print('connect ', sid)

@sio.event
def createAlarm(sid, data):
    print(data)
    input_values(data['arrivalTime'], str(data['delayTime']), data['curr'], data['dest'])

@sio.event
def cancelAlarm(sid, data):
    alarmCanceled = True

def input_values(arriveTimeInput, bufferTimeInput, startPointInput, destinationInput):
    alarmCanceled = False
    arriveTime = datetime.strptime(arriveTimeInput, "%H:%M")
    bufferTime = time.strptime(bufferTimeInput, "%M")
    startPoint = startPointInput #Add inputted start point
    destination = destinationInput #Add destination

    reqTime = datetime.now().strftime("%H:%M:%S")
    str = "http://dev.virtualearth.net/REST/v1/Routes?wp.0=" + startPoint + "&wp.1=" + destination + "&optimize=timeWithTraffic&routeAttributes=routeSummariesOnly&timeType=Departure&dateTime=" + reqTime + "&key="
    response = requests.get(str)
    parse = json.loads(response.text)
    driveTime = parse['resourceSets'][0]['resources'][0]['travelDurationTraffic']
    while(alarmCanceled == False):
        changeTime = timedelta(minutes=(driveTime/60 + bufferTime.tm_min))
        wakeup = arriveTime - changeTime
        if(datetime.now().strftime("%H:%M") > wakeup.strftime("%H:%M")):
            print("Time to wakeup!") #Add call to alarm here
            sio.emit("alarmOutWake",'shoes come off and the freaks come out')
            alarmCanceled = True
        if(int(datetime.now().strftime("%H")) < int(wakeup.strftime("%H")) - 1):
            time.sleep(60)
        time.sleep(4)

if __name__ == '__main__':
  eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 3000)), app)