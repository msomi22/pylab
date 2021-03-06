#!/usr/bin/python
from __future__ import print_function
from pyrad.client import Client
from pyrad.dictionary import Dictionary
import socket
import sys
import pyrad.packet

srv = Client(server="121.37.24.177", authport=52335, secret=b"123456", dict=Dictionary("dictionary"))

req = srv.CreateAuthPacket(code=pyrad.packet.AccessRequest, User_Name="svip1")

req["User-Password"] = req.PwCrypt("123456")
req["NAS-IP-Address"] = "192.168.1.10"
req["NAS-Port"] = 0
req["NAS-Identifier"] = "adc-wifi"

#req["Service-Type"] = "Login-User"
#req["NAS-Identifier"] = "adc-wifi"
#req["Called-Station-Id"] = "00-04-5F-00-0F-D1"
#req["Calling-Station-Id"] = "00-01-24-80-B3-9C"
#req["Framed-IP-Address"] = "10.0.0.100"

try:
    print("Sending authentication request")
    reply = srv.SendPacket(req)
except pyrad.client.Timeout:
    print("RADIUS server does not reply")
    sys.exit(1)
except socket.error as error:
    print("Network error: " + error[1])
    sys.exit(1)

if reply.code == pyrad.packet.AccessAccept:
    print("Access accepted")
else:
    print("Access denied")

print("Attributes returned by server:")
for i in reply.keys():
    print("%s: %s" % (i, reply[i]))
