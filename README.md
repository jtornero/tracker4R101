# tracker4R101
A simple tracker for Ronda's 101 km ultratrail (or whatever) based on Python, MQTT and QGIS
==============================================================================
This is a simple, yet functional proof of concept

Requisites and dependences
==========================
To be able to track, you need:

1) Account in a MQTT broker site like cloudMQTT
2) QPython installed in your mobile devie (MUST BE ANDROID), as well as paho-mqtt module
3) Python 2.7, paho-mqtt and QGIS installed in your system

Small How-to
============

First you must modify the script according to your server, port, etc. configuration
Then run the DEVICE.py script in your cell phone. I suggest you to use QPython QRCode service to get the code in:

http://qpython.com/#qrcode

On tracker side, you must run TRACKER.py script to get the data from the mqtt broker.
The script saves the received data to a file called tracking.csv. You could create a file before with a suitable
header. Now the fields are:
mobile_id;point_id;lat;lon

To show the tracked points over a map, just load the file tracking.csv
as a CSV layer in QGIS enabling file whatching, so everytime a new point is appended by TRACKER.py it is shown

TODO:
=====
A lot, and for instance
- Because all data tranmsission will be through GSM connections, and because high chances of 
  running into no coverage zones, store-and-send procedures for positions.

  



