import pandas as pd
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.16.0.60', 80, 'admin', 'P@55word')

# Get Hostname
#resp = mycam.devicemgmt.GetHostname()

#d = [[resp.Name, resp.FromDHCP, resp.Extension]]
#df = pd.DataFrame(d, columns = ['Name' , 'From DHCP' , 'Extension'])
#print(df)


#Get network protocols
net= mycam.devicemgmt.GetNetworkProtocols()
print(net)
