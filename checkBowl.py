#!/usr/bin/env python
# Reading an analogue sensor with
# a single GPIO pin

# Author : Matt Hawkins
# Distribution : Raspbian
# Python : 2.7
# GPIO   : RPi.GPIO v3.1.0a

import RPi.GPIO as GPIO, time
import pycurl, json
from StringIO import StringIO


# Tell the GPIO library to use
# Broadcom GPIO references
GPIO.setmode(GPIO.BCM)

appID = ""

# add your Instapush Application Secret
appSecret = ""
pushEvent = "Empty"
pushMessage = "Cat bowl is empty"

pushEvent2 = "Full"
pushMessage2 = "Cat bowl is full"
# use this to capture the response from our push API call
buffer = StringIO()




# Define function to measure charge time
def RCtime (PiPin):
  measurement = 0
  # Discharge capacitor
  GPIO.setup(PiPin, GPIO.OUT)
  GPIO.output(PiPin, GPIO.LOW)
  time.sleep(0.1)

  GPIO.setup(PiPin, GPIO.IN)
  # Count loops until voltage across
  # capacitor reads high on GPIO
  while (GPIO.input(PiPin) == GPIO.LOW):
    measurement += 1

  return measurement

# Main program loop
#Edit pin
if RCtime(18) < 1000:
   print "1000"
   c = pycurl.Curl()

   # set API URL
   c.setopt(c.URL, 'https://api.instapush.im/v1/post')

   #setup custom headers for authentication variables and content type
   c.setopt(c.HTTPHEADER, ['x-instapush-appid: ' + appID,
			'x-instapush-appsecret: ' + appSecret,
			'Content-Type: application/json'])


   # create a dict structure for the JSON data to post
   json_fields = {}

   # setup JSON values
   json_fields['event']=pushEvent
   json_fields['trackers'] = {}
   json_fields['trackers']['message']=pushMessage
   #print(json_fields)
   postfields = json.dumps(json_fields)

   # make sure to send the JSON with post
   c.setopt(c.POSTFIELDS, postfields)

   # set this so we can capture the resposne in our buffer
   c.setopt(c.WRITEFUNCTION, buffer.write)

   # uncomment to see the post sent
   #c.setopt(c.VERBOSE, True)

   c.perform()

   body= buffer.getvalue()


   print(body)

   # reset the buffer
   buffer.truncate(0)
   buffer.seek(0)
   c.close()
   GPIO.cleanup()

else:
   c = pycurl.Curl()

   # set API URL
   c.setopt(c.URL, 'https://api.instapush.im/v1/post')

   #setup custom headers for authentication variables and content type
   c.setopt(c.HTTPHEADER, ['x-instapush-appid: ' + appID,
			'x-instapush-appsecret: ' + appSecret,
			'Content-Type: application/json'])


   # create a dict structure for the JSON data to post
   json_fields = {}

   # setup JSON values
   json_fields['event']=pushEvent2
   json_fields['trackers'] = {}
   json_fields['trackers']['message']=pushMessage2
   #print(json_fields)
   postfields = json.dumps(json_fields)

   # make sure to send the JSON with post
   c.setopt(c.POSTFIELDS, postfields)

   # set this so we can capture the resposne in our buffer
   c.setopt(c.WRITEFUNCTION, buffer.write)

   # uncomment to see the post sent
   #c.setopt(c.VERBOSE, True)

   c.perform()

   body= buffer.getvalue()


   print(body)

   # reset the buffer
   buffer.truncate(0)
   buffer.seek(0)
   c.close()
   GPIO.cleanup()

