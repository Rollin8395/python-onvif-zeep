from onvif import ONVIFCamera
mycam = ONVIFCamera('172.16.0.60', 80, 'admin', 'P@55word')

event_service=mycam.create_events_service()
print(event_service.GetEventProperties())
