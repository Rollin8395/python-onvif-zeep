
from onvif import ONVIFCamera
mycam = ONVIFCamera('172.16.0.60', 80, 'admin', 'P@55word')

# Get Hostname
resp = mycam.devicemgmt.GetHostname()
print(resp)

#Get system date and time
dt = mycam.devicemgmt.GetSystemDateAndTime()
tz = dt.TimeZone
year = dt.UTCDateTime.Date.Year
hour = dt.UTCDateTime.Time.Hour
print(dt,tz,hour,year)

#Get Device info
info = mycam.devicemgmt.GetDeviceInformation()
print(info)

#Get device capability
capa= mycam.devicemgmt.GetCapabilities()
print(capa)

#Get network protocols
net= mycam.devicemgmt.GetNetworkProtocols()
print(net)
