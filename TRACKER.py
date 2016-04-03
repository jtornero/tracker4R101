# TRACKER.py
# This file is part of trackerR101
# https://github.com/jtornero/tracker4R101
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

#/usr/bin/env python


import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
  print message.payload
  ide,pid,lat,lon=message.payload.split(';')
  if (lat!='0' and lon!='0'):
    
    fichero=open('tracking.csv','a')
    fichero.write(message.payload+'\n')


mqtt_client=mqtt.Client()

#Here goes your broker IP/Address and port, username, and password if appliable
broker=
broker_port=
user=
passwd=


#The topic for the data will be TRACK but use what you want; must match the DEVICE script topic
mqtt_client.subscribe('TRACK')

mqtt_client.on_message=on_message
mqtt_client.loop_forever()
