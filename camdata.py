from __future__ import unicode_literals
import json
jsonFile = open("data.json", 'r')
jsonData = json.load(jsonFile)

for k, v in jsonData['CameraApp'].iteritems():
    #print(k, v.keys())

    try:
        print("{0:15} , {1:15},{2:15}, {3:15}, {4:15} , {5:15} , {6:15}".format(k, v['Model'], v['Country'], v['ScreenSize'], v['DeviceType'],v.get("LastUsed", "None"),v.get("AppVersion", "None")))

    except Exception as err:
        pass
        #print(err)

print("***********************************************************")
print("Total device: {} ".format(len(jsonData['CameraApp'].keys())))
print("***********************************************************")
