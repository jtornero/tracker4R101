#DEVICE.py
# This file is part of trackerR101
# https://github.com/jtornero/tracker4R101.git
# Programmed by Jorge Tornero http://imasdemase.com @imasdemase
# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <http://unlicense.org/>

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import androidhelper
import time

#Here goes your broker IP/Address and port, username, and password if appliable
broker=
broker_port=
user=
passwd=
#Just a name to identify the runner, vehicle...
mobile_id = 

# MQTT inicialzation
mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(user,passwd)
mqtt_client.connect(broker,broker_port)
#Android inicialization
droid = androidhelper.Android()
point_id=0

while True:
    droid.startLocating()
    time.sleep(120) # For walking, running, etc 5-30 seconds should be appropiate
    loc = droid.readLocation()[1]
    lat = 0
    lon = 0
    if loc != {}:
        try:
            data = loc['gps']
            source='GPS'
        except KeyError:
            data = loc['network']
            point_id += 1
            source='NETWORK'
     
        timestamp=int(time.time())
        lat = data['latitude'] 
        lon = data['longitude']

        msg = '{"tid":"%s","tst":%i,"lat":%s,"lon":%s}' %(mobile_id, timestamp, lat, lon)
    
        try:
            mqtt_client.connect(broker,broker_port)
            #The topic for the data will be TRACK but use what you want; must match the TRACKER script topic
            publish.single('YOUR TOPIC HERE',msg,qos=2,hostname=broker,port=broker_port,auth={'username':user,'password':passwd})
            print 'DATA SENT->',source,msg
            mqtt_client.disconnect()
        except Exception as e:
            print e, "Error while connecting to MQTT broker"
    else:
        print "Location not available. Check your device settings"
        
droid.stopLocating()
