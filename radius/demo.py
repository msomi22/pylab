from __future__ import print_function
from pyrad.client import Client
from pyrad.dictionary import Dictionary
import pyrad.packet

srv = Client(server="121.37.24.177", authport=52335, secret=b"123456",
             dict=None)
#Dictionary("dictionary")

# create request
req = srv.CreateAuthPacket(code=pyrad.packet.AccessRequest, User_Name="svip1", NAS_Identifier="localhost") 

req["User-Password"] = req.PwCrypt("123456")

# send request
reply = srv.SendPacket(req)

if reply.code == pyrad.packet.AccessAccept:
    print("access accepted")
else:
    print("access denied")

print("Attributes returned by server:")
for i in reply.keys():
    print("%s: %s" % (i, reply[i]))